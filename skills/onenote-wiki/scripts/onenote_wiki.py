# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "msal",
#     "markdownify",
#     "beautifulsoup4",
#     "orjson",
#     "python-dotenv",
# ]
# ///
"""
OneNote Wiki Fetcher — Fetch SharePoint OneNote pages via Graph API,
cache locally with modification-time invalidation, and convert to Markdown.

Usage:
    # As a library
    from onenote_wiki import OneNoteClient
    client = OneNoteClient()
    sites = client.list_sites("DevSecOps")
    client.sync_site(sites[0]["id"], output_dir="./wiki")

    # As a CLI
    uv run onenote_wiki.py sync --site-search "DevSecOps" --output ./wiki
    uv run onenote_wiki.py sync-section --site-id <id> --section-id <id> --output ./wiki
    uv run onenote_wiki.py list-sites "DevSecOps"
    uv run onenote_wiki.py list-sections --site-id <id> --notebook-id <id>
    uv run onenote_wiki.py list-pages --site-id <id>
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import time
from functools import cache
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import httpx
import orjson
from dotenv import dotenv_values
from markdownify import markdownify
from msal import PublicClientApplication

# =============================================================================
# Configuration
# =============================================================================

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
SCOPES = ["Notes.Read.All", "Sites.Read.All"]
CACHE_DIR = Path.home() / ".cache" / "onenote-wiki"
DEFAULT_ENV_PATH = Path(__file__).resolve().parents[1] / ".env"


# =============================================================================
# Authentication (reuses pattern from IACB/utils.py)
# =============================================================================


def _update_env_refresh_token(env_path: Path, new_token: str) -> None:
    """Persist new refresh token back to .env file."""
    if not env_path.exists():
        return
    lines = env_path.read_text().splitlines(keepends=True)
    found = False
    with env_path.open("w") as f:
        for line in lines:
            if line.startswith("MICROSOFT_REFRESH_TOKEN="):
                f.write(f"MICROSOFT_REFRESH_TOKEN={new_token}\n")
                found = True
            else:
                f.write(line)
        if not found:
            f.write(f"MICROSOFT_REFRESH_TOKEN={new_token}\n")


@cache
def _get_msal_app(client_id: str, authority: str) -> PublicClientApplication:
    return PublicClientApplication(client_id, authority=authority)


def _get_access_token(env_path: Path) -> str:
    """Acquire access token via MSAL with refresh token rotation."""
    config = dotenv_values(env_path)
    client_id = config.get("MICROSOFT_CLIENT_ID", "")
    authority = config.get("MICROSOFT_AUTHORITY", "")
    if not client_id or not authority:
        raise ValueError(
            f"Missing MICROSOFT_CLIENT_ID or MICROSOFT_AUTHORITY in {env_path}"
        )

    app = _get_msal_app(client_id, authority)

    # Try refresh token first
    refresh_token = config.get("MICROSOFT_REFRESH_TOKEN")
    if refresh_token:
        result = app.acquire_token_by_refresh_token(refresh_token, scopes=SCOPES)
        if "access_token" in result:
            if "refresh_token" in result:
                _update_env_refresh_token(env_path, result["refresh_token"])
            return result["access_token"]

    # Fallback to interactive login
    result = app.acquire_token_interactive(scopes=SCOPES)
    if "access_token" not in result:
        raise ValueError(f"Authentication failed: {result.get('error_description')}")
    if "refresh_token" in result:
        _update_env_refresh_token(env_path, result["refresh_token"])
    return result["access_token"]


# =============================================================================
# Graph API Helpers
# =============================================================================


def _graph_get(
    path: str, headers: dict[str, str], *, params: dict | None = None
) -> dict[str, Any]:
    """GET request to Graph API, return JSON."""
    url = f"{GRAPH_BASE}{path}" if path.startswith("/") else path
    resp = httpx.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def _graph_get_all(path: str, headers: dict[str, str]) -> list[dict[str, Any]]:
    """GET with automatic pagination via @odata.nextLink."""
    results: list[dict[str, Any]] = []
    url: str | None = f"{GRAPH_BASE}{path}" if path.startswith("/") else path
    while url:
        resp = httpx.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        results.extend(data.get("value", []))
        url = data.get("@odata.nextLink")
    return results


def _graph_get_content(path: str, headers: dict[str, str]) -> str:
    """GET page content (returns HTML text, not JSON)."""
    url = f"{GRAPH_BASE}{path}"
    resp = httpx.get(url, headers=headers, timeout=60)
    resp.raise_for_status()
    return resp.text


# =============================================================================
# HTML → Markdown Conversion (single BS4 pass)
# =============================================================================


def _sanitize_filename(name: str) -> str:
    """Sanitize string for use as filename."""
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:200] if name else "untitled"


def _preprocess_onenote_html(html: str) -> str:
    """Single-pass BS4 preprocessing for all OneNote HTML quirks.

    1. Promote first table row to <thead>/<th>
    2. Flatten <ul>/<ol> inside table cells to "; "-joined text
    3. Convert onenote:# internal links to relative .md links
    """
    from bs4 import BeautifulSoup, NavigableString

    soup = BeautifulSoup(html, "html.parser")

    # 1. Promote first table row to <thead>/<th>
    for table in soup.find_all("table"):
        if table.find("thead") or table.find("th"):
            continue
        first_tr = table.find("tr")
        if not first_tr:
            continue
        for td in first_tr.find_all("td"):
            td.name = "th"
        thead = soup.new_tag("thead")
        first_tr.wrap(thead)
        remaining_trs = table.find_all("tr")
        if remaining_trs:
            tbody = soup.new_tag("tbody")
            for tr in remaining_trs:
                tbody.append(tr.extract())
            table.append(tbody)

    # 2. Flatten <ul>/<ol> inside table cells to "; "-joined plain text
    for cell in soup.find_all(["td", "th"]):
        for ul in cell.find_all(["ul", "ol"]):
            items = [li.get_text(strip=True) for li in ul.find_all("li")]
            ul.replace_with(NavigableString("; ".join(items)))

    # 3. Convert onenote:# internal links to relative .md links
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith("onenote:"):
            continue
        match = re.match(r"onenote:#(.+?)&", href)
        if match:
            title = unquote(match.group(1))
            a["href"] = f"{_sanitize_filename(title)}.md"

    return str(soup)


def html_to_markdown(html: str) -> str:
    """Convert OneNote HTML to Markdown.

    Handles OneNote-specific quirks in a single BS4 pass:
    - Promotes first table row to <thead>/<th>
    - Flattens lists inside table cells to "; "-joined text
    - Converts onenote:# links to relative .md links
    - Converts data-tag="to-do" to markdown checkboxes
    """
    # Pre-process: convert OneNote todo tags to checkbox syntax
    html = re.sub(
        r'<p[^>]*data-tag="to-do"[^>]*>(.*?)</p>',
        r"<li>[ ] \1</li>",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'<p[^>]*data-tag="to-do:completed"[^>]*>(.*?)</p>',
        r"<li>[x] \1</li>",
        html,
        flags=re.DOTALL,
    )

    # Single BS4 pass for table headers, cell lists, internal links
    html = _preprocess_onenote_html(html)

    md = markdownify(html, heading_style="ATX", strip=["style", "script"])

    # Clean up excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


# =============================================================================
# Cache Management (HTML + meta only, no .md duplication)
# =============================================================================


def _cache_dir_for_site(site_id: str) -> Path:
    site_hash = hashlib.md5(site_id.encode()).hexdigest()[:12]
    return CACHE_DIR / site_hash


def _read_meta(meta_path: Path) -> dict[str, Any]:
    if meta_path.exists():
        return orjson.loads(meta_path.read_bytes())
    return {}


def _write_meta(meta_path: Path, meta: dict[str, Any]) -> None:
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_bytes(orjson.dumps(meta, option=orjson.OPT_INDENT_2))


# =============================================================================
# OneNote Client
# =============================================================================


class OneNoteClient:
    """Client for fetching OneNote content from SharePoint via Graph API."""

    def __init__(self, env_path: str | Path | None = None):
        self._env_path = Path(env_path) if env_path else DEFAULT_ENV_PATH
        self._headers: dict[str, str] | None = None

    @property
    def headers(self) -> dict[str, str]:
        if self._headers is None:
            token = _get_access_token(self._env_path)
            self._headers = {"Authorization": f"Bearer {token}"}
        return self._headers

    def _refresh_token(self) -> None:
        """Force token refresh."""
        self._headers = None

    # ---- Discovery ----

    def list_sites(self, search: str) -> list[dict[str, Any]]:
        """Search SharePoint sites by keyword."""
        return _graph_get_all(f"/sites?search={search}", self.headers)

    # ---- Notebooks & Structure ----

    def list_notebooks(self, site_id: str) -> list[dict[str, Any]]:
        """List all notebooks on a SharePoint site."""
        return _graph_get_all(
            f"/sites/{site_id}/onenote/notebooks", self.headers
        )

    def list_section_groups(
        self, site_id: str, notebook_id: str
    ) -> list[dict[str, Any]]:
        """List section groups in a notebook."""
        return _graph_get_all(
            f"/sites/{site_id}/onenote/notebooks/{notebook_id}/sectionGroups",
            self.headers,
        )

    def list_sections(
        self, site_id: str, notebook_id: str
    ) -> list[dict[str, Any]]:
        """List sections in a notebook."""
        return _graph_get_all(
            f"/sites/{site_id}/onenote/notebooks/{notebook_id}/sections",
            self.headers,
        )

    def list_pages(
        self,
        site_id: str,
        *,
        section_id: str | None = None,
    ) -> list[dict[str, Any]]:
        """List pages. If section_id given, list pages in that section only."""
        if section_id:
            path = f"/sites/{site_id}/onenote/sections/{section_id}/pages"
        else:
            path = f"/sites/{site_id}/onenote/pages"
        return _graph_get_all(path, self.headers)

    # ---- Content Fetching ----

    def fetch_page_html(self, site_id: str, page_id: str) -> str:
        """Fetch raw HTML content of a page."""
        return _graph_get_content(
            f"/sites/{site_id}/onenote/pages/{page_id}/content", self.headers
        )

    def fetch_page_markdown(
        self,
        site_id: str,
        page_id: str,
        *,
        use_cache: bool = True,
    ) -> str:
        """Fetch page content and return as Markdown.

        Caches raw HTML + meta locally. Converts to Markdown on-the-fly.
        Cache invalidation based on lastModifiedDateTime.
        """
        cache_dir = _cache_dir_for_site(site_id)
        html_path = cache_dir / f"{page_id}.html"
        meta_path = cache_dir / f"{page_id}.meta.json"

        if use_cache and html_path.exists():
            meta = _read_meta(meta_path)
            if meta.get("lastModifiedDateTime"):
                page_info = _graph_get(
                    f"/sites/{site_id}/onenote/pages/{page_id}",
                    self.headers,
                )
                if (
                    page_info.get("lastModifiedDateTime")
                    == meta["lastModifiedDateTime"]
                ):
                    return html_to_markdown(
                        html_path.read_text(encoding="utf-8")
                    )

        # Fetch fresh content
        html = self.fetch_page_html(site_id, page_id)

        # Cache HTML + meta
        page_info = _graph_get(
            f"/sites/{site_id}/onenote/pages/{page_id}", self.headers
        )
        cache_dir.mkdir(parents=True, exist_ok=True)
        html_path.write_text(html, encoding="utf-8")
        _write_meta(
            meta_path,
            {
                "page_id": page_id,
                "title": page_info.get("title", ""),
                "lastModifiedDateTime": page_info.get("lastModifiedDateTime"),
                "cached_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
        )

        return html_to_markdown(html)

    # ---- Bulk Sync ----

    def _sync_pages(
        self,
        site_id: str,
        pages: list[dict[str, Any]],
        output_dir: Path,
        *,
        verbose: bool = True,
    ) -> list[Path]:
        """Shared helper: sync a list of pages to output_dir."""
        written: list[Path] = []
        total = len(pages)
        for i, page in enumerate(pages, 1):
            title = page.get("title", page["id"][:12])
            filename = _sanitize_filename(title) + ".md"
            if verbose:
                print(f"  [{i}/{total}] {title}")
            try:
                md = self.fetch_page_markdown(site_id, page["id"])
                file_path = output_dir / filename
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(
                    f"# {title}\n\n{md}", encoding="utf-8"
                )
                written.append(file_path)
            except Exception as e:
                if verbose:
                    print(f"    ⚠️  Error: {e}")
        return written

    def sync_section(
        self,
        site_id: str,
        section_id: str,
        output_dir: str | Path = "./wiki_cache",
        *,
        verbose: bool = True,
    ) -> list[Path]:
        """Sync all pages from a section to local Markdown files."""
        output = Path(output_dir)
        pages = self.list_pages(site_id, section_id=section_id)
        if verbose:
            print(f"📑 {len(pages)} pages in section")
        written = self._sync_pages(site_id, pages, output, verbose=verbose)
        if verbose:
            print(f"\n✅ Synced {len(written)} pages to {output}")
        return written

    def sync_notebook(
        self,
        site_id: str,
        notebook_id: str,
        output_dir: str | Path = "./wiki_cache",
        *,
        verbose: bool = True,
    ) -> list[Path]:
        """Sync a specific notebook to local Markdown files.

        Structure: {output_dir}/{section}/{page_title}.md
        """
        output = Path(output_dir)
        written: list[Path] = []

        nb_info = _graph_get(
            f"/sites/{site_id}/onenote/notebooks/{notebook_id}", self.headers
        )
        nb_name = _sanitize_filename(nb_info.get("displayName", "notebook"))
        if verbose:
            print(f"📓 Notebook: {nb_name}")

        sections = self.list_sections(site_id, notebook_id)
        for sec in sections:
            sec_name = _sanitize_filename(sec.get("displayName", "section"))
            if verbose:
                print(f"📑 Section: {sec_name}")
            pages = self.list_pages(site_id, section_id=sec["id"])
            sec_written = self._sync_pages(
                site_id, pages, output / nb_name / sec_name, verbose=verbose
            )
            written.extend(sec_written)

        if verbose:
            print(f"\n✅ Synced {len(written)} pages to {output}")
        return written

    def sync_site(
        self,
        site_id: str,
        output_dir: str | Path = "./wiki_cache",
        *,
        verbose: bool = True,
    ) -> list[Path]:
        """Sync all pages from a site to local Markdown files.

        Structure: {output_dir}/{notebook}/{section}/{page_title}.md
        """
        output = Path(output_dir)
        written: list[Path] = []

        notebooks = self.list_notebooks(site_id)
        for nb in notebooks:
            nb_written = self.sync_notebook(
                site_id, nb["id"], output_dir=output, verbose=verbose
            )
            written.extend(nb_written)

        if verbose:
            print(f"\n✅ Total: {len(written)} pages synced to {output}")
        return written


# =============================================================================
# CLI
# =============================================================================


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch OneNote wiki pages from SharePoint via Graph API"
    )
    parser.add_argument(
        "--env", default=None, help="Path to .env file (default: skill dir .env)"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # list-sites
    p_sites = sub.add_parser("list-sites", help="Search SharePoint sites")
    p_sites.add_argument("search", help="Search keyword")

    # list-notebooks
    p_nb = sub.add_parser("list-notebooks", help="List notebooks on a site")
    p_nb.add_argument("--site-id", required=True)

    # list-sections
    p_sec = sub.add_parser("list-sections", help="List sections in a notebook")
    p_sec.add_argument("--site-id", required=True)
    p_sec.add_argument("--notebook-id", required=True)

    # list-pages
    p_pages = sub.add_parser("list-pages", help="List pages")
    p_pages.add_argument("--site-id", required=True)
    p_pages.add_argument("--section-id", default=None)

    # fetch
    p_fetch = sub.add_parser("fetch", help="Fetch a single page as Markdown")
    p_fetch.add_argument("--site-id", required=True)
    p_fetch.add_argument("--page-id", required=True)

    # sync
    p_sync = sub.add_parser("sync", help="Sync site/notebook to local Markdown")
    p_sync.add_argument("--site-search", required=True)
    p_sync.add_argument("--output", default="./wiki_cache")
    p_sync.add_argument("--notebook-id", default=None)

    # sync-section
    p_ss = sub.add_parser("sync-section", help="Sync a section to local Markdown")
    p_ss.add_argument("--site-id", required=True)
    p_ss.add_argument("--section-id", required=True)
    p_ss.add_argument("--output", default="./wiki_cache")

    args = parser.parse_args()
    client = OneNoteClient(env_path=args.env)

    if args.command == "list-sites":
        sites = client.list_sites(args.search)
        for s in sites:
            print(f"  {s['displayName']:<30} {s['id']}")

    elif args.command == "list-notebooks":
        notebooks = client.list_notebooks(args.site_id)
        for nb in notebooks:
            print(f"  {nb.get('displayName', '?'):<30} {nb['id']}")

    elif args.command == "list-sections":
        sections = client.list_sections(args.site_id, args.notebook_id)
        for sec in sections:
            print(f"  {sec.get('displayName', '?'):<30} {sec['id']}")

    elif args.command == "list-pages":
        pages = client.list_pages(args.site_id, section_id=args.section_id)
        for p in pages:
            print(f"  {p.get('title', '?'):<40} {p['id']}")

    elif args.command == "fetch":
        md = client.fetch_page_markdown(args.site_id, args.page_id)
        print(md)

    elif args.command == "sync":
        sites = client.list_sites(args.site_search)
        if not sites:
            print(f"No sites found for '{args.site_search}'", file=sys.stderr)
            sys.exit(1)
        site_id = sites[0]["id"]
        print(f"Using site: {sites[0]['displayName']} ({site_id})")
        if args.notebook_id:
            client.sync_notebook(site_id, args.notebook_id, args.output)
        else:
            client.sync_site(site_id, args.output)

    elif args.command == "sync-section":
        client.sync_section(args.site_id, args.section_id, args.output)


if __name__ == "__main__":
    main()

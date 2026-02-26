---
name: onenote-wiki
description: >
  Fetch OneNote wiki pages from SharePoint sites via Microsoft Graph API,
  cache locally with modification-time invalidation, and convert HTML to Markdown.
  This skill should be used when asked to "fetch onenote", "read wiki",
  "download onenote pages", "sync onenote", "拉取 onenote", "同步 wiki",
  "读取笔记本".
---

# OneNote Wiki Fetcher

Fetch OneNote notebook pages from SharePoint via Microsoft Graph API,
convert HTML content to Markdown, and cache locally for offline use.

## Prerequisites

### .env Configuration

The skill includes a `.env` file with Microsoft credentials at the skill root.
Required variables:

| Variable                  | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| `MICROSOFT_CLIENT_ID`     | Azure AD app registration client ID                             |
| `MICROSOFT_AUTHORITY`     | `https://login.microsoftonline.com/<tenant-id>`                 |
| `MICROSOFT_REFRESH_TOKEN` | Leave empty for first run; auto-updated after interactive login |

See `.env.example` for the template.

### Dependencies

Managed via PEP 723 inline metadata in `scripts/onenote_wiki.py`.
Run with `uv run scripts/onenote_wiki.py` — dependencies install automatically.

## Workflow

### Step 1: Discover the SharePoint Site

```bash
uv run scripts/onenote_wiki.py list-sites "DevSecOps"
```

### Step 2: Browse Structure

```bash
# List notebooks on a site
uv run scripts/onenote_wiki.py list-notebooks --site-id <id>

# List sections in a notebook
uv run scripts/onenote_wiki.py list-sections --site-id <id> --notebook-id <id>

# List pages (site-wide or by section)
uv run scripts/onenote_wiki.py list-pages --site-id <id> [--section-id <id>]
```

### Step 3: Fetch or Sync Content

Fetch a single page as Markdown:

```bash
uv run scripts/onenote_wiki.py fetch --site-id <id> --page-id <id>
```

Sync an entire site to local Markdown files:

```bash
uv run scripts/onenote_wiki.py sync --site-search "DevSecOps" --output ./wiki
```

Sync a specific section:

```bash
uv run scripts/onenote_wiki.py sync-section --site-id <id> --section-id <id> --output ./wiki
```

Output structure: `{output}/{notebook}/{section}/{page_title}.md`

### Library Usage

For programmatic access within Python:

```python
from onenote_wiki import OneNoteClient

client = OneNoteClient(env_path="<skill-dir>/.env")
sites = client.list_sites("DevSecOps")
site_id = sites[0]["id"]

# Sync all pages
client.sync_site(site_id, output_dir="./wiki")

# Or fetch a single page
md = client.fetch_page_markdown(site_id, page_id)
```

## Caching

HTML and metadata are cached at `~/.cache/onenote-wiki/{site_hash}/`.
Cache invalidation uses `lastModifiedDateTime` — only re-fetches modified pages.

## Resources

- `scripts/onenote_wiki.py` — Main script (CLI + library). Handles auth, API calls,
  HTML→Markdown conversion, caching, and bulk sync.
- `references/graph_api.md` — OneNote Graph API endpoint reference, pagination,
  HTML quirks, authentication details, and error handling.
- `.env` / `.env.example` — Microsoft Graph API credentials.

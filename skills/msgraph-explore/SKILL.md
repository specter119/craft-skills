---
name: msgraph-explore
description: >
  Unified Microsoft Graph skill for SharePoint, OneDrive, and OneNote.
  Supports content search via Graph Search API, SharePoint file fetch,
  drive folder sync, site discovery, notebook discovery, and OneNote
  sync to Markdown.
---

# Microsoft Graph Explore

统一承接 Microsoft Graph 相关取数和搜索能力，覆盖：

- **Content search** via Graph Search API (SharePoint, OneDrive)
- SharePoint file fetch
- OneDrive / SharePoint drive folder sync
- SharePoint site discovery
- OneNote notebook / section discovery
- OneNote sync to Markdown

当用户需要"搜索 SharePoint 内容"、"搜索内部 wiki"、"拉 SharePoint 文件"、"同步 OneDrive 目录"、"列出 site/notebook/section"、"同步 OneNote wiki"时使用这个 skill。

## Architecture

```text
scripts/
  msgraph_auth.py    # Shared module: GraphClient, MSAL auth, constants
  msgraph_search.py  # PEP 723 script: Graph Search API search
  msgraph_fetch.py   # PEP 723 script: OneNote + Drive fetch/sync
```

## Prerequisites

### `.env`

将 `.env.example` 复制到你的项目目录或 skill 目录：

```bash
cp skills/msgraph-explore/.env.example /path/to/project/.env
```

需要的环境变量：

| Variable | Description |
| --- | --- |
| `MICROSOFT_CLIENT_ID` | Azure AD app registration client ID |
| `MICROSOFT_AUTHORITY` | `https://login.microsoftonline.com/<tenant-id>` |
| `MICROSOFT_REFRESH_TOKEN` | 首次可留空，登录后会自动回写 |

### Permissions

建议同一个 delegated app registration 一次性配置：

- `Sites.Read.All`
- `Notes.Read.All`
- `Files.Read.All`

脚本会按命令申请最小 scope：

- Search 命令：`Sites.Read.All` + `Files.Read.All`
- OneNote 命令：`Sites.Read.All` + `Notes.Read.All`
- Drive 命令：`Sites.Read.All` + `Files.Read.All`

## CLI

### Search Content (NEW)

搜索 SharePoint 和 OneDrive 中的内容：

```bash
uv run skills/msgraph-explore/scripts/msgraph_search.py "Fin skill design"
```

可选参数：

```bash
uv run skills/msgraph-explore/scripts/msgraph_search.py "Fin skill design" \
  --entity-types driveItem,listItem \
  --site-path "sites/IACB" \
  --max-results 10
```

输出 JSON（含完整 resource 对象，便于 chaining）：

```bash
uv run skills/msgraph-explore/scripts/msgraph_search.py "Fin skill design" --json
```

参数说明：

- `query`：搜索关键词，支持 KQL 语法
- `--entity-types`：搜索实体类型（默认 `driveItem,listItem`，可选 `site`）
- `--site-path`：KQL path scope（如 `"sites/IACB"`）
- `--max-results`：最大结果数（默认 25）
- `--json`：输出包含 raw identifiers 的 JSON

**注意**：OneNote 页面的搜索覆盖取决于 Graph Search 索引状态，为 best-effort / discovery-only。如需完整 OneNote 内容搜索，建议先 `fetch-onenote` 同步到本地再用 grep。

### Fetch SharePoint File

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-file \
  --url "<sharepoint-url>"
```

可选：

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-file \
  --url "<sharepoint-url>" \
  --output-dir "./downloads"
```

不传 `--output-dir` 时，默认写到：

```plain
~/.cache/msgraph-explore/materialized/files/
```

成功时 `stdout` 最后一行只输出最终本地绝对路径。

### Sync Drive Folder

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py sync-folder \
  --remote-path "ByProject/IACB/smart-invoice" \
  --output-dir "./data/smart-invoice"
```

可选定位参数：

- 默认 `me/drive`
- `--site-id`
- `--site-search`
- `--force`

### Discover Sites / Notebooks / Sections

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-sites "DevSecOps"
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-notebooks --site-id "<site-id>"
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-sections \
  --site-id "<site-id>" \
  --notebook-id "<notebook-id>"
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-pages \
  --site-id "<site-id>"
```

可选：

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-pages \
  --site-id "<site-id>" \
  --section-id "<section-id>"
```

### Fetch Single OneNote Page

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-onenote-page \
  --site-id "<site-id>" \
  --page-id "<page-id>"
```

命令会输出该页面的 Markdown 内容到 `stdout`。

### Fetch OneNote

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-onenote \
  --site-id "<site-id>" \
  --output-dir "./wiki_cache"
```

可选参数：

- `--site-search`
- `--notebook-id`
- `--section-id`

语义：

- 不带额外参数时，抓取整个 site 下的 OneNote 内容
- 带 `--notebook-id` 时，抓取单个 notebook
- 带 `--section-id` 时，抓取单个 section
- 单页抓取不走这个命令，使用上面的 `fetch-onenote-page --page-id`

说明：

- `fetch-onenote` 是从 Graph 单向抓取到本地 Markdown

### CLI Entry Point

统一使用 `scripts/msgraph_fetch.py` 作为取数入口：

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-file --url "..."
```

## Cache Layout

统一使用：

```plain
~/.cache/msgraph-explore/
```

缓存按资源分层：

```plain
sources/
  drive/
  onenote/
derived/
  onenote/
meta/
  drive/
  onenote/
```

说明：

- `sources` 存远端原始内容
- `derived/onenote` 存 Markdown 派生结果
- `meta` 存 eTag、`lastModifiedDateTime`、缓存时间等元数据

OneNote 不只缓存 Markdown，也保留原始 HTML，便于后续重新渲染。

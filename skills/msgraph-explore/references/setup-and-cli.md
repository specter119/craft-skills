# Setup 与 CLI

## 环境准备

```bash
cp skills/msgraph-explore/.env.example /path/to/project/.env
```

需要的环境变量：

| Variable | Description |
| --- | --- |
| `MICROSOFT_CLIENT_ID` | Azure AD app registration client ID |
| `MICROSOFT_AUTHORITY` | `https://login.microsoftonline.com/<tenant-id>` |
| `MICROSOFT_REFRESH_TOKEN` | 首次可为空，登录后可自动回写 |

## 权限

建议一次性配置：

- `Sites.Read.All`
- `Notes.Read.All`
- `Files.Read.All`

脚本会按命令申请最小 scope：

- OneNote: `Sites.Read.All` + `Notes.Read.All`
- Drive: `Sites.Read.All` + `Files.Read.All`

## 常用命令

### Search Content

```bash
uv run skills/msgraph-explore/scripts/msgraph_search.py "Fin skill design"
```

可选：

```bash
uv run skills/msgraph-explore/scripts/msgraph_search.py "Fin skill design" \
  --entity-types driveItem,listItem \
  --site-path "sites/IACB" \
  --max-results 10 \
  --json
```

### Fetch SharePoint File

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-file \
  --url "<sharepoint-url>"
```

### Sync Drive Folder

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py sync-folder \
  --remote-path "ByProject/IACB/smart-invoice" \
  --output-dir "./data/smart-invoice"
```

### Discover Sites / Notebooks / Sections

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-sites "DevSecOps"
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-notebooks --site-id "<site-id>"
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-sections \
  --site-id "<site-id>" \
  --notebook-id "<notebook-id>"
uv run skills/msgraph-explore/scripts/msgraph_fetch.py list-pages --site-id "<site-id>"
```

### Fetch Single OneNote Page

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-onenote-page \
  --site-id "<site-id>" \
  --page-id "<page-id>"
```

### Fetch OneNote

```bash
uv run skills/msgraph-explore/scripts/msgraph_fetch.py fetch-onenote \
  --site-id "<site-id>" \
  --output-dir "./wiki_cache"
```

## 缓存布局

```plain
~/.cache/msgraph-fetch/
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
- `meta` 存 eTag、缓存时间等元数据

# OneNote Graph API Reference

## Key Endpoints

| Action                  | Method | URL                                                          |
| ----------------------- | ------ | ------------------------------------------------------------ |
| Search sites            | GET    | `/v1.0/sites?search={keyword}`                               |
| List notebooks          | GET    | `/v1.0/sites/{site-id}/onenote/notebooks`                    |
| List section groups     | GET    | `/v1.0/sites/{site-id}/onenote/notebooks/{id}/sectionGroups` |
| List sections           | GET    | `/v1.0/sites/{site-id}/onenote/notebooks/{id}/sections`      |
| List pages (site-wide)  | GET    | `/v1.0/sites/{site-id}/onenote/pages`                        |
| List pages (by section) | GET    | `/v1.0/sites/{site-id}/onenote/sections/{id}/pages`          |
| Get page content        | GET    | `/v1.0/sites/{site-id}/onenote/pages/{id}/content`           |
| Personal notebooks      | GET    | `/v1.0/me/onenote/notebooks`                                 |
| Personal pages          | GET    | `/v1.0/me/onenote/pages`                                     |

## Hierarchy

```plain
SharePoint Site
  └── OneNote Notebooks
        └── Section Groups (optional nesting)
              └── Sections
                    └── Pages (HTML content)
```

## Pagination

OneNote API uses `@odata.nextLink` for pagination. Default page size is 20.
Always follow `@odata.nextLink` to get all results.

## Page Content (HTML)

The `/content` endpoint returns HTML (not JSON):

- Content-Type: `text/html`
- Contains OneNote-specific HTML elements (`data-id`, `data-tag` attributes)
- Embedded images use `src` pointing to Graph API resource URLs
- Tables, lists, headings are standard HTML

## HTML → Markdown Quirks

- `<br>` tags within paragraphs (preserve as line breaks)
- `<table>` with merged cells (simplify to flat tables)
- `<img>` src pointing to Graph API (optionally download and embed)
- `data-tag="to-do"` for checkboxes (convert to `- [ ]` / `- [x]`)

## Authentication

OneNote Graph API dropped app-only auth support (March 2025).
Must use delegated (user) auth via `PublicClientApplication`.

Required delegated permissions:

- `Notes.Read.All` — read all OneNote notebooks the user can access
- `Sites.Read.All` — resolve SharePoint site IDs

## Error Handling

| Error                 | Cause                   | Resolution                                                                       |
| --------------------- | ----------------------- | -------------------------------------------------------------------------------- |
| 401 Unauthorized      | Token expired           | Auto-refresh via MSAL; if refresh token also expired, triggers interactive login |
| 404 Not Found         | Wrong site/page ID      | Verify IDs via list endpoints                                                    |
| 429 Too Many Requests | Rate limiting           | Respect `Retry-After` header, add delays between batch requests                  |
| Scope consent needed  | Missing API permissions | Re-run interactive auth to consent to `Notes.Read.All`                           |

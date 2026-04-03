---
name: msgraph-fetch
description: >
  Fetch files and notes from Microsoft Graph across SharePoint, OneDrive, and OneNote.
  Use when the task is to fetch a SharePoint file, sync a drive folder, discover sites/notebooks,
  or export OneNote content to Markdown.
---

# Microsoft Graph Fetch

统一承接 Microsoft Graph 取数任务，但入口只负责回答：

- 什么时候该用这个 skill
- 当前任务属于哪一类取数
- 应该调用哪条 CLI

## 适用边界

### 应该路由到这里

- 拉取单个 SharePoint 文件
- 同步 OneDrive / SharePoint drive 目录
- 发现 site / notebook / section / page
- 从 OneNote 导出 Markdown

### 不应该路由到这里

- 纯文档整理或总结
- 不依赖 Microsoft Graph 的本地文件处理
- 图形界面操作或浏览器自动化

## 执行骨架

1. 先识别任务类型：单文件、整目录、site/notebook 发现、单页导出、整本导出。
2. 再按 `references/setup-and-cli.md` 检查 `.env`、权限和目标命令。
3. 默认直接调用 `scripts/msgraph_fetch.py`，不要在入口重复解释全部参数。
4. 输出本地路径或 Markdown 内容，并说明用了哪种定位方式（URL、site-id、page-id 等）。

## 参考地图

- `references/setup-and-cli.md`: 环境变量、权限、命令示例、缓存布局
- `evals/trigger-cases.md`: 最小路由样例
- `reports/optimization-notes.md`: 本轮重构判断

## 输出契约

- 文件抓取：返回最终本地绝对路径
- 列表发现：返回站点 / notebook / section / page 的可继续使用标识
- OneNote 导出：返回 Markdown 或输出目录说明

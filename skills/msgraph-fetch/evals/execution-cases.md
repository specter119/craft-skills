# Execution Cases

## 场景 1：下载单个 SharePoint 文件

- 输入：可访问的 SharePoint URL
- 预期：调用正确命令并返回最终本地绝对路径

## 场景 2：同步目录

- 输入：remote path + output dir
- 预期：完成目录同步，并明确定位方式与输出位置

## 场景 3：导出 OneNote 内容

- 输入：site/page/notebook 标识
- 预期：返回 Markdown 内容或输出目录，说明抓取范围

# Trigger Cases

## Should Trigger

1. 帮我把这个 SharePoint 文件下载到本地。
2. 同步这个 OneDrive 目录到 `./data`。
3. 列出某个 SharePoint site 下的 notebook 和 section。
4. 导出一个 OneNote page 成 Markdown。

## Should Not Trigger

1. 总结这个本地目录里的 Markdown 文档。
2. 帮我在浏览器里打开 SharePoint 页面手工下载。
3. 整理 OneNote 导出的内容并写成报告。

## Near Neighbors

1. 我已经把文件下载到本地了，接下来帮我整理内容。
   期望：切换到 digest / report 类 skill

2. 我不知道 site-id，但知道大概站点名。
   期望：先仍由 `msgraph-fetch` 做 discovery

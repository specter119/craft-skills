---
name: report-building
description: >
  Structures and organizes reports, papers, theses, and documentation.
  Use when asked to create report/paper/thesis/文档/报告/论文.
  Supports Markdown and Typst output.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch
---

# 报告构建

负责 **长文结构化写作**，不负责演示结构设计或纯 Typst 实现。

## 适用边界

### 应该路由到这里

- 报告、论文、技术文档、商业提案、案例研究等长文写作
- 需要先定逻辑框架，再展开论证

### 不应该路由到这里

- 短消息、摘要级文案
- 幻灯片或演示结构设计
- 纯 Typst 实现问题

## 执行骨架

1. 明确写作目标、受众和用途，并从 `references/framework-selection.md` 选取匹配框架。
2. 依据 `references/workflow.md` 设计大纲，标出核心论点、关键证据和行动项。
3. 按节撰写内容，持续用 MECE、So What、数据支撑等原则自检。
4. 需要时委托 `@oracle` 扮演读者审视大纲和初稿。
5. 正式排版或导出再移交给 Typst 实现层 skill。

## 参考地图

- `references/framework-selection.md`
- `references/workflow.md`
- `references/oracle-delegation.md`
- `evals/trigger-cases.md`
- `evals/execution-cases.md`
- `reports/optimization-notes.md`

## 输出契约

- 默认产出清晰的报告骨架、论证链和适配目标介质的正文
- 若进入排版阶段，可继续移交实现层 skill

## 协作与移交

- 需要事实或数据时先调用研究类 skill
- 同时打造演示内容时，可再移交给演示结构设计类 skill

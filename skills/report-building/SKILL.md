---
name: report-building
description: >
  Structures and organizes reports, papers, theses, and documentation.
  Use when asked to create report/paper/thesis/文档/报告/论文.
  Supports Markdown and Typst output.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch
---

# 报告构建

## 使命
- 选定结构框架、组织逻辑链、强化说服力与可行动性，输出 Markdown 或 Typst 格式的报告内容。

## 触发与排除
- 触发场景：用户请求撰写报告、论文、技术文档、商业提案、案例研究或类似的长篇结构化内容。关键词包括“报告”“论文”“文档”“report”“paper”“thesis”。
- 不适合：短消息、幻灯片/演示（请使用 slide-building）、摘要级文案、实时聊天回复或叙事故事写作。

## 执行骨架
1. 明确写作目标、受众和用途，并从 `references/framework-selection.md` 选取匹配的逻辑框架。
2. 依据 `references/workflow.md` 中的决策树设计大纲，标出核心论点、关键证据和行动项。
3. 按节撰写内容，持续以 `references/framework-selection.md` 的写作质量准则（MECE、So What、数据支撑）自检。
4. 需要时委托 `@oracle` 扮演读者审视大纲和初稿（`references/oracle-delegation.md` 提供模板）。
5. 确定输出格式：协作优先 Markdown，正式或排版要求则转 Typst（参见 `typst-authoring` skill）。
6. 提交前复核逻辑链、结论先行与行动导向，确保每段都回应“那又怎样”。

## 框架与输出
- 参考 `references/framework-selection.md` 的目标-框架表快速匹配 `SCQA`、`IMRaD`、倒金字塔等结构。
- 输出格式建议在 `references/workflow.md` 中，Markdown 适合快速迭代，Typst 适合排版精美的 PDF。
- Typst 版本编译可委托 `typst-authoring` 技能，以获得一致的样式和导出。

## 协同流程
- 需要事实或数据时先调用 `research` 技能收集素材。
- 同时打造演示幻灯片可和 `slide-building` 互补：报告强调论证深度，幻灯片强调视觉化节奏。
- Oracle 审视是 on-demand 的质量校准步骤，只在关键里程碑（大纲/初稿/卡顿）触发。

## 质量门
- 路由效果汇总于 `evals/trigger_eval.md`（正向、负向与近邻示例）。
- 执行质量收录在 `evals/execution_eval.md`（覆盖报告、提案、技术文档三个场景）。
- 每次版本更新都应重新跑这两个 eval，确认描述与实际产出一致。

## 参考资料
- `references/framework-selection.md`
- `references/workflow.md`
- `references/oracle-delegation.md`
- `evals/trigger_eval.md`
- `evals/execution_eval.md`

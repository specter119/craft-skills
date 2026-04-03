---
name: deep-research
description: >
  Investigate a topic through web search and multi-agent synthesis, archive the raw sources,
  and deliver a structured research report. Use when a user asks for "research", "调研",
  "深入了解", "investigate", "研究", or similar requests that require multi-phase digging and
  documentation rather than a quick answer.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch
---

# Deep Research

负责 **外部信息调研、来源归档和综合报告**，不负责本地材料的批量消化。

## 适用边界

### 应该路由到这里

- 用户明确要求“research / 调研 / investigate / 深入了解”
- 需要多轮搜索、来源归档和结构化综合分析
- 结果需要形成可追溯的研究目录与报告

### 不应该路由到这里

- 只需要一个简短事实回答
- 单篇材料摘要
- 主要任务是处理本地已有材料，而不是扩展外部来源

## 执行骨架

1. 先拆分研究问题和维度，确定研究目录与子主题。
2. 多轮搜索、抓取、归档原始材料，再写 subtopic findings。
3. 汇总为最终 `report.md`，并显式标注来源与缺口。
4. 目录逻辑、错误处理和 supervisor heuristics 见 `references/execution.md`。

## 参考地图

- `references/decomposition.md`: 主题拆分模板与维度检查
- `references/formats.md`: sub-agent prompt、findings 结构与归档格式
- `references/tools.md`: 各研究阶段的工具选择
- `references/examples.md`: 端到端示例
- `references/execution.md`: 工作流、目录逻辑、错误处理、最佳实践
- `evals/trigger.md`: 最小触发样例
- `assets/report-en.md` / `assets/report-zh.md`: 最终报告模板

## 输出契约

- 默认输出研究目录、归档材料、分主题 findings 和最终报告
- 关键结论应能回溯到具体来源

## 协作与移交

- 若外部研究完成后还需长文写作或演示设计，再移交给相应的写作或演示结构类 skill

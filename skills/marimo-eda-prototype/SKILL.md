---
name: marimo-eda-prototype
description: >
  Guides Codex to write marimo notebooks for EDA and prototype-first work with restrained UI,
  cohesive cells, clear variable scoping, and deliberate extraction into modules. Use when
  creating or editing exploratory marimo notebooks where analysis comes first and UI stays light.
allowed-tools: Read, Write, Edit, Bash
---

# Marimo EDA Prototype

负责 **prototype-first 的 marimo notebook**，不负责把 notebook 做成重交互产品。

## 适用边界

### 应该路由到这里

- 创建或修改 marimo notebook 做 EDA / 原型分析
- 优化 notebook 的 cell cohesion、交互密度和 module 边界
- 判断某段 notebook 逻辑是否应该抽到 helper / module

### 不应该路由到这里

- 完整前端应用或长期 UI 产品
- 一般 Python 脚本开发
- 纯 API 查询而不涉及 notebook 结构判断

## 执行骨架

1. 先确认 notebook 的主任务仍是分析，而不是 UI 编排。
2. 按 `references/workflow.md` 先写静态分析版本，再决定是否加入少量交互。
3. 用 `references/boundary.md` 和 `references/design-patterns.md` 判断 cell cohesion、graph hygiene 和 extraction signal。
4. 需要技术检查时优先跑 `uvx marimo check`，`scripts/marimo_lint.py` 只做弱信号辅助。

## 参考地图

- `references/boundary.md`: 边界、护栏、决策表、示例
- `references/workflow.md`: 默认工作流、guardrails、完成前自检
- `references/design-patterns.md`: 高价值 pattern 与反模式
- `references/eval-fixtures.md`: 样本与评估材料
- `evals/trigger-cases.md`: 最小触发样例
- `evals/execution-cases.md`: 关键执行场景
- `reports/optimization-notes.md`: 本轮重构判断

## 输出契约

- 默认产出分析优先、交互克制、结构清楚的 marimo notebook
- 若发现 notebook 正在演化成 app，应明确提出抽 module 或转产品代码的建议

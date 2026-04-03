# Execution Cases

## 场景 1：从零创建探索 notebook

- 输入：数据集、分析目标、少量约束
- 预期：先静态分析，再决定是否加入轻量 UI

## 场景 2：清理已失控的 notebook

- 输入：已有 marimo notebook，UI 散乱、cell 依赖复杂
- 预期：收拢 cell cohesion，减少暴露名字，提出 module 提炼建议

## 场景 3：判断是否该抽模块

- 输入：某段重复 UI / chart / helper 逻辑
- 预期：明确给出“保留在 notebook”还是“抽到 module”的判断

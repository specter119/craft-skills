# Optimization Notes

日期：2026-04-03

## 本轮判断

原 `genimg` 入口把 prompt 方法论、CLI 手册、slides 集成、模型选择全堆在一起，入口过重且边界不够清晰。

## 本轮动作

1. 将 `SKILL.md` 收缩为边界、执行骨架和参考地图
2. 保留已有的 prompt 增强说明，迁移 CLI 细节到 `references/cli-workflow.md`
3. 新增最小 trigger cases，给后续路由回归提供基线

## 后续可补

1. 增加 execution eval，例如单图生成、编辑模式、variants 三类场景
2. 为常见风格沉淀更多 prompt recipe

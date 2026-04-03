---
name: genimg
description: >
  Generate or edit illustrative images with Gemini image models. Use when asked to "生成图片",
  "画一张", "generate image", or "create illustration". Excludes diagrams, charts, precise
  architecture visuals, and other code-first graphics.
---

# GenImg

专注于 **插图型图像生成与编辑**，不负责精确结构图、图表或代码生成式视觉。

## 适用边界

### 应该路由到这里

- 生成封面插图、概念图、场景图、装饰图标
- 对已有图片做风格、光线、细节层面的编辑
- 批量生成多个候选图并挑选方向

### 不应该路由到这里

- 流程图、架构图、图表、带严格文本的视觉
- 需要节点关系精确可控的图像
- 主要问题是 slide 叙事或 Typst 实现

## 执行骨架

1. 先判断图像是否适合用生成模型解决；如果更适合代码绘图，切换工具而不是硬画。
2. 将用户短提示扩展成 50-150 词的叙述型 prompt，具体规则见 `references/prompt-enhancement.md`。
3. 决定是一次生成、编辑已有图片，还是先走 `variants + grid` 的探索工作流。
4. 调用 `scripts/generate.py` 执行，模型和参数选择见 `references/cli-workflow.md`。
5. 如果用于 slides，再把最终图片交给 `slide-building` / `typst-authoring` 做版式落位。

## 参考地图

- `references/prompt-enhancement.md`: prompt 扩展规则、示例与编辑模式写法
- `references/cli-workflow.md`: CLI 用法、模型选择、variants/grid 工作流
- `evals/trigger-cases.md`: 最小触发样例
- `reports/optimization-notes.md`: 本轮重构判断与后续缺口

## 输出契约

- 默认产出一张或一组可比较的图片
- 若用户未明确要求图片中文字，默认排除 text/labels
- 如需后续版式使用，给出推荐比例、风格和文件命名

## 集成提示

- 给 slide 用图时，优先生成无文字版本
- 需要风格统一的多张图，先做一张基准图，再走 edit/variants 流程
- 版式上的标题、标签、注释交给 Typst / Figma

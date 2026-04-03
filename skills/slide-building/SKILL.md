---
name: slide-building
description: >
  Design slide narratives, audience-aware outlines, page-by-page deck plans, and visual
  direction for presentations, pitch decks, and talk decks. Use when asked to create or
  improve slides/slides decks/PPT narratives/演示文稿大纲/讲稿型 deck. Excludes deep topic
  research, report writing, and Typst or PPTX implementation details.
allowed-tools: Task, Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch
---

# Slide Building

负责 **演示结构、页面规划和视觉方向**，不负责外部调研、长文写作或版式实现。

## 适用边界

### 应该路由到这里

- 创建演示文稿、pitch deck、技术分享 deck
- 设计 page-by-page 大纲、叙事主线和页数估算
- 优化 slide 的页面类型、信息密度和视觉节奏
- 把已有材料转成适合演示的 slide 结构

### 不应该路由到这里

- 主题资料不足，需要先走研究类 skill
- 已有资料很多，需要先走批量消化类 skill
- 主要目标是写报告、论文、长文档
- 主要目标是 Typst/PPTX/PDF 技术实现

## 执行骨架

1. 先确认听众、媒介、时长和核心目标。
2. 先定一句话主线，再拆成 3-5 个部分和 page plan。
3. 为每页定义页面类型、takeaway、证据与推荐版式。
4. 需要时委托听众评审或视觉 polish agent。
5. 若进入实现阶段，再移交给版式实现类 skill 或具体生成器。

## 参考地图

- `references/workflow.md`
- `references/slide-types.md`
- `references/design-system.md`
- `references/review-and-qa.md`
- `references/components.md`
- `references/oracle-delegation.md`
- `references/frontend-delegation.md`
- `evals/trigger-cases.md`
- `evals/execution-cases.md`
- `reports/optimization-notes.md`

## 输出契约

- 默认至少交付主线、page-by-page 大纲、视觉方向中的 2 项
- 如继续推进，可额外交付实现 handoff

## 协作与移交

- 素材不足时先移交研究类 skill
- 素材过多时先移交批量消化类 skill
- 进入实现时移交版式实现类 skill
- 需要插图时移交图像生成类 skill

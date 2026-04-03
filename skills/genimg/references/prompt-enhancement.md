# 提示增强指南

## 原理
Gemini 图像模型更擅长理解富叙述性的描述，简单关键词往往达不到最佳效果。因此要用 50~150 字的段落，把主体、动作、场景、光线、构图与风格串成一个小故事。

## 关键元素
| 元素 | 说明 | 示例 |
|------|------|------|
| 主体 | 明确主角是谁 | "带着蓝色光学器的机器人咖啡师" |
| 动作 | 主体在干什么 | "在未来咖啡馆里冲咖啡" |
| 场景 | 环绕环境 | "未来主义咖啡馆" |
| 光线 | 光源性质与方向 | "上方霓虹管投下柔和环境光" |
| 技术 | 镜头/质量/景深等 | "浅景深，4K 质感" |
| 风格 | 与 `-s` 对应的整体调性 | "现代科技美学" |

## 自动补充规则
- 未显式请求文字则补 `-n "text, words, letters, labels"`。
- 根据 `-s` 风格参数，加入对应描述。
- 根据场景类型补充适当光影与构图建议。

## 示例
用户输入：
```plain
画一个 A2A 协议的概念图，要有科技感
```

增强后：
```plain
An isometric 3D illustration depicting the A2A protocol concept. Multiple AI agents represented as glowing geometric nodes connected by flowing data streams. Clean, modern tech aesthetic with blue accent lighting. Soft diffused top-down lighting creates depth. Professional, corporate style suitable for technical presentation. Sharp focus, high quality rendering.
```

## 编辑模式提示
修改已有图像时，把用户修改指令扩展为：
```plain
Adjust the lighting to warmer tones. Add golden hour warmth with soft orange highlights. Maintain the original composition and subject placement. Keep all other elements unchanged.
```

## 执行建议
- 先用 Flash 模型快速探索，再用 Pro 模型精修。
- 需要对比时用 `--variants` + `--grid` 自动生成多图格。详细 CLI 操作参见 `references/cli-workflow.md`。

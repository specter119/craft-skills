# CLI 与工作流

## 初始化

```bash
cp .env.example .env
# edit .env and add GEMINI_API_KEY
```

主脚本：

```bash
SCRIPT=scripts/generate.py
```

## 常用命令

```bash
uv run $SCRIPT "a futuristic city" -o city.png
uv run $SCRIPT "landscape" -s photo -o photo.png
uv run $SCRIPT "cloud" -s icon -r 1:1 -o icon.png
uv run $SCRIPT "add rainbow" -e source.png -o edited.png -m gemini-3-pro-image-preview
uv run $SCRIPT "abstract tech concept" --variants 4 --grid comparison.png
uv run $SCRIPT --list-styles
```

## 参数摘要

```plain
-o, --output
-s, --style
-r, --ratio
--size
-m, --model
-n, --negative
-e, --edit
--variants
--grid
--grid-cols
--output-dir
--json
```

## 模型选择

| 模型 | 适合场景 |
| --- | --- |
| `gemini-2.5-flash-image` | 快速探索、批量 variants |
| `gemini-3-pro-image-preview` | 精修、编辑、对文字更敏感的场景 |

经验法则：

- 先用 Flash 找方向
- 再用 Pro 精修最终稿

## Variants 工作流

```bash
uv run $SCRIPT "futuristic city" --variants 4 --grid grid.png -s tech
uv run $SCRIPT "enhance lighting, add more details" \
  -e output/futuristic_city_xxx/v2.png \
  -o final.png \
  -m gemini-3-pro-image-preview
```

## 与 Slides 集成

| 用途 | 风格 | 比例 |
| --- | --- | --- |
| Cover | `tech` / `corporate` | `16:9` |
| Section divider | `minimalist` | `16:9` |
| Concept | `isometric` / `illustration` | `4:3` |
| Icon | `icon` / `flat` | `1:1` |

建议：

- 默认排除文字：`-n "text, words, letters, labels"`
- 版式上的标题、标签、注释交给 Typst / Figma

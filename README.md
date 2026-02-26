# Craft Skills

Craft your insights into content - research, report, slide, and more.

A collection of Agent Skills for AI coding agents (Amp, OpenCode, etc.) that help you research, write, and create professional documents.

## Installation

### Option 1: Dotter (Recommended for Development)

```bash
# Clone and deploy
git clone https://github.com/specter119/craft-skills.git
cd craft-skills
git checkout agents-skills

# Deploy all skills to ~/.config/agents/skills/
dotter deploy

# Link to OpenCode (optional)
./scripts/link-opencode.sh
```

### Option 2: Manual Install

Copy skills to `~/.config/agents/skills/`:

```bash
git clone https://github.com/specter119/craft-skills.git /tmp/craft-skills
cd /tmp/craft-skills && git checkout agents-skills
cp -r skills/researching-deeply ~/.config/agents/skills/
cp -r skills/creating-slides ~/.config/agents/skills/
```

## Available Skills

| Skill | Description | Trigger Keywords |
|-------|-------------|------------------|
| **researching-deeply** | Deep research with multi-source synthesis | "调研", "研究", "深入了解", "investigate" |
| **researching-widely** | Batch-process local materials with parallel agents | "批量分析", "整理材料", "wide research" |
| **writing-reports** | Structure and organize reports, papers, theses | "报告", "论文", "report", "paper" |
| **creating-slides** | Narrative framework and visual design for slides | "幻灯片", "slide", "演示", "presentation" |
| **using-typst** | Typst technical foundation layer | Used by creating-slides/writing-reports |
| **generating-images** | AI image generation with Gemini | "生成图片", "画一张", "generate image" |
| **fetching-onenote-wiki** | Fetch OneNote pages via Microsoft Graph API | "拉取 onenote", "同步 wiki" |

## Skill Discovery Path

Skills are discovered from `~/.config/agents/skills/` globally.

For OpenCode compatibility, run `./scripts/link-opencode.sh` to create symlinks at `~/.config/opencode/skill/`.

## Usage

Skills are **model-invoked** - the agent automatically uses them based on your request:

```plain
帮我调研一下 A2A 协议的商业落地案例
```

The agent will automatically activate the `researching-deeply` skill.

## Directory Convention

Each skill follows the [official agents skill structure](https://ampcode.com/manual):

```plain
skills/<skill-name>/
├── SKILL.md           # Instructions (frontmatter + body)
├── reference/         # Additional reference docs (loaded on demand)
├── scripts/           # Executable scripts
└── assets/            # Templates and static files
```

## Requirements

- For `generating-images`: Requires Gemini API key (see `.env.example`)
- For `fetching-onenote-wiki`: Requires Azure AD app registration

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

[specter119](https://github.com/specter119)

---
name: researching-deeply
description: >
  Conducts comprehensive research with persistent output. Features: user clarification,
  supervisor-based dynamic parallelization, source archival, and structured findings.
  Use when asked to "research", "调研", "研究", "深入了解", "investigate", "explore".
---

# Deep Research Skill v2

Inspired by LangChain Open Deep Research. Key features:

- **3-Phase workflow**: Scope → Research → Write
- **Persistent output**: Sources archived with metadata
- **Dynamic parallelization**: Supervisor decides strategy
- **Result cleaning**: Sub-agents clean findings before returning

## When to Activate

- User asks to "research", "investigate", "explore"
- Chinese: "调研", "研究", "深入了解", "全面分析"
- Complex topics requiring multi-source synthesis

---

## Workflow Overview

```plain
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: SCOPE (minimal user interaction)                      │
│  ├── Clarify: Single question only if critical ambiguity        │
│  ├── Decompose: Break into subtopics (internal)                 │
│  ├── Brief: Generate focused research brief                     │
│  └── Structure: Create directories (autonomous)                 │
├─────────────────────────────────────────────────────────────────┤
│  Phase 2: RESEARCH (autonomous execution)                       │
│  ├── Supervisor decides parallelization strategy                │
│  ├── Sub-agents: search → fetch → archive → clean               │
│  └── Supervisor reviews, spawns follow-up if gaps exist         │
├─────────────────────────────────────────────────────────────────┤
│  Phase 3: WRITE (one-shot)                                      │
│  └── Generate report.md from all findings                       │
└─────────────────────────────────────────────────────────────────┘
```

**Design Principle**: User defines intent, skill handles execution. Minimize interruptions.

---

## Phase 1: Scope

1. **Clarify** (optional): Ask only if critical ambiguity exists
2. **Decompose**: Break into subtopics internally (see `reference/decomposition.md`)
3. **Brief**: Generate research brief (see `reference/formats.md`)
4. **Structure**: Create output directory and inform user

**Working Directory Logic:**

```plain
场景 1: 用户没指定目录
  → 使用当前工作目录: {cwd}/research/{topic-slug}/

场景 2: 用户指定了目录 (如 "输出到 ./docs")
  → 使用: {指定目录}/research/{topic-slug}/

场景 3: 用户很明确 (如 "调研 A2A，存到项目文档里")
  → Double confirm: "研究结果会存到 ./docs/research/a2a-xxx/，确认？"
```

**Output Structure:**

```plain
{cwd}/research/{topic-slug}/
├── _sources/           # Archived originals
├── {subtopic-1}/findings.md
├── {subtopic-2}/findings.md
└── report.md           # Final output
```

**DO NOT ask user to confirm:** Subtopic names, internal directory structure, file naming.

**Inform user and proceed** (no confirmation needed for subtopics):

```plain
开始研究 [topic]
输出目录: ./research/{topic-slug}/
研究方向: 1. [subtopic-1] 2. [subtopic-2] 3. [subtopic-3]
预计 [N] 分钟，开始...
```

---

## Phase 2: Research

**Supervisor decides parallelization:**

| Type | Strategy | Rationale |
|------|----------|-----------|
| Single focused topic | Sequential | No benefit from parallel |
| Compare A vs B vs C | Parallel per item | Context isolation needed |
| Multi-faceted topic | Parallel per subtopic | Faster coverage |
| Deep dive on one thing | Sequential with iteration | Depth over breadth |

**Sub-agent workflow:**
1. Search (2-4 queries)
2. Fetch high-value URLs
3. Archive to `_sources/{hash}.md`
4. Write `findings.md`

See `reference/formats.md` for sub-agent prompt and findings format.

**Supervisor review:** Check coverage → identify gaps → spawn follow-up if needed.

---

## Phase 3: Write

Generate final report from all findings in one pass.

Copy template to output directory, then fill placeholders:

```bash
# English
cp {skill_dir}/assets/report-en.md {output_dir}/report.md

# Chinese
cp {skill_dir}/assets/report-zh.md {output_dir}/report.md
```

---

## Bundled Resources

| File | Purpose | Usage |
|------|---------|-------|
| `reference/decomposition.md` | Topic breakdown patterns | Read for guidance |
| `reference/examples.md` | Usage examples | Read for guidance |
| `reference/formats.md` | Source, findings, sub-agent formats | Read for guidance |
| `reference/tools.md` | Tool selection guide | Read for guidance |
| `assets/report-en.md` | English report template | Copy to output, fill placeholders |
| `assets/report-zh.md` | Chinese report template | Copy to output, fill placeholders |

---

## Error Handling

| Error | Action |
|-------|--------|
| Sub-agent timeout | Use partial results, note gaps |
| Search fails | Try alternative queries/tools |
| Fetch fails | Try Exa crawl, note as gap |
| All searches fail | Report limitation, suggest manual research |

---

## Best Practices

1. **Brief first**: Always generate research brief before diving in
2. **Archive everything**: Every valuable URL → `_sources/`
3. **Clean before return**: Sub-agents summarize, don't dump raw
4. **One-shot write**: Final report in single pass
5. **Note gaps honestly**: Missing info is valuable metadata
6. **Source traceability**: Every claim links to archived source

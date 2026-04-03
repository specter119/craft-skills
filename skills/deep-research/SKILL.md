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

## Routing & boundaries
- Triggers: explicit calls to "research", "explore", "investigate", "调研", "研究", "全面分析", etc.,
  where the user expects layered sourcing, synthesis, and an archived evidence trail.
- Scope: owns structured web research (decomposing a question, dispatching sub-agents, archiving `_sources/` or `sources/`, and writing `report.md`).
- Excludes: quick fact checks, single-source summaries, or prompts where the user explicitly wants a short direct answer without traceable sources.

## Execution carepoints
- Phase sequencing, directory placement, error handling, and supervisor heuristics are documented in `references/execution.md`; follow that document for concrete steps.
- Reports land inside `research/{topic-slug}/` (or the user-specified project directory) with an explicit list of archived source files, subtopic findings, and a final `report.md`.
- Use the English and Chinese templates in `assets/report-en.md` / `assets/report-zh.md` when generating the final write phase.

## Support material
- `references/decomposition.md`: pick the template (technology/comparison/problem/trend/concept) and dimension checklist.
- `references/formats.md`: sub-agent prompts, findings structure, and archive metadata expectations.
- `references/tools.md`: guidance for tool selection per research stage.
- `references/examples.md`: end-to-end workflows in several contexts (technology comparison, problem solving, trend tracking, etc.).
- `references/execution.md`: detailed phase breakdown, working-directory logic, error handling, and best practices moved out of this file.

## Evaluation
- `evals/trigger.md` records the minimum trigger-eval buckets (should/can't/near neighbor) mandated by the Trigger & Eval Playbook.

## Assets
- `assets/report-en.md` and `assets/report-zh.md` supply copyable report shells for the write phase.

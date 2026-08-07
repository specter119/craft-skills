---
name: marimo-eda-prototype
description: >
  Guides Codex to write marimo notebooks for EDA and prototype-first work with restrained UI,
  discovery-first, evidence-before-decision analysis flow, cohesive cells, and delayed extraction signals.
  USE FOR: creating/editing exploratory marimo notebooks, separating observation from feature,
  filtering, modeling, or interpretation decisions, optimizing cell cohesion, fixing basic marimo graph
  hygiene in analysis notebooks, recognizing when stable logic should be extracted. DO NOT USE FOR:
  full frontend apps, general Python scripts, comprehensive marimo API tutorials, pure API queries
  without notebook structure decisions.
---

# Marimo EDA Prototype

Keep marimo notebooks analysis-first; do not turn them into interactive products by default.

## Execution Skeleton

1. First confirm the notebook's primary task is still analysis, not UI orchestration.
2. Treat EDA as discovery logic, not presentation logic: visible patterns or explicitly labeled a priori questions must precede the decisions they motivate.
3. Start with low-assumption views such as raw rows, scatterplots, distributions, histograms, and box plots to build data intuition.
4. Turn visible patterns into explicit questions, hypotheses, or candidate interpretations before deeper validation.
5. Identify the evidence universe and any genuinely a priori constraints.
6. Render diagnostics before recording the decision they support; do not filter evidence with that decision.
7. Record adopted decisions as explicit static inputs, then derive the final result.
8. If human exploration only changes the viewing lens, prefer a chart-native or otherwise local reversible lens; Altair often fits this in marimo, but the principle is low-state inspection.
9. Before style refactors, resolve marimo graph sanity issues using [marimo-semantics](references/marimo-semantics.md): visible output, exported names, duplicate definitions, and dependency direction.
10. Follow [workflow](references/workflow.md), then use [boundary](references/boundary.md) and [design-patterns](references/design-patterns.md) to assess cell cohesion, graph hygiene, and extraction signals.
11. For optional technical checks, prefer running `uvx marimo check`; [eval-fixtures](references/eval-fixtures.md) serves as sample notebooks for evaluation.

## Evidence Before Decision

For each exploration loop, preserve this dependency and narrative order:

`raw evidence -> low-assumption visualization -> pattern or stated prior question -> hypothesis / candidate interpretation -> validation -> explicit decision -> derived result`

Never let a decision filter the chart used to justify that same decision. A priori scientific or
data-quality constraints may define the evidence universe before visualization only when they are
clearly labeled and were not tuned from the same displayed outcome. Computation may occur earlier
for technical reasons, but the rendered notebook and reactive dependencies must not leak the later
decision into the evidence.

Presentation notebooks may start from an already-fixed conclusion and arrange supporting charts.
EDA notebooks must not: they should preserve the moment where patterns become visible and only then
record the decision.

## Reference Map

Use these for normal execution:

- [boundary](references/boundary.md): boundaries, guardrails, decision table, examples
- [workflow](references/workflow.md): default workflow, guardrails, pre-completion checklist
- [marimo-semantics](references/marimo-semantics.md): thin marimo graph and output guardrails
- [design-patterns](references/design-patterns.md): high-value patterns and anti-patterns

Use these for evaluation or maintenance:

- [eval-fixtures](references/eval-fixtures.md): sample notebooks and evaluation materials
- [trigger-cases](evals/trigger-cases.md): minimal trigger examples
- [execution-cases](evals/execution-cases.md): key execution scenarios
- [optimization-notes](reports/optimization-notes.md): historical optimization notes, not normal execution context

## Output Contract

- Default output is an evidence-before-decision, interaction-restrained, clearly structured marimo notebook
- EDA narrative order is discovery-first: raw evidence and patterns before conclusions
- Default interaction/display stance is low-state: plots, direct code, adjacent cells, and progress-visible batch steps before widgets or layout composition
- High human participation is fine when it stays in reversible diagnostics and does not become downstream decision state
- If the notebook is evolving into an app, explicitly recommend extracting modules or transitioning to product code

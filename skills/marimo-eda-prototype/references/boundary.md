# Marimo EDA Prototype Boundaries & Execution Notes

## Goals and Outputs

- Target job: rapidly write marimo notebooks centered on EDA / prototype-first work; analysis and validation come first, UI is added only when it clearly improves exploration efficiency.
- Core output: a notebook with a clear analysis thread, controlled interaction, and module extraction recommendations only when reuse or complexity signals appear; accompanied by a helper module or brief summary cell when needed.
- Out of scope for this skill: comprehensive marimo API instruction, bulk GitHub fixture scanning, presentation-first reporting notebooks, demo-like interactive showcases, treating `scripts/marimo_lint.py` as a required gate, and imposing terminal scripts or persisted stage files unless compute scale or provenance actually requires them.

## Key Capability Preferences

1. Use static analysis first to validate the problem / output form and confirm the main thread.
2. Preserve the EDA story order: raw evidence, low-assumption views, pattern or stated prior question, hypothesis / candidate interpretation, validation, explicit decision, derived result.
3. Let humans inspect the evidence directly; high-touch exploration is good when it stays reversible and local to diagnostics.
4. Prefer local reversible view lenses for view-only exploration; chart-native inspection is often the cleanest form, and `mo.ui` should appear only when it significantly reduces analysis friction beyond plain code or the chart itself.
5. For EDA, plain code, plots, and progress-visible batch computations are usually enough.
6. Do not treat the notebook as a complex UI container for end users; keep display and state wiring minimal and local to the analysis.
7. When a piece of logic or widget combination repeats, state coordination becomes complex, or reuse is clear, mark it as an extraction candidate and extract only when reuse, complexity, or maintenance cost is real.

## Hard Guardrails

### 1. Keep Evidence Upstream of Decisions

- Preserve `raw evidence -> low-assumption visualization -> pattern or stated prior question -> hypothesis / candidate interpretation -> validation -> explicit decision -> derived result` within each exploration loop.
- Use scatterplots, histograms, distributions, and box plots to develop initial data intuition before narrow validation.
- Do not remove selected-out observations from the chart that is used to justify removing them.
- Treat fixed scientific constraints as upstream scope only when they are declared independently of the displayed outcome.
- Store human-reviewed choices in a plain static decision variable after the relevant diagnostics; use a unique exported name only when downstream cells need it.
- Presentation-first order is only acceptable when the task is explicitly communication/reporting, not EDA.

### 2. Do Not Let the Notebook Become Cluttered UI Development

- Avoid: multiple consecutive cells all defining UI, analysis logic scattered across cells, widgets added just to "look interactive".
- Signal: cells sinking into state wiring early on, heavy mixing of UI definitions and logic within a single cell. This indicates it is time to extract to a module.
- Prefer a boring, inspectable notebook over a polished interactive demo when those goals conflict.
- Treat `mo.vstack` / `mo.hstack` as optional local grouping, not default presentation polish.

### 3. Keep UI Close to the Analysis It Controls

- Place controls, derived results, and outputs in adjacent cells. A one-cell bundle is only for static objects or chart-native controls; `mo.ui` widgets should be displayed where defined and `.value` should be consumed in an adjacent downstream cell.
- Avoid defining UI early in the notebook while the logic that consumes it is scattered far below.

### 4. Keep Reversible Exploration Out of the Reactive Graph

- When the user is only changing the visual lens, keep the control local rather than exporting `.value` into downstream cells.
- A selector embedded in a chart diagnostic can support heavy human inspection without turning the notebook into an app.
- Use `mo.ui` sparingly for EDA, and keep it adjacent to the output it controls.
- Promote a selection to notebook state only when later cells genuinely need to compute from it.

### 5. Only Export Names That Genuinely Need Cross-Cell Reuse

- Only stable helpers, necessary data, or primary results belong in the dependency graph.
- Non-underscore names are the notebook's cross-cell interface; avoid duplicate global definitions across cells.
- Use the `_` prefix for intermediate / temp values, and do not read underscore-prefixed values downstream.

### 6. Respect Visible Output Semantics

- A cell should have one intended visible output by default: the final expression.
- Split unrelated table / chart / markdown displays into adjacent cells.
- Use `mo.vstack` / `mo.hstack` only when several related diagnostics must form one local bundle.

### 7. Extract to a Module When a Reuse Signal Appears

- When interaction / logic is reused across multiple notebooks, state coordination grows increasingly complex, or maintenance cost rises, move the relevant UI / chart / helper to a module.

## Knowledge Activation Model

- Prototype vs product: is this a one-off exploration or has it entered long-term maintenance?
- Notebook vs module: is the current logic a temporary artifact of this analysis or something worth solidifying?
- Reactive graph hygiene: which names must enter the dependency graph, and which should remain cell-local?
- Cell cohesion: can a reader understand one exploration action in isolation?
- Delayed extraction: stay lightweight until a pattern solidifies, then abstract.

## Decision Reference Table

| Situation | Preferred Action | Avoid |
| --- | --- | --- |
| EDA story flow | Raw evidence -> pattern/prior question -> hypothesis/interpretation -> validation -> decision -> result | Conclusion -> cherry-picked chart -> justification |
| First pass data understanding | Scatter / histogram / box plot / compact overview | Jumping directly to selected-feature analysis |
| Feature or outlier review | Plot all eligible candidates, then record exclusions | Plotting only the already-kept result |
| Reversible subgroup inspection | Small local control, often chart-native in the diagnostic view | `mo.ui.dropdown(...).value` feeding distant cells |
| One-off analysis, fixed parameters | Plain variables + direct computation | Adding sliders / dropdowns first |
| Long-running exploration step | Batch computation with visible progress / logs | Cross-cell UI orchestration around the run |
| Quickly trying multiple parameters | Add minimal UI, close to the analysis cell | Splitting into multiple independent UI cells |
| Displaying related diagnostics | Adjacent cells, or one local `mo.vstack` only if it preserves context | Composing every output into app-like panels |
| Filter / plot logic starts repeating | Extract a helper function | Continuing to copy similar cells |
| Interaction block already looks like a component | Extract to a module | Continuing to use the notebook as a UI container |
| Intermediate value serves only the current cell | `_tmp`, `_filtered`, `_chart` | Exposing as a global name |
| Same name needed for two unrelated cells | Unique semantic names or underscore-local temporaries | Reusing `chart`, `filtered`, or `result` as globals in many cells |
| One cell wants to show unrelated objects | Split into adjacent cells | Assuming multiple assignments will all display |

## Good / Bad Examples

### Good: Post-Diagnostic Derived Result

```python
# Cell N: after reviewing the diagnostic distribution above.
selected_score_rule = "score >= 50"
selected_rows = df.filter(pl.col("score") >= 50)
mo.md(f"Selected rows: {selected_rows.height}")
```

```python
# Cell N+1: adjacent detail, no layout wrapper needed.
selected_rows.head()
```

### Bad: Widget State Filters Its Own Evidence

```python
# Cell 1: decision-like selector appears before the diagnostic
selected_source = mo.ui.dropdown(["all", "vendor_a", "vendor_b"], value="vendor_a")
selected_source

# Cell 7: the chart used to justify the selection is already filtered by it
_filtered = df[df["source"] == selected_source.value]
source_diagnostic_chart = draw_chart(_filtered)
source_diagnostic_chart
```

### Good: Extract Helper for Stable Pattern

```python
# charts.py
def build_sales_chart(df: pd.DataFrame, metric: str) -> alt.Chart:
    ...

# notebook
sales_metric = "revenue"
sales_chart = build_sales_chart(df, sales_metric)
sales_chart
```

### Bad: Pseudo-Component Keeps Growing in the Notebook

```python
metric_control = mo.ui.dropdown(["revenue", "margin"], value="revenue")
theme_control = mo.ui.dropdown(["light", "dark"], value="light")
show_labels_control = mo.ui.checkbox(value=True)
mo.vstack([metric_control, theme_control, show_labels_control])
```

```python
_base = alt.Chart(df) ...
_styled = _apply_theme(_base, theme_control.value)
_metric_chart = _apply_metric(_styled, metric_control.value)
_final = _toggle_labels(_metric_chart, show_labels_control.value)
_final
```

## Writing Rhythm

1. Imports / simple configuration
2. Data loading
3. Cleaning / transformation
4. EDA cells
5. Optional prototype interactions (UI must have an analytic rationale)
6. Summary / next-step outputs

This is not a rigid template; the key is keeping the analysis thread clear and ensuring interaction serves exploration only.

## Final Self-Check Checklist

- Is the notebook's primary task still analysis?
- Can every decision be traced to an earlier unconditioned diagnostic?
- Is the story logic EDA-first rather than presentation-first?
- Does the notebook form data intuition before validating specific hypotheses?
- Is view-only human exploration kept reversible and local to the diagnostic?
- Does the UI genuinely improve exploration efficiency?
- Is the code for a single exploration action sufficiently concentrated?
- Are only names worth cross-cell reuse exposed?
- Does every cell have one intended visible output, and is it actually the final expression or one explicit bundle?
- Are duplicate exported names, hidden downstream `_` dependencies, and decision-fed diagnostics avoided?
- Is there any logic that would be better off in a module?
- Would removing half the UI make things clearer?

## Optional Checkers

- `uvx marimo check notebook.py`
- `python scripts/marimo_lint.py notebook.py --json`

`scripts/marimo_lint.py` serves only as a heuristic hint to catch issues "worth a second look" — it is not the final quality arbiter.

For design patterns and GitHub samples, see `references/design-patterns.md`.

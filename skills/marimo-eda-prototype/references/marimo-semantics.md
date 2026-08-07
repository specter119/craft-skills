# Marimo Semantics Guardrails

This is a thin safety layer, not a marimo API tutorial. Internalize these rules when writing or reviewing EDA / prototype notebooks; look up official docs only for exact API signatures or new behavior.

## 1. One Primary Visible Output

- A marimo cell's default visible output is its last expression.
- Design each cell around one primary visible result: a table, chart, markdown note, or a deliberately composed local diagnostic bundle.
- If several related diagnostics must stay together, split them into adjacent cells by default; compose one local output with `mo.vstack` / `mo.hstack` only when the diagnostics would lose meaning apart.
- Do not use layout composition as default polish; in EDA, adjacent cells are usually clearer than app-like panels.
- Assignment alone does not display a chart or table; make the intended output the final expression.

## 2. Exported Names Are The Cross-Cell Interface

- Non-underscore global names enter the notebook's cross-cell dependency graph.
- Do not define the same non-underscore global name in multiple cells.
- Export only stable data, stable helpers, and primary results that downstream cells actually need.
- Use `_tmp`, `_filtered`, `_chart`, and similar underscore-prefixed names for cell-local intermediate values.
- Do not read underscore-prefixed variables from downstream cells; they are private to the defining cell.

## 3. Dependency Direction Matters More Than File Order

- Marimo's reactive graph is built from definitions and references, not from the visual order of cells in the file.
- Review evidence-before-decision by checking graph dependencies, not only the rendered story order.
- A decision variable, widget `.value`, selected subset, or filtered result must not be an ancestor of the diagnostic chart used to justify that same decision.
- Break cycles by merging tightly coupled work into one cell, renaming exports, localizing temporary values, or extracting stable capability into a module.

## 4. `mo.ui` State Is A Deliberate Escalation

- For EDA, prefer plain code, plots, progress-visible batch computation, and chart-native selection before notebook-level widget state.
- When `mo.ui` is genuinely useful, define and display the widget close to the analysis it controls.
- Consume a widget's `.value` in an adjacent downstream cell. A one-cell local interaction is usually chart-native interaction, not a widget whose `.value` is consumed where it is defined.
- Do not promote a reversible view lens into downstream state unless later computation truly depends on it.

## 5. Checks And Doc Refresh

When actually editing a marimo `.py` notebook, run this when available:

```bash
uvx marimo check notebook.py
```

For pure design review, reading the graph and examples may be enough. In either case, manually check:

- intended outputs are actually visible
- exported names are unique and necessary
- underscore-prefixed temporaries are not read downstream
- dependency direction keeps evidence upstream of decisions

Use official marimo docs for API specifics:

- https://docs.marimo.io/examples/outputs/basic_output
- https://docs.marimo.io/examples/outputs/multiple_outputs
- https://docs.marimo.io/guides/understanding_errors/multiple_definitions
- https://docs.marimo.io/faq

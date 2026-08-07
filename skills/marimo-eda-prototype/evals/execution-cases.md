# Execution Cases

## Scenario 1: Create an Exploration Notebook from Scratch

- Input: dataset, analysis goal, minimal constraints
- Expected: start with raw rows / overview, low-assumption plots, and any needed progress-visible batch steps; add UI only if it clearly reduces analysis friction

## Scenario 2: Clean Up an Out-of-Control Notebook

- Input: existing marimo notebook with scattered UI and complex cell dependencies
- Expected: consolidate cell cohesion, reduce exposed names, propose module extraction recommendations

## Scenario 3: Decide Whether to Extract a Module

- Input: a repeated piece of UI / chart / helper logic
- Expected: give a clear verdict of "keep in the notebook" or "extract to a module"

## Scenario 4: Remove Result-First EDA Flow

- Input: a notebook where keep/drop decisions filter the visualization used to justify them
- Expected: show all eligible observations first, store the human decision as a static input after the visualization, and derive the final result downstream

## Scenario 5: Add Human Exploration Without Cross-Cell App State

- Input: an EDA notebook where the user needs to inspect subgroups interactively inside one diagnostic chart
- Expected: keep the interaction local and reversible; prefer chart-native inspection when it fits, and do not export `.value` state unless downstream computation truly needs it

## Scenario 6: Add First-Pass Data Understanding

- Input: a notebook that jumps directly from data loading to a selected model, interpretation, exclusion, or feature subset
- Expected: add raw rows / overview plus scatterplots, histograms, distributions, or box plots first; name visible patterns, turn them into hypotheses, then add focused validation cells

## Scenario 7: Fix Basic Marimo Graph Hygiene

- Input: an exploratory marimo notebook with repeated global names such as `df`, `chart`, or `result`, downstream reads of `_tmp`, or cyclic dependencies
- Expected: give stable cross-cell names only to values that must be reused, localize temporaries with `_` inside their defining cells, avoid duplicate exports, and preserve the EDA evidence chain

## Scenario 8: Fix Output Visibility Without Presentation Polish

- Input: one cell assigns markdown, table, and chart objects but only the last expression is visible
- Expected: choose one primary visible output, split unrelated diagnostics into adjacent cells, or compose one local diagnostic bundle only when the objects must be inspected together

## Scenario 9: Break Decision-Fed Diagnostics

- Input: a selected subset, widget `.value`, or static keep/drop decision feeds the chart used to justify that same decision
- Expected: move the broad diagnostic upstream of the decision, record the human decision after validation, and keep downstream results separate from the evidence chart

## Scenario 10: Resist Demo / Presentation Drift

- Input: an exploratory notebook has dashboard-like `mo.vstack` / `mo.hstack` panels, multiple widget sections, staged reveal, and explanatory copy before raw diagnostics
- Expected: restore EDA order with raw rows, distributions, scatterplots, and validation cells first; remove app-like polish; keep only minimal local reversible controls that improve inspection

## Scenario 11: Repair Tiny Marimo Semantics Regressions

- Input:

```python
# Cell A
chart = build_chart(df)
chart

# Cell B
chart = build_other_chart(df)
chart
```

- Expected: use unique semantic exported names or underscore-local final expressions, avoiding duplicate global `chart`

- Input:

```python
# Cell A
slider = mo.ui.slider(0, 10)
mo.md(f"Selected: {slider.value}")
```

- Expected: display `slider` in Cell A and consume `slider.value` in an adjacent downstream cell

- Input:

```python
# Cell A
diagnostic_chart = build_chart(df)
```

- Expected: make `diagnostic_chart` the final expression, or use `_diagnostic_chart` as a local final expression if it is not reused downstream

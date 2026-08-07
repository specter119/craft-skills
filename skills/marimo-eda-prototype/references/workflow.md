# Workflow

## Default Order

1. Define the observation dataset and label any a priori constraints
2. Show a raw sample or compact overview before deriving interpretations
3. Add low-assumption diagnostics: scatterplots for relationships, histograms for distributions, box plots for group spread / outliers
4. Name the visible pattern or anomaly before interpreting it
5. Turn the pattern into a question, hypothesis, or candidate interpretation
6. Render the focused validation view for that question without conditioning it on the eventual decision
7. Use the smallest local reversible control for view changes; chart-native interaction is often the cleanest form for in-chart inspection
8. Let validated patterns motivate the human decision
9. Record the adopted decision as an explicit static input
10. Derive and display the selected result after the decision
11. Prefer plain code, plots, and batch steps with visible progress over cross-cell interaction
12. Add `mo.ui` only when interaction clearly improves exploration efficiency beyond plain code or chart-native inspection
13. Extract logic or UI only once it has stabilized or is being reused
14. Keep marimo's graph semantics intact: one intended visible output per cell, unique exported names, local underscore temporaries, and evidence dependencies upstream of decisions

## Hard Guardrails

### 1. Do Not Condition Evidence on Its Decision

- A chart used to justify a decision must not depend on that decision.
- Use broad, low-assumption diagnostics before narrow validation whenever the data shape is still unknown.
- Show the complete relevant candidate set before feature selection, exclusion, or ranking choices.
- Keep a priori constraints separate from decisions inferred from the current visualization.
- Prefer a plain static decision variable after the diagnostic view for human-reviewed decisions; export it with a unique semantic name only when downstream cells need it.
- Do not rewrite an EDA notebook into presentation order where the final decision silently selects which evidence is shown.

### 2. Do Not Turn the Notebook into Scattered UI Development

Watch for these signals:

- Multiple consecutive cells doing nothing but defining UI
- A simple exploration action split into many mutually dependent UI cells
- Interaction added just to "look more like a product", not for analysis efficiency
- Demo-like interactivity that makes the notebook more impressive but makes the analysis harder to reason about
- Presentation composition such as `mo.vstack` / `mo.hstack` used only to make the notebook look app-like

### 3. Keep UI Close to the Analysis It Controls

- Keep controls, derived results, and outputs adjacent. Compose one explicit output only for static objects or chart-native controls; `mo.ui` widgets should be displayed where defined and `.value` should be consumed in an adjacent downstream cell.
- Avoid defining a widget at the top and consuming it far below
- Avoid a parameter dependency chain so long it becomes hard to trace

### 4. Prefer Local View Lenses Over Notebook State

- If a human is only selecting a subgroup to inspect, keep the control local and reversible; chart-native interaction is often the cleanest form.
- Do not expose a selection as a marimo widget or global variable unless downstream cells genuinely need it.
- Treat reversible filtering as a lens on the evidence, not as a recorded decision.
- Avoid complex or cross-cell `mo.ui` orchestration in EDA; it is easy for the logic to become presentation/app-like.
- Use `mo.vstack` / `mo.hstack` sparingly; plain adjacent cells are usually clearer for EDA unless a local diagnostic bundle would otherwise split apart.

### 5. Only Export Stable Names

In marimo, exported non-underscore names are the cross-cell interface. By default, only expose:

- Data that needs to be reused by other cells
- Stable helper functions
- The primary result of the current cell

Use local names like `_tmp`, `_filtered`, `_chart` for intermediate values. Do not define the same exported name in multiple cells.

### 6. Abstract Only After a Pattern Stabilizes

These are typically extraction signals:

- The same UI / logic starts repeating
- A clear input/output boundary has formed
- Maintaining it requires a long cell or copy-paste
- You are already treating the notebook as an app source

## Pre-Completion Checklist

- Is the notebook's primary task still analysis?
- Does each decision follow the evidence used to support it?
- Is the notebook preserving discovery order rather than presenting a preselected conclusion?
- Does the notebook build initial data intuition before jumping to specific tests or decisions?
- Is any visualization filtered by the decision it is meant to justify?
- Are reversible exploration controls kept inside diagnostic views instead of exported as decisions?
- Does the UI genuinely improve exploration efficiency?
- Is each exploration action sufficiently concentrated?
- Are only names worth cross-cell reuse exposed?
- Is the intended output the final expression, or explicitly composed as one output?
- Are duplicate definitions, cycles, and downstream reads of `_` temporaries avoided?
- Is there anything that would be better moved to a module?

## Check Policy

When actually editing a marimo `.py` notebook, run `uvx marimo check notebook.py` when available. Treat `scripts/marimo_lint.py` as an optional structural smell checker, not a correctness gate.

```bash
uvx marimo check notebook.py
python scripts/marimo_lint.py notebook.py --json
```

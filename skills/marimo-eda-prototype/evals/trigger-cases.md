# Trigger Cases

## Should Trigger

1. Help me write a marimo notebook for exploratory data analysis.
2. I want to turn this analysis prototype into a lightweight interactive notebook without it becoming a complex app.
3. Optimize this marimo notebook's cell boundaries and UI density.
4. Refactor this EDA notebook so feature-selection plots show the evidence before manual exclusions.
5. Fix my marimo EDA notebook: `marimo check` reports duplicate definitions and a cyclic dependency.
6. Refactor this exploratory marimo notebook so cell outputs and exported names follow marimo graph rules.
7. 这个 marimo notebook 一个 cell 好像输出不对，帮我看下。
8. 帮我理一下这个 EDA notebook 的变量作用域和 cell 依赖。
9. 这个 EDA 太像 presentation/demo 了，帮我改回探索逻辑。
10. `mo.vstack` / `mo.ui` 是不是在这个 EDA 里用过了？
11. My marimo notebook errors because `slider.value` is read in the same cell where the slider is created.

## Should Not Trigger

1. Help me build a complete frontend application.
2. Fix a pandas bug in an ordinary Python script.
3. Write a Jupyter tutorial.
4. Teach me the full marimo API.
5. Explain Python LEGB scoping in a script.
6. Turn this completed analysis into a polished dashboard for end users.

## Near Neighbors

1. I have already decided to refactor the notebook into a formal module.
   Expected: no longer primarily depends on `marimo-eda-prototype`

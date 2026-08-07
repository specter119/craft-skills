# Optimization Notes

Date: 2026-06-22

## Current Assessment

The notebook/UI boundaries remain useful, but the skill lacked an explicit evidence-before-decision invariant. It could accept result-conditioned charts as long as the cells and UI were otherwise tidy.

## Follow-Up Actions

1. Add the `observations -> visualization -> decision -> result` invariant
2. Distinguish a priori constraints from decisions inferred from the current visualization
3. Add a feature-selection execution case that guards against result-conditioned evidence

## Follow-Up Assessment

Date: 2026-08-07

The `fsw_unified_desp/00_data_eval.py` reference showed a better high-participation EDA pattern: human inspection can be intense while still avoiding cross-cell marimo widget state. Its alloy selector is embedded inside the Altair diagnostic and acts as a reversible view lens, not as a downstream decision.

## Actions This Round

1. Add low-state, local controls as the preferred pattern for reversible subgroup inspection, with Altair / chart-native interaction as the best fit when the exploration stays inside one chart
2. Clarify that terminal scripts and persisted stage files are not default notebook rules; they are justified only by compute scale or provenance needs
3. Add an execution case for human exploration without app state

## Follow-Up Assessment

Date: 2026-08-07

EDA needs a different story logic from presentation. It should first create data intuition with raw rows, scatterplots, distributions, histograms, and box plots; then turn observed patterns into questions or hypotheses; then validate them with focused data-level analysis. Presentation can start from a conclusion, but exploratory notebooks should not.

## Follow-Up Actions

1. Add low-assumption first-pass diagnostics as part of the default EDA flow
2. Add discovery-first EDA narrative as an explicit invariant
3. Add an execution case for notebooks that jump directly to selected models, interpretations, exclusions, or feature subsets

## Follow-Up Assessment

Date: 2026-08-07

Basic marimo semantics belong inside the skill as thin design guardrails, not as an online-doc-only concern. One visible output, exported-name scope, duplicate definitions, private underscore temporaries, and reactive dependency direction directly affect whether an EDA notebook is runnable and whether evidence truly remains upstream of decisions.

## Follow-Up Actions

1. Add a concise marimo semantics reference for graph and output guardrails
2. Keep full widget, layout, and output API details delegated to official marimo docs
3. Add trigger and execution cases for duplicate definitions, cycles, output visibility, and decision-fed diagnostics

## Follow-Up Assessment

Date: 2026-08-07

Adversarial review found the design mostly sound but still too easy to misread in three ways: Altair could look like the principle rather than an example of a local reversible lens, module extraction still appeared too early, and some examples used generic global names or same-cell widget `.value` patterns that conflict with marimo graph semantics. Sub-documents also needed clearer roles: normal execution references should stay short and active; evals and reports are maintenance context.

## Follow-Up Actions

1. Demote Altair from principle to example and make local reversible inspection the rule
2. Replace module-first language with extraction-candidate language
3. Add Chinese trigger cases, demo/presentation anti-cases, and tiny marimo semantics anti-fixtures
4. Keep `mo.vstack` / `mo.hstack` as exceptional diagnostic bundling, not default EDA composition

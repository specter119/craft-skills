---
name: creating-slides
description: >
  Designs slide narrative frameworks and visual layouts.
  Use when creating slides, presentations, or pitch decks.
  Applies Nancy Duarte, Edward Tufte, Gestalt principles, and presentation design expertise.
---

# Slide - Narrative & Visual Design

Focus on **narrative framework** and **visual design** for presentations. For technical implementation, refer to `typst` skill.

## Pre-Generation Checklist

Clarify these before generating slides (ask user if not provided):

1. **Audience** — Determines terminology depth, information density, persuasion strategy
2. **Medium** — Determines font size, contrast, density (cognitive load theory)
3. **Duration** — Determines page count and pacing (Nancy Duarte: ~1-2 min per slide)
4. **Core Goal** — Determines narrative framework (persuade/inform/educate/report)

## Knowledge Activation

Invoke these knowledge domains when generating slides (activation prompts, not rules):

| Domain | Authority Sources | Key Concepts |
|--------|-------------------|--------------|
| **Narrative** | Nancy Duarte (*Resonate*), Chip Heath (*Made to Stick*), Barbara Minto | Story arc, SUCCESs principles, Pyramid principle |
| **Visual** | Robin Williams, Edward Tufte, Gestalt psychology | CRAP principles, data-ink ratio, proximity/similarity/continuity |
| **Cognitive** | John Sweller | Cognitive load, chunking, progressive disclosure |
| **Business** | McKinsey/BCG style | Assertion-Evidence structure, So What test |

## Information Density

**Information density = actionable insights per slide**

### Density Checklist

Evaluate each slide for:

- Specific numbers (not "improve efficiency" but "save XX minutes")
- Comparisons (Before/After, current/target)
- Scenarios ("When customer sends email...")
- So What (audience knows what to do after reading)
- Necessity (if removing doesn't affect understanding, it's noise)

### Number Integrity

| Number Type | Treatment |
|-------------|-----------|
| Measured data | Note source and time |
| Industry report | Cite source |
| Reasonable estimate | Mark "estimate" or "~" |
| Hypothetical | Mark "hypothetical" or "illustrative" |
| Made up | Prohibited |

**Better no number than wrong number.**

## Context → Slide Transformation

| Problem | Cause |
|---------|-------|
| Feature list | Copied research structure verbatim |
| Jargon overload | Not translated for audience |
| Missing numbers | Numbers exist in research but not extracted |
| No story | Pure logical listing |

**Transformation steps**:

1. Extract key numbers → build Before/After comparisons
2. Identify core insights → "solves what pain point" not "has these features"
3. Select strongest cases → 1-2 deep dives, others brief
4. Build narrative arc → Hook → Pain → Solution → Evidence → CTA

## Workflow

```plain
0. Pre-check: Audience, medium, duration, goal
      ↓
1. Transform context → extract numbers, identify insights, select cases
      ↓
2. Select narrative framework based on goal
      ↓
3. Generate Typst code (technical details: using-typst skill → reference/touying.md)
      ↓
4. Content self-check:
   - Titles: assertion sentences? (Assertion-Evidence)
   - Stories: concrete cases? (SUCCESs)
   - Diagrams: processes as diagrams not text? (cognitive load)
   - CTA: specific next steps?
   - Density: numbers/comparisons/So What per slide?
      ↓
5. Compile: tinymist diagnostics → typst compile
      ↓
6. Page validation: Grep title count → pdfinfo actual pages
   (details: using-typst skill → reference/touying.md "Page Validation")
      ↓
7. Visual check: pdftoppm → Read PNG → evaluate with design knowledge
      ↓
8. Iterate until all checks pass
```

## Visual Design Evaluation

After screenshot, evaluate using design knowledge (intuition, not checklist):

**Squint test**: After blurring vision, is the most important content seen first?

- If not → insufficient contrast (CRAP - Contrast)

**Whitespace test**: Is whitespace meaningful breathing room or filler for lack of content?

- Tufte: "data-ink ratio" — every drop of ink should convey information

**Rhythm test**: Flipping through 5 pages, is there visual variation?

- Nancy Duarte: "rhythm" — avoid monotonous repetition

**So What test**: After reading this slide, does audience know what to think/do?

- McKinsey: "one So What per slide"

## Narrative Framework Reference

| Goal | Framework | Source |
|------|-----------|--------|
| Business proposal | Problem-Solution-Impact | McKinsey/BCG consulting |
| Pitch deck | 10-20-30 rule | Guy Kawasaki |
| Case sharing | STAR method | Behavioral interview |
| Training | Story arc, STAR moments | Nancy Duarte |
| Technical proposal | Status-Challenge-Solution-Validation | Engineering culture |

These are references, not templates. Adapt based on content and audience.

## Skill Integration

```plain
[research skill] → gather information
       ↓
[creating-slides skill] → narrative + visual design
       ↓
[using-typst skill] → technical implementation
       ↓
[generating-images skill] → AI-generated illustrations
```

## GenImg Integration

Technical slides benefit from concept illustrations. Use `genimg` for:

### When to Use GenImg

| Scenario | Use GenImg | Use Diagraph/Code |
|----------|------------|-------------------|
| Abstract concepts (创新、协作、AI) | ✅ | ❌ |
| Emotional hook (cover image, section dividers) | ✅ | ❌ |
| Decorative elements (icons, backgrounds) | ✅ | ❌ |
| Logical flow (A→B→C) | ❌ | ✅ |
| System architecture | ❌ | ✅ |
| Data visualization | ❌ | ✅ |
| Comparison diagrams | ❌ | ✅ |

### Recommended Styles for Slides

| Slide Context | Style | Ratio |
|---------------|-------|-------|
| Cover/Title | `corporate`, `tech` | 16:9 |
| Section divider | `minimalist`, `flat` | 16:9 |
| Concept illustration | `illustration`, `isometric` | 4:3 or 1:1 |
| Icon/Badge | `icon`, `flat` | 1:1 |
| Background | `minimalist` with `-n "text"` | 16:9 |

### Workflow

```bash
# 1. Generate image
SCRIPT=~/.claude/skills/genimg/scripts/generate.py
uv run $SCRIPT "AI agents collaborating" -s tech -r 16:9 -o cover.png

# 2. Import in Typst
#image("cover.png", width: 100%)

# 3. Or use in slide grid
#grid(
  columns: (1fr, 1fr),
  image("concept.png", width: 90%),
  [Text content...]
)
```

### Quality Checklist

- [ ] Image supports narrative, not just decorative
- [ ] Style consistent across slides
- [ ] Resolution sufficient (use 16:9 for full-width)
- [ ] No text in generated images (Typst adds text)
- [ ] Concept clearly communicated

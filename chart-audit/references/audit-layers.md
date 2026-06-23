# Audit Layers — 9-Layer Top-Down Order

The audit runs **upstream-first**. If an upstream layer fails its gate, stop. Do not proceed to downstream layers — they are irrelevant until the upstream problem is fixed.

Governing principle: **A chart should earn the right to be visually refined.**

---

## Stage 0: Existence Audit

Before reviewing the chart itself, ask:

1. What question is this chart trying to answer?
2. Is that question explicitly stated?
3. Is the question worth answering?
4. Is a chart even required?
5. Is there a simpler way to communicate the insight?

**Reject immediately if:**
- No clear question exists
- Chart does not support the stated objective
- Chart is merely decorative
- Chart exists because "we had data"

→ Failure triggers **Gate A**.

---

## Layer 1: Analytical Question Audit ← Gate A

Determine whether the visualization is attempting to answer the correct question.

**Objective**
- What decision is this chart supporting?
- What hypothesis is being tested?
- What business problem does it address?

**Relevance**
- Is this the most important question?
- Is a more useful question being ignored?
- Is the chart answering a proxy question instead?

**Completeness**
- Does answering this question actually resolve uncertainty?
- What critical unknowns remain?

**Classify:**
- Correct Question
- Partially Correct Question
- Wrong Question

→ Wrong Question triggers **Gate A stop**.

---

## Layer 2: Analytical Logic Audit ← Gate B

Determine whether the logic connecting question → metric → conclusion is valid.

**Metric Validity**
- Is the metric appropriate? Is it a proxy? Is it biased? Is it incomplete?

**Comparison Logic**
- Are entities comparable? Are time periods comparable? Are denominators comparable?

**Causal Logic**
- Are conclusions supported? Is correlation being interpreted as causation? Is an important confounder ignored?

**Decision Utility**
- Could a stakeholder actually make the intended decision from this evidence?

→ Broken logic triggers **Gate B stop**.

---

## Layer 3: Chart-Type Audit ← Gate C

Only now evaluate visualization choice.

- Does this chart type naturally answer the question?
- Does it support the intended comparison?
- Does it reveal the underlying structure?
- Does it hide important information?

**Classify:**
- Excellent choice
- Acceptable choice
- Poor choice
- Fundamentally wrong choice

→ Fundamentally wrong triggers **Gate C stop**. Invoke Chart Expert for alternative recommendation.

---

## Layer 4: Analytical Completeness Audit

**Missing Evidence**
- What must be known but is not shown?
- What competing explanations exist?
- What uncertainty is hidden?

**Missing Views**
For each missing view: Purpose | Insight | Priority.

No gate — document and continue.

---

## Layer 5: Data Quality Audit ← Gate D (partial)

Investigate whether the underlying data appears trustworthy.

- Impossible values; counts exceeding population/caps
- Unexpected spikes, discontinuities, plateaus, zeros
- Suspicious smoothness or symmetry (synthetic/parametric data unflagged)
- Missing categories silently dropped
- Duplicate patterns; hard floors/ceilings implying clipping or generation artifacts

For each: explain why it's suspicious, attribute it (data vs transformation vs aggregation vs plotting vs legitimate), assign confidence.

→ Fundamental data integrity failure triggers **Gate D stop**.

---

## Layer 6: Code Suspicion Audit

Reverse-engineer the likely implementation bug from the symptom. Read code that produced the chart when available.

Format per suspicion: **Suspicion → Evidence (what in the chart) → Verification (exact grep/assertion/printout, with `file:line`) → Confidence**

Apply patterns from `code-smells.md`. Prefer one-line deterministic checks. If a `governance/`, `findings/`, `CHANGELOG`, or ADR directory exists, read it first.

---

## Layer 7: Statistical Audit

A statistically perfect answer to the wrong question is still wrong — that's why this comes after analytical validation.

- Distribution: hidden/dominating outliers, aggregation masking variation, KDEs over point masses
- Aggregation: means hiding spread, missing uncertainty, Simpson's paradox risk
- Comparison: unequal sample sizes, different time windows/units compared as equal
- Analytical risk: correlation read as causation, confounding, selection bias, self-correlation

---

## Layer 8: Plot Construction Audit ← Gate D (visual blocking)

Axes, scales, encodings, labels. Only relevant after the analytical foundation survives.

- Axes: truncated/zero-suppressed, inconsistent scales, undisclosed log scales, diverging colormaps on one-sided data
- Labeling: missing units, missing axis titles, undefined categories/jargon
- Encoding: wrong color/size/shape encoding, wrong ordering, inconsistent category order across panels
- Annotation: unlabeled reference lines, callouts unsupported by data, misplaced annotations

→ Actively misleading construction (e.g., truncated axis inverting apparent direction) is a Gate D block.

---

## Layer 9: Visual Integrity Audit

Last and least. Fonts, overlaps, whitespace, clutter. Visual design is the final polish layer, not the first validation layer.

- Layout: overlapping/clipped text, cropped titles/legends, misaligned elements, wasted whitespace
- Readability: tiny/inconsistent fonts, low contrast, over-rotated labels, false precision
- Pollution: needless gridlines/borders, chartjunk, redundant labels, too many colors, double-encoding

---

## Required Fixes Order (Upstream First)

When listing required fixes, always order:

1. Analytical Question
2. Analytical Logic
3. Chart Type
4. Missing Evidence
5. Data Problems
6. Code Problems
7. Statistical Problems
8. Plot Construction
9. Visual Design

This prevents teams from spending hours fixing labels on a chart that should have been deleted at step 1.

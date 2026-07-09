The current framework is optimized for **chart polishing**, not **analytical validation**.

It starts at the bottom of the causal chain:

```text
Fonts
 ↓
Layout
 ↓
Plot construction
 ↓
Statistics
 ↓
Data
 ↓
Code
 ↓
Chart choice
 ↓
Analytical question
```

This guarantees rework because you may spend time fixing a beautifully rendered chart that:

- answers the wrong question,
- uses the wrong metric,
- uses the wrong chart type,
- is built from incorrect transformations,
- or should not exist at all.

A better audit process follows the same direction as analytical production:

```text
Business / Research Question
        ↓
Analytical Logic
        ↓
Chart Choice
        ↓
Data
        ↓
Code
        ↓
Statistics
        ↓
Plot Construction
        ↓
Visual Design
```

If an upstream layer fails, downstream layers become largely irrelevant.

For example:

```text
Question:
"Did campaign A outperform campaign B?"

↓

Chart chosen:
Treemap

↓

Finding:
Treemap is inappropriate for comparison.

STOP.

Do not spend 20 minutes reviewing fonts,
axis labels,
or annotation placement.
```

---

# Recommended Audit Hierarchy

## Stage 0: Existence Audit (NEW)

Before reviewing the chart itself:

### Ask

1. What question is this chart trying to answer?
2. Is that question explicitly stated?
3. Is the question worth answering?
4. Is a chart even required?
5. Is there a simpler way to communicate the insight?

### Failure Conditions

Reject immediately if:

- no clear question exists
- chart does not support stated objective
- chart is merely decorative
- chart exists because "we had data"

This becomes the first gate.

---

# Layer 1: Analytical Question Audit

Determine whether the visualization is attempting to answer the correct question.

Ask:

### Objective

- What decision is this chart supporting?
- What hypothesis is being tested?
- What business problem does it address?
### Relevance

- Is this the most important question?
- Is a more useful question being ignored?
- Is the chart answering a proxy question instead?

### Completeness

- Does answering this question actually resolve uncertainty?
- What critical unknowns remain?

### Output

Classify:

- Correct Question
- Partially Correct Question
- Wrong Question

If wrong:
### Stop Condition

State:

> "The chart may be technically correct but answers the wrong question. Rebuild analytical framing before revising visualization."

---

# Layer 2: Analytical Logic Audit

Before looking at the chart type.

Determine whether the logic connecting question → metric → conclusion is valid.

Look for:

### Metric Validity

- Is the metric appropriate?
- Is it a proxy?
- Is it biased?
- Is it incomplete?

### Comparison Logic

- Are entities comparable?
- Are time periods comparable?
- Are denominators comparable?
    

### Causal Logic

- Are conclusions supported?
- Is correlation being interpreted as causation?
- Is an important confounder ignored?

### Decision Utility

Could a stakeholder actually make the intended decision from this evidence?

---

# Layer 3: Chart-Type Audit

Only now evaluate visualization choice.

Ask:

### Does this chart type naturally answer the question?
### Does it support the intended comparison?
### Does it reveal the underlying structure?
### Does it hide important information?

Classify:

- Excellent choice
- Acceptable choice
- Poor choice
- Fundamentally wrong choice

If fundamentally wrong:

State:

> "Further visual review has limited value until chart type is reconsidered."

---

# Layer 4: Analytical Completeness Audit

Ask:

### Missing Evidence

- What must be known but is not shown?
- What competing explanations exist?
- What uncertainty is hidden?

### Missing Views

What additional charts are required?

For each:
- Purpose    
- Insight
- Priority

---

# Layer 5: Data Quality Audit

Now investigate whether the underlying data appears trustworthy.

Current Layer 4 moves here.

---

# Layer 6: Code Suspicion Audit

Current Layer 5.

Now that we know the analysis itself is worth doing, inspect implementation risks.

---

# Layer 7: Statistical Audit

Current Layer 3.

Move statistics after analytical validation.

Reason:

A statistically perfect answer to the wrong question is still wrong.

---

# Layer 8: Plot Construction Audit

Current Layer 2.

Axes, scales, encodings, labels.
Only relevant after the analytical foundation survives.

---

# Layer 9: Visual Integrity Audit

Current Layer 1.

Fonts, overlaps, whitespace, clutter.

Last.

Reason:

Visual design is the final polish layer, not the first validation layer.

---

# Add Explicit Audit Gates

A major improvement would be introducing hard stop conditions:

## Gate A: Question Validity

Fail:

```text
Reject and Reframe
```

No further review required.

---

## Gate B: Analytical Logic

Fail:

```text
Reject and Redesign Analysis
```

No further review required.

---

## Gate C: Chart Type

Fail:

```text
Reject and Rebuild Visualization
```

Only high-level comments on remaining layers.

---

## Gate D: Data Integrity

Fail:

```text
Reject Pending Data Validation
```

Statistical and visual review become secondary.

---

# Priority of Fixes

Also change this section:

Current:

```text
Required Fixes
```

to

```text
Required Fixes (Upstream First)
```

ordered as:

1. Analytical Question
    
2. Analytical Logic
    
3. Chart Type
    
4. Missing Evidence
    
5. Data Problems
    
6. Code Problems
    
7. Statistical Problems
    
8. Plot Construction
    
9. Visual Design
    

```

This prevents teams from spending hours fixing labels on a chart that should have been deleted after step 1.

The governing principle should be:

> A chart should earn the right to be visually refined. First prove that the question is correct, the analytical logic is sound, the chart type is appropriate, and the underlying evidence is trustworthy. Only then optimize statistical presentation, plotting mechanics, and visual design.
```
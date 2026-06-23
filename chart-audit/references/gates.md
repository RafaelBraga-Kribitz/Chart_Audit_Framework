# Audit Gates — Hard Stop Conditions

Four hard gates enforce early-exit. When a gate fires, output the gate verdict and stop. Do not produce findings for downstream layers — they are irrelevant until the upstream problem is fixed.

---

## Gate A: Question Validity

**Fires when:** Layer 1 classifies the analytical question as **Wrong Question**, OR Stage 0 finds no defensible reason for the chart to exist.

**Verdict label:** `REJECT AND REFRAME`

**Output when Gate A fires:**
```
Gate A — REJECT AND REFRAME

The chart may be technically correct but answers the wrong question (or no question).
Rebuild analytical framing before revising visualization.

Finding: [state what question the chart actually answers, and what question it should answer]
Next step: [define the correct question; route to Chart Expert if chart type must also change]
```

**What NOT to do:** Do not comment on chart type, data quality, code, statistics, or visual design. They are all irrelevant until the question is right.

---

## Gate B: Analytical Logic

**Fires when:** Layer 2 finds a fundamental flaw in the logic chain connecting question → metric → conclusion. Examples: metric is a proxy for a different quantity than claimed, comparison is between non-comparable populations, causal conclusion has no causal evidence.

**Verdict label:** `REJECT AND REDESIGN ANALYSIS`

**Output when Gate B fires:**
```
Gate B — REJECT AND REDESIGN ANALYSIS

The analytical logic is broken. A correct visualization of a broken analysis misleads.
Redesign the analysis before touching the chart.

Finding: [state exactly which logic step fails and why]
Fix: [what must change in the analysis]
```

**What NOT to do:** Do not comment on chart type selection, code implementation, or visual styling.

---

## Gate C: Chart Type

**Fires when:** Layer 3 classifies the chart type as **Fundamentally Wrong** — meaning the chosen type structurally cannot answer the question, hides the relevant structure, or actively creates a false impression.

**Verdict label:** `REJECT AND REBUILD VISUALIZATION`

**Output when Gate C fires:**
```
Gate C — REJECT AND REBUILD VISUALIZATION

The chart type is fundamentally wrong for this question and data structure.
Further visual review has limited value until chart type is reconsidered.

Finding: [state what the current type does and why it fails]
Recommended alternative(s): [name the correct type(s); invoke Chart Expert for deterministic recommendation]
```

**What NOT to do:** Do not audit Layer 5 (data quality) or below in detail. A high-level note on any obvious data problems is acceptable, but full downstream audit is premature.

**Integration:** Gate C should trigger an invocation of the `chart-expert` skill with the current data shape and analytical function to get a deterministic replacement recommendation.

---

## Gate D: Data/Plot Integrity

**Fires when:** Either (a) Layer 5 finds a fundamental data integrity problem that invalidates the chart's numbers entirely (e.g., outcome anchoring confirmed, constraint violation confirmed, metric is measuring a completely different quantity), OR (b) Layer 8 finds actively misleading plot construction (e.g., truncated axis that inverts the apparent direction of a trend, stacked chart of mutually exclusive scenarios).

**Verdict label:** `REJECT PENDING DATA VALIDATION` (data trigger) or `BLOCK ON MISLEADING CONSTRUCTION` (plot trigger)

**Output when Gate D fires:**
```
Gate D — [REJECT PENDING DATA VALIDATION | BLOCK ON MISLEADING CONSTRUCTION]

[State the specific violation: what is wrong, confirmed at file:line if available]

Statistical and visual review are secondary until this is resolved.
Required fix: [concrete action — e.g., "fix the outcome anchor term at model.py:147 and regenerate"]
```

**Note:** Gate D does not prevent you from documenting Layer 7 (statistical) issues if they are already visible — but it blocks treating the chart as publishable.

---

## Gate Summary

| Gate | Layer | Label | Stops at |
|------|-------|-------|---------|
| A | 1 (Question) | REJECT AND REFRAME | Everything downstream |
| B | 2 (Logic) | REJECT AND REDESIGN ANALYSIS | Layers 3–9 |
| C | 3 (Chart Type) | REJECT AND REBUILD VISUALIZATION | Layers 5–9 (detailed) |
| D | 5/8 (Data/Plot) | REJECT PENDING DATA VALIDATION or BLOCK ON MISLEADING CONSTRUCTION | Treat as non-publishable |

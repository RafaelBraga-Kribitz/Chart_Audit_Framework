# Audit Framework — the 8 layers, the rubric, the template

Table of contents
1. The eight layers (what to look for in each)
2. Scoring rubric (the five 0–10 axes)
3. The "does this chart earn its place" test
4. Per-chart output template
5. Severity classification

---

## 1. The eight layers

Keep these strictly separate in the write-up. A single visual symptom often spans several; the
reader fixes each in a different place (the stylesheet, the model, the data loader, the chart-type
decision), so merging them destroys the fix.

### Layer 1 — Visual Integrity (the pixels themselves)
Layout: overlapping/clipped text, cropped titles/legends/labels, misaligned elements, watermark
collisions, wasted whitespace, legend parked over data. Readability: tiny/inconsistent fonts, low
contrast, same-color text on same-color fill, over-rotated labels, false precision. Pollution:
needless gridlines/borders, chartjunk, redundant labels/legends, too many colors, double-encoding
one variable into two channels.

### Layer 2 — Plot Construction
Axes: truncated/zero-suppressed axes, inconsistent or unequal scales, undisclosed log scales,
ranges that exaggerate, diverging colormaps applied to one-sided data. Labeling: missing units,
missing axis titles, undefined categories/jargon/codes, no definition of the measured quantity.
Encoding: wrong color/size/shape encoding, wrong or arbitrary ordering (especially alphabetical or
index order where magnitude is the point), inconsistent category order across panels. Annotation:
unlabeled reference lines, callouts unsupported by the data, misplaced annotations.

### Layer 3 — Statistical Integrity
Distribution: hidden or dominating outliers, compression, aggregation masking variation, KDEs drawn
over point masses/atoms (spike heights become meaningless). Aggregation: means hiding spread,
missing dispersion/uncertainty, Simpson's-paradox risk, over-aggregation. Comparison: unequal
sample sizes, different time windows/units compared as if equal, ranking quantities that are within
Monte-Carlo or sampling error of each other. Analytical risk: correlation read as causation,
confounding, selection/survivorship bias, missing baseline, self-correlation (plotting a ratio
against its own numerator or denominator).

### Layer 4 — Data Quality
Impossible values; counts exceeding population/caps; unexpected spikes, discontinuities, plateaus,
zeros; suspicious smoothness or symmetry (often = synthetic/parametric data unflagged); missing
categories silently dropped; duplicate patterns; hard floors/ceilings implying clipping or
generation artifacts. For each: explain why it's suspicious, attribute it (data vs transformation
vs aggregation vs plotting vs legitimate), and assign confidence.

### Layer 5 — Code Suspicion
Reverse-engineer the likely implementation bug from the symptom. State Suspicion → Evidence (what in
the chart) → Verification (the exact grep/assertion/printout that would confirm) → Confidence. See
`code-smells.md` for the catalogue.

### Layer 6 — Chart-Type Fit
Is the chosen type acceptable, merely adequate, or wrong? Name better alternatives (line, scatter,
histogram, density, box, violin, heatmap, slope, dumbbell, small multiples, facets, ridgeline,
ECDF, Sankey, network, treemap, mosaic) and say *what insight each improves* and *what weakness it
fixes*. ECDF is the default rescue for "distribution with atoms"; dot-plot-with-error-bars for
"ranked near-equal values"; slope/paired-bars for "two scenarios" (never stack alternatives).

### Layer 7 — Analytical Completeness
What's still unknown after this chart? What follow-up question does it raise? What competing
explanation isn't ruled out? What evidence is missing? Suggest follow-up charts with Purpose /
Insight / Priority.

### Layer 8 — Executive Communication
Could a decision-maker understand it quickly, trust it, and act on it? Watch the inversion where
confident-looking pixels carry the headline while the disqualifying caveat hides in a footnote,
JSON dump, or fine print. The caveat must live *in the exhibit*.

---

## 2. Scoring rubric (five axes, 0–10)

- **Visual Design** — layout, readability, restraint, absence of chartjunk. 8+ only if nothing
  clipped/colliding and encoding is clean.
- **Statistical Integrity** — does the picture faithfully represent the data and its uncertainty?
  Cap at 3 if a quantity within sampling/MC noise is presented as a real difference, or a ratio is
  plotted against its own component, or atoms are KDE'd.
- **Analytical Value** — does it answer a real question / support a decision? A chart can score high
  here *as a diagnostic* even when it's an ugly rendering of a defect (a good bug-finder earns it).
- **Communication Quality** — clarity and honesty to a stakeholder; penalize buried caveats.
- **Confidence in Correctness** — *your* confidence that the chart is right. Low when the producing
  code is unseen, when sibling charts contradict it, or when the result is "too clean." This axis is
  about epistemic status, not aesthetics.

---

## 3. The "earn its place" test (apply to every chart)

Ask, in order:
1. Does it convey something text/a table/a single statistic cannot (shape, geography, structure,
   interaction, uncertainty)? If no → recommend replacement by that sentence/table/stat.
2. Is the thing it conveys *real* (above noise, not self-correlated, not an artifact)? If no →
   Reject And Rebuild regardless of how polished it looks.
3. Is there another chart already in scope conveying the same insight better? If yes → recommend
   consolidation; flag the weaker one for removal.
4. Does it advance the project's central narrative (understanding / decision / causal reasoning /
   evidence quality)? If it's technically correct but inert → recommend removal.

A chart that fails 1, 2, or 4 should be removed or rebuilt even when its Visual score is high.
"Technically correct but inert" is a removal, not a pass.

---

## 4. Per-chart output template

```
## <chart id> — <title>

Verdict: <one sentence, the sharp summary>

Scores: Visual x/10 · Statistical x/10 · Analytical x/10 · Communication x/10 · Confidence x/10

Critical Issues
  (by layer; the ones that block publication or mislead)
Moderate Issues
Minor Issues

Possible Data Problems   (why suspicious · attribution · confidence)
Possible Code Problems   (Suspicion · Evidence · Verification [file:line or exact check] · Confidence)

Better Chart Options     (alternative · what it improves)
Follow-Up Charts         (purpose · insight · priority)

Narrative Contribution: <keep / keep-promoted / rework / remove / replace> — <reason>

Required Fixes (priority-ordered)

Final Assessment: <Approved | Approved With Revisions | Significant Rework Needed | Reject And Rebuild>
  <justification>
```

Across a whole project, also produce the cross-cutting section: contradictions between exhibits,
shared root causes (one bug poisoning N charts), duplication/version-hygiene, and a cull count
(of N exhibits, M earn their existence).

---

## 5. Severity classification

- **Critical** — misleads a reader, hides a constraint violation, presents noise/artifact as a
  finding, or contradicts another published exhibit. Blocks publication.
- **Moderate** — degrades trust or readability or omits needed context, but the core quantity is
  defensible once fixed.
- **Minor** — cosmetic; fix opportunistically.

When in doubt between Moderate and Critical, ask: "would a stakeholder make a worse decision because
of this?" If yes, it's Critical.

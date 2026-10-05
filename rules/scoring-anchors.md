# Scoring anchors — numeric thresholds for the five rubric axes

Companion to `chart-audit/references/scoring-rubric.md`. The rubric defines
five 0–10 axes; this table pins each axis to observable conditions so two
isolated chart-adversary sessions cannot score the same defect differently.
Rows are checked top-down; the FIRST matching row caps or floors the score.
Conditions reference rule ids from `rules/manifest.yaml`.

## Statistical Integrity

| Score band | Condition (observable) |
|---|---|
| ≤ 3 (cap) | Any Gate-D-class failure confirmed: SMELL-E (within-noise difference presented as real), SMELL-K (self-correlated ratio), or SMELL-G (atoms KDE'd) — this is the rubric's existing anchor, unchanged |
| ≤ 5 (cap) | SMELL-B, SMELL-C, or SMELL-H confirmed but disclosed on-chart (defect present, honestly annotated) |
| ≥ 8 (floor allowed) | No smell in {A,B,C,E,G,H,I,K} confirmed AND uncertainty is shown wherever an estimate is plotted |

## Visual Design

| Score band | Condition |
|---|---|
| ≤ 3 (cap) | Labels/marks clipped or colliding (illegible at export size), or a 3D/perspective distortion of a quantitative encoding |
| ≤ 5 (cap) | Legend is the sole decoder for >6 categories, or a colorblind-unsafe pair (red/green class) carries the only distinction between series |
| ≥ 8 (floor allowed) | Nothing clipped/colliding, ≤ 2 non-redundant encoding channels, direct labels where the form permits |

## Analytical Value

| Score band | Condition |
|---|---|
| ≤ 3 (cap) | Fails "Earn Its Place" step 1 or 2 (no real question, or a table/sentence conveys the same content) |
| ≤ 5 (cap) | Answers a real question but duplicates another exhibit's contribution (SMELL-M sibling overlap without contradiction) |
| ≥ 8 (floor allowed) | Chart is the decision-relevant answer to a stated question and no simpler exhibit conveys the same insight |

## Communication Quality

| Score band | Condition |
|---|---|
| ≤ 3 (cap) | A load-bearing caveat exists only outside the exhibit (footnote, appendix, JSON, commit message) |
| ≤ 5 (cap) | Caveat is on-chart but jargon-bound (a non-technical stakeholder would misread the conclusion) |
| ≥ 8 (floor allowed) | Caveats in-exhibit; a non-technical stakeholder reads the correct conclusion unaided |

## Confidence in Correctness

| Score band | Condition |
|---|---|
| ≤ 3 (cap) | Producing code unseen (Inferred-only), or a sibling artifact contradicts the chart (SMELL-M confirmed), or Gate D fired |
| ≤ 5 (cap) | Code seen but the plotted artifact could not be regenerated / lineage (run_id) unverifiable |
| ≥ 8 (floor allowed) | Confirmed at file:line, artifact regenerable, no contradiction found across sibling artifacts |

Scores between the capped and floored bands (4–7) remain judgment calls
inside the bounds these rows establish; the anchors bound the drift, they do
not eliminate judgment.

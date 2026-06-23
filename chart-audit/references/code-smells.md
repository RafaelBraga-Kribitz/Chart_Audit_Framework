# Code Smells — visual symptom → likely bug → how to confirm

Each entry: the **visual symptom** you can see in the figure, the **likely bug**, the **exact check**
to confirm it in code/data, and a default **confidence** when you see the symptom alone. These are
generalized from real audits; the verification step is what turns a guess into a finding.

---

## A. "Forecast" that lands exactly on the known outcome
**Symptom.** A time-series posterior whose mean terminates at the verified result and whose interval
funnels to implausibly narrow on the final date; a static "final-day" chart centered on an anchor
line.
**Likely bug.** The outcome is wired into the likelihood as a soft observation on the terminal
latent state — a *smoother/retrodiction* mislabeled as a *forecast*.
**Confirm.** Grep the model for the outcome value or an `*_anchor` / `observed=` term on the last
state, e.g. a `Normal("outcome_anchor", mu=mu[-1], sigma=σ, observed=m_star)`. Check that the
in-sample series and the walk-forward/out-of-sample series are *different objects* and that
walk-forward never sees the outcome.
**Confidence on symptom alone:** High.

## B. "Distribution" that is a flat line / zero variance across groups
**Symptom.** Box/violin/strip per group collapses to identical lines; y-axis auto-zoomed to a
microscopic range to fake separation.
**Likely bug.** A scalar aggregate is broadcast to every row instead of a per-draw computation; the
varying quantity (e.g. a shock) multiplies a *different* column than the one plotted.
**Confirm.** `df.groupby(group)[metric].std()` — if ~0, the metric never varied. Trace the column:
is it set once (`mean(...)`) and attached to all draws? Does the shock actually enter the plotted
metric's formula?
**Confidence:** High.

## C. Percentile interval mislabeled as "HDI" (and inconsistent levels)
**Symptom.** Bands/tables labeled "94% HDI" in one figure and "95% HDI" in another for the same
quantity; numbers differ between a forest plot and its table.
**Likely bug.** Intervals computed as `quantile(0.05)/quantile(0.95)` (a 90% *equal-tailed* interval)
but stored in columns named `hdi_low/high` and titled with yet another percentage; and/or two
different runs feeding two artifacts (SSOT drift).
**Confirm.** Read the export function: are low/high `quantile(...)` or `az.hdi(..., hdi_prob=...)`?
Do the figure title, the column name, and the table header agree on the level and the interval type?
Are both artifacts generated from one posterior object with a shared run id?
**Confidence:** High for the mislabel; Medium that two runs exist (confirm via run ids / timestamps).

## D. Ranked categories whose order is an array index, not a magnitude
**Symptom.** A ranked bar/dot chart where adjacent values differ by less than plausible noise, and
the order looks suspiciously like input order.
**Likely bug.** A tiny deterministic term tied to row index leaks into the score, e.g.
`z = base + noise + 0.001*i`, so "rank" encodes position in a list.
**Confirm.** Grep the score formula for `* i`, `+ i`, `enumerate`, or index arithmetic. Compute the
between-category spread vs the Monte-Carlo/sampling standard error (for a probability p over N draws,
SE ≈ sqrt(p(1-p)/N)); if the spread ≲ a few SE, the ranking is noise.
**Confidence:** Medium on symptom; High after seeing the `*i` term.

## E. Quantity that is within Monte-Carlo / sampling noise presented as a difference
**Symptom.** Win probabilities all in 49–51%; a diverging colormap or zero-suppressed bars
manufacturing visual contrast from a 1–2 pp spread.
**Likely bug.** A national scalar jittered per category with no real group-level model; noise term
dominates the systematic term.
**Confirm.** Inspect the generation: `z = a*(national - pivot) + noise`. With national ≈ pivot the
systematic term ≈ 0 and noise rules. Compute SE per category; compare to spread.
**Confidence:** High.

## F. Map that renders as a near-uniform block / overlapping boxes
**Symptom.** A "choropleth" that is one flat color field, sometimes with small boxes nested inside,
no recognizable geography.
**Likely bug.** Placeholder geometry — axis-aligned bounding-box rectangles (5-point polygons) that
overlap — combined with values confined to a narrow band rendered on a wide diverging scale.
**Confirm.** Load the GeoJSON: `len(features)` and points-per-feature; if every polygon has ~5
points it's a bounding box, not a border. Check the value range vs the colormap domain.
**Confidence:** High.

## G. KDE / density spikes of arbitrary height
**Symptom.** A "density" plot with towering thin spikes; legends literally saying "point mass = …".
**Likely bug.** KDE applied to a distribution containing atoms/point masses; spike height is a
bandwidth artifact and is not comparable across series; the one continuous series gets crushed.
**Confirm.** `value_counts()` on the variable — if a few values carry most mass, it's atomic.
**Fix (chart-type):** ECDF (atoms become clean vertical jumps) or labeled stems + histogram.
**Confidence:** High.

## H. Utilisation/coverage pinned at exactly 1.00 everywhere; "expected" exceeds the cap
**Symptom.** A utilisation heatmap that is wall-to-wall 1.00; a bars chart where "actual/expected"
towers over the "cap" in every category; caps that exceed the population.
**Likely bug.** The optimizer/computation ignored the constraint (wrong units, constraint not wired,
or value computed unconstrained then `min(x,1)`-clipped for display); "contacts" are impressions
(with frequency) mislabeled as people.
**Confirm.** Assert `value <= cap` per cell in the *pre-display* output; trace whether the cap is in
the optimizer's constraint set; compare contact totals to population. Look for a clip
(`np.minimum(util, 1.0)`) hiding the violation.
**Confidence:** High that a units/constraint bug exists.

## I. Stacked area/bars of mutually exclusive scenarios
**Symptom.** A stacked chart whose total exceeds any real-world total; legend lists alternative
*scenarios* (e.g., "baseline" + "counterfactual") as if they coexist.
**Likely bug.** `stackplot`/stacked bars used to "compare" scenarios that are alternatives, not
components — the stacked total is a fabricated number.
**Confirm.** Are the stacked series alternatives (only one obtains at a time)? If so they must be
overlaid lines / paired bars / a slope chart, never stacked.
**Confidence:** High.

## J. Silently dropped categories
**Symptom.** A chart shows fewer categories than the legend, the schema, or a sibling chart implies
(e.g., 3 channel types plotted, 4 budgeted; one panel missing two of its intent classes).
**Likely bug.** A `groupby`/filter/join dropped rows; a category with zero/NaN silently vanished;
inconsistent filters across sibling charts.
**Confirm.** Compare the plotted category set to the schema/contract and to sibling charts;
`set(expected) - set(plotted)`. Check joins for key mismatches.
**Confidence:** Medium–High.

## K. Self-correlated scatter (ratio vs its own component)
**Symptom.** A compelling "economies of scale" curve where y = a/b is plotted against b (or a), often
with the same variable also encoding bubble size and color.
**Likely bug.** Algebraic self-correlation; the structure is arithmetic, not empirical. Double/triple
encoding of one variable compounds it.
**Confirm.** Identify the axis/size/color definitions; if y contains x, the relationship is partly
mechanical. Re-plot against a normalized independent quantity (per-capita) to test.
**Confidence:** High.

## L. Suspiciously smooth / symmetric series
**Symptom.** An FX or time series with no realistic jitter; a perfectly symmetric early "prior" band.
**Likely bug.** Synthetic/parametric generation unflagged; early-window band is prior visualization,
not inference.
**Confirm.** Look for closed-form generation; check whether early dates predate any data. Label as
synthetic if so.
**Confidence:** Medium.

## M. Cross-artifact contradiction (the highest-value smell)
**Symptom.** Two exhibits disagree: a near-certain national result beside coin-flip departments; two
tables of the same parameter with different numbers; a composite that disagrees with its source;
three renderings of one "forecast" in different colors.
**Likely bug.** Stale runs, two pipelines sharing labels, missing run ids, narrative links that were
never wired (one module never actually reads another's artifacts).
**Confirm.** Diff the numbers; hunt for run ids / timestamps / model_version strings; check whether
the "integration" between stages is a real file read or just prose. Look in any governance/findings
log — the maintainers may already know.
**Confidence:** High that *something* is stale/unwired; the diff tells you which.

---

### General verification habits
- Prefer one-line, deterministic checks (`std`, `value_counts`, `set difference`, an `assert`).
- Always cite `file:line` once confirmed; downgrade to "inferred" otherwise.
- If a `governance/`, `findings/`, `CHANGELOG`, or ADR directory exists, read it first — known
  defects save time and tell you whether the *code* is fixed but the *figure* is stale.

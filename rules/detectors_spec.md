# Detector specifications (signature level)

Deterministic detectors for the mechanically checkable code smells. These are
interface contracts — no implementation ships with this document (see
`cli-spec.md` for the execution surface a future implementation must satisfy).
Every detector reports its result as a structured finding; when an LLM layer
also judges the same smell, both verdicts are reported as separate fields —
a detector result is never silently overridden.

Common output shape:

```
Finding = {
  smell: "B" | "C" | "J",
  fired: bool,
  evidence: str,          # human-readable, includes the offending values
  inputs_digest: str,     # hash of the inputs examined, for reproducibility
}
```

Common exit-code semantics (per detector invocation):
- `0` — ran cleanly, smell did not fire
- `1` — ran cleanly, smell fired
- `2` — input error (missing column, empty frame, malformed label); an input
  error is NEVER reported as "no smell"

---

## detect_flat_distribution — Smell B

```
detect_flat_distribution(df, group_col: str, metric_col: str,
                         std_threshold: float = 1e-9) -> Finding
```

Algorithm: compute `df.groupby(group_col)[metric_col].std()`. The smell fires
when EVERY group's standard deviation is below `std_threshold` while the
group count is ≥ 2 — a "distribution" chart of this data would render
variation that does not exist. Groups with a single row are reported in
`evidence` but do not by themselves fire the smell.

Errors (exit 2): `group_col`/`metric_col` missing, empty frame,
non-numeric `metric_col`.

Confirm step cross-reference: `code-smells.md#B` (grouped-std check).

## detect_interval_mislabel — Smell C

```
detect_interval_mislabel(declared_label: str,
                         computed_low: float, computed_high: float,
                         quantile_low: float, quantile_high: float,
                         level_tolerance: float = 0.005) -> Finding
```

Algorithm: parse `declared_label` for (a) interval TYPE ("HDI" vs
percentile/equal-tailed wording) and (b) nominal LEVEL (e.g. "95%"). Compare:
- type: if the computation used symmetric quantiles (`quantile_low +
  quantile_high == 1` within tolerance) but the label says "HDI", fire;
- level: implied level `quantile_high − quantile_low` must match the labeled
  level within `level_tolerance` (e.g. 0.03/0.97 labeled "95%" fires — it is
  94%).

Errors (exit 2): unparseable label (no percentage found), quantiles outside
(0,1), `computed_low > computed_high`.

Confirm step cross-reference: `code-smells.md#C` (label-vs-computation).

## detect_dropped_categories — Smell J

```
detect_dropped_categories(expected_categories: set[str],
                          plotted_categories: set[str]) -> Finding
```

Algorithm: `missing = expected_categories − plotted_categories`. Fires when
`missing` is non-empty; `evidence` names every dropped category. Extra
plotted categories (present but unexpected) are reported in `evidence` as a
warning without firing this smell.

Errors (exit 2): empty `expected_categories` (an empty expectation set means
the caller has no contract to check against — refuse rather than pass).

Confirm step cross-reference: `code-smells.md#J` (set-difference check).

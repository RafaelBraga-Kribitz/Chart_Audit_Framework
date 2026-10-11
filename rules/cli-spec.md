# CLI specification — chart-audit-rules

Interface contract for the deterministic rule layer's single entry point.
Implemented by `rules/chart_audit_rules.py` (stdlib + PyYAML) and gated in CI
by `.github/workflows/rules-engine.yml`, mirroring the target repo's
`scripts/check_*.py` exit-code convention.

Detector inputs: `--data <csv> --group-col G --metric-col M` (Smell B);
`--interval-labels <yaml>`, a list of `{declared_label, computed_low,
computed_high, quantile_low, quantile_high}` (Smell C);
`--expected-categories <txt> --plotted-categories <txt>`, one category per
line (Smell J). `--check-manifest` validates the manifest and
`COVERAGE_MATRIX.md` only; `--json` emits one finding per line.

## Invocation

```
chart-audit-rules <chart_path> <code_path> [--manifest rules/manifest.yaml]
                  [--expected-categories <file>] [--interval-labels <file>]
```

- `chart_path` — the rendered artifact under audit (png/svg/html).
- `code_path` — the generator source for that chart.
- Optional inputs supply the contracts the detectors need (expected category
  sets, declared interval labels with their computed quantiles).

## Behavior

1. Load `rules/manifest.yaml`; abort (exit 2) on unknown enforcement values,
   duplicate ids, or a detector entry whose spec is missing.
2. Run every `detector-backed` rule whose required inputs are available;
   skip-with-notice detectors whose inputs were not supplied (a skipped
   detector is reported as `skipped`, never as `clean`).
3. Emit one structured finding per executed detector (shape defined in
   `detectors_spec.md`), plus a summary line:
   `ran=<n> fired=<n> skipped=<n>`.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | All executed detectors clean (fired = 0); skips allowed but reported |
| 1 | At least one detector fired |
| 2 | Input/manifest error (missing manifest entry, malformed paths, missing required columns, unparseable labels) |

## Non-goals

- LLM-judged rules (see `COVERAGE_MATRIX.md`) are outside this CLI; their
  verdicts come from the chart-adversary agent and are merged at the report
  layer, never inside this process.
- No network access; inputs are local files only.

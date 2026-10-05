# Cross-repo audit ratchet (IMP-F03)

`ratchet.py` turns the chart-audit skill from "fresh audit every time" into a
regression ratchet against a decision-analytics-reconstruction checkout.

```
python3 ratchet/ratchet.py <target_checkout> [--state PATH] [--report PATH]
                           [--no-verify] [--rewind]
```

- **Input contract:** the target's `governance/FIGURE_MANIFEST.yaml`
  (`schema_version` handshake — unsupported/absent versions abort, exit 2)
  and `governance/findings/F-*.yaml`. The finding↔chart coverage lives in
  `finding_chart_map.yaml` here (schema-checked: unknown finding ids abort).
- **Routing per chart id:** `verify-only` (closed-finding coverage — the
  invariant script is the authority; failures report `REGRESSION of F-NNN`
  and exit 1, never file duplicates), `full-audit` (new/changed generator —
  chart-adversary LLM layers; rows carry `llm-judged` until `rules/`
  detectors are implemented), `skip` (unchanged + previously clean).
- **Granularity note:** generator hashing is file-level, so a change to the
  shared chart factory re-audits every non-invariant-covered chart it
  generates — conservative by design.
- **State:** `state.json` records per-chart generator hash, verdict, rule
  version, and the audited target commit; a run against an ancestor commit
  requires `--rewind`.

Measured on the target's 41-chart manifest: no-delta routing run 0.18 s;
full verify-only execution (15 unique invariant scripts, memoized) ~21 s.

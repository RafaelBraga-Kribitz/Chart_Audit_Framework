# Chart Audit Framework

![Chart Audit Framework: skill pack and read-only ratchet that routes each chart in a target repository to skip, re-verify, or re-audit.](docs/assets/hero.png)

[![Status: Foundation](https://img.shields.io/badge/status-Foundation-5A5C61?labelColor=26282C)](#status)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-5A5C61?labelColor=26282C)](LICENSE)

**Status:** Foundation

Python 3 · PyYAML · Apache-2.0 (author's files; third-party references excluded, see NOTICE)

Charts that look finished can still encode a flat distribution, a mislabeled interval, or a silently dropped category, and a fresh language-model audit of every figure cannot tell a closed finding from a regression. This framework is the skill pack and read-only ratchet that routes each chart to skip, re-verify, or re-audit against a target repository's figure manifest.

```mermaid
%%{init: {
  "theme": "base",
  "fontFamily": "BKribitz, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif",
  "themeVariables": {
    "background": "#E4E6EA",
    "primaryColor": "#DCDEE2",
    "primaryTextColor": "#26282C",
    "primaryBorderColor": "#26282C",
    "secondaryColor": "#E4E6EA",
    "secondaryTextColor": "#26282C",
    "secondaryBorderColor": "#5A5C61",
    "tertiaryColor": "#E4E6EA",
    "tertiaryTextColor": "#26282C",
    "tertiaryBorderColor": "#C2C4CA",
    "lineColor": "#5A5C61",
    "textColor": "#26282C",
    "mainBkg": "#DCDEE2",
    "nodeBorder": "#26282C",
    "clusterBkg": "#E4E6EA",
    "clusterBorder": "#C2C4CA",
    "edgeLabelBackground": "#E4E6EA",
    "titleColor": "#26282C",
    "fontFamily": "BKribitz, system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif",
    "fontSize": "14px"
  },
  "flowchart": { "curve": "linear", "htmlLabels": true, "padding": 8 }
}}%%
flowchart TD
  T[Target checkout<br/>FIGURE_MANIFEST + findings] --> R[ratchet.py]
  R -->|unchanged and previously clean| S[skip]
  R -->|closed-finding coverage| V[verify-only]
  R -->|new or changed generator| A[full-audit]
  V --> I[run the closed finding's invariant]
  I -->|script fails| X[REGRESSION of F-NNN / exit 1]
  I -->|script passes| P[exit 0]
  A --> L[chart-adversary LLM layers]
  L --> D[chart-audit-rules<br/>detectors B / C / J]
```

## The idea

Chart review is ordered **upstream-first** (question → logic → type → data/plot) with four hard gates. Three mechanically checkable smells have deterministic detectors (flat distribution, interval mislabel, dropped categories). The rest stay language-model judged, merged at the report layer, never inside the detector process.

The shipped executable is the **cross-repo ratchet**: it reads `governance/FIGURE_MANIFEST.yaml` and `governance/findings/F-*.yaml` from a [decision-analytics-reconstruction](https://github.com/RafaelBraga-Kribitz/decision-analytics-reconstruction) checkout, then routes each chart id:

| Route | When | What runs |
| --- | --- | --- |
| `skip` | generator hash unchanged and previously clean | nothing |
| `verify-only` | a closed finding covers the chart | that finding's `verification_script` is the authority |
| `full-audit` | new or changed generator | chart-adversary layers; rows marked `llm-judged` until `rules/` detectors exist |

A verify-only failure is reported as `REGRESSION of F-NNN` and exits 1. The ratchet does not file a duplicate issue.

## Project status

The improvement-plan register (`improvement_plan/INDEX.md`) lists IMP-F01–F04 as **done**. What is in this tree:

| ID | Title | In this tree |
| --- | --- | --- |
| IMP-F01 | Deterministic rule engine + numeric rubric anchors | `rules/detectors.py` (smells B, C, J) and the `rules/chart_audit_rules.py` CLI (exit 0/1/2, manifest and coverage-matrix validation), tested by `.github/workflows/rules-engine.yml`. |
| IMP-F02 | Chart-library verification pipeline | Curator path fixed; `chart-expert/scripts/validate_library.py` checks verified entries. |
| IMP-F03 | Cross-repo audit ratchet | `ratchet/ratchet.py` is present and is the only command documented here. |
| IMP-F04 | Repo hygiene | Legacy trees removed; `hygiene/check_repo_hygiene.py` gates duplicates outside the scraped site mirrors. |

No results exist yet from a fully deterministic audit: only smells B, C and J have detectors, and every other rule is still `llm-judged`.

## Quick start

Requires Python 3 and PyYAML. Point the ratchet at a target checkout that has `governance/FIGURE_MANIFEST.yaml` (`schema_version` 1) and `governance/findings/F-*.yaml`.

```bash
pip install pyyaml
python3 ratchet/ratchet.py <target_checkout> [--state PATH] [--report PATH]
                           [--no-verify] [--rewind]
```

- `--no-verify`: route only; do not execute the target's verification scripts.
- `--rewind`: required if the target HEAD is an ancestor of the commit recorded in `ratchet/state.json`.
- Unsupported or absent `schema_version` aborts (exit 2). Unknown finding ids in `ratchet/finding_chart_map.yaml` abort (exit 2).

Measured on the target's 41-chart manifest: no-delta routing 0.18 s; full verify-only (15 unique invariant scripts, memoized) ~21 s.

The detector CLI (`rules/chart_audit_rules.py`):

```
python3 rules/chart_audit_rules.py [chart_path] [code_path] [--manifest rules/manifest.yaml]
        [--data <csv> --group-col <col> --metric-col <col>]
        [--interval-labels <file>] [--expected-categories <file> --plotted-categories <file>]
python3 rules/chart_audit_rules.py --check-manifest
```

## Explore this project

| Path | Start here |
| --- | --- |
| Fast path | [The idea](#the-idea) and the workflow diagram above |
| Deep path | [Validation](#validation), [Architecture](#architecture), `rules/cli-spec.md`, `rules/detectors_spec.md`, `ratchet/README.md` |

## Validation

Acceptance is exit-code behaviour, not a published chart score.

**Ratchet** (`ratchet/ratchet.py`):

| Code | Meaning |
| --- | --- |
| 0 | Ran; no closed-finding regressions |
| 1 | At least one closed-finding `REGRESSION` |
| 2 | Input / manifest error (unsupported `schema_version`, missing manifest, mapping-table schema violation, backwards run without `--rewind`) |

**Detector CLI** (`rules/chart_audit_rules.py`, contract in `rules/cli-spec.md`):

| Code | Meaning |
| --- | --- |
| 0 | All executed detectors clean (`fired = 0`); skips allowed but reported |
| 1 | At least one detector fired |
| 2 | Input / manifest error |

A skipped detector is reported as `skipped`, never as `clean`. A detector result is never silently overridden by a language-model verdict. Input errors are never reported as "no smell."

Detectors (`rules/detectors.py`):

| Smell | Function | Fires when |
| --- | --- | --- |
| B | `detect_flat_distribution` | every group's `std` of the metric is below threshold and there are ≥ 2 groups |
| C | `detect_interval_mislabel` | declared interval type/level disagrees with the quantiles used |
| J | `detect_dropped_categories` | `expected − plotted` is non-empty |

## Architecture

```
target checkout                     this repository
─────────────────                   ────────────────
FIGURE_MANIFEST.yaml  ──reads──►    ratchet/ratchet.py
findings/F-*.yaml     ──reads──►        │
verification_script   ◄──runs──         │  verify-only
                                        │
                                   ratchet/state.json
                                   ratchet/finding_chart_map.yaml
                                        │
                                   rules/manifest.yaml     (registry)
                                   rules/detectors_spec.md (B, C, J)
                                   rules/chart_audit_rules.py (CLI)
                                        │
                                   chart-audit/            (LLM skill)
                                   chart-expert/           (LLM skill)
```

The ratchet is strictly read-only against the target. State (per-chart generator hash, verdict, rule-version hash, target commit) lives in `ratchet/state.json`. Generator hashing is file-level: a change to a shared chart factory re-audits every non-invariant-covered chart that factory generates.

Language-model judged rules stay outside `chart-audit-rules`; their verdicts come from the chart-adversary agent and are merged at the report layer. The CLI has no network access.

IMP-F01 is the dependency for the ratchet's detector path. IMP-F03 can already route and re-verify closed findings without those detectors. IMP-F02 and IMP-F04 do not block IMP-F03.

## Limitations

- **Most of the rule registry is language-model judged.** Detector-backed today: smells B, C, J. Gates A–D and smells A, D–I, K–M have no deterministic detector.
- **The ratchet does not write the target.** Reopening a regressed finding is the target repository's governance action.
- **Coverage is only what the manifest names.** Charts absent from `FIGURE_MANIFEST.yaml` are not routed.
- **File-level dirty detection is conservative.** Editing a shared generator re-audits every chart it produces that is not verify-only.
- **No CI for the ratchet itself.** The four workflows cover the README quality gate, the chart-expert library (generators `--check` plus `chart-expert/scripts/validate_library.py`), the rules engine (`rules/test_rules_engine.py` and `--check-manifest`) and repository hygiene; `ratchet/ratchet.py` has no automated test run in this repository.

What would change this status: deterministic detectors for more of the registry than smells B, C and J, and automated tests for `ratchet/ratchet.py`.

## Stack

| Technology | Role |
| --- | --- |
| Python 3 standard library | Detectors (`rules/detectors.py`) and the hygiene check; CI runs Python 3.12 |
| PyYAML | Reads `FIGURE_MANIFEST.yaml`, findings, `rules/manifest.yaml` and the ratchet map |
| `unittest` | `rules/test_rules_engine.py` |
| Claude Code skills | `chart-audit/` (adversary) and `chart-expert/` (chart selection), the language-model judged layers |
| GitHub Actions | Four workflows: README quality, chart-expert library, rules engine, repository hygiene |

## Versioning

There is no release tag and no package version yet; pin this framework by commit. The
ratchet records the rule-version hash and the audited target commit in
`ratchet/state.json`, and refuses a backwards run without `--rewind`.

## Repository structure

```
chart-audit/           Adversary skill: 9 layers, gates A–D, code smells
chart-expert/          Chart-selection skill, chart library, authored measure library
rules/                 Rule registry, detectors, CLI, anchors
hygiene/               Repo hygiene check (IMP-F04)
ratchet/               Cross-repo ratchet (the runnable entry point)
improvement_plan/      IMP-F01–F04 specifications (register: done)
docs/design-history/   Why the audit is top-down
```

## Status

**Status:** Foundation

Last described against `improvement_plan/INDEX.md`, `ratchet/README.md`, `rules/cli-spec.md`, and `rules/detectors_spec.md`.

Repository last updated 2026-10-11.

## License

Apache-2.0. See [`LICENSE`](LICENSE). Third-party material bundled in this repository is listed in [`NOTICE`](NOTICE) and is not covered by that grant.

## Author

<table>
  <tr>
    <td width="110">
      <img
        src="docs/assets/Author_MDS_Rafael_Braga-Kribitz_kroped.png"
        alt="Rafael Braga-Kribitz"
        width="96"
      />
    </td>
    <td>
      <strong>Rafael Braga-Kribitz</strong><br />
      Seiersberg-Pirka, Austria · Portfolio project, 2026<br />
      <a href="https://www.linkedin.com/in/rafaelbragakribitz/">LinkedIn</a>
      ·
      <a href="mailto:rafaelbragakribitz@gmail.com">rafaelbragakribitz@gmail.com</a>
    </td>
  </tr>
</table>

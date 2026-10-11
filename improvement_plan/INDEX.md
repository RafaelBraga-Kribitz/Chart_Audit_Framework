# Improvement Plan — Chart_Audit_Framework (IMP-F series)

Specification documents for this repository's slice of the cross-repo
statistical/analytical improvement plan. The **master index** — phase plan,
dependency graph, 59-code traceability matrix, and acceptance criteria —
lives in the companion repository:
`decision-analytics-reconstruction/governance/improvement_plan/INDEX.md`.
Document format is defined by `governance/improvement_plan/TEMPLATE.md`
there.

These documents are specifications, not code. They execute through GitHub
Issues in this repository (plus one companion issue in
decision-analytics-reconstruction for IMP-F03).

## Register

| ID | Title (short) | Pri | Effort | Depends on | Issue | Status |
|---|---|---|---|---|---|---|
| IMP-F01 | Deterministic rule engine + numeric rubric anchors | P1 | high | — | #1 | done |
| IMP-F02 | Chart-library verification pipeline (fire the curator loop, fix its path) | P2 | high | soft: F01 | #2 | done |
| IMP-F03 | Cross-repo audit ratchet (manifest + findings state, deltas only) | P1 | medium | F01; soft: repo-1 IMP-V02 | #3 (+ companion decision-analytics-reconstruction#71) | done |
| IMP-F04 | Repo hygiene (delete legacy trees, single-source refs, design history) | P2 | low | — | #4 | done |

Register reconciled 2026-10-11 against the tree:
- IMP-F01 — `rules/detectors.py` (smells B/C/J), `rules/chart_audit_rules.py`
  (CLI, manifest + coverage-matrix validation) and
  `.github/workflows/rules-engine.yml`; spec, anchors and matrix were already
  in `rules/`.
- IMP-F02 — curator `library_root` resolves repo-locally
  (`chart-expert/agents/library-curator.md`); first verified entry with
  `source_file` provenance; `validate_library.py` checks verified entries.
- IMP-F03 — `ratchet/ratchet.py` consumes the target's FIGURE_MANIFEST
  `schema_version` + findings state and audits deltas only.
- IMP-F04 — legacy trees deleted, design history in `docs/design-history/`,
  single-sourced references, WordPress plugin/theme trees removed. The
  zero-duplicate invariant was amended (2026-10-11) to exempt groups lying
  entirely inside the scraped site mirrors; the one duplicate outside them
  (an unreferenced `references/IMGs/` copy of a mirror image) was deleted.
  Gate: `hygiene/check_repo_hygiene.py` (`.github/workflows/repo-hygiene.yml`).

Audit-code traceability (CF1–CF7 → docs) is maintained in the master
index's matrix; this register does not duplicate it.

## Sequencing

IMP-F01 first — it converts the prose methodology into executable rules and
is the dependency for the ratchet (IMP-F03). IMP-F04 (hygiene) and IMP-F02
(library verification) are independent fillers; F02 benefits from F01's
detectors but is not blocked by them. IMP-F03 additionally wants repo 1's
IMP-V02 (full manifest lineage) before its coverage is complete, but can
ship against partial coverage.

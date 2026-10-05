---
id: IMP-F03
title: "Cross-repo audit ratchet: consume decision-analytics-reconstruction's manifest and findings state; audit deltas only"
absorbs: [CF5]
overlaps_triage: []
priority: P1
effort: medium
depends_on: [IMP-F01]
soft_depends_on: [IMP-V02]
queue: issues
target_repo: Chart_Audit_Framework
issue: 3            # companion issue in decision-analytics-reconstruction: #71
status: draft
---

# IMP-F03 — Cross-Repo Audit Ratchet

Nothing in `chart-audit/` or `chart-expert/` programmatically reads the
target repository's governance state. The single-chart sub-agent's pre-flight
(`chart-audit/agents/chart-adversary.md:20-26`) instructs an LLM to manually
read `governance/findings/F-*.yaml`, `reports/epistemic_boundaries.md`, and
`governance/FIGURE_MANIFEST.yaml` on every invocation. Consequences:

- every audit session starts from scratch and can re-litigate defects the
  target repo's governance already closed (F-053..F-067 and successors);
- there is no dirty-detection — unchanged charts get re-audited at full cost
  while a changed generator can slip through between sessions;
- audit output is not keyed to the target's chart identities, so results
  can't accumulate into a ratchet the way the target repo's own Adversary
  job does.

This document specifies the adapter that turns the framework from
"fresh audit every time" into a regression ratchet. It depends on IMP-F01
(the rule engine that makes checks executable) and soft-depends on the
target repo's IMP-V02 (100% manifest lineage coverage — the ratchet can ship
against partial coverage but only ratchets what the manifest names).

## 1. Define the Scope (The Data Guardrails)

**In-Scope:**
- An **input contract** for the ratchet, read from the target repo checkout:
  (a) `governance/FIGURE_MANIFEST.yaml` — chart id → generator path →
  artifact path (+ `run_id` where present); (b) findings state — the set of
  closed findings with their `verification_script` paths and the chart ids
  they cover (derivable from the finding YAMLs' evidence/notes fields via an
  explicit mapping table maintained in this repo, not guessed).
- **Skip/verify/audit routing** per chart id:
  `verify-only` for charts covered by a closed finding (run/require the
  finding's invariant instead of re-auditing); `full audit` for new charts
  or charts whose generator content hash changed since the last ratchet
  run; `skip` for unchanged, previously-clean charts.
- A **ratchet state file** (in this repo or emitted alongside the audit
  report) recording, per chart id: last audited generator hash, verdict,
  rule versions used — so consecutive runs are incremental.
- **Output contract:** audit report keyed by chart id, each finding row
  naming the rule id (IMP-F01 registry) that fired, filable through the
  existing `chart-audit/references/github-issue-template.md` unchanged.
- A **companion issue in the target repo** (filed with this one): expose a
  stable read surface — manifest schema version field and a documented
  guarantee that chart ids are stable identifiers — so the adapter has
  something versioned to parse.

**Out-of-Scope:**
- The rules themselves (IMP-F01).
- Any write access to the target repo — the ratchet is read-only against
  the target, mirroring the target's own Adversary discipline.
- Auditing artifacts the target manifest does not name (dashboard live
  views, notebooks) until the target's IMP-V02 brings them under lineage.

## 2. Data-Driven "Given-When-Then" Scenarios

**Scenario: Incremental run on an unchanged repo (Happy Path)**
- **Given** a ratchet state file from a prior run and a target checkout
  where no chart generator changed,
- **When** the ratchet runs,
- **Then** every previously-clean chart is `skip`, every
  closed-finding-covered chart is `verify-only` (its invariant script exits
  0), no full audits execute, and the run completes in under a minute —
  the report says "no deltas" rather than re-printing old findings.

**Scenario: Changed generator (Happy Path)**
- **Given** a target checkout where one chart's generator section changed
  (content hash differs from the ratchet state),
- **When** the ratchet runs,
- **Then** exactly that chart routes to `full audit` (rule-engine
  execution + LLM layers where rules don't cover), the report keys the
  results to its chart id, and the state file updates its hash and verdict.

**Scenario: Regressed closed finding (Edge Case)**
- **Given** a chart covered by a closed target finding whose
  `verification_script` now exits non-zero on the current checkout,
- **When** the ratchet runs,
- **Then** the report flags `REGRESSION of F-NNN` for that chart id —
  distinct from a new finding — and does NOT file a duplicate issue for the
  underlying defect; the regression row points at the target's own reopen
  procedure (AUDIT_PROCEDURE.md), respecting that reopening is the target
  repo's governance action, not this framework's.

**Scenario: Manifest schema drift (Edge Case)**
- **Given** a target checkout whose FIGURE_MANIFEST schema version is newer
  than the adapter supports (or the version field is absent),
- **When** the ratchet loads it,
- **Then** it aborts with a named incompatibility error before auditing
  anything — a misparsed manifest must never produce a silently partial
  audit.

## 3. Specify Undesirable Behaviors (Negative Constraints)

**Scenario: Preventing re-litigation of closed findings**
- **Given** any chart whose defect class is covered by a closed target
  finding with a passing invariant,
- **When** the ratchet produces its report,
- **Then** it must not emit a new finding for that same defect class on
  that chart — the closed finding's invariant is the authority; disagreement
  with the invariant's sufficiency is raised as a comment on the mapping
  table, not as a duplicate audit finding.

**Scenario: Preventing unkeyed audit output**
- **Given** any finding row in the ratchet's report,
- **When** it is emitted,
- **Then** it carries a chart id from the manifest and a rule id from the
  IMP-F01 registry (or an explicit `llm-judged` marker with the layer
  name); free-floating prose findings with neither are a failing output.

**Scenario: Preventing hidden state divergence**
- **Given** the ratchet state file,
- **When** any run completes,
- **Then** the state file records the target repo commit hash it audited;
  a subsequent run against an older commit than the state's must warn and
  require an explicit `--rewind` acknowledgment rather than silently
  ratcheting backwards.

## 4. Detail Data-Specific Non-Functional Requirements

- **Model fairness / bias:** N/A — audit tooling.
- **Performance & decay:** incremental no-delta run < 1 minute; full-repo
  cold run bounded by the target's chart count (27 currently) at ≤ ~2 min
  per chart for the rule-engine portion (LLM layers excluded from this
  budget and clearly separated in the report).
- **Data integrity:** the adapter validates manifest entries (generator
  path exists, artifact path exists where committed) and reports dangling
  entries as manifest defects rather than crashing; the
  finding↔chart mapping table is schema-checked (every finding id must
  exist in the target checkout).
- **Reproducibility:** given the same target commit, rule versions, and
  state file, two ratchet runs produce identical reports (LLM-judged layers
  are marked non-deterministic and excluded from the identity requirement,
  per IMP-F01's rule/LLM coverage split).

## 5. Queue Stub (ready to file)

This document files **two issues** — the primary in this repo, a companion
in the target repo.

**Issue 1 (this repo — Chart_Audit_Framework):**

> **Title:** Cross-repo audit ratchet: consume the target's FIGURE_MANIFEST + findings state, audit deltas only (IMP-F03)
>
> **Problem.** `chart-adversary.md:20-26` has an LLM manually re-read the
> target repo's governance files on every invocation; nothing programmatic
> consumes `FIGURE_MANIFEST.yaml` or the closed-findings state, so every
> audit restarts from scratch and can re-litigate F-053..F-067.
>
> **Acceptance criteria.**
> 1. Adapter reads manifest + findings state from a target checkout;
>    routing per chart id: skip / verify-only / full-audit (generator-hash
>    dirty detection).
> 2. Ratchet state file with per-chart hash, verdict, rule versions, target
>    commit; backwards runs require explicit acknowledgment.
> 3. Report rows keyed by chart id + rule id; closed-finding regressions
>    flagged as `REGRESSION of F-NNN`, never duplicate-filed.
> 4. Manifest schema-version handshake; abort on unsupported/absent version.
> 5. No-delta incremental run < 1 min on the target's current 27-chart set.
>
> **Blocked by:** IMP-F01 (rule engine) — `status:blocked` until it closes.
>
> **Spec:** `Chart_Audit_Framework/improvement_plan/IMP-F03_cross-repo-ratchet.md`

Labels: `type:feature`, `skill:infra`, `effort:medium`, `priority:p1`,
`status:blocked`

**Issue 2 (companion, decision-analytics-reconstruction):**

> **Title:** Expose a versioned read surface for the chart-audit ratchet: FIGURE_MANIFEST schema version + stable chart ids (IMP-F03 companion)
>
> **Problem.** `governance/FIGURE_MANIFEST.yaml` has no schema-version field
> and no documented stability guarantee for chart ids, so external tooling
> (Chart_Audit_Framework's ratchet, IMP-F03) has nothing versioned to parse.
>
> **Acceptance criteria.**
> 1. `schema_version` field added to FIGURE_MANIFEST.yaml with a documented
>    bump policy.
> 2. Chart ids documented as stable identifiers (rename = retire + add).
> 3. One-paragraph consumer contract note in the manifest header naming
>    what external read-only consumers may rely on.
>
> **Spec:** `Chart_Audit_Framework/improvement_plan/IMP-F03_cross-repo-ratchet.md`

Labels: `type:governance`, `skill:infra`, `effort:low`, `priority:p1`,
`status:claude-ready`

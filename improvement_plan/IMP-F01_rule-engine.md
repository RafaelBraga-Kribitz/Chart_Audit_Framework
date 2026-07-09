---
id: IMP-F01
title: "Deterministic rule engine: executable detectors and numeric rubric anchors"
absorbs: [CF1, CF4]
overlaps_triage: []
priority: P1
effort: high
depends_on: []
soft_depends_on: []
queue: issues
target_repo: Chart_Audit_Framework
issue: 1
status: filed
---

# IMP-F01 — Deterministic Rule Engine

`chart-audit/` and `chart-expert/` contain **zero executable code**. The
entire methodology — 9 audit layers (`chart-audit/references/audit-layers.md`),
4 hard gates A–D (`chart-audit/references/gates.md`), and 13 code smells A–M
(`chart-audit/references/code-smells.md`, 9155 bytes of prose) — is Markdown an
LLM sub-agent must interpret fresh on every invocation. The one place the
framework gestures at determinism, `chart-expert/references/input-type-schema.md:380-425`,
defines a `def auto_select_chart(data: DataFrame) -> str:` function under the
heading "Pseudo-Code for Claude Skill" (line 380) — it is never imported,
never called, and has no test. There is no CI entry point anywhere in the
repository (no `.github/workflows/*.yml`, no `scripts/`, no `Makefile`),
in contrast to `decision-analytics-reconstruction`'s `scripts/check_*.py`
exit-code-gated pattern that the Adversary CI job (`.github/workflows/governance.yml`
in that repo) invokes per finding.

Separately, `chart-audit/references/scoring-rubric.md` defines five 0–10 axes
(Visual Design, Statistical Integrity, Analytical Value, Communication
Quality, Confidence in Correctness) and a severity rule (Critical/Moderate/
Minor), but only **one** axis has a concrete numeric anchor: "Cap at 3 if a
quantity within sampling/MC noise is presented as a real difference..."
(Statistical Integrity). The other four axes are qualitative prose ("Score
8+ only if nothing is clipped/colliding") with no cross-session-stable
threshold table. Two different chart-adversary invocations (necessarily
context-isolated per `chart-audit/SKILL.md`'s "fresh sub-agent invocation
with no shared context" guarantee) can score the same defect a 4 or a 7 on
Statistical Integrity with no way to detect the drift — this is exactly the
cross-session inconsistency `decision-analytics-reconstruction`'s governance
system (`CLAUDE.md`, "Anti-patterns (banned)") was built to eliminate, just
manifesting in the sister repo instead.

## 1. Define the Scope (The Data Guardrails)

**In-Scope:**
- A `rules/` manifest at the framework root: a machine-readable registry
  (one entry per rule) mapping `id` → `{smell_id | gate_id}`, `detector_signature`,
  `inputs` (chart artifact / dataframe / code path), and `pass_fail_semantics`.
  Schema only in this document — no implementation.
- Detector specifications (signature + inputs + expected exit semantics, not
  code) for the three mechanically-checkable smells named in the parent audit:
  - **Smell B** (flat-distribution / zero-variance groups,
    `chart-audit/references/code-smells.md` §B) — detectable via
    `df.groupby(group)[metric].std() ≈ 0`, exactly the "Confirm" step
    already written in prose at that section.
  - **Smell C** (interval mislabel, §C) — detectable by comparing the label
    string ("94% HDI") against the actual computation
    (`quantile(0.05)/quantile(0.95)` is a 90% equal-tailed interval, not an
    HDI at any level).
  - **Smell J** (silently dropped categories, §J) — detectable via
    `set(expected_categories) - set(plotted_categories)` against a schema or
    sibling chart, the same "Confirm" step already documented.
- A numeric anchor table for all five scoring-rubric axes (not just
  Statistical Integrity), each anchor keyed to an observable condition (gate
  fired, smell confirmed, specific check failing) rather than an adjective.
- A single CLI entry point (name and interface only, e.g.
  `chart-audit-verify <chart_dir>`) returning a process exit code (0 = no
  detector fired, 1 = at least one detector fired, 2 = detector error) so a
  CI job can gate on it the way `decision-analytics-reconstruction`'s
  Adversary job gates on `scripts/check_*.py`.
- A rule-coverage matrix: for each of the 13 smells (A–M) and 4 gates (A–D),
  whether a detector exists or the item remains LLM-judged-only.

**Out-of-Scope:**
- Detectors for smells that are inherently narrative/contextual and cannot
  be reduced to a deterministic check without a live model object or
  domain judgment (Smell A — outcome anchoring, requires reading model code
  semantics; Smell M — cross-artifact contradiction, requires narrative
  understanding). These remain LLM-judged and the coverage matrix must say
  so explicitly rather than silently omitting them.
- Any change to the 9-layer ordering or the 4-gate definitions themselves —
  this spec adds executable teeth to the existing methodology, it does not
  redesign it (per `CLAUDE.md`'s ban, inherited by this framework's
  companion repo, on inventing a new methodology).
- The chart-library verification pipeline (stub → verified transitions) —
  that is IMP-F02.
- Actually writing the detector code — this document is the specification;
  writing and merging the code is the PR that closes the resulting GitHub
  issue.

## 2. Data-Driven "Given-When-Then" Scenarios

**Scenario: Deterministic detection of a flat-distribution smell (Happy Path)**
- **Given** a chart artifact whose underlying dataframe has a `group` column
  and a `metric` column, and `df.groupby("group")["metric"].std()` is
  `< 1e-9` for every group,
- **When** the Smell-B detector runs via the CLI entry point,
- **Then** it exits non-zero, emits a structured finding
  `{smell: B, confidence: high, evidence: "std=<value> for all groups"}`,
  and this result is identical across repeated runs and across different
  chart-adversary sessions — no LLM judgment call is involved in the
  detection step (an LLM may still be invoked to explain *why* the metric
  never varied, but not to decide *whether* it varied).

**Scenario: Rubric anchor disagreement across sessions (Edge Case)**
- **Given** two independent chart-adversary invocations auditing the same
  chart with a confirmed Gate-D data-integrity failure,
- **When** each session scores the Statistical Integrity axis using the
  anchor table from this spec (which states "≤3 iff any Gate-D failure
  confirmed"),
- **Then** both sessions produce a score in the same anchored range (0–3),
  eliminating the drift possible today where the same defect could score a
  4 in one session and a 7 in another under the current prose-only rubric.

## 3. Specify Undesirable Behaviors (Negative Constraints)

**Scenario: Preventing detector/prose disagreement**
- **Given** a chart that a Smell-B detector marks as passing (no flat
  distribution) but that a chart-adversary sub-agent's prose judgment
  flags as suspicious,
- **When** the finding is emitted,
- **Then** the report must surface both the detector result and the LLM
  judgment as separate fields — the detector result must never be silently
  overridden by prose narrative, and a disagreement must be flagged for
  human review rather than resolved by whichever ran last.

**Scenario: Preventing coverage-matrix drift**
- **Given** a new smell or gate added to `code-smells.md` or `gates.md` in a
  future PR,
- **When** that PR is reviewed,
- **Then** the rule-coverage matrix in `rules/` must be updated in the same
  PR to list the new item as either detector-backed or explicitly
  LLM-judged-only — an undocumented item (neither detector nor
  explicitly-marked-manual) is a failing state for this spec's acceptance.

## 4. Detail Data-Specific Non-Functional Requirements

- **Model fairness / bias:** N/A — this framework audits chart artifacts and
  code, not a scored population; no protected-attribute exposure.
- **Performance & decay:** the CLI entry point must run the mechanically-
  checkable detectors (B, C, J) in under 5 seconds per chart on a typical
  chart-plus-dataframe input, so it is cheap enough to run in a pre-PR hook
  or lightweight CI job analogous to `decision-analytics-reconstruction`'s
  `make verify`. The rule-coverage matrix's detector-vs-judged ratio is the
  decay metric to monitor: if it does not increase over subsequent sessions,
  the self-improvement claim in `chart-expert/SKILL.md` ("Self-Improvement
  Loop") has no analog on the audit side and that gap should be re-raised.
- **Data integrity:** detectors must fail loudly (non-zero exit, explicit
  error field) on malformed input (missing `group`/`metric` columns, empty
  dataframe) rather than silently returning "no smell detected."
- **Reproducibility:** every detector must be a pure function of its inputs
  (dataframe + chart metadata) — no reliance on session-local state, so that
  re-running the same detector on the same chart between the Remediator and
  the Adversary role (mirroring `decision-analytics-reconstruction`'s
  three-role protocol) always agrees.

## 5. Queue Stub (ready to file)

```markdown
## Problem statement
The chart-audit and chart-expert skills define a 9-layer audit, 4 hard gates,
and 13 code smells entirely in prose (chart-audit/references/audit-layers.md,
gates.md, code-smells.md) with the only pseudo-code in the framework
(chart-expert/references/input-type-schema.md:380-425, `def
auto_select_chart(...)`) never implemented or tested. There is no CI entry
point anywhere in the repo. Separately, scoring-rubric.md's five 0-10 axes
have only one numeric anchor (Statistical Integrity "cap at 3"); the other
four are qualitative, so two isolated chart-adversary sessions can score an
identical defect differently with no way to detect the drift.

## Evidence
- chart-audit/references/code-smells.md (9155 bytes, 13 prose smells A-M, no code)
- chart-expert/references/input-type-schema.md:380-425 (pseudo-code, never called)
- chart-audit/references/scoring-rubric.md (5 axes, 1 numeric anchor)
- chart-audit/SKILL.md ("fresh sub-agent invocation with no shared context" — isolation that makes drift undetectable without a shared numeric anchor)
- No .github/workflows/, scripts/, or Makefile in this repo (contrast decision-analytics-reconstruction's scripts/check_*.py + governance.yml Adversary job)

## Acceptance criteria
- [ ] `rules/` manifest exists with an entry per smell/gate, mapping to detector signature or "LLM-judged-only"
- [ ] Detectors specified (signature-level) for Smell B, C, and J
- [ ] Numeric anchor table exists for all five scoring-rubric axes, not just Statistical Integrity
- [ ] A single CLI entry point spec returns documented exit codes (0/1/2)
- [ ] Rule coverage matrix committed, listing detector-backed vs LLM-judged items for all 13 smells + 4 gates

## Verification
Manual review of the rules/ manifest and coverage matrix against
code-smells.md and gates.md — every smell/gate must appear exactly once,
tagged detector-backed or LLM-judged-only. No automated verification script
exists yet in this repo (there is no CI); writing that script is a
follow-on task, not a blocker for closing this issue, since this issue's
acceptance criteria are documentation/spec artifacts (the manifest and
matrix), not the detector implementations themselves.

## Spec
See Chart_Audit_Framework/improvement_plan/IMP-F01_rule-engine.md for full scope, scenarios, and non-functional requirements.
```

Labels: `type:refactor`, `skill:infra`, `effort:high`, `priority:p1`, `status:claude-ready`

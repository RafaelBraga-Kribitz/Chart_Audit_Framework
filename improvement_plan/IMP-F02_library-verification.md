---
id: IMP-F02
title: "Chart-library verification pipeline: fire the self-improvement loop"
absorbs: [CF2, CF3]
overlaps_triage: []
priority: P2
effort: high
depends_on: []
soft_depends_on: [IMP-F01]
queue: issues
target_repo: Chart_Audit_Framework
issue: 2
status: filed
---

# IMP-F02 — Chart-Library Verification Pipeline

`chart-expert/SKILL.md` promises a "Self-Improvement Loop": "the library's
`verified` implementation count increases with every session." The observed
state contradicts that promise on every axis:

- **Zero verified entries.** All 129 files under `chart-expert/library/CHARTS/`
  carry `status: stub` in their `implementations` front matter; `grep -rl
  "status: verified"` returns 0 files. Every one of the 903
  tool-implementation stanzas across the library is
  `{status: stub, source_file: null, last_iterated: null}` — e.g.
  `chart-expert/library/CHARTS/Comparison/bar-chart.md:18-24`, which lists
  seven tools (matplotlib, plotly, altair, d3, tableau, powerbi, excel), all
  stub, all `source_file: null`. The library-curator agent designed to flip
  these has never fired: `last_iterated: null` everywhere, and the single
  substantive commit in the repo's history (72b6387, "Reorganize repo...")
  created the stubs in the state they remain in today.
- **The curator writes to the wrong place.**
  `chart-expert/agents/library-curator.md:9` declares the agent "write-only
  on the library at `~/.claude/skills/chart-expert/library/`" — a
  user-global install path. The library actually lives repo-locally at
  `chart-expert/library/`. If the skill is run from a repo checkout (the
  only mode this repository's layout supports), a faithful curator would
  write updates into a `~/.claude` tree that the repo never sees, and the
  committed library would stay at 0/129 forever — silently, because nothing
  checks the two locations against each other.

## 1. Define the Scope (The Data Guardrails)

**In-Scope:**
- **Path resolution (CF3).** Amend `chart-expert/agents/library-curator.md`
  so the library path is either (a) a parameter the caller must supply
  (`library_root`, defaulting to the repo-local `chart-expert/library/`
  relative to the SKILL.md that invoked it), or (b) standardized on exactly
  one install mode with the other explicitly declared unsupported. The spec
  requires that a curator invocation can never succeed while writing outside
  the tree that `chart-expert/SKILL.md` Step 2 reads its indices from.
- **Verification protocol.** For each library entry: render the chart type
  with a small reference dataset matching the entry's `input_type` (e.g.
  `cat-value` for bar-chart), confirm the render succeeds without exception
  and produces a non-empty artifact, capture the working snippet into the
  entry's `Implementation Notes.<tool>` section, then flip the front matter
  to `{status: verified, source_file: <path>, last_iterated: <date>}` —
  i.e., execute the exact Situation-1 update already specified in
  `library-curator.md:36-51`, but actually run it, with provenance.
- **Priority order.** Verify first the ~15 chart forms actually consumed by
  the companion repo `decision-analytics-reconstruction` (its
  `governance/FIGURE_MANIFEST.yaml` enumerates the published figures: bar,
  grouped/stacked bar, heatmap, histogram/KDE, box/violin, scatter, line,
  ECDF, forest/interval plot, biplot, choropleth, and the small set of
  bespoke forms in its reports). Verifying matplotlib (that repo's tool)
  before plotly/altair/d3/tableau/powerbi/excel.
- **Progress metric.** A `verified/129` counter (per tool and overall)
  maintained in `chart-expert/library/_INDICES/` or a new
  `library/_INDICES/verification-index.md`, regenerated on every curator
  write (the "After Any Write" step at `library-curator.md:135-137` already
  requires index regeneration; this adds one more index to that step).

**Out-of-Scope:**
- Writing the executable render-check harness itself — if IMP-F01's rule
  engine lands first, the verification runner should reuse its CLI/exit-code
  conventions (hence `soft_depends_on: [IMP-F01]`), but this spec does not
  block on it: manual verification sessions that follow the protocol and
  commit provenance are acceptable.
- Adding new chart types to the library or editing the prose content of
  entries (Description / When to Use / Best Practices) beyond pasting the
  verified snippet.
- The retrieval flow (`chart-expert/SKILL.md` Steps 1–5) — this spec changes
  what `implementations.status` says, not how candidates are ranked, except
  that Step 4's existing preference for `status == verified` finally starts
  discriminating once at least one entry is verified.

## 2. Data-Driven "Given-When-Then" Scenarios

**Scenario: First verified entry with provenance (Happy Path)**
- **Given** the reference dataset for `cat-value` (a small categorical/
  numeric frame) and the library entry
  `chart-expert/library/CHARTS/Comparison/bar-chart.md` at
  `{status: stub, source_file: null}` (its current lines 18–24),
- **When** the verification protocol runs for the matplotlib tool,
- **Then** a rendered artifact exists, the working snippet is committed
  into the entry's `Implementation Notes.matplotlib` section, the front
  matter reads `{status: verified, source_file: <committed snippet path>,
  last_iterated: <ISO date>}`, and the verification index reports
  `matplotlib: 1/129` — all inside the repo-local `chart-expert/library/`
  tree, verifiable with `git diff`.

**Scenario: Curator invoked from a repo checkout (Edge Case)**
- **Given** a Chart Expert session running against a clone at an arbitrary
  path (not `~/.claude/skills/`),
- **When** the post-render curator invocation (`chart-expert/SKILL.md`
  Step 7) fires,
- **Then** the curator resolves `library_root` to the repo-local
  `chart-expert/library/` of the invoking checkout, its write lands in that
  tree (observable as an uncommitted `git status` change), and no file is
  created or modified under `~/.claude/skills/chart-expert/library/`.

## 3. Specify Undesirable Behaviors (Negative Constraints)

**Scenario: Preventing silent wrong-location writes**
- **Given** any future curator invocation,
- **When** the resolved library path does not contain the entry named by
  `library_path` (e.g. the caller passed a repo-local path but the agent
  prepended `~/.claude/...`),
- **Then** the curator must abort with an explicit error naming both paths,
  rather than creating a new file at the wrong location — a curator write
  that does not show up in `git status` of the working checkout is a failing
  state, never a success.

**Scenario: Preventing verification-by-assertion**
- **Given** a library entry whose status is being flipped to `verified`,
- **When** the flip is reviewed (PR diff),
- **Then** the same diff must contain the non-null `source_file` reference
  and the captured snippet in `Implementation Notes.<tool>` — a bare
  `status: stub` → `status: verified` edit with `source_file: null` left in
  place is the chart-library equivalent of the "closed without a passing
  verification_script" anti-pattern banned in the companion repo's
  CLAUDE.md, and must be rejected in review.

**Scenario: Preventing index drift**
- **Given** any PR that changes one or more `implementations.status` fields,
- **When** the PR is reviewed,
- **Then** the verification index must be regenerated in the same PR;
  an index that disagrees with `grep -c "status: verified"` over
  `library/CHARTS/` is a failing state.

## 4. Detail Data-Specific Non-Functional Requirements

- **Model fairness / bias:** N/A — reference datasets are synthetic fixture
  frames chosen for shape (input_type), not for any population semantics.
- **Performance & decay:** each single-entry verification (render + capture
  + flip) should complete in one short session; the progress metric
  `verified/129` must be monotonically non-decreasing — a verified entry
  reverting to stub requires an explicit rationale in the commit message
  (analogous to reopening a closed finding in the companion repo). Target:
  the ~15 priority forms verified for matplotlib before any long-tail form
  is attempted.
- **Data integrity:** reference datasets are committed fixtures (deterministic
  content, no network fetch); a render that emits an empty (0-byte) or
  exception-aborted artifact must not flip status.
- **Reproducibility:** verified snippets must run against the committed
  fixture with a fixed seed where randomness exists (jitter, sampling), so
  re-running the snippet reproduces the artifact byte-stably or within an
  explicitly documented tolerance.

## 5. Queue Stub (ready to file)

```markdown
## Problem statement
The chart-expert library's self-improvement loop has never fired: 0 of 129
chart entries are verified. Every entry is `status: stub` with
`source_file: null` in all tool stanzas (903 stanzas total). Worse, the
library-curator agent that is supposed to flip these targets the wrong
path — `~/.claude/skills/chart-expert/library/` — while the library lives
repo-locally at `chart-expert/library/`, so even a faithful curator run
would write its updates where the repo never sees them, silently.

## Evidence
- chart-expert/library/CHARTS/Comparison/bar-chart.md:18-24 — seven tool stanzas, all `{status: stub, source_file: null, last_iterated: null}`
- `grep -rl "status: verified" chart-expert/library/CHARTS` → 0 files; `grep -rl "status: stub"` → 129 files
- chart-expert/agents/library-curator.md:9 — "write-only on the library at `~/.claude/skills/chart-expert/library/`" (path mismatch)
- chart-expert/SKILL.md "Self-Improvement Loop" — "the library's `verified` implementation count increases with every session" (contradicted by 0/129)
- git log: the stubs are unchanged since commit 72b6387 created them

## Acceptance criteria
- [ ] library-curator.md path resolution fixed: `library_root` parameterized (default repo-local) or one install mode standardized with the other declared unsupported
- [ ] Verification protocol documented in the curator or a sibling reference: render with fixture → capture snippet → flip status with non-null source_file + last_iterated
- [ ] Priority list committed: the ~15 chart forms used by decision-analytics-reconstruction, matplotlib first
- [ ] At least the first priority entry (bar-chart) verified end-to-end as the protocol's proof case
- [ ] Verification index exists under library/_INDICES/ reporting verified/129 per tool, regenerated on every status flip

## Verification
`grep -rc "status: verified" chart-expert/library/CHARTS/` must be >= 1 and
must equal the count reported by the verification index; the flipped
entry/entries must have non-null source_file and a committed snippet in
Implementation Notes; `git log` must show no writes targeting ~/.claude
paths.

## Spec
See Chart_Audit_Framework/improvement_plan/IMP-F02_library-verification.md for full scope, scenarios, and non-functional requirements.
```

Labels: `type:feature`, `skill:shared`, `effort:high`, `priority:p2`, `status:claude-ready`

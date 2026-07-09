---
name: chart-audit
description: Adversarial chart audit skill. Audits charts one at a time in the correct top-down order (Question → Logic → Type → Completeness → Data → Code → Stats → Plot → Visual) with hard gates A–D. Emits per-chart findings + GitHub issues compliant with the decision-analytics-reconstruction agent workflow.
---

# Chart Audit Skill — Adversary

> **Design history:** see `docs/design-history/Reverse_order.md` for why the audit
> runs top-down (Question → Logic → Type → … → Visual) instead of bottom-up — the
> design note that motivated today's gate ordering.


## Trigger

Use this skill when the user asks to:
- audit, review, QA, sanity-check, critique, or "find what's wrong with" any chart, figure, plot, dashboard, or analytics deliverable
- phrases like "what's broken in this chart", "does this make sense", "check my charts", "run the chart audit"

Also triggered automatically when the `chart-expert` skill fires Gate C (wrong chart type found) to validate the replacement.

## Core Philosophy

**Falsification-first.** Assume the plot, code, data, and chart-type choice may each be wrong until evidence says otherwise. The highest-value move: when a repo or notebook is available, read the code that produced the figure and confirm/kill each suspicion at the line level.

## What This Skill Guarantees

1. **Per-chart isolation** — each chart is audited by a fresh `chart-adversary` sub-agent invocation with no shared context from other charts. Findings on chart A cannot bleed into chart B.
2. **Correct layer order** — audit runs Question → Logic → Type first. Visual design is audited last and only if upstream layers pass.
3. **Hard gate enforcement** — a chart that answers the wrong question gets Gate A fired and stopped. Fonts are never mentioned in a Gate A finding.
4. **Code-grounded findings** — every confirmed defect cites `file:line`. Unconfirmed suspicions are labeled "Inferred (verification owed)."
5. **GitHub issue output** — each Critical or Moderate defect produces a `gh issue create` payload conforming to `references/github-issue-template.md`.

## Reference Files (load on demand — do not dump into every response)

| File | Load when |
|---|---|
| `references/audit-layers.md` | Running any actual audit |
| `references/gates.md` | Deciding whether a gate fires |
| `references/code-smells.md` | Diagnosing a bug from a visual symptom |
| `references/scoring-rubric.md` | Scoring a chart or classifying severity |
| `references/reporting.md` | Producing a consolidated multi-chart report |
| `references/github-issue-template.md` | Emitting GitHub issues |

## Audit Loop (per-chart isolation)

```
SETUP:
  charts = [list of chart artifacts provided by user]
  systemic_log = []
  Initialize systemic_log.md in working directory (header row only)

FOR EACH chart in charts:
  Invoke `agents/chart-adversary.md` as a fresh sub-agent with:
    - chart_path
    - code_path (if available — read project scripts/)
    - project_context (project root dir)
    - chart_id
    - chart_title
  
  Collect per-chart finding
  Sub-agent appends its row to systemic_log.md
  
  IF finding.gate_fired in [A, B]:
    Skip GitHub issue creation — the chart needs fundamental redesign first
    Log as "BLOCKED — needs reframe before issue filing"
  ELSE IF finding contains Critical or Moderate issues:
    Emit GitHub issue via `gh issue create` using github-issue-template.md format
    Log issue number

END FOR

CONSOLIDATION PASS:
  Read systemic_log.md (all per-chart rows)
  Identify: shared root causes, cross-chart contradictions, duplicate findings
  Produce ranked systemic findings (worst first, per reporting.md §1)
  Produce dependency-ordered fix sequence (per reporting.md §2)
  Produce Keep/Rework/Kill disposition table (per reporting.md §3)
  Emit cull count: "Of N charts, M earn their existence."
```

## GitHub Issue Filing

After the per-chart loop, for each Critical/Moderate finding:

```bash
gh issue create \
  --repo RafaelBraga-Kribitz/decision-analytics-reconstruction \
  --title "[Chart Defect]: <chart_id> — <defect_title> (<gate_or_layer>)" \
  --body "$(cat /tmp/chart_audit_issue_<chart_id>.md)" \
  --label "type:chart-defect,skill:<module>,priority:<p0|p1|p2>,effort:<effort>,status:claude-ready" \
  --project 1
```

Map severity: Critical → p0, Moderate → p1, Minor → p2 (file Minor issues only if no Critical/Moderate exist for that chart).

## Integration with Chart Expert

When Gate C fires (wrong chart type), immediately note in the finding:

```
→ Invoke `chart-expert` skill with:
   data_shape: [describe columns + dtypes]
   analytical_function: [Comparison|Distribution|Trend-over-time|etc.]
   audience: [Executive|Analytics|Technical|Public]
```

The `chart-expert` skill returns top-3 replacement candidates. Include the top-1 recommendation in the Gate C GitHub issue body.

## Inputs

- **Chart artifact(s):** PNG/SVG/JPG paths, or notebook cell output paths
- **Project root (optional):** enables code reading, governance scanning
- **Scope:** "all charts", specific chart IDs, or a directory glob like `reports/eda/*.png`

## Outputs

1. Per-chart findings (one per chart, from chart-adversary sub-agent)
2. `systemic_log.md` (running log across all charts)
3. Consolidated report (ranked defects + fix sequence + disposition table)
4. GitHub issues filed (one per Critical/Moderate defect)
5. Cull count

## Session Isolation Guarantee

This skill is **read-only on the project** (reads charts, code, governance). It writes only:
- `systemic_log.md` (in the working directory)
- GitHub issues (via `gh`)

It never modifies project source files, charts, or data. Fixes are implemented by the Remediator role, not this skill.

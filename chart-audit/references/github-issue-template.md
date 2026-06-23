# GitHub Issue Template — Chart Defect

Issues created by the `chart-audit` skill must conform to the `decision-analytics-reconstruction` project's Agent Workflow Guide schema. This ensures issues appear in `.claude/agent_queue.json` and are auto-closeable by CI.

---

## Required Labels (all four must be present for queue inclusion)

| Label group | Options |
|---|---|
| `type:` | `type:chart-defect` |
| `skill:` | `skill:module-a` / `skill:module-b` / `skill:module-c` / `skill:shared` |
| `priority:` | `priority:p0` (Critical) / `priority:p1` (Moderate) / `priority:p2` (Minor) |
| `effort:` | `effort:low` / `effort:medium` / `effort:high` |
| `status:` | `status:claude-ready` (add when spec is complete and actionable) |

Severity → priority mapping: Critical → p0, Moderate → p1, Minor → p2.

---

## Issue Title Format

```
[Chart Defect]: <chart_id> — <short defect title> (<gate or layer>)
```

Examples:
- `[Chart Defect]: A3 — Treemap used for comparison question (Gate C)`
- `[Chart Defect]: B7 — KDE over point masses, spike heights meaningless (Layer 7 / Smell G)`
- `[Chart Defect]: C2 — Outcome anchored in likelihood, mislabeled as forecast (Layer 5 / Smell A)`

---

## Issue Body Template

```markdown
## Problem statement
<!-- One paragraph: what is wrong with this chart and why it matters to decisions. -->

## Chart details
- **Chart ID:** <!-- e.g., A3 -->
- **Chart file:** <!-- e.g., reports/eda/A3_segment_composition.png -->
- **Producing script:** <!-- e.g., scripts/module_a/generate_eda.py:147 (or Unknown) -->
- **Gate fired:** <!-- None | A | B | C | D -->
- **Layers affected:** <!-- e.g., Layer 3 (Chart-Type), Layer 7 (Statistical) -->

## Scores
- Visual: x/10 · Statistical: x/10 · Analytical: x/10 · Communication: x/10 · Confidence: x/10

## Defect detail
<!-- Suspicion → Evidence (what in the chart) → Verification (exact check / file:line) → Confidence -->

## Root cause
<!-- Inferred or confirmed bug at file:line. Reference code smell ID if applicable (A–M). -->

## Fix
<!-- Concrete steps ordered upstream-first. -->
1. 
2. 

## Acceptance criteria
- [ ] <!-- Specific verifiable outcome 1 -->
- [ ] <!-- Specific verifiable outcome 2 -->
- [ ] Chart regenerated and disposition upgraded to Approved or Approved With Revisions

## Disposition
<!-- Keep | Rework | Kill -->

## Narrative contribution
<!-- keep / keep-promoted / rework / remove / replace — one sentence reason -->

## Related findings
<!-- Link sibling issues or governance/findings/F-NNN.yaml if applicable -->
```

---

## CLI Command

```bash
gh issue create \
  --repo RafaelBraga-Kribitz/decision-analytics-reconstruction \
  --title "[Chart Defect]: <chart_id> — <title> (<gate/layer>)" \
  --body "$(cat issue_body.md)" \
  --label "type:chart-defect,skill:<module>,priority:<p0|p1|p2>,effort:<low|medium|high>,status:claude-ready" \
  --project 1
```

---

## Queue Requirements

For the issue to appear in `.claude/agent_queue.json`:
1. Must have ALL of: `type:*`, `skill:*`, `priority:*`, `effort:*` labels
2. Must have `status:claude-ready` label
3. Body must have `## Acceptance criteria` heading with `- [ ]` checkboxes
4. PR closing the issue must have `Closes #NNN` or `Fixes #NNN` in the body for auto-close

---

## Effort Estimation for Chart Defects

| Defect type | Typical effort |
|---|---|
| Visual/label fix only | low |
| Chart type swap (data unchanged) | medium |
| Pipeline/data bug fix + regen | high |
| Gate A/B — analytical redesign | high |

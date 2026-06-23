# Reporting — consolidated report + disposition table

When the audit covers more than a handful of charts, or the user asks for a project-level view,
produce three things in this order.

## 1. Ranked defects (top N)
A numbered list, worst first. Each entry:
- **Title** (short, memorable: "Outcome anchoring", "Dead MC engine", "Segment label mapping").
- **Severity** and **blast radius** (how many exhibits/decisions it poisons).
- **Confirmed at** (`file:line`) or **Inferred** (with the verification still owed).
- **Why it matters** in one line (the decision that goes wrong).
- **Linked finding id** if the repo already tracks it.

Rank by: (decisions corrupted) × (confidence it's real) × (number of exhibits affected), with a
bump for anything that *contradicts another published exhibit* or *presents an artifact as a
finding*.

## 2. Dependency-ordered fix sequence
Fixes are not independent. Order them so upstream truth is established before downstream charts are
regenerated. The canonical shape:
1. **Identity/label layer** (e.g., cluster→name mapping) — cheapest, unblocks the most.
2. **Single-source-of-truth / run hygiene** (pick a canonical run, stamp run ids, regenerate from
   one posterior/allocation object) — stops contradictions from reappearing.
3. **Estimand/likelihood correctness** (anchoring, objective function, constraint enforcement,
   unit definitions) — the substance.
4. **Pipeline wiring** (real file reads between stages, not narrative links).
5. **Per-chart construction/labeling** (interval type, axis range, colormap domain, dropped
   categories, chart-type swaps).
6. **Regenerate exhibits A→B→C** in dependency order; re-export the public report at full
   resolution; re-run the disposition check.

State, for each step, what it unblocks and which charts it forces a regen of.

## 3. Keep / Rework / Kill disposition table
One row per exhibit. Columns:

| Exhibit | What it shows | Verdict | Disposition | Blocking defect(s) | Action |
|---|---|---|---|---|---|

- **Verdict** = one of Approved / Approved With Revisions / Significant Rework Needed / Reject And
  Rebuild.
- **Disposition** = Keep / Keep-Promoted / Rework / Replace-with-{table|sentence|other chart} /
  Kill.
- **Blocking defect(s)** = the ranked-defect ids that must be fixed before this exhibit is trusted.
- **Action** = the concrete next step ("relabel band as 90% ETI; overlay polls", "delete; replace
  with national posterior sentence", "rebuild as ECDF after metric fix").

End with a **cull count**: "Of N exhibits, M earn their existence." and the headline root causes
(usually 2–4 bugs explain most of the defects).

## Tone
Factual, specific, reproducible. Credit the genuinely good exhibits (especially honest diagnostics)
so the ranking is believable. Never merge issue classes. Make every recommendation actionable by
someone who will open a specific file.

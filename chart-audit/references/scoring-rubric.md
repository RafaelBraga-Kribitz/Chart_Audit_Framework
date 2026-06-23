# Scoring Rubric — Five Axes + Severity + Earn Its Place

---

## Scoring (five axes, 0–10 each)

- **Visual Design** — layout, readability, restraint, absence of chartjunk. Score 8+ only if nothing is clipped/colliding and encoding is clean.

- **Statistical Integrity** — does the picture faithfully represent the data and its uncertainty? Cap at 3 if a quantity within sampling/MC noise is presented as a real difference, or a ratio is plotted against its own component, or atoms are KDE'd.

- **Analytical Value** — does it answer a real question / support a decision? A chart can score high here *as a diagnostic* even when it's an ugly rendering of a defect (a good bug-finder earns its keep).

- **Communication Quality** — clarity and honesty to a stakeholder. Penalize buried caveats. The caveat must live *in the exhibit*, not in a footnote, JSON dump, or fine print.

- **Confidence in Correctness** — *your* confidence that the chart is right. Low when the producing code is unseen, when sibling charts contradict it, or when the result is "too clean." This axis is about epistemic status, not aesthetics.

---

## The "Earn Its Place" Test

Apply to every chart, in order:

1. Does it convey something text / a table / a single statistic cannot (shape, geography, structure, interaction, uncertainty)? If no → recommend replacement by that sentence/table/stat.

2. Is the thing it conveys *real* (above noise, not self-correlated, not an artifact)? If no → Reject And Rebuild regardless of how polished it looks.

3. Is there another chart already in scope conveying the same insight better? If yes → recommend consolidation; flag the weaker one for removal.

4. Does it advance the project's central narrative (understanding / decision / causal reasoning / evidence quality)? If it's technically correct but inert → recommend removal.

A chart that fails 1, 2, or 4 should be removed or rebuilt even when its Visual score is high. "Technically correct but inert" is a removal, not a pass.

---

## Severity Classification

- **Critical** — misleads a reader, hides a constraint violation, presents noise/artifact as a finding, or contradicts another published exhibit. Blocks publication.

- **Moderate** — degrades trust or readability or omits needed context, but the core quantity is defensible once fixed.

- **Minor** — cosmetic; fix opportunistically.

**Decision rule for Moderate vs Critical:** "Would a stakeholder make a worse decision because of this?" If yes → Critical.

---

## Per-Chart Output Template

```
## <chart id> — <title>

Verdict: <one sentence, the sharp summary>

Scores: Visual x/10 · Statistical x/10 · Analytical x/10 · Communication x/10 · Confidence x/10

Critical Issues
  (by layer; the ones that block publication or mislead)
Moderate Issues
Minor Issues

Possible Data Problems   (why suspicious · attribution · confidence)
Possible Code Problems   (Suspicion · Evidence · Verification [file:line or exact check] · Confidence)

Better Chart Options     (alternative · what it improves)
Follow-Up Charts         (purpose · insight · priority)

Narrative Contribution: <keep / keep-promoted / rework / remove / replace> — <reason>

Required Fixes (Upstream First)
  1. [Analytical Question issues]
  2. [Analytical Logic issues]
  3. [Chart Type issues]
  4. [Missing Evidence]
  5. [Data Problems]
  6. [Code Problems]
  7. [Statistical Problems]
  8. [Plot Construction]
  9. [Visual Design]

Final Assessment: <Approved | Approved With Revisions | Significant Rework Needed | Reject And Rebuild>
  <justification>

Gate Fired: <None | A | B | C | D> — <brief reason>
```

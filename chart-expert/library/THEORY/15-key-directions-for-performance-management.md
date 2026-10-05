# Key directions for performance management

The useful directions, stated so a later design can follow them:

- **Fewer keys, fuller definitions.** Breadth belongs in the catalog. The live scorecard stays short. Every entry in this library has a full definition so selection is possible.
- **Formulas that cite inputs.** Sub-metrics are first-class. A KPI that cannot be recomputed is retired.
- **Leading and lagging as pairs.** Steering views include a driver. Reporting views may be lagging, but they say so.
- **Risk beside success.** KRIs sit next to the KPI they can contradict.
- **Levels kept apart.** Strategic, tactical, operational, and individual packs do not share a canvas.
- **Targets with a source.** Plan, threshold, baseline, or labeled benchmark.
- **Notation over decoration.** IBCS-style comparison (actual, plan, forecast) beats ornamental dials.
- **Stories with a decision.** A dashboard that cannot produce a sentence is a dead end.
- **Learning over punishment.** Individual indicators are for the person who owns the work.
- **Systems over heroes.** If a rate is produced by the process, manage the process.

## Rule

When you extend this library, add a full entry or an explicit exception. Do not add a name-only row and call the catalog finished.

## Worked example

A new function or area arrives. Add each KPI to `CORE` in `scripts/build_measures.py` with its formula, inputs, and charts; the build writes its dashboard specification. Add at least one objective whose key results cite those KPIs. Then select the live scorecard from that menu.

## Failure this chapter prevents

A measurement program that grows by accumulation and shrinks in meaning.

## Open next

`references/selection-playbook.md`.

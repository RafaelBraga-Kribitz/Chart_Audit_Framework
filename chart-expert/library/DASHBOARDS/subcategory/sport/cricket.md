---
id: dash.sport.cricket
type: dashboard
status: placeholder
category: Sport
subcategory: Cricket
context: organizational
audiences: [Executive, Data Analytics]
---

# Sport / Cricket

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Cricket on the right side of their targets?
- Which input moved, and is that a signal or a tail?

## Audiences and surfaces

- Communication (executive, client, HR business partner): dashboard or report. Use each KPI's communication chart.
- Analysis (data scientist, researcher, R&D, marketing analytics, development): notebook or pandas/matplotlib plot. Use each KPI's analysis chart. Do not paste that figure onto the executive page unchanged.

## Zones (communication)

| Zone | What goes here |
|---|---|
| Score | Big number or bullet versus target for the OMTM of this subcategory |
| Trend | Line of that KPI |
| Breakdown | Sorted bar of the entities |
| Variance | Waterfall or diverging bar versus plan |
| Detail | Data table of the rows a person can act on |

## KPIs

- `kpi.sport.wide-bowled` Wide bowled. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.runs-connected` Runs connected. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.no-boundary-shots` No boundary shots. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.strike-rate` Strike rate. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.sport.scoring-shots` Scoring shots. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.sport.centuries-scored` Centuries scored. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.no-boundary-balls` No boundary balls. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.bowling-average` Bowling average. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.run-out-conversion` Run out conversion. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.sport.batting-average` Batting average. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

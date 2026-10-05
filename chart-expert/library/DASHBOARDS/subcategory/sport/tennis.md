---
id: dash.sport.tennis
type: dashboard
status: placeholder
category: Sport
subcategory: Tennis
context: organizational
audiences: [Executive, Data Analytics]
---

# Sport / Tennis

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Tennis on the right side of their targets?
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

- `kpi.sport.break-points-conversion` Break points conversion. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.sport.first-serve` First serve. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.sport.second-serve-win` Second serve win. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.sport.service-points-win` Service points win. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

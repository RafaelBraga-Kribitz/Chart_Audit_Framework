---
id: dash.sport.badminton
type: dashboard
status: placeholder
category: Sport
subcategory: Badminton
context: organizational
audiences: [Executive, Data Analytics]
---

# Sport / Badminton

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Badminton on the right side of their targets?
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

- `kpi.sport.a-rallies-per-game` a Rallies per game. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.sport.a-shuttle-in-play` a Shuttle in play. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.a-shots-per-rally` a Shots per rally. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.sport.a-shots-per-game` a Shots per game. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.sport.b-game-intensity` b Game intensity. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.a-distance-covered` a Distance covered. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.a-drives` a Drives. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.b-low-serve` b Low serve. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.b-high-serve` b High serve. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.sport.a-smashes` a Smashes. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

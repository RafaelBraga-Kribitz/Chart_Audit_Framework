---
id: dash.portfolio-and-project-management.delivery
type: dashboard
status: placeholder
category: Portfolio and Project Management
subcategory: Delivery
context: organizational
audiences: [Executive, Data Analytics]
---

# Portfolio and Project Management / Delivery

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Delivery on the right side of their targets?
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

- `kpi.portfolio-and-project-management.billed-versus-expected` Billed versus expected. Communication `bullet-graph`. Analysis `scatter-plot`.
- `kpi.portfolio-and-project-management.project-contribution-margin` Project contribution margin. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.portfolio-and-project-management.estimated-versus-actual-project-time` Estimated versus actual project time. Communication `bullet-graph`. Analysis `scatter-plot`.
- `kpi.portfolio-and-project-management.estimated-versus-actual-project-cost` Estimated versus actual project cost. Communication `bullet-graph`. Analysis `scatter-plot`.
- `kpi.portfolio-and-project-management.lead-time-per-project` Lead time per project. Communication `horizontal-bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

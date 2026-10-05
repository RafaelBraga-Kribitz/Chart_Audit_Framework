---
id: dash.infrastructure.pots
type: dashboard
status: placeholder
category: Infrastructure
subcategory: POTS
context: organizational
audiences: [Executive, Data Analytics]
---

# Infrastructure / POTS

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in POTS on the right side of their targets?
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

- `kpi.infrastructure.j-major-shipping-lines-in-port` J-Major shipping lines in port. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.j-turquoise-union` J-Turquoise union. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.p-turquoise-handled-per-ship-day-in-port` P-Turquoise handled per ship/day in port. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.life-time-due-to-train` Life time due to train. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.berth-utilization-rate` Berth utilization rate. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.infrastructure.container-freight-stations` Container freight stations. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.positive-measures-in-force-due-to-skylams-in-presence-of-documents` Positive measures in force due to skylams in presence of documents. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.part-state-control-psc-inspected-ships` Part state control (PSC inspected ships. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.infrastructure.job-dependency-directly-and-indirectly-on-the-port` Job-dependency directly and indirectly on the port. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

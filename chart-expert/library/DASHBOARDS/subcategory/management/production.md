---
id: dash.management.production
type: dashboard
status: placeholder
category: Management
subcategory: Production
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Production

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Production on the right side of their targets?
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

- `kpi.management.energy-used-per-unit-of-production` Energy used per unit of production. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.hazardous-operational-waste` Hazardous operational waste. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.unit-production-time` * Unit production time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.energy-cost-per-unit-of-production` § Energy cost per unit of production. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.fixed-production-overhead-volume-capacity-variance` § Fixed production overhead volume capacity variance. Communication `waterfall-chart`. Analysis `bar-chart`.
- `kpi.management.units-per-man-hour` § Units per man-hour. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.time-yield` § Time yield. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.piece-variance` Piece variance. Communication `waterfall-chart`. Analysis `bar-chart`.
- `kpi.management.average-cycle-time-act` Average cycle time (ACT). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.tak-time` Tak time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.startup-rejects` Startup rejects. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.production-rejects` Production rejects. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.production-losses` Production losses. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.production-lead-time` Production lead time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.working-stock` Working stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.decoupling-stock` Decoupling stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.slow-servoing-stock` Slow servoing stock. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.boomerang-return-rate` Boomerang return rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.residual-value` Residual value. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.fired-production-overhead-total-variance` Fired production overhead total variance. Communication `waterfall-chart`. Analysis `bar-chart`.
- `kpi.management.emissions-from-production` Emissions from production. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.direct-labor-efficiency-variance` Direct labor efficiency variance. Communication `waterfall-chart`. Analysis `bar-chart`.
- `kpi.management.production-delays-due-to-raw-material-shortage` Production delays due to raw material shortage. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.production-uptime` Production uptime. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.work-in-progress-days` Work in progress days. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.unplanned-maintenance` Unplanned maintenance. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.value-of-finished-products` Value of finished products. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.value-of-work-in-progress` Value of work in progress. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.material-cost-per-product` Material cost per product. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.schedule-cycle-variances` Schedule cycle variances. Communication `waterfall-chart`. Analysis `bar-chart`.
- `kpi.management.labor-cost-per-unit-production` Labor cost per unit production. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.small-tasks` Small tasks. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.production-volume` Production volume. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.idle-time` Idle time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.material-consumption-per-product` Material consumption per product. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.production-orders-finished-late` Production orders finished late. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.production-orders-shipped-ahead-time` Production orders shipped ahead time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.production-schedule-adherence` Production schedule adherence. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.production-costs-per-unit` Production costs per unit. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.actual-to-projected-unit-production-costs` Actual to projected unit production costs. Communication `bar-chart`. Analysis `bar-chart`.
- ... 20 more in the subcategory KPI page.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

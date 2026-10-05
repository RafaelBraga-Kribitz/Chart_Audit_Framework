---
id: dash.manufacturing.general
type: dashboard
status: placeholder
category: Manufacturing
subcategory: General
context: organizational
audiences: [Executive, Data Analytics]
---

# Manufacturing / General

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in General on the right side of their targets?
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

- `kpi.planning.cost-of-goods-sold-cogs` § Cost of goods sold (COGS). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.electricity-consumption-per-manufactured-product` ▼ Electricity consumption per manufactured product. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.hazardous-raw-material-per-kilogram-of-product` ▼ Hazardous raw material per kilogram of product. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.maintenance-cost-from-equipment-cost` Maintenance cost from equipment cost. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.working-stock` Working stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.decoupling-stock` Decoupling stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.production-costs-per-unit` Production costs per unit. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.recovery-yield-rate-of-returned-products` Recovery yield rate of returned products. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.production-plants` Production plants. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.scrap-rate` Scrap rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.quality-awareness-programs` Quality awareness programs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.informative-inspections` Informative inspections. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.stock-value` Stock value. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.sales-order-cancellation-rate` Sales order cancellation rate. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.management.safety-stock` Safety stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.reorder-point-rop` Reorder point (ROP). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.anticipation-stock` Anticipation stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.distracted-stock` Distracted stock. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.obsolete-stock` Obsolete stock. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.cost-of-goods-sold` Cost of goods sold. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.time-to-manufacturing` Time to manufacturing. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.bulk-containers-with-obvious-signs-of-internal-rusting` bulk containers with obvious signs of internal rusting. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.unit-production-limit` unit production limit. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.interruptions-in-raw-material-supply` interruptions in raw material supply. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.manufacturing-contractors-not-used` Manufacturing contractors not used. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.deflections-improvement` Deflections improvement. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.altman-2-score` Altman 2-Score. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.deflections-per-manufacturing-plant-inspection` Deflections per manufacturing plant inspection. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.critical-equipment-availability` Critical equipment availability. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.bulk-containers-compliance` Bulk containers compliance. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.3-manufacturing-flow-control-system-utilization` 3 Manufacturing flow control system utilization. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.people-productivity` People productivity. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.not-right-first-time` Not right first time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.delivery-cost-on-time-and-in-fall` Delivery cost on time and in fall. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.inventory-turns` Inventory turns. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.parts-ordered` Parts ordered. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.calendar-time` Calendar time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.flannel-downtime` Flannel downtime. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.manufacturing.value-of-work-is-proper` Value of work is proper. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.manufacturing.schedule-operation-time` Schedule operation time. Communication `bar-chart`. Analysis `bar-chart`.
- ... 14 more in the subcategory KPI page.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

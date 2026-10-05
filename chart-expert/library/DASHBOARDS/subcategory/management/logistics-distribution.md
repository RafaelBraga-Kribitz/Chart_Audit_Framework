---
id: dash.management.logistics-distribution
type: dashboard
status: placeholder
category: Management
subcategory: Logistics / Distribution
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Logistics / Distribution

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Logistics / Distribution on the right side of their targets?
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

- `kpi.online-presence.on-time-delivery` On-time delivery. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.online-presence.items-per-order` Items per order. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.orders-delivered-with-complete-and-accurate-documentation` Orders delivered with complete and accurate documentation. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.point-consumption-per-100-kilometers` Point consumption per 100 kilometers. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.spots-rep-trip` Spots rep trip. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.transport-capacity-utilization` Transport capacity utilization. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.order-fill-rate` Order fill rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.backorder-costs` Backorder costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.time-spent-picking-back-orders-or-stock-outs` Time spent picking back orders or stock-outs. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.orders-picked-per-hour` Orders picked per hour. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.baggage-transfer-time` Baggage transfer time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.fuel-cost` Fuel cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.freight-revenue-per-ton-mile` Freight revenue per ton-mile. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.packaging-to-product-ratio` Packaging to product ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.distribution-cost` Distribution cost. Communication `bullet-graph`. Analysis `histogram`.
- `kpi.management.pick-to-chip-service-time-for-customer-orders` Pick-to-chip service time for customer orders. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.institutional-logistics-costs` Institutional logistics costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.outsourced-logistics-costs` Outsourced logistics costs. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.class-docking-operations` Class-docking operations. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

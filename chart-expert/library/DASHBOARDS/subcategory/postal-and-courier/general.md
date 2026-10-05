---
id: dash.postal-and-courier.general
type: dashboard
status: placeholder
category: Postal and Courier
subcategory: General
context: organizational
audiences: [Executive, Data Analytics]
---

# Postal and Courier / General

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

- `kpi.management.transport-capacity-utilization` Transport capacity utilization. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.fuel-cost` Fuel cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.customer-shipment-to-delivery-cycle-time` Customer shipment to delivery cycle time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.shipment-traceability` Shipment traceability. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.transit-time` Transit time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.delivery-routes-competing-each-day` Delivery routes competing each day. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.transbound-time` ▲Transbound time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.special-delivery-by-end-day` Special delivery by end day. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.residential-deliveries` Residential deliveries. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.business-deliveries` Business deliveries. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.express-services-tonnes` Express services tonnes. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.post-office-delivery-losses` Post office delivery losses. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.collection-points-served-each-day` Collection points served each day. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.public-mail-collection-points` Public mail collection points. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.mail-volume-processed-per-hour` Mail volume processed per hour. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.delivery-points` Delivery points. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.nolauklans-served-by-post-office` Nolauklans served by post office. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.stamped-and-metered-mail-sent-by-first-class` Stamped and metered mail sent by first class. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.post-offices` Post offices. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.electronic-sorting-machines` Electronic sorting machines. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.distance-traveled-by-postal-vehicles` Distance traveled by postal vehicles. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.parcels-posted-at-the-post-offices` Parcels posted at the post offices. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.mail-delivered-by-next-working-day` Mail delivered by next working day. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.parcels-posted-in-the-post-offices-that-were-the-origin-of-a-complaint` Parcels posted in the post offices that were the origin of a complaint. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.outgoing-international-mail-shipped-by-next-working-day` Outgoing international mail shipped by next working day. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.mail-volume-processed-per-day` Mail volume processed per day. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.mail-delivered-by-postcode-area` Mail delivered by postcode area. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.postal-and-courier.mail-volume-handled` Mail volume handled. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.postal-address-changes-processed` Postal address changes processed. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.postal-and-courier.advertising-mail-out-of-domestic-letter-posts` Advertising mail out of domestic letter posts. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

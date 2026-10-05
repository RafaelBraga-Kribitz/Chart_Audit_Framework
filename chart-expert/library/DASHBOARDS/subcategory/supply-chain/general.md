---
id: dash.supply-chain.general
type: dashboard
status: placeholder
category: Supply Chain
subcategory: General
context: organizational
audiences: [Executive, Data Analytics]
---

# Supply Chain / General

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

- `kpi.supply-chain.product-return-rate` Product return rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.empty-running` Empty running. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.delivered-in-full-on-time` Delivered in-Full, On-Time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.order-entry-accuracy` Order entry accuracy. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.supply-chain-response-time` 'Supply chain response time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.order-processing-time` Order processing time. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.order-fulfillment-lead-time` Order fulfillment lead time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.order-receipt-to-order-entry-complete-time` Order receipt to order entry complete time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.scheduling-to-customer-request` Scheduling to customer request. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.delivery-to-request-date` Delivery to request date. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.delivery-to-commit-date` Delivery to commit date. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.time-from-customer-authorization-to-order-receipt` Time from customer authorization to order receipt. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.order-entry-complete-to-start-manufacture-time` Order entry complete to start manufacture time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.start-manufacture-to-order-complete-manufacture-time` Start manufacture to order complete manufacture time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.order-complete-manufacture-to-customer-receipt-of-order` Order complete manufacture to customer receipt of order. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.customer-receipt-of-order-to-installation-complete-time` Customer receipt of order to installation complete time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.cash-to-cash-cycle-time` Cash-to-cash cycle time. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.days-sales-outstanding-dso` Days sales outstanding (DSO). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.cost-of-goods-sold` Cost of goods sold. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.supply-chain-management-cost` Supply chain management cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.order-management-cost` Order management cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.if-for-out-supply-chain` If for out supply chain. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.supply-chain-related-order-management-cost` Supply chain related order management cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.the-supply-chain-related-finance-and-planning-cost` The supply chain related finance and planning cost. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.return-management-costs` Return management costs. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.lines-per-order` Lines per order. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.full-part-for-ship-from-stock` Full part for ship-from stock. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.upside-supply-chain-flexibility` Upside supply chain flexibility. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.adherence-to-delivery-schedule` Adherence to delivery schedule. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.unshakable-cost` Unshakable cost. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.cost-per-line-dispatched` Cost per line dispatched. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.software-used-to-support-supply-chain` Software used to support supply chain. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.documents-per-trade-transaction` Documents per trade transaction. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.customers-errors-placing-orders` Customers errors placing orders. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.employees-allocated-to-order-processing` Employees allocated to order processing. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.supply-chain.freight-cost-per-ton-shipped` Freight cost per ton shipped. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.intermediaries-in-raw-material-supply` Intermediaries in raw material supply. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.processing-time-in-days` Processing time in days. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.relative-asset-utilization-frequency` Relative asset utilization frequency. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.supply-chain.order-cycle-time` Order cycle time. Communication `bar-chart`. Analysis `bar-chart`.
- ... 19 more in the subcategory KPI page.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

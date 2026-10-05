---
id: dash.online-presence.email-marketing
type: dashboard
status: placeholder
category: Online Presence
subcategory: Email Marketing
context: personal
audiences: [Executive, Data Analytics, Marketing Analytics]
---

# Online Presence / Email Marketing

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Email Marketing on the right side of their targets?
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

- `kpi.online-presence.email-list-hurdle-rate` Email list hurdle rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.online-presence.email-list-size` Email list size. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.online-presence.auto-expensive-emails-to-customer-inquiries` Auto-expensive emails to customer inquiries. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.online-presence.order-size-per-email` Order size per email. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.online-presence.orders-per-email` Orders per email. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.online-presence.click-to-open-cto` Click to open (CTO). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.online-presence.personalisation-errors-in-emails` Personalisation errors in emails. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.online-presence.email-tests-conducted-per-email-marketing-campaign` Email tests conducted per email marketing campaign. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.online-presence.email-conversion-rate` Email conversion rate. Communication `bullet-graph`. Analysis `diverging-bar`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

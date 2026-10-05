---
id: dash.management.governance
type: dashboard
status: placeholder
category: Management
subcategory: Governance
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Governance

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Governance on the right side of their targets?
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

- `kpi.management.b-outstanding-shares-considered-as-free-float` b) Outstanding shares considered as free float. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.f-board-meetings` f) Board meetings. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.f-board-director-tenure` f) Board director tenure. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.b-executive-directors` b) Executive directors. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.b-independent-directors` b) Independent directors. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.b-new-board-members-with-industry-expertise` b) New board members with industry expertise. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.b-strategic-objectives-achieved` b) Strategic objectives achieved. Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.management.c-corporate-governance-index-cgi` c) Corporate governance index (CGI). Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.management.b-board-committees` b) Board committees. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.b-non-board-members-attendance` b) Non-board members' attendance. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.b-board-meetings-attendance` b) Board meetings attendance. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.days-in-advance-to-send-out-notice-of-general-shareholders-meetings` Days in advance to send out notice of general shareholders' meetings. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.c-cases-of-insider-trading-involving-company-management` c) Cases of insider trading involving company management. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

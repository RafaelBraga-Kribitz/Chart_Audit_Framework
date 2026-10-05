---
id: dash.management.financial-stability
type: dashboard
status: placeholder
category: Management
subcategory: Financial stability
context: organizational
audiences: [Executive, Data Analytics]
---

# Management / Financial stability

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Financial stability on the right side of their targets?
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

- `kpi.accounting.interest-cover` Interest cover. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.times-interest-earned` Times interest earned. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.planning.net-debt` § Net debt. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.weighted-average-cost-of-capital-wacc` Weighted average cost of capital (WACC). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.altman-z-score-for-public-manufacturing-companies` Altman Z-Score (for public manufacturing companies). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.altman-z-score-for-privately-held-manufacturing-companies` Altman Z-Score (for privately held manufacturing companies). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.altman-z-score-for-privately-held-non-manufacturing-companies` Altman Z-Score (for privately held non-manufacturing companies). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.debt-ratio` Debt ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.debt-to-equity-ratio` Debt-to-equity ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.cash-flow-per-share` Cash flow per share. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.management.debt-to-capital-ratio` Debt-to-capital ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.expense-coverage-days` Expense coverage days. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.current-liabilities-to-sales` Current liabilities to sales. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.ebitda-coverage` EBITDA coverage. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.fixed-assets-to-short-term-debt` Fixed assets to short term debt. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.gearing-ratio` Gearing ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.loan-bills-to-coverage-ratio` Loan bills to coverage ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.long-term-debt-to-capitalization-ratio` Long-term debt to capitalization ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.short-to-long-term-debt` Short to long term debt. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.capital-employed` Capital employed. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.cash-flow-to-long-term-debt` Cash flow to long term debt. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.sub-divided-cash-flow-mccf` Sub-divided cash flow (MCCF). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.capital-acquisition-ratio` Capital acquisition ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.liabilities-to-net-worth` Liabilities to net worth. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.current-liabilities-to-net-worth` Current liabilities to net worth. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.operating-assets-ratio` Operating assets ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.interest-expense` Interest expense. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.long-term-debt-to-total-debt` Long-term debt to total debt. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.short-term-to-total-debt` Short-term to total debt. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.solvency-ratio` Solvency ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.cash-maturity-coverage` Cash maturity coverage. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.common-shares-2` Common shares\( ^{2} \). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.texas-ratio` Texas ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.defensive-interval-ratio-dir` Defensive interval ratio (DIR). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.firm-exposure` Firm exposure. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.payroll-tax-paid-by-the-employer` Payroll tax paid by the employer. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.bad-debt-write-offs-from-gross-revenue` Bad debt write-offs from gross revenue. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.management.time-to-rescind-credit-balances` Time to rescind credit balances. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.capital-gearing` Capital gearing. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.management.capital-return-for-the-current-and-prior-three-quarters` Capital return for the current and prior three quarters. Communication `bar-chart`. Analysis `bar-chart`.
- ... 2 more in the subcategory KPI page.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

---
id: dash.accounting.cost-analysis
type: dashboard
status: placeholder
category: Accounting
subcategory: Cost Analysis
context: organizational
audiences: [Executive, Data Analytics]
---

# Accounting / Cost Analysis

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Cost Analysis on the right side of their targets?
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

- `kpi.accounting.wages-cost-from-sales` Wages cost from sales. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.contribution-margin-ratio` Contribution margin ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.gross-profit-margin` Gross profit margin. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.costs-per-fte-employee` Costs per FTE employee. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.overhead-cost-ratio` Overhead cost ratio. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.total-acquisition-cost-tac` Total acquisition cost (TAC). Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.marginal-propensity-to-consume-mpc` Marginal propensity to consume (MPC). Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.accounting.interest-expense-to-debt` Interest expense to debt. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.accounting-rate-of-return-arr` Accounting rate of return (ARR). Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.accounting.audit-ratio` Audit ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.burning-cost-ratio` Burning cost ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.cash-overflow-for-debt-service-cads` Cash overflow for debt service (CADS). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.cash-conversion-cycle-ccc` Cash conversion cycle (CCC). Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.discretionary-costs` Discretionary costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.cost-accrual-ratio` Cost accrual ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.operating-costs` Operating costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.expenses-claims-processed-per-employee` Expenses claims processed per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.fixed-cost-per-employee` Fixed cost per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.fixed-charge-coverage-ratio` Fixed charge coverage ratio. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.overdue-invoices` Overdue invoices. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.back-taxes` Back taxes. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.repairs-and-maintenance-expenses-to-fixed-assets` Repairs and maintenance expenses to fixed assets. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.fixed-costs` Fixed costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.indirect-costs` Indirect costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.sales-to-general-and-administrative-expenses` Sales to general and administrative expenses. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.marginal-costs-mc` Marginal costs (MC). Communication `bullet-graph`. Analysis `bar-chart`.
- `kpi.accounting.photos-costs-per-employee` Photos costs per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.variable-costs` Variable costs. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.working-capital-per-employee` Working capital per employee. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.cost-with-employees-from-the-operating-revenue` Cost with employees from the operating revenue. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.cost-of-the-finance-function-from-revenue` Cost of the finance function from revenue. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.department-cost-from-revenue` Department cost from revenue. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.discretionary-costs-from-sales` Discretionary costs from sales. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.indirect-expenses-per-sales` Indirect expenses per sales. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.royalty-rate` Royalty rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.payout-cost-paid-by-the-employer` Payout cost paid by the employer. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.charity-rate` Charity rate. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.obsolescence-costs-from-total-inventory` Obsolescence costs from total inventory. Communication `bullet-graph`. Analysis `diverging-bar`.
- `kpi.accounting.cost-to-maintain-vendor-master-data` Cost to maintain vendor master data. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.accounting.savings-achieved` Savings achieved. Communication `bar-chart`. Analysis `bar-chart`.
- ... 3 more in the subcategory KPI page.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

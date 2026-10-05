# Accounting / Cost Analysis

Context: organizational. Group: functional. KPIs: 43.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Wages cost from sales

- id: `kpi.accounting.wages-cost-from-sales`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Wages cost from sales measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is Wages cost, B is sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wages cost from sales on the desired side of its target for this period?

Inputs:

- `metric.wages-cost` (Wages cost)
- `metric.sales` (sales)

Placements:

- organizational / functional / Accounting / Cost Analysis (x8140, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contribution margin ratio

- id: `kpi.accounting.contribution-margin-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contribution margin ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is Contribution profit ratio, B is revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contribution margin ratio on the desired side of its target for this period?

Inputs:

- `metric.contribution-profit-ratio` (Contribution profit ratio)
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x8314, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gross profit margin

- id: `kpi.accounting.gross-profit-margin`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of revenue left after direct cost. Placed under Accounting / Cost Analysis.

Questions: Is Gross profit margin on the desired side of its target for this period?

Inputs:

- `metric.gross-profit` (gross profit)
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x8316, page_0009)
- organizational / functional / Management / Profitability (K316, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Costs per FTE employee

- id: `kpi.accounting.costs-per-fte-employee`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Costs per FTE employee measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is A / B, where A is Costs, B is FTE employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Costs per FTE employee on the desired side of its target for this period?

Inputs:

- `metric.costs` (Costs)
- `metric.fte-employee` (FTE employee)

Placements:

- organizational / functional / Accounting / Cost Analysis (x8267, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overhead cost ratio

- id: `kpi.accounting.overhead-cost-ratio`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overhead cost ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is numerator of Overhead cost ratio, B is base of Overhead cost ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overhead cost ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-overhead-cost-ratio` (numerator of Overhead cost ratio)
- `metric.base-of-overhead-cost-ratio` (base of Overhead cost ratio)

Placements:

- organizational / functional / Accounting / Cost Analysis (x8303, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Total acquisition cost (TAC)

- id: `kpi.accounting.total-acquisition-cost-tac`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Total acquisition cost (TAC) measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is part named by Total acquisition cost (TAC), B is whole named by Total acquisition cost (TAC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Total acquisition cost (TAC) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-total-acquisition-cost-tac` (part named by Total acquisition cost (TAC))
- `metric.whole-named-by-total-acquisition-cost-tac` (whole named by Total acquisition cost (TAC))

Placements:

- organizational / functional / Accounting / Cost Analysis (x8308, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marginal propensity to consume (MPC)

- id: `kpi.accounting.marginal-propensity-to-consume-mpc`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marginal propensity to consume (MPC) measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is (A / B) * 100, where A is Marginal propensity to consume (MPC), B is revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marginal propensity to consume (MPC) on the desired side of its target for this period?

Inputs:

- `metric.marginal-propensity-to-consume-mpc` (Marginal propensity to consume (MPC))
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83094, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interest expense to debt

- id: `kpi.accounting.interest-expense-to-debt`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Interest expense to debt measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is Interest expense, B is debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interest expense to debt on the desired side of its target for this period?

Inputs:

- `metric.interest-expense` (Interest expense)
- `metric.debt` (debt)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83232, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accounting rate of return (ARR)

- id: `kpi.accounting.accounting-rate-of-return-arr`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accounting rate of return (ARR) measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Accounting rate of return (ARR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accounting rate of return (ARR) on the desired side of its target for this period?

Inputs:

- `metric.accounting-rate-of-return-arr` (Accounting rate of return (ARR))

Placements:

- organizational / functional / Accounting / Cost Analysis (x83140, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Audit ratio

- id: `kpi.accounting.audit-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Audit ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Audit ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Audit ratio on the desired side of its target for this period?

Inputs:

- `metric.audit-ratio` (Audit ratio)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83140, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Burning cost ratio

- id: `kpi.accounting.burning-cost-ratio`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Burning cost ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Burning cost ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Burning cost ratio on the desired side of its target for this period?

Inputs:

- `metric.burning-cost-ratio` (Burning cost ratio)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83145, page_0009)
- organizational / industries / Financial Institutions / Insurance (sK145, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash overflow for debt service (CADS)

- id: `kpi.accounting.cash-overflow-for-debt-service-cads`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash overflow for debt service (CADS) measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Cash overflow for debt service (CADS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash overflow for debt service (CADS) on the desired side of its target for this period?

Inputs:

- `metric.cash-overflow-for-debt-service-cads` (Cash overflow for debt service (CADS))

Placements:

- organizational / functional / Accounting / Cost Analysis (x83146, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash conversion cycle (CCC)

- id: `kpi.accounting.cash-conversion-cycle-ccc`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash conversion cycle (CCC) measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Cash conversion cycle (CCC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash conversion cycle (CCC) on the desired side of its target for this period?

Inputs:

- `metric.cash-conversion-cycle-ccc` (Cash conversion cycle (CCC))

Placements:

- organizational / functional / Accounting / Cost Analysis (x83149, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Discretionary costs

- id: `kpi.accounting.discretionary-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Discretionary costs measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Discretionary costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Discretionary costs on the desired side of its target for this period?

Inputs:

- `metric.discretionary-costs` (Discretionary costs)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83153, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost accrual ratio

- id: `kpi.accounting.cost-accrual-ratio`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost accrual ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Cost accrual ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost accrual ratio on the desired side of its target for this period?

Inputs:

- `metric.cost-accrual-ratio` (Cost accrual ratio)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83158, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operating costs

- id: `kpi.accounting.operating-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating costs measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Operating costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating costs on the desired side of its target for this period?

Inputs:

- `metric.operating-costs` (Operating costs)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83159, page_0009)
- organizational / industries / Financial Institutions / Banking and Credit (sKR159, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expenses claims processed per employee

- id: `kpi.accounting.expenses-claims-processed-per-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Expenses claims processed per employee measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A / B, where A is Expenses claims processed, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expenses claims processed per employee on the desired side of its target for this period?

Inputs:

- `metric.expenses-claims-processed` (Expenses claims processed)
- `metric.employee` (employee)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83214, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed cost per employee

- id: `kpi.accounting.fixed-cost-per-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed cost per employee measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A / B, where A is Fixed cost, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed cost per employee on the desired side of its target for this period?

Inputs:

- `metric.fixed-cost` (Fixed cost)
- `metric.employee` (employee)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83217, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed charge coverage ratio

- id: `kpi.accounting.fixed-charge-coverage-ratio`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed charge coverage ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Fixed charge coverage ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed charge coverage ratio on the desired side of its target for this period?

Inputs:

- `metric.fixed-charge-coverage-ratio` (Fixed charge coverage ratio)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83218, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overdue invoices

- id: `kpi.accounting.overdue-invoices`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overdue invoices measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Overdue invoices. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overdue invoices on the desired side of its target for this period?

Inputs:

- `metric.overdue-invoices` (Overdue invoices)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83224, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Back taxes

- id: `kpi.accounting.back-taxes`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Back taxes measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Back taxes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Back taxes on the desired side of its target for this period?

Inputs:

- `metric.back-taxes` (Back taxes)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83255, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Repairs and maintenance expenses to fixed assets

- id: `kpi.accounting.repairs-and-maintenance-expenses-to-fixed-assets`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Repairs and maintenance expenses to fixed assets measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Repairs and maintenance expenses to fixed assets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Repairs and maintenance expenses to fixed assets on the desired side of its target for this period?

Inputs:

- `metric.repairs-and-maintenance-expenses-to-fixed-assets` (Repairs and maintenance expenses to fixed assets)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83257, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed costs

- id: `kpi.accounting.fixed-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed costs measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Fixed costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed costs on the desired side of its target for this period?

Inputs:

- `metric.fixed-costs` (Fixed costs)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83282, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Indirect costs

- id: `kpi.accounting.indirect-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Indirect costs measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Indirect costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Indirect costs on the desired side of its target for this period?

Inputs:

- `metric.indirect-costs` (Indirect costs)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83284, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sales to general and administrative expenses

- id: `kpi.accounting.sales-to-general-and-administrative-expenses`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sales to general and administrative expenses measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Sales to general and administrative expenses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sales to general and administrative expenses on the desired side of its target for this period?

Inputs:

- `metric.sales-to-general-and-administrative-expenses` (Sales to general and administrative expenses)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83286, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marginal costs (MC)

- id: `kpi.accounting.marginal-costs-mc`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marginal costs (MC) measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is (A / B) * 100, where A is Marginal costs (MC), B is revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marginal costs (MC) on the desired side of its target for this period?

Inputs:

- `metric.marginal-costs-mc` (Marginal costs (MC))
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83289, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Photos costs per employee

- id: `kpi.accounting.photos-costs-per-employee`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Photos costs per employee measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A / B, where A is Photos costs, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Photos costs per employee on the desired side of its target for this period?

Inputs:

- `metric.photos-costs` (Photos costs)
- `metric.employee` (employee)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83296, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Variable costs

- id: `kpi.accounting.variable-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Variable costs measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Variable costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Variable costs on the desired side of its target for this period?

Inputs:

- `metric.variable-costs` (Variable costs)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83210, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Working capital per employee

- id: `kpi.accounting.working-capital-per-employee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Working capital per employee measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A / B, where A is Working capital, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Working capital per employee on the desired side of its target for this period?

Inputs:

- `metric.working-capital` (Working capital)
- `metric.employee` (employee)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83231, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost with employees from the operating revenue

- id: `kpi.accounting.cost-with-employees-from-the-operating-revenue`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost with employees from the operating revenue measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Cost with employees from the operating revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost with employees from the operating revenue on the desired side of its target for this period?

Inputs:

- `metric.cost-with-employees-from-the-operating-revenue` (Cost with employees from the operating revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83333, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of the finance function from revenue

- id: `kpi.accounting.cost-of-the-finance-function-from-revenue`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of the finance function from revenue measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Cost of the finance function from revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of the finance function from revenue on the desired side of its target for this period?

Inputs:

- `metric.cost-of-the-finance-function-from-revenue` (Cost of the finance function from revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83234, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Department cost from revenue

- id: `kpi.accounting.department-cost-from-revenue`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Department cost from revenue measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Department cost from revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Department cost from revenue on the desired side of its target for this period?

Inputs:

- `metric.department-cost-from-revenue` (Department cost from revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83337, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Discretionary costs from sales

- id: `kpi.accounting.discretionary-costs-from-sales`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Discretionary costs from sales measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is Discretionary costs, B is sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Discretionary costs from sales on the desired side of its target for this period?

Inputs:

- `metric.discretionary-costs` (Discretionary costs)
- `metric.sales` (sales)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83339, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Indirect expenses per sales

- id: `kpi.accounting.indirect-expenses-per-sales`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Indirect expenses per sales measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is A / B, where A is Indirect expenses, B is sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Indirect expenses per sales on the desired side of its target for this period?

Inputs:

- `metric.indirect-expenses` (Indirect expenses)
- `metric.sales` (sales)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83409, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Royalty rate

- id: `kpi.accounting.royalty-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Royalty rate measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is numerator of Royalty rate, B is base of Royalty rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Royalty rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-royalty-rate` (numerator of Royalty rate)
- `metric.base-of-royalty-rate` (base of Royalty rate)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83419, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Payout cost paid by the employer

- id: `kpi.accounting.payout-cost-paid-by-the-employer`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Payout cost paid by the employer measures that result inside Accounting, subcategory Cost Analysis. The unit is currency. The formula is A, where A is Payout cost paid by the employer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Payout cost paid by the employer on the desired side of its target for this period?

Inputs:

- `metric.payout-cost-paid-by-the-employer` (Payout cost paid by the employer)

Placements:

- organizational / functional / Accounting / Cost Analysis (x87432, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Charity rate

- id: `kpi.accounting.charity-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Charity rate measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is numerator of Charity rate, B is base of Charity rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Charity rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-charity-rate` (numerator of Charity rate)
- `metric.base-of-charity-rate` (base of Charity rate)

Placements:

- organizational / functional / Accounting / Cost Analysis (x86319, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Obsolescence costs from total inventory

- id: `kpi.accounting.obsolescence-costs-from-total-inventory`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Obsolescence costs from total inventory measures that result inside Accounting, subcategory Cost Analysis. The unit is percent. The formula is (A / B) * 100, where A is Obsolescence costs, B is total inventory. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Obsolescence costs from total inventory on the desired side of its target for this period?

Inputs:

- `metric.obsolescence-costs` (Obsolescence costs)
- `metric.total-inventory` (total inventory)

Placements:

- organizational / functional / Accounting / Cost Analysis (x86294, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost to maintain vendor master data

- id: `kpi.accounting.cost-to-maintain-vendor-master-data`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost to maintain vendor master data measures that result inside Accounting, subcategory Cost Analysis. The unit is currency. The formula is A, where A is Cost to maintain vendor master data. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost to maintain vendor master data on the desired side of its target for this period?

Inputs:

- `metric.cost-to-maintain-vendor-master-data` (Cost to maintain vendor master data)

Placements:

- organizational / functional / Accounting / Cost Analysis (x86949, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Savings achieved

- id: `kpi.accounting.savings-achieved`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Savings achieved measures that result inside Accounting, subcategory Cost Analysis. The unit is currency. The formula is A, where A is Savings achieved. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Savings achieved on the desired side of its target for this period?

Inputs:

- `metric.savings-achieved` (Savings achieved)

Placements:

- organizational / functional / Accounting / Cost Analysis (x87057, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Life cycle cost (LCC)

- id: `kpi.accounting.life-cycle-cost-lcc`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Life cycle cost (LCC) measures that result inside Accounting, subcategory Cost Analysis. The unit is currency. The formula is A, where A is Life cycle cost (LCC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Life cycle cost (LCC) on the desired side of its target for this period?

Inputs:

- `metric.life-cycle-cost-lcc` (Life cycle cost (LCC))

Placements:

- organizational / functional / Accounting / Cost Analysis (x87059, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Amortization period in months

- id: `kpi.accounting.amortization-period-in-months`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Amortization period in months measures that result inside Accounting, subcategory Cost Analysis. The unit is currency. The formula is A, where A is Amortization period in months. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Amortization period in months on the desired side of its target for this period?

Inputs:

- `metric.amortization-period-in-months` (Amortization period in months)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83198, page_0009)
- organizational / functional / Management / Organizational » Functional Areas (sK13980, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost improvement plan

- id: `kpi.accounting.cost-improvement-plan`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost improvement plan measures that result inside Accounting, subcategory Cost Analysis. The unit is currency. The formula is A, where A is Cost improvement plan. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost improvement plan on the desired side of its target for this period?

Inputs:

- `metric.cost-improvement-plan` (Cost improvement plan)

Placements:

- organizational / functional / Accounting / Cost Analysis (x81405, page_0009)
- organizational / functional / Management / Organizational » Functional Areas (sK14056, page_0057)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

# Accounting / General

Context: organizational. Group: functional. KPIs: 61.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Interest cover

- id: `kpi.accounting.interest-cover`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Interest cover measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Interest cover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interest cover on the desired side of its target for this period?

Inputs:

- `metric.interest-cover` (Interest cover)

Placements:

- organizational / functional / Accounting / General (0605, page_0008)
- organizational / functional / Management / Financial stability (x865, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash flow after taxes (CFAT)

- id: `kpi.accounting.cash-flow-after-taxes-cfat`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash flow after taxes (CFAT) measures that result inside Accounting, subcategory General. The unit is number. The formula is A, where A is Cash flow after taxes (CFAT). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash flow after taxes (CFAT) on the desired side of its target for this period?

Inputs:

- `metric.cash-flow-after-taxes-cfat` (Cash flow after taxes (CFAT))

Placements:

- organizational / functional / Accounting / General (8529, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer invoices paid through electronic sourcing

- id: `kpi.accounting.customer-invoices-paid-through-electronic-sourcing`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer invoices paid through electronic sourcing measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer invoices paid through electronic sourcing, B is whole named by Customer invoices paid through electronic sourcing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer invoices paid through electronic sourcing on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-invoices-paid-through-electronic-sourcing` (part named by Customer invoices paid through electronic sourcing)
- `metric.whole-named-by-customer-invoices-paid-through-electronic-sourcing` (whole named by Customer invoices paid through electronic sourcing)

Placements:

- organizational / functional / Accounting / General (82959, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Times interest earned

- id: `kpi.accounting.times-interest-earned`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Times interest earned measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Times interest earned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Times interest earned on the desired side of its target for this period?

Inputs:

- `metric.times-interest-earned` (Times interest earned)

Placements:

- organizational / functional / Accounting / General (83025, page_0008)
- organizational / functional / Management / Financial stability (x3025, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accuracy of expense reimbursement requests

- id: `kpi.accounting.accuracy-of-expense-reimbursement-requests`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accuracy of expense reimbursement requests measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Accuracy, B is expense reimbursement requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accuracy of expense reimbursement requests on the desired side of its target for this period?

Inputs:

- `metric.accuracy` (Accuracy)
- `metric.expense-reimbursement-requests` (expense reimbursement requests)

Placements:

- organizational / functional / Accounting / General (83190, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### By-Electronic invoices

- id: `kpi.accounting.by-electronic-invoices`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

By-Electronic invoices measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by By-Electronic invoices, B is whole named by By-Electronic invoices. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is By-Electronic invoices on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-by-electronic-invoices` (part named by By-Electronic invoices)
- `metric.whole-named-by-by-electronic-invoices` (whole named by By-Electronic invoices)

Placements:

- organizational / functional / Accounting / General (83361, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees managing the accounting processes

- id: `kpi.accounting.employees-managing-the-accounting-processes`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees managing the accounting processes measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Employees managing the accounting processes, B is whole named by Employees managing the accounting processes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees managing the accounting processes on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-employees-managing-the-accounting-processes` (part named by Employees managing the accounting processes)
- `metric.whole-named-by-employees-managing-the-accounting-processes` (whole named by Employees managing the accounting processes)

Placements:

- organizational / functional / Accounting / General (83341, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to execute and manage financial performance

- id: `kpi.accounting.employees-allocated-to-execute-and-manage-financial-performance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to execute and manage financial performance measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is execute and manage financial performance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to execute and manage financial performance on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.execute-and-manage-financial-performance` (execute and manage financial performance)

Placements:

- organizational / functional / Accounting / General (83344, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to fixe and manage financial performance

- id: `kpi.accounting.employees-allocated-to-fixe-and-manage-financial-performance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to fixe and manage financial performance measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is fixe and manage financial performance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to fixe and manage financial performance on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.fixe-and-manage-financial-performance` (fixe and manage financial performance)

Placements:

- organizational / functional / Accounting / General (83347, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to fixed asset management

- id: `kpi.accounting.employees-allocated-to-fixed-asset-management`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to fixed asset management measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is fixed asset management. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to fixed asset management on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.fixed-asset-management` (fixed asset management)

Placements:

- organizational / functional / Accounting / General (83349, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to general accounting and reporting

- id: `kpi.accounting.employees-allocated-to-general-accounting-and-reporting`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to general accounting and reporting measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is general accounting and reporting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to general accounting and reporting on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.general-accounting-and-reporting` (general accounting and reporting)

Placements:

- organizational / functional / Accounting / General (83350, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to internal controls

- id: `kpi.accounting.employees-allocated-to-internal-controls`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to internal controls measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is internal controls. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to internal controls on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.internal-controls` (internal controls)

Placements:

- organizational / functional / Accounting / General (83351, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to manage and process collections

- id: `kpi.accounting.employees-allocated-to-manage-and-process-collections`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to manage and process collections measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is manage and process collections. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to manage and process collections on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.manage-and-process-collections` (manage and process collections)

Placements:

- organizational / functional / Accounting / General (83353, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to manage and process collection

- id: `kpi.accounting.employees-allocated-to-manage-and-process-collection`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to manage and process collection measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is manage and process collection. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to manage and process collection on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.manage-and-process-collection` (manage and process collection)

Placements:

- organizational / functional / Accounting / General (83354, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to manage financial policies and procedures

- id: `kpi.accounting.employees-allocated-to-manage-financial-policies-and-procedures`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to manage financial policies and procedures measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is manage financial policies and procedures. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to manage financial policies and procedures on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.manage-financial-policies-and-procedures` (manage financial policies and procedures)

Placements:

- organizational / functional / Accounting / General (83355, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to manage payments

- id: `kpi.accounting.employees-allocated-to-manage-payments`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to manage payments measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is manage payments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to manage payments on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.manage-payments` (manage payments)

Placements:

- organizational / functional / Accounting / General (83356, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to payroll

- id: `kpi.accounting.employees-allocated-to-payroll`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to payroll measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is payroll. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to payroll on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.payroll` (payroll)

Placements:

- organizational / functional / Accounting / General (83358, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to perform financial reporting

- id: `kpi.accounting.employees-allocated-to-perform-financial-reporting`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to perform financial reporting measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is perform financial reporting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to perform financial reporting on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.perform-financial-reporting` (perform financial reporting)

Placements:

- organizational / functional / Accounting / General (83362, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to perform general accounting

- id: `kpi.accounting.employees-allocated-to-perform-general-accounting`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to perform general accounting measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is perform general accounting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to perform general accounting on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.perform-general-accounting` (perform general accounting)

Placements:

- organizational / functional / Accounting / General (83364, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to perform planning/budgeting/forecasting

- id: `kpi.accounting.employees-allocated-to-perform-planning-budgeting-forecasting`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to perform planning/budgeting/forecasting measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is perform planning/budgeting/forecasting. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to perform planning/budgeting/forecasting on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.perform-planning-budgeting-forecasting` (perform planning/budgeting/forecasting)

Placements:

- organizational / functional / Accounting / General (83365, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to manage financial performance evaluation

- id: `kpi.accounting.employees-allocated-to-manage-financial-performance-evaluation`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to manage financial performance evaluation measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is manage financial performance evaluation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to manage financial performance evaluation on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.manage-financial-performance-evaluation` (manage financial performance evaluation)

Placements:

- organizational / functional / Accounting / General (83366, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to report on internal controls compliance

- id: `kpi.accounting.employees-allocated-to-report-on-internal-controls-compliance`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to report on internal controls compliance measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is report on internal controls compliance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to report on internal controls compliance on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.report-on-internal-controls-compliance` (report on internal controls compliance)

Placements:

- organizational / functional / Accounting / General (83369, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to report payroll taxes

- id: `kpi.accounting.employees-allocated-to-report-payroll-taxes`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to report payroll taxes measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is report payroll taxes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to report payroll taxes on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.report-payroll-taxes` (report payroll taxes)

Placements:

- organizational / functional / Accounting / General (83370, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to tax

- id: `kpi.accounting.employees-allocated-to-tax`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to tax measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is tax. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to tax on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.tax` (tax)

Placements:

- organizational / functional / Accounting / General (83372, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employees allocated to treasury operations

- id: `kpi.accounting.employees-allocated-to-treasury-operations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employees allocated to treasury operations measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Employees allocated, B is treasury operations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employees allocated to treasury operations on the desired side of its target for this period?

Inputs:

- `metric.employees-allocated` (Employees allocated)
- `metric.treasury-operations` (treasury operations)

Placements:

- organizational / functional / Accounting / General (83373, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Manual payroll payments

- id: `kpi.accounting.manual-payroll-payments`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Manual payroll payments measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Manual payroll payments, B is whole named by Manual payroll payments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Manual payroll payments on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-manual-payroll-payments` (part named by Manual payroll payments)
- `metric.whole-named-by-manual-payroll-payments` (whole named by Manual payroll payments)

Placements:

- organizational / functional / Accounting / General (83385, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of outsourced finance function

- id: `kpi.accounting.cost-of-outsourced-finance-function`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of outsourced finance function measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Cost, B is outsourced finance function. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of outsourced finance function on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.outsourced-finance-function` (outsourced finance function)

Placements:

- organizational / functional / Accounting / General (83387, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accounting system downtime

- id: `kpi.accounting.accounting-system-downtime`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accounting system downtime measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Accounting system downtime, B is whole named by Accounting system downtime. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accounting system downtime on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-accounting-system-downtime` (part named by Accounting system downtime)
- `metric.whole-named-by-accounting-system-downtime` (whole named by Accounting system downtime)

Placements:

- organizational / functional / Accounting / General (83401, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Risen ratio

- id: `kpi.accounting.risen-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Risen ratio measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Risen ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Risen ratio on the desired side of its target for this period?

Inputs:

- `metric.risen-ratio` (Risen ratio)

Placements:

- organizational / functional / Accounting / General (83460, page_0008)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Billable fees write-downs

- id: `kpi.planning.billable-fees-write-downs`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Billable fees write-downs measures that result inside Planning, subcategory Organizational » Functional Areas. The unit is count. The formula is A, where A is Billable fees write-downs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Billable fees write-downs on the desired side of its target for this period?

Inputs:

- `metric.billable-fees-write-downs` (Billable fees write-downs)

Placements:

- organizational / functional / Planning / Organizational » Functional Areas (sK4715, page_0011)
- organizational / functional / Accounting / General (aK671, page_0158)
- organizational / functional / Accounting / Business Consulting (#K715, page_0158)
- organizational / industries / Media / Recruitment/Employment Activities (sK4715, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Certified accountants

- id: `kpi.human-resources.certified-accountants`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.organizational-function-of-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Certified accountants measures that result inside Human Resources, subcategory Organizational Function of Areas. The unit is percent. The formula is (A / B) * 100, where A is part named by Certified accountants, B is whole named by Certified accountants. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Certified accountants on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-certified-accountants` (part named by Certified accountants)
- `metric.whole-named-by-certified-accountants` (whole named by Certified accountants)

Placements:

- organizational / functional / Human Resources / Organizational Function of Areas (sK464.8, page_0025)
- organizational / functional / Accounting / General (aK648, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profitable projects

- id: `kpi.management.profitable-projects`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profitable projects measures that result inside Management, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Profitable projects, B is whole named by Profitable projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profitable projects on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-profitable-projects` (part named by Profitable projects)
- `metric.whole-named-by-profitable-projects` (whole named by Profitable projects)

Placements:

- organizational / functional / Management / General (#K116, page_0045)
- organizational / functional / Accounting / General (aK416, page_0158)
- organizational / functional / Accounting / Business Consulting (#K416, page_0158)
- organizational / industries / Accounting / Engineering (sK416, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profit per project

- id: `kpi.management.profit-per-project`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profit per project measures that result inside Management, subcategory General. The unit is count. The formula is A / B, where A is Profit, B is project. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profit per project on the desired side of its target for this period?

Inputs:

- `metric.profit` (Profit)
- `metric.project` (project)

Placements:

- organizational / functional / Management / General (#K4658, page_0045)
- organizational / functional / Accounting / General (aK668, page_0158)
- organizational / industries / Accounting / Engineering (sK455, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4658, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Potential new clients contacted

- id: `kpi.sales-and-customer-service.potential-new-clients-contacted`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Potential new clients contacted measures that result inside Sales and Customer Service, subcategory Organizational > Functional Areas. The unit is count. The formula is A, where A is Potential new clients contacted. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Potential new clients contacted on the desired side of its target for this period?

Inputs:

- `metric.potential-new-clients-contacted` (Potential new clients contacted)

Placements:

- organizational / functional / Sales and Customer Service / Organizational > Functional Areas (sK6916, page_0052)
- organizational / functional / Accounting / General (aK6916, page_0158)
- organizational / functional / Accounting / Business Consulting (#K916, page_0158)
- organizational / industries / Media / Organizational » Industries (sE0516, page_0164)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Chargeable ratio

- id: `kpi.accounting.chargeable-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Chargeable ratio measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Chargeable ratio, B is base of Chargeable ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Chargeable ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-chargeable-ratio` (numerator of Chargeable ratio)
- `metric.base-of-chargeable-ratio` (base of Chargeable ratio)

Placements:

- organizational / functional / Accounting / General (aK014, page_0158)
- organizational / industries / Media / Recruitment/Employment Activities (sK014, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Backlog of commissioned projects

- id: `kpi.accounting.backlog-of-commissioned-projects`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Backlog of commissioned projects measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Backlog, B is commissioned projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Backlog of commissioned projects on the desired side of its target for this period?

Inputs:

- `metric.backlog` (Backlog)
- `metric.commissioned-projects` (commissioned projects)

Placements:

- organizational / functional / Accounting / General (aK016, page_0158)
- organizational / functional / Accounting / Business Consulting (#K106, page_0158)
- organizational / industries / Accounting / Engineering (sK106, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK016, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bill rate

- id: `kpi.accounting.bill-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bill rate measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Bill rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bill rate on the desired side of its target for this period?

Inputs:

- `metric.bill-rate` (Bill rate)

Placements:

- organizational / functional / Accounting / General (aK131, page_0158)
- organizational / functional / Accounting / Business Consulting (#K313, page_0158)
- organizational / industries / Accounting / Engineering (sK131, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Employee utilization rate

- id: `kpi.accounting.employee-utilization-rate`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Employee utilization rate measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of Employee utilization rate, B is base of Employee utilization rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Employee utilization rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-employee-utilization-rate` (numerator of Employee utilization rate)
- `metric.base-of-employee-utilization-rate` (base of Employee utilization rate)

Placements:

- organizational / functional / Accounting / General (aK320, page_0158)
- organizational / industries / Accounting / Engineering (sK320, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK220, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### No realization rate

- id: `kpi.accounting.no-realization-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

No realization rate measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is numerator of No realization rate, B is base of No realization rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is No realization rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-no-realization-rate` (numerator of No realization rate)
- `metric.base-of-no-realization-rate` (base of No realization rate)

Placements:

- organizational / functional / Accounting / General (aK321, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consultant retention by client

- id: `kpi.accounting.consultant-retention-by-client`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consultant retention by client measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Consultant retention by client, B is whole named by Consultant retention by client. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consultant retention by client on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-consultant-retention-by-client` (part named by Consultant retention by client)
- `metric.whole-named-by-consultant-retention-by-client` (whole named by Consultant retention by client)

Placements:

- organizational / functional / Accounting / General (aK115, page_0158)
- organizational / functional / Accounting / Business Consulting (#K315, page_0158)
- organizational / industries / Accounting / Engineering (sK415, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hourly fee

- id: `kpi.accounting.hourly-fee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hourly fee measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Hourly fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hourly fee on the desired side of its target for this period?

Inputs:

- `metric.hourly-fee` (Hourly fee)

Placements:

- organizational / functional / Accounting / General (aK417, page_0158)
- organizational / functional / Accounting / Business Consulting (#K317, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Successful financial audits

- id: `kpi.accounting.successful-financial-audits`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Successful financial audits measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Successful financial audits, B is whole named by Successful financial audits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Successful financial audits on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-successful-financial-audits` (part named by Successful financial audits)
- `metric.whole-named-by-successful-financial-audits` (whole named by Successful financial audits)

Placements:

- organizational / functional / Accounting / General (aK223, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fines received by clients

- id: `kpi.accounting.fines-received-by-clients`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fines received by clients measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Fines received by clients. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fines received by clients on the desired side of its target for this period?

Inputs:

- `metric.fines-received-by-clients` (Fines received by clients)

Placements:

- organizational / functional / Accounting / General (aK642, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reduction in mistakes

- id: `kpi.accounting.reduction-in-mistakes`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reduction in mistakes measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Reduction in mistakes, B is whole named by Reduction in mistakes. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reduction in mistakes on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-reduction-in-mistakes` (part named by Reduction in mistakes)
- `metric.whole-named-by-reduction-in-mistakes` (whole named by Reduction in mistakes)

Placements:

- organizational / functional / Accounting / General (aK643, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Successful fiscal controls

- id: `kpi.accounting.successful-fiscal-controls`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Successful fiscal controls measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Successful fiscal controls, B is whole named by Successful fiscal controls. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Successful fiscal controls on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-successful-fiscal-controls` (part named by Successful fiscal controls)
- `metric.whole-named-by-successful-fiscal-controls` (whole named by Successful fiscal controls)

Placements:

- organizational / functional / Accounting / General (aK644, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tax returns submitted in specified time

- id: `kpi.accounting.tax-returns-submitted-in-specified-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tax returns submitted in specified time measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Tax returns submitted in specified time, B is whole named by Tax returns submitted in specified time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tax returns submitted in specified time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-tax-returns-submitted-in-specified-time` (part named by Tax returns submitted in specified time)
- `metric.whole-named-by-tax-returns-submitted-in-specified-time` (whole named by Tax returns submitted in specified time)

Placements:

- organizational / functional / Accounting / General (aK645, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Clients with more than one service provided

- id: `kpi.accounting.clients-with-more-than-one-service-provided`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Clients with more than one service provided measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Clients with more than one service provided, B is whole named by Clients with more than one service provided. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Clients with more than one service provided on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-clients-with-more-than-one-service-provided` (part named by Clients with more than one service provided)
- `metric.whole-named-by-clients-with-more-than-one-service-provided` (whole named by Clients with more than one service provided)

Placements:

- organizational / functional / Accounting / General (aK646, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Knowledge of accounting and fiscal regulations

- id: `kpi.accounting.knowledge-of-accounting-and-fiscal-regulations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Knowledge of accounting and fiscal regulations measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Knowledge, B is accounting and fiscal regulations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Knowledge of accounting and fiscal regulations on the desired side of its target for this period?

Inputs:

- `metric.knowledge` (Knowledge)
- `metric.accounting-and-fiscal-regulations` (accounting and fiscal regulations)

Placements:

- organizational / functional / Accounting / General (aK649, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of services delivered

- id: `kpi.accounting.cost-of-services-delivered`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of services delivered measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Cost of services delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of services delivered on the desired side of its target for this period?

Inputs:

- `metric.cost-of-services-delivered` (Cost of services delivered)

Placements:

- organizational / functional / Accounting / General (aK650, page_0158)
- organizational / functional / Accounting / Business Consulting (#K603, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Delivery overhead costs

- id: `kpi.accounting.delivery-overhead-costs`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Delivery overhead costs measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Delivery overhead costs, B is whole named by Delivery overhead costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Delivery overhead costs on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-delivery-overhead-costs` (part named by Delivery overhead costs)
- `metric.whole-named-by-delivery-overhead-costs` (whole named by Delivery overhead costs)

Placements:

- organizational / functional / Accounting / General (aK651, page_0158)
- organizational / functional / Accounting / Business Consulting (#K651, page_0158)
- organizational / industries / Accounting / Engineering (sK451, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK1651, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adherence to schedule estimate

- id: `kpi.accounting.adherence-to-schedule-estimate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Adherence to schedule estimate measures that result inside Accounting, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Adherence, B is schedule estimate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adherence to schedule estimate on the desired side of its target for this period?

Inputs:

- `metric.adherence` (Adherence)
- `metric.schedule-estimate` (schedule estimate)

Placements:

- organizational / functional / Accounting / General (aK663, page_0158)
- organizational / industries / Media / Recruitment/Employment Activities (sK465, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Project assignment or work package duration

- id: `kpi.accounting.project-assignment-or-work-package-duration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Project assignment or work package duration measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Project assignment or work package duration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Project assignment or work package duration on the desired side of its target for this period?

Inputs:

- `metric.project-assignment-or-work-package-duration` (Project assignment or work package duration)

Placements:

- organizational / functional / Accounting / General (aK666, page_0158)
- organizational / industries / Media / Recruitment/Employment Activities (sK4656, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net revenue per technical staff

- id: `kpi.accounting.net-revenue-per-technical-staff`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net revenue per technical staff measures that result inside Accounting, subcategory General. The unit is currency. The formula is A / B, where A is Net revenue, B is technical staff. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net revenue per technical staff on the desired side of its target for this period?

Inputs:

- `metric.net-revenue` (Net revenue)
- `metric.technical-staff` (technical staff)

Placements:

- organizational / functional / Accounting / General (aK664, page_0158)
- organizational / functional / Accounting / Business Consulting (#K664, page_0158)
- organizational / industries / Accounting / Engineering (sK464, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4665, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue by practice

- id: `kpi.accounting.revenue-by-practice`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue by practice measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Revenue by practice. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue by practice on the desired side of its target for this period?

Inputs:

- `metric.revenue-by-practice` (Revenue by practice)

Placements:

- organizational / functional / Accounting / General (aK666, page_0158)
- organizational / functional / Accounting / Business Consulting (#K665, page_0158)
- organizational / industries / Accounting / Engineering (sK465, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4655, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Labor multiplier

- id: `kpi.accounting.labor-multiplier`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Labor multiplier measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Labor multiplier. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Labor multiplier on the desired side of its target for this period?

Inputs:

- `metric.labor-multiplier` (Labor multiplier)

Placements:

- organizational / functional / Accounting / General (aK672, page_0158)
- organizational / industries / Media / Recruitment/Employment Activities (sK4672, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Billable hours

- id: `kpi.accounting.billable-hours`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Billable hours measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Billable hours. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Billable hours on the desired side of its target for this period?

Inputs:

- `metric.billable-hours` (Billable hours)

Placements:

- organizational / functional / Accounting / General (aK673, page_0158)
- organizational / functional / Accounting / Business Consulting (#K703, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Blended rate

- id: `kpi.accounting.blended-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Blended rate measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Blended rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Blended rate on the desired side of its target for this period?

Inputs:

- `metric.blended-rate` (Blended rate)

Placements:

- organizational / functional / Accounting / General (aK671, page_0158)
- organizational / functional / Accounting / Business Consulting (#K710, page_0158)
- organizational / industries / Accounting / Engineering (sK710, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net fees

- id: `kpi.accounting.net-fees`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net fees measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Net fees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net fees on the desired side of its target for this period?

Inputs:

- `metric.net-fees` (Net fees)

Placements:

- organizational / functional / Accounting / General (aK713, page_0158)
- organizational / functional / Accounting / Business Consulting (#K713, page_0158)
- organizational / industries / Accounting / Engineering (sK713, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK4713, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net fees per FTE

- id: `kpi.accounting.net-fees-per-fte`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net fees per FTE measures that result inside Accounting, subcategory General. The unit is currency. The formula is A / B, where A is Net fees, B is FTE. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net fees per FTE on the desired side of its target for this period?

Inputs:

- `metric.net-fees` (Net fees)
- `metric.fte` (FTE)

Placements:

- organizational / functional / Accounting / General (aK714, page_0158)
- organizational / functional / Accounting / Business Consulting (#K714, page_0158)
- organizational / functional / Accounting / Business Consulting (#K715, page_0158)
- organizational / industries / Accounting / Engineering (sK714, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Research and preparation from chargeable time

- id: `kpi.accounting.research-and-preparation-from-chargeable-time`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Research and preparation from chargeable time measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Research and preparation from chargeable time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Research and preparation from chargeable time on the desired side of its target for this period?

Inputs:

- `metric.research-and-preparation-from-chargeable-time` (Research and preparation from chargeable time)

Placements:

- organizational / functional / Accounting / General (aK676, page_0158)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Travel time from chargeable time

- id: `kpi.accounting.travel-time-from-chargeable-time`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Travel time from chargeable time measures that result inside Accounting, subcategory General. The unit is currency. The formula is A, where A is Travel time from chargeable time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Travel time from chargeable time on the desired side of its target for this period?

Inputs:

- `metric.travel-time-from-chargeable-time` (Travel time from chargeable time)

Placements:

- organizational / functional / Accounting / General (aK6764, page_0158)
- organizational / functional / Accounting / Business Consulting (#K764, page_0158)
- organizational / industries / Accounting / Engineering (sK766, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

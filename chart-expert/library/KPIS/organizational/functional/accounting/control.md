# Accounting / Control

Context: organizational. Group: functional. KPIs: 9.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Bill and proposal costs

- id: `kpi.accounting.bill-and-proposal-costs`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.control`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bill and proposal costs measures that result inside Accounting, subcategory Control. The unit is number. The formula is A, where A is Bill and proposal costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bill and proposal costs on the desired side of its target for this period?

Inputs:

- `metric.bill-and-proposal-costs` (Bill and proposal costs)

Placements:

- organizational / functional / Accounting / Control (x8033, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Financial reports submitted as correct and on time

- id: `kpi.accounting.financial-reports-submitted-as-correct-and-on-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Financial reports submitted as correct and on time measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is part named by Financial reports submitted as correct and on time, B is whole named by Financial reports submitted as correct and on time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Financial reports submitted as correct and on time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-financial-reports-submitted-as-correct-and-on-time` (part named by Financial reports submitted as correct and on time)
- `metric.whole-named-by-financial-reports-submitted-as-correct-and-on-time` (whole named by Financial reports submitted as correct and on time)

Placements:

- organizational / functional / Accounting / Control (x3838, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non-compliance statements evolved

- id: `kpi.accounting.non-compliance-statements-evolved`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non-compliance statements evolved measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is part named by Non-compliance statements evolved, B is whole named by Non-compliance statements evolved. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non-compliance statements evolved on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-non-compliance-statements-evolved` (part named by Non-compliance statements evolved)
- `metric.whole-named-by-non-compliance-statements-evolved` (whole named by Non-compliance statements evolved)

Placements:

- organizational / functional / Accounting / Control (x8394, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time allocated to central financial data

- id: `kpi.accounting.time-allocated-to-central-financial-data`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time allocated to central financial data measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is Time allocated, B is central financial data. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time allocated to central financial data on the desired side of its target for this period?

Inputs:

- `metric.time-allocated` (Time allocated)
- `metric.central-financial-data` (central financial data)

Placements:

- organizational / functional / Accounting / Control (x8397, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time allocated to decision support

- id: `kpi.accounting.time-allocated-to-decision-support`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time allocated to decision support measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is Time allocated, B is decision support. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time allocated to decision support on the desired side of its target for this period?

Inputs:

- `metric.time-allocated` (Time allocated)
- `metric.decision-support` (decision support)

Placements:

- organizational / functional / Accounting / Control (x8398, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time allocated to financial management activities

- id: `kpi.accounting.time-allocated-to-financial-management-activities`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time allocated to financial management activities measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is Time allocated, B is financial management activities. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time allocated to financial management activities on the desired side of its target for this period?

Inputs:

- `metric.time-allocated` (Time allocated)
- `metric.financial-management-activities` (financial management activities)

Placements:

- organizational / functional / Accounting / Control (x8399, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Accuracy financial reports

- id: `kpi.accounting.accuracy-financial-reports`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Accuracy financial reports measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is part named by Accuracy financial reports, B is whole named by Accuracy financial reports. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Accuracy financial reports on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-accuracy-financial-reports` (part named by Accuracy financial reports)
- `metric.whole-named-by-accuracy-financial-reports` (whole named by Accuracy financial reports)

Placements:

- organizational / functional / Accounting / Control (x8402, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Economic value added per employee

- id: `kpi.accounting.economic-value-added-per-employee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Economic value added per employee measures that result inside Accounting, subcategory Control. The unit is percent. The formula is A / B, where A is Economic value added, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Economic value added per employee on the desired side of its target for this period?

Inputs:

- `metric.economic-value-added` (Economic value added)
- `metric.employee` (employee)

Placements:

- organizational / functional / Accounting / Control (x8448, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue leakage from total revenue

- id: `kpi.accounting.revenue-leakage-from-total-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.control`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue leakage from total revenue measures that result inside Accounting, subcategory Control. The unit is percent. The formula is (A / B) * 100, where A is Revenue leakage, B is total revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue leakage from total revenue on the desired side of its target for this period?

Inputs:

- `metric.revenue-leakage` (Revenue leakage)
- `metric.total-revenue` (total revenue)

Placements:

- organizational / functional / Accounting / Control (x8567, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

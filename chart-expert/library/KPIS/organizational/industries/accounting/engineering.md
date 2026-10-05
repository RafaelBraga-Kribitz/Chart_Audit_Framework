# Accounting / Engineering

Context: organizational. Group: industries. KPIs: 40.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

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

### Realization rate

- id: `kpi.accounting.realization-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Realization rate measures that result inside Accounting, subcategory Business Consulting. The unit is percent. The formula is (A / B) * 100, where A is numerator of Realization rate, B is base of Realization rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Realization rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-realization-rate` (numerator of Realization rate)
- `metric.base-of-realization-rate` (base of Realization rate)

Placements:

- organizational / functional / Accounting / Business Consulting (#K321, page_0158)
- organizational / industries / Accounting / Engineering (sK321, page_0159)
- organizational / industries / Media / Recruitment/Employment Activities (sK141, page_0163)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consulting hours sold

- id: `kpi.accounting.consulting-hours-sold`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.business-consulting`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consulting hours sold measures that result inside Accounting, subcategory Business Consulting. The unit is count. The formula is A, where A is Consulting hours sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consulting hours sold on the desired side of its target for this period?

Inputs:

- `metric.consulting-hours-sold` (Consulting hours sold)

Placements:

- organizational / functional / Accounting / Business Consulting (#K779, page_0158)
- organizational / industries / Accounting / Engineering (sK779, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Charges able ratio

- id: `kpi.accounting.charges-able-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Charges able ratio measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is numerator of Charges able ratio, B is base of Charges able ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Charges able ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-charges-able-ratio` (numerator of Charges able ratio)
- `metric.base-of-charges-able-ratio` (base of Charges able ratio)

Placements:

- organizational / industries / Accounting / Engineering (sK104, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Regression testing

- id: `kpi.accounting.regression-testing`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Regression testing measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Regression testing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Regression testing on the desired side of its target for this period?

Inputs:

- `metric.regression-testing` (Regression testing)

Placements:

- organizational / industries / Accounting / Engineering (sK397, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hourly fees

- id: `kpi.accounting.hourly-fees`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Hourly fees measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is part named by Hourly fees, B is whole named by Hourly fees. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hourly fees on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-hourly-fees` (part named by Hourly fees)
- `metric.whole-named-by-hourly-fees` (whole named by Hourly fees)

Placements:

- organizational / industries / Accounting / Engineering (sK417, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Consultant greening revenue

- id: `kpi.accounting.consultant-greening-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Consultant greening revenue measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is part named by Consultant greening revenue, B is whole named by Consultant greening revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Consultant greening revenue on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-consultant-greening-revenue` (part named by Consultant greening revenue)
- `metric.whole-named-by-consultant-greening-revenue` (whole named by Consultant greening revenue)

Placements:

- organizational / industries / Accounting / Engineering (sK418, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost of reviews delivered

- id: `kpi.accounting.cost-of-reviews-delivered`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost of reviews delivered measures that result inside Accounting, subcategory Engineering. The unit is currency. The formula is A, where A is Cost of reviews delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost of reviews delivered on the desired side of its target for this period?

Inputs:

- `metric.cost-of-reviews-delivered` (Cost of reviews delivered)

Placements:

- organizational / industries / Accounting / Engineering (sK450, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Periurement expenditure on work package duration

- id: `kpi.accounting.periurement-expenditure-on-work-package-duration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Periurement expenditure on work package duration measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Periurement expenditure on work package duration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Periurement expenditure on work package duration on the desired side of its target for this period?

Inputs:

- `metric.periurement-expenditure-on-work-package-duration` (Periurement expenditure on work package duration)

Placements:

- organizational / industries / Accounting / Engineering (sK454, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Solutions revenue

- id: `kpi.accounting.solutions-revenue`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Solutions revenue measures that result inside Accounting, subcategory Engineering. The unit is currency. The formula is A, where A is Solutions revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Solutions revenue on the desired side of its target for this period?

Inputs:

- `metric.solutions-revenue` (Solutions revenue)

Placements:

- organizational / industries / Accounting / Engineering (sK466, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Labour multiplier

- id: `kpi.accounting.labour-multiplier`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Labour multiplier measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Labour multiplier. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Labour multiplier on the desired side of its target for this period?

Inputs:

- `metric.labour-multiplier` (Labour multiplier)

Placements:

- organizational / industries / Accounting / Engineering (sK470, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Generations of product family concurrently worked on

- id: `kpi.accounting.generations-of-product-family-concurrently-worked-on`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Generations of product family concurrently worked on measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Generations of product family concurrently worked on. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Generations of product family concurrently worked on on the desired side of its target for this period?

Inputs:

- `metric.generations-of-product-family-concurrently-worked-on` (Generations of product family concurrently worked on)

Placements:

- organizational / industries / Accounting / Engineering (sK474, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Projects simultaneously worked on by a single person

- id: `kpi.accounting.projects-simultaneously-worked-on-by-a-single-person`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Projects simultaneously worked on by a single person measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Projects simultaneously worked on by a single person. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Projects simultaneously worked on by a single person on the desired side of its target for this period?

Inputs:

- `metric.projects-simultaneously-worked-on-by-a-single-person` (Projects simultaneously worked on by a single person)

Placements:

- organizational / industries / Accounting / Engineering (sK475, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Units of work signed off

- id: `kpi.accounting.units-of-work-signed-off`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Units of work signed off measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Units of work signed off. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Units of work signed off on the desired side of its target for this period?

Inputs:

- `metric.units-of-work-signed-off` (Units of work signed off)

Placements:

- organizational / industries / Accounting / Engineering (sK476, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Break-even time

- id: `kpi.accounting.break-even-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Break-even time measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Break-even time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Break-even time on the desired side of its target for this period?

Inputs:

- `metric.break-even-time` (Break-even time)

Placements:

- organizational / industries / Accounting / Engineering (sK477, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned to actual product development cycle time

- id: `kpi.accounting.planned-to-actual-product-development-cycle-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: operational
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Planned to actual product development cycle time measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is Planned, B is actual product development cycle time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned to actual product development cycle time on the desired side of its target for this period?

Inputs:

- `metric.planned` (Planned)
- `metric.actual-product-development-cycle-time` (actual product development cycle time)

Placements:

- organizational / industries / Accounting / Engineering (sK478, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Product development completion dates met

- id: `kpi.accounting.product-development-completion-dates-met`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Product development completion dates met measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is part named by Product development completion dates met, B is whole named by Product development completion dates met. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Product development completion dates met on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-product-development-completion-dates-met` (part named by Product development completion dates met)
- `metric.whole-named-by-product-development-completion-dates-met` (whole named by Product development completion dates met)

Placements:

- organizational / industries / Accounting / Engineering (sK490, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Planned jobs executed using the specified amount of labor

- id: `kpi.accounting.planned-jobs-executed-using-the-specified-amount-of-labor`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Planned jobs executed using the specified amount of labor measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is Planned jobs executed using the specified amount, B is labor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Planned jobs executed using the specified amount of labor on the desired side of its target for this period?

Inputs:

- `metric.planned-jobs-executed-using-the-specified-amount` (Planned jobs executed using the specified amount)
- `metric.labor` (labor)

Placements:

- organizational / industries / Accounting / Engineering (sK498, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Automation delivered by the product

- id: `kpi.accounting.automation-delivered-by-the-product`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Automation delivered by the product measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is part named by Automation delivered by the product, B is whole named by Automation delivered by the product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Automation delivered by the product on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-automation-delivered-by-the-product` (part named by Automation delivered by the product)
- `metric.whole-named-by-automation-delivered-by-the-product` (whole named by Automation delivered by the product)

Placements:

- organizational / industries / Accounting / Engineering (sK503, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Review rate

- id: `kpi.accounting.review-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Review rate measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Review rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Review rate on the desired side of its target for this period?

Inputs:

- `metric.review-rate` (Review rate)

Placements:

- organizational / industries / Accounting / Engineering (sK505, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ratio of design engineers to manufacturing engineers

- id: `kpi.accounting.ratio-of-design-engineers-to-manufacturing-engineers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ratio of design engineers to manufacturing engineers measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Ratio of design engineers to manufacturing engineers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ratio of design engineers to manufacturing engineers on the desired side of its target for this period?

Inputs:

- `metric.ratio-of-design-engineers-to-manufacturing-engineers` (Ratio of design engineers to manufacturing engineers)

Placements:

- organizational / industries / Accounting / Engineering (sK506, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ratio of engineering support staff to value adding engineers

- id: `kpi.accounting.ratio-of-engineering-support-staff-to-value-adding-engineers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ratio of engineering support staff to value adding engineers measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Ratio of engineering support staff to value adding engineers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ratio of engineering support staff to value adding engineers on the desired side of its target for this period?

Inputs:

- `metric.ratio-of-engineering-support-staff-to-value-adding-engineers` (Ratio of engineering support staff to value adding engineers)

Placements:

- organizational / industries / Accounting / Engineering (sK507, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tillable fees write-downs

- id: `kpi.accounting.tillable-fees-write-downs`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Tillable fees write-downs measures that result inside Accounting, subcategory Engineering. The unit is currency. The formula is A, where A is Tillable fees write-downs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tillable fees write-downs on the desired side of its target for this period?

Inputs:

- `metric.tillable-fees-write-downs` (Tillable fees write-downs)

Placements:

- organizational / industries / Accounting / Engineering (sK715, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Package quality charges

- id: `kpi.accounting.package-quality-charges`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Package quality charges measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Package quality charges. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Package quality charges on the desired side of its target for this period?

Inputs:

- `metric.package-quality-charges` (Package quality charges)

Placements:

- organizational / industries / Accounting / Engineering (sK210, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Engineering technical adequacy

- id: `kpi.accounting.engineering-technical-adequacy`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Engineering technical adequacy measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Engineering technical adequacy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Engineering technical adequacy on the desired side of its target for this period?

Inputs:

- `metric.engineering-technical-adequacy` (Engineering technical adequacy)

Placements:

- organizational / industries / Accounting / Engineering (sK210, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Organizational quality clock

- id: `kpi.accounting.organizational-quality-clock`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Organizational quality clock measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Organizational quality clock. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Organizational quality clock on the desired side of its target for this period?

Inputs:

- `metric.organizational-quality-clock` (Organizational quality clock)

Placements:

- organizational / industries / Accounting / Engineering (sK2108, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Plant engineering personnel error rate

- id: `kpi.accounting.plant-engineering-personnel-error-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.engineering`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Plant engineering personnel error rate measures that result inside Accounting, subcategory Engineering. The unit is percent. The formula is (A / B) * 100, where A is numerator of Plant engineering personnel error rate, B is base of Plant engineering personnel error rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Plant engineering personnel error rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-plant-engineering-personnel-error-rate` (numerator of Plant engineering personnel error rate)
- `metric.base-of-plant-engineering-personnel-error-rate` (base of Plant engineering personnel error rate)

Placements:

- organizational / industries / Accounting / Engineering (sK2110, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unplanned change package revisions due to design errors

- id: `kpi.accounting.unplanned-change-package-revisions-due-to-design-errors`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.engineering`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unplanned change package revisions due to design errors measures that result inside Accounting, subcategory Engineering. The unit is count. The formula is A, where A is Unplanned change package revisions due to design errors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unplanned change package revisions due to design errors on the desired side of its target for this period?

Inputs:

- `metric.unplanned-change-package-revisions-due-to-design-errors` (Unplanned change package revisions due to design errors)

Placements:

- organizational / industries / Accounting / Engineering (sK2110, page_0159)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

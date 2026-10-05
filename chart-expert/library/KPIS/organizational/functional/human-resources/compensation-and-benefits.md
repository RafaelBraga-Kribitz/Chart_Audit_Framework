# Human Resources / Compensation and Benefits

Context: organizational. Group: functional. KPIs: 12.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Compensation per employee

- id: `kpi.human-resources.compensation-per-employee`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Compensation per employee measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is number. The formula is A / B, where A is Compensation, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compensation per employee on the desired side of its target for this period?

Inputs:

- `metric.compensation` (Compensation)
- `metric.employee` (employee)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK46, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Compensation revenue rate

- id: `kpi.human-resources.compensation-revenue-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Compensation revenue rate measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is percent. The formula is (A / B) * 100, where A is numerator of Compensation revenue rate, B is base of Compensation revenue rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compensation revenue rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-compensation-revenue-rate` (numerator of Compensation revenue rate)
- `metric.base-of-compensation-revenue-rate` (base of Compensation revenue rate)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK53, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Entry level wage to local minimum wage

- id: `kpi.human-resources.entry-level-wage-to-local-minimum-wage`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Entry level wage to local minimum wage measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is count. The formula is A, where A is Entry level wage to local minimum wage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Entry level wage to local minimum wage on the desired side of its target for this period?

Inputs:

- `metric.entry-level-wage-to-local-minimum-wage` (Entry level wage to local minimum wage)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK85, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Means payout

- id: `kpi.human-resources.means-payout`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: average
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Means payout measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is currency. The formula is A / B, where A is sum underlying Means payout, B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Means payout on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-means-payout` (sum underlying Means payout)
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK86, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Actual or potential bonus paid

- id: `kpi.human-resources.actual-or-potential-bonus-paid`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Actual or potential bonus paid measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is percent. The formula is (A / B) * 100, where A is part named by Actual or potential bonus paid, B is whole named by Actual or potential bonus paid. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Actual or potential bonus paid on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-actual-or-potential-bonus-paid` (part named by Actual or potential bonus paid)
- `metric.whole-named-by-actual-or-potential-bonus-paid` (whole named by Actual or potential bonus paid)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK175, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Compensation and benefits cost to annual sales turnover

- id: `kpi.human-resources.compensation-and-benefits-cost-to-annual-sales-turnover`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Compensation and benefits cost to annual sales turnover measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is percent. The formula is (A / B) * 100, where A is Compensation and benefits cost, B is annual sales turnover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compensation and benefits cost to annual sales turnover on the desired side of its target for this period?

Inputs:

- `metric.compensation-and-benefits-cost` (Compensation and benefits cost)
- `metric.annual-sales-turnover` (annual sales turnover)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK715, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Wage rate

- id: `kpi.human-resources.wage-rate`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Wage rate measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is currency. The formula is A, where A is Wage rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wage rate on the desired side of its target for this period?

Inputs:

- `metric.wage-rate` (Wage rate)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK726, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Social insurance cost per employee

- id: `kpi.human-resources.social-insurance-cost-per-employee`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Social insurance cost per employee measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is currency. The formula is A / B, where A is Social insurance cost, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Social insurance cost per employee on the desired side of its target for this period?

Inputs:

- `metric.social-insurance-cost` (Social insurance cost)
- `metric.employee` (employee)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK728, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical insurance cost per employee

- id: `kpi.human-resources.medical-insurance-cost-per-employee`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Medical insurance cost per employee measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is currency. The formula is A / B, where A is Medical insurance cost, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical insurance cost per employee on the desired side of its target for this period?

Inputs:

- `metric.medical-insurance-cost` (Medical insurance cost)
- `metric.employee` (employee)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK729, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Hourly compensation per employee

- id: `kpi.human-resources.hourly-compensation-per-employee`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Hourly compensation per employee measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is currency. The formula is A / B, where A is Hourly compensation, B is employee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Hourly compensation per employee on the desired side of its target for this period?

Inputs:

- `metric.hourly-compensation` (Hourly compensation)
- `metric.employee` (employee)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK731, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Income per employee by position

- id: `kpi.human-resources.income-per-employee-by-position`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: operational
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Income per employee by position measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is currency. The formula is A / B, where A is Income, B is employee by position. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Income per employee by position on the desired side of its target for this period?

Inputs:

- `metric.income` (Income)
- `metric.employee-by-position` (employee by position)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK731, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Workforce on individual employment contracts

- id: `kpi.human-resources.workforce-on-individual-employment-contracts`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.human-resources.compensation-and-benefits`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Workforce on individual employment contracts measures that result inside Human Resources, subcategory Compensation and Benefits. The unit is percent. The formula is (A / B) * 100, where A is part named by Workforce on individual employment contracts, B is whole named by Workforce on individual employment contracts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Workforce on individual employment contracts on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-workforce-on-individual-employment-contracts` (part named by Workforce on individual employment contracts)
- `metric.whole-named-by-workforce-on-individual-employment-contracts` (whole named by Workforce on individual employment contracts)

Placements:

- organizational / functional / Human Resources / Compensation and Benefits (sK737, page_0021)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

# Finance / Profitability

Context: organizational. Group: functional. KPIs: 5.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Revenue per employee

- id: `kpi.finance.revenue-per-employee`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.finance.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue divided by headcount. Placed under Finance / Profitability.

Questions: Is Revenue per employee on the desired side of its target for this period?

Inputs:

- `metric.revenue` (revenue)
- `metric.employees` (employees)

Placements:

- organizational / functional / Finance / Profitability (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Net revenue minus CAC

- id: `kpi.finance.net-revenue-minus-cac`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A - B`
- formula type: difference
- dashboard: `dash.finance.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net revenue left after acquisition cost. Placed under Finance / Profitability.

Questions: Is Net revenue minus CAC on the desired side of its target for this period?

Inputs:

- `metric.net-revenue` (net revenue)
- `metric.customer-acquisition-cost` (customer acquisition cost)

Placements:

- organizational / functional / Finance / Profitability (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### LTV to CAC ratio

- id: `kpi.finance.ltv-to-cac-ratio`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.finance.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

How many times acquisition cost is covered by lifetime value. Placed under Finance / Profitability.

Questions: Is LTV to CAC ratio on the desired side of its target for this period?

Inputs:

- `metric.customer-lifetime-value` (customer lifetime value)
- `metric.customer-acquisition-cost` (customer acquisition cost)

Placements:

- organizational / functional / Finance / Profitability (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Net profit

- id: `kpi.finance.net-profit`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A - B`
- formula type: difference
- dashboard: `dash.finance.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

What remains after costs. Placed under Finance / Profitability.

Questions: Is Net profit on the desired side of its target for this period?

Inputs:

- `metric.revenue` (revenue)
- `metric.total-costs` (total costs)

Placements:

- organizational / functional / Finance / Profitability (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Monthly recurring profit

- id: `kpi.finance.monthly-recurring-profit`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.finance.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Recurring profit normalized to one month. Placed under Finance / Profitability.

Questions: Is Monthly recurring profit on the desired side of its target for this period?

Inputs:

- `metric.recurring-profit-for-the-month` (recurring profit for the month)

Placements:

- organizational / functional / Finance / Profitability (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

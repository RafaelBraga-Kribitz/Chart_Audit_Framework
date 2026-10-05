# Sales and Customer Service / Customers

Context: organizational. Group: functional. KPIs: 4.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Customer interviews

- id: `kpi.sales-and-customer-service.customer-interviews`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customers`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Completed interviews with customers in the period. An activity count; pair it with an outcome such as retention or NPS. Placed under Sales and Customer Service / Customers.

Questions: Is Customer interviews on the desired side of its target for this period?

Inputs:

- `metric.customer-interviews-completed` (customer interviews completed)

Placements:

- organizational / functional / Sales and Customer Service / Customers (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Weekly active users

- id: `kpi.sales-and-customer-service.weekly-active-users`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customers`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of customers who used the product in the week. Placed under Sales and Customer Service / Customers.

Questions: Is Weekly active users on the desired side of its target for this period?

Inputs:

- `metric.customers-active-in-the-week` (customers active in the week)
- `metric.customers` (customers)

Placements:

- organizational / functional / Sales and Customer Service / Customers (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Accounts with health score

- id: `kpi.sales-and-customer-service.accounts-with-health-score`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customers`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of active accounts with a health score inside the freshness window. Placed under Sales and Customer Service / Customers.

Questions: Is Accounts with health score on the desired side of its target for this period?

Inputs:

- `metric.accounts-with-a-current-health-score` (accounts with a current health score)
- `metric.active-accounts` (active accounts)

Placements:

- organizational / functional / Sales and Customer Service / Customers (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### At risk accounts contacted

- id: `kpi.sales-and-customer-service.at-risk-accounts-contacted`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customers`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of accounts flagged at risk that were contacted in the window. Placed under Sales and Customer Service / Customers.

Questions: Is At risk accounts contacted on the desired side of its target for this period?

Inputs:

- `metric.flagged-accounts-contacted` (flagged accounts contacted)
- `metric.accounts-flagged-at-risk` (accounts flagged at risk)

Placements:

- organizational / functional / Sales and Customer Service / Customers (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

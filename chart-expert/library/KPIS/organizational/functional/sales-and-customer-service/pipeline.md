# Sales and Customer Service / Pipeline

Context: organizational. Group: functional. KPIs: 7.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Closed won rate

- id: `kpi.sales-and-customer-service.closed-won-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Wins divided by decisions. Placed under Sales and Customer Service / Pipeline.

Questions: Is Closed won rate on the desired side of its target for this period?

Inputs:

- `metric.deals-won` (deals won)
- `metric.deals-closed` (deals closed)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Average deal size

- id: `kpi.sales-and-customer-service.average-deal-size`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Closed-won revenue divided by closed-won deals. Placed under Sales and Customer Service / Pipeline.

Questions: Is Average deal size on the desired side of its target for this period?

Inputs:

- `metric.closed-won-revenue` (closed-won revenue)
- `metric.closed-won-deals` (closed-won deals)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Pipeline created

- id: `kpi.sales-and-customer-service.pipeline-created`
- kind: kpi
- unit: currency
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of opportunities created in the period, on the stated stage rule. Placed under Sales and Customer Service / Pipeline.

Questions: Is Pipeline created on the desired side of its target for this period?

Inputs:

- `metric.new-pipeline-value` (new pipeline value)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Product demos

- id: `kpi.sales-and-customer-service.product-demos`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Demos delivered, not demos scheduled. Placed under Sales and Customer Service / Pipeline.

Questions: Is Product demos on the desired side of its target for this period?

Inputs:

- `metric.demos-delivered` (demos delivered)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Coaching sessions

- id: `kpi.sales-and-customer-service.coaching-sessions`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Coaching sessions held. Pair with a pipeline or win-rate outcome. Placed under Sales and Customer Service / Pipeline.

Questions: Is Coaching sessions on the desired side of its target for this period?

Inputs:

- `metric.coaching-sessions-held` (coaching sessions held)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### New accounts

- id: `kpi.sales-and-customer-service.new-accounts`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Named accounts opened in the period. Placed under Sales and Customer Service / Pipeline.

Questions: Is New accounts on the desired side of its target for this period?

Inputs:

- `metric.new-named-accounts` (new named accounts)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Sales qualified leads

- id: `kpi.sales-and-customer-service.sales-qualified-leads`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.pipeline`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Leads sales accepted under the written qualification rule. Placed under Sales and Customer Service / Pipeline.

Questions: Is Sales qualified leads on the desired side of its target for this period?

Inputs:

- `metric.leads-accepted-by-sales` (leads accepted by sales)

Placements:

- organizational / functional / Sales and Customer Service / Pipeline (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

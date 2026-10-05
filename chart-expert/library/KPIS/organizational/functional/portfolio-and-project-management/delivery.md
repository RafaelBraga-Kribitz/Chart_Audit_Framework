# Portfolio and Project Management / Delivery

Context: organizational. Group: functional. KPIs: 5.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Billed versus expected

- id: `kpi.portfolio-and-project-management.billed-versus-expected`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.portfolio-and-project-management.delivery`
- analysis chart: `scatter-plot` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

What was billed divided by what the plan said would be billed. Placed under Portfolio and Project Management / Delivery.

Questions: Is Billed versus expected on the desired side of its target for this period?

Inputs:

- `metric.amount-billed` (amount billed)
- `metric.amount-expected` (amount expected)

Placements:

- organizational / functional / Portfolio and Project Management / Delivery (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Project contribution margin

- id: `kpi.portfolio-and-project-management.project-contribution-margin`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.portfolio-and-project-management.delivery`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of project revenue left after direct delivery cost. Placed under Portfolio and Project Management / Delivery.

Questions: Is Project contribution margin on the desired side of its target for this period?

Inputs:

- `metric.project-revenue-minus-direct-cost` (project revenue minus direct cost)
- `metric.project-revenue` (project revenue)

Placements:

- organizational / functional / Portfolio and Project Management / Delivery (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Estimated versus actual project time

- id: `kpi.portfolio-and-project-management.estimated-versus-actual-project-time`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.portfolio-and-project-management.delivery`
- analysis chart: `scatter-plot` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Estimated hours divided by actual hours. Above 100 means the work took fewer hours than estimated. Placed under Portfolio and Project Management / Delivery.

Questions: Is Estimated versus actual project time on the desired side of its target for this period?

Inputs:

- `metric.estimated-hours` (estimated hours)
- `metric.actual-hours` (actual hours)

Placements:

- organizational / functional / Portfolio and Project Management / Delivery (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Estimated versus actual project cost

- id: `kpi.portfolio-and-project-management.estimated-versus-actual-project-cost`
- kind: kpi
- unit: percent
- direction: corridor
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.portfolio-and-project-management.delivery`
- analysis chart: `scatter-plot` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Estimated cost divided by actual cost. Placed under Portfolio and Project Management / Delivery.

Questions: Is Estimated versus actual project cost on the desired side of its target for this period?

Inputs:

- `metric.estimated-cost` (estimated cost)
- `metric.actual-cost` (actual cost)

Placements:

- organizational / functional / Portfolio and Project Management / Delivery (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Lead time per project

- id: `kpi.portfolio-and-project-management.lead-time-per-project`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.portfolio-and-project-management.delivery`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calendar time a project takes. Placed under Portfolio and Project Management / Delivery.

Questions: Is Lead time per project on the desired side of its target for this period?

Inputs:

- `metric.elapsed-time-from-start-to-finish` (elapsed time from start to finish)

Placements:

- organizational / functional / Portfolio and Project Management / Delivery (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

# Professional Services / Clients

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Client breakeven

- id: `kpi.professional-services.client-breakeven`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.professional-services.clients`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

How long until the client covers the cost to serve and acquire them. Placed under Professional Services / Clients.

Questions: Is Client breakeven on the desired side of its target for this period?

Inputs:

- `metric.months-or-revenue-until-client-contribution-turns-positive` (months or revenue until client contribution turns positive)

Placements:

- organizational / functional / Professional Services / Clients (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Client ROI

- id: `kpi.professional-services.client-roi`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.professional-services.clients`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profit from the client divided by the cost to serve them. Placed under Professional Services / Clients.

Questions: Is Client ROI on the desired side of its target for this period?

Inputs:

- `metric.client-profit` (client profit)
- `metric.cost-to-serve-the-client` (cost to serve the client)

Placements:

- organizational / functional / Professional Services / Clients (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

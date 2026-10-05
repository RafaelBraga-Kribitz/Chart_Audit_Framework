# Marketing and Communications / Community

Context: organizational. Group: functional. KPIs: 3.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Community page visits

- id: `kpi.marketing-and-communications.community-page-visits`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.community`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Visits to community pages in the period. Placed under Marketing and Communications / Community.

Questions: Is Community page visits on the desired side of its target for this period?

Inputs:

- `metric.community-page-visits` (community page visits)

Placements:

- organizational / functional / Marketing and Communications / Community (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Community participation rate

- id: `kpi.marketing-and-communications.community-participation-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.marketing-and-communications.community`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Share of customers who did something in the community beyond a visit. Placed under Marketing and Communications / Community.

Questions: Is Community participation rate on the desired side of its target for this period?

Inputs:

- `metric.customers-who-participated` (customers who participated)
- `metric.customers` (customers)

Placements:

- organizational / functional / Marketing and Communications / Community (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Experts contacted

- id: `kpi.marketing-and-communications.experts-contacted`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.community`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Experts contacted. Contact is an activity; publication is the result. Placed under Marketing and Communications / Community.

Questions: Is Experts contacted on the desired side of its target for this period?

Inputs:

- `metric.experts-contacted` (experts contacted)

Placements:

- organizational / functional / Marketing and Communications / Community (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

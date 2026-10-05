# Finance / Planning

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Budgets reviewed

- id: `kpi.finance.budgets-reviewed`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.finance.planning`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Function budgets reviewed against the request. A process count, not the financial outcome. Placed under Finance / Planning.

Questions: Is Budgets reviewed on the desired side of its target for this period?

Inputs:

- `metric.function-budgets-reviewed` (function budgets reviewed)

Placements:

- organizational / functional / Finance / Planning (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

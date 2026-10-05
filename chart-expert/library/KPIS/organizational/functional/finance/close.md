# Finance / Close

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Days to close

- id: `kpi.finance.days-to-close`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.finance.close`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Business days from period end until the books are closed. Placed under Finance / Close.

Questions: Is Days to close on the desired side of its target for this period?

Inputs:

- `metric.business-days-from-period-end-to-close` (business days from period end to close)

Placements:

- organizational / functional / Finance / Close (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

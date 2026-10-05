# Information Technology / Reliability

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Unplanned downtime

- id: `kpi.information-technology.unplanned-downtime`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.reliability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Duration of unplanned unavailability in the period. Placed under Information Technology / Reliability.

Questions: Is Unplanned downtime on the desired side of its target for this period?

Inputs:

- `metric.unplanned-downtime-duration` (unplanned downtime duration)

Placements:

- organizational / functional / Information Technology / Reliability (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Restore tests passed

- id: `kpi.information-technology.restore-tests-passed`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.information-technology.reliability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Development, Data Scientist
- provenance: authored

Backup restore tests that passed the agreed check. Placed under Information Technology / Reliability.

Questions: Is Restore tests passed on the desired side of its target for this period?

Inputs:

- `metric.restore-tests-passed` (restore tests passed)

Placements:

- organizational / functional / Information Technology / Reliability (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

# Professional Services / Business Development

Context: organizational. Group: functional. KPIs: 1.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Lead to client conversion rate

- id: `kpi.professional-services.lead-to-client-conversion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.professional-services.business-development`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of leads that become clients. Placed under Professional Services / Business Development.

Questions: Is Lead to client conversion rate on the desired side of its target for this period?

Inputs:

- `metric.clients-won` (clients won)
- `metric.leads` (leads)

Placements:

- organizational / functional / Professional Services / Business Development (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

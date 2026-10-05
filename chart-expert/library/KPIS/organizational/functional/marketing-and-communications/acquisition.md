# Marketing and Communications / Acquisition

Context: organizational. Group: functional. KPIs: 3.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Wins by lead source

- id: `kpi.marketing-and-communications.wins-by-lead-source`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.acquisition`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Closed work split by the source of the lead. Placed under Marketing and Communications / Acquisition.

Questions: Is Wins by lead source on the desired side of its target for this period?

Inputs:

- `metric.wins-coded-to-a-lead-source` (wins coded to a lead source)

Placements:

- organizational / functional / Marketing and Communications / Acquisition (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Click through rate

- id: `kpi.marketing-and-communications.click-through-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.marketing-and-communications.acquisition`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Clicks divided by impressions. Placed under Marketing and Communications / Acquisition.

Questions: Is Click through rate on the desired side of its target for this period?

Inputs:

- `metric.clicks` (clicks)
- `metric.impressions` (impressions)

Placements:

- organizational / functional / Marketing and Communications / Acquisition (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Marketing qualified leads

- id: `kpi.marketing-and-communications.marketing-qualified-leads`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.acquisition`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Leads that meet the written qualification rule. Say the channel when the result is channel-specific. Placed under Marketing and Communications / Acquisition.

Questions: Is Marketing qualified leads on the desired side of its target for this period?

Inputs:

- `metric.leads-meeting-the-qualification-rule` (leads meeting the qualification rule)

Placements:

- organizational / functional / Marketing and Communications / Acquisition (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

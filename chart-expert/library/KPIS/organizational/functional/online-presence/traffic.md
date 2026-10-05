# Online Presence / Traffic

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Website visitors

- id: `kpi.online-presence.website-visitors`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.traffic`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

People or sessions on the site. A leading input, not the outcome. Placed under Online Presence / Traffic.

Questions: Is Website visitors on the desired side of its target for this period?

Inputs:

- `metric.sessions-or-users-in-the-period` (sessions or users in the period)

Placements:

- organizational / functional / Online Presence / Traffic (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Referring domains

- id: `kpi.online-presence.referring-domains`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.traffic`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Distinct sites that newly link to the property in the period. Placed under Online Presence / Traffic.

Questions: Is Referring domains on the desired side of its target for this period?

Inputs:

- `metric.new-referring-domains` (new referring domains)

Placements:

- organizational / functional / Online Presence / Traffic (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

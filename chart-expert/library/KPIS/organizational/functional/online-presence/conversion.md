# Online Presence / Conversion

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Landing page conversion rate

- id: `kpi.online-presence.landing-page-conversion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.conversion`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Conversions divided by visits to the page. Placed under Online Presence / Conversion.

Questions: Is Landing page conversion rate on the desired side of its target for this period?

Inputs:

- `metric.conversions` (conversions)
- `metric.landing-page-visits` (landing page visits)

Placements:

- organizational / functional / Online Presence / Conversion (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Pages meeting speed budget

- id: `kpi.online-presence.pages-meeting-speed-budget`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.online-presence.conversion`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Pages whose measured speed is inside the agreed budget. Placed under Online Presence / Conversion.

Questions: Is Pages meeting speed budget on the desired side of its target for this period?

Inputs:

- `metric.pages-inside-the-speed-budget` (pages inside the speed budget)

Placements:

- organizational / functional / Online Presence / Conversion (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

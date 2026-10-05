# Marketing and Communications / Content

Context: organizational. Group: functional. KPIs: 5.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Email click through rate

- id: `kpi.marketing-and-communications.email-click-through-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.marketing-and-communications.content`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Clicks divided by emails delivered. Placed under Marketing and Communications / Content.

Questions: Is Email click through rate on the desired side of its target for this period?

Inputs:

- `metric.clicks` (clicks)
- `metric.emails-delivered` (emails delivered)

Placements:

- organizational / functional / Marketing and Communications / Content (user-note, note)

Target notes:

- None.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Newsletters published

- id: `kpi.marketing-and-communications.newsletters-published`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.content`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Issues actually sent. A task count; pair it with click-through or pipeline. Placed under Marketing and Communications / Content.

Questions: Is Newsletters published on the desired side of its target for this period?

Inputs:

- `metric.newsletter-issues-published` (newsletter issues published)

Placements:

- organizational / functional / Marketing and Communications / Content (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Blog posts published

- id: `kpi.marketing-and-communications.blog-posts-published`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.content`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Posts published in the period. Placed under Marketing and Communications / Content.

Questions: Is Blog posts published on the desired side of its target for this period?

Inputs:

- `metric.posts-published` (posts published)

Placements:

- organizational / functional / Marketing and Communications / Content (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Expert interviews

- id: `kpi.marketing-and-communications.expert-interviews`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.content`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

Interviews published, not conversations merely scheduled. Placed under Marketing and Communications / Content.

Questions: Is Expert interviews on the desired side of its target for this period?

Inputs:

- `metric.expert-interviews-published` (expert interviews published)

Placements:

- organizational / functional / Marketing and Communications / Content (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Blog subscribers

- id: `kpi.marketing-and-communications.blog-subscribers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.marketing-and-communications.content`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

People subscribed to the blog at period end. Placed under Marketing and Communications / Content.

Questions: Is Blog subscribers on the desired side of its target for this period?

Inputs:

- `metric.subscribers` (subscribers)

Placements:

- organizational / functional / Marketing and Communications / Content (user-note, note)

Target notes:

- None.

Pitfall: An activity count is a weak key result on its own. Pair it with the outcome it is supposed to move. Do not brief the analysis chart to an executive if the communication chart already answers the decision.

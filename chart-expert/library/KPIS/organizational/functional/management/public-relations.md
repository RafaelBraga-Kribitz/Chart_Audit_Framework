# Management / Public Relations

Context: organizational. Group: functional. KPIs: 31.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Community satisfaction index

- id: `kpi.management.community-satisfaction-index`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: index
- dashboard: `dash.management.corporate-social-responsibility`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Community satisfaction index measures that result inside Management, subcategory Corporate Social Responsibility. The unit is count. The formula is (A / B) * 100, where A is current Community satisfaction index, B is base-period Community satisfaction index. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Community satisfaction index on the desired side of its target for this period?

Inputs:

- `metric.current-community-satisfaction-index` (current Community satisfaction index)
- `metric.base-period-community-satisfaction-index` (base-period Community satisfaction index)

Placements:

- organizational / functional / Management / Corporate Social Responsibility (sK1379, page_0013)
- organizational / functional / Management / Public Relations (sK1379, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sponsorship projects

- id: `kpi.management.sponsorship-projects`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.corporate-social-responsibility`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sponsorship projects measures that result inside Management, subcategory Corporate Social Responsibility. The unit is count. The formula is A, where A is Sponsorship projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sponsorship projects on the desired side of its target for this period?

Inputs:

- `metric.sponsorship-projects` (Sponsorship projects)

Placements:

- organizational / functional / Management / Corporate Social Responsibility (sK1387, page_0013)
- organizational / functional / Management / Public Relations (sK1387, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Entries to environment / community awards

- id: `kpi.management.entries-to-environment-community-awards`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.environmental-care`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Entries to environment / community awards measures that result inside Management, subcategory Environmental Care. The unit is count. The formula is A, where A is Entries to environment / community awards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Entries to environment / community awards on the desired side of its target for this period?

Inputs:

- `metric.entries-to-environment-community-awards` (Entries to environment / community awards)

Placements:

- organizational / functional / Management / Environmental Care (sK1382, page_0014)
- organizational / functional / Management / Public Relations (sK1382, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marketing projects that are environmentally friendly

- id: `kpi.management.marketing-projects-that-are-environmentally-friendly`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.environmental-care`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marketing projects that are environmentally friendly measures that result inside Management, subcategory Environmental Care. The unit is percent. The formula is (A / B) * 100, where A is part named by Marketing projects that are environmentally friendly, B is whole named by Marketing projects that are environmentally friendly. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marketing projects that are environmentally friendly on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-marketing-projects-that-are-environmentally-friendly` (part named by Marketing projects that are environmentally friendly)
- `metric.whole-named-by-marketing-projects-that-are-environmentally-friendly` (whole named by Marketing projects that are environmentally friendly)

Placements:

- organizational / functional / Management / Environmental Care (sK1389, page_0014)
- organizational / functional / Management / Public Relations (sK1389, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Marketing spend of revenues

- id: `kpi.management.marketing-spend-of-revenues`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Marketing spend of revenues measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is Marketing spend, B is revenues. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Marketing spend of revenues on the desired side of its target for this period?

Inputs:

- `metric.marketing-spend` (Marketing spend)
- `metric.revenues` (revenues)

Placements:

- organizational / functional / Management / Public Relations (sK1323, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Local residents in out workforce

- id: `kpi.management.local-residents-in-out-workforce`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Local residents in out workforce measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Local residents in out workforce, B is whole named by Local residents in out workforce. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Local residents in out workforce on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-local-residents-in-out-workforce` (part named by Local residents in out workforce)
- `metric.whole-named-by-local-residents-in-out-workforce` (whole named by Local residents in out workforce)

Placements:

- organizational / functional / Management / Public Relations (sK1381, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Media coverage events

- id: `kpi.management.media-coverage-events`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Media coverage events measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Media coverage events. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Media coverage events on the desired side of its target for this period?

Inputs:

- `metric.media-coverage-events` (Media coverage events)

Placements:

- organizational / functional / Management / Public Relations (sK1385, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Photos in papers

- id: `kpi.management.photos-in-papers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Photos in papers measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Photos in papers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Photos in papers on the desired side of its target for this period?

Inputs:

- `metric.photos-in-papers` (Photos in papers)

Placements:

- organizational / functional / Management / Public Relations (sK1386, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Task- hour participation

- id: `kpi.management.task-hour-participation`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Task- hour participation measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Task- hour participation, B is whole named by Task- hour participation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Task- hour participation on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-task-hour-participation` (part named by Task- hour participation)
- `metric.whole-named-by-task-hour-participation` (whole named by Task- hour participation)

Placements:

- organizational / functional / Management / Public Relations (sK1390, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Industry analysts coverage volume

- id: `kpi.management.industry-analysts-coverage-volume`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Industry analysts coverage volume measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Industry analysts coverage volume. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Industry analysts coverage volume on the desired side of its target for this period?

Inputs:

- `metric.industry-analysts-coverage-volume` (Industry analysts coverage volume)

Placements:

- organizational / functional / Management / Public Relations (sK1391, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Industry analyst recommendations

- id: `kpi.management.industry-analyst-recommendations`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Industry analyst recommendations measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Industry analyst recommendations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Industry analyst recommendations on the desired side of its target for this period?

Inputs:

- `metric.industry-analyst-recommendations` (Industry analyst recommendations)

Placements:

- organizational / functional / Management / Public Relations (sK1392, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Keynote speeches

- id: `kpi.management.keynote-speeches`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Keynote speeches measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Keynote speeches. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Keynote speeches on the desired side of its target for this period?

Inputs:

- `metric.keynote-speeches` (Keynote speeches)

Placements:

- organizational / functional / Management / Public Relations (sK1393, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Media coverage quality

- id: `kpi.management.media-coverage-quality`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Media coverage quality measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Media coverage quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Media coverage quality on the desired side of its target for this period?

Inputs:

- `metric.media-coverage-quality` (Media coverage quality)

Placements:

- organizational / functional / Management / Public Relations (sK1394, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Special events

- id: `kpi.management.special-events`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Special events measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Special events. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Special events on the desired side of its target for this period?

Inputs:

- `metric.special-events` (Special events)

Placements:

- organizational / functional / Management / Public Relations (sK1396, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Negative buzz

- id: `kpi.management.negative-buzz`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Negative buzz measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Negative buzz, B is whole named by Negative buzz. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Negative buzz on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-negative-buzz` (part named by Negative buzz)
- `metric.whole-named-by-negative-buzz` (whole named by Negative buzz)

Placements:

- organizational / functional / Management / Public Relations (sK1397, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Positive buzz

- id: `kpi.management.positive-buzz`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Positive buzz measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Positive buzz, B is whole named by Positive buzz. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Positive buzz on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-positive-buzz` (part named by Positive buzz)
- `metric.whole-named-by-positive-buzz` (whole named by Positive buzz)

Placements:

- organizational / functional / Management / Public Relations (sK1398, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Media mentions

- id: `kpi.management.media-mentions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Media mentions measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Media mentions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Media mentions on the desired side of its target for this period?

Inputs:

- `metric.media-mentions` (Media mentions)

Placements:

- organizational / functional / Management / Public Relations (sK1399, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visibility

- id: `kpi.management.visibility`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visibility measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Visibility. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visibility on the desired side of its target for this period?

Inputs:

- `metric.visibility` (Visibility)

Placements:

- organizational / functional / Management / Public Relations (sK1400, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Advertising values equivalents (AVEs)

- id: `kpi.management.advertising-values-equivalents-aves`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Advertising values equivalents (AVEs) measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Advertising values equivalents (AVEs). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Advertising values equivalents (AVEs) on the desired side of its target for this period?

Inputs:

- `metric.advertising-values-equivalents-aves` (Advertising values equivalents (AVEs))

Placements:

- organizational / functional / Management / Public Relations (sK1401, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recall events

- id: `kpi.management.recall-events`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Recall events measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Recall events, B is whole named by Recall events. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recall events on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-recall-events` (part named by Recall events)
- `metric.whole-named-by-recall-events` (whole named by Recall events)

Placements:

- organizational / functional / Management / Public Relations (sK1402, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Awareness of messages via PR

- id: `kpi.management.awareness-of-messages-via-pr`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Awareness of messages via PR measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is Awareness, B is messages via PR. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Awareness of messages via PR on the desired side of its target for this period?

Inputs:

- `metric.awareness` (Awareness)
- `metric.messages-via-pr` (messages via PR)

Placements:

- organizational / functional / Management / Public Relations (sK1403, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inquiries generated

- id: `kpi.management.inquiries-generated`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Inquiries generated measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Inquiries generated. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inquiries generated on the desired side of its target for this period?

Inputs:

- `metric.inquiries-generated` (Inquiries generated)

Placements:

- organizational / functional / Management / Public Relations (sK1404, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Copayments charged

- id: `kpi.management.copayments-charged`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Copayments charged measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Copayments charged, B is whole named by Copayments charged. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Copayments charged on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-copayments-charged` (part named by Copayments charged)
- `metric.whole-named-by-copayments-charged` (whole named by Copayments charged)

Placements:

- organizational / functional / Management / Public Relations (sK1405, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Target audience that receives messages

- id: `kpi.management.target-audience-that-receives-messages`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Target audience that receives messages measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Target audience that receives messages, B is whole named by Target audience that receives messages. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Target audience that receives messages on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-target-audience-that-receives-messages` (part named by Target audience that receives messages)
- `metric.whole-named-by-target-audience-that-receives-messages` (whole named by Target audience that receives messages)

Placements:

- organizational / functional / Management / Public Relations (sK1406, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Press releases picked up by media outlets

- id: `kpi.management.press-releases-picked-up-by-media-outlets`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Press releases picked up by media outlets measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Press releases picked up by media outlets, B is whole named by Press releases picked up by media outlets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Press releases picked up by media outlets on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-press-releases-picked-up-by-media-outlets` (part named by Press releases picked up by media outlets)
- `metric.whole-named-by-press-releases-picked-up-by-media-outlets` (whole named by Press releases picked up by media outlets)

Placements:

- organizational / functional / Management / Public Relations (sK1407, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Press releases picked up by media

- id: `kpi.management.press-releases-picked-up-by-media`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Press releases picked up by media measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Press releases picked up by media. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Press releases picked up by media on the desired side of its target for this period?

Inputs:

- `metric.press-releases-picked-up-by-media` (Press releases picked up by media)

Placements:

- organizational / functional / Management / Public Relations (sK1408, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Negative media stories

- id: `kpi.management.negative-media-stories`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Negative media stories measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Negative media stories. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Negative media stories on the desired side of its target for this period?

Inputs:

- `metric.negative-media-stories` (Negative media stories)

Placements:

- organizational / functional / Management / Public Relations (sK1409, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Positive to negative editorial feedback comments

- id: `kpi.management.positive-to-negative-editorial-feedback-comments`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Positive to negative editorial feedback comments measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Positive to negative editorial feedback comments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Positive to negative editorial feedback comments on the desired side of its target for this period?

Inputs:

- `metric.positive-to-negative-editorial-feedback-comments` (Positive to negative editorial feedback comments)

Placements:

- organizational / functional / Management / Public Relations (sK1411, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Aggregated rating in review sites

- id: `kpi.management.aggregated-rating-in-review-sites`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Aggregated rating in review sites measures that result inside Management, subcategory Public Relations. The unit is percent. The formula is (A / B) * 100, where A is part named by Aggregated rating in review sites, B is whole named by Aggregated rating in review sites. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Aggregated rating in review sites on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-aggregated-rating-in-review-sites` (part named by Aggregated rating in review sites)
- `metric.whole-named-by-aggregated-rating-in-review-sites` (whole named by Aggregated rating in review sites)

Placements:

- organizational / functional / Management / Public Relations (sK9008, page_0041)
- organizational / industries / Healthcare / Organizational = Industries (60908, page_0130)
- organizational / industries / Healthcare / Organizational » Industries (K6908, page_0132)
- organizational / industries / Healthcare / Tour Operator (kX6908, page_0133)
- organizational / industries / Healthcare / Tour Operator (kK6908, page_0133)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Exit rates to awards

- id: `kpi.management.exit-rates-to-awards`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Exit rates to awards measures that result inside Management, subcategory Public Relations. The unit is count. The formula is A, where A is Exit rates to awards. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Exit rates to awards on the desired side of its target for this period?

Inputs:

- `metric.exit-rates-to-awards` (Exit rates to awards)

Placements:

- organizational / functional / Management / Public Relations (sK14129, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per information product

- id: `kpi.management.cost-per-information-product`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.public-relations`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per information product measures that result inside Management, subcategory Public Relations. The unit is currency. The formula is A / B, where A is Cost, B is information product. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per information product on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.information-product` (information product)

Placements:

- organizational / functional / Management / Public Relations (sK20660, page_0041)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

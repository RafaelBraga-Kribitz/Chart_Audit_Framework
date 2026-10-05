# Publishing / Web Analytics

Context: organizational. Group: functional. KPIs: 60.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### New visitors

- id: `kpi.publishing.new-visitors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New visitors measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by New visitors, B is whole named by New visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New visitors on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-new-visitors` (part named by New visitors)
- `metric.whole-named-by-new-visitors` (whole named by New visitors)

Placements:

- organizational / functional / Publishing / Web Analytics (sK114, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visits per visit

- id: `kpi.publishing.visits-per-visit`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visits per visit measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A / B, where A is Visits, B is visit. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visits per visit on the desired side of its target for this period?

Inputs:

- `metric.visits` (Visits)
- `metric.visit` (visit)

Placements:

- organizational / functional / Publishing / Web Analytics (sK115, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per lead

- id: `kpi.publishing.cost-per-lead`
- kind: kpi
- unit: currency
- direction: down
- timing: leading
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per lead measures that result inside Publishing, subcategory Web Analytics. The unit is currency. The formula is A / B, where A is Cost, B is lead. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per lead on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.lead` (lead)

Placements:

- organizational / functional / Publishing / Web Analytics (sK116, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Web traffic concentration

- id: `kpi.publishing.web-traffic-concentration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Web traffic concentration measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Web traffic concentration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Web traffic concentration on the desired side of its target for this period?

Inputs:

- `metric.web-traffic-concentration` (Web traffic concentration)

Placements:

- organizational / functional / Publishing / Web Analytics (sK203, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique authenticated visitors

- id: `kpi.publishing.unique-authenticated-visitors`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unique authenticated visitors measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Unique authenticated visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique authenticated visitors on the desired side of its target for this period?

Inputs:

- `metric.unique-authenticated-visitors` (Unique authenticated visitors)

Placements:

- organizational / functional / Publishing / Web Analytics (sK205, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visits under one minute

- id: `kpi.publishing.visits-under-one-minute`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visits under one minute measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Visits under one minute, B is whole named by Visits under one minute. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visits under one minute on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-visits-under-one-minute` (part named by Visits under one minute)
- `metric.whole-named-by-visits-under-one-minute` (whole named by Visits under one minute)

Placements:

- organizational / functional / Publishing / Web Analytics (sK206, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bounce rate

- id: `kpi.publishing.bounce-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bounce rate measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is numerator of Bounce rate, B is base of Bounce rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bounce rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-bounce-rate` (numerator of Bounce rate)
- `metric.base-of-bounce-rate` (base of Bounce rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK308, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time on site

- id: `kpi.publishing.time-on-site`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time on site measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Time on site. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time on site on the desired side of its target for this period?

Inputs:

- `metric.time-on-site` (Time on site)

Placements:

- organizational / functional / Publishing / Web Analytics (sK449, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time on page

- id: `kpi.publishing.time-on-page`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time on page measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Time on page. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time on page on the desired side of its target for this period?

Inputs:

- `metric.time-on-page` (Time on page)

Placements:

- organizational / functional / Publishing / Web Analytics (sK450, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page views per session

- id: `kpi.publishing.page-views-per-session`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page views per session measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A / B, where A is Page views, B is session. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page views per session on the desired side of its target for this period?

Inputs:

- `metric.page-views` (Page views)
- `metric.session` (session)

Placements:

- organizational / functional / Publishing / Web Analytics (sK451, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page exit rate

- id: `kpi.publishing.page-exit-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page exit rate measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is numerator of Page exit rate, B is base of Page exit rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page exit rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-page-exit-rate` (numerator of Page exit rate)
- `metric.base-of-page-exit-rate` (base of Page exit rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK452, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visitor recency

- id: `kpi.publishing.visitor-recency`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visitor recency measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Visitor recency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visitor recency on the desired side of its target for this period?

Inputs:

- `metric.visitor-recency` (Visitor recency)

Placements:

- organizational / functional / Publishing / Web Analytics (sK453, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Website access rate

- id: `kpi.publishing.website-access-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Website access rate measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Website access rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Website access rate on the desired side of its target for this period?

Inputs:

- `metric.website-access-rate` (Website access rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK454, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page redirect latency

- id: `kpi.publishing.page-redirect-latency`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page redirect latency measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Page redirect latency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page redirect latency on the desired side of its target for this period?

Inputs:

- `metric.page-redirect-latency` (Page redirect latency)

Placements:

- organizational / functional / Publishing / Web Analytics (sK798, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page idle time

- id: `kpi.publishing.page-idle-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page idle time measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Page idle time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page idle time on the desired side of its target for this period?

Inputs:

- `metric.page-idle-time` (Page idle time)

Placements:

- organizational / functional / Publishing / Web Analytics (sK799, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Session blink time

- id: `kpi.publishing.session-blink-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Session blink time measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Session blink time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Session blink time on the desired side of its target for this period?

Inputs:

- `metric.session-blink-time` (Session blink time)

Placements:

- organizational / functional / Publishing / Web Analytics (sK800, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page views

- id: `kpi.publishing.page-views`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page views measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Page views. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page views on the desired side of its target for this period?

Inputs:

- `metric.page-views` (Page views)

Placements:

- organizational / functional / Publishing / Web Analytics (sK147, page_0044)
- organizational / industries / Media / Organizational Industries ($K18140, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Conversion of RSS subscribers to blog readers

- id: `kpi.publishing.conversion-of-rss-subscribers-to-blog-readers`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Conversion of RSS subscribers to blog readers measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is Conversion, B is RSS subscribers to blog readers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Conversion of RSS subscribers to blog readers on the desired side of its target for this period?

Inputs:

- `metric.conversion` (Conversion)
- `metric.rss-subscribers-to-blog-readers` (RSS subscribers to blog readers)

Placements:

- organizational / functional / Publishing / Web Analytics (sK249, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Maintenance cost of the website

- id: `kpi.publishing.maintenance-cost-of-the-website`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Maintenance cost of the website measures that result inside Publishing, subcategory Web Analytics. The unit is currency. The formula is A, where A is Maintenance cost of the website. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Maintenance cost of the website on the desired side of its target for this period?

Inputs:

- `metric.maintenance-cost-of-the-website` (Maintenance cost of the website)

Placements:

- organizational / functional / Publishing / Web Analytics (sK250, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Error pages served

- id: `kpi.publishing.error-pages-served`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Error pages served measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Error pages served, B is whole named by Error pages served. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Error pages served on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-error-pages-served` (part named by Error pages served)
- `metric.whole-named-by-error-pages-served` (whole named by Error pages served)

Placements:

- organizational / functional / Publishing / Web Analytics (sK252, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page exits due to inactivity

- id: `kpi.publishing.page-exits-due-to-inactivity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page exits due to inactivity measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Page exits due to inactivity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page exits due to inactivity on the desired side of its target for this period?

Inputs:

- `metric.page-exits-due-to-inactivity` (Page exits due to inactivity)

Placements:

- organizational / functional / Publishing / Web Analytics (sK257, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Incoming backlinks

- id: `kpi.publishing.incoming-backlinks`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Incoming backlinks measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Incoming backlinks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Incoming backlinks on the desired side of its target for this period?

Inputs:

- `metric.incoming-backlinks` (Incoming backlinks)

Placements:

- organizational / functional / Publishing / Web Analytics (sK253, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Search depth

- id: `kpi.publishing.search-depth`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Search depth measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Search depth. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Search depth on the desired side of its target for this period?

Inputs:

- `metric.search-depth` (Search depth)

Placements:

- organizational / functional / Publishing / Web Analytics (sK256, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Search exits

- id: `kpi.publishing.search-exits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Search exits measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Search exits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Search exits on the desired side of its target for this period?

Inputs:

- `metric.search-exits` (Search exits)

Placements:

- organizational / functional / Publishing / Web Analytics (sK261, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique searches

- id: `kpi.publishing.unique-searches`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unique searches measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Unique searches. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique searches on the desired side of its target for this period?

Inputs:

- `metric.unique-searches` (Unique searches)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2562, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Website downtime

- id: `kpi.publishing.website-downtime`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Website downtime measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Website downtime, B is whole named by Website downtime. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Website downtime on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-website-downtime` (part named by Website downtime)
- `metric.whole-named-by-website-downtime` (whole named by Website downtime)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2563, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Search refinements

- id: `kpi.publishing.search-refinements`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Search refinements measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Search refinements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Search refinements on the desired side of its target for this period?

Inputs:

- `metric.search-refinements` (Search refinements)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2565, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Task completion rate

- id: `kpi.publishing.task-completion-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Task completion rate measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is numerator of Task completion rate, B is base of Task completion rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Task completion rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-task-completion-rate` (numerator of Task completion rate)
- `metric.base-of-task-completion-rate` (base of Task completion rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2566, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stickiness

- id: `kpi.publishing.stickiness`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Stickiness measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Stickiness. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stickiness on the desired side of its target for this period?

Inputs:

- `metric.stickiness` (Stickiness)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2567, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Subscription rate

- id: `kpi.publishing.subscription-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Subscription rate measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is numerator of Subscription rate, B is base of Subscription rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Subscription rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-subscription-rate` (numerator of Subscription rate)
- `metric.base-of-subscription-rate` (base of Subscription rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2568, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Depth of visits

- id: `kpi.publishing.depth-of-visits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Depth of visits measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Depth of visits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Depth of visits on the desired side of its target for this period?

Inputs:

- `metric.depth-of-visits` (Depth of visits)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2570, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Referral traffic

- id: `kpi.publishing.referral-traffic`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Referral traffic measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Referral traffic, B is whole named by Referral traffic. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Referral traffic on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-referral-traffic` (part named by Referral traffic)
- `metric.whole-named-by-referral-traffic` (whole named by Referral traffic)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2574, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On site searches

- id: `kpi.publishing.on-site-searches`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

On site searches measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by On site searches, B is whole named by On site searches. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On site searches on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-on-site-searches` (part named by On site searches)
- `metric.whole-named-by-on-site-searches` (whole named by On site searches)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2581, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Searches leading to website (by keyword)

- id: `kpi.publishing.searches-leading-to-website-by-keyword`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Searches leading to website (by keyword) measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Searches leading to website (by keyword). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Searches leading to website (by keyword) on the desired side of its target for this period?

Inputs:

- `metric.searches-leading-to-website-by-keyword` (Searches leading to website (by keyword))

Placements:

- organizational / functional / Publishing / Web Analytics (sK2583, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page requests growth rate

- id: `kpi.publishing.page-requests-growth-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page requests growth rate measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is numerator of Page requests growth rate, B is base of Page requests growth rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page requests growth rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-page-requests-growth-rate` (numerator of Page requests growth rate)
- `metric.base-of-page-requests-growth-rate` (base of Page requests growth rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2586, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily page requests

- id: `kpi.publishing.daily-page-requests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily page requests measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Daily page requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily page requests on the desired side of its target for this period?

Inputs:

- `metric.daily-page-requests` (Daily page requests)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2587, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page views per visitor

- id: `kpi.publishing.page-views-per-visitor`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page views per visitor measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A / B, where A is Page views, B is visitor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page views per visitor on the desired side of its target for this period?

Inputs:

- `metric.page-views` (Page views)
- `metric.visitor` (visitor)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2588, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time on site search (TOSAS)

- id: `kpi.publishing.time-on-site-search-tosas`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time on site search (TOSAS) measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Time on site search (TOSAS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time on site search (TOSAS) on the desired side of its target for this period?

Inputs:

- `metric.time-on-site-search-tosas` (Time on site search (TOSAS))

Placements:

- organizational / functional / Publishing / Web Analytics (sK2590, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Session times

- id: `kpi.publishing.session-times`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Session times measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Session times. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Session times on the desired side of its target for this period?

Inputs:

- `metric.session-times` (Session times)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2592, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Heavy user share

- id: `kpi.publishing.heavy-user-share`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Heavy user share measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is numerator of Heavy user share, B is base of Heavy user share. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Heavy user share on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-heavy-user-share` (numerator of Heavy user share)
- `metric.base-of-heavy-user-share` (base of Heavy user share)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2596, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Committed visitors

- id: `kpi.publishing.committed-visitors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Committed visitors measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Committed visitors, B is whole named by Committed visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Committed visitors on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-committed-visitors` (part named by Committed visitors)
- `metric.whole-named-by-committed-visitors` (whole named by Committed visitors)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2597, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Inline browsers

- id: `kpi.publishing.inline-browsers`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Inline browsers measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Inline browsers, B is whole named by Inline browsers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Inline browsers on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-inline-browsers` (part named by Inline browsers)
- `metric.whole-named-by-inline-browsers` (whole named by Inline browsers)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2598, page_0044)
- organizational / functional / Publishing / Web Analytics (sK2600, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Site reach

- id: `kpi.publishing.site-reach`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Site reach measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Site reach, B is whole named by Site reach. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Site reach on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-site-reach` (part named by Site reach)
- `metric.whole-named-by-site-reach` (whole named by Site reach)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2602, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visitor loyalty and recency

- id: `kpi.publishing.visitor-loyalty-and-recency`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visitor loyalty and recency measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Visitor loyalty and recency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visitor loyalty and recency on the desired side of its target for this period?

Inputs:

- `metric.visitor-loyalty-and-recency` (Visitor loyalty and recency)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2603, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Page depth

- id: `kpi.publishing.page-depth`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Page depth measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Page depth. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Page depth on the desired side of its target for this period?

Inputs:

- `metric.page-depth` (Page depth)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2604, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Returning visitors

- id: `kpi.publishing.returning-visitors`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Returning visitors measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Returning visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Returning visitors on the desired side of its target for this period?

Inputs:

- `metric.returning-visitors` (Returning visitors)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2605, page_0044)
- organizational / functional / Publishing / Web Analytics (sK2606, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Visitors per conversion

- id: `kpi.publishing.visitors-per-conversion`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Visitors per conversion measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A / B, where A is Visitors, B is conversion. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Visitors per conversion on the desired side of its target for this period?

Inputs:

- `metric.visitors` (Visitors)
- `metric.conversion` (conversion)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2607, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Website visits per day

- id: `kpi.publishing.website-visits-per-day`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Website visits per day measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A / B, where A is Website visits, B is day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Website visits per day on the desired side of its target for this period?

Inputs:

- `metric.website-visits` (Website visits)
- `metric.day` (day)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2612, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### One page visits

- id: `kpi.publishing.one-page-visits`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

One page visits measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by One page visits, B is whole named by One page visits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is One page visits on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-one-page-visits` (part named by One page visits)
- `metric.whole-named-by-one-page-visits` (whole named by One page visits)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2613, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique visits

- id: `kpi.publishing.unique-visits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unique visits measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Unique visits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique visits on the desired side of its target for this period?

Inputs:

- `metric.unique-visits` (Unique visits)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2614, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### In-stream advertisements

- id: `kpi.publishing.in-stream-advertisements`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

In-stream advertisements measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is In-stream advertisements. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is In-stream advertisements on the desired side of its target for this period?

Inputs:

- `metric.in-stream-advertisements` (In-stream advertisements)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2328, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Recommendations on site on social networks

- id: `kpi.publishing.recommendations-on-site-on-social-networks`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Recommendations on site on social networks measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Recommendations on site on social networks, B is whole named by Recommendations on site on social networks. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Recommendations on site on social networks on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-recommendations-on-site-on-social-networks` (part named by Recommendations on site on social networks)
- `metric.whole-named-by-recommendations-on-site-on-social-networks` (whole named by Recommendations on site on social networks)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2348, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pase-along rate

- id: `kpi.publishing.pase-along-rate`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pase-along rate measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Pase-along rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pase-along rate on the desired side of its target for this period?

Inputs:

- `metric.pase-along-rate` (Pase-along rate)

Placements:

- organizational / functional / Publishing / Web Analytics (sK2346, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Scanning visitors

- id: `kpi.publishing.scanning-visitors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Scanning visitors measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Scanning visitors, B is whole named by Scanning visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Scanning visitors on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-scanning-visitors` (part named by Scanning visitors)
- `metric.whole-named-by-scanning-visitors` (whole named by Scanning visitors)

Placements:

- organizational / functional / Publishing / Web Analytics (sK3267, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New versus returning visitors

- id: `kpi.publishing.new-versus-returning-visitors`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `scatter-plot` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New versus returning visitors measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is New, B is returning visitors. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New versus returning visitors on the desired side of its target for this period?

Inputs:

- `metric.new` (New)
- `metric.returning-visitors` (returning visitors)

Placements:

- organizational / functional / Publishing / Web Analytics (sK3938, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Followers on social media platforms

- id: `kpi.publishing.followers-on-social-media-platforms`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Followers on social media platforms measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Followers on social media platforms. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Followers on social media platforms on the desired side of its target for this period?

Inputs:

- `metric.followers-on-social-media-platforms` (Followers on social media platforms)

Placements:

- organizational / functional / Publishing / Web Analytics (sK6851, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Online pushout comments

- id: `kpi.publishing.online-pushout-comments`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Online pushout comments measures that result inside Publishing, subcategory Web Analytics. The unit is percent. The formula is (A / B) * 100, where A is part named by Online pushout comments, B is whole named by Online pushout comments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Online pushout comments on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-online-pushout-comments` (part named by Online pushout comments)
- `metric.whole-named-by-online-pushout-comments` (whole named by Online pushout comments)

Placements:

- organizational / functional / Publishing / Web Analytics (sK6852, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Website visits

- id: `kpi.publishing.website-visits`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Website visits measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Website visits. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Website visits on the desired side of its target for this period?

Inputs:

- `metric.website-visits` (Website visits)

Placements:

- organizational / functional / Publishing / Web Analytics (sK6904, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Daily active users (DAU)

- id: `kpi.publishing.daily-active-users-dau`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Daily active users (DAU) measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Daily active users (DAU). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Daily active users (DAU) on the desired side of its target for this period?

Inputs:

- `metric.daily-active-users-dau` (Daily active users (DAU))

Placements:

- organizational / functional / Publishing / Web Analytics (sK7063, page_0044)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Trial accounts

- id: `kpi.publishing.trial-accounts`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.publishing.web-analytics`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Trial accounts measures that result inside Publishing, subcategory Web Analytics. The unit is count. The formula is A, where A is Trial accounts. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Trial accounts on the desired side of its target for this period?

Inputs:

- `metric.trial-accounts` (Trial accounts)

Placements:

- organizational / functional / Publishing / Web Analytics (sK7065, page_0044)
- organizational / functional / Sales and Customer Service / Organizational > Functional Areas (sK7065, page_0052)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

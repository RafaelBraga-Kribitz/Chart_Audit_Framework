# Management / Forecasts & Valuation

Context: organizational. Group: functional. KPIs: 3.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### § Earnings per share (EPS)

- id: `kpi.planning.earnings-per-share-eps`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Earnings per share (EPS) measures that result inside Planning, subcategory General. The unit is number. The formula is A / B, where A is § Earnings, B is share (EPS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Earnings per share (EPS) on the desired side of its target for this period?

Inputs:

- `metric.earnings` (§ Earnings)
- `metric.share-eps` (share (EPS))

Placements:

- personal / productivity / Planning / General (xK468, page_0009)
- organizational / functional / Management / Forecasts & Valuation (x466, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Price-to-earnings ratio

- id: `kpi.management.price-to-earnings-ratio`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.forecasts-and-valuation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Price-to-earnings ratio measures that result inside Management, subcategory Forecasts & Valuation. The unit is currency. The formula is A, where A is Price-to-earnings ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Price-to-earnings ratio on the desired side of its target for this period?

Inputs:

- `metric.price-to-earnings-ratio` (Price-to-earnings ratio)

Placements:

- organizational / functional / Management / Forecasts & Valuation (x469, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Economic value added (EVA)

- id: `kpi.management.economic-value-added-eva`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.forecasts-and-valuation`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Economic value added (EVA) measures that result inside Management, subcategory Forecasts & Valuation. The unit is currency. The formula is A, where A is Economic value added (EVA). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Economic value added (EVA) on the desired side of its target for this period?

Inputs:

- `metric.economic-value-added-eva` (Economic value added (EVA))

Placements:

- organizational / functional / Management / Forecasts & Valuation (x475, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

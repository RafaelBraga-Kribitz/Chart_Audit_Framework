# Planning / General

Context: personal. Group: productivity. KPIs: 18.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### § EBIT (Earnings Before Interest and Taxes)

- id: `kpi.planning.ebit-earnings-before-interest-and-taxes`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ EBIT (Earnings Before Interest and Taxes) measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § EBIT (Earnings Before Interest and Taxes). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § EBIT (Earnings Before Interest and Taxes) on the desired side of its target for this period?

Inputs:

- `metric.ebit-earnings-before-interest-and-taxes` (§ EBIT (Earnings Before Interest and Taxes))

Placements:

- personal / productivity / Planning / General (xK190, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Operating expenses

- id: `kpi.planning.operating-expenses`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Operating expenses measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Operating expenses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Operating expenses on the desired side of its target for this period?

Inputs:

- `metric.operating-expenses` (§ Operating expenses)

Placements:

- personal / productivity / Planning / General (xKP02, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Cost of goods sold (COGS)

- id: `kpi.planning.cost-of-goods-sold-cogs`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Cost of goods sold (COGS) measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Cost of goods sold (COGS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Cost of goods sold (COGS) on the desired side of its target for this period?

Inputs:

- `metric.cost-of-goods-sold-cogs` (§ Cost of goods sold (COGS))

Placements:

- personal / productivity / Planning / General (xK414, page_0009)
- organizational / industries / Manufacturing / General (▲K14, page_0142)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Asset turnover

- id: `kpi.planning.asset-turnover`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Asset turnover measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Asset turnover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Asset turnover on the desired side of its target for this period?

Inputs:

- `metric.asset-turnover` (§ Asset turnover)

Placements:

- personal / productivity / Planning / General (xK466, page_0009)
- organizational / functional / Management / Profitability (K486, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

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

### § Budget variance

- id: `kpi.planning.budget-variance`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A - B`
- formula type: difference
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `waterfall-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Budget variance measures that result inside Planning, subcategory General. The unit is number. The formula is A - B, where A is actual § Budget variance, B is reference § Budget variance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Budget variance on the desired side of its target for this period?

Inputs:

- `metric.actual-budget-variance` (actual § Budget variance)
- `metric.reference-budget-variance` (reference § Budget variance)

Placements:

- personal / productivity / Planning / General (xK479, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Price to sales ratio

- id: `kpi.planning.price-to-sales-ratio`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Price to sales ratio measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Price to sales ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Price to sales ratio on the desired side of its target for this period?

Inputs:

- `metric.price-to-sales-ratio` (§ Price to sales ratio)

Placements:

- personal / productivity / Planning / General (xK513, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Perry ratio

- id: `kpi.planning.perry-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Perry ratio measures that result inside Planning, subcategory General. The unit is count. The formula is A, where A is Perry ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Perry ratio on the desired side of its target for this period?

Inputs:

- `metric.perry-ratio` (Perry ratio)

Placements:

- personal / productivity / Planning / General (xK517, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Current ratio

- id: `kpi.planning.current-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Current ratio measures that result inside Planning, subcategory General. The unit is count. The formula is A, where A is Current ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Current ratio on the desired side of its target for this period?

Inputs:

- `metric.current-ratio` (Current ratio)

Placements:

- personal / productivity / Planning / General (xK520, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Working capital turnover

- id: `kpi.planning.working-capital-turnover`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Working capital turnover measures that result inside Planning, subcategory General. The unit is count. The formula is A, where A is Working capital turnover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Working capital turnover on the desired side of its target for this period?

Inputs:

- `metric.working-capital-turnover` (Working capital turnover)

Placements:

- personal / productivity / Planning / General (xK525, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Earnings before interest, taxes, depreciation, amortization, and restructuring or net costs (EBITDAR)

- id: `kpi.planning.earnings-before-interest-taxes-depreciation-amortization-and-restructuri`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Earnings before interest, taxes, depreciation, amortization, and restructuring or net costs (EBITDAR) measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Earnings before interest, taxes, depreciation, amortization, and restructuring or net costs (EBITDAR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Earnings before interest, taxes, depreciation, amortization, and restructuring or net costs (EBITDAR) on the desired side of its target for this period?

Inputs:

- `metric.earnings-before-interest-taxes-depreciation-amortization-and-restructuri` (§ Earnings before interest, taxes, depreciation, amortization, and restructuring or net costs (EBITDAR))

Placements:

- personal / productivity / Planning / General (xK535, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Net debt

- id: `kpi.planning.net-debt`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Net debt measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Net debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Net debt on the desired side of its target for this period?

Inputs:

- `metric.net-debt` (§ Net debt)

Placements:

- personal / productivity / Planning / General (xK538, page_0009)
- organizational / functional / Management / Financial stability (x3005, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Net income after taxes (NIAT)

- id: `kpi.planning.net-income-after-taxes-niat`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Net income after taxes (NIAT) measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Net income after taxes (NIAT). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Net income after taxes (NIAT) on the desired side of its target for this period?

Inputs:

- `metric.net-income-after-taxes-niat` (§ Net income after taxes (NIAT))

Placements:

- personal / productivity / Planning / General (xK539, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Shareholders' equity

- id: `kpi.planning.shareholders-equity`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Shareholders' equity measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Shareholders' equity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Shareholders' equity on the desired side of its target for this period?

Inputs:

- `metric.shareholders-equity` (§ Shareholders' equity)

Placements:

- personal / productivity / Planning / General (xK549, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Tangible book value per share (TBVP5)

- id: `kpi.planning.tangible-book-value-per-share-tbvp5`
- kind: kpi
- unit: count
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

Tangible book value per share (TBVP5) measures that result inside Planning, subcategory General. The unit is count. The formula is A / B, where A is Tangible book value, B is share (TBVP5). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Tangible book value per share (TBVP5) on the desired side of its target for this period?

Inputs:

- `metric.tangible-book-value` (Tangible book value)
- `metric.share-tbvp5` (share (TBVP5))

Placements:

- personal / productivity / Planning / General (xK550, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Earnings before interest, taxes, depreciation and amortization (EBITIA)

- id: `kpi.planning.earnings-before-interest-taxes-depreciation-and-amortization-ebitia`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Earnings before interest, taxes, depreciation and amortization (EBITIA) measures that result inside Planning, subcategory General. The unit is number. The formula is A, where A is § Earnings before interest, taxes, depreciation and amortization (EBITIA). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Earnings before interest, taxes, depreciation and amortization (EBITIA) on the desired side of its target for this period?

Inputs:

- `metric.earnings-before-interest-taxes-depreciation-and-amortization-ebitia` (§ Earnings before interest, taxes, depreciation and amortization (EBITIA))

Placements:

- personal / productivity / Planning / General (xK551, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Breakdown point (BEP)

- id: `kpi.planning.breakdown-point-bep`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Breakdown point (BEP) measures that result inside Planning, subcategory General. The unit is count. The formula is A, where A is Breakdown point (BEP). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Breakdown point (BEP) on the desired side of its target for this period?

Inputs:

- `metric.breakdown-point-bep` (Breakdown point (BEP))

Placements:

- personal / productivity / Planning / General (xK552, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### § Fixed assets per PTE (full Time Equivalent)

- id: `kpi.planning.fixed-assets-per-pte-full-time-equivalent`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.planning.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

§ Fixed assets per PTE (full Time Equivalent) measures that result inside Planning, subcategory General. The unit is number. The formula is A / B, where A is § Fixed assets, B is PTE (full Time Equivalent). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is § Fixed assets per PTE (full Time Equivalent) on the desired side of its target for this period?

Inputs:

- `metric.fixed-assets` (§ Fixed assets)
- `metric.pte-full-time-equivalent` (PTE (full Time Equivalent))

Placements:

- personal / productivity / Planning / General (xK570, page_0009)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

# Management / Financial stability

Context: organizational. Group: functional. KPIs: 42.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Interest cover

- id: `kpi.accounting.interest-cover`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Interest cover measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Interest cover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interest cover on the desired side of its target for this period?

Inputs:

- `metric.interest-cover` (Interest cover)

Placements:

- organizational / functional / Accounting / General (0605, page_0008)
- organizational / functional / Management / Financial stability (x865, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Times interest earned

- id: `kpi.accounting.times-interest-earned`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Times interest earned measures that result inside Accounting, subcategory General. The unit is count. The formula is A, where A is Times interest earned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Times interest earned on the desired side of its target for this period?

Inputs:

- `metric.times-interest-earned` (Times interest earned)

Placements:

- organizational / functional / Accounting / General (83025, page_0008)
- organizational / functional / Management / Financial stability (x3025, page_0017)

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

### Weighted average cost of capital (WACC)

- id: `kpi.management.weighted-average-cost-of-capital-wacc`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Weighted average cost of capital (WACC) measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is Weighted average cost, B is capital (WACC). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Weighted average cost of capital (WACC) on the desired side of its target for this period?

Inputs:

- `metric.weighted-average-cost` (Weighted average cost)
- `metric.capital-wacc` (capital (WACC))

Placements:

- organizational / functional / Management / Financial stability (x470, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Altman Z-Score (for public manufacturing companies)

- id: `kpi.management.altman-z-score-for-public-manufacturing-companies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: survey
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Altman Z-Score (for public manufacturing companies) measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Altman Z-Score (for public manufacturing companies). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Altman Z-Score (for public manufacturing companies) on the desired side of its target for this period?

Inputs:

- `metric.altman-z-score-for-public-manufacturing-companies` (Altman Z-Score (for public manufacturing companies))

Placements:

- organizational / functional / Management / Financial stability (x491, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Altman Z-Score (for privately held manufacturing companies)

- id: `kpi.management.altman-z-score-for-privately-held-manufacturing-companies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: survey
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Altman Z-Score (for privately held manufacturing companies) measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Altman Z-Score (for privately held manufacturing companies). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Altman Z-Score (for privately held manufacturing companies) on the desired side of its target for this period?

Inputs:

- `metric.altman-z-score-for-privately-held-manufacturing-companies` (Altman Z-Score (for privately held manufacturing companies))

Placements:

- organizational / functional / Management / Financial stability (x494, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Altman Z-Score (for privately held non-manufacturing companies)

- id: `kpi.management.altman-z-score-for-privately-held-non-manufacturing-companies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: survey
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Altman Z-Score (for privately held non-manufacturing companies) measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Altman Z-Score (for privately held non-manufacturing companies). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Altman Z-Score (for privately held non-manufacturing companies) on the desired side of its target for this period?

Inputs:

- `metric.altman-z-score-for-privately-held-non-manufacturing-companies` (Altman Z-Score (for privately held non-manufacturing companies))

Placements:

- organizational / functional / Management / Financial stability (x595, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt ratio

- id: `kpi.management.debt-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Debt ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt ratio on the desired side of its target for this period?

Inputs:

- `metric.debt-ratio` (Debt ratio)

Placements:

- organizational / functional / Management / Financial stability (x5110, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt-to-equity ratio

- id: `kpi.management.debt-to-equity-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt-to-equity ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Debt-to-equity ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt-to-equity ratio on the desired side of its target for this period?

Inputs:

- `metric.debt-to-equity-ratio` (Debt-to-equity ratio)

Placements:

- organizational / functional / Management / Financial stability (x5111, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash flow per share

- id: `kpi.management.cash-flow-per-share`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash flow per share measures that result inside Management, subcategory Financial stability. The unit is currency. The formula is A / B, where A is Cash flow, B is share. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash flow per share on the desired side of its target for this period?

Inputs:

- `metric.cash-flow` (Cash flow)
- `metric.share` (share)

Placements:

- organizational / functional / Management / Financial stability (x5230, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt-to-capital ratio

- id: `kpi.management.debt-to-capital-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt-to-capital ratio measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is numerator of Debt-to-capital ratio, B is base of Debt-to-capital ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt-to-capital ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-debt-to-capital-ratio` (numerator of Debt-to-capital ratio)
- `metric.base-of-debt-to-capital-ratio` (base of Debt-to-capital ratio)

Placements:

- organizational / functional / Management / Financial stability (x5334, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expense coverage days

- id: `kpi.management.expense-coverage-days`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Expense coverage days measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Expense coverage days. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expense coverage days on the desired side of its target for this period?

Inputs:

- `metric.expense-coverage-days` (Expense coverage days)

Placements:

- organizational / functional / Management / Financial stability (x5132, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Current liabilities to sales

- id: `kpi.management.current-liabilities-to-sales`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Current liabilities to sales measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Current liabilities to sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Current liabilities to sales on the desired side of its target for this period?

Inputs:

- `metric.current-liabilities-to-sales` (Current liabilities to sales)

Placements:

- organizational / functional / Management / Financial stability (x2980, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### EBITDA coverage

- id: `kpi.management.ebitda-coverage`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

EBITDA coverage measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is EBITDA coverage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is EBITDA coverage on the desired side of its target for this period?

Inputs:

- `metric.ebitda-coverage` (EBITDA coverage)

Placements:

- organizational / functional / Management / Financial stability (x2987, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Fixed assets to short term debt

- id: `kpi.management.fixed-assets-to-short-term-debt`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Fixed assets to short term debt measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Fixed assets to short term debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Fixed assets to short term debt on the desired side of its target for this period?

Inputs:

- `metric.fixed-assets-to-short-term-debt` (Fixed assets to short term debt)

Placements:

- organizational / functional / Management / Financial stability (x2992, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gearing ratio

- id: `kpi.management.gearing-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Gearing ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Gearing ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gearing ratio on the desired side of its target for this period?

Inputs:

- `metric.gearing-ratio` (Gearing ratio)

Placements:

- organizational / functional / Management / Financial stability (x2995, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Loan bills to coverage ratio

- id: `kpi.management.loan-bills-to-coverage-ratio`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Loan bills to coverage ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Loan bills to coverage ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Loan bills to coverage ratio on the desired side of its target for this period?

Inputs:

- `metric.loan-bills-to-coverage-ratio` (Loan bills to coverage ratio)

Placements:

- organizational / functional / Management / Financial stability (x2999, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Long-term debt to capitalization ratio

- id: `kpi.management.long-term-debt-to-capitalization-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Long-term debt to capitalization ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Long-term debt to capitalization ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Long-term debt to capitalization ratio on the desired side of its target for this period?

Inputs:

- `metric.long-term-debt-to-capitalization-ratio` (Long-term debt to capitalization ratio)

Placements:

- organizational / functional / Management / Financial stability (x3000, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Short to long term debt

- id: `kpi.management.short-to-long-term-debt`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Short to long term debt measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Short to long term debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Short to long term debt on the desired side of its target for this period?

Inputs:

- `metric.short-to-long-term-debt` (Short to long term debt)

Placements:

- organizational / functional / Management / Financial stability (x3020, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Capital employed

- id: `kpi.management.capital-employed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Capital employed measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Capital employed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Capital employed on the desired side of its target for this period?

Inputs:

- `metric.capital-employed` (Capital employed)

Placements:

- organizational / functional / Management / Financial stability (x3024, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash flow to long term debt

- id: `kpi.management.cash-flow-to-long-term-debt`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash flow to long term debt measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Cash flow to long term debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash flow to long term debt on the desired side of its target for this period?

Inputs:

- `metric.cash-flow-to-long-term-debt` (Cash flow to long term debt)

Placements:

- organizational / functional / Management / Financial stability (x3038, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sub-divided cash flow (MCCF)

- id: `kpi.management.sub-divided-cash-flow-mccf`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sub-divided cash flow (MCCF) measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Sub-divided cash flow (MCCF). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sub-divided cash flow (MCCF) on the desired side of its target for this period?

Inputs:

- `metric.sub-divided-cash-flow-mccf` (Sub-divided cash flow (MCCF))

Placements:

- organizational / functional / Management / Financial stability (x3041, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Capital acquisition ratio

- id: `kpi.management.capital-acquisition-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Capital acquisition ratio measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is numerator of Capital acquisition ratio, B is base of Capital acquisition ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Capital acquisition ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-capital-acquisition-ratio` (numerator of Capital acquisition ratio)
- `metric.base-of-capital-acquisition-ratio` (base of Capital acquisition ratio)

Placements:

- organizational / functional / Management / Financial stability (x3011, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Liabilities to net worth

- id: `kpi.management.liabilities-to-net-worth`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Liabilities to net worth measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Liabilities to net worth. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Liabilities to net worth on the desired side of its target for this period?

Inputs:

- `metric.liabilities-to-net-worth` (Liabilities to net worth)

Placements:

- organizational / functional / Management / Financial stability (x3107, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Current liabilities to net worth

- id: `kpi.management.current-liabilities-to-net-worth`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Current liabilities to net worth measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Current liabilities to net worth. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Current liabilities to net worth on the desired side of its target for this period?

Inputs:

- `metric.current-liabilities-to-net-worth` (Current liabilities to net worth)

Placements:

- organizational / functional / Management / Financial stability (x3109, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operating assets ratio

- id: `kpi.management.operating-assets-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating assets ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Operating assets ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating assets ratio on the desired side of its target for this period?

Inputs:

- `metric.operating-assets-ratio` (Operating assets ratio)

Placements:

- organizational / functional / Management / Financial stability (x3118, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interest expense

- id: `kpi.management.interest-expense`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Interest expense measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Interest expense. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interest expense on the desired side of its target for this period?

Inputs:

- `metric.interest-expense` (Interest expense)

Placements:

- organizational / functional / Management / Financial stability (x3123, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Long-term debt to total debt

- id: `kpi.management.long-term-debt-to-total-debt`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Long-term debt to total debt measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is Long-term debt, B is total debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Long-term debt to total debt on the desired side of its target for this period?

Inputs:

- `metric.long-term-debt` (Long-term debt)
- `metric.total-debt` (total debt)

Placements:

- organizational / functional / Management / Financial stability (x3124, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Short-term to total debt

- id: `kpi.management.short-term-to-total-debt`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Short-term to total debt measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is Short-term, B is total debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Short-term to total debt on the desired side of its target for this period?

Inputs:

- `metric.short-term` (Short-term)
- `metric.total-debt` (total debt)

Placements:

- organizational / functional / Management / Financial stability (x3129, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Solvency ratio

- id: `kpi.management.solvency-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Solvency ratio measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is numerator of Solvency ratio, B is base of Solvency ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Solvency ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-solvency-ratio` (numerator of Solvency ratio)
- `metric.base-of-solvency-ratio` (base of Solvency ratio)

Placements:

- organizational / functional / Management / Financial stability (x3130, page_0017)
- organizational / industries / Financial Institutions / Insurance (sK16822, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash maturity coverage

- id: `kpi.management.cash-maturity-coverage`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash maturity coverage measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Cash maturity coverage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash maturity coverage on the desired side of its target for this period?

Inputs:

- `metric.cash-maturity-coverage` (Cash maturity coverage)

Placements:

- organizational / functional / Management / Financial stability (x3269, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Common shares\( ^{2} \)

- id: `kpi.management.common-shares-2`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Common shares\( ^{2} \) measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Common shares\( ^{2} \). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Common shares\( ^{2} \) on the desired side of its target for this period?

Inputs:

- `metric.common-shares-2` (Common shares\( ^{2} \))

Placements:

- organizational / functional / Management / Financial stability (x3327, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Texas ratio

- id: `kpi.management.texas-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Texas ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Texas ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Texas ratio on the desired side of its target for this period?

Inputs:

- `metric.texas-ratio` (Texas ratio)

Placements:

- organizational / functional / Management / Financial stability (x3426, page_0017)
- organizational / industries / Financial Institutions / xKPI ▼ Key Performance Indicator name (xCI426, page_0082)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Defensive interval ratio (DIR)

- id: `kpi.management.defensive-interval-ratio-dir`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Defensive interval ratio (DIR) measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Defensive interval ratio (DIR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Defensive interval ratio (DIR) on the desired side of its target for this period?

Inputs:

- `metric.defensive-interval-ratio-dir` (Defensive interval ratio (DIR))

Placements:

- organizational / functional / Management / Financial stability (x3433, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Firm exposure

- id: `kpi.management.firm-exposure`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Firm exposure measures that result inside Management, subcategory Financial stability. The unit is currency. The formula is A, where A is Firm exposure. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Firm exposure on the desired side of its target for this period?

Inputs:

- `metric.firm-exposure` (Firm exposure)

Placements:

- organizational / functional / Management / Financial stability (x3842, page_0017)
- organizational / industries / Financial Institutions / xKPI ▼ Key Performance Indicator name (xCI842, page_0082)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Payroll tax paid by the employer

- id: `kpi.management.payroll-tax-paid-by-the-employer`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Payroll tax paid by the employer measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Payroll tax paid by the employer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Payroll tax paid by the employer on the desired side of its target for this period?

Inputs:

- `metric.payroll-tax-paid-by-the-employer` (Payroll tax paid by the employer)

Placements:

- organizational / functional / Management / Financial stability (x3945, page_0017)
- organizational / industries / Non-profit / Other (xK5945, page_0153)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Bad debt write-offs from gross revenue

- id: `kpi.management.bad-debt-write-offs-from-gross-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.financial-stability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Bad debt write-offs from gross revenue measures that result inside Management, subcategory Financial stability. The unit is percent. The formula is (A / B) * 100, where A is Bad debt write-offs, B is gross revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Bad debt write-offs from gross revenue on the desired side of its target for this period?

Inputs:

- `metric.bad-debt-write-offs` (Bad debt write-offs)
- `metric.gross-revenue` (gross revenue)

Placements:

- organizational / functional / Management / Financial stability (x6138, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to rescind credit balances

- id: `kpi.management.time-to-rescind-credit-balances`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to rescind credit balances measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Time to rescind credit balances. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to rescind credit balances on the desired side of its target for this period?

Inputs:

- `metric.time-to-rescind-credit-balances` (Time to rescind credit balances)

Placements:

- organizational / functional / Management / Financial stability (x6105, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Capital gearing

- id: `kpi.management.capital-gearing`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Capital gearing measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Capital gearing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Capital gearing on the desired side of its target for this period?

Inputs:

- `metric.capital-gearing` (Capital gearing)

Placements:

- organizational / functional / Management / Financial stability (x6103, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Capital return for the current and prior three quarters

- id: `kpi.management.capital-return-for-the-current-and-prior-three-quarters`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Capital return for the current and prior three quarters measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Capital return for the current and prior three quarters. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Capital return for the current and prior three quarters on the desired side of its target for this period?

Inputs:

- `metric.capital-return-for-the-current-and-prior-three-quarters` (Capital return for the current and prior three quarters)

Placements:

- organizational / functional / Management / Financial stability (x1620, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt to assets

- id: `kpi.management.debt-to-assets`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt to assets measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Debt to assets. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt to assets on the desired side of its target for this period?

Inputs:

- `metric.debt-to-assets` (Debt to assets)

Placements:

- organizational / functional / Management / Financial stability (x1602, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt-Equity ratio

- id: `kpi.management.debt-equity-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.financial-stability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt-Equity ratio measures that result inside Management, subcategory Financial stability. The unit is count. The formula is A, where A is Debt-Equity ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt-Equity ratio on the desired side of its target for this period?

Inputs:

- `metric.debt-equity-ratio` (Debt-Equity ratio)

Placements:

- organizational / functional / Management / Financial stability (x1603, page_0017)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

# Management / Profitability

Context: organizational. Group: functional. KPIs: 7.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Gross profit margin

- id: `kpi.accounting.gross-profit-margin`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Share of revenue left after direct cost. Placed under Accounting / Cost Analysis.

Questions: Is Gross profit margin on the desired side of its target for this period?

Inputs:

- `metric.gross-profit` (gross profit)
- `metric.revenue` (revenue)

Placements:

- organizational / functional / Accounting / Cost Analysis (x8316, page_0009)
- organizational / functional / Management / Profitability (K316, page_0018)

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

### SBIT (Farnings Before Interest and Taxes)

- id: `kpi.management.sbit-farnings-before-interest-and-taxes`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

SBIT (Farnings Before Interest and Taxes) measures that result inside Management, subcategory Profitability. The unit is number. The formula is A, where A is SBIT (Farnings Before Interest and Taxes). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is SBIT (Farnings Before Interest and Taxes) on the desired side of its target for this period?

Inputs:

- `metric.sbit-farnings-before-interest-and-taxes` (SBIT (Farnings Before Interest and Taxes))

Placements:

- organizational / functional / Management / Profitability (K190, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Return on equity (ROE)

- id: `kpi.management.return-on-equity-roe`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.profitability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Return on equity (ROE) measures that result inside Management, subcategory Profitability. The unit is percent. The formula is (A / B) * 100, where A is part named by Return on equity (ROE), B is whole named by Return on equity (ROE). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Return on equity (ROE) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-return-on-equity-roe` (part named by Return on equity (ROE))
- `metric.whole-named-by-return-on-equity-roe` (whole named by Return on equity (ROE))

Placements:

- organizational / functional / Management / Profitability (K298, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Return on asset

- id: `kpi.management.return-on-asset`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.profitability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Return on asset measures that result inside Management, subcategory Profitability. The unit is percent. The formula is (A / B) * 100, where A is part named by Return on asset, B is whole named by Return on asset. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Return on asset on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-return-on-asset` (part named by Return on asset)
- `metric.whole-named-by-return-on-asset` (whole named by Return on asset)

Placements:

- organizational / functional / Management / Profitability (K400, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Return on security investment (ROSII)

- id: `kpi.management.return-on-security-investment-rosii`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.profitability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Return on security investment (ROSII) measures that result inside Management, subcategory Profitability. The unit is percent. The formula is (A / B) * 100, where A is part named by Return on security investment (ROSII), B is whole named by Return on security investment (ROSII). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Return on security investment (ROSII) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-return-on-security-investment-rosii` (part named by Return on security investment (ROSII))
- `metric.whole-named-by-return-on-security-investment-rosii` (whole named by Return on security investment (ROSII))

Placements:

- organizational / functional / Management / Profitability (K431, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Return on total assets (ROTA)

- id: `kpi.management.return-on-total-assets-rota`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.profitability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Return on total assets (ROTA) measures that result inside Management, subcategory Profitability. The unit is percent. The formula is (A / B) * 100, where A is part named by Return on total assets (ROTA), B is whole named by Return on total assets (ROTA). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Return on total assets (ROTA) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-return-on-total-assets-rota` (part named by Return on total assets (ROTA))
- `metric.whole-named-by-return-on-total-assets-rota` (whole named by Return on total assets (ROTA))

Placements:

- organizational / functional / Management / Profitability (K463, page_0018)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

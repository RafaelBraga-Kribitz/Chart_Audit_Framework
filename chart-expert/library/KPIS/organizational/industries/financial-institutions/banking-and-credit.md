# Financial Institutions / Banking and Credit

Context: organizational. Group: industries. KPIs: 45.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Operating costs

- id: `kpi.accounting.operating-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.accounting.cost-analysis`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating costs measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Operating costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating costs on the desired side of its target for this period?

Inputs:

- `metric.operating-costs` (Operating costs)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83159, page_0009)
- organizational / industries / Financial Institutions / Banking and Credit (sKR159, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Reserve ratio

- id: `kpi.planning.reserve-ratio`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.planning.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Reserve ratio measures that result inside Planning, subcategory Organizational • Functional Areas. The unit is currency. The formula is A, where A is Reserve ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Reserve ratio on the desired side of its target for this period?

Inputs:

- `metric.reserve-ratio` (Reserve ratio)

Placements:

- organizational / functional / Planning / Organizational • Functional Areas (xS392, page_0010)
- organizational / industries / Financial Institutions / Banking and Credit (sKR392, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of loans and investments

- id: `kpi.management.value-of-loans-and-investments`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: strategic
- formula: `A`
- formula type: count
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of loans and investments measures that result inside Management, subcategory Organizational » Functional Areas. The unit is number. The formula is A, where A is Value of loans and investments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of loans and investments on the desired side of its target for this period?

Inputs:

- `metric.value-of-loans-and-investments` (Value of loans and investments)

Placements:

- organizational / functional / Management / Organizational » Functional Areas (x3090, page_0017)
- organizational / industries / Financial Institutions / Banking and Credit (sKR090, page_0079)
- organizational / industries / Financial Institutions / Insurance (sK390, page_0081)
- organizational / industries / Financial Institutions / xKPI ▼ Key Performance Indicator name (xSC090, page_0082)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Combined loan to value ratio (CLTV ratio)

- id: `kpi.management.combined-loan-to-value-ratio-cltv-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: strategic
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.management.organizational-functional-areas`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Combined loan to value ratio (CLTV ratio) measures that result inside Management, subcategory Organizational» Functional Areas. The unit is percent. The formula is (A / B) * 100, where A is Combined loan, B is value ratio (CLTV ratio). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Combined loan to value ratio (CLTV ratio) on the desired side of its target for this period?

Inputs:

- `metric.combined-loan` (Combined loan)
- `metric.value-ratio-cltv-ratio` (value ratio (CLTV ratio))

Placements:

- organizational / functional / Management / Organizational» Functional Areas (x31105, page_0018)
- organizational / industries / Financial Institutions / Banking and Credit (sKR105, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Soft prepayment penalty

- id: `kpi.financial-institutions.soft-prepayment-penalty`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Soft prepayment penalty measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is currency. The formula is A, where A is Soft prepayment penalty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Soft prepayment penalty on the desired side of its target for this period?

Inputs:

- `metric.soft-prepayment-penalty` (Soft prepayment penalty)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR85, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Efficiency ratio

- id: `kpi.financial-institutions.efficiency-ratio`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Efficiency ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is currency. The formula is A, where A is Efficiency ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Efficiency ratio on the desired side of its target for this period?

Inputs:

- `metric.efficiency-ratio` (Efficiency ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR43, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt service ratio (DS)

- id: `kpi.financial-institutions.debt-service-ratio-ds`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt service ratio (DS) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Debt service ratio (DS), B is base of Debt service ratio (DS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt service ratio (DS) on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-debt-service-ratio-ds` (numerator of Debt service ratio (DS))
- `metric.base-of-debt-service-ratio-ds` (base of Debt service ratio (DS))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR44, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gross debt service ratio (GDIS)

- id: `kpi.financial-institutions.gross-debt-service-ratio-gdis`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Gross debt service ratio (GDIS) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Gross debt service ratio (GDIS), B is base of Gross debt service ratio (GDIS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gross debt service ratio (GDIS) on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-gross-debt-service-ratio-gdis` (numerator of Gross debt service ratio (GDIS))
- `metric.base-of-gross-debt-service-ratio-gdis` (base of Gross debt service ratio (GDIS))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR54, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adjusted return on equity

- id: `kpi.financial-institutions.adjusted-return-on-equity`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Adjusted return on equity measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Adjusted return on equity, B is whole named by Adjusted return on equity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adjusted return on equity on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-adjusted-return-on-equity` (part named by Adjusted return on equity)
- `metric.whole-named-by-adjusted-return-on-equity` (whole named by Adjusted return on equity)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR399, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Adjusted return on assets (AROA)

- id: `kpi.financial-institutions.adjusted-return-on-assets-aroa`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Adjusted return on assets (AROA) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Adjusted return on assets (AROA), B is whole named by Adjusted return on assets (AROA). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Adjusted return on assets (AROA) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-adjusted-return-on-assets-aroa` (part named by Adjusted return on assets (AROA))
- `metric.whole-named-by-adjusted-return-on-assets-aroa` (whole named by Adjusted return on assets (AROA))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR61, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Capital adequacy ratio (CAR)

- id: `kpi.financial-institutions.capital-adequacy-ratio-car`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Capital adequacy ratio (CAR) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Capital adequacy ratio (CAR), B is base of Capital adequacy ratio (CAR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Capital adequacy ratio (CAR) on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-capital-adequacy-ratio-car` (numerator of Capital adequacy ratio (CAR))
- `metric.base-of-capital-adequacy-ratio-car` (base of Capital adequacy ratio (CAR))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR42, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Portfolio at risk

- id: `kpi.financial-institutions.portfolio-at-risk`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Portfolio at risk measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Portfolio at risk, B is whole named by Portfolio at risk. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Portfolio at risk on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-portfolio-at-risk` (part named by Portfolio at risk)
- `metric.whole-named-by-portfolio-at-risk` (whole named by Portfolio at risk)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR43, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Financial self-sufficiency

- id: `kpi.financial-institutions.financial-self-sufficiency`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Financial self-sufficiency measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Financial self-sufficiency, B is whole named by Financial self-sufficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Financial self-sufficiency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-financial-self-sufficiency` (part named by Financial self-sufficiency)
- `metric.whole-named-by-financial-self-sufficiency` (whole named by Financial self-sufficiency)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR44, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Operating self-sufficiency (OSS)

- id: `kpi.financial-institutions.operating-self-sufficiency-oss`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Operating self-sufficiency (OSS) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Operating self-sufficiency (OSS), B is whole named by Operating self-sufficiency (OSS). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Operating self-sufficiency (OSS) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-operating-self-sufficiency-oss` (part named by Operating self-sufficiency (OSS))
- `metric.whole-named-by-operating-self-sufficiency-oss` (whole named by Operating self-sufficiency (OSS))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR05, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Portfolio yield

- id: `kpi.financial-institutions.portfolio-yield`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Portfolio yield measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Portfolio yield, B is whole named by Portfolio yield. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Portfolio yield on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-portfolio-yield` (part named by Portfolio yield)
- `metric.whole-named-by-portfolio-yield` (whole named by Portfolio yield)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR06, page_0079)
- organizational / industries / Financial Institutions / xKPI ▼ Key Performance Indicator name (xK406, page_0082)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Price-to-income ratio

- id: `kpi.financial-institutions.price-to-income-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Price-to-income ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Price-to-income ratio, B is base of Price-to-income ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Price-to-income ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-price-to-income-ratio` (numerator of Price-to-income ratio)
- `metric.base-of-price-to-income-ratio` (base of Price-to-income ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR13, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net interest spread

- id: `kpi.financial-institutions.net-interest-spread`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net interest spread measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Net interest spread, B is whole named by Net interest spread. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net interest spread on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-net-interest-spread` (part named by Net interest spread)
- `metric.whole-named-by-net-interest-spread` (whole named by Net interest spread)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR26, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Annual equivalent rate

- id: `kpi.financial-institutions.annual-equivalent-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Annual equivalent rate measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Annual equivalent rate, B is base of Annual equivalent rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Annual equivalent rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-annual-equivalent-rate` (numerator of Annual equivalent rate)
- `metric.base-of-annual-equivalent-rate` (base of Annual equivalent rate)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR15, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Gross interest rate

- id: `kpi.financial-institutions.gross-interest-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Gross interest rate measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Gross interest rate, B is base of Gross interest rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Gross interest rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-gross-interest-rate` (numerator of Gross interest rate)
- `metric.base-of-gross-interest-rate` (base of Gross interest rate)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR18, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Herd prepayment penalty

- id: `kpi.financial-institutions.herd-prepayment-penalty`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Herd prepayment penalty measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Herd prepayment penalty, B is whole named by Herd prepayment penalty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Herd prepayment penalty on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-herd-prepayment-penalty` (part named by Herd prepayment penalty)
- `metric.whole-named-by-herd-prepayment-penalty` (whole named by Herd prepayment penalty)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR48, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt-service coverage ratio (DSCR)

- id: `kpi.financial-institutions.debt-service-coverage-ratio-dscr`
- kind: kpi
- unit: count
- direction: corridor
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt-service coverage ratio (DSCR) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is count. The formula is A, where A is Debt-service coverage ratio (DSCR). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt-service coverage ratio (DSCR) on the desired side of its target for this period?

Inputs:

- `metric.debt-service-coverage-ratio-dscr` (Debt-service coverage ratio (DSCR))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR65, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Loan-to-value (LTV)

- id: `kpi.financial-institutions.loan-to-value-ltv`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Loan-to-value (LTV) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Loan-to-value (LTV), B is whole named by Loan-to-value (LTV). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Loan-to-value (LTV) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-loan-to-value-ltv` (part named by Loan-to-value (LTV))
- `metric.whole-named-by-loan-to-value-ltv` (whole named by Loan-to-value (LTV))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR065, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Debt-to-income ratio (DTI)

- id: `kpi.financial-institutions.debt-to-income-ratio-dti`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Debt-to-income ratio (DTI) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Debt-to-income ratio (DTI), B is base of Debt-to-income ratio (DTI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Debt-to-income ratio (DTI) on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-debt-to-income-ratio-dti` (numerator of Debt-to-income ratio (DTI))
- `metric.base-of-debt-to-income-ratio-dti` (base of Debt-to-income ratio (DTI))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR266, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Securitized loans

- id: `kpi.financial-institutions.securitized-loans`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Securitized loans measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Securitized loans, B is whole named by Securitized loans. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Securitized loans on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-securitized-loans` (part named by Securitized loans)
- `metric.whole-named-by-securitized-loans` (whole named by Securitized loans)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR276, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Probability of default (PD)

- id: `kpi.financial-institutions.probability-of-default-pd`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Probability of default (PD) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is Probability, B is default (PD). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Probability of default (PD) on the desired side of its target for this period?

Inputs:

- `metric.probability` (Probability)
- `metric.default-pd` (default (PD))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR279, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Long term loan default risk (ELDI)

- id: `kpi.financial-institutions.long-term-loan-default-risk-eldi`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Long term loan default risk (ELDI) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Long term loan default risk (ELDI), B is whole named by Long term loan default risk (ELDI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Long term loan default risk (ELDI) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-long-term-loan-default-risk-eldi` (part named by Long term loan default risk (ELDI))
- `metric.whole-named-by-long-term-loan-default-risk-eldi` (whole named by Long term loan default risk (ELDI))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR11, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Exposure of default (LAD)

- id: `kpi.financial-institutions.exposure-of-default-lad`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Exposure of default (LAD) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is Exposure, B is default (LAD). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Exposure of default (LAD) on the desired side of its target for this period?

Inputs:

- `metric.exposure` (Exposure)
- `metric.default-lad` (default (LAD))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR451, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Exposure to default (LAD)

- id: `kpi.financial-institutions.exposure-to-default-lad`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Exposure to default (LAD) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is Exposure, B is default (LAD). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Exposure to default (LAD) on the desired side of its target for this period?

Inputs:

- `metric.exposure` (Exposure)
- `metric.default-lad` (default (LAD))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR452, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expected loss from exposure at default (ELI)

- id: `kpi.financial-institutions.expected-loss-from-exposure-at-default-eli`
- kind: kri
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Expected loss from exposure at default (ELI) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is Expected loss, B is exposure at default (ELI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expected loss from exposure at default (ELI) on the desired side of its target for this period?

Inputs:

- `metric.expected-loss` (Expected loss)
- `metric.exposure-at-default-eli` (exposure at default (ELI))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR53, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Corporate credit rating

- id: `kpi.financial-institutions.corporate-credit-rating`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Corporate credit rating measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is count. The formula is A, where A is Corporate credit rating. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Corporate credit rating on the desired side of its target for this period?

Inputs:

- `metric.corporate-credit-rating` (Corporate credit rating)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR279, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Credit loss ratio

- id: `kpi.financial-institutions.credit-loss-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Credit loss ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Credit loss ratio, B is base of Credit loss ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Credit loss ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-credit-loss-ratio` (numerator of Credit loss ratio)
- `metric.base-of-credit-loss-ratio` (base of Credit loss ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR279, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Maximum loan-to-value ratio

- id: `kpi.financial-institutions.maximum-loan-to-value-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Maximum loan-to-value ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Maximum loan-to-value ratio, B is base of Maximum loan-to-value ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Maximum loan-to-value ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-maximum-loan-to-value-ratio` (numerator of Maximum loan-to-value ratio)
- `metric.base-of-maximum-loan-to-value-ratio` (base of Maximum loan-to-value ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR301, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Risk-adjusted capital ratio

- id: `kpi.financial-institutions.risk-adjusted-capital-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Risk-adjusted capital ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Risk-adjusted capital ratio, B is base of Risk-adjusted capital ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Risk-adjusted capital ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-risk-adjusted-capital-ratio` (numerator of Risk-adjusted capital ratio)
- `metric.base-of-risk-adjusted-capital-ratio` (base of Risk-adjusted capital ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR015, page_0079)
- organizational / industries / Financial Institutions / Insurance (sK1015, page_0081)
- organizational / industries / Financial Institutions / xKPI ▼ Key Performance Indicator name (xSC015, page_0082)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net interest income (NEI)

- id: `kpi.financial-institutions.net-interest-income-nei`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net interest income (NEI) measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Net interest income (NEI), B is whole named by Net interest income (NEI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net interest income (NEI) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-net-interest-income-nei` (part named by Net interest income (NEI))
- `metric.whole-named-by-net-interest-income-nei` (whole named by Net interest income (NEI))

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR061, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Front-end rating

- id: `kpi.financial-institutions.front-end-rating`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Front-end rating measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Front-end rating, B is whole named by Front-end rating. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Front-end rating on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-front-end-rating` (part named by Front-end rating)
- `metric.whole-named-by-front-end-rating` (whole named by Front-end rating)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR117, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### High risk ratio

- id: `kpi.financial-institutions.high-risk-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

High risk ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of High risk ratio, B is base of High risk ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is High risk ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-high-risk-ratio` (numerator of High risk ratio)
- `metric.base-of-high-risk-ratio` (base of High risk ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR132, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Liquidity ratio

- id: `kpi.financial-institutions.liquidity-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Liquidity ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Liquidity ratio, B is base of Liquidity ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Liquidity ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-liquidity-ratio` (numerator of Liquidity ratio)
- `metric.base-of-liquidity-ratio` (base of Liquidity ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR132, page_0079)
- organizational / industries / Financial Institutions / Insurance (sK1322, page_0081)
- organizational / industries / Financial Institutions / xKPI ▼ Key Performance Indicator name (xCI122, page_0082)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Young debt

- id: `kpi.financial-institutions.young-debt`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Young debt measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Young debt, B is whole named by Young debt. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Young debt on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-young-debt` (part named by Young debt)
- `metric.whole-named-by-young-debt` (whole named by Young debt)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR231, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Amortization term

- id: `kpi.financial-institutions.amortization-term`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Amortization term measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Amortization term, B is whole named by Amortization term. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Amortization term on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-amortization-term` (part named by Amortization term)
- `metric.whole-named-by-amortization-term` (whole named by Amortization term)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR231, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Prepayment penalty

- id: `kpi.financial-institutions.prepayment-penalty`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Prepayment penalty measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by Prepayment penalty, B is whole named by Prepayment penalty. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Prepayment penalty on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-prepayment-penalty` (part named by Prepayment penalty)
- `metric.whole-named-by-prepayment-penalty` (whole named by Prepayment penalty)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR337, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### McDown/推开

- id: `kpi.financial-institutions.mcdown`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

McDown/推开 measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is part named by McDown/推开, B is whole named by McDown/推开. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is McDown/推开 on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-mcdown` (part named by McDown/推开)
- `metric.whole-named-by-mcdown` (whole named by McDown/推开)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR419, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Texan ratio

- id: `kpi.financial-institutions.texan-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Texan ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Texan ratio, B is base of Texan ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Texan ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-texan-ratio` (numerator of Texan ratio)
- `metric.base-of-texan-ratio` (base of Texan ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR426, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cooke ratio

- id: `kpi.financial-institutions.cooke-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cooke ratio measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is percent. The formula is (A / B) * 100, where A is numerator of Cooke ratio, B is base of Cooke ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cooke ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-cooke-ratio` (numerator of Cooke ratio)
- `metric.base-of-cooke-ratio` (base of Cooke ratio)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR453, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Loan officer productivity

- id: `kpi.financial-institutions.loan-officer-productivity`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Loan officer productivity measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is count. The formula is A, where A is Loan officer productivity. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Loan officer productivity on the desired side of its target for this period?

Inputs:

- `metric.loan-officer-productivity` (Loan officer productivity)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR616, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per dollar loaned

- id: `kpi.financial-institutions.cost-per-dollar-loaned`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.financial-institutions.banking-and-credit`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per dollar loaned measures that result inside Financial Institutions, subcategory Banking and Credit. The unit is count. The formula is A / B, where A is Cost, B is dollar loaned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per dollar loaned on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.dollar-loaned` (dollar loaned)

Placements:

- organizational / industries / Financial Institutions / Banking and Credit (sKR526, page_0079)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

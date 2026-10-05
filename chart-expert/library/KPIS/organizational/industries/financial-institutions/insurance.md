# Financial Institutions / Insurance

Context: organizational. Group: industries. KPIs: 69.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Burning cost ratio

- id: `kpi.accounting.burning-cost-ratio`
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

Burning cost ratio measures that result inside Accounting, subcategory Cost Analysis. The unit is count. The formula is A, where A is Burning cost ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Burning cost ratio on the desired side of its target for this period?

Inputs:

- `metric.burning-cost-ratio` (Burning cost ratio)

Placements:

- organizational / functional / Accounting / Cost Analysis (x83145, page_0009)
- organizational / industries / Financial Institutions / Insurance (sK145, page_0081)

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

### Combined ratio

- id: `kpi.financial-institutions.combined-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Combined ratio measures that result inside Financial Institutions, subcategory Organizational = Industries. The unit is count. The formula is A, where A is Combined ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Combined ratio on the desired side of its target for this period?

Inputs:

- `metric.combined-ratio` (Combined ratio)

Placements:

- organizational / industries / Financial Institutions / Organizational = Industries (sK14789, page_0080)
- organizational / industries / Financial Institutions / Insurance (sK352, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policy reserves

- id: `kpi.financial-institutions.policy-reserves`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policy reserves measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Policy reserves, B is whole named by Policy reserves. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policy reserves on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-policy-reserves` (part named by Policy reserves)
- `metric.whole-named-by-policy-reserves` (whole named by Policy reserves)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK161, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Missed payments or lapses

- id: `kpi.financial-institutions.missed-payments-or-lapses`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Missed payments or lapses measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Missed payments or lapses, B is whole named by Missed payments or lapses. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Missed payments or lapses on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-missed-payments-or-lapses` (part named by Missed payments or lapses)
- `metric.whole-named-by-missed-payments-or-lapses` (whole named by Missed payments or lapses)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK162, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insurance policy value

- id: `kpi.financial-institutions.insurance-policy-value`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insurance policy value measures that result inside Financial Institutions, subcategory Insurance. The unit is currency. The formula is A, where A is Insurance policy value. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insurance policy value on the desired side of its target for this period?

Inputs:

- `metric.insurance-policy-value` (Insurance policy value)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK163, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policy sales

- id: `kpi.financial-institutions.policy-sales`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policy sales measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Policy sales. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policy sales on the desired side of its target for this period?

Inputs:

- `metric.policy-sales` (Policy sales)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK440, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Not take up (NTU) ratio

- id: `kpi.financial-institutions.not-take-up-ntu-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Not take up (NTU) ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Not take up (NTU) ratio, B is base of Not take up (NTU) ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Not take up (NTU) ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-not-take-up-ntu-ratio` (numerator of Not take up (NTU) ratio)
- `metric.base-of-not-take-up-ntu-ratio` (base of Not take up (NTU) ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK146, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insurance loss ratio

- id: `kpi.financial-institutions.insurance-loss-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insurance loss ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Insurance loss ratio, B is base of Insurance loss ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insurance loss ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-insurance-loss-ratio` (numerator of Insurance loss ratio)
- `metric.base-of-insurance-loss-ratio` (base of Insurance loss ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK54, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insurance claim processing time

- id: `kpi.financial-institutions.insurance-claim-processing-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insurance claim processing time measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Insurance claim processing time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insurance claim processing time on the desired side of its target for this period?

Inputs:

- `metric.insurance-claim-processing-time` (Insurance claim processing time)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK573, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insurance underwriting time

- id: `kpi.financial-institutions.insurance-underwriting-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insurance underwriting time measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Insurance underwriting time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insurance underwriting time on the desired side of its target for this period?

Inputs:

- `metric.insurance-underwriting-time` (Insurance underwriting time)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK579, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New insurance policies issued

- id: `kpi.financial-institutions.new-insurance-policies-issued`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New insurance policies issued measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is New insurance policies issued. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New insurance policies issued on the desired side of its target for this period?

Inputs:

- `metric.new-insurance-policies-issued` (New insurance policies issued)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK580, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insured claims processed

- id: `kpi.financial-institutions.insured-claims-processed`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insured claims processed measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Insured claims processed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insured claims processed on the desired side of its target for this period?

Inputs:

- `metric.insured-claims-processed` (Insured claims processed)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK581, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Free asset ratio (PAI)

- id: `kpi.financial-institutions.free-asset-ratio-pai`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Free asset ratio (PAI) measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Free asset ratio (PAI), B is base of Free asset ratio (PAI). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Free asset ratio (PAI) on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-free-asset-ratio-pai` (numerator of Free asset ratio (PAI))
- `metric.base-of-free-asset-ratio-pai` (base of Free asset ratio (PAI))

Placements:

- organizational / industries / Financial Institutions / Insurance (sK994, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insured but not represented review

- id: `kpi.financial-institutions.insured-but-not-represented-review`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insured but not represented review measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Insured but not represented review. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insured but not represented review on the desired side of its target for this period?

Inputs:

- `metric.insured-but-not-represented-review` (Insured but not represented review)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK552, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Profit on risk elements to provisions ratio

- id: `kpi.financial-institutions.profit-on-risk-elements-to-provisions-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Profit on risk elements to provisions ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Profit on risk elements to provisions ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Profit on risk elements to provisions ratio on the desired side of its target for this period?

Inputs:

- `metric.profit-on-risk-elements-to-provisions-ratio` (Profit on risk elements to provisions ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK568, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insurance solvency ratio

- id: `kpi.financial-institutions.insurance-solvency-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insurance solvency ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Insurance solvency ratio, B is base of Insurance solvency ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insurance solvency ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-insurance-solvency-ratio` (numerator of Insurance solvency ratio)
- `metric.base-of-insurance-solvency-ratio` (base of Insurance solvency ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK657, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claim denials

- id: `kpi.financial-institutions.claim-denials`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claim denials measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Claim denials. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claim denials on the desired side of its target for this period?

Inputs:

- `metric.claim-denials` (Claim denials)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK4575, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claims reported

- id: `kpi.financial-institutions.claims-reported`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claims reported measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Claims reported. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claims reported on the desired side of its target for this period?

Inputs:

- `metric.claims-reported` (Claims reported)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK576, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cash claims

- id: `kpi.financial-institutions.cash-claims`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cash claims measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Cash claims. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cash claims on the desired side of its target for this period?

Inputs:

- `metric.cash-claims` (Cash claims)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK577, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insured claims

- id: `kpi.financial-institutions.insured-claims`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insured claims measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Insured claims. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insured claims on the desired side of its target for this period?

Inputs:

- `metric.insured-claims` (Insured claims)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK579, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Promotions and credit status

- id: `kpi.financial-institutions.promotions-and-credit-status`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Promotions and credit status measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Promotions and credit status, B is whole named by Promotions and credit status. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Promotions and credit status on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-promotions-and-credit-status` (part named by Promotions and credit status)
- `metric.whole-named-by-promotions-and-credit-status` (whole named by Promotions and credit status)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK580, page_0081)
- organizational / industries / Financial Institutions / Insurance (sK588, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claims settlement

- id: `kpi.financial-institutions.claims-settlement`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claims settlement measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Claims settlement. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claims settlement on the desired side of its target for this period?

Inputs:

- `metric.claims-settlement` (Claims settlement)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK587, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Funding expense ratio

- id: `kpi.financial-institutions.funding-expense-ratio`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Funding expense ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Funding expense ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Funding expense ratio on the desired side of its target for this period?

Inputs:

- `metric.funding-expense-ratio` (Funding expense ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK589, page_0081)
- organizational / industries / Financial Institutions / Insurance (sK595, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expense ratio per line of insurance

- id: `kpi.financial-institutions.expense-ratio-per-line-of-insurance`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Expense ratio per line of insurance measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is A / B, where A is Expense ratio, B is line of insurance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expense ratio per line of insurance on the desired side of its target for this period?

Inputs:

- `metric.expense-ratio` (Expense ratio)
- `metric.line-of-insurance` (line of insurance)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK595, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expense to previous

- id: `kpi.financial-institutions.expense-to-previous`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Expense to previous measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Expense, B is previous. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expense to previous on the desired side of its target for this period?

Inputs:

- `metric.expense` (Expense)
- `metric.previous` (previous)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK595, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Incurred expense ratio

- id: `kpi.financial-institutions.incurred-expense-ratio`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Incurred expense ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Incurred expense ratio, B is base of Incurred expense ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Incurred expense ratio on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-incurred-expense-ratio` (numerator of Incurred expense ratio)
- `metric.base-of-incurred-expense-ratio` (base of Incurred expense ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK598, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Face value of policies sold

- id: `kpi.financial-institutions.face-value-of-policies-sold`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Face value of policies sold measures that result inside Financial Institutions, subcategory Insurance. The unit is currency. The formula is A, where A is Face value of policies sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Face value of policies sold on the desired side of its target for this period?

Inputs:

- `metric.face-value-of-policies-sold` (Face value of policies sold)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK4055, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Lapsed policies from sold

- id: `kpi.financial-institutions.lapsed-policies-from-sold`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Lapsed policies from sold measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Lapsed policies, B is sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Lapsed policies from sold on the desired side of its target for this period?

Inputs:

- `metric.lapsed-policies` (Lapsed policies)
- `metric.sold` (sold)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK4056, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policies that lapsed within the first two years

- id: `kpi.financial-institutions.policies-that-lapsed-within-the-first-two-years`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policies that lapsed within the first two years measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Policies that lapsed within the first two years, B is whole named by Policies that lapsed within the first two years. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policies that lapsed within the first two years on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-policies-that-lapsed-within-the-first-two-years` (part named by Policies that lapsed within the first two years)
- `metric.whole-named-by-policies-that-lapsed-within-the-first-two-years` (whole named by Policies that lapsed within the first two years)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK4057, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policyholder liabilities to shareholder/-funds ratio

- id: `kpi.financial-institutions.policyholder-liabilities-to-shareholder-funds-ratio`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policyholder liabilities to shareholder/-funds ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Policyholder liabilities, B is shareholder/-funds ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policyholder liabilities to shareholder/-funds ratio on the desired side of its target for this period?

Inputs:

- `metric.policyholder-liabilities` (Policyholder liabilities)
- `metric.shareholder-funds-ratio` (shareholder/-funds ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK4059, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Women policy holders

- id: `kpi.financial-institutions.women-policy-holders`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Women policy holders measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Women policy holders, B is whole named by Women policy holders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Women policy holders on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-women-policy-holders` (part named by Women policy holders)
- `metric.whole-named-by-women-policy-holders` (whole named by Women policy holders)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6010, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Premium collection rate

- id: `kpi.financial-institutions.premium-collection-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Premium collection rate measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Premium collection rate, B is base of Premium collection rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Premium collection rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-premium-collection-rate` (numerator of Premium collection rate)
- `metric.base-of-premium-collection-rate` (base of Premium collection rate)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6011, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Premium income

- id: `kpi.financial-institutions.premium-income`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Premium income measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Premium income, B is whole named by Premium income. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Premium income on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-premium-income` (part named by Premium income)
- `metric.whole-named-by-premium-income` (whole named by Premium income)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6015, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Premium rate charged to clients

- id: `kpi.financial-institutions.premium-rate-charged-to-clients`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Premium rate charged to clients measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Premium rate charged, B is clients. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Premium rate charged to clients on the desired side of its target for this period?

Inputs:

- `metric.premium-rate-charged` (Premium rate charged)
- `metric.clients` (clients)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6019, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unearned premium reserve

- id: `kpi.financial-institutions.unearned-premium-reserve`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unearned premium reserve measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Unearned premium reserve, B is whole named by Unearned premium reserve. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unearned premium reserve on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-unearned-premium-reserve` (part named by Unearned premium reserve)
- `metric.whole-named-by-unearned-premium-reserve` (whole named by Unearned premium reserve)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6023, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Ratio of collective bonus potential to provisions

- id: `kpi.financial-institutions.ratio-of-collective-bonus-potential-to-provisions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Ratio of collective bonus potential to provisions measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Ratio of collective bonus potential to provisions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Ratio of collective bonus potential to provisions on the desired side of its target for this period?

Inputs:

- `metric.ratio-of-collective-bonus-potential-to-provisions` (Ratio of collective bonus potential to provisions)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6023, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Return on current fund

- id: `kpi.financial-institutions.return-on-current-fund`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Return on current fund measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Return on current fund, B is whole named by Return on current fund. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Return on current fund on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-return-on-current-fund` (part named by Return on current fund)
- `metric.whole-named-by-return-on-current-fund` (whole named by Return on current fund)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6024, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Interest rate risk

- id: `kpi.financial-institutions.interest-rate-risk`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Interest rate risk measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Interest rate risk, B is base of Interest rate risk. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Interest rate risk on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-interest-rate-risk` (numerator of Interest rate risk)
- `metric.base-of-interest-rate-risk` (base of Interest rate risk)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK5639, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Not in good order account applications (NGO)

- id: `kpi.financial-institutions.not-in-good-order-account-applications-ngo`
- kind: kpi
- unit: percent
- direction: up
- timing: leading
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Not in good order account applications (NGO) measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Not in good order account applications (NGO), B is whole named by Not in good order account applications (NGO). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Not in good order account applications (NGO) on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-not-in-good-order-account-applications-ngo` (part named by Not in good order account applications (NGO))
- `metric.whole-named-by-not-in-good-order-account-applications-ngo` (whole named by Not in good order account applications (NGO))

Placements:

- organizational / industries / Financial Institutions / Insurance (sK5827, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Screening of unknown claimants and high-dollar outpatients for financial assistance

- id: `kpi.financial-institutions.screening-of-unknown-claimants-and-high-dollar-outpatients-for-financial`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Screening of unknown claimants and high-dollar outpatients for financial assistance measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Screening, B is unknown claimants and high-dollar outpatients for financial assistance. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Screening of unknown claimants and high-dollar outpatients for financial assistance on the desired side of its target for this period?

Inputs:

- `metric.screening` (Screening)
- `metric.unknown-claimants-and-high-dollar-outpatients-for-financial-assistance` (unknown claimants and high-dollar outpatients for financial assistance)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6121, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to process medicare supplement insurance billing

- id: `kpi.financial-institutions.time-to-process-medicare-supplement-insurance-billing`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to process medicare supplement insurance billing measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Time to process medicare supplement insurance billing. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to process medicare supplement insurance billing on the desired side of its target for this period?

Inputs:

- `metric.time-to-process-medicare-supplement-insurance-billing` (Time to process medicare supplement insurance billing)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6156, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Denial rate (clinical and technical) out of gross revenue

- id: `kpi.financial-institutions.denial-rate-clinical-and-technical-out-of-gross-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Denial rate (clinical and technical) out of gross revenue measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Denial rate (clinical and technical) out, B is gross revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Denial rate (clinical and technical) out of gross revenue on the desired side of its target for this period?

Inputs:

- `metric.denial-rate-clinical-and-technical-out` (Denial rate (clinical and technical) out)
- `metric.gross-revenue` (gross revenue)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6171, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Additional collection for underpayments

- id: `kpi.financial-institutions.additional-collection-for-underpayments`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Additional collection for underpayments measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Additional collection for underpayments, B is whole named by Additional collection for underpayments. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Additional collection for underpayments on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-additional-collection-for-underpayments` (part named by Additional collection for underpayments)
- `metric.whole-named-by-additional-collection-for-underpayments` (whole named by Additional collection for underpayments)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6174, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Appeals overturned

- id: `kpi.financial-institutions.appeals-overturned`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Appeals overturned measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Appeals overturned, B is whole named by Appeals overturned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Appeals overturned on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-appeals-overturned` (part named by Appeals overturned)
- `metric.whole-named-by-appeals-overturned` (whole named by Appeals overturned)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6175, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Electronic eligibility rate

- id: `kpi.financial-institutions.electronic-eligibility-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Electronic eligibility rate measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Electronic eligibility rate, B is base of Electronic eligibility rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Electronic eligibility rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-electronic-eligibility-rate` (numerator of Electronic eligibility rate)
- `metric.base-of-electronic-eligibility-rate` (base of Electronic eligibility rate)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6176, page_0081)
- organizational / industries / Healthcare / Organizational » Industries (sKZ176, page_0112)
- organizational / industries / Healthcare / Organizational - Industries (sK6176, page_0125)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Underpayments overturn

- id: `kpi.financial-institutions.underpayments-overturn`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Underpayments overturn measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Underpayments overturn, B is whole named by Underpayments overturn. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Underpayments overturn on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-underpayments-overturn` (part named by Underpayments overturn)
- `metric.whole-named-by-underpayments-overturn` (whole named by Underpayments overturn)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK8181, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Medical claim denial reason codes per claim

- id: `kpi.financial-institutions.medical-claim-denial-reason-codes-per-claim`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Medical claim denial reason codes per claim measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A / B, where A is Medical claim denial reason codes, B is claim. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Medical claim denial reason codes per claim on the desired side of its target for this period?

Inputs:

- `metric.medical-claim-denial-reason-codes` (Medical claim denial reason codes)
- `metric.claim` (claim)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK8183, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overturn denial rate

- id: `kpi.financial-institutions.overturn-denial-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overturn denial rate measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is numerator of Overturn denial rate, B is base of Overturn denial rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overturn denial rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-overturn-denial-rate` (numerator of Overturn denial rate)
- `metric.base-of-overturn-denial-rate` (base of Overturn denial rate)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK8188, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claim claim payment duration

- id: `kpi.financial-institutions.claim-claim-payment-duration`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claim claim payment duration measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Claim claim payment duration. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claim claim payment duration on the desired side of its target for this period?

Inputs:

- `metric.claim-claim-payment-duration` (Claim claim payment duration)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK6189, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claim denials value from gross revenue

- id: `kpi.financial-institutions.claim-denials-value-from-gross-revenue`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claim denials value from gross revenue measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Claim denials value, B is gross revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claim denials value from gross revenue on the desired side of its target for this period?

Inputs:

- `metric.claim-denials-value` (Claim denials value)
- `metric.gross-revenue` (gross revenue)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK8208, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Claim ratio

- id: `kpi.financial-institutions.claim-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Claim ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Claim ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Claim ratio on the desired side of its target for this period?

Inputs:

- `metric.claim-ratio` (Claim ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK14721, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Expense ratio

- id: `kpi.financial-institutions.expense-ratio`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Expense ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Expense ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Expense ratio on the desired side of its target for this period?

Inputs:

- `metric.expense-ratio` (Expense ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK15229, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Net income ratio

- id: `kpi.financial-institutions.net-income-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Net income ratio measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Net income ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Net income ratio on the desired side of its target for this period?

Inputs:

- `metric.net-income-ratio` (Net income ratio)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK17983, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Amount of any additional dollar-based management costs

- id: `kpi.financial-institutions.amount-of-any-additional-dollar-based-management-costs`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Amount of any additional dollar-based management costs measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Amount of any additional dollar-based management costs. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Amount of any additional dollar-based management costs on the desired side of its target for this period?

Inputs:

- `metric.amount-of-any-additional-dollar-based-management-costs` (Amount of any additional dollar-based management costs)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK19332, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per year for the amount of cover

- id: `kpi.financial-institutions.cost-per-year-for-the-amount-of-cover`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per year for the amount of cover measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A / B, where A is Cost, B is year for the amount of cover. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per year for the amount of cover on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.year-for-the-amount-of-cover` (year for the amount of cover)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK19428, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Service fee

- id: `kpi.financial-institutions.service-fee`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Service fee measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Service fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Service fee on the desired side of its target for this period?

Inputs:

- `metric.service-fee` (Service fee)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK19794, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Contribution fee

- id: `kpi.financial-institutions.contribution-fee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Contribution fee measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Contribution fee, B is whole named by Contribution fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Contribution fee on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-contribution-fee` (part named by Contribution fee)
- `metric.whole-named-by-contribution-fee` (whole named by Contribution fee)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK20390, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Management costs for investment option to account

- id: `kpi.financial-institutions.management-costs-for-investment-option-to-account`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Management costs for investment option to account measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is Management costs for investment option, B is account. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Management costs for investment option to account on the desired side of its target for this period?

Inputs:

- `metric.management-costs-for-investment-option` (Management costs for investment option)
- `metric.account` (account)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK20977, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Termination fee

- id: `kpi.financial-institutions.termination-fee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Termination fee measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Termination fee, B is whole named by Termination fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Termination fee on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-termination-fee` (part named by Termination fee)
- `metric.whole-named-by-termination-fee` (whole named by Termination fee)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK21865, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Withdrawal fee

- id: `kpi.financial-institutions.withdrawal-fee`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Withdrawal fee measures that result inside Financial Institutions, subcategory Insurance. The unit is percent. The formula is (A / B) * 100, where A is part named by Withdrawal fee, B is whole named by Withdrawal fee. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Withdrawal fee on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-withdrawal-fee` (part named by Withdrawal fee)
- `metric.whole-named-by-withdrawal-fee` (whole named by Withdrawal fee)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK21919, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policies sold

- id: `kpi.financial-institutions.policies-sold`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policies sold measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Policies sold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policies sold on the desired side of its target for this period?

Inputs:

- `metric.policies-sold` (Policies sold)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK22391, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Foreign exchange transactions

- id: `kpi.financial-institutions.foreign-exchange-transactions`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Foreign exchange transactions measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Foreign exchange transactions. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Foreign exchange transactions on the desired side of its target for this period?

Inputs:

- `metric.foreign-exchange-transactions` (Foreign exchange transactions)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK22428, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Policies in force

- id: `kpi.financial-institutions.policies-in-force`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Policies in force measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Policies in force. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Policies in force on the desired side of its target for this period?

Inputs:

- `metric.policies-in-force` (Policies in force)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK22429, page_0081)
- organizational / industries / Financial Institutions / Insurance (sK22432, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Insurance for individuals

- id: `kpi.financial-institutions.insurance-for-individuals`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Insurance for individuals measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Insurance for individuals. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Insurance for individuals on the desired side of its target for this period?

Inputs:

- `metric.insurance-for-individuals` (Insurance for individuals)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK22430, page_0081)
- organizational / industries / Financial Institutions / Insurance (sK22433, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Annuities for individuals

- id: `kpi.financial-institutions.annuities-for-individuals`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.financial-institutions.insurance`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Annuities for individuals measures that result inside Financial Institutions, subcategory Insurance. The unit is count. The formula is A, where A is Annuities for individuals. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Annuities for individuals on the desired side of its target for this period?

Inputs:

- `metric.annuities-for-individuals` (Annuities for individuals)

Placements:

- organizational / industries / Financial Institutions / Insurance (sK22431, page_0081)
- organizational / industries / Financial Institutions / Insurance (sK22434, page_0081)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

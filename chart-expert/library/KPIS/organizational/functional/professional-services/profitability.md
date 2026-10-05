# Professional Services / Profitability

Context: organizational. Group: functional. KPIs: 2.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Gross profit per head

- id: `kpi.professional-services.gross-profit-per-head`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.professional-services.profitability`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Gross profit per fee earner. Published agency rules of thumb exist and are target notes, not laws. Placed under Professional Services / Profitability.

Questions: Is Gross profit per head on the desired side of its target for this period?

Inputs:

- `metric.gross-profit` (gross profit)
- `metric.fee-earners` (fee earners)

Placements:

- organizational / functional / Professional Services / Profitability (user-note, note)

Target notes:

- Published agency rule of thumb, not a law: about 135,000 AUD, 75,000 GBP, or 95,000 USD gross profit per head per year.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

### Team cost to gross profit

- id: `kpi.professional-services.team-cost-to-gross-profit`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.professional-services.profitability`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Team cost as a share of gross profit. Placed under Professional Services / Profitability.

Questions: Is Team cost to gross profit on the desired side of its target for this period?

Inputs:

- `metric.team-cost` (team cost)
- `metric.gross-profit` (gross profit)

Placements:

- organizational / functional / Professional Services / Profitability (user-note, note)

Target notes:

- Published agency rule of thumb: team cost at most 60 percent of gross profit.

Pitfall: Do not brief the analysis chart to an executive if the communication chart already answers the decision.

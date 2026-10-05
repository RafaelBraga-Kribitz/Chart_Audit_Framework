# Non-profit / General

Context: organizational. Group: industries. KPIs: 33.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Internal reports to members

- id: `kpi.human-resources.internal-reports-to-members`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.human-resources.efficiency-and-effectiveness`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, HR
- provenance: authored

Internal reports to members measures that result inside Human Resources, subcategory Efficiency and Effectiveness. The unit is count. The formula is A, where A is Internal reports to members. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Internal reports to members on the desired side of its target for this period?

Inputs:

- `metric.internal-reports-to-members` (Internal reports to members)

Placements:

- organizational / functional / Human Resources / Efficiency and Effectiveness (K85943, page_0022)
- organizational / industries / Non-profit / General (kS5943, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non-profit community projects

- id: `kpi.administration.non-profit-community-projects`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non-profit community projects measures that result inside Administration, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Non-profit community projects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non-profit community projects on the desired side of its target for this period?

Inputs:

- `metric.non-profit-community-projects` (Non-profit community projects)

Placements:

- organizational / industries / Administration / Organizational » Industries (sK9515, page_0097)
- organizational / industries / Non-profit / General (kS5915, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Community volunteers participation

- id: `kpi.administration.community-volunteers-participation`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Community volunteers participation measures that result inside Administration, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Community volunteers participation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Community volunteers participation on the desired side of its target for this period?

Inputs:

- `metric.community-volunteers-participation` (Community volunteers participation)

Placements:

- organizational / industries / Administration / Organizational » Industries (sK9712, page_0097)
- organizational / industries / Non-profit / General (kS5917, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Value of a volunteer work

- id: `kpi.administration.value-of-a-volunteer-work`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Value of a volunteer work measures that result inside Administration, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Value of a volunteer work. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Value of a volunteer work on the desired side of its target for this period?

Inputs:

- `metric.value-of-a-volunteer-work` (Value of a volunteer work)

Placements:

- organizational / industries / Administration / Organizational » Industries (sK5936, page_0097)
- organizational / industries / Non-profit / General (kS5938, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Non-profit organizations

- id: `kpi.administration.non-profit-organizations`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.administration.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Non-profit organizations measures that result inside Administration, subcategory General. The unit is count. The formula is A, where A is Non-profit organizations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Non-profit organizations on the desired side of its target for this period?

Inputs:

- `metric.non-profit-organizations` (Non-profit organizations)

Placements:

- global / human-development / Administration / General (sK594, page_0102)
- organizational / industries / Non-profit / General (kS5941, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Appeal Coverage

- id: `kpi.non-profit.appeal-coverage`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Appeal Coverage measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Appeal Coverage, B is whole named by Appeal Coverage. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Appeal Coverage on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-appeal-coverage` (part named by Appeal Coverage)
- `metric.whole-named-by-appeal-coverage` (whole named by Appeal Coverage)

Placements:

- organizational / industries / Non-profit / General (kS368, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from donations

- id: `kpi.non-profit.revenue-from-donations`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue from donations measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is Revenue, B is donations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from donations on the desired side of its target for this period?

Inputs:

- `metric.revenue` (Revenue)
- `metric.donations` (donations)

Placements:

- organizational / industries / Non-profit / General (kS5919, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Term loan donated delivered

- id: `kpi.non-profit.term-loan-donated-delivered`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Term loan donated delivered measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Term loan donated delivered, B is whole named by Term loan donated delivered. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Term loan donated delivered on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-term-loan-donated-delivered` (part named by Term loan donated delivered)
- `metric.whole-named-by-term-loan-donated-delivered` (whole named by Term loan donated delivered)

Placements:

- organizational / industries / Non-profit / General (kS590, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### New volunteers recruited in the last three months

- id: `kpi.non-profit.new-volunteers-recruited-in-the-last-three-months`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `line-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

New volunteers recruited in the last three months measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is New volunteers recruited in the last three months. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is New volunteers recruited in the last three months on the desired side of its target for this period?

Inputs:

- `metric.new-volunteers-recruited-in-the-last-three-months` (New volunteers recruited in the last three months)

Placements:

- organizational / industries / Non-profit / General (kS5920, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Donation to delivery time

- id: `kpi.non-profit.donation-to-delivery-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Donation to delivery time measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Donation to delivery time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Donation to delivery time on the desired side of its target for this period?

Inputs:

- `metric.donation-to-delivery-time` (Donation to delivery time)

Placements:

- organizational / industries / Non-profit / General (kK370, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Revenue from grants obtained

- id: `kpi.non-profit.revenue-from-grants-obtained`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Revenue from grants obtained measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Revenue from grants obtained. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Revenue from grants obtained on the desired side of its target for this period?

Inputs:

- `metric.revenue-from-grants-obtained` (Revenue from grants obtained)

Placements:

- organizational / industries / Non-profit / General (kS5921, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Donor financial efficiency

- id: `kpi.non-profit.donor-financial-efficiency`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Donor financial efficiency measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Donor financial efficiency, B is whole named by Donor financial efficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Donor financial efficiency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-donor-financial-efficiency` (part named by Donor financial efficiency)
- `metric.whole-named-by-donor-financial-efficiency` (whole named by Donor financial efficiency)

Placements:

- organizational / industries / Non-profit / General (kS371, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to submit grant applications

- id: `kpi.non-profit.time-to-submit-grant-applications`
- kind: kpi
- unit: count
- direction: down
- timing: leading
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to submit grant applications measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Time to submit grant applications. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to submit grant applications on the desired side of its target for this period?

Inputs:

- `metric.time-to-submit-grant-applications` (Time to submit grant applications)

Placements:

- organizational / industries / Non-profit / General (kS5922, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Donation transportation cost efficiency

- id: `kpi.non-profit.donation-transportation-cost-efficiency`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Donation transportation cost efficiency measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Donation transportation cost efficiency, B is whole named by Donation transportation cost efficiency. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Donation transportation cost efficiency on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-donation-transportation-cost-efficiency` (part named by Donation transportation cost efficiency)
- `metric.whole-named-by-donation-transportation-cost-efficiency` (whole named by Donation transportation cost efficiency)

Placements:

- organizational / industries / Non-profit / General (kS372, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Meeting Frequency with volunteers

- id: `kpi.non-profit.meeting-frequency-with-volunteers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Meeting Frequency with volunteers measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Meeting Frequency with volunteers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Meeting Frequency with volunteers on the desired side of its target for this period?

Inputs:

- `metric.meeting-frequency-with-volunteers` (Meeting Frequency with volunteers)

Placements:

- organizational / industries / Non-profit / General (kS5923, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Assessment accuracy

- id: `kpi.non-profit.assessment-accuracy`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Assessment accuracy measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Assessment accuracy, B is whole named by Assessment accuracy. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Assessment accuracy on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-assessment-accuracy` (part named by Assessment accuracy)
- `metric.whole-named-by-assessment-accuracy` (whole named by Assessment accuracy)

Placements:

- organizational / industries / Non-profit / General (kK376, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Governance steering groups

- id: `kpi.non-profit.governance-steering-groups`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Governance steering groups measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Governance steering groups. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Governance steering groups on the desired side of its target for this period?

Inputs:

- `metric.governance-steering-groups` (Governance steering groups)

Placements:

- organizational / industries / Non-profit / General (kS5924, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mentored youth who improved their academic results

- id: `kpi.non-profit.mentored-youth-who-improved-their-academic-results`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mentored youth who improved their academic results measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Mentored youth who improved their academic results, B is whole named by Mentored youth who improved their academic results. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mentored youth who improved their academic results on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-mentored-youth-who-improved-their-academic-results` (part named by Mentored youth who improved their academic results)
- `metric.whole-named-by-mentored-youth-who-improved-their-academic-results` (whole named by Mentored youth who improved their academic results)

Placements:

- organizational / industries / Non-profit / General (kK377, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Partners for reserving campaigns and events

- id: `kpi.non-profit.partners-for-reserving-campaigns-and-events`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Partners for reserving campaigns and events measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Partners for reserving campaigns and events. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Partners for reserving campaigns and events on the desired side of its target for this period?

Inputs:

- `metric.partners-for-reserving-campaigns-and-events` (Partners for reserving campaigns and events)

Placements:

- organizational / industries / Non-profit / General (kS5926, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mentored youth who establish themselves in employment

- id: `kpi.non-profit.mentored-youth-who-establish-themselves-in-employment`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mentored youth who establish themselves in employment measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Mentored youth who establish themselves in employment, B is whole named by Mentored youth who establish themselves in employment. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mentored youth who establish themselves in employment on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-mentored-youth-who-establish-themselves-in-employment` (part named by Mentored youth who establish themselves in employment)
- `metric.whole-named-by-mentored-youth-who-establish-themselves-in-employment` (whole named by Mentored youth who establish themselves in employment)

Placements:

- organizational / industries / Non-profit / General (kS378, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Alumni staff other entry support

- id: `kpi.non-profit.alumni-staff-other-entry-support`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Alumni staff other entry support measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Alumni staff other entry support, B is whole named by Alumni staff other entry support. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Alumni staff other entry support on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-alumni-staff-other-entry-support` (part named by Alumni staff other entry support)
- `metric.whole-named-by-alumni-staff-other-entry-support` (whole named by Alumni staff other entry support)

Placements:

- organizational / industries / Non-profit / General (kS5929, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Improved alliances in the community

- id: `kpi.non-profit.improved-alliances-in-the-community`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Improved alliances in the community measures that result inside Non-profit, subcategory General. The unit is percent. The formula is (A / B) * 100, where A is part named by Improved alliances in the community, B is whole named by Improved alliances in the community. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Improved alliances in the community on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-improved-alliances-in-the-community` (part named by Improved alliances in the community)
- `metric.whole-named-by-improved-alliances-in-the-community` (whole named by Improved alliances in the community)

Placements:

- organizational / industries / Non-profit / General (kS379, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Mechanisms for self-check and complaints

- id: `kpi.non-profit.mechanisms-for-self-check-and-complaints`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Mechanisms for self-check and complaints measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Mechanisms for self-check and complaints. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Mechanisms for self-check and complaints on the desired side of its target for this period?

Inputs:

- `metric.mechanisms-for-self-check-and-complaints` (Mechanisms for self-check and complaints)

Placements:

- organizational / industries / Non-profit / General (kS5931, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Donating per donor

- id: `kpi.non-profit.donating-per-donor`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Donating per donor measures that result inside Non-profit, subcategory General. The unit is currency. The formula is A / B, where A is Donating, B is donor. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Donating per donor on the desired side of its target for this period?

Inputs:

- `metric.donating` (Donating)
- `metric.donor` (donor)

Placements:

- organizational / industries / Non-profit / General (kS653, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Stakeholder groups involved regarding NGO policies

- id: `kpi.non-profit.stakeholder-groups-involved-regarding-ngo-policies`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Stakeholder groups involved regarding NGO policies measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Stakeholder groups involved regarding NGO policies. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Stakeholder groups involved regarding NGO policies on the desired side of its target for this period?

Inputs:

- `metric.stakeholder-groups-involved-regarding-ngo-policies` (Stakeholder groups involved regarding NGO policies)

Placements:

- organizational / industries / Non-profit / General (kS5932, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Cost per dollar raised

- id: `kpi.non-profit.cost-per-dollar-raised`
- kind: kpi
- unit: currency
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Cost per dollar raised measures that result inside Non-profit, subcategory General. The unit is currency. The formula is A / B, where A is Cost, B is dollar raised. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Cost per dollar raised on the desired side of its target for this period?

Inputs:

- `metric.cost` (Cost)
- `metric.dollar-raised` (dollar raised)

Placements:

- organizational / industries / Non-profit / General (kS654, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Funding per individual reached

- id: `kpi.non-profit.funding-per-individual-reached`
- kind: kpi
- unit: currency
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Funding per individual reached measures that result inside Non-profit, subcategory General. The unit is currency. The formula is A / B, where A is Funding, B is individual reached. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Funding per individual reached on the desired side of its target for this period?

Inputs:

- `metric.funding` (Funding)
- `metric.individual-reached` (individual reached)

Placements:

- organizational / industries / Non-profit / General (kS5935, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Volunteers

- id: `kpi.non-profit.volunteers`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Volunteers measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Volunteers. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Volunteers on the desired side of its target for this period?

Inputs:

- `metric.volunteers` (Volunteers)

Placements:

- organizational / industries / Non-profit / General (kS5911, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Volunteers to paid employees ratio

- id: `kpi.non-profit.volunteers-to-paid-employees-ratio`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Volunteers to paid employees ratio measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Volunteers to paid employees ratio. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Volunteers to paid employees ratio on the desired side of its target for this period?

Inputs:

- `metric.volunteers-to-paid-employees-ratio` (Volunteers to paid employees ratio)

Placements:

- organizational / industries / Non-profit / General (kS5913, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Public recognition awards within the community

- id: `kpi.non-profit.public-recognition-awards-within-the-community`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Public recognition awards within the community measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Public recognition awards within the community. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Public recognition awards within the community on the desired side of its target for this period?

Inputs:

- `metric.public-recognition-awards-within-the-community` (Public recognition awards within the community)

Placements:

- organizational / industries / Non-profit / General (kS5938, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sources of revenue

- id: `kpi.non-profit.sources-of-revenue`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sources of revenue measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Sources of revenue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sources of revenue on the desired side of its target for this period?

Inputs:

- `metric.sources-of-revenue` (Sources of revenue)

Placements:

- organizational / industries / Non-profit / General (kS5914, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Philanthropists with non-profit organizations

- id: `kpi.non-profit.philanthropists-with-non-profit-organizations`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Philanthropists with non-profit organizations measures that result inside Non-profit, subcategory General. The unit is count. The formula is A, where A is Philanthropists with non-profit organizations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Philanthropists with non-profit organizations on the desired side of its target for this period?

Inputs:

- `metric.philanthropists-with-non-profit-organizations` (Philanthropists with non-profit organizations)

Placements:

- organizational / industries / Non-profit / General (kS5942, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sponsors per project

- id: `kpi.non-profit.sponsors-per-project`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.non-profit.general`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sponsors per project measures that result inside Non-profit, subcategory General. The unit is count. The formula is A / B, where A is Sponsors, B is project. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sponsors per project on the desired side of its target for this period?

Inputs:

- `metric.sponsors` (Sponsors)
- `metric.project` (project)

Placements:

- organizational / industries / Non-profit / General (kS5916, page_0145)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

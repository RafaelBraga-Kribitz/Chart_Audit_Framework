# Healthcare / Veterinary Medicine

Context: organizational. Group: industries. KPIs: 7.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### Animal sterilizations

- id: `kpi.healthcare.animal-sterilizations`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.organizational-industries`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Animal sterilizations measures that result inside Healthcare, subcategory Organizational » Industries. The unit is count. The formula is A, where A is Animal sterilizations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Animal sterilizations on the desired side of its target for this period?

Inputs:

- `metric.animal-sterilizations` (Animal sterilizations)

Placements:

- organizational / industries / Healthcare / Organizational » Industries (sK4144, page_0104)
- organizational / industries / Healthcare / Veterinary Medicine (KSL144, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Veterinary visits per household

- id: `kpi.healthcare.veterinary-visits-per-household`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.veterinary-medicine`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Veterinary visits per household measures that result inside Healthcare, subcategory Veterinary Medicine. The unit is number. The formula is A / B, where A is Veterinary visits, B is household. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Veterinary visits per household on the desired side of its target for this period?

Inputs:

- `metric.veterinary-visits` (Veterinary visits)
- `metric.household` (household)

Placements:

- organizational / industries / Healthcare / Veterinary Medicine (KFL708, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### S Veterinary expenses per pet household

- id: `kpi.healthcare.s-veterinary-expenses-per-pet-household`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.healthcare.veterinary-medicine`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

S Veterinary expenses per pet household measures that result inside Healthcare, subcategory Veterinary Medicine. The unit is number. The formula is A / B, where A is S Veterinary expenses, B is pet household. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is S Veterinary expenses per pet household on the desired side of its target for this period?

Inputs:

- `metric.s-veterinary-expenses` (S Veterinary expenses)
- `metric.pet-household` (pet household)

Placements:

- organizational / industries / Healthcare / Veterinary Medicine (KFL725, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Household shots own a pet

- id: `kpi.healthcare.household-shots-own-a-pet`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.veterinary-medicine`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Household shots own a pet measures that result inside Healthcare, subcategory Veterinary Medicine. The unit is number. The formula is A, where A is Household shots own a pet. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Household shots own a pet on the desired side of its target for this period?

Inputs:

- `metric.household-shots-own-a-pet` (Household shots own a pet)

Placements:

- organizational / industries / Healthcare / Veterinary Medicine (KFL726, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Compound means pet registered to a veterinarian

- id: `kpi.healthcare.compound-means-pet-registered-to-a-veterinarian`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: average
- dashboard: `dash.healthcare.veterinary-medicine`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Compound means pet registered to a veterinarian measures that result inside Healthcare, subcategory Veterinary Medicine. The unit is number. The formula is A / B, where A is sum underlying Compound means pet registered to a veterinarian, B is count of observations. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Compound means pet registered to a veterinarian on the desired side of its target for this period?

Inputs:

- `metric.sum-underlying-compound-means-pet-registered-to-a-veterinarian` (sum underlying Compound means pet registered to a veterinarian)
- `metric.count-of-observations` (count of observations)

Placements:

- organizational / industries / Healthcare / Veterinary Medicine (KFL727, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Companion pets owned

- id: `kpi.healthcare.companion-pets-owned`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.veterinary-medicine`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

Companion pets owned measures that result inside Healthcare, subcategory Veterinary Medicine. The unit is number. The formula is A, where A is Companion pets owned. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Companion pets owned on the desired side of its target for this period?

Inputs:

- `metric.companion-pets-owned` (Companion pets owned)

Placements:

- organizational / industries / Healthcare / Veterinary Medicine (KFL728, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### \( \dagger \)Resusable medical devices properly decontaminated

- id: `kpi.healthcare.dagger-resusable-medical-devices-properly-decontaminated`
- kind: kpi
- unit: number
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.healthcare.veterinary-medicine`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics, Researcher, R&D
- provenance: authored

\( \dagger \)Resusable medical devices properly decontaminated measures that result inside Healthcare, subcategory Veterinary Medicine. The unit is number. The formula is A, where A is \( \dagger \)Resusable medical devices properly decontaminated. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is \( \dagger \)Resusable medical devices properly decontaminated on the desired side of its target for this period?

Inputs:

- `metric.dagger-resusable-medical-devices-properly-decontaminated` (\( \dagger \)Resusable medical devices properly decontaminated)

Placements:

- organizational / industries / Healthcare / Veterinary Medicine (KSL426, page_0129)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

# Sales and Customer Service / Customer Service

Context: organizational. Group: functional. KPIs: 44.

Each entry is an original definition. The source label is a crosswalk, not the public id.
The analysis chart is for a notebook or a technical review. The communication chart is for a dashboard, report, or story.

### On-time delivery

- id: `kpi.online-presence.on-time-delivery`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.online-presence.ecommerce`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics, Marketing Analytics
- provenance: authored

On-time delivery measures that result inside Online Presence, subcategory eCommerce. The unit is percent. The formula is (A / B) * 100, where A is part named by On-time delivery, B is whole named by On-time delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On-time delivery on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-on-time-delivery` (part named by On-time delivery)
- `metric.whole-named-by-on-time-delivery` (whole named by On-time delivery)

Placements:

- organizational / functional / Online Presence / eCommerce (x810, page_0042)
- organizational / functional / Sales and Customer Service / Customer Service (xK10, page_0049)
- organizational / functional / Management / Logistics / Distribution (sK10, page_0054)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to needs on installation

- id: `kpi.sales-and-customer-service.time-to-needs-on-installation`
- kind: kpi
- unit: number
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to needs on installation measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is number. The formula is A, where A is Time to needs on installation. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to needs on installation on the desired side of its target for this period?

Inputs:

- `metric.time-to-needs-on-installation` (Time to needs on installation)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2335, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Order entry error rate

- id: `kpi.sales-and-customer-service.order-entry-error-rate`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Order entry error rate measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is numerator of Order entry error rate, B is base of Order entry error rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Order entry error rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-order-entry-error-rate` (numerator of Order entry error rate)
- `metric.base-of-order-entry-error-rate` (base of Order entry error rate)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2355, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Service request per customer

- id: `kpi.sales-and-customer-service.service-request-per-customer`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Service request per customer measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is A / B, where A is Service request, B is customer. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Service request per customer on the desired side of its target for this period?

Inputs:

- `metric.service-request` (Service request)
- `metric.customer` (customer)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2356, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Service calls to travel time

- id: `kpi.sales-and-customer-service.service-calls-to-travel-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Service calls to travel time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is Service calls, B is travel time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Service calls to travel time on the desired side of its target for this period?

Inputs:

- `metric.service-calls` (Service calls)
- `metric.travel-time` (travel time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK11, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calls on hold longer than X seconds

- id: `kpi.sales-and-customer-service.calls-on-hold-longer-than-x-seconds`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calls on hold longer than X seconds measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Calls on hold longer than X seconds, B is whole named by Calls on hold longer than X seconds. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calls on hold longer than X seconds on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-calls-on-hold-longer-than-x-seconds` (part named by Calls on hold longer than X seconds)
- `metric.whole-named-by-calls-on-hold-longer-than-x-seconds` (whole named by Calls on hold longer than X seconds)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2357, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer calls answered in the first minute

- id: `kpi.sales-and-customer-service.customer-calls-answered-in-the-first-minute`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer calls answered in the first minute measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer calls answered in the first minute, B is whole named by Customer calls answered in the first minute. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer calls answered in the first minute on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-calls-answered-in-the-first-minute` (part named by Customer calls answered in the first minute)
- `metric.whole-named-by-customer-calls-answered-in-the-first-minute` (whole named by Customer calls answered in the first minute)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK12, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complaints not resolved in first call

- id: `kpi.sales-and-customer-service.complaints-not-resolved-in-first-call`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complaints not resolved in first call measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Complaints not resolved in first call, B is whole named by Complaints not resolved in first call. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complaints not resolved in first call on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-complaints-not-resolved-in-first-call` (part named by Complaints not resolved in first call)
- `metric.whole-named-by-complaints-not-resolved-in-first-call` (whole named by Complaints not resolved in first call)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2358, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Completion to billings

- id: `kpi.sales-and-customer-service.completion-to-billings`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Completion to billings measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Completion to billings. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Completion to billings on the desired side of its target for this period?

Inputs:

- `metric.completion-to-billings` (Completion to billings)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK16, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complaint not responded time

- id: `kpi.sales-and-customer-service.complaint-not-responded-time`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complaint not responded time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Complaint not responded time, B is whole named by Complaint not responded time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complaint not responded time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-complaint-not-responded-time` (part named by Complaint not responded time)
- `metric.whole-named-by-complaint-not-responded-time` (whole named by Complaint not responded time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2359, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Call handling rate

- id: `kpi.sales-and-customer-service.call-handling-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Call handling rate measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is numerator of Call handling rate, B is base of Call handling rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Call handling rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-call-handling-rate` (numerator of Call handling rate)
- `metric.base-of-call-handling-rate` (base of Call handling rate)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK16, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Credit request processing time

- id: `kpi.sales-and-customer-service.credit-request-processing-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Credit request processing time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Credit request processing time, B is whole named by Credit request processing time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Credit request processing time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-credit-request-processing-time` (part named by Credit request processing time)
- `metric.whole-named-by-credit-request-processing-time` (whole named by Credit request processing time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2360, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Call abandon rate

- id: `kpi.sales-and-customer-service.call-abandon-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Call abandon rate measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is numerator of Call abandon rate, B is base of Call abandon rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Call abandon rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-call-abandon-rate` (numerator of Call abandon rate)
- `metric.base-of-call-abandon-rate` (base of Call abandon rate)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK168, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complete and on time delivery

- id: `kpi.sales-and-customer-service.complete-and-on-time-delivery`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complete and on time delivery measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Complete and on time delivery, B is whole named by Complete and on time delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complete and on time delivery on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-complete-and-on-time-delivery` (part named by Complete and on time delivery)
- `metric.whole-named-by-complete-and-on-time-delivery` (whole named by Complete and on time delivery)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2362, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Unique received calls

- id: `kpi.sales-and-customer-service.unique-received-calls`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Unique received calls measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Unique received calls, B is whole named by Unique received calls. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Unique received calls on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-unique-received-calls` (part named by Unique received calls)
- `metric.whole-named-by-unique-received-calls` (whole named by Unique received calls)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK292, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Service request outstanding

- id: `kpi.sales-and-customer-service.service-request-outstanding`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Service request outstanding measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Service request outstanding, B is whole named by Service request outstanding. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Service request outstanding on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-service-request-outstanding` (part named by Service request outstanding)
- `metric.whole-named-by-service-request-outstanding` (whole named by Service request outstanding)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2363, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Response time to business partner request

- id: `kpi.sales-and-customer-service.response-time-to-business-partner-request`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Response time to business partner request measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Response time to business partner request. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Response time to business partner request on the desired side of its target for this period?

Inputs:

- `metric.response-time-to-business-partner-request` (Response time to business partner request)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK380, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Sale invoices issued on time

- id: `kpi.sales-and-customer-service.sale-invoices-issued-on-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Sale invoices issued on time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Sale invoices issued on time, B is whole named by Sale invoices issued on time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Sale invoices issued on time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-sale-invoices-issued-on-time` (part named by Sale invoices issued on time)
- `metric.whole-named-by-sale-invoices-issued-on-time` (whole named by Sale invoices issued on time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2365, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Report submitted on-time

- id: `kpi.sales-and-customer-service.report-submitted-on-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Report submitted on-time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Report submitted on-time, B is whole named by Report submitted on-time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Report submitted on-time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-report-submitted-on-time` (part named by Report submitted on-time)
- `metric.whole-named-by-report-submitted-on-time` (whole named by Report submitted on-time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK383, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Resolution of queries the same day

- id: `kpi.sales-and-customer-service.resolution-of-queries-the-same-day`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Resolution of queries the same day measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is Resolution, B is queries the same day. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Resolution of queries the same day on the desired side of its target for this period?

Inputs:

- `metric.resolution` (Resolution)
- `metric.queries-the-same-day` (queries the same day)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2366, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Timeliness of issues resolution

- id: `kpi.sales-and-customer-service.timeliness-of-issues-resolution`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Timeliness of issues resolution measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is Timeliness, B is issues resolution. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Timeliness of issues resolution on the desired side of its target for this period?

Inputs:

- `metric.timeliness` (Timeliness)
- `metric.issues-resolution` (issues resolution)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK384, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Orders processed

- id: `kpi.sales-and-customer-service.orders-processed`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Orders processed measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Orders processed, B is whole named by Orders processed. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Orders processed on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-orders-processed` (part named by Orders processed)
- `metric.whole-named-by-orders-processed` (whole named by Orders processed)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2367, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time to rectify defects

- id: `kpi.sales-and-customer-service.time-to-rectify-defects`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time to rectify defects measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Time to rectify defects. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time to rectify defects on the desired side of its target for this period?

Inputs:

- `metric.time-to-rectify-defects` (Time to rectify defects)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK433, page_0049)
- organizational / industries / Construction / General (sK433, page_0068)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Correspondence replied on to time

- id: `kpi.sales-and-customer-service.correspondence-replied-on-to-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Correspondence replied on to time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is Correspondence replied on, B is time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Correspondence replied on to time on the desired side of its target for this period?

Inputs:

- `metric.correspondence-replied-on` (Correspondence replied on)
- `metric.time` (time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2370, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Work orders closed within the specified time period

- id: `kpi.sales-and-customer-service.work-orders-closed-within-the-specified-time-period`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Work orders closed within the specified time period measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Work orders closed within the specified time period, B is whole named by Work orders closed within the specified time period. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Work orders closed within the specified time period on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-work-orders-closed-within-the-specified-time-period` (part named by Work orders closed within the specified time period)
- `metric.whole-named-by-work-orders-closed-within-the-specified-time-period` (whole named by Work orders closed within the specified time period)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR598, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Time taken on order to delivery

- id: `kpi.sales-and-customer-service.time-taken-on-order-to-delivery`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Time taken on order to delivery measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Time taken on order to delivery. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Time taken on order to delivery on the desired side of its target for this period?

Inputs:

- `metric.time-taken-on-order-to-delivery` (Time taken on order to delivery)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2371, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer complaints due to poor service or product quality

- id: `kpi.sales-and-customer-service.customer-complaints-due-to-poor-service-or-product-quality`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer complaints due to poor service or product quality measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is Customer complaints due, B is poor service or product quality. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer complaints due to poor service or product quality on the desired side of its target for this period?

Inputs:

- `metric.customer-complaints-due` (Customer complaints due)
- `metric.poor-service-or-product-quality` (poor service or product quality)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK621, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Longest call hold

- id: `kpi.sales-and-customer-service.longest-call-hold`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Longest call hold measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Longest call hold. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Longest call hold on the desired side of its target for this period?

Inputs:

- `metric.longest-call-hold` (Longest call hold)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2372, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pick-to-ship cycle time for customer orders

- id: `kpi.sales-and-customer-service.pick-to-ship-cycle-time-for-customer-orders`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pick-to-ship cycle time for customer orders measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Pick-to-ship cycle time for customer orders. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pick-to-ship cycle time for customer orders on the desired side of its target for this period?

Inputs:

- `metric.pick-to-ship-cycle-time-for-customer-orders` (Pick-to-ship cycle time for customer orders)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK701, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Longest delay in queue

- id: `kpi.sales-and-customer-service.longest-delay-in-queue`
- kind: kpi
- unit: count
- direction: up
- timing: leading
- level: operational
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Longest delay in queue measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Longest delay in queue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Longest delay in queue on the desired side of its target for this period?

Inputs:

- `metric.longest-delay-in-queue` (Longest delay in queue)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2373, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complaints received

- id: `kpi.sales-and-customer-service.complaints-received`
- kind: kri
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complaints received measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Complaints received. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complaints received on the desired side of its target for this period?

Inputs:

- `metric.complaints-received` (Complaints received)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK751, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Pay issue

- id: `kpi.sales-and-customer-service.pay-issue`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Pay issue measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Pay issue. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Pay issue on the desired side of its target for this period?

Inputs:

- `metric.pay-issue` (Pay issue)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2374, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Overdue service requests

- id: `kpi.sales-and-customer-service.overdue-service-requests`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Overdue service requests measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Overdue service requests, B is whole named by Overdue service requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Overdue service requests on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-overdue-service-requests` (part named by Overdue service requests)
- `metric.whole-named-by-overdue-service-requests` (whole named by Overdue service requests)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK1001, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### On-hold time

- id: `kpi.sales-and-customer-service.on-hold-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

On-hold time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is On-hold time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is On-hold time on the desired side of its target for this period?

Inputs:

- `metric.on-hold-time` (On-hold time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2375, page_0049)
- organizational / industries / Sport / specific operations. (xK2375, page_0179)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Call transfer rate

- id: `kpi.sales-and-customer-service.call-transfer-rate`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Call transfer rate measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is numerator of Call transfer rate, B is base of Call transfer rate. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Call transfer rate on the desired side of its target for this period?

Inputs:

- `metric.numerator-of-call-transfer-rate` (numerator of Call transfer rate)
- `metric.base-of-call-transfer-rate` (base of Call transfer rate)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK1017, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Complaints resolved

- id: `kpi.sales-and-customer-service.complaints-resolved`
- kind: kri
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Complaints resolved measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Complaints resolved, B is whole named by Complaints resolved. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Complaints resolved on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-complaints-resolved` (part named by Complaints resolved)
- `metric.whole-named-by-complaints-resolved` (whole named by Complaints resolved)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2376, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Service requests per agent

- id: `kpi.sales-and-customer-service.service-requests-per-agent`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A / B`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `horizontal-bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Service requests per agent measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A / B, where A is Service requests, B is agent. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Service requests per agent on the desired side of its target for this period?

Inputs:

- `metric.service-requests` (Service requests)
- `metric.agent` (agent)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK1079, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Talk time

- id: `kpi.sales-and-customer-service.talk-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Talk time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Talk time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Talk time on the desired side of its target for this period?

Inputs:

- `metric.talk-time` (Talk time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2377, page_0049)
- organizational / industries / Sport / specific operations. (xK2378, page_0179)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### After call work time

- id: `kpi.sales-and-customer-service.after-call-work-time`
- kind: kpi
- unit: count
- direction: down
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

After call work time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is After call work time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is After call work time on the desired side of its target for this period?

Inputs:

- `metric.after-call-work-time` (After call work time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK1081, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Customer satisfaction with service levels

- id: `kpi.sales-and-customer-service.customer-satisfaction-with-service-levels`
- kind: kpi
- unit: percent
- direction: up
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Customer satisfaction with service levels measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Customer satisfaction with service levels, B is whole named by Customer satisfaction with service levels. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Customer satisfaction with service levels on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-customer-satisfaction-with-service-levels` (part named by Customer satisfaction with service levels)
- `metric.whole-named-by-customer-satisfaction-with-service-levels` (whole named by Customer satisfaction with service levels)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2380, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Speed of answer (5A)

- id: `kpi.sales-and-customer-service.speed-of-answer-5a`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Speed of answer (5A) measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Speed of answer (5A). Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Speed of answer (5A) on the desired side of its target for this period?

Inputs:

- `metric.speed-of-answer-5a` (Speed of answer (5A))

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK1133, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Wright answers or advice the first time

- id: `kpi.sales-and-customer-service.wright-answers-or-advice-the-first-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Wright answers or advice the first time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Wright answers or advice the first time, B is whole named by Wright answers or advice the first time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Wright answers or advice the first time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-wright-answers-or-advice-the-first-time` (part named by Wright answers or advice the first time)
- `metric.whole-named-by-wright-answers-or-advice-the-first-time` (whole named by Wright answers or advice the first time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2381, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Calls answered within service level time

- id: `kpi.sales-and-customer-service.calls-answered-within-service-level-time`
- kind: kpi
- unit: percent
- direction: down
- timing: lagging
- level: tactical
- formula: `(A / B) * 100`
- formula type: ratio
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `diverging-bar` (notebook)
- communication chart: `bullet-graph` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Calls answered within service level time measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is percent. The formula is (A / B) * 100, where A is part named by Calls answered within service level time, B is whole named by Calls answered within service level time. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Calls answered within service level time on the desired side of its target for this period?

Inputs:

- `metric.part-named-by-calls-answered-within-service-level-time` (part named by Calls answered within service level time)
- `metric.whole-named-by-calls-answered-within-service-level-time` (whole named by Calls answered within service level time)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xK1134, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

### Support requests

- id: `kpi.sales-and-customer-service.support-requests`
- kind: kpi
- unit: count
- direction: up
- timing: lagging
- level: tactical
- formula: `A`
- formula type: count
- dashboard: `dash.sales-and-customer-service.customer-service`
- analysis chart: `bar-chart` (notebook)
- communication chart: `bar-chart` (dashboard)
- audiences: Executive, Data Analytics
- provenance: authored

Support requests measures that result inside Sales and Customer Service, subcategory Customer Service. The unit is count. The formula is A, where A is Support requests. Read it against a target, a prior period, or a corridor, and do not treat a move as success unless the definition of each input stayed fixed.

Questions: Is Support requests on the desired side of its target for this period?

Inputs:

- `metric.support-requests` (Support requests)

Placements:

- organizational / functional / Sales and Customer Service / Customer Service (xR2382, page_0049)

Target notes:

- None.

Pitfall: Do not change an input's definition mid-series. Do not brief an executive with the analysis chart if a simpler comparison chart answers the decision.

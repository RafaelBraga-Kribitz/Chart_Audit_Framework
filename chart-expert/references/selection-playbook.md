# Selection playbook

Load this file when the question is what to measure, what to show, or how a dashboard, report, or story should be built. Load `references/chart-library-index.md` only after the measure and the question are known. Chart retrieval stays deterministic: the same data shape and the same analytical function return the same top candidates.

## Walk

1. **Audience and surface.** Name who will read the result and where it will live. Audiences include Executive, Public, HR, Marketing Analytics, Data Analytics, Data Scientist, Researcher, R&D, and Development. Surfaces include a Jupyter notebook, a pandas or matplotlib plot, a dashboard, a report, and a story. An executive or client surface uses a basic comparison and refuses gauges, pies, and radar as the message. A research or data-science surface may use the advanced chart the question actually needs. When both exist, pick an analysis chart and a communication chart. Do not collapse the library to the executive set.
2. **Question.** Write the decision as a question. "Are we on pace?" is different from "Where did the money go?" and from "Which segment is different?"
3. **OMTM.** Open `library/OMTM/` for the business model. If the work is a single bet inside a function, the OMTM may be one KPI from that function instead of the company card.
4. **Objective and key results.** Open `library/OKRS/` for the function, the category, and the context (`internal`, `project`, or `client`). Keep one to three key results. Reject lines that are tasks.
5. **KPIs and KRIs.** Each key result cites a KPI id. Open the subcategory page under `library/KPIS/` or filter `library/KPIS/_catalog/kpis.jsonl`. Separate KRIs (risk) from KPIs (success). Keep at least one leading indicator if the decision is about what to do next.
6. **Metrics and sub-metrics.** Read the formula. Every input id must exist under `library/METRICS/`. If an input is missing, the KPI is not ready to report.
7. **Chart.** Classify the data shape with `references/input-type-schema.md`. Filter `library/_INDICES/` by input type, then by analytical function, then by audience and cardinality. For an executive or client surface, skip `ibcs_status: avoid`. For a notebook or a technical review, those charts remain eligible. Return the top three for the surface you are filling, with the tradeoff and the failure modes. If the analysis chart and the communication chart differ, return both.
8. **Surface.** A dashboard is optional. Open `library/DASHBOARDS/` when the surface is a dashboard: zones are score, trend, breakdown, variance, detail. A `placeholder` still has suggested zones, chart ids, audiences, and data sources. If a Databox or Zebra template is linked, it is a communication layout, not the analytical view. When the surface is a notebook or a plot, point at the chart card's implementation notes and skip the dashboard grid.
9. **Report.** Open `library/REPORTS/` for the meeting the dashboard serves (board, monthly review, variance, client, pipeline, operations, personal).
10. **Story.** Open `library/STORIES/` for the job (single message, comparison, pace, diagnostic, part-to-whole, change, distribution, flow). Apply the failure rules (red and green as the only signal, pies, dead-end filters, impersonal scope).
11. **Format.** Apply `library/STANDARDS/ibcs-success.md`: one term per measure, comparable scales, a message title, no decorative chart types.

## Worked path

Communication surface, audience agency principal (`Executive`). Question: are client projects earning the gross profit we planned? OMTM: `library/OMTM/agency.md`. Objective: deliver projects inside the estimated hours and cost (`context: project`). Key results cite estimated-versus-actual hours, estimated-versus-actual cost, and project contribution margin. Those KPIs cite hours, cost, revenue, and direct cost as metrics. Communication charts: a bullet or variance bar for the score, a waterfall for the bridge from estimate to actual, a table for the project list. Dashboard: the project-delivery subcategory card. Report: client or monthly business review. Story: diagnostic. Format: IBCS variance notation, actual versus plan, no gauge.

Analysis surface, audience data analyst or operations analyst. Same KPIs. The notebook can show the distribution of hour variance, a scatter of estimated versus actual, and the project-level tail. Those plots are not pasted onto the principal's page. The principal gets the variance bar and the few projects that explain the gap.

## What to open

| Need | File |
|---|---|
| Word meanings | `library/ONTOLOGY.md` |
| Why measurement works or fails | `library/THEORY/` |
| Notation | `library/STANDARDS/ibcs-success.md` |
| Chart lookup | `references/chart-library-index.md` and `library/_INDICES/` |
| KPI lookup | `library/KPIS/_catalog/kpis.jsonl` and subcategory pages |
| Coverage gaps | `library/KPIS/_inventory/exceptions.md` |
| Existing scraped templates | `library/DASHBOARDS/vault-index.md` |

## Determinism

Do not invent a chart that the index does not list. Do not invent a KPI id. If the inventory exceptions file still lists a name, say it is unresolved rather than guessing a formula. If two charts tie, rank by the rules in `references/retrieval-dimensions.md`: exact input type, exact function, audience fit, cardinality, then fewer failure modes.

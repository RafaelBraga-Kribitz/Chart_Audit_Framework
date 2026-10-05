# Selection playbook

Load this file when the question is what to measure, what to show, or how a dashboard, report, or story should be built. Load `references/chart-library-index.md` only after the measure and the question are known. Chart retrieval stays deterministic: the same data shape and the same analytical function return the same top candidates.

## Walk

1. **Audience and surface.** Name who will read the result and where it will live. Use the reader roles in `library/ONTOLOGY.md` (Executive, Client, HR business partner, Marketing lead, Marketing analytics, Data analytics, Data scientist, Researcher, R&D, Development, Public); each maps to one chart-audience tolerance in `references/retrieval-dimensions.md`. Surfaces are analysis (Jupyter notebook, pandas or matplotlib plot, exploratory dashboard) or communication (dashboard, report, story). An executive, client, or public communication surface uses a basic comparison and refuses gauges, pies, and radar as the message. A research or data-science analysis surface may use the advanced chart the question actually needs. When both exist, pick an analysis chart and a communication chart. Do not collapse the library to the executive set.
2. **Question.** Write the decision as a question. "Are we on pace?" is different from "Where did the money go?" and from "Which segment is different?"
3. **OMTM.** Open `library/OMTM/` for the business model (agency, SaaS, ecommerce, marketplace, professional services). If the work is a single bet inside a function, the OMTM may be one KPI from that function instead of the company card.
4. **Objective and key results.** Model the objective on `library/OKRS/note/`, which carries `context: internal`, `project`, or `client`. Keep two to five key results, usually three. Each one cites a KPI id, a target, and a cadence; the direction comes from the KPI. Reject lines that are tasks.
5. **KPIs and KRIs.** Look the measure up in `library/KPIS/index.md` or filter `library/KPIS/_catalog/kpis.jsonl`. Separate KRIs (`measure_kind: kri`, listed in `library/KRIS/index.md`) from KPIs. Keep at least one leading indicator if the decision is about what to do next. If the measure is not in the library, write its card with the fields in `library/ONTOLOGY.md` (definition, unit, formula, inputs, direction, timing, charts) instead of citing an id that does not exist.
6. **Metrics and sub-metrics.** Read the formula. Every input id must exist in `library/KPIS/_catalog/metrics.jsonl`, where `used_by` lists the KPIs that share it. A KPI whose only input is the KPI itself has no formula yet and is not ready to report.
7. **Chart.** Classify the data shape with `references/input-type-schema.md`. Filter `library/_INDICES/` by input type, then by analytical function, then by audience and cardinality. On an executive, public, or client communication surface, skip `ibcs_status: avoid`; on a notebook or a technical review those charts remain eligible. Return the top three for the surface you are filling, with the tradeoff and the failure modes. If the analysis chart and the communication chart differ, return both.
8. **Surface.** A dashboard is optional. When the surface is a dashboard, open the specification under `library/DASHBOARDS/<function>/<area>.md`: zones are score, trend, breakdown, variance, detail. A Databox or Zebra template is a communication layout, not the analytical view. When the surface is a notebook or a plot, point at the chart card's implementation notes and skip the dashboard grid. `library/DASHBOARDS/patterns/` holds scenario rules (pace to goal, now versus then, no dead end).
9. **Report.** Open `library/REPORTS/` for the meeting the dashboard serves (board pack, monthly business review, variance report, scorecard, client report, operational review, pipeline review, personal review).
10. **Story.** Open `library/STORIES/` for the job (single message, comparison, pace, diagnostic, part-to-whole, change, distribution, flow). Apply the failure rules (red and green as the only signal, time not on an axis, dead-end filters, impersonal scope).
11. **Format.** Apply `library/STANDARDS/ibcs-success.md`: one term per measure, comparable scales, a message title, no decorative chart types.

## Worked path

Communication surface, reader an agency principal (role `Executive`). Question: are client projects earning the margin we quoted?

- OMTM: `library/OMTM/agency.md` → `kpi.portfolio-and-project-management.project-contribution-margin`.
- Objective: `okr.note.agency-delivery`, "Deliver projects inside the hours and cost we quoted" (`context: project`).
- Key results cite three KPIs:
  - `kpi.portfolio-and-project-management.estimated-versus-actual-project-time` (estimated hours / actual hours, corridor)
  - `kpi.portfolio-and-project-management.estimated-versus-actual-project-cost` (estimated cost / actual cost, corridor)
  - `kpi.portfolio-and-project-management.project-contribution-margin` ((project revenue − direct cost) / project revenue)
- Their inputs are metrics: estimated hours, actual hours, estimated cost, actual cost, project revenue, direct cost.
- Communication charts: `bullet-graph` for each score against its band, `waterfall-chart` for the bridge from quoted to delivered margin, `data-table` for the project list.
- Dashboard: `dash.portfolio-and-project-management.delivery` (`library/DASHBOARDS/portfolio-and-project-management/delivery.md`).
- Report: `library/REPORTS/client-report.md` or `monthly-business-review.md`. Story: `library/STORIES/diagnostic.md`.
- Format: IBCS variance notation, actual versus plan, no gauge.

Analysis surface, reader a data analyst (role `Data analytics`). Same KPIs. The notebook shows a `histogram` of hour variance across projects, a `scatter-plot` of estimated versus actual hours, and the project-level tail. Those plots are not pasted onto the principal's page. The principal gets the bullet graphs and the few projects that explain the gap.

## What to open

| Need | File |
|---|---|
| Word meanings | `library/ONTOLOGY.md` |
| Why measurement works or fails | `library/THEORY/` |
| Notation | `library/STANDARDS/ibcs-success.md` |
| Chart lookup | `references/chart-library-index.md` and `library/_INDICES/` |
| KPI lookup | `library/KPIS/index.md` and `library/KPIS/_catalog/kpis.jsonl` |
| Metric lookup | `library/KPIS/_catalog/metrics.jsonl` |
| Dashboard specifications | `library/DASHBOARDS/index.md` |

The KPI, OKR, OMTM, and dashboard files are generated by `scripts/build_measures.py`; the chart indices by `scripts/build_charts.py`. Edit the script, not the output.

## Determinism

Do not invent a chart that the index does not list. Do not invent a KPI id. If the measure is not in the library, say so and write the card rather than guessing an id. If two charts tie, rank by the Retrieval Priority Rules in `references/retrieval-dimensions.md` in order (input type, function, audience fit, cardinality, tool support, failure-mode count), then by chart file name, ascending.

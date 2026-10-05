---
name: Bar Chart
category: Comparison
input_type: [cat-value, cat-multi-value]
it_variants: [IT026, IT005, IT029, IT031]
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position, length, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [D, J]
alternatives: [horizontal-bar-chart, lollipop-chart, dot-plot, column-range]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: verified, source_file: "chart-expert/library/_SNIPPETS/bar-chart_matplotlib.py", last_iterated: 2026-07-09}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: magnitude
ibcs_status: preferred
questions: ["Which category is larger, and by how much?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: [kpi.finance.budgets-reviewed, kpi.finance.monthly-recurring-profit, kpi.finance.net-profit, kpi.finance.net-revenue-minus-cac, kpi.finance.operating-cash-flow, kpi.finance.revenue-per-employee, kpi.human-resources.account-executives-hired, kpi.human-resources.employee-pulse-score, kpi.human-resources.sales-development-hires, kpi.human-resources.sdrs-trained, kpi.human-resources.town-hall-held, kpi.information-technology.critical-defects, kpi.information-technology.regressions, kpi.information-technology.restore-tests-passed, kpi.management.usability-score, kpi.marketing-and-communications.analyst-briefings, kpi.marketing-and-communications.analyst-webinars, kpi.marketing-and-communications.blog-posts-published, kpi.marketing-and-communications.blog-subscribers, kpi.marketing-and-communications.community-page-visits, kpi.marketing-and-communications.cost-per-lead, kpi.marketing-and-communications.customer-acquisition-cost, kpi.marketing-and-communications.expert-interviews, kpi.marketing-and-communications.experts-contacted, kpi.marketing-and-communications.influencer-meetings, kpi.marketing-and-communications.marketing-qualified-leads, kpi.marketing-and-communications.media-meetings, kpi.marketing-and-communications.newsletters-published, kpi.marketing-and-communications.product-pages-shipped, kpi.marketing-and-communications.sales-enablement-assets, kpi.marketing-and-communications.speaking-slots, kpi.marketing-and-communications.wins-by-lead-source, kpi.online-presence.pages-meeting-speed-budget, kpi.online-presence.referring-domains, kpi.online-presence.website-visitors, kpi.professional-services.gross-profit-per-head, kpi.sales-and-customer-service.average-deal-size, kpi.sales-and-customer-service.coaching-sessions, kpi.sales-and-customer-service.customer-interviews, kpi.sales-and-customer-service.expansion-revenue, kpi.sales-and-customer-service.new-accounts, kpi.sales-and-customer-service.partner-events, kpi.sales-and-customer-service.partner-webinars, kpi.sales-and-customer-service.partner-whitepapers, kpi.sales-and-customer-service.pipeline-created, kpi.sales-and-customer-service.product-demos, kpi.sales-and-customer-service.resellers-onboarded, kpi.sales-and-customer-service.revenue, kpi.sales-and-customer-service.sales-qualified-leads]
analysis_surface: plot
communication_surface: dashboard
---

# Bar Chart

## Description
A bar chart (vertical orientation, also called a column chart) represents categorical data with rectangular bars whose heights are proportional to the values they represent. Each bar corresponds to a category on the x-axis, and the y-axis encodes the quantitative value. It is the most fundamental and widely understood chart type for comparing discrete quantities across categories.

## When to Use
- Comparing a single quantitative value across a set of discrete categories
- Showing rankings or relative magnitudes when time is not the primary axis
- Displaying counts, totals, or averages for a categorical breakdown
- When the audience needs to precisely compare values using bar length

## When NOT to Use
- Category labels are long (use a horizontal bar chart to give labels space)
- More than ~15–20 categories (bars become too narrow; consider a dot plot or table)
- The variable on y-axis is continuous and ordered (use a histogram or line chart)
- Part-to-whole is the message (use a stacked or 100% bar chart)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | The groups being compared; x-axis |
| value | numeric | The measured quantity; y-axis |
| color_group (optional) | categorical | Only use if a secondary grouping is needed |

## Best Practices
- Always start the y-axis at zero — truncation makes length comparisons misleading
- Sort bars by value (descending or ascending) unless category order is intrinsically meaningful — see Smell D
- Use a single consistent color unless color encodes a meaningful distinction
- Add value labels directly on or above bars for precise reading
- Limit to ~12 bars before switching to horizontal orientation or a table

## Common Mistakes
- Not starting the y-axis at zero, exaggerating apparent differences
- Leaving bars in arbitrary/alphabetical order instead of sorting by value — see Smell D
- Silently omitting categories with zero or near-zero values — see Smell J
- Using 3D bars, which distort length perception

## Dashboard and other surfaces

status: placeholder

Bar Chart can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `horizontal-bar-chart`, `lollipop-chart`, `dot-plot`.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib

Verified 2026-07-09 — runnable snippet:
`chart-expert/library/_SNIPPETS/bar-chart_matplotlib.py` (inline fixture,
zero baseline, value-sorted categories, direct bar labels via `ax.bar_label`,
top/right spines hidden, Agg backend, non-empty PNG asserted). Core pattern:

```python
bars = ax.bar(cats_sorted, vals_sorted, color="#4477AA")
ax.bar_label(bars, padding=2)      # direct labels beat a legend for one series
ax.set_ylim(0, max(vals_sorted) * 1.15)  # zero baseline
ax.spines[["top", "right"]].set_visible(False)
```

### plotly
`px.bar(df, x='category', y='value', color='color_group')` or `go.Bar`.

### altair
`alt.Chart(df).mark_bar().encode(x=alt.X('category:N', sort='-y'), y='value:Q')`

### excel / tableau
Excel: Insert > Column Chart. Tableau: Drag measure to Rows, dimension to Columns; Marks card = Bar.

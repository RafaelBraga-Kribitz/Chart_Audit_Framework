---
name: Line Chart
category: Temporal
input_type: [time-series, xy-simple]
it_variants: [IT018, IT001, IT034]
analytical_function: Trend-over-time
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Executive, Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [L, B]
alternatives: [area-chart, sparkline, slope-chart, stepped-line-graph]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: change-over-time
ibcs_status: preferred
questions: ["How has the series changed over time?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: [kpi.finance.budgets-reviewed, kpi.finance.days-sales-outstanding, kpi.finance.days-to-close, kpi.finance.monthly-recurring-profit, kpi.finance.net-profit, kpi.finance.net-revenue-minus-cac, kpi.finance.operating-cash-flow, kpi.finance.revenue-per-employee, kpi.human-resources.account-executives-hired, kpi.human-resources.sales-development-hires, kpi.human-resources.sdrs-trained, kpi.human-resources.town-hall-held, kpi.information-technology.restore-tests-passed, kpi.marketing-and-communications.analyst-briefings, kpi.marketing-and-communications.analyst-webinars, kpi.marketing-and-communications.blog-posts-published, kpi.marketing-and-communications.blog-subscribers, kpi.marketing-and-communications.community-page-visits, kpi.marketing-and-communications.cost-per-lead, kpi.marketing-and-communications.customer-acquisition-cost, kpi.marketing-and-communications.expert-interviews, kpi.marketing-and-communications.experts-contacted, kpi.marketing-and-communications.influencer-meetings, kpi.marketing-and-communications.marketing-qualified-leads, kpi.marketing-and-communications.media-meetings, kpi.marketing-and-communications.newsletters-published, kpi.marketing-and-communications.product-pages-shipped, kpi.marketing-and-communications.sales-enablement-assets, kpi.marketing-and-communications.speaking-slots, kpi.online-presence.pages-meeting-speed-budget, kpi.online-presence.referring-domains, kpi.online-presence.website-visitors, kpi.portfolio-and-project-management.lead-time-per-project, kpi.professional-services.client-breakeven, kpi.professional-services.gross-profit-per-head, kpi.sales-and-customer-service.average-deal-size, kpi.sales-and-customer-service.coaching-sessions, kpi.sales-and-customer-service.customer-churn-rate, kpi.sales-and-customer-service.customer-interviews, kpi.sales-and-customer-service.expansion-revenue, kpi.sales-and-customer-service.first-response-time, kpi.sales-and-customer-service.monthly-recurring-revenue, kpi.sales-and-customer-service.new-accounts, kpi.sales-and-customer-service.partner-events, kpi.sales-and-customer-service.partner-webinars, kpi.sales-and-customer-service.partner-whitepapers, kpi.sales-and-customer-service.pipeline-created, kpi.sales-and-customer-service.product-demos, kpi.sales-and-customer-service.resellers-onboarded, kpi.sales-and-customer-service.resolution-time, kpi.sales-and-customer-service.revenue, kpi.sales-and-customer-service.sales-qualified-leads]
analysis_surface: plot
communication_surface: dashboard
---

# Line Chart

## Description
A line chart displays quantitative values over a continuous interval or time period by connecting data points with straight line segments. The x-axis typically encodes time or an ordered sequence, while the y-axis encodes the measured value. Multiple series can be overlaid using distinct colors to enable direct comparison of trends.

## When to Use
- Showing how a metric changes over time (revenue, temperature, user counts)
- Comparing the trajectory of multiple series across the same time period
- Identifying trends, cycles, and turning points in sequential data
- Communicating rate of change between periods

## When NOT to Use
- Data has fewer than 3 time points (use a bar chart or slope chart instead)
- Values represent discrete, unordered categories
- You need to show part-to-whole relationships (use stacked area or pie)
- The lines cross so frequently they become illegible (limit to ~5-7 series)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Must be sorted ascending |
| value | numeric | The measured quantity |
| series (optional) | categorical | Used to differentiate multiple lines |

## Best Practices
- Start the y-axis at zero only when the baseline is meaningful; truncating can be appropriate for showing variance
- Use consistent time intervals on the x-axis to avoid visual distortion
- Label lines directly at their endpoints rather than relying solely on a legend
- Limit to 5-7 lines before considering small multiples
- Use a dashed or lighter style for projected/forecast portions — see Smell A

## Common Mistakes
- Interpolating over long gaps in data as if values are known — see Smell L
- Showing a flat line on a zero-variance metric as if it is informative — see Smell B
- Encoding rank changes with a line chart when a bump chart is clearer
- Using a line chart for nominal categorical x-axis data

## Dashboard and other surfaces

status: placeholder

Line Chart can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with `area-chart`, `sparkline`, `slope-chart`.

Suggested communication placement: **trend** zone. Coarse template type, when a Databox or Zebra template is the layout: **Line**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(df['date'], df['value'], color='steelblue', linewidth=1.5)
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Metric Over Time')
plt.tight_layout()
```

### plotly
Use `px.line(df, x='date', y='value', color='series')` or `go.Scatter(mode='lines')`.

### altair
`alt.Chart(df).mark_line().encode(x='date:T', y='value:Q', color='series:N')`

### excel / tableau
Excel: Insert > Line Chart. Tableau: drag date to Columns, measure to Rows; Marks card set to Line.

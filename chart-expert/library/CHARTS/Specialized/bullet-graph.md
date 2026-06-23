---
name: Bullet Graph
category: Specialized
input_type: [cat-value, interval-range]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [length, position, color-value]
tool_support: [matplotlib, plotly, d3, tableau, powerbi]
failure_modes: [B]
alternatives: [angular-gauge, lollipop-chart, bar-chart]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---
# Bullet Graph

## Description
Designed by Stephen Few as a compact replacement for dashboard gauges and meters, a Bullet Graph shows a primary measure (a solid bar), a comparative target or benchmark (a short perpendicular line), and performance range bands (Poor/Satisfactory/Good) as shaded background segments. All this information is packed into a single linear bar without wasted space. It answers the question "how is this metric performing against its target and acceptable ranges?" at a glance.

## When to Use
- KPI and dashboard performance reporting where actual vs. target comparison is the primary message
- Replacing dial/speedometer gauges with a space-efficient linear alternative
- Showing multiple KPIs in a small space using stacked bullet graphs

## When NOT to Use
- When performance ranges (Poor/Good) are not meaningful or definable
- When comparison between many metrics requires equal-scale alignment (use a bar chart)
- When the audience is not familiar with the chart format and cannot be briefed (gauge may be more intuitive)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| metric | string | KPI or metric name |
| actual | numeric | The primary measure (the filled bar) |
| target | numeric | The comparative reference mark |
| poor_max | numeric | Upper bound of "Poor" range |
| satisfactory_max | numeric | Upper bound of "Satisfactory" range |
| good_max | numeric | Upper bound of "Good" range |

## Best Practices
- Use 2–3 performance bands; more than 3 reduces contrast between shades
- Place target line at a visually distinct width (thicker than data lines)
- Stack multiple bullet graphs with aligned axes for cross-metric comparison
- Add metric label and unit on the left axis; value annotation on the bar

## Common Mistakes
- Performance bands that are too similar in shade, making them hard to distinguish (smell B — zero-variance-broadcast applied to ranges)
- Inconsistent scales across stacked bullet graphs, making cross-metric comparison invalid
- Target line that blends into the bar colour
- Using a bullet graph when actual vs. target bar chart is sufficient and more familiar to the audience

## Implementation Notes

### matplotlib
```python
ax.barh(0, good_max, color='#d3d3d3', height=0.8)    # Good band
ax.barh(0, sat_max, color='#a8a8a8', height=0.8)     # Satisfactory band
ax.barh(0, poor_max, color='#696969', height=0.8)    # Poor band
ax.barh(0, actual, color='black', height=0.35)        # Primary measure
ax.plot([target, target], [-0.4, 0.4], color='white', linewidth=3)  # Target
```

### plotly
`go.Indicator(mode='number+gauge+delta', gauge=dict(shape='bullet', steps=[...], threshold=dict(value=target)))`.

### altair
Compose with layered `mark_bar()` for bands, a narrower `mark_bar()` for the actual value, and `mark_tick()` for the target.

### excel / tableau
**Tableau**: Dual-axis bar chart with reference lines and background bands. **Excel**: Stacked bar chart with manual formatting.

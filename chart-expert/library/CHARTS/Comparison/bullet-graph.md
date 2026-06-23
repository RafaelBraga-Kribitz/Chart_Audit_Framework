---
name: Bullet Graph
category: Comparison
input_type: [cat-value, interval-range]
it_variants: []
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Bar, Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics]
complexity: Intermediate
encoding_channels: [position, length, color-value]
tool_support: [plotly, d3, tableau, powerbi, matplotlib]
failure_modes: [B]
alternatives: [bar-chart, lollipop-chart, gauge-chart]
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
A bullet graph, invented by Stephen Few, is a compact bar chart designed to replace dashboard gauges and meters. It features a primary bar showing the actual value, a vertical marker line showing the target value, and background shading bands representing qualitative performance ranges (e.g., poor/satisfactory/good). It communicates actual vs. target vs. performance range in a single, space-efficient glyph.

## When to Use
- Dashboard KPIs where actual performance must be compared to a target
- When space is limited and multiple metrics need to be shown compactly
- Replacing bloated gauge/speedometer charts in executive dashboards
- Communicating performance against tiered thresholds (e.g., below target / on target / exceeds target)

## When NOT to Use
- No meaningful target or benchmark exists (use a simple bar chart)
- Zero-variance metric where all values are identical — see Smell B
- The audience is unfamiliar with bullet graph encoding and cannot distinguish the three visual elements
- More than 6–8 bullet graphs in a single view (space savings diminish; consider a table)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| metric | categorical | KPI name |
| actual | numeric | The current measured value (primary bar) |
| target | numeric | The goal/benchmark (marker line) |
| range_poor | numeric | Upper boundary of poor performance band |
| range_satisfactory | numeric | Upper boundary of satisfactory band |
| range_good | numeric | Maximum expected value (good performance band) |

## Best Practices
- Use shades of a single neutral gray for performance bands; use a single bold color for the actual bar
- The target marker should be a thin, high-contrast vertical line or tick
- Align multiple bullet graphs on the same scale when comparing multiple metrics
- Label the metric name on the left, range descriptions optionally below
- Horizontal orientation is standard and reads more naturally for most KPI names

## Common Mistakes
- Using three distinct hues for performance bands, creating an unnecessary rainbow effect
- Making the primary bar the same width as the background bands (use a narrower bar)
- Showing a bullet graph for a metric with zero variance — see Smell B
- Omitting the target line, removing the bullet graph's primary comparison capability

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 1.5))
ax.barh(0, range_good, height=0.6, color='#d0d0d0')
ax.barh(0, range_satisfactory, height=0.6, color='#a0a0a0')
ax.barh(0, range_poor, height=0.6, color='#707070')
ax.barh(0, actual, height=0.3, color='steelblue')
ax.axvline(target, color='black', linewidth=3)
ax.set_yticks([])
plt.tight_layout()
```

### plotly
`go.Indicator(mode='number+gauge+delta', gauge={'axis': {'range': [0, range_good]}, ...})` — or build with stacked bar traces.

### altair
Requires layering multiple `mark_bar` (for bands and actual) with `mark_rule` for the target line.

### excel / tableau
Tableau: Use stacked bar chart with a reference line for target. Excel: Stacked bar + secondary axis for target marker.

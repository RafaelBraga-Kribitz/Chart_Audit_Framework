---
name: Angular Gauge
category: Specialized
input_type: [cat-value]
it_variants: []
analytical_function: Deviation
visual_family: Chart
shape_primitive: [Polygon, Line]
cardinality_fit: [small-N]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [angle, color-hue, color-value]
tool_support: [plotly, d3, powerbi]
failure_modes: [B]
alternatives: [bullet-graph, semi-circle-donut-chart, lollipop-chart]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
---
# Angular Gauge

## Description
Also known as a Speedometer Chart, Dial Chart, or Gauge Chart. An Angular Gauge displays a single KPI value on a circular arc, with a needle or fill indicating the current value's position between minimum and maximum. Colour-coded zones (red/amber/green) on the arc communicate performance thresholds at a glance. Despite their popularity in executive dashboards, gauge charts are frequently criticised by data visualisation experts because they use a large amount of space to encode a single number that could simply be displayed as text.

## When to Use
- Single-metric KPI dashboards where the visual metaphor of "how full is the tank" resonates with the audience
- Operational monitoring displays where analogue gauges are the established communication convention
- When the actual number needs emotional/status context (danger zone vs. safe zone)

## When NOT to Use
- When precise values matter — a number label or bar is more readable
- Multiple KPIs needing comparison — gauge charts are space-inefficient
- When trend over time matters alongside the current value (add a small line chart instead)
- When Stephen Few's Bullet Graph would convey the same information more compactly

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| value | numeric | Current KPI value |
| min | numeric | Minimum of the scale |
| max | numeric | Maximum of the scale |
| zone_thresholds | numeric[] | Boundaries between red/amber/green zones |

## Best Practices
- Always display the numeric value as text within or below the gauge
- Use 2–3 zones maximum; don't crowd the arc with many colours
- Label the min and max endpoints of the arc
- Place target or benchmark as a secondary marker on the arc

## Common Mistakes
- Zone widths that don't reflect the actual performance distribution (equal widths when ranges are asymmetric) (smell B)
- Gauge with no numeric annotation, forcing viewers to estimate the needle position
- Using a 3D or embossed gauge aesthetic that distorts the arc length
- Comparing multiple gauges on a single page without aligned scales

## Implementation Notes

### matplotlib
```python
# Semi-circle gauge using a donut arc
theta = np.linspace(np.pi, 0, 100)
ax.plot(np.cos(theta), np.sin(theta), 'lightgrey', linewidth=20)
needle_angle = np.pi - (value - min_val) / (max_val - min_val) * np.pi
ax.annotate('', xy=(0.7*np.cos(needle_angle), 0.7*np.sin(needle_angle)),
            xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=2))
```

### plotly
`go.Indicator(mode='gauge+number', value=val, gauge=dict(axis=dict(range=[min_v,max_v]), bar=dict(color='darkblue'), steps=[...]))`.

### altair
Not natively supported; implement with polar arc marks and manual needle calculation.

### excel / tableau
**Excel**: Doughnut chart technique with semi-circle and needle. **Power BI**: Native Gauge visual. **Tableau**: Requires calculated fields and dual-axis technique.

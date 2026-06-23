---
name: Waffle Chart
category: Composition
input_type: [composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Square]
cardinality_fit: [small-N]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [color-hue, area]
tool_support: [matplotlib, d3, powerbi]
failure_modes: [I, J]
alternatives: [pie-chart, stacked-bar-100pct]
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
# Waffle Chart

## Description
A Waffle Chart (also called a Square Pie Chart) represents part-to-whole composition as a 10×10 grid of cells, where each cell equals 1% of the total. Categories are coloured to fill their proportional share of the grid. Compared to a Pie Chart, it allows more accurate reading of percentages (by counting cells) while remaining visually engaging. The square grid metaphor is immediately intuitive to general audiences.

## When to Use
- Showing a single percentage or simple 2–3 way composition to a general audience
- Infographics and reports where visual appeal and quick percentage reading matter
- When a Pie Chart feels too clichéd and a bar chart too plain for the context

## When NOT to Use
- More than 4–5 categories (too many colours in the grid; cells become fragmentary)
- When exact values differ by less than 1% (grid resolution is limited to 1% steps)
- High-density dashboards where space is at a premium

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| category | categorical | Each category receives a colour |
| value | numeric [0–100] | Percentage (rounds to nearest integer cell count) |

## Best Practices
- Always use a 10×10 grid (100 cells = 100%); avoid non-standard grid sizes
- Fill categories left-to-right, top-to-bottom in a consistent direction
- Round percentages carefully to ensure cells sum to exactly 100
- Annotate each category with its label and percentage value outside the grid

## Common Mistakes
- Percentages not summing to 100 after rounding, causing gaps or overflow (smell I)
- Using waffle charts for data with more decimal precision than 1% (misleading rounding)
- Silently dropping the smallest category when rounding down to 0 cells (smell J)
- Comparing multiple waffle charts side-by-side — use a grouped bar chart instead

## Implementation Notes

### matplotlib
```python
import pywaffle
fig = plt.figure(FigureClass=pywaffle.Waffle,
                 rows=10, values=values, labels=labels,
                 legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4)})
```

### plotly
Not natively available; use `go.Heatmap` with a 10×10 categorical colour grid as a workaround.

### altair
Use `mark_square()` with a pre-computed 10×10 grid of x/y positions and colour encoding.

### excel / tableau
**Excel**: Not natively supported; use a 10×10 conditional formatting table. **Tableau**: Use a 10×10 scatter with square marks and colour encoding.

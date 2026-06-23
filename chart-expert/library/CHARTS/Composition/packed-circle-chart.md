---
name: Packed Circle Chart
category: Composition
input_type: [hierarchical-cat, cat-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Circle]
cardinality_fit: [medium, large]
audience: [Analytics, Public]
complexity: Intermediate
encoding_channels: [area, color-hue, color-value]
tool_support: [d3, plotly, matplotlib]
failure_modes: [I, J]
alternatives: [treemap, sunburst-diagram, bubble-map]
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
# Packed Circle Chart

## Description
Also known as Circle Packing or Bubble Chart (hierarchical). A Packed Circle Chart represents hierarchical or flat categorical data as circles packed tightly together, with each circle's area proportional to a value. In hierarchical mode, parent circles enclose their children. It is more visually striking than a Treemap but less space-efficient and less accurate for precise value comparison, since circle areas are harder to compare than rectangle areas.

## When to Use
- Presenting a large number of entities where relative size differences are pronounced
- Infographic or editorial contexts where visual appeal matters alongside data accuracy
- Showing two levels of hierarchy (parent group → leaf items) in a compact view

## When NOT to Use
- Precise value comparisons required — treemap or bar chart is more accurate
- Very large datasets where small circles become invisible
- Data without a natural part-to-whole or categorical grouping structure

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique node identifier |
| parent | string | Parent id; empty for root (hierarchical mode) |
| label | string | Display name |
| value | numeric (≥0) | Circle area proportional to this |
| group | categorical (optional) | Colour grouping for flat mode |

## Best Practices
- Use colour to distinguish top-level groups; use tints within each group for children
- Always label the largest circles; use tooltips for smaller ones
- Ensure parent circle area exceeds the sum-of-children visual area (packing wastes space)
- Combine with interaction (zoom/drill) for deeper hierarchies

## Common Mistakes
- Comparing circles of similar size — area perception is less accurate than length (smell B if differences are invisible)
- Silently omitting small-value items that don't render (smell J)
- Using this chart when a simple ranked bar chart would communicate the ranking more clearly

## Implementation Notes

### matplotlib
```python
# Use circlify library for layout
import circlify
circles = circlify.circlify(values, show_enclosure=False)
for c in circles:
    ax.add_patch(plt.Circle((c.x, c.y), c.r, alpha=0.6))
```

### plotly
`go.Treemap` with `tiling_packing_algorithm` or use `go.Scatter` with circle markers sized by value as a workaround.

### altair
`mark_circle()` with `size=alt.Size('value:Q')` for flat mode; no native circle-packing layout.

### excel / tableau
Not natively supported in either tool. Use D3.js `d3.pack()` for production implementations.

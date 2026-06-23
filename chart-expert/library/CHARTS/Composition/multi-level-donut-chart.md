---
name: Multi-Level Donut Chart
category: Composition
input_type: [hierarchical-cat, composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Polygon]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Intermediate
encoding_channels: [angle, area, color-hue, color-value]
tool_support: [plotly, d3, tableau, powerbi]
failure_modes: [I, J]
alternatives: [sunburst-diagram, treemap]
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
# Multi-Level Donut Chart

## Description
A Multi-Level Donut Chart stacks concentric rings, each ring representing one hierarchical level of a dataset. The innermost ring shows the top-level categories; each subsequent ring subdivides those categories into finer groups. Arc widths within each ring are proportional to values, preserving part-to-whole relationships at every level. It is functionally equivalent to a Sunburst Diagram but uses uniform-width rings rather than wedge-based radii.

## When to Use
- Visualising two or three levels of a hierarchy with part-to-whole relationships at each level
- When a Sunburst is too complex and a flat Treemap loses the layered structure
- Comparing category shares at multiple hierarchical levels simultaneously

## When NOT to Use
- More than 3 hierarchical levels (rings become too thin)
- More than ~5 items per ring (labels collide)
- When precise value comparison is needed — a bar chart hierarchy is more accurate

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| level | categorical | Ring identifier (e.g., "L1", "L2") |
| category | categorical | Node name at this level |
| parent | categorical | Parent node name; null for root |
| value | numeric (≥0) | Determines arc length at each level |

## Best Practices
- Use colour families: outer rings as lighter tints of the inner ring's hue
- Limit to 2–3 rings; add interaction (hover tooltips) for deeper hierarchies
- Ensure parent values equal the sum of their children
- Label the innermost ring only; use tooltips for outer rings

## Common Mistakes
- Inner and outer rings not aligning parent–child relationships visually (smell J)
- Categories at different levels that are not mutually exclusive (smell I)
- Using this chart when a simple pie would suffice (over-engineering)
- Inconsistent colour mapping across levels confusing parent–child linkage

## Implementation Notes

### matplotlib
```python
# Two rings: inner categories, outer subcategories
ax.pie(inner_vals, radius=0.8, wedgeprops=dict(width=0.4, edgecolor='w'))
ax.pie(outer_vals, radius=1.2, wedgeprops=dict(width=0.4, edgecolor='w'))
```

### plotly
`go.Sunburst` with `branchvalues='total'` is the closest native equivalent. For true concentric donuts use stacked `go.Pie` traces with `hole` and `domain` parameters.

### altair
Not natively supported; requires custom layer composition with arc marks at different radii.

### excel / tableau
**Tableau**: Requires calculated fields and dual-axis technique per ring. **Excel**: Not natively supported; use add-ins.

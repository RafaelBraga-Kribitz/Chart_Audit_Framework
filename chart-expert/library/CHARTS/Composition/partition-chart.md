---
name: Partition Chart
category: Composition
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Bar, Polygon]
cardinality_fit: [small-N, medium]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [length, area, color-hue]
tool_support: [d3, plotly]
failure_modes: [I, J]
alternatives: [treemap, sunburst-diagram, icicle-chart]
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
# Partition Chart

## Description
Also known as an Icicle Chart or Partition Layout. A Partition Chart displays hierarchical data as a set of adjacent, nested rectangles arrayed along one axis (typically top-to-bottom or left-to-right). Unlike a Treemap where rectangles fill a 2D space with varying aspect ratios, a Partition Chart fixes one dimension — each level of the hierarchy occupies a uniform band height, with width proportional to value. This makes the hierarchical structure more immediately readable than a Treemap.

## When to Use
- Exploring multi-level hierarchies where the tree structure should be visually explicit
- File directory trees, organisational hierarchies, or taxonomies with proportional values
- When Treemap's variable aspect ratios make label reading difficult

## When NOT to Use
- Very deep hierarchies (many levels create extremely thin bands)
- When a compact overview matters more than structural clarity (Treemap is more space-efficient)
- Non-hierarchical data

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique node identifier |
| parent | string | Parent node id; null/empty for root |
| label | string | Display name |
| value | numeric (≥0) | Leaf value; parent value = sum of children |

## Best Practices
- Root node occupies the full width at the top; children subdivide below
- Use colour to distinguish top-level categories; use tints/shades for deeper levels
- Label only nodes wide enough to contain legible text; use tooltips otherwise
- Allow click-to-zoom for interactive exploration of deep hierarchies

## Common Mistakes
- Categories at the same level that are not mutually exclusive (smell I)
- Small nodes silently not rendered at fine hierarchy levels (smell J)
- Confusing this with a Gantt Chart (which also uses horizontal bars but for time ranges)

## Implementation Notes

### matplotlib
Not natively supported; requires custom rectangle drawing with recursive subdivision.

### plotly
`go.Icicle(ids=ids, labels=labels, parents=parents, values=values, branchvalues='total')` — Plotly's native icicle/partition chart.

### altair
Not natively supported; requires precomputed x/y/width/height positions as `mark_rect()`.

### excel / tableau
Not natively available in either tool. Use Plotly or D3.js `d3.partition()` for production implementations.

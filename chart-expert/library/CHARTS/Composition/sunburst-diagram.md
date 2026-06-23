---
name: Sunburst Diagram
category: Composition
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Part-to-whole
visual_family: Diagram
shape_primitive: [Polygon]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [angle, area, color-hue, color-value]
tool_support: [plotly, d3, tableau, powerbi]
failure_modes: [I, J]
alternatives: [treemap, multi-level-donut-chart, partition-chart]
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
# Sunburst Diagram

## Description
Also known as a Ring Chart, Multi-level Pie Chart, Belt Chart, or Radial Treemap. A Sunburst Diagram shows hierarchical data through a series of concentric rings where each ring represents one hierarchical level, with the centre being the root. Rings are sliced into arcs proportional to their value relative to their parent, enabling viewers to read both the hierarchy structure and each node's contribution to its parent level simultaneously.

## When to Use
- Exploring multi-level hierarchical data where part-to-whole relationships matter at every level
- File system sizes, organisational rollups, budget breakdowns with sub-categories
- Interactive dashboards where users can click to drill down into segments

## When NOT to Use
- Flat (non-hierarchical) data — use a pie or bar chart instead
- More than 4 levels deep — outer rings become unreadably thin
- Precise value comparison between nodes at the same level

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique node identifier |
| parent | string | Parent node id; empty string or null for root |
| label | string | Display name |
| value | numeric (≥0) | Leaf values; parent values derived from sum of children |

## Best Practices
- Use a consistent colour family per top-level branch (hue for L1, tints for L2+)
- Provide interactive hover/click to reveal exact values — static labels crowd quickly
- Verify that leaf values sum correctly to their parent (no silent gaps, smell J)
- Start with the root in the centre and expand outward; avoid reversing the hierarchy

## Common Mistakes
- Showing too many levels, making outer arcs pixel-thin and unreadable
- Categories at the same level that are not mutually exclusive (smell I)
- Using equal-angle slices rather than value-proportional angles (misleading proportions)
- Missing or inconsistent parent–child linkage in the data model (smell J)

## Implementation Notes

### matplotlib
Not directly supported; build with custom `Wedge` patches at increasing radii or use the `squarify` + polar coordinate workaround.

### plotly
```python
go.Sunburst(ids=ids, labels=labels, parents=parents, values=values,
            branchvalues='total')
```

### altair
Not natively supported; requires custom arc transform with nested grouping.

### excel / tableau
**Excel**: Not natively available; use Power BI or third-party add-ins. **Tableau**: Requires significant calculated field workarounds; use built-in Hierarchy + Treemap as alternative.

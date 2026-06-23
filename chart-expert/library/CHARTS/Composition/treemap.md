---
name: Treemap
category: Composition
input_type: [hierarchical-cat]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Square, Polygon]
cardinality_fit: [medium, large]
audience: [Analytics, Technical, Executive]
complexity: Intermediate
encoding_channels: [area, color-hue, color-value]
tool_support: [matplotlib, plotly, altair, d3, tableau, powerbi, excel]
failure_modes: [I, J]
alternatives: [sunburst-diagram, packed-circle-chart, partition-chart]
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
# Treemap

## Description
A Treemap visualises hierarchical data as nested rectangles where each rectangle's area is proportional to a quantitative value. Parent categories contain their children as smaller rectangles within them. The squarified tiling algorithm (the default in most libraries) keeps rectangles as square-like as possible for optimal area comparison. Originally developed by Ben Shneiderman to visualise file directory sizes.

## When to Use
- Showing composition of a large hierarchical dataset in compact screen space
- Comparing proportions between dozens of leaf nodes across a few parent categories
- When both the hierarchy structure and the magnitude of individual items matter

## When NOT to Use
- Comparing items with very similar values (area discrimination is imprecise)
- More than 3–4 levels of nesting (inner rectangles become invisible)
- Time-series data or data without a natural hierarchy

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| id | string | Unique node identifier |
| parent | string | Parent id; empty for root |
| label | string | Display name |
| value | numeric (≥0) | Leaf area; parent area = sum of children |
| color_metric | numeric (optional) | Secondary encoding for colour (e.g., growth rate) |

## Best Practices
- Use colour to encode a secondary dimension (e.g., performance vs. size)
- Label only rectangles large enough to contain legible text; use tooltips for small ones
- Group small categories into an "Other" bucket to avoid micro-sliver rectangles (smell J)
- Use a diverging palette for colour if encoding positive/negative deviation

## Common Mistakes
- Encoding raw counts instead of normalised values in colour, misleading relative performance
- Categories at the same level that are not mutually exclusive (smell I)
- Silently dropping small categories without an "Other" label (smell J)
- Over-nesting (4+ levels) making the chart unnavigable without interaction

## Implementation Notes

### matplotlib
```python
import squarify
squarify.plot(sizes=values, label=labels, alpha=0.8, ax=ax)
ax.axis('off')
```

### plotly
```python
go.Treemap(ids=ids, labels=labels, parents=parents, values=values,
           branchvalues='total', textinfo='label+percent parent')
```

### altair
Not natively supported; requires pre-computed rectangle coordinates (e.g., from `squarify`) passed as `mark_rect()`.

### excel / tableau
**Excel**: Insert → Treemap (Excel 2016+). **Tableau**: Built-in Treemap mark type; drag hierarchy to Detail shelf.

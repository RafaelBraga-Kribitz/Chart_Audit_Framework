---
name: Marimekko Chart
category: Composition
input_type: [cat-multi-value]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Bar, Polygon]
cardinality_fit: [small-N, medium]
audience: [Analytics, Executive]
complexity: Intermediate
encoding_channels: [length, area, color-hue]
tool_support: [d3, tableau, plotly]
failure_modes: [I, J]
alternatives: [stacked-bar-100pct, treemap]
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
# Marimekko Chart

## Description
Also known as a Mosaic Plot or Mekko Chart. A Marimekko Chart is a two-dimensional 100% stacked bar chart where both the width and height of each column segment are variable. The column width encodes one categorical dimension (e.g., market share by region) and the segment height encodes a second dimension (e.g., product mix within that region). This allows simultaneous visualisation of two categorical variables and their proportional relationships.

## When to Use
- Comparing market share or composition across multiple categories on two dimensions simultaneously
- Business strategy presentations showing segment size × sub-segment mix
- When the audience needs to see both "how big is each group" and "what is each group composed of"

## When NOT to Use
- When precise comparisons between non-adjacent segments are needed (no common baseline)
- More than 5–6 column categories or 5–6 segment categories (chart becomes cluttered)
- When one dimension has uniform width (use a simple 100% stacked bar instead)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| x_category | categorical | Determines column identity and width (sum of values) |
| segment | categorical | Sub-category within each column |
| value | numeric (≥0) | Cell value; column widths = sum of all segments per x_category |

## Best Practices
- Label segment percentages inside each cell only when cells are large enough
- Sort columns by descending total size (left to right) to create a natural ranking
- Use consistent segment ordering across all columns
- Add a legend for the segment colours; keep the palette to ≤6 distinct hues

## Common Mistakes
- Non-mutually-exclusive segments that inflate column totals (smell I)
- Silently dropping small segments below a display threshold without labelling them (smell J)
- Misleading the viewer by not labelling column widths, hiding the size dimension
- Too many segments making the chart a confusing mosaic with no clear story

## Implementation Notes

### matplotlib
```python
# Compute cumulative widths and heights manually
for i, (cat, width) in enumerate(zip(categories, widths)):
    bottom = 0
    for seg, height in zip(segments, seg_heights[i]):
        ax.bar(x=cumulative_x[i], height=height, width=width,
               bottom=bottom, align='edge')
        bottom += height
```

### plotly
No native Marimekko type; construct using `go.Bar` with custom `x` positions and widths, or use community libraries like `plotly-mekko`.

### altair
Use `mark_rect()` with pre-computed x/y/width/height columns as position encodings.

### excel / tableau
**Tableau**: Achievable with calculated fields for Gantt Bar mark type. **Excel**: Not natively supported; requires manual positioning.

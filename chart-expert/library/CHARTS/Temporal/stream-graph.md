---
name: Stream Graph
category: Temporal
input_type: [time-series, composition]
it_variants: []
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Area]
cardinality_fit: [medium, large]
audience: [Analytics, Public]
complexity: Advanced
encoding_channels: [position, color-hue, area]
tool_support: [d3, plotly, altair, matplotlib]
failure_modes: [I, J, L]
alternatives: [stacked-area-chart, sorted-stream-graph, line-chart]
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

# Stream Graph

## Description
A stream graph (also called a ThemeRiver) is a stacked area chart where the baseline is displaced to center the bands symmetrically around a horizontal axis, creating a flowing, organic shape. Each layer represents a category's value over time, and layers are stacked symmetrically above and below the center. The visual emphasis is on the overall flow and shape rather than precise values.

## When to Use
- Exploratory visualization of many time-varying categories (5–20+)
- When the overall aesthetic and flow pattern is more important than precision
- Magazine-style or public-facing storytelling about compositional change over time
- Highlighting dominant periods and shifts in category prominence

## When NOT to Use
- Precise value reading is required (use stacked bar or table instead)
- Series are not additive parts of a meaningful whole — see Smell I
- Audience needs to identify exact category boundaries (they float and shift)
- Fewer than 4–5 categories (a stacked area chart is clearer)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Sorted ascending |
| value | numeric | Non-negative; represents part of a flowing total |
| category | categorical | The series dimension; should be mutually exclusive |

## Best Practices
- Sort categories by order of peak dominance or by color family for readability
- Use a categorical color palette with enough contrast; avoid too many similar hues
- Add interactive tooltips (hover) since precise values are hard to read visually
- Label the largest/most prominent streams directly
- Use the "wiggle" offset (minimize displacement) rather than "silhouette" for aesthetics

## Common Mistakes
- Using non-additive series that create a misleading total shape — see Smell I
- Silently dropping small categories, inflating apparent totals — see Smell J
- Over-smoothing the streams to hide actual step changes in data — see Smell L
- Using a stream graph in a context where precision is expected

## Implementation Notes

### matplotlib
Not natively stream-layout aware; use `ax.stackplot` with the `baseline='wiggle'` option (via scipy or manual centring).

### plotly
Not directly supported; build using `go.Scatter(fill='tonexty')` with pre-computed baseline offsets.

### altair
Not natively supported. Requires pre-computed stream offsets as data columns, then layered area marks.

### d3
`d3.stack().offset(d3.stackOffsetWiggle)` with `d3.area()` — the canonical implementation.

### excel / tableau
Not natively supported in either tool.

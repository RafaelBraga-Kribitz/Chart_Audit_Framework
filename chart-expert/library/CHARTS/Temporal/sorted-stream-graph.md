---
name: Sorted Stream Graph
category: Temporal
input_type: [time-series, composition]
it_variants: [IT001, IT007]
analytical_function: Part-to-whole
visual_family: Chart
shape_primitive: [Area]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [position, color-hue, area]
tool_support: [d3, matplotlib]
failure_modes: [I, J, L]
alternatives: [stream-graph, stacked-area-chart, line-chart]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: part-to-whole
ibcs_status: conditional
questions: ["How is the whole split on Sorted Stream Graph?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Sorted Stream Graph

## Description
A sorted stream graph is a variant of the stream graph where categories are sorted at each time step by their value, ensuring that dominant categories always appear in the same relative position (typically the center or the largest bands on the outside). This sorting reduces the visual chaos of standard stream graphs and makes individual category trajectories easier to follow across time.

## When to Use
- When a standard stream graph is too chaotic to read due to many crossing bands
- When the rank ordering of categories changes over time and those rank changes are the story
- Exploratory analysis of many compositional time series where pattern tracking matters
- When you want to retain the flow aesthetic while improving interpretability

## When NOT to Use
- Categories are few enough that a stacked area chart is clearer
- Precise value reading is the primary goal
- Categories should not be re-sorted (their fixed order carries meaning)
- Series are not additive parts of a whole — see Smell I

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| date / time | date or ordered numeric | Sorted ascending |
| value | numeric | Non-negative; part of a compositional total |
| category | categorical | Series identifier; mutually exclusive |

## Best Practices
- Pre-compute the sorted order at each time step and pass as explicit layer ordering
- Use consistent color assignment per category even as layer order changes
- Add direct labels or interactive tooltips — sort-scrambled positions are hard to track
- Document the sort criterion clearly (e.g., "sorted by value at each time step")

## Common Mistakes
- Sorting in a way that makes colors appear to jump discontinuously, confusing viewers
- Using non-additive series — see Smell I
- Silently dropping thin categories after sorting — see Smell J
- Applying smooth interpolation that hides actual ranking changes — see Smell L


## Dashboard and other surfaces

status: placeholder

`Sorted Stream Graph` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with stream-graph, stacked-area-chart, line-chart. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Bar**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
Requires manual computation: at each time step sort categories by value, reorder the data matrix before passing to `stackplot`. Not trivial to implement.

### plotly
No native support. Requires pre-sorted data matrices with explicit layer ordering via `go.Scatter` traces.

### altair
Not natively supported; requires pre-computed layout offsets.

### d3
Extend the standard `d3.stack()` with a custom sort function applied per time step, then render with `d3.area()`.

### excel / tableau
Not supported natively.

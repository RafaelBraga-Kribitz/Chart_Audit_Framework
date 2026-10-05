---
name: Parallel Sets
category: Composition
input_type: [cat-multi-value, composition]
it_variants: [IT029, IT031, IT007, IT016, IT020, IT023]
analytical_function: Flow
visual_family: Diagram
shape_primitive: [Area, Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Advanced
encoding_channels: [length, area, color-hue]
tool_support: [d3, plotly]
failure_modes: [I, J]
alternatives: [sankey-diagram, alluvial-diagram, parallel-coordinates]
source: [datavizproject, datavizcatalogue]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: flow
ibcs_status: conditional
questions: ["How does quantity move between states?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: none
---
# Parallel Sets

## Description
Parallel Sets (also called Parsets) visualise the distribution of categorical variables and the flow of counts or proportions between them. Each vertical axis represents a categorical dimension, divided into segments proportional to the category frequency. Ribbon-like flows connecting the axes show how entities are distributed across combinations of categories. Unlike Sankey Diagrams, flows are divided and recombined at each axis; unlike Parallel Coordinates, the axes hold discrete categories rather than continuous values.

## When to Use
- Exploring relationships and distribution patterns across multiple categorical variables
- Understanding how populations split across categories (e.g., demographics × outcome × treatment)
- When Sankey Diagram flows represent category membership rather than directed process stages

## When NOT to Use
- Continuous numeric variables (use Parallel Coordinates instead)
- Fewer than 3 categorical dimensions (a grouped bar chart is simpler)
- Very high cardinality dimensions with many unique values per axis

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| dim_1 … dim_n | categorical | One column per axis/dimension |
| weight | numeric (optional) | Count or value to aggregate; uniform if omitted |

## Best Practices
- Order axes by the most important or grouping dimension first (leftmost)
- Colour ribbons by the first dimension's categories for a consistent visual anchor
- Limit each axis to ≤6 categories; aggregate rare values into "Other"
- Provide interactive highlighting to trace individual flow paths

## Common Mistakes
- Treating flows as causal or directional when they are purely distributional (smell I)
- Axes with high cardinality creating a hairball of thin ribbons (smell J)
- Missing data silently absorbed into undefined flows (smell J)
- Confusing Parallel Sets with Parallel Coordinates (continuous vs categorical axes)

## Dashboard and other surfaces

status: placeholder

Parallel Sets is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with `sankey-diagram`, `alluvial-diagram`, `parallel-coordinates`. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Coarse template type, when a Databox or Zebra template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Dashboard specifications that cite this chart are under `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
Not directly supported; requires custom polygon rendering using Bezier curves for ribbons.

### plotly
`go.Parcats(dimensions=[...], line=dict(color=color_arr, colorscale=...))` — native Parallel Categories plot.

### altair
Not natively supported; requires custom rendering.

### excel / tableau
Not natively available in either tool. Use D3.js or Plotly for production use.

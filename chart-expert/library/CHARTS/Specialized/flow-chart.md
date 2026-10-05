---
name: Flow Chart
category: Specialized
input_type: [cat-multi-value]
it_variants: [IT029]
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Polygon, Line]
cardinality_fit: [small-N, medium]
audience: [Executive, Analytics, Technical, Public]
complexity: Basic
encoding_channels: [position, shape, color-hue]
tool_support: [d3]
failure_modes: []
alternatives: [swimlane-chart, mind-map, network-diagram]
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
ibcs_status: preferred
questions: ["What structure or process does Flow Chart explain?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: plot
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Flow Chart

## Description
A Flow Chart (or Flowchart) is a diagram that represents a process, algorithm, or workflow using standardised symbols connected by directed arrows. Rectangles represent process steps, diamonds represent decision points, ovals represent start/end (terminal) nodes, and parallelograms represent input/output. The symbols and arrow directions make logical flow, branching conditions, and process sequences immediately readable without domain expertise.

## When to Use
- Documenting business processes, algorithms, or operational workflows
- Communicating decision logic or conditional branching to diverse audiences
- Onboarding documentation, standard operating procedures, troubleshooting guides

## When NOT to Use
- Quantitative data (no encoding for values, frequencies, or magnitudes)
- Very long or parallel processes better shown as a Swimlane or Gantt Chart
- Cyclical processes with many feedback loops (becomes unnavigable)

## Data Requirements
A flow chart is typically drawn manually or from a structured process definition:
| Field | Type | Notes |
|-------|------|-------|
| node_id | string | Unique step identifier |
| label | string | Step description |
| type | categorical | "process", "decision", "terminal", "io" |
| next | string(s) | Connected node ids (one for linear, two for decision branches) |
| condition | string (optional) | Branch condition label for decision edges |

## Best Practices
- Use standard ISO 5807 / ANSI symbols consistently
- Flow top-to-bottom or left-to-right; avoid bidirectional flow without explicit loops
- Label all decision branches (Yes/No, True/False, or specific conditions)
- Limit to ~10–15 steps per chart; create sub-process charts for complex segments

## Common Mistakes
- Using non-standard shapes inconsistently across the diagram
- Omitting decision branch labels, leaving viewers to guess conditions
- Creating multi-page flowcharts that lose the reader's position context
- Using flowcharts for data visualisation tasks where charts are more appropriate


## Dashboard and other surfaces

status: placeholder

`Flow Chart` can sit on a dashboard, in a report, or in a notebook. Executives and clients get it when the comparison is direct. Analysts may still pair it with a diagnostic plot. If the page is only a score, pair it with swimlane-chart, mind-map, network-diagram.

Suggested communication placement: **detail** zone. Vault coarse type, when a scraped template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
Not well-suited; use `matplotlib.patches` with Fancy Arrow and Rectangle patches for simple diagrams.

### plotly
`go.Scatter` with annotation arrows; very manual process. Use Mermaid or dedicated tools instead.

### altair
Not supported for flow chart creation.

### excel / tableau
**Excel**: Insert → SmartArt → Process, or use shapes manually. Dedicated tools: Lucidchart, draw.io, Mermaid (code-based), Microsoft Visio.

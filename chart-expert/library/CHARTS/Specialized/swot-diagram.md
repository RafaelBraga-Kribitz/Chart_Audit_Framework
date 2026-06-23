---
name: SWOT Diagram
category: Specialized
input_type: [cat-multi-value]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Square, Polygon]
cardinality_fit: [small-N]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [color-hue, position]
tool_support: []
failure_modes: []
alternatives: [2x2-matrix, fishbone-diagram]
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
# SWOT Diagram

## Description
A SWOT Diagram is a 2×2 strategic analysis framework displaying Strengths, Weaknesses, Opportunities, and Threats across four quadrants. The top row shows internal factors (Strengths left, Weaknesses right); the bottom row shows external factors (Opportunities left, Threats right). Each quadrant contains bullet points from a qualitative analysis session. It is a text-first diagram rather than a data visualisation, used for strategic planning in business, product management, and policy contexts.

## When to Use
- Strategic planning: auditing an organisation, product, or initiative's strategic position
- Workshop facilitation and structured brainstorming sessions
- Presenting the results of a situational analysis to executive stakeholders

## When NOT to Use
- When quantitative data or precise scoring is available (use a 2×2 matrix with data)
- When more than 4–5 bullet points per quadrant are needed (the diagram becomes unreadable)
- As a substitute for rigorous competitive or environmental analysis

## Data Requirements
A SWOT Diagram is text-content driven:
| Quadrant | Content |
|----------|---------|
| Strengths | Internal positive factors |
| Weaknesses | Internal negative factors |
| Opportunities | External positive factors |
| Threats | External negative factors |

## Best Practices
- Keep each bullet point to one concise, specific insight (not vague generalities)
- Limit each quadrant to 3–5 items to maintain scannability
- Colour-code: green for Strengths/Opportunities, red for Weaknesses/Threats (or use neutral palette)
- Follow up with a TOWS analysis to derive strategic options from the SWOT quadrants

## Common Mistakes
- Overloading quadrants with too many items making the diagram unreadable
- Vague or generic entries ("Good team", "Market competition") that provide no actionable insight
- Mixing internal and external factors within a quadrant
- Treating SWOT as a complete strategy rather than an input to further analysis

## Implementation Notes

### matplotlib
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
labels = [('Strengths', content_S, 'lightgreen'), ('Weaknesses', content_W, 'lightyellow'),
          ('Opportunities', content_O, 'lightblue'), ('Threats', content_T, 'lightsalmon')]
for ax, (title, content, color) in zip(axes.flat, labels):
    ax.set_facecolor(color)
    ax.text(0.05, 0.95, title, fontsize=14, fontweight='bold', va='top', transform=ax.transAxes)
    ax.text(0.05, 0.8, '\n'.join(f'• {item}' for item in content),
            va='top', transform=ax.transAxes, wrap=True)
    ax.axis('off')
```

### plotly
Not the right tool; use a 2×2 grid of text boxes via `go.Table` or PowerPoint/presentation tool.

### altair
Not applicable; this is a text-content diagram.

### excel / tableau
**Excel/PowerPoint**: Use a 2×2 table with colour-filled cells and bullet point text. This is not a data visualisation task for Tableau.

---
name: 2x2 Matrix
category: Specialized
input_type: [cat-multi-value, xy-simple]
it_variants: []
analytical_function: Concept-viz
visual_family: Diagram
shape_primitive: [Square, Dot, Icon]
cardinality_fit: [small-N]
audience: [Executive, Analytics]
complexity: Basic
encoding_channels: [position, color-hue]
tool_support: [matplotlib, d3]
failure_modes: []
alternatives: [swot-diagram, scatter-plot]
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
# 2x2 Matrix

## Description
A 2×2 Matrix (also called a Four-Quadrant Matrix or Priority Matrix) divides a 2D space into four quadrants by two intersecting axes, each representing a dimension of evaluation. Entities (products, initiatives, ideas, risks) are placed in the appropriate quadrant based on their scores on both dimensions. Classic examples include the BCG Growth-Share Matrix (cash cows, stars, dogs, question marks), the Eisenhower Urgency-Importance Matrix, and the Risk-Impact Matrix. It is primarily a strategic decision-making and communication tool rather than a precision data visualisation.

## When to Use
- Strategic prioritisation: classifying items by two criteria simultaneously
- Executive communication where quadrant labels tell the strategic story
- Risk assessment, portfolio analysis, feature prioritisation

## When NOT to Use
- When precise quantitative positions matter more than quadrant membership (use a scatter plot)
- More than ~20 items (the quadrant becomes cluttered)
- When the two dimensions are not independent or binary

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| item | string | Entity being classified |
| x_score | numeric | Score on the horizontal axis dimension |
| y_score | numeric | Score on the vertical axis dimension |
| quadrant | categorical (optional) | Explicit quadrant assignment |

## Best Practices
- Label each quadrant with a memorable name that captures its strategic meaning
- Label the axes clearly with the dimension name and direction (High → Low or Low → High)
- Use consistent scale boundaries; document how midpoint thresholds are set
- Annotate items with labels; use different colours or shapes for sub-groups

## Common Mistakes
- Moving items between quadrants to tell a desired story rather than following data-driven thresholds
- Unlabelled axes making it unclear what each dimension represents
- Treating the matrix as a precise data visualisation when it is a conceptual tool
- Setting the midpoint arbitrarily without disclosing the threshold rule

## Implementation Notes

### matplotlib
```python
ax.axvline(x=midpoint_x, color='black', linewidth=1)
ax.axhline(y=midpoint_y, color='black', linewidth=1)
ax.scatter(df.x_score, df.y_score, s=100, color='steelblue')
for _, row in df.iterrows():
    ax.annotate(row.item, (row.x_score, row.y_score),
                textcoords='offset points', xytext=(5, 5))
# Add quadrant labels as text
ax.text(x_max, y_max, 'Q1 Label', ha='right', va='top', fontsize=12, alpha=0.3)
```

### plotly
`go.Scatter(x=x_scores, y=y_scores, mode='markers+text', text=items)` with `add_hline` and `add_vline` for quadrant dividers.

### altair
`mark_point()` + `mark_text()` with rule marks at midpoints using `mark_rule()`.

### excel / tableau
**Excel**: Scatter chart with added horizontal/vertical reference lines. **Tableau**: Scatter plot with reference lines at midpoints.

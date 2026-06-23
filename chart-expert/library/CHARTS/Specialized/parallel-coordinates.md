---
name: Parallel Coordinates
category: Specialized
input_type: [cat-multi-value, xy-dual-series]
it_variants: []
analytical_function: Comparison
visual_family: Chart
shape_primitive: [Line]
cardinality_fit: [medium, large]
audience: [Analytics, Technical]
complexity: Intermediate
encoding_channels: [position, color-hue]
tool_support: [matplotlib, plotly, altair, d3, tableau]
failure_modes: [J]
alternatives: [radar-chart, parallel-sets, heatmap]
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
# Parallel Coordinates

## Description
A Parallel Coordinates Plot displays multivariate data by placing each dimension on a parallel vertical axis. Each observation is a polyline crossing all axes at its value for each dimension. Patterns of clustering, correlation (axes where lines are parallel = positive correlation; lines that cross = negative correlation), and outliers emerge visually. It is one of the few chart types that can display many dimensions simultaneously without dimensionality reduction. Note: when axes hold categorical variables instead of continuous, the chart becomes Parallel Sets.

## When to Use
- Exploring multivariate continuous data for patterns, clusters, and correlations
- Comparing many-dimensional profiles across entities (e.g., car performance specs, patient clinical variables)
- Feature selection: identifying axes where class separation is clear

## When NOT to Use
- Large datasets (>500 lines) without interaction for filtering and brushing
- Categorical variables on axes (use Parallel Sets)
- When axis ordering matters critically and the reader doesn't know to reorder

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | string | One polyline per observation/entity |
| dim_1 … dim_n | numeric | One axis per dimension; normalise if scales differ |
| group | categorical (optional) | Colour coding for entity class |

## Best Practices
- Normalise axes to [0,1] or z-score when dimensions have very different scales
- Colour lines by the target variable or cluster membership for pattern discovery
- Allow axis reordering interactively — axis order dramatically changes the visual
- Use transparency (alpha 0.1–0.3) for large datasets to manage overplotting

## Common Mistakes
- Unnormalised axes making high-scale dimensions dominate the visual (smell B)
- Too many opaque lines creating an unreadable black mass
- Silently dropping rows with missing values on any dimension (smell J)
- Confusing correlation direction: parallel lines = positive; crossing lines = negative

## Implementation Notes

### matplotlib
```python
from pandas.plotting import parallel_coordinates
parallel_coordinates(df[dims + ['group']], 'group',
                     colormap='tab10', alpha=0.3, ax=ax)
```

### plotly
`go.Parcoords(dimensions=[dict(label=d, values=df[d]) for d in dims], line=dict(color=df.group, colorscale='Viridis'))`.

### altair
Not natively supported; requires coordinate transformation and `mark_line()` with pivoted data.

### excel / tableau
**Tableau**: Achievable via calculated fields and dual-axis technique. **Excel**: Not natively supported.

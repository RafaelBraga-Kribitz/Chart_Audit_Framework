---
name: Chernoff Faces
category: Specialized
input_type: [cat-multi-value]
it_variants: []
analytical_function: Comparison
visual_family: Glyph
shape_primitive: [Circle, Line]
cardinality_fit: [small-N]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [shape, area, position]
tool_support: [matplotlib]
failure_modes: [J]
alternatives: [radar-chart, parallel-coordinates, heatmap]
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
# Chernoff Faces

## Description
Proposed by Herman Chernoff in 1973, Chernoff Faces encode multivariate data as cartoon human faces where different facial features (eye size, mouth curvature, nose size, eyebrow angle, face shape, etc.) represent different data dimensions. The motivation is that humans are highly attuned to detecting differences in facial features, making this a novel perceptual channel for multidimensional data. In practice, Chernoff Faces are rarely used in production analytics due to serious limitations: feature-to-variable mapping is arbitrary, the ordering of features matters enormously, and emotional connotations of face features (happy vs. sad mouth) can bias interpretation.

## When to Use
- Academic or exploratory demonstrations of multivariate glyph visualisation techniques
- Very small datasets where up to 18 dimensions need to be visually compared per observation
- As a conversation starter or teaching example for multivariate visualisation challenges

## When NOT to Use
- Production data analytics (nearly all other multivariate chart types are more reliable)
- Large datasets (glyph-based approaches don't scale)
- When emotional neutrality is required (happy/sad face encoding biases interpretation)
- When the arbitrary mapping of variables to facial features would mislead non-expert audiences

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| entity | string | One face per observation |
| var_1 … var_n | numeric | Each variable maps to one facial feature (n ≤ 18 typically) |

Variable-to-feature mapping must be explicitly defined and disclosed.

## Best Practices
- Assign the most important variable to the most perceptually salient feature (mouth curve)
- Always provide a legend table mapping features to variables
- Arrange faces in a grid sorted by the primary dimension of interest
- Label each face with the entity name beneath it

## Common Mistakes
- Undisclosed or arbitrary variable-to-feature assignments making the chart uninterpretable
- Mapping variables to features with emotional connotations (happy mouth = high value looks positive regardless of context)
- Using Chernoff Faces where a small-multiple bar chart or heatmap would communicate more clearly
- Silently omitting entities with missing values without disclosure (smell J)

## Implementation Notes

### matplotlib
```python
# Use the `chernoff` or `faces` Python package
from matplotlib_faces import chernoff_faces
chernoff_faces(data_matrix, labels=entity_names, feature_names=var_names, ax=ax)
# Or implement manually using Ellipse, Arc patches for each face component
```

### plotly
Not natively supported; would require SVG custom glyphs.

### altair
Not natively supported.

### excel / tableau
Not available in any standard tool. This is primarily a research/academic visualisation.

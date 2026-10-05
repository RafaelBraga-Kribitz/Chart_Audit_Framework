---
name: Nomogram
category: Relationship
input_type: [cat-multi-value, demo-grouped]
it_variants: [IT029, IT011]
analytical_function: Correlation
visual_family: Diagram
shape_primitive: [Line, Dot]
cardinality_fit: [small-N, medium]
audience: [Technical, Analytics]
complexity: Advanced
encoding_channels: [position, length]
tool_support: [matplotlib, d3]
failure_modes: [E, A]
alternatives: [parallel-coordinates, scatter-plot, decision-tree, regression-table]
source: [datavizproject]
implementations:
  matplotlib: {status: stub, source_file: null, last_iterated: null}
  plotly: {status: stub, source_file: null, last_iterated: null}
  altair: {status: stub, source_file: null, last_iterated: null}
  d3: {status: stub, source_file: null, last_iterated: null}
  tableau: {status: stub, source_file: null, last_iterated: null}
  powerbi: {status: stub, source_file: null, last_iterated: null}
  excel: {status: stub, source_file: null, last_iterated: null}
ft_family: correlation
ibcs_status: conditional
questions: ["Do the two measures in Nomogram move together?", "Who is the audience, and is this the analysis surface or the communication surface?"]
related_kpis: []
analysis_surface: notebook
communication_surface: dashboard
audience_roles: [Executive, Data Scientist, Researcher, R&D, Marketing Analytics, Data Analytics, Development, HR]
---
# Nomogram

## Description
A Nomogram is a graphical calculation tool that encodes a mathematical relationship between multiple variables as a set of parallel scales arranged so that a straight line (called an isopleth or index line) drawn across the scales simultaneously satisfies the encoded equation. Nomograms were historically used before electronic calculators as rapid analog computation devices. Today they are widely used in clinical medicine (scoring systems for disease risk or treatment outcomes), where a clinician draws a line across predictor scales to read a predicted probability directly from an output scale.

## When to Use
- Clinical risk scoring: presenting a multivariable regression model as an interactive visual calculator for bedside use
- Engineering and scientific contexts where rapid, repeated calculation from a fixed equation is needed
- Communicating a calibrated model's predictions to practitioners who need to apply it without software
- Displaying the contribution of each predictor variable to a final score on a common "Points" scale

## When NOT to Use
- When the audience has access to a digital calculator or tool — nomograms are analog substitutes
- When the underlying mathematical relationship is not a fixed formula (nomograms encode a specific equation)
- When more than ~7–8 predictor variables are present — the nomogram becomes too wide and cramped
- For exploratory analysis of relationships (use scatter matrix or correlation matrix instead)

## Data Requirements
- A calibrated multivariable model (regression, logistic regression, Cox model) with fixed coefficients
- Defined input variable ranges and units for each predictor
- A defined output variable (probability, score, predicted value)

## Best Practices
- Label each scale with the variable name and unit clearly
- Include a "Total Points" scale that aggregates individual predictor points
- Provide a worked example (sample patient or scenario) with the isopleth drawn in
- Document the underlying model and its derivation dataset in the chart caption
- Include a confidence interval or calibration plot alongside the nomogram to communicate uncertainty

## Common Mistakes
- A (forecast-anchoring): clinicians may anchor to a nomogram prediction even when the patient is outside the model's derivation population
- E (MC-noise-as-difference): the visual isopleth can imply precision that the underlying model does not support
- Omitting calibration information — a nomogram with poor model calibration can systematically mislead clinical decisions
- Using non-linear scales without clearly labelling the transformation


## Dashboard and other surfaces

status: placeholder

`Nomogram` is a valid analysis chart for a data scientist, researcher, R&D, or development notebook (matplotlib, pandas, or plotly). It is a poor primary mark for an executive, HR business-partner, or client page. Communication surface: retell the finding with parallel-coordinates, scatter-plot, decision-tree. `ibcs_status: conditional` applies to that communication surface only.

Suggested communication placement: **breakdown** zone. Vault coarse type, when a scraped template is the layout: **Number**. Pair it with a second view rather than leaving a lonely number. Analysis placement: a notebook cell or a pandas/matplotlib figure when the audience is technical. Subcategory dashboards that cite this chart are linked from `library/DASHBOARDS/`.

## Implementation Notes

### matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(14, 8))
axes_data = {
    'Age': (0, 100, 10),
    'Predictor B': (0, 50, 5),
    'Predictor C': (0, 10, 1),
    'Total Points': (0, 200, 20),
    'Predicted Prob': (0.01, 0.99, None)
}
x_positions = np.linspace(0, 1, len(axes_data))
for x_pos, (name, (lo, hi, step)) in zip(x_positions, axes_data.items()):
    ax.axvline(x=x_pos, color='black', linewidth=1)
    ax.text(x_pos, 1.02, name, ha='center', transform=ax.transAxes, fontsize=9)
    ticks = np.arange(lo, hi + (step or 1), step or 1)
    for tick in ticks:
        y = (tick - lo) / (hi - lo)
        ax.plot([x_pos - 0.01, x_pos + 0.01], [y, y], 'k-', linewidth=0.5)
        ax.text(x_pos + 0.015, y, f'{tick}', va='center', fontsize=7)
ax.axis('off')
plt.tight_layout()
```

### plotly
No native nomogram. Use `go.Scatter` with vertical line segments at fixed x-positions for each scale, and text annotations for tick labels.

### altair
No native nomogram support. Pre-compute all scale positions and render as layered `mark_rule` (vertical lines) + `mark_text` (tick labels).

### excel / tableau
Not supported natively. Nomograms are typically delivered as paper printouts, web applications, or PDF documents generated from dedicated statistical packages (e.g., R's `rms::nomogram()`).

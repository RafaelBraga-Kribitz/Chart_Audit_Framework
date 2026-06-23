---
name: Tag Cloud
category: Specialized
input_type: [cat-value]
it_variants: []
analytical_function: Concept-viz
visual_family: Chart
shape_primitive: [Icon]
cardinality_fit: [medium, large]
audience: [Executive, Public]
complexity: Basic
encoding_channels: [area, color-hue, color-value]
tool_support: [d3, matplotlib]
failure_modes: [G, J]
alternatives: [bar-chart, lollipop-chart]
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
# Tag Cloud

## Description
Also known as a Word Cloud. A Tag Cloud visualises a set of terms (tags, keywords, words) where the font size of each term is proportional to its frequency or importance. Terms are arranged in a compact layout, often centred. Colour can encode categories or a second variable. While visually engaging, word clouds are criticised by data visualisation practitioners for imprecise area encoding and sensitivity to word length (longer words appear larger regardless of frequency).

## When to Use
- Communicating the most prominent themes or keywords from a text corpus to a general audience
- Quick exploratory overview of term frequency in social media, survey responses, or documents
- Infographics and editorial contexts where aesthetic impact matters alongside data accuracy

## When NOT to Use
- When precise frequency comparison is required — use a bar chart
- Multi-word phrases that differ in character count but not importance
- When the bottom half of the frequency distribution matters — low-frequency words are tiny and visually suppressed (smell J)

## Data Requirements
| Column | Type | Notes |
|--------|------|-------|
| term | string | The word or phrase |
| frequency | numeric (≥0) | Font size is proportional to this |
| category | categorical (optional) | Colour encoding |

## Best Practices
- Remove stop words, punctuation, and irrelevant terms before generating
- Use a maximum of 50–100 terms; more creates visual noise
- Apply a square-root scale for font sizes to prevent the most frequent term from overwhelming the layout
- Prefer a horizontal layout (no rotated text) for readability

## Common Mistakes
- Font size driven by character length rather than frequency (cosmetic arrangement algorithm artefact) (smell G)
- Including stop words that are high-frequency but semantically meaningless
- Silently dropping low-frequency terms without communicating that the tail is truncated (smell J)
- Using word clouds for quantitative comparisons where a sorted bar chart is more accurate

## Implementation Notes

### matplotlib
```python
from wordcloud import WordCloud
wc = WordCloud(width=800, height=400, background_color='white',
               max_words=100, colormap='viridis')
wc.generate_from_frequencies(freq_dict)
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
```

### plotly
Not natively supported; use the `wordcloud` library and display as an image in Plotly.

### altair
Not natively supported.

### excel / tableau
Not natively available. Use dedicated tools: WordArt (Excel, aesthetic only), Power BI Word Cloud visual, or online generators.

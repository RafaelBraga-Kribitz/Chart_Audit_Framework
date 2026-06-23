# Retrieval Dimensions — Chart Library Tagging Schema

Every chart in the library is tagged across these 12 dimensions. The retrieval engine filters and ranks candidates by combining dimension tags. Load the relevant `_INDICES/` file for the dimension you're filtering on rather than scanning all chart files.

---

## Dimension 1: Data Input Type

The canonical data shape that the chart requires. Defined in `input-type-schema.md`.

**12 canonical IDs:**
- `xy-simple` — [numeric, numeric]
- `xy-dual-series` — [num/cat, num, num]
- `xyz-trivariate` — [num, num, num]
- `cat-value` — [categorical, numeric]
- `cat-multi-value` — [categorical, num, num...]
- `time-series` — [datetime, num...]
- `interval-range` — [cat, num, num] to [cat, num×4]
- `demo-grouped` — [cat, cat, num...]
- `composition` — [cat, num...] where rows sum to 100%
- `hierarchical-cat` — [num/ordered, cat, cat, cat...]
- `matrix-grid` — 2D grid: row-cat × col-cat → value
- `event-time` — [categorical, datetime]

**Granular variants:** IT001–IT040 (see `input-type-inventory.md`). These map to canonical IDs but encode additional structural constraints (e.g., IT017 = OHLC financial = interval-range).

---

## Dimension 2: Analytical Function

What question the chart is designed to answer.

| Value | Description |
|---|---|
| `Comparison` | Compare magnitudes across categories or entities |
| `Correlation` | Show relationship between two or more variables |
| `Distribution` | Show spread, shape, density of a variable |
| `Part-to-whole` | Show components as fractions of a total |
| `Trend-over-time` | Show change over time |
| `Geographical` | Show spatial/location-based patterns |
| `Flow` | Show movement between states or nodes |
| `Ranking` | Show ordered magnitude with identity |
| `Deviation` | Show departure from a reference or baseline |
| `Concept-viz` | Illustrate a concept, structure, or process (not data-driven) |

---

## Dimension 3: Visual Family

| Value | Examples |
|---|---|
| `Chart` | Bar, Line, Area, Pie |
| `Diagram` | Sankey, Chord, Network |
| `Plot` | Scatter, Box, Violin, Hex |
| `Map` | Choropleth, Dot-density, Flow-map |
| `Table` | Heatmap-table, Matrix |
| `Glyph` | Chernoff faces, Star plot, Radar |

---

## Dimension 4: Visual Shape Primitive

The primary geometric encoding. From datavizproject taxonomy.

`Area` | `Bar` | `Circle` | `Dot` | `Icon` | `Line` | `Polygon` | `Pyramid` | `Square`

---

## Dimension 5: Cardinality Fit

How many data points / categories the chart handles well.

| Value | Range |
|---|---|
| `small-N` | < 10 items |
| `medium` | 10–50 items |
| `large` | 50–500 items |
| `very-large` | 500+ items |

---

## Dimension 6: Audience

| Value | Description |
|---|---|
| `Executive` | Decision-maker, needs immediate takeaway, low tolerance for complexity |
| `Analytics` | Data analyst, comfortable with distributions and uncertainty |
| `Technical` | Engineer/scientist, can read code-style output, residuals, etc. |
| `Public` | General audience, needs accessible design and minimal jargon |

---

## Dimension 7: Complexity

| Value | Description |
|---|---|
| `Basic` | Standard chart type, widely understood, minimal cognitive load |
| `Intermediate` | Requires some data literacy (e.g., box plot, violin, ECDF) |
| `Advanced` | Requires domain or statistical expertise (e.g., Sankey, alluvial, hexbin) |

---

## Dimension 8: Encoding Channels Used

Which perceptual channels the chart employs for data encoding.

`position` | `length` | `angle` | `area` | `color-hue` | `color-value` | `shape` | `texture` | `motion`

Note: Charts using `area` or `angle` as primary encodings (pie, bubble) are harder to read accurately than `position` or `length`. Flag in Best Practices section of each chart file.

---

## Dimension 9: Tool Support

Which tools have implementation notes in this chart's library entry.

`matplotlib` | `plotly` | `altair` | `d3` | `tableau` | `powerbi` | `excel`

Each tool gets an `implementations.<tool>.status` field in front-matter:
- `stub` — field exists but no implementation notes yet
- `verified` — working implementation from a real project has been generalized into this entry

---

## Dimension 10: Known Failure Modes

Links to code smell IDs from `references/code-smells.md` that commonly appear with this chart type.

Examples:
- Bar chart → smells D (index-ordered ranking), J (silently dropped categories)
- KDE plot → smell G (point masses)
- Stacked chart → smell I (mutually exclusive scenarios)
- Scatter with ratio → smell K (self-correlation)
- Choropleth → smell F (bounding-box geometry)

---

## Dimension 11: Alternatives & Co-Charts

Charts to suggest when this type is Gate C–rejected or when the user needs a follow-up view. Stored as wikilinks to adjacent library entries.

Format in front-matter:
```yaml
alternatives:
  - name: ECDF Plot
    improves: Shows distribution with atoms cleanly; no KDE bandwidth artifacts
    fixes_smell: G
  - name: Dot Plot with Error Bars
    improves: Ranks near-equal values without false precision
    fixes_smell: D
```

---

## Dimension 12: Source Provenance

Which reference sites document this chart type. Enables tracing description accuracy.

| Value | Site |
|---|---|
| `datavizproject` | datavizproject.com (166 entries, primary source) |
| `datavizcatalogue` | datavizcatalogue.com/methods/ (61 entries) |
| `data-to-viz` | data-to-viz.com/graph/ (68 entries) |
| `depictdatastudio` | depictdatastudio.com/charts/ (39 entries) |
| `chartmaker` | chartmaker.visualisingdata.com |

---

## Retrieval Priority Rules

When multiple candidates match, rank by:

1. **Input type match** (exact match > parent canonical match)
2. **Analytical function match** (exact match required for top-3)
3. **Audience complexity fit** (don't suggest Advanced for Executive)
4. **Cardinality fit** (penalize charts that break at the dataset's N)
5. **Tool support status** (prefer `verified` over `stub` when tool is known)
6. **Failure mode count** (all else equal, prefer charts with fewer applicable smells)

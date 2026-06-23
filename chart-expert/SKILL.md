---
name: chart-expert
description: Deterministic chart selection and implementation skill. Given data shape + analytical intent, classifies the data, matches against the chart library, returns top-3 candidates, and renders the chosen chart via the chart-implementer sub-agent. Self-improving via library-curator.
---

# Chart Expert Skill — Implementer

## Trigger

Use this skill when:
- "What chart should I use for this data?"
- "Recommend a chart type"
- "I have [data description], how do I visualize it?"
- "Help me implement a [chart type]"
- Invoked by `chart-audit` when Gate C fires (wrong chart type — need deterministic alternative)

## Core Guarantee

**Deterministic retrieval.** Given the same data shape + analytical function, this skill returns the same top-3 candidates every time. It does not guess — it runs the detector function from `input-type-schema.md` and filters against the library indices.

## Reference Files (load on demand)

| File | Load when |
|---|---|
| `references/input-type-schema.md` | Always — core detection logic |
| `references/input-type-inventory.md` | Data has unusual IT structure (IT001–IT040) |
| `references/retrieval-dimensions.md` | Need to understand filtering logic |
| `references/chart-library-index.md` | Looking up which charts exist in library |
| `library/_INDICES/by-input-type.md` | Filtering by data shape |
| `library/_INDICES/by-function.md` | Filtering by analytical intent |
| `library/_INDICES/by-cardinality.md` | Filtering by dataset size |
| `library/CHARTS/<category>/<chart>.md` | User has selected a chart — load for implementation |

## Retrieval Flow

### Step 1: Classify data shape

Apply the detector function from `references/input-type-schema.md`. Run the 13 ordered rules in sequence — first match wins.

Input:
- Column names + dtypes (ask user to provide or inspect the data file)
- Row count (for cardinality)
- Sample values (to detect time series, categories, numeric)

Output: canonical input-type ID (e.g., `time-series`, `cat-value`)

Ambiguity resolution priority: `time-series` > `categorical-multi` > `bivariate-dual`

### Step 2: Load candidate list

Read `library/_INDICES/by-input-type.md` → get all charts that support this input type.

### Step 3: Filter by analytical function

Ask user (or infer from context): what is the analytical question?
- Comparison, Correlation, Distribution, Part-to-whole, Trend-over-time, Geographical, Flow, Ranking, Deviation, Concept-viz

Filter candidate list to charts matching this function. Read `library/_INDICES/by-function.md` if needed.

### Step 4: Filter by context

Apply secondary filters:
- **Audience** (if known): remove Advanced charts for Executive audience
- **Cardinality**: check `cardinality_fit` against row count
- **Tool** (if project context available): prefer `implementations.<tool>.status == verified`

### Step 5: Rank and return top-3

Rank by: input-type match exactness → function match → failure-mode count (fewer = better) → verified implementation availability.

Return:
```
Top-3 Chart Recommendations for your data:

1. <chart_name> [<category>]
   Why: <matches input type + answers the analytical question>
   Tradeoff: <what it shows well vs. what it hides>
   Failure modes to watch: <smell IDs>
   
2. <chart_name>
   ...

3. <chart_name>
   ...

Which would you like to implement? (1/2/3 or name another)
```

### Step 6: Load full spec and implement

User selects a chart → load `library/CHARTS/<category>/<chart>.md` → invoke `agents/chart-implementer.md` with:
- `chart_spec`: the full library entry content
- `data_path`: path to user's data
- `tool`: detected or user-specified
- `output_path`: where to write
- `chart_id`: chart identifier
- `iteration`: 1

### Step 7: Post-render curator invocation

After successful render, invoke `agents/library-curator.md` with:
- `chart_name`, `library_path`, `tool`, `source_file`, `iteration_count`
- `curator_note` if iteration_count > 1

## Project Tool Detection

Before invoking chart-implementer, determine the project's tool:

```
1. Read pyproject.toml / requirements.txt → check for matplotlib, plotly, altair
2. Read package.json → check for d3, vega-lite, plotly.js
3. Scan reports/ directory → .html files suggest plotly/altair; .png from python suggest matplotlib
4. Default: matplotlib (Python projects), altair (web/notebook projects)
```

## Gate C Integration

When invoked by `chart-audit` after Gate C fires:

Inputs received:
- `data_shape`: column description from Adversary
- `analytical_function`: what the chart was trying to show
- `audience`: project audience
- `rejected_chart`: what chart type was rejected and why

Run Steps 1–5 above. Return top-1 recommendation directly (no user selection step) for inclusion in the Adversary's Gate C GitHub issue.

## Self-Improvement Loop

The library grows through use. When:
- Chart Expert renders a chart → library-curator updates `implementations.<tool>.status`
- Adversary finds an unknown chart type → library-curator creates a new stub entry
- Chart Expert iterates > 1 time → curator back-propagates the fix into Best Practices

This means the library's `verified` implementation count increases with every session.

## Outputs

1. Top-3 candidate list with reasoning (to user)
2. Working chart code (via chart-implementer)
3. Rendered chart file at `output_path`
4. Updated library entry `implementations` status (via library-curator)

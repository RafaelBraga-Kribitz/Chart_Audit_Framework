# Data Input Types: Integration Guide

**Quick start for Rafael's chart catalogue system.**

---

## Files Created

1. **DataInputTypes_Catalogue.md** → Visual + Human-Readable
   - 12 data input types with visual examples
   - Shorthand tags (#xy-simple, #time-series, etc.)
   - Chart recommendations for each type
   - Quick reference table

2. **DataInputTypes_Schema.md** → Machine-Readable
   - Complete JSON schema for all types
   - Detector logic (for Claude skill)
   - Pseudo-code implementation
   - Chart capability matrix

3. **ChartCatalogue_Template.md** → Obsidian Structure
   - 5 template examples (Line, Bar, Heatmap, Bubble, Matrix)
   - Front matter structure for each chart
   - File organization strategy
   - DataView queries for indexing

---

## Workflow: How This System Works

### For You (Human)

```
Step 1: Add a chart to your vault
└─ Use ChartCatalogue_Template.md as starting point

Step 2: Identify its data input type
└─ Reference DataInputTypes_Catalogue.md
└─ Match your data to a signature (e.g., [numeric, numeric] = xy-simple)

Step 3: Tag it with the shorthand
└─ Add to front matter: tags: [time-series, line-chart, sales]

Step 4: Link it to the catalogue
└─ Use Obsidian wikilinks: [[time-series]]

Step 5: Build your index
└─ Use DataView queries to auto-organize by type or chart
```

### For Claude Skill (Automatic)

```
Input: Raw dataset (CSV, JSON, DataFrame)
  ↓
Step 1: Detector Function
  └─ Count columns, infer types, sample values
  ↓
Step 2: Match to Signature
  └─ Use decision_tree from DataInputTypes_Schema.md
  └─ Example: 2 cols, both numeric → "bivariate-simple"
  ↓
Step 3: Return Primary Charts
  └─ Look up in charts.primary array
  └─ Example: ["line", "scatter", "area"]
  ↓
Output: Recommended chart type + Obsidian link to example
```

---

## Implementation: Setup Your Obsidian Vault

### Directory Structure

```
YOUR_VAULT/
├── CHARTS/
│   ├── _REFERENCE/
│   │   ├── DataInputTypes_Catalogue.md      ← Copy here
│   │   ├── DataInputTypes_Schema.md         ← Copy here
│   │   └── ChartCatalogue_Template.md       ← Copy here
│   │
│   ├── TIME_SERIES/
│   │   ├── Sales Trend.md                   ← Use template
│   │   ├── Traffic Pattern.md
│   │   └── Stock Performance.md
│   │
│   ├── CATEGORICAL/
│   │   ├── Product Mix.md
│   │   ├── Regional Sales.md
│   │   └── Market Share.md
│   │
│   ├── DISTRIBUTION/
│   │   ├── Demographics.md
│   │   ├── Customer Segments.md
│   │   └── Age Distribution.md
│   │
│   ├── RELATIONSHIP/
│   │   ├── Risk-Return.md
│   │   ├── Correlation Matrix.md
│   │   └── Scatter Analysis.md
│   │
│   └── _INDEX/
│       ├── By Data Type.md
│       ├── By Chart Type.md
│       └── By Use Case.md
```

### Copy These Files Into Obsidian

```bash
# From terminal (if you're syncing):
cp DataInputTypes_Catalogue.md ~/Obsidian/Vault/CHARTS/_REFERENCE/
cp DataInputTypes_Schema.md ~/Obsidian/Vault/CHARTS/_REFERENCE/
cp ChartCatalogue_Template.md ~/Obsidian/Vault/CHARTS/_REFERENCE/
```

Or drag-and-drop into Obsidian.

---

## Usage Examples

### Example 1: You Find a Chart in the Wild

**You see:** A line chart showing monthly revenue

**You do:**
1. Open ChartCatalogue_Template.md → Example 1
2. Copy structure (keep front matter format)
3. Fill in your data example
4. Check DataInputTypes_Catalogue.md → time-series
5. Add tags: `[time-series, line-chart, revenue, trend-analysis]`
6. Save as: `CHARTS/TIME_SERIES/Monthly Revenue.md`

**Result:** Chartable in your vault, tagged, searchable, linked to system

---

### Example 2: You Want to Build a Skill

**You need:** Auto-suggest the right chart for a dataset

**You do:**
1. Read DataInputTypes_Schema.md → detector_function section
2. Extract the JSON into your Claude skill prompt
3. Implement the decision tree in your skill
4. When given data, run detector → match to type → return primary charts
5. Include Obsidian link: `[[xy-simple]]` for user to see example

**Result:** Skill can deterministically choose charts based on data shape

---

### Example 3: You Want to Find All Time Series Charts

**In Obsidian:**
```
Type in search bar: tag:#time-series
```

**Or use a DataView query in an index file:**
```
LIST WHERE contains(tags, "time-series")
SORT BY title ASC
```

**Result:** All time-series charts in one view, filterable by chart type, use case, etc.

---

## Shorthand Tags Quick Reference

Copy-paste these into your chart front matter:

```yaml
# Pick the data input type that matches your data:
tags: [
  #xy-simple              # 2 numeric columns
  #xy-dual-series         # 3 columns: cat/num, num, num
  #xyz-trivariate         # 3 numeric columns
  #cat-value              # category + value
  #cat-multi-value        # category + 2+ numeric
  #time-series            # date + value(s)
  #interval-range         # bounds or OHLC
  #demo-grouped           # age/region + F/M + numeric
  #composition            # parts sum to 100%
  #hierarchical-cat       # 3+ categorical levels
  #matrix-grid            # 2D grid structure
  #event-time             # event + timestamp
]

# Then add 1-2 chart type tags:
# line-chart, bar-chart, pie-chart, scatter-chart, heatmap, bubble-chart,
# stacked-bar, area-chart, treemap, sunburst, candlestick, etc.

# Then any domain tags:
# sales, marketing, finance, operations, analytics, customer-data, etc.
```

---

## Minimal Example: Your First Chart

**Create file:** `CHARTS/TIME_SERIES/First Example.md`

```markdown
---
title: My First Charted Data
chart_type: Line Chart
data_input_type: time-series
tags: [time-series, line-chart]
created: 2026-06-23
---

# My First Charted Data

## Data Structure
**Input Type:** [[time-series]]  
**Shorthand:** `#time-series`

Data format:
```
| Date   | Value |
|--------|-------|
| 1-1-25 | 100   |
| 2-1-25 | 120   |
| 3-1-25 | 115   |
```

## Why This Chart Type
- Shows change over time
- Good for identifying trends

## Tools
- Excel, Tableau, Power BI, etc.

## Related
- [[xy-simple|Simple Scatter]] (if no time ordering)
```

**Done.** Now it's in your system, tagged, findable, and linked to the catalogue.

---

## Claude Skill: Pseudo-Implementation

If you want to create a skill that auto-selects charts:

```python
# In your skill prompt or code:

# 1. Include this JSON from DataInputTypes_Schema.md
data_input_types = [...]  # Full JSON structure

# 2. Implement detector function
def detect_data_type(data):
    col_count = len(data.columns)
    col_types = [infer_type(col) for col in data.columns]
    
    # Use detector_function logic from schema
    if col_count == 2 and all(t == 'numeric' for t in col_types):
        return "bivariate-simple"
    # ... more rules

# 3. Return chart recommendation
def suggest_chart(data):
    data_type = detect_data_type(data)
    chart_entry = find_in_schema(data_type)
    return chart_entry['charts']['primary']

# 4. In skill output, include Obsidian link
output = f"Recommended: {chart} [[{data_type}|See example]]"
```

---

## Integration with Your BRAGA Portfolio

**These files support:**

- **Portfolio project ideas:** Each data shape suggests different project angles
- **LLM automation:** Skill can deterministically suggest charts (no human vagueness)
- **Reusability:** Template structure works across Austrian market data, ski tourism data, retail data, etc.
- **Obsidian as source of truth:** Charts tagged and linked = queryable knowledge base

---

## Next Steps

1. **Copy the 3 files into Obsidian** under `CHARTS/_REFERENCE/`
2. **Create your first chart file** using the template
3. **Tag it with shorthand** from the catalogue
4. **Build an index** using DataView queries
5. **Reference when building skills** that choose charts

---

## Debugging: If Detection Fails

If the skill can't auto-detect your data:

1. Check column count and types
2. Cross-reference to the decision tree in DataInputTypes_Schema.md
3. If ambiguous (e.g., could be `time-series` OR `categorical-multi`), check for:
   - Temporal columns → time-series wins
   - Categorical first column → categorical-multi wins
4. If still unclear, append note to schema with your example

---

## Version Info

| File | Purpose | Status |
|------|---------|--------|
| DataInputTypes_Catalogue.md | Visual reference for 12 data types | Ready |
| DataInputTypes_Schema.md | Machine-readable spec + detector | Ready |
| ChartCatalogue_Template.md | Obsidian template + examples | Ready |

**All files ready to copy into Obsidian immediately.**

---

## Questions?

When implementing the skill:
- Refer to `detector_function` in DataInputTypes_Schema.md for detection logic
- Refer to `chart_capabilities` matrix for reverse lookups (which types can use which chart)
- Use pseudo-code as starting point; adapt to your implementation language

**System is designed to be:**
- ✓ Human-readable (use Catalogue.md)
- ✓ Machine-parseable (use Schema.md)
- ✓ Obsidian-native (use Template.md)
- ✓ Deterministic (no ambiguity in matching)

---

**Ready to start.** Copy files, tag charts, build skill.

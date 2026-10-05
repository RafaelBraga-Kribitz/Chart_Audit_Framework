# IBCS SUCCESS (working rules)

These are original working rules for this library, aligned to the seven SUCCESS rule groups of the International Business Communication Standards (IBCS), published by the IBCS Association (ibcs.com). They are not the text of the standard. Chart cards carry `ibcs_status`; `library/_INDICES/by-ibcs.md` lists the charts by status.

SUCCESS: **S**ay, **U**nify, **C**ondense, **C**heck, **E**xpress, **S**implify, **S**tructure.

## Say: convey a message

The title is a message, not a topic. "Margin missed the quote by 3 points" is a title. "Margin overview" is a label. State the objective of the page before adding charts. Introduce the comparison, deliver the evidence, support it with the breakdown, and end with the implication.

## Unify: apply semantic notation

One term per measure, the same term as the KPI card. One format for dates, units, and variances. Scenarios have stable meanings and stable visual treatment across pages: actual (AC) is the solid series, previous year (PY) and plan (PL) are references, forecast (FC) is visually distinct from actual. Color is not a second rainbow for categories that are already labeled.

## Condense: increase information density

Prefer small multiples, overlays of actual and plan, and sparklines inside a variance table to a stack of single-number tiles. A lonely number needs a comparison. Embed the trend in the row when the row is the entity (a project, a customer, a rep).

## Check: ensure visual integrity

Axes start at zero when length encodes magnitude. Scales that compare are shared. Do not crop a bar axis. Label omissions. If a component is missing, say so. Adjustments (currency, restatement, partial period) are written next to the title, not hidden in a footnote no one opens.

## Express: choose a proper visualization

Use the chart that encodes the comparison:

- Time: line, column only when the periods are few.
- Rank: bar, sorted.
- Part-to-whole: stacked column or bar, or a table of shares.
- Deviation: bar diverging from a baseline, bullet, waterfall.
- Distribution: dots, box, histogram.
- Correlation: scatter.

Replace, for management communication: gauges, radar charts, pie and donut charts, spaghetti lines, and traffic-light tiles used as the only encoding. Those types remain in the chart library with `ibcs_status: avoid` so an agent can recognize them and refuse them for this job. Tables carry precise values. Charts carry patterns.

## Simplify: avoid clutter

Remove gridlines, shadows, 3D, and legends that repeat direct labels. A marker must encode data or it goes. Whitespace is structure, not a theme.

## Structure: organize content

One page, one question. Sections are mutually exclusive and together cover the question. Put the score and the message first, then the trend, then the breakdown, then the detail a person can act on. Do not make the reader discover the structure.

## Status values on chart cards

- `preferred`: the chart can carry a management comparison without a warning.
- `conditional`: usable when the audience knows the encoding, or when a warning is attached (dual axis, horizon mirroring, radial layouts, area as the only magnitude encoding).
- `avoid`: removed from Executive, Public, and client communication surfaces (dashboard, report, story). It stays eligible on Analytics and Technical analysis surfaces (notebook, exploratory plot), and when the user is studying the chart type itself.

# IBCS SUCCESS (working rules)

These are original working rules for this library, aligned to the SUCCESS structure of the International Business Communication Standards. They are not the text of the standard. The local source PDF and OCR live at `C:/Users/Benutzer1/Dev/dashboard-library/ibcs-v2`. Chart cards point here with `ibcs_status`.

## Say

The title is a message, not a topic. "Margin missed the quote by 3 points" is a title. "Margin overview" is a label. State the objective of the page before adding charts. Introduce the comparison, deliver the evidence, support it with the breakdown, and end with the implication.

## Structure

One page, one question. Sections are mutually exclusive and together cover the question. Put the score and the message first, then the trend, then the breakdown, then the detail a person can act on. Do not make the reader discover the structure.

## Express

Use the chart that encodes the comparison:

- Time: line, column only when the periods are few.
- Rank: bar, sorted.
- Part-to-whole: stacked column or bar, or a table of shares.
- Deviation: bar diverging from a baseline, bullet, waterfall.
- Distribution: dots, box, histogram.
- Correlation: scatter.

Replace, for management communication: gauges, radar charts, pie and donut charts, spaghetti lines, and traffic-light tiles used as the only encoding. Those types remain in the chart library with `ibcs_status: avoid` so an agent can recognize them and refuse them for this job. Tables carry precise values. Charts carry patterns.

## Condense

Prefer small multiples, overlays of actual and plan, and sparklines inside a variance table to a stack of single-number tiles. A lonely number needs a comparison. Embed the trend in the row when the row is the entity (a project, a customer, a rep).

## Check

Axes start at zero when length encodes magnitude. Scales that compare are shared. Do not crop a bar axis. Label omissions. If a component is missing, say so. Adjustments (currency, restatement, partial period) are written next to the title, not hidden in a footnote no one opens.

## Unify

One term per measure, the same term as the KPI card. One format for dates, units, and variances. Actual, plan, and forecast have stable meanings and stable visual treatment across pages: actual is the solid series, plan is the reference, forecast is visually distinct from both. Color is not a second rainbow for categories that are already labeled.

## Simplify

Remove gridlines, shadows, 3D, and legends that repeat direct labels. A marker must encode data or it goes. Whitespace is structure, not a theme.

## Status values on chart cards

- `preferred`: the chart can carry a management comparison without a warning.
- `conditional`: usable when the audience knows the encoding, or when a warning is attached (dual axis, horizon mirroring, area as the only magnitude encoding).
- `avoid`: do not recommend for executive or client reporting. Still available when the user is studying the chart type itself.

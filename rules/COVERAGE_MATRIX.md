# Rule coverage matrix

One row per code smell (13) and hard gate (4). Enforcement:
`detector-backed` = deterministic signature in `detectors_spec.md`;
`llm-judged-only` = judged by the chart-adversary agent against the source
prose, bounded by `scoring-anchors.md`.

| ID | Name | Enforcement | Manifest ref |
|---|---|---|---|
| SMELL-A | "Forecast" that lands exactly on the known outcome | llm-judged-only | rules/manifest.yaml#SMELL-A |
| SMELL-B | "Distribution" that is a flat line / zero variance across groups | detector-backed | rules/manifest.yaml#SMELL-B |
| SMELL-C | Percentile interval mislabeled as "HDI" (and inconsistent levels) | detector-backed | rules/manifest.yaml#SMELL-C |
| SMELL-D | Ranked categories whose order is an array index, not a magnitude | llm-judged-only | rules/manifest.yaml#SMELL-D |
| SMELL-E | Quantity within MC/sampling noise presented as a difference | llm-judged-only | rules/manifest.yaml#SMELL-E |
| SMELL-F | Map that renders as a near-uniform block / overlapping boxes | llm-judged-only | rules/manifest.yaml#SMELL-F |
| SMELL-G | KDE / density spikes of arbitrary height | llm-judged-only | rules/manifest.yaml#SMELL-G |
| SMELL-H | Utilisation pinned at exactly 1.00; "expected" exceeds the cap | llm-judged-only | rules/manifest.yaml#SMELL-H |
| SMELL-I | Stacked area/bars of mutually exclusive scenarios | llm-judged-only | rules/manifest.yaml#SMELL-I |
| SMELL-J | Silently dropped categories | detector-backed | rules/manifest.yaml#SMELL-J |
| SMELL-K | Self-correlated scatter (ratio vs its own component) | llm-judged-only | rules/manifest.yaml#SMELL-K |
| SMELL-L | Suspiciously smooth / symmetric series | llm-judged-only | rules/manifest.yaml#SMELL-L |
| SMELL-M | Cross-artifact contradiction | llm-judged-only | rules/manifest.yaml#SMELL-M |
| GATE-A | Question Validity | llm-judged-only | rules/manifest.yaml#GATE-A |
| GATE-B | Analytical Logic | llm-judged-only | rules/manifest.yaml#GATE-B |
| GATE-C | Chart Type | llm-judged-only | rules/manifest.yaml#GATE-C |
| GATE-D | Data/Plot Integrity | llm-judged-only | rules/manifest.yaml#GATE-D |

Detector-backed today: 3 of 13 smells (B, C, J). Future detector candidates
flagged in the manifest rationale fields: E, G, H, K.

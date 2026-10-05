---
id: dash.healthcare.veterinary-medicine
type: dashboard
status: placeholder
category: Healthcare
subcategory: Veterinary Medicine
context: organizational
audiences: [Executive, Data Analytics, Researcher, R&D]
---

# Healthcare / Veterinary Medicine

This card is a specification, not a claim that a live executive dashboard exists.

## Questions

- Are the few outcomes in Veterinary Medicine on the right side of their targets?
- Which input moved, and is that a signal or a tail?

## Audiences and surfaces

- Communication (executive, client, HR business partner): dashboard or report. Use each KPI's communication chart.
- Analysis (data scientist, researcher, R&D, marketing analytics, development): notebook or pandas/matplotlib plot. Use each KPI's analysis chart. Do not paste that figure onto the executive page unchanged.

## Zones (communication)

| Zone | What goes here |
|---|---|
| Score | Big number or bullet versus target for the OMTM of this subcategory |
| Trend | Line of that KPI |
| Breakdown | Sorted bar of the entities |
| Variance | Waterfall or diverging bar versus plan |
| Detail | Data table of the rows a person can act on |

## KPIs

- `kpi.healthcare.animal-sterilizations` Animal sterilizations. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.veterinary-visits-per-household` Veterinary visits per household. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.s-veterinary-expenses-per-pet-household` S Veterinary expenses per pet household. Communication `horizontal-bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.household-shots-own-a-pet` Household shots own a pet. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.compound-means-pet-registered-to-a-veterinarian` Compound means pet registered to a veterinarian. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.companion-pets-owned` Companion pets owned. Communication `bar-chart`. Analysis `bar-chart`.
- `kpi.healthcare.dagger-resusable-medical-devices-properly-decontaminated` \( \dagger \)Resusable medical devices properly decontaminated. Communication `bar-chart`. Analysis `bar-chart`.

## Vault templates

- None matched. Placeholder layout above is the suggestion. Data sources: the system of record for this subcategory (ledger, CRM, product analytics, or survey).

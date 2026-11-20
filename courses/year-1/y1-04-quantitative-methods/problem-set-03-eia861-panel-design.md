# Y1-04 Problem Set 3 — EIA-861 Measurement, Panel Data, and Causal Identification

**Estimated time:** 4–5 hours  
**Companion protocol:** [EIA-861 Research Design](../../../research/data-pipelines/eia861/research-design.md)  
**Data source:** [EIA Form 861 annual detailed files](https://www.eia.gov/electricity/data/eia861/)

This assignment evaluates measurement and identification. It does not assume that a balanced panel exists or that a causal policy effect can be estimated.

## Problem 1 — Survey architecture and measurement

EIA-861 and EIA-861S collect annual information from electric utilities. The schedules have different geographic levels and historical changes.

1. Explain the difference between a utility-year observation and a state-sector-year aggregate.
2. Explain why the presence of an EIA utility ID in one 2025 worksheet does not establish historical coverage.
3. Identify two implications of the 2016 non-net-metered distributed-generation schedule changes and the 2020 expansion of EIA-861S imputation.
4. Explain why blank energy-sold-back fields cannot be coded as zero exports without examining the source instructions.

## Problem 2 — Cumulative stock and annual flow

Suppose a comparable utility-level PV installation series reports 8,000 installations in year t and 10,500 in year t+1.

1. Calculate the change in cumulative installations.
2. Explain when this first difference can be interpreted as net additions.
3. Give at least three reasons a negative first difference might occur without physical DER retirement.
4. Explain why installation count and MW capacity should be analyzed separately.

## Problem 3 — Missingness and unbalanced panels

The historical coverage audit finds utility-level PPL observations in only some years and some schedules.

1. Distinguish missing-at-random, missing-completely-at-random, and missing-not-at-random mechanisms.
2. Explain why listwise deletion or linear interpolation may be inappropriate.
3. Design a coverage table that reports schedule, year, respondent form, utility ID, and missingness reason.
4. State the minimum evidence needed before combining two years into a time series.

## Problem 4 — Difference-in-differences critique

A researcher proposes estimating the effect of PPL's Second DER Management Plan by comparing PPL's net-metered PV capacity before and after approval with the statewide Pennsylvania series.

1. Define treatment and control in the proposed design.
2. Explain why a statewide series that includes PPL is not an independent control group.
3. List the identifying assumptions required for a difference-in-differences interpretation.
4. Explain why projected hosting-capacity benefits are not a realized treatment outcome.
5. Propose a better comparison design, or explain why no causal estimate is currently justified.

## Problem 5 — Research decision memo

Write a 1,000–1,500 word memo that recommends one of the following:
- a PPL utility-year descriptive series;
- a multi-utility panel;
- a state-level comparative descriptive analysis;
- a qualitative regulatory case study with no quantitative outcome model.

Your recommendation must be conditional on the actual coverage audit. Include a data dictionary, a missingness analysis, a graph design, a causal-identification assessment, and a clear statement of what the data cannot establish about feeder hosting capacity or interconnection performance.

## Submission

- EIA schedule coverage matrix.
- Variable-definition and source-provenance table.
- Reproducible calculations for Problem 2.
- Research decision memo.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Survey architecture and source discipline | 20% |
| Measurement and stock/flow reasoning | 20% |
| Missing-data and panel design | 20% |
| Causal identification and counterfactual reasoning | 25% |
| Limitations and communication | 15% |

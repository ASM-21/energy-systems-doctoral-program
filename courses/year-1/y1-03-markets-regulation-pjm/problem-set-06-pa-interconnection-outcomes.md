# Problem Set 6 — Pennsylvania DER Interconnection Outcomes: Measurement, Peer Comparison, and Policy Evaluation

**Level:** Graduate / doctoral preparation  
**Estimated effort:** 4–6 hours  
**Data:** Pennsylvania PUC, *Net-Metering and Interconnection Report 2023–2025*; structured extracts linked below.  
**Research boundary:** Public-source analysis only. Do not use employer-confidential procedures, internal queue records, customer data, or nonpublic work product.

## Learning objectives

By completing this assignment, you should be able to:
1. Reconstruct utility-level interconnection request trends from a regulator's aggregate report.
2. Distinguish stocks, flows, review-level counts, approval-time statistics, and status categories.
3. Detect and document source-table reconciliation failures.
4. Explain why an annual aggregate panel does not identify the effect of a tariff or DER management program.
5. Specify the minimum data needed for a defensible follow-up study.

## Source packet

- PUC report: [Net-Metering and Interconnection Report 2023–2025](https://www.puc.pa.gov/media/3770/net-metering-interconnection-report-2023-2025_final.pdf).
- [All-EDC request-count and mean-time extract](../../../research/casebooks/pa-der-interconnection/pa_edc_interconnection_2023_2025.csv).
- [PPL detailed metric and status extract](../../../research/casebooks/pa-der-interconnection/ppl_interconnection_2023_2025.csv).
- [Research note and measurement caveats](../../../research/casebooks/pa-der-interconnection/puc-interconnection-report-2023-2025.md).

The report's reporting year runs from June 1 through May 31. The 2025 reporting year therefore covers June 1, 2024 through May 31, 2025.

## Part A — Reconstruct the PPL request series

Using Tables 4A–4C, produce a table with PPL request counts by review level for 2023, 2024, and 2025. Confirm that the review-level counts sum to the reported PPL total in each year.

1. Calculate the percentage change in PPL total requests from 2023 to 2025.
2. Calculate PPL's share of statewide requests in each reporting year.
3. Rank PPL among the 11 EDC service territories by total request volume for each year.
4. Explain why the annual request count is a flow measure, while customer-generators and interconnected nameplate capacity are stock measures.

## Part B — Compare the 2025 large-project request mix

The 2025 report splits Levels 2–4 at 500 kW. For PPL, calculate:
1. The share of statewide Level 2 requests at or above 500 kW.
2. The share of statewide Level 3 requests at or above 500 kW.
3. The share of PPL's total requests represented by its Level 3 requests at or above 500 kW.

Explain why the 2025 size-band split cannot be backfilled into the 2023–2024 tables without source-level data. Also explain why a request that moves between review levels should not be treated as a fixed project characteristic.

4. Compare the PUC report's two descriptions of Level 3 eligibility with 52 Pa. Code §§ 75.34(3) and 75.39(a). Identify the capacity-threshold inconsistency and explain why the table's review-level labels do not resolve it. Cite the exact statutory subsections.

## Part C — Interpret stocks, flows, and approval times

For PPL, calculate the 2023–2025 percentage change in:
- customer-generators;
- total interconnected nameplate capacity;
- annual interconnection requests.

Then examine the reported mean Level 1 approval time (1, 1, and 10 days in 2023, 2024, and 2025).

1. State what the three-year movement does and does not establish.
2. Explain why requests received in a reporting year and approvals completed in that reporting year may be different cohorts.
3. Explain why the mean-time zeroes in some size/review cells must not automatically be interpreted as zero-day reviews.

## Part D — Audit the 2025 status table

For the 2025 PPL row, the report lists:
- submitted: 6,844;
- reported completed: 6,487;
- approved: 5,043;
- denied: 0;
- cancelled by customer: 852;
- pending customer action: 0;
- pending EDC action: 592.

1. Sum the listed status categories.
2. Compare that sum with submitted requests.
3. Compare reported completed with approved + denied + cancelled.
4. Compare the same arithmetic for 2023 and 2024.
5. Write a short data-quality note specifying exactly what needs clarification before calculating completion rates.

Do not impute the difference or silently redefine a status field.

## Part E — Policy timing and causal identification

PPL Rule 12's new applicability date is January 3, 2026. PPL states that implementation of its Second DER Management Program began January 5, 2026.

1. Explain why the 2023–2025 PUC report is a pre-implementation baseline for these milestones.
2. Identify the exposure problem in the next reporting year, June 1, 2025–May 31, 2026.
3. Propose a credible descriptive follow-up design.
4. Assess whether the available three-year detailed PUC tables support a causal claim about Rule 12 or DERMS. State the missing identification assumptions and evidence.

## Part F — Design a defensible data request

Specify a minimum application-level data dictionary that would allow an independent researcher to distinguish:
- time in applicant action;
- time in utility action;
- review-level changes;
- study and upgrade requirements;
- approval, denial, cancellation, and permission-to-operate outcomes;
- exposure to tariff and DERMS changes.

At minimum, define an anonymized application key, received date, completeness date, review start/end dates, review level history, capacity, EDC service territory, status history, applicant-action intervals, utility-action intervals, upgrade indicators, and applicable tariff/program version.

Explain which fields could be released in aggregated public form without exposing customer or commercially sensitive information. If the records are not public, identify the appropriate regulatory filing or records process; do not attempt to obtain internal employer data.

## Submission

Submit:
- one reproducible CSV or notebook with all calculations;
- two figures (EDC request totals by year; PPL review-level composition);
- a 1,000–1,500 word methods memo;
- a one-page data dictionary and data-quality register.

Every calculated figure must identify its denominator, reporting period, source table, and whether it is a stock, flow, or duration statistic.

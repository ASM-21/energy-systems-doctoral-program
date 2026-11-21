# Problem Set 6 — Worked Solution Notes

These notes give a defensible calculation path and identify where the source does not support a stronger inference. Small rounding differences are acceptable.

## Part A — PPL request series

| Reporting year | Level 1 | Level 2 | Level 3 | Level 4 | Total |
|---|---:|---:|---:|---:|---:|
| 2023 | 4,698 | 2,854 | 15 | 0 | 7,567 |
| 2024 | 4,732 | 2,779 | 8 | 0 | 7,519 |
| 2025 | 4,008 | 2,425 | 411 | 0 | 6,844 |

The request-level totals reconcile in all three years.

PPL's 2023–2025 request change is:

\[
\left(\frac{6{,}844}{7{,}567}-1\right)\times100=-9.55\%.
\]

| Year | PPL requests | Statewide requests | PPL share | PPL rank |
|---|---:|---:|---:|---:|
| 2023 | 7,567 | 19,202 | 39.41% | 1 |
| 2024 | 7,519 | 18,582 | 40.46% | 1 |
| 2025 | 6,844 | 20,202 | 33.88% | 1 |

PPL is the largest EDC by reported request volume in each year. Its statewide share falls in 2025 even though it remains first by volume.

Annual requests are a **flow** received during a defined reporting period. Customer-generators and interconnected nameplate capacity are **stocks** measured at a date (May 31 in the report). A growing stock can coexist with falling annual requests because the installed base accumulates over time and request flows are not equal to completed installations.

## Part B — 2025 large-project mix

For Level 2 at or above 500 kW:

\[
\frac{135}{196}\times100=68.88\%.
\]

For Level 3 at or above 500 kW:

\[
\frac{411}{954}\times100=43.08\%.
\]

PPL's Level 3 at-or-above-500-kW requests as a share of all PPL requests:

\[
\frac{411}{6{,}844}\times100=6.00\%.
\]

The PUC did not publish the 2023–2024 Level 2–4 request counts using the same 500 kW split. Do not infer or backfill the missing categories from the 2025 distribution. The report also records requests moved between levels; review level can change after screening or applicant changes, so it is not necessarily an immutable project attribute.

## Part C — Stocks, flows, and approval times

For customer-generators:

\[
\left(\frac{28{,}819}{19{,}685}-1\right)\times100=46.40\%.
\]

For total interconnected nameplate capacity:

\[
\left(\frac{477{,}019}{310{,}199}-1\right)\times100=53.78\%.
\]

For annual requests, the change is -9.55% as calculated in Part A. These statistics describe different concepts and should not be interpreted as a contradiction.

The reported Level 1 mean approval times are 1, 1, and 10 days. The report states that Level 1 review is subject to a 25-business-day requirement and describes PPL and PECO as having the best large-EDC Level 1 mean in 2025 at 10 business days. The values do not establish a causal change in utility performance. The mean approval-time statistic relates to approvals completed in the reporting year; request counts relate to requests received in that year. Without application-level cohort matching and denominators, they need not describe the same cases. Zero-valued mean-time cells may indicate no completed approvals or non-applicability, not literal zero-day review.

## Part D — Status-table audit

For 2025, the listed PPL status categories sum to:

\[
5{,}043+0+852+0+592=6{,}487.
\]

This is 357 fewer than the 6,844 submitted requests. The reported Completed field is 6,487, and:

\[
6{,}487-(5{,}043+0+852)=592,
\]

which equals pending EDC action. By contrast, in 2023 and 2024, the reported Completed field equals approved + denied + cancelled, without adding pending EDC action.

A defensible data-quality note is:

> The PPL 2025 status categories sum to 6,487, leaving 357 of 6,844 submitted requests unallocated in the displayed categories. The reported Completed value includes the 592 requests separately labelled Pending EDC Action. In 2023 and 2024, Completed equals approved + denied + customer-cancelled. The PUC should clarify the definition of Completed, the treatment of pending EDC action, and the 357-request gap before these fields are used for completion-rate or backlog analysis.

Do not divide approvals by submitted or reported completed until the denominator is resolved.

## Part E — Policy timing and causal identification

The report's last detailed reporting year ends May 31, 2025. Both the January 3, 2026 Rule 12 applicability date and January 5, 2026 Second DER Management Program implementation occur after the entire observed period. The data are a pre-implementation baseline.

The next annual period, June 1, 2025–May 31, 2026, includes only the final five months after the January 2026 milestones. It also mixes requests submitted before and after the change if the report only aggregates by receipt year and approvals completed during the period. The analyst needs application-received dates and applicable tariff/program version, not only a year label.

A defensible next step is a descriptive cohort study that separately tracks:
- requests received before and after January 3, 2026;
- completeness dates and utility review start/end dates;
- review-level changes;
- applicant and utility waiting intervals;
- study/upgrade requirements and capacity bands;
- approval, cancellation, denial, and permission-to-operate milestones.

A causal estimate would additionally require a stable outcome definition, a credible comparison group, multiple pre-periods, comparable service territories, no differential concurrent policy or technology shocks, and an argument against selection and spillovers. Three detailed annual observations are not enough. The 2026 report may be useful for follow-up but will not by itself solve the cohort or identification problems.

## Part F — Minimum data dictionary

| Field | Definition | Why needed |
|---|---|---|
| anonymized_application_id | Stable non-identifying request key | Follow a request across status/review-level changes |
| received_date | Date initial request received | Assign reporting year and policy exposure |
| complete_date | Date application deemed complete | Separate applicant delay from utility review |
| review_level_history | Dated Level 1–4 assignments | Capture screening and reclassification |
| nameplate_capacity_kw | AC capacity, with basis documented | Size-band and technology controls |
| edc_service_territory | Stable service-territory code | Preserve geographic/organizational unit |
| utility_review_start/end | Dates of utility action intervals | Measure utility-controlled duration |
| applicant_action_start/end | Dates of applicant action intervals | Measure customer-controlled delay |
| study_required / study_type | Feasibility, system impact, facilities, or none | Explain long review durations |
| upgrade_required / upgrade_type | Distribution or service upgrade category | Measure technical and cost drivers |
| upgrade_cost_band | Publicly releasable cost range | Study upgrade burden without exposing bids |
| status_history | Dated status transitions | Reconstruct status cohorts and backlog |
| cancellation_reason_group | Standardized non-identifying reason | Separate customer-driven withdrawal causes |
| approval_date / PTO_date | Approval and permission-to-operate dates | Distinguish review approval from actual operation |
| tariff_version / DERMS_applicability | Applicable rule/program by application date | Define policy exposure |

Release should use suppression thresholds and aggregated size/territory/time cells where necessary. Customer names, addresses, account numbers, exact feeder identifiers, detailed protection settings, and commercially sensitive study narratives should not be included in a public research extract. If records are not public, use the PUC's formal filing or records process and request non-identifying aggregated data; do not use internal employer data.

## Final methodological conclusion

The PUC report supports a useful descriptive baseline and peer comparison. It does not yet support a causal statement about PPL's 2026 Rule 12 or DER Management Program. The highest-value next step is to obtain a reconciled public status definition and application-cohort data, while preserving the EDC service-territory unit and the 500 kW schema break.

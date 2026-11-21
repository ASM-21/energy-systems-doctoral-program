# Pennsylvania PUC Net-Metering and Interconnection Report (2023–2025)

**Primary source:** Pennsylvania Public Utility Commission, *Net-Metering and Interconnection Report 2023–2025*, 30 pages.  
**Official PDF:** https://www.puc.pa.gov/media/3770/net-metering-interconnection-report-2023-2025_final.pdf  
**Accessed:** 2026-11-21  
**Data files:** [PPL 2023–2025 detailed metrics](ppl_interconnection_2023_2025.csv); [all-EDC request-count panel](pa_edc_interconnection_2023_2025.csv)

## Why this source changes the research design

EIA-861 provides a useful cumulative utility-level net-metered PV series, but the PUC report provides much closer measures of distribution interconnection activity: annual request counts by review level and EDC service territory, mean approval times, interconnected customer-generator counts and nameplate capacity, and request status. The report's reporting year runs from June 1 through May 31. It includes a ten-year trend for request counts and capacity (2016–2025), with detailed utility-level tables for 2023–2025.

This should become the primary quantitative dataset for the Pennsylvania interconnection case study. EIA-861 remains a complementary source for cumulative reported DER adoption and other utility-level indicators, not the main measure of interconnection performance.

## PPL descriptive results

| Measure | 2023 reporting year | 2024 reporting year | 2025 reporting year |
|---|---:|---:|---:|
| Customer-generators | 19,685 | 25,252 | 28,819 |
| Solar customer-generators | 19,535 | 25,100 | 28,654 |
| Interconnected nameplate capacity, all Tier I/II (kW) | 310,199 | 394,276 | 477,019 |
| Solar nameplate capacity (kW) | 270,641 | 351,718 | 439,371 |
| Total interconnection requests | 7,567 | 7,519 | 6,844 |
| Level 1 requests | 4,698 | 4,732 | 4,008 |
| Level 2 requests | 2,854 | 2,779 | 2,425 |
| Level 3 requests | 15 | 8 | 411 |
| Level 4 requests | 0 | 0 | 0 |
| Mean Level 1 approval time (days as tabulated) | 1 | 1 | 10 |
| Pending EDC action | 0 | 0 | 592 |
| Pending customer action | 2,385 | 1,891 | 0 |
| Approved | 5,175 | 5,568 | 5,043 |
| Cancelled by customer | 5 | 60 | 852 |

The 2025 Level 2 total is 2,425, comprising 2,290 requests below 500 kW and 135 at or above 500 kW. The 2025 Level 3 total is 411, all reported at or above 500 kW; none are reported below 500 kW. Level 4 remains zero. The 2025 review-time table separates Levels 2–4 at 500 kW, while the 2023 and 2024 tables do not.

Between the 2023 and 2025 reporting years, the reported PPL customer-generator count increased by approximately 46.4%, and total interconnected nameplate capacity increased by approximately 53.8%. Total annual requests declined by approximately 9.6% over the same interval. These are descriptive changes in reported counts and capacity, not a causal estimate of any tariff, program, or utility intervention.

The 2025 table reports 592 PPL requests pending EDC action, compared with zero in the 2023 and 2024 tables. It also reports 852 customer cancellations in 2025, compared with 60 in 2024 and 5 in 2023. These are material signals for follow-up, but the report does not provide application-level cohort histories or cancellation reasons. Do not interpret the year-to-year status movement as a measured change in utility processing performance without resolving the report's status definitions and cohort accounting.

## Pennsylvania EDC peer comparison

The structured extract now covers all 11 EDC service territories for 2023–2025, not only PPL. Each EDC's review-level request counts reconcile to its reported total, and the 11 EDC totals reconcile to the statewide totals in the PUC report.

| EDC service territory | 2023 requests | 2024 requests | 2025 requests |
|---|---:|---:|---:|
| Citizens | 17 | 15 | 17 |
| Duquesne Light | 2,325 | 1,955 | 2,520 |
| Met-Ed | 2,630 | 2,742 | 3,658 |
| PECO | 4,527 | 4,071 | 3,776 |
| Penelec | 561 | 772 | 1,226 |
| Penn Power | 407 | 421 | 583 |
| Pike | 12 | 9 | 6 |
| PPL | 7,567 | 7,519 | 6,844 |
| UGI | 82 | 82 | 183 |
| Wellsboro | 5 | 13 | 13 |
| West Penn | 1,069 | 983 | 1,376 |
| **Statewide total** | **19,202** | **18,582** | **20,202** |

PPL ranked first in total request volume in all three reporting years. Its share of statewide requests was 39.41% in 2023, 40.46% in 2024, and 33.88% in 2025. PPL remained the largest EDC by request volume even as its annual count fell by 9.55% from 2023 to 2025.

In 2025, PPL accounted for 135 of the 196 Level 2 requests at or above 500 kW (68.88%) and 411 of the 954 Level 3 requests at or above 500 kW (43.08%). These are request counts, not unique-project counts, approvals, completed installations, or capacity totals. The 500 kW threshold split is only available in the 2025 tables.

The complete 33-row, 11-EDC dataset is [pa_edc_interconnection_2023_2025.csv](pa_edc_interconnection_2023_2025.csv). The reproducible peer audit is analyze_pa_edc_interconnection.py, with unit tests in test_analyze_pa_edc_interconnection.py. It validates each EDC's review-level count sum, reconciles statewide totals to the PUC's reported totals, and computes PPL's rank/share without estimating causal effects.

## Policy timing: these data are a pre-implementation baseline

All three detailed reporting years in this report end on May 31, 2025. They therefore predate PPL's Rule 12 applicability date of January 3, 2026 and the stated January 5, 2026 implementation start of the Second DER Management Program. The 2023–2025 tables cannot measure the effects of either 2026 change.

The next reporting year (June 1, 2025–May 31, 2026) would contain only a partial post-implementation window beginning in January 2026. Even that aggregate annual table would not cleanly identify treatment exposure: applications received before January 3 may be completed after that date, while new applications may be reviewed under the new process. Application-level received dates, completion dates, review level, and policy applicability would be needed to distinguish cohorts. Treat the current data as a baseline and avoid before/after causal language.

## Review-level definitions

The report describes four Pennsylvania interconnection review levels:

- **Level 1:** Certified inverter-based facilities no larger than 10 kW. The report states that Level 1 applications are to be completed within 25 business days, with up to 10 business days for completeness review and 15 business days for technical screens.
- **Level 2:** Inverter-based facilities greater than 10 kW and no larger than 2 MW, subject to the applicable screening criteria.
- **Level 3:** Non-inverter-based facilities up to 2 MW, or facilities that do not pass Level 1/2 review.
- **Level 4:** Facilities that do not qualify for Level 1/2 and do not export power beyond the point of common coupling.

The PUC's 2025 report begins splitting Level 2, 3, and 4 requests and average approval times at 500 kW. Preserve that change; do not silently compare the 2025 split cells with the unsplit 2023–2024 values.

## Critical measurement caveats

1. **Reporting period:** Each annual reporting year is June 1 through May 31, not a calendar year.
2. **Request cohort versus approvals:** Request counts and mean approval times are not necessarily the same cohort. The mean time table concerns approvals completed in the reporting year; the request table counts requests received in the reporting year. Do not divide or directly match these without cohort-level data.
3. **Mean-time zeroes:** Some cells in the PUC tables are reported as zero. A zero may indicate no completed cases in that cell or a non-applicable category; it must not be interpreted as a literal zero-day review time without denominator information.
4. **2025 capacity threshold split:** Level 2–4 counts and average days are split at 500 kW in 2025 but not in 2023–2024.
5. **Level reclassification:** The report includes tables for requests moved between review levels. A request can move to a different review level, so level-specific counts are not immutable project attributes.
6. **Status-table accounting:** Preserve the PUC's exact status fields. In the 2023 and 2024 PPL rows, `Completed` equals approved plus denied plus cancelled. In the 2025 PPL row, reported `Completed` (6,487) equals approved (5,043) plus customer-cancelled (852) plus pending EDC action (592), even though pending EDC action is separately named. Further, the listed 2025 status categories sum to 6,487, which is **357 fewer than submitted (6,844)**. The report does not allocate that 357-request difference in the PPL row. This is an unresolved reporting/accounting discrepancy, not a denominator to impute. Do not calculate completion rates or interpret `Completed` as closed applications until the PUC clarifies the field definitions and 2025 discrepancy.
7. **No project-level records:** The report is aggregated by EDC service territory. It does not contain individual application dates, locations, feeder IDs, study results, upgrade costs, queue positions, or applicant characteristics.
8. **Customer-generator scope:** This is Pennsylvania net-metered customer-generator interconnection reporting. It is not a complete census of all DERs, non-net-metered generation, transmission-level PJM queue projects, or all storage.
9. **No causal inference:** These tables are descriptive. The PUC report itself notes that responsiveness from applicants can contribute to lengthy review times. The data do not identify the causal effect of Rule 12, DERMS deployment, hosting-capacity investments, or other policies.

## 2025 PPL request composition

The 2025 PPL total of 6,844 requests is reported as:
- Level 1: 4,008
- Level 2 below 500 kW: 2,290
- Level 2 at or above 500 kW: 135
- Level 3 below 500 kW: 0
- Level 3 at or above 500 kW: 411
- Level 4 below 500 kW: 0
- Level 4 at or above 500 kW: 0

This distribution warrants a dedicated check against the source EDC filing and the PUC's 500 kW threshold definitions. In particular, do not infer that 411 requests represent 411 distinct projects or that all such requests were approved or interconnected.

## Corporate-identity and service-territory reconciliation

EIA's respondent frame identifies FirstEnergy Pennsylvania Electric Co as EIA utility ID 66101 in 2025, while the earlier Pennsylvania utility panel includes legacy respondents such as Pennsylvania Electric Co (EIA ID 14711). FirstEnergy's 2023 Form 10-K states that on January 1, 2024, the Pennsylvania operating companies were consolidated into FE PA, a new single operating entity and successor to their assets and liabilities. The PUC report nevertheless continues to present separate EDC service territories/rate districts such as Met-Ed, Penelec, Penn Power, and West Penn Power.

This is a concrete reason not to treat the EIA utility-ID panel as a simple stable peer panel. The PUC's EDC service-territory series is more appropriate for these interconnection comparisons, while EIA utility-level records require a time-varying entity/territory crosswalk. Do not merge the old IDs into 66101 without explicit source-backed mapping and a decision about whether the analysis unit is the historic rate district or consolidated FE PA legal respondent.

## Recommended empirical design

### Primary descriptive study

Use the PUC annual report tables as the primary panel:
- Unit: EDC service territory × reporting year × review level.
- Years: detailed 2023–2025 tables; 2016–2025 trend figures as a longer context series.
- Outcomes: request counts, average approval times, interconnected customer-generators, nameplate capacity, and status categories.
- Denominators: installed customer-generator base, request totals, and review-level totals, where definitions align.
- Comparisons: PPL versus other large EDC territories, with separate small-EDC comparisons.
- Required figures: request counts by level, mean review days by level, status composition, cumulative capacity, and customer-generator counts.

### Research questions

1. How did PPL's request volume and review-level composition change from reporting year 2023 to 2025?
2. Did the reported shift toward Level 3 requests at or above 500 kW coincide with changes in average review time or pending-EDC status?
3. How did PPL's Level 1 review time compare with other large Pennsylvania EDCs?
4. Are changes in PPL's reported request status driven by EDC action, applicant action, cancellations, or changes in request composition?
5. How should PPL's Second DER Management Plan and Rule 12 implementation be evaluated without conflating cumulative DER adoption, requests received, approvals, and actual interconnected capacity?

### Required next evidence

- Obtain the underlying annual EDC submissions referenced by the PUC report, particularly PPL's 2023, 2024, and 2025 submissions.
- Obtain the source definitions and denominator for each mean approval-time statistic.
- Resolve the 2025 status-table arithmetic and whether `Completed` includes requests pending EDC action.
- Verify the count and treatment of requests moved between review levels.
- Identify the precise effective dates and affected application cohorts for Rule 12 and the Second DER Management Plan.
- Search for subsequent reports and any corrections to the 2023–2025 report.

## Source notes

- PUC report background, reporting period, and summary: pp. 4–5.
- Customer-generator counts: Table 2A–2C, p. 6.
- Interconnected nameplate capacity: Table 3A–3C, p. 9.
- Request counts by level: Table 4A–4C, pp. 12–13.
- Mean approval times: Table 5A–5C, pp. 19–20.
- Status of requests: Table 6A–6C, pp. 22–23.
- Review-level movements: Tables 6D–6F and Table 7, pp. 23–24.
- FirstEnergy corporate consolidation: FirstEnergy 2023 Form 10-K, Pennsylvania section, describing the January 1, 2024 consolidation of the Pennsylvania Companies into FE PA.

A reproducible validation script and unit tests are provided in `analyze_puc_interconnection.py` and `test_analyze_puc_interconnection.py`. The tests require request-level totals to reconcile and explicitly flag the 2025 status discrepancy rather than silently normalizing it. The official PUC report and FirstEnergy filing are listed in the casebook source register. 

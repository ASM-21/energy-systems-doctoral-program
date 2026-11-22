# Pennsylvania EDC Interconnection Panel: Data Dictionary

**Source file:** `research/casebooks/pa-der-interconnection/pa_edc_interconnection_2023_2025.csv`  
**Rows:** 33 (11 EDC territories × 3 reporting years)  
**Source:** Pennsylvania PUC, *Net-Metering and Interconnection Report 2023–2025*, tables 4A–4C and 5A–5C.  
**Reporting period:** June 1 through May 31.

| Field | Type / unit | Definition | Comparability / caveat |
|---|---|---|---|
| reporting_year | integer | PUC reporting-year label | Not calendar year; use period_start/end |
| period_start | date | First day of reporting period | June 1 |
| period_end | date | Last day of reporting period | May 31 |
| edc | category | EDC service territory label | Do not assume direct equivalence to EIA utility IDs |
| level1_requests | count | Requests assigned to Level 1 in report | Review-level classification; not approvals |
| level2_requests | count | Requests assigned to Level 2 | Aggregate total; no size split in 2023–2024 |
| level2_lt500kw_requests | count | Level 2 requests below 500 kW | Reported in 2025 only |
| level2_ge500kw_requests | count | Level 2 requests at or above 500 kW | Reported in 2025 only |
| level3_requests | count | Requests assigned to Level 3 | Level definitions have source/code inconsistencies documented in casebook |
| level3_lt500kw_requests | count | Level 3 requests below 500 kW | Reported in 2025 only |
| level3_ge500kw_requests | count | Level 3 requests at or above 500 kW | Reported in 2025 only |
| level4_requests | count | Requests assigned to Level 4 | Reported zero for all rows in this panel |
| level4_lt500kw_requests | count | Level 4 requests below 500 kW | Reported in 2025 only |
| level4_ge500kw_requests | count | Level 4 requests at or above 500 kW | Reported in 2025 only |
| total_requests | count | EDC's total reported requests | Sum of Levels 1–4; reconciliation tested |
| mean_level1_days | days | Mean Level 1 approval/review time as tabulated | Do not interpret without exact denominator and clock definition |
| mean_level2_days | days | Mean Level 2 approval/review time as tabulated | Review level and size splits vary by year |
| mean_level2_lt500kw_days | days | Mean Level 2 time below 500 kW | 2025 subcategory only |
| mean_level2_ge500kw_days | days | Mean Level 2 time at/above 500 kW | 2025 subcategory only |
| mean_level3_days | days | Mean Level 3 approval/review time as tabulated | Some zero values require source-definition review |
| mean_level3_lt500kw_days | days | Mean Level 3 time below 500 kW | 2025 subcategory only |
| mean_level3_ge500kw_days | days | Mean Level 3 time at/above 500 kW | 2025 subcategory only |
| mean_level4_days | days | Mean Level 4 approval/review time as tabulated | Zero requests in this extract; not a meaningful observed duration |
| mean_level4_lt500kw_days | days | Mean Level 4 time below 500 kW | 2025 subcategory only |
| mean_level4_ge500kw_days | days | Mean Level 4 time at/above 500 kW | 2025 subcategory only |
| source_table | text | PUC table identifier(s) used | 4C/5C (2023), 4B/5B (2024), 4A/5A (2025) |
| source_pages | text | PUC PDF pages for the source rows | Retained for traceability |
| reported_statewide_total | count | PUC-published statewide total repeated on each row | Reconciliation target, not an EDC-specific measure |

## Derived fields

- **EDC request share:** EDC total requests divided by the sum of EDC total requests in the same reporting year.
- **PPL rank:** descending rank by EDC total request count; ties would require an explicit tie rule.
- **Request-count HHI:** (10{,}000\sum_i s_i^2), where (s_i) is EDC i's share of statewide request counts. This is not a product-market HHI.
- **Top-three share:** sum of the three largest EDC request counts divided by statewide requests.
- **Year-over-year change:** current EDC request count divided by its prior reporting-year count, minus one.

## Missingness and zero rules

Blank 2023–2024 size-band subcategories mean the source did not provide that split. They are not evidence of zero requests in each size band. The analysis script treats blank numeric cells as zero only when summing mutually exclusive reported count fields where the total is known; it does not construct cross-year comparisons for unavailable size bands.

A reported zero is different from a blank. A zero request count may be a valid observed count. A zero mean duration where no relevant requests are reported is not an observed processing time. Do not compute a mean of means or use these aggregate means as application-level duration observations.

## Prohibited inferences

This panel does not contain linked application identifiers, cohort transitions, individual received/completed dates, project-level capacity, feeder constraints, approval probability, installed capacity, or causal treatment assignment. It cannot support application-level approval rates, time-to-decision survival analysis, hosting-capacity estimates, or causal effects of tariff/DERMS changes.

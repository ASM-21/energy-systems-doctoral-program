# Pennsylvania EIA-861 Net-Metering Utility Panel: Coverage Audit

**Audit window:** 2015–2025  
**Source:** Official annual EIA-861 detailed-data ZIP archives  
**Workflow run:** [Corrected historical coverage and extraction](https://github.com/ASM-21/energy-systems-doctoral-program/actions/runs/44915910602)  
**Workflow commit:** `2a64ca6f855fd4e1f3f0182ec56fe6fe780290b6`  
**Status:** Coverage extraction validated; cross-utility variable harmonization not performed.

## Executive result

The corrected extraction produces **249 Pennsylvania utility-year rows**, covering **33 distinct EIA utility IDs** over 2015–2025. The panel audit reports **zero duplicate year/utility-ID keys** and **zero invalid rows**. Annual coverage is unbalanced: 18–32 utilities per year. Seventeen EIA utility IDs appear in all 11 years.

This is a successful coverage and identity audit, not yet an analytically comparable panel. The output retains raw annual fields and provenance; it does not establish consistent service territories, respondent forms, ownership, or measurement definitions. No cross-utility growth rates, rankings, or causal estimates should be calculated from the extract.

## Annual coverage

| Year | Utility IDs | Rows |
|---:|---:|---:|
| 2015 | 24 | 24 |
| 2016 | 24 | 24 |
| 2017 | 25 | 25 |
| 2018 | 24 | 24 |
| 2019 | 32 | 32 |
| 2020 | 21 | 21 |
| 2021 | 21 | 21 |
| 2022 | 21 | 21 |
| 2023 | 21 | 21 |
| 2024 | 18 | 18 |
| 2025 | 18 | 18 |
| **Total** | **33 unique IDs** | **249** |

The 2019 peak includes seven short-form respondents; the 2020–2025 rows are all full-form. The subsequent decline also includes fewer full-form respondents, so the coverage change needs more than one explanation. It is not evidence that utilities entered or exited net-metering activity. Missing utility-years are not zeros.

## Extraction controls and exclusions

The corrected extractor uses utility-level respondent sheets and excludes third-party-owned (TPO) schedules and administrative adjustment rows. The archive manifests record the excluded source sheets/rows.

- **13 TPO worksheets** excluded across the 11 annual archives.
- **7 administrative adjustment rows** excluded, including EIA utility ID 99999.
- **0 duplicate year/utility-ID keys** remain in the corrected extract.
- **0 invalid rows** were flagged by the audit.

These exclusions are explicit and reproducible. They correct a prior extraction that had inadvertently treated TPO schedules and adjustment rows as ordinary EDC utility respondents.

## Respondent-frame linkage (2016–2025)

The annual respondent-frame linkage was executed successfully for every year from 2016 through 2025. All **225** Pennsylvania utility-year IDs matched exactly one record in their corresponding annual frame: **zero unmatched IDs and zero duplicate frame IDs**. Every matched record had the net-metering schedule flag set to `X`.

The frame audit adds a useful explanation for the coverage pattern. The 2019 panel contains 32 respondents, of which **7 were EIA-861S short-form respondents** and 25 were full-form respondents. Every respondent in the 2020–2025 panel is full-form: 21 per year in 2020–2023 and 18 per year in 2024–2025. Thus, the 2019 peak is not a homogeneous full-form panel, and the 2020 drop partly coincides with the disappearance of those seven short-form respondents. Four fewer full-form IDs also appear in 2020 than in 2019, so short-form status alone does not explain the full coverage change. EIA's short-form imputation note beginning in 2020 should be read alongside this actual frame result: no Pennsylvania net-metering respondents in this extract are marked short-form from 2020 onward.

The identity history is also clear in the frame: PPL ID **14715** is present throughout 2016–2025; Pennsylvania Electric Co ID **14711** is present through 2023; FirstEnergy Pennsylvania Electric Co ID **66101** appears in 2024–2025. See the corporate-consolidation explanation below.

## Identifier continuity and respondent-name variants

Seventeen IDs are present in every year. Two of those IDs have respondent-name variants across years:

- EIA ID **3329**: Borough of Chambersburg / Borough of Chambersburg - (PA).
- EIA ID **40290**: Tri-County Rural Elec Coop Inc / Tri-County Rural Elec Coop Inc (PA).

The audit records the variants but does not assume that the names prove a legal or territorial change. The name variants may be formatting or respondent-label changes; confirm against EIA respondent frames and source instructions before harmonization.

Other discontinuities require review. EIA ID **14711** (Pennsylvania Electric Co) is observed through 2023, while ID **66101** (FirstEnergy Pennsylvania Electric Co) appears in 2024–2025. This timing aligns with FirstEnergy's disclosed consolidation of the Pennsylvania operating companies into FE PA effective January 1, 2024. FirstEnergy's 2023 Form 10-K describes FE PA as the successor to the Pennsylvania companies' assets and liabilities. This makes ID 66101 a consolidated successor respondent, not a one-for-one continuation of ID 14711. Do not combine the pre-2024 IDs into 66101 without a documented territory crosswalk. The Pennsylvania PUC's 2023–2025 Net-Metering and Interconnection Report continues to present legacy EDC service territories/rate districts separately (Met-Ed, Penelec, Penn Power, West Penn), which is a more suitable unit for the interconnection process analysis. See [the PUC report casebook](../../casebooks/pa-der-interconnection/puc-interconnection-report-2023-2025.md). Similarly, some municipal/cooperative IDs appear only in selected years. These may reflect changing coverage, respondent reporting, or schedule availability rather than true service-territory entry/exit.

## Measurement and schema limitations

The CSV is a union of raw columns across annual workbooks. Different years have different worksheet names, header structures, and fields. A field present in one year's schema may be absent in another; blank values must not be converted to zero. The extraction script preserves raw source fields and source-row metadata, but does not yet produce a harmonized variable dictionary.

Before using any outcome across utilities or years, inspect:
1. Annual respondent frames and EIA utility-ID continuity. The 2016–2025 linkage has no unmatched/duplicate IDs.
2. Form type (full EIA-861 versus EIA-861S/short form) and reporting obligations. The 2019 panel includes seven short-form respondents; none of the 2020–2025 PA net-metering rows are short-form.
3. Service-territory, ownership, and respondent changes.
4. Capacity basis (AC/DC/unspecified), technology scope, and treatment of virtual net metering.
5. Customer versus installation count definitions and schedule redesigns.
6. Whether values are observed, imputed, adjusted, suppressed, or missing.
7. Units, sector definitions, and aggregation levels.

A stable ID is not proof of a stable service territory or stable variable definition. A name change is not proof of a new utility. Both require source-level evidence.

## What can proceed

- Use the coverage table to select candidate utilities for a source-level comparability review.
- Continue the PPL-only descriptive series, subject to its separately documented year-specific measurement breaks.
- Build a harmonization crosswalk only for fields whose definitions and units are supported by annual instructions and source workbooks.
- Publish a balanced/unbalanced sample description and missingness table before any peer comparison.

## What cannot proceed yet

- No multi-utility capacity growth rankings or CAGR comparisons.
- No peer-adjusted PPL performance claim.
- No causal effect estimate for PPL's DER Management Plan, Rule 12, or another policy.
- No inference about feeder hosting capacity, interconnection queue outcomes, upgrade costs, or DER curtailment from this aggregate net-metering schedule.

## Reproduction

The workflow runs the tests, downloads and hashes official annual archives, extracts Pennsylvania utility rows, writes source manifests and schema inventories, audits coverage and identity continuity, and uploads the resulting files as a workflow artifact. The artifact for the run linked above contains the raw extract, annual coverage table, audit JSON, identity history, schema inventory, and the separate PPL harmonized series.

Primary script paths:
- `extract_pa_utility_net_metering.py`
- `audit_pa_utility_panel.py`
- `test_extract_pa_utility_net_metering.py`
- `test_audit_pa_utility_panel.py`

The panel audit is intentionally diagnostic. It must not be mistaken for a panel-data preparation or estimation routine.


## Additional source-based interpretation of the FirstEnergy ID break

FirstEnergy's 2023 Form 10-K states that its Pennsylvania operating companies were consolidated into FE PA effective January 1, 2024, with FE PA as successor to the prior Pennsylvania companies' assets and liabilities: https://www.sec.gov/Archives/edgar/data/1031296/000103129624000008/fe-20231231.htm. This explains why EIA respondent 66101 appears while legacy Pennsylvania utility respondents disappear from later annual frames, but it does not make their historical observations a homogeneous single-utility series. The PUC's aggregated report preserves separate EDC service-territory/rate-district statistics for the former companies. Use the PUC unit for interconnection comparisons and retain the EIA ID discontinuity in any EIA-861 analysis.

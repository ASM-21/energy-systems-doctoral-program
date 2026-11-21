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

The 2019 peak and subsequent coverage decline are reasons to investigate reporting coverage and respondent-frame changes. They are not evidence that utilities entered or exited net-metering activity. Missing utility-years are not zeros.

## Extraction controls and exclusions

The corrected extractor uses utility-level respondent sheets and excludes third-party-owned (TPO) schedules and administrative adjustment rows. The archive manifests record the excluded source sheets/rows.

- **13 TPO worksheets** excluded across the 11 annual archives.
- **7 administrative adjustment rows** excluded, including EIA utility ID 99999.
- **0 duplicate year/utility-ID keys** remain in the corrected extract.
- **0 invalid rows** were flagged by the audit.

These exclusions are explicit and reproducible. They correct a prior extraction that had inadvertently treated TPO schedules and adjustment rows as ordinary EDC utility respondents.

## Identifier continuity and respondent-name variants

Seventeen IDs are present in every year. Two of those IDs have respondent-name variants across years:

- EIA ID **3329**: Borough of Chambersburg / Borough of Chambersburg - (PA).
- EIA ID **40290**: Tri-County Rural Elec Coop Inc / Tri-County Rural Elec Coop Inc (PA).

The audit records the variants but does not assume that the names prove a legal or territorial change. The name variants may be formatting or respondent-label changes; confirm against EIA respondent frames and source instructions before harmonization.

Other discontinuities require review. EIA ID **14711** (Pennsylvania Electric Co) is observed through 2023, while ID **66101** (FirstEnergy Pennsylvania Electric Co) appears in 2024–2025. Do not automatically stitch these IDs together. Determine whether this reflects an EIA respondent-ID change, reporting-frame revision, organizational change, or another cause using the annual respondent frames and EIA documentation. Similarly, some municipal/cooperative IDs appear only in selected years. These may reflect changing coverage, respondent reporting, or schedule availability rather than true service-territory entry/exit.

## Measurement and schema limitations

The CSV is a union of raw columns across annual workbooks. Different years have different worksheet names, header structures, and fields. A field present in one year's schema may be absent in another; blank values must not be converted to zero. The extraction script preserves raw source fields and source-row metadata, but does not yet produce a harmonized variable dictionary.

Before using any outcome across utilities or years, inspect:
1. Annual respondent frames and EIA utility-ID continuity.
2. Form type (full EIA-861 versus EIA-861S/short form) and reporting obligations.
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

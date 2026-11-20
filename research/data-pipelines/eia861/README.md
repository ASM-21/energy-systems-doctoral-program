# EIA-861 2025 public-data pipeline

## Purpose

Build a reproducible inventory of the official 2025 final EIA-861 detailed-data ZIP before deciding which schedules support a Pennsylvania distribution/DER research question. The pipeline does not assume that every DER schedule is utility-specific or that EIA-861 contains feeder-level interconnection outcomes.

## Source and known limits

- Official source: [EIA Form 861 detailed data](https://www.eia.gov/electricity/data/eia861/).
- Direct 2025 final ZIP: https://www.eia.gov/electricity/data/eia861/zip/f8612025.zip.
- EIA describes Form 861 as a census of U.S. electric utilities and publishes separate schedules for service territory, reliability, distribution systems, utility data, net metering, and non-net-metered distributed generation.
- Net-metering and non-net-metered distributed-generation summaries are aggregated by state, sector, and balancing authority. They are not a PPL-specific project/interconnection queue or feeder hosting-capacity dataset.
- PPL Electric Utilities Corp is EIA utility ID 14715, confirmed in the downloaded official `Frame_2025.xlsx` respondent frame. The extraction script checks that ID 14715 continues to map to a PPL Electric name in every selected sheet.

## Run

    python -m pip install -r requirements.txt
    python inventory_eia861.py --archive data/raw/f8612025.zip --output-dir outputs/eia861-2025
    python extract_ppl_eia861.py --workbooks-dir outputs/eia861-2025/workbooks --output-dir outputs/ppl-eia861-2025

If the archive is absent, the script downloads it from EIA. It verifies the ZIP CRC, calculates SHA-256, inventories every workbook and worksheet, and records the first 12 rows of each sheet for schema inspection. It extracts workbooks only into the output directory; raw and derived data are not committed to Git. The PPL extraction writes a long-form CSV with source workbook, sheet, row, field, and value, plus a coverage table that explicitly records sheets where no PPL row exists. A missing row is not silently converted to zero.

## Verified 2025 PPL coverage

The first official 2025 final-data inventory completed in GitHub Actions on 2026-11-20. The ZIP SHA-256 was `f59f6c732bf685fe0a1591b32227f5ce572dc0dfd26bb5caaeed128ac4e3a396`; the archive contained 20 workbooks and 60 worksheets. The PPL respondent was confirmed as EIA utility 14715.

Utility-specific PPL rows were found in the 2025 frame, utility data, operational data, distribution systems, reliability, net metering, advanced meters, dynamic pricing, energy efficiency, sales to ultimate customers, and service-territory schedules.

Important granularity correction: the 2025 Net_Metering workbook contains a `States- Utility Level` worksheet with an explicit utility-number field and a PPL row. The generic EIA webpage describes net-metering data in state/sector/BA terms, but the actual 2025 final ZIP provides this additional utility-level worksheet. Do not generalize from the webpage summary alone.

The PPL row reports 505.746 MW of standard net-metered PV capacity and 31,400 standard PV installations. It separately reports 33.474 MW of virtual PV capacity (10.3 MW at 1 MW and over, 23.174 MW under 1 MW), 0.45 MW of net-metered wind, and 38.037 MW of other net-metered capacity. The all-technologies total is 577.707 MW and 31,932 installations. PV-paired and standalone battery fields contain blanks/zero totals in this row; treat those as reported-field status, not proof that no batteries exist. Energy-sold-back values are blank/zero in the utility row and do not provide a usable measured export total.

The PPL row is absent from the Non_Net_Metering_Distributed and Demand_Response utility-level schedules, and the respondent frame does not flag PPL as reporting those schedules in 2025. This is not evidence of zero non-net-metered DER or zero demand response; it is a reporting-coverage limitation.

Other utility-level measures include 1,292 distribution circuits (1,292 reported with voltage optimization), 1,504,018 AMI meters, summer/winter peak demand of 7,366/7,840 MW, and reliability values of SAIDI 198.1 minutes and SAIFI 0.974 with major-event days (SAIDI 115.6 minutes and SAIFI 0.765 without major-event days). Keep each definition, reporting basis, and unit attached to the number.

**Research implication:** A PPL utility-level descriptive panel is feasible for selected measures, including net-metered PV adoption, reliability, circuit counts, AMI, operational data, and sales. EIA-861 still does not provide feeder-level hosting capacity, interconnection queue outcomes, project-level upgrade costs, or realized DER curtailment. Do not infer those outcomes from aggregate utility measures.

[First inventory workflow and artifact](https://github.com/ASM-21/energy-systems-doctoral-program/actions/runs/44832915360).

## Historical utility-level coverage audit

The 2025 package contains a utility-level net-metering worksheet even though EIA's public schedule description characterizes net-metering reporting at state, sector, and balancing-authority levels. Do not assume that this 2025 sheet exists in earlier annual releases. The historical audit scans the actual workbook/worksheet contents for EIA utility ID 14715 and records, by year, whether a worksheet has both a utility identity field and a PPL row.

Run:

    python audit_historical_coverage.py --start-year 2015 --end-year 2025 --output-dir outputs/historical-coverage

The script uses EIA's official annual ZIP archives, checks ZIP CRCs, records each archive's SHA-256, and writes a worksheet-level coverage CSV plus manifest. Historical files use EIA's `/archive/zip/` path; the latest 2025 final release uses `/zip/`. The audit deliberately does not harmonize variables or treat a missing utility row as zero. It is a prerequisite to a historical panel, not the panel itself.

EIA warns that schedule definitions and coverage change over time. Examples include the 2016 change that renamed the non-net-metered distributed-generation schedule and added sector breakdowns, and the 2020 expansion of Form EIA-861S imputation. See the [official EIA-861 schedule descriptions and historical changes](https://www.eia.gov/electricity/data/eia861/). A valid panel must separately document reporting-form coverage, utility mergers/name changes, units, AC/DC adjustments, imputation, and survey redesigns.

## Research protocol

1. Inspect the utility frame and verify EIA ID 14715, exact respondent name, reporting year, ownership, state, and form type.
2. Inspect the workbook inventory and schedule-level row previews before selecting tables.
3. Determine the reporting unit and aggregation level for each candidate schedule. Keep observed, imputed, adjusted, and confidential/redacted values distinct.
4. Link utility-level schedules by EIA utility ID only where the source schema supports that join. Do not join state/sector/BA-level DER capacity to a utility as though it were PPL-specific.
5. Build a source-to-variable dictionary and record units, definitions, missingness, and historical breaks before analysis.
6. If the data do not identify PPL-level DER adoption or interconnection outcomes, report the limitation and use the dataset only for state/BA context.

## Candidate research questions

- How did PPL's reported customer counts, sales, service territory, reliability, and distribution-system descriptors evolve over time?
- Which EIA-861 schedules report utility-specific observations, and which only provide state/sector/BA aggregates?
- What can be said about Pennsylvania DER adoption trends without falsely attributing aggregate net-metering capacity to a specific EDC?
- Can public utility-level reliability and distribution descriptors be used as controls in a broader utility panel, and what endogeneity and comparability issues arise?

## Reproducibility

Every run writes a SHA-256 digest, retrieval timestamp, workbook inventory, and schema previews. The ZIP is not checked into the repository. Preserve the manifest with any analysis output and record the exact data release. The 2025 final release may have revisions or corrections later; rerun the inventory when EIA republishes the file.
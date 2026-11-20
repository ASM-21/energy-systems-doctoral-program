# EIA-861 Public-Data Pipeline and PPL Net-Metering Analysis

## Purpose

Build a reproducible inventory of official annual EIA-861 detailed-data ZIPs and a historical PPL utility-level net-metering PV series. The pipeline does not assume that every DER schedule is utility-specific or that EIA-861 contains feeder-level interconnection outcomes.

## Source and known limits

- Official source: [EIA Form 861 detailed data](https://www.eia.gov/electricity/data/eia861/).
- Direct 2025 final ZIP: https://www.eia.gov/electricity/data/eia861/zip/f8612025.zip.
- EIA describes Form 861 as a census of U.S. electric utilities and publishes separate schedules for service territory, reliability, distribution systems, utility data, net metering, and non-net-metered distributed generation.
- EIA's generic schedule description emphasizes state/sector/balancing-authority net-metering reporting. However, the actual annual Net_Metering workbooks contain a utility-level PPL row in every archive from 2015 through 2025. This schedule-specific observation is verified by the historical archive audit below. The files still do not provide a PPL-specific project/interconnection queue or feeder hosting-capacity dataset.
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

**Research implication:** A PPL utility-level cross-section is available for several 2025 measures. The historical 2015–2025 panel is currently established for net-metered PV capacity/counts and virtual PV capacity; historical comparability for reliability, circuit counts, AMI, operational data, and sales must be audited separately. EIA-861 still does not provide feeder-level hosting capacity, interconnection queue outcomes, project-level upgrade costs, or realized DER curtailment. Do not infer those outcomes from aggregate utility measures.

[First inventory workflow and artifact](https://github.com/ASM-21/energy-systems-doctoral-program/actions/runs/44832915360).

## Historical utility-level coverage audit and extraction

The 2015–2025 annual packages contain utility-level PPL net-metering rows, although worksheet names vary. The historical audit scans actual workbook/worksheet contents for EIA utility ID 14715 and records, by year, whether a worksheet has both a utility identity field and a PPL row. This avoids assuming that a single fixed sheet name or the generic EIA schedule description captures every annual file's structure.

Run:

    python audit_historical_coverage.py --start-year 2015 --end-year 2025 --output-dir outputs/historical-coverage
    python extract_historical_net_metering.py --start-year 2015 --end-year 2025 --output-dir outputs/historical-net-metering
    python normalize_ppl_net_metering.py --input-csv outputs/historical-net-metering/ppl_net_metering_raw.csv --output-dir outputs/historical-net-metering/harmonized
    python plot_ppl_net_metering.py --input-csv outputs/historical-net-metering/harmonized/ppl_net_metering_harmonized.csv --output-dir outputs/historical-net-metering/figures

The script uses EIA's official annual ZIP archives, checks ZIP CRCs, records each archive's SHA-256, and writes a worksheet-level coverage CSV plus manifest. Historical files use EIA's `/archive/zip/` path; the latest 2025 final release uses `/zip/`. The audit deliberately does not harmonize variables or treat a missing utility row as zero. The extraction script preserves the complete PPL row and its source provenance. The normalizer then creates a conservative descriptive series, preserving annual schema breaks and omitting growth calculations across non-comparable capacity bases. The plotting script produces PNG and SVG figures that show the 2015 unknown-basis point separately from the 2016–2025 AC series.

EIA warns that schedule definitions and coverage change over time. Examples include the 2016 change that renamed the non-net-metered distributed-generation schedule and added sector breakdowns, and the 2020 expansion of Form EIA-861S imputation. See the [official EIA-861 schedule descriptions and historical changes](https://www.eia.gov/electricity/data/eia861/). A valid panel must separately document reporting-form coverage, utility mergers/name changes, units, AC/DC adjustments, imputation, and survey redesigns.

## Verified PPL net-metered PV series (2015–2025)

The 2015–2025 historical extraction workflow completed successfully. It found exactly one PPL utility-level net-metering row in each annual archive. The normalized standard net-metered PV capacity series is 76.686 MW in 2015, rising to 505.746 MW in 2025, an increase of 429.060 MW (559.5%) and a 20.76% compound annual growth rate over ten years. These are EIA-reported utility-level standard net-metered PV capacity values, not feeder hosting capacity or all DER capacity.

The annual PV customer/installations field is reported as `Customers` through 2020 and `Installations` beginning in 2021. The labels may describe similar cumulative measures, but they are retained as a measurement break pending confirmation from year-specific instructions. The capacity type is not separately reported in the 2015 PPL row; 2016–2025 report AC. Virtual PV capacity is not separately identified in the 2015 row, reported as a combined virtual capacity field in 2016–2022, and split into >=1 MW and <1 MW categories in 2023–2025. The normalized virtual capacity sums the later size bands, while preserving the source field names. The standard PV capacity series excludes those virtual capacity categories.

The 11-row harmonized dataset snapshot is committed at [data/ppl_net_metering_harmonized.csv](data/ppl_net_metering_harmonized.csv), with variable notes in [data/README.md](data/README.md). The annual archive hashes and full source-row provenance are retained in the CSV and workflow artifact. The full descriptive series, annual increments, sector composition, and measurement caveats are documented in [PPL Reported Net-Metered PV Capacity, 2015–2025](../../casebooks/pa-der-interconnection/eia861-ppl-net-metering-trend.md). The generated figure is available at [figures/ppl-standard-net-metered-pv-capacity.svg](figures/ppl-standard-net-metered-pv-capacity.svg). The 2015–2025 values are suitable for a descriptive trend analysis after a final source-instruction review. They do not identify the causal effect of PPL's Second DER Management Plan, Rule 12, or any other policy, and they do not measure feeder-level interconnection performance.

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
# EIA-861 2025 public-data pipeline

## Purpose

Build a reproducible inventory of the official 2025 final EIA-861 detailed-data ZIP before deciding which schedules support a Pennsylvania distribution/DER research question. The pipeline does not assume that every DER schedule is utility-specific or that EIA-861 contains feeder-level interconnection outcomes.

## Source and known limits

- Official source: [EIA Form 861 detailed data](https://www.eia.gov/electricity/data/eia861/).
- Direct 2025 final ZIP: https://www.eia.gov/electricity/data/eia861/zip/f8612025.zip.
- EIA describes Form 861 as a census of U.S. electric utilities and publishes separate schedules for service territory, reliability, distribution systems, utility data, net metering, and non-net-metered distributed generation.
- Net-metering and non-net-metered distributed-generation summaries are aggregated by state, sector, and balancing authority. They are not a PPL-specific project/interconnection queue or feeder hosting-capacity dataset.
- PPL Electric Utilities Corp is commonly identified as EIA utility ID 14715; the pipeline must confirm the identity from the downloaded EIA utility frame before attributing any rows to PPL.

## Run

    python -m pip install -r requirements.txt
    python inventory_eia861.py --archive data/raw/f8612025.zip --output-dir outputs/eia861-2025

If the archive is absent, the script downloads it from EIA. It verifies the ZIP CRC, calculates SHA-256, inventories every workbook and worksheet, and records the first 12 rows of each sheet for schema inspection. It extracts workbooks only into the output directory; raw and derived data are not committed to Git.

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
# PPL EIA-861 Derived Data Snapshot

The file in this directory is a 2015–2025 derived snapshot of the PPL Electric Utilities Corp utility-level Net Metering row from the annual EIA Form 861 detailed-data archives.

- Utility ID: 14715
- Observations: one per year, 2015–2025
- Main outcome: standard net-metered PV capacity (MW), with residential/commercial/industrial/transportation sector fields
- Source provenance: workbook, worksheet, row, and annual archive SHA-256 are retained in each row
- Transformation: research/data-pipelines/eia861/normalize_ppl_net_metering.py
- Raw source extraction: research/data-pipelines/eia861/extract_historical_net_metering.py

## Interpretation constraints

- 2015 capacity basis is not separately reported; do not use the 2015–2016 change as an AC-basis annual change.
- 2016–2025 standard PV capacity is reported on an AC basis.
- PV count labels change from Customers (2015–2020) to Installations (2021–2025).
- Virtual PV capacity is combined in 2016–2022 and summed from size bands in 2023–2025; it is missing in 2015.
- Missing values are blank, not zero. For example, 2025 transportation-sector PV capacity is blank; 2016 reports a numeric zero.
- This is reported standard net-metered PV capacity, not all installed PV, all DER, project interconnection outcomes, or feeder hosting capacity.

The source archives are public EIA data. The annual archive hashes and exact source-row provenance permit independent verification. Re-run the historical workflow and update this snapshot only after reviewing any new year-specific schema or survey-instruction changes.

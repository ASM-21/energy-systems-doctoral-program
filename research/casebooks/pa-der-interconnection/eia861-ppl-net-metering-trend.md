# PPL Reported Net-Metered PV Capacity, 2015–2025

**Research status:** Reproducible descriptive series; no causal estimate.  
**Respondent:** PPL Electric Utilities Corp, EIA utility ID 14715.  
**Unit:** Utility-year.  
**Primary source:** Annual EIA Form 861 final detailed ZIP archives, Net Metering workbook, PPL utility-level row.

## Executive result

EIA's annual 2015–2025 detailed archives each contain exactly one PPL utility-level net-metering row. The standard net-metered PV capacity series is available in all eleven years.

The most defensible comparison begins in 2016 because EIA explicitly reports the PV capacity basis as AC from 2016 onward. Reported standard net-metered PV capacity increased from 92.915 MW AC in 2016 to 505.746 MW AC in 2025: +412.831 MW, +444.31%, and a 20.7149% compound annual growth rate over nine years.

The 2015 row reports 76.686 MW but does not separately identify AC/DC basis. It is retained as a historical observation but excluded from comparable annual-change calculations and the AC-basis CAGR.

## Annual series

| Year | Standard PV capacity (MW) | Basis | PV count value | Count label | Virtual PV capacity (MW) | Comparable annual capacity change (MW) |
|---:|---:|---|---:|---|---:|---:|
| 2015 | 76.686 | Not separately reported | 3,554 | Customers | Not reported | — |
| 2016 | 92.915 | AC | 4,496 | Customers | 9.291 | — |
| 2017 | 112.757 | AC | 6,014 | Customers | 10.277 | 19.842 |
| 2018 | 133.851 | AC | 7,416 | Customers | 10.990 | 21.094 |
| 2019 | 158.398 | AC | 9,170 | Customers | 8.108 | 24.547 |
| 2020 | 186.727 | AC | 11,293 | Customers | 13.324 | 28.329 |
| 2021 | 212.677 | AC | 13,534 | Installations | 13.643 | 25.950 |
| 2022 | 256.071 | AC | 17,586 | Installations | 13.715 | 43.394 |
| 2023 | 349.083 | AC | 24,496 | Installations | 14.872 | 93.012 |
| 2024 | 414.331 | AC | 28,621 | Installations | 18.922 | 65.248 |
| 2025 | 505.746 | AC | 31,400 | Installations | 33.474 | 91.415 |

The annual capacity change is deliberately blank for 2016 because the preceding 2015 observation has no reported AC/DC type. Changes from 2017 onward compare AC observations. The count measure is labeled "Customers" through 2020 and "Installations" beginning in 2021; it should not be treated as a perfectly homogeneous series without reviewing the year-specific instructions.

Virtual capacity is reported as one combined PV virtual-capacity measure in 2016–2022. In 2023–2025 it is reported in two size categories; the table sums the >=1 MW and <1 MW categories. The 2015 row has no virtual-capacity field. Standard PV capacity and virtual PV capacity remain separate columns.

## Sector composition

The 2016 standard PV capacity row reports 29.061 MW residential, 52.823 MW commercial, and 11.031 MW industrial. In 2025, the corresponding values are 277.812 MW, 195.427 MW, and 32.507 MW. Residential therefore represents approximately 54.9% of standard net-metered PV capacity in 2025, compared with 31.3% in 2016. Commercial's share falls from approximately 56.9% to 38.6%, while industrial falls from approximately 11.9% to 6.4%.

These are shares of the standard net-metered PV capacity reported in the PPL row, not shares of all solar installed in PPL's territory. The 2025 transportation-sector field is blank, not zero; the three reported residential, commercial, and industrial values sum to the reported total. The 2016 transportation-sector value is a reported numeric zero. The sector categories and reported totals should be checked against the applicable annual schedule instructions before publication.

## Measurement and interpretation

1. **Capacity basis:** 2015 does not separately report the PV capacity type. The 2016–2025 PPL rows report AC. The 2015 point is not used to calculate the AC-basis growth rate.
2. **Count labels:** the PV count field is labeled "Customers" through 2020 and "Installations" from 2021. Preserve this break in any figure or model.
3. **Virtual PV:** 2016–2022 uses a combined virtual-capacity field; 2023–2025 separates >=1 MW and <1 MW categories. The normalized series sums the two later categories, while preserving the source field names.
4. **Missing values:** blanks and "." remain missing. They are not converted to zero. A numeric zero is retained as zero.
5. **Stock versus flow:** reported capacity and counts are cumulative stocks. First differences are changes in reported stocks, not necessarily the number or capacity of projects interconnected during that calendar year. Revisions, reclassification, and reporting changes can affect them.
6. **Scope:** this is standard net-metered PV capacity. It is not total installed PV, all DER, inverter nameplate capacity, annual generation, energy exported, or feeder hosting capacity.

## What the data do not establish

The EIA series cannot establish:
- the causal effect of PPL's Second DER Management Plan, Rule 12, or any other regulatory action;
- the number, MW, location, or disposition of PPL interconnection applications;
- distribution feeder loading, voltage headroom, thermal constraints, protection limits, or hosting capacity;
- non-net-metered PV adoption where PPL is not a respondent in the relevant utility-level schedule;
- actual DER curtailment, export behavior, or customer economics.

A 2023 increase of 93.012 MW in reported standard net-metered PV capacity is a descriptive observation. It is not evidence that a particular PPL policy caused the increase. A causal design would require treatment timing, a credible counterfactual, comparable outcome measurement, and controls for concurrent market and policy changes.

## Reproducibility

From `research/data-pipelines/eia861`:

    python -m pip install -r requirements.txt
    python audit_historical_coverage.py --start-year 2015 --end-year 2025
    python extract_historical_net_metering.py --start-year 2015 --end-year 2025
    python normalize_ppl_net_metering.py

The GitHub Actions workflow runs tests, audits all annual archives, extracts the PPL rows, harmonizes the standard PV series, and uploads the raw and derived outputs as an artifact. Each row retains its source workbook, worksheet, row number, and annual archive SHA-256.

## Sources

- [EIA Form 861 annual detailed data and schedule descriptions](https://www.eia.gov/electricity/data/eia861/)
- Official annual ZIP pattern for 2015–2024: `https://www.eia.gov/electricity/data/eia861/archive/zip/f861YYYY.zip`
- Official 2025 final ZIP: `https://www.eia.gov/electricity/data/eia861/zip/f8612025.zip`

The source workbook/sheet names and hashes are stored in the generated raw and harmonized CSVs and manifest. The source files are not committed to Git because the workflow artifact provides a reproducible, versioned extract without bloating the curriculum repository.

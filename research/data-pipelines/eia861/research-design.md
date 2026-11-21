# EIA-861 Research Design: PPL Distributed-Energy Adoption and Utility Outcomes

**Status:** Preliminary empirical descriptive result; causal analysis is not identified. Historical coverage and harmonization have been completed for 2015–2025.  
**Unit of analysis:** Utility-year only where EIA actually reports a utility-level observation; state-year or state-sector-year otherwise.  
**Primary source:** EIA Form 861 annual detailed files.

## 1. Research question

What can public EIA-861 data establish about the evolution of PPL Electric Utilities' customer-sited distributed-energy adoption and selected utility operating characteristics, and what cannot be inferred about distribution hosting capacity or interconnection performance?

This is deliberately a descriptive and measurement-first study. A single-utility time series does not identify the causal effect of PPL's DER Management Plan, Rule 12 changes, or any other policy. The design must not be upgraded to a causal claim merely because a time series is available.

## 2. Data hierarchy and release control

1. Use the official annual EIA-861 ZIP, not third-party re-hosted data, as the authoritative input.
2. Preserve the exact archive SHA-256, retrieval date, archive year, workbook, worksheet, row, column label, and reported unit.
3. Inspect each schedule's instructions and historical changes before combining years.
4. Distinguish Form EIA-861 from EIA-861S reporting and any imputed or adjusted values.
5. Retain the original source row and raw field names in the long-form extract. Build a separate, explicit crosswalk for harmonized variables.
6. Never convert missing rows, blank cells, suppressed values, or non-reporting to zero.

EIA states that Form EIA-861 is a census of U.S. electric utilities but that the short form has less detailed responses. EIA's schedule descriptions identify substantial definition changes: non-net-metered distributed generation was renamed in 2016, sector disaggregation and AC conversion adjustments were introduced, and Form EIA-861S imputation expanded in 2020. Although the generic net-metering schedule description emphasizes state/sector/balancing-authority reporting, the actual annual Net_Metering workbooks contain a utility-level PPL row in every year from 2015 through 2025. The row is located in Net_Metering_States (2015), Utility_Level-States (2016), States (2017–2022 and 2024), and States- Utility Level (2023 and 2025). The coverage audit checks the actual files, not just the generic webpage description.

## 3. Candidate variables and measurement rules

| Concept | Candidate variable | Unit | Main caveat |
|---|---|---|---|
| Net-metered PV adoption | Standard PV capacity | MW AC where specified | Confirm whether capacity is AC/DC, standard/virtual, and whether storage is paired |
| Net-metered PV adoption | Installation count | installations | Cumulative count, not annual additions |
| Virtual net metering | Virtual PV capacity by size band | MW | Keep below/above 1 MW categories separate |
| Other net-metered DER | Wind/other capacity | MW | Technology definitions may shift |
| Distribution-system scale | Number of distribution circuits | circuits | May be reported only at aggregate geography |
| AMI deployment | AMI meters | meters | Coverage and definitions may change |
| Reliability | SAIDI / SAIFI | minutes / interruptions per customer | Reporting conditions and major-event treatment must be retained |
| Utility scale | Peak demand, customers, sales | MW / customers / MWh | Service-type categories must not be double-counted |

A cumulative installation count should not be interpreted as annual installations. To derive an annual change, calculate first differences only for consecutive, comparable observations and flag any discontinuity in definition, respondent, or reporting basis. A negative first difference may indicate reclassification, revision, acquisition, or reporting correction rather than physical DER removal.

## 4. Historical audit decision gate

The historical coverage audit and raw extraction have now been run for 2015–2025. Each annual archive contains exactly one PPL utility-level net-metering row in the relevant schedule. The standard net-metered PV capacity series is 76.686 MW in 2015 (AC/DC basis not separately reported) and 505.746 MW in 2025 (AC). The comparable AC-basis series rises from 92.915 MW in 2016 to 505.746 MW in 2025 (+412.831 MW; +444.31%; 20.7149% CAGR). The normalized file preserves source field names, archive hashes, and annual source-row provenance. This is a measured utility-level reported-capacity series, not feeder hosting capacity.

- **Observed result:** the 2015–2025 archives each contain one PPL net-metering row. Use the 2016–2025 AC series for comparable growth calculations; retain 2015 as a historical observation with unknown capacity basis. Keep the Customers-to-Installations count-label break in 2021 explicit.
- The workflow extracts Pennsylvania EDC utility-level net-metering rows for 2015–2025, excludes third-party-owned (TPO) schedules and administrative adjustment rows, and records those exclusions in the archive manifests. It then runs a separate coverage/identity audit. The audit reports annual utility-ID coverage, duplicate year/ID keys, and respondent-name variants. Its output is a diagnostic artifact, not a harmonized panel; no cross-utility growth or estimation is authorized by this step alone. Do not calculate cross-utility growth or estimate a treatment effect until EIA IDs, survey forms, definitions, units, service territories, and reporting changes have been reconciled.
- **Next decision gate:** inspect the generated audit artifact and source workbook schemas. Only then decide whether any candidate fields support a comparable utility-year panel. If peer utilities have comparable rows, construct a panel only after verifying consistent EIA IDs, respondent form, schedule definitions, service territories, and variable units. Report the unbalanced panel and missingness mechanism.

The audit is a data-feasibility step, not a reason to select a favorable sample after looking at outcomes. Preserve the full set of candidate utilities and years in the coverage manifest.

## 5. Descriptive analysis

For each comparable variable:

1. Plot levels and, separately, first differences.
2. Show observation coverage alongside the series.
3. Report units and denominators on every figure.
4. Annotate known survey-definition and tariff/order milestones without implying causation.
5. Compare PPL observations with Pennsylvania totals only when the geographic and respondent definitions align.
6. Run sensitivity checks excluding years affected by reporting-form or definition changes.
7. Report missingness explicitly and never silently fill gaps.

Potential figures:
- cumulative standard net-metered PV capacity and its AC-basis annual changes;
- PV capacity by residential, commercial, and industrial customer sectors;
- virtual PV capacity, with the combined-to-size-band definition change annotated;
- annual changes in cumulative capacity, with missing years shown as gaps;
- EIA schedule coverage heatmap by year and workbook;
- PPL reliability and AMI indicators, if their reporting bases are comparable;
- Pennsylvania state-level DER adoption alongside PPL utility-level values, with clear separation of geographic units.

## 6. Causal inference: what would be required

A causal estimate of a PPL DER policy effect would require a defensible counterfactual and treatment timing, not merely a before/after graph. Potential designs are only exploratory until data support them:

- **Comparative interrupted time series:** requires a sufficiently long, stable PPL series and one or more credible comparison utilities not exposed to the same intervention.
- **Difference-in-differences:** requires a defined treatment, untreated comparison group, multiple pre-treatment periods, plausible parallel trends, no differential concurrent shocks, and stable measurement.
- **Event study:** requires enough observations around the event and transparent pre-trend diagnostics; event-time coefficients do not solve selection or measurement problems.
- **Synthetic control:** requires a long pre-period and a donor pool with comparable outcomes and no spillovers. Utility-level EIA schedule coverage may be too sparse.

Potential confounders include state net-metering policy, federal tax incentives, retail rates, equipment prices, utility service-territory composition, customer income and housing stock, interconnection rules, interest rates, supply-chain constraints, weather, and reporting changes. The PPL Second DER Management Plan's projected hosting-capacity effect is not a treatment outcome. Any causal design must identify the actual implementation date, mechanism, and measurable outcome from primary records.

## 7. Engineering boundary

EIA-861 does not provide feeder topology, conductor impedances, phase allocation, transformer loading, protection settings, voltage profiles, queued project locations, interconnection study results, upgrade costs, or DER curtailment. Aggregate DER capacity is not hosting capacity. A change in utility-level PV capacity cannot be translated into feeder headroom.

The engineering workstream should therefore remain separate: use the IEEE 13-node OpenDSS benchmark to test methods and assumptions, and use public PPL tariffs and filings to reconstruct institutional rules. Never calibrate the synthetic feeder to EIA totals and then present the result as an observed PPL feeder.

## 8. Required deliverables

- archive and worksheet coverage manifest;
- raw long-form PPL extract with source provenance;
- variable dictionary and historical crosswalk;
- reproducible descriptive notebook or script;
- figures with observation-coverage annotations;
- a 1,500–2,000 word measurement and limitations memo;
- a separate causal-identification memo explaining whether any quasi-experimental design is feasible.

## 9. Stop/go criteria

**Go** to a utility-year descriptive panel only if the audit finds repeated, comparable utility-level observations.  
**Go** to a broader peer panel only if the coverage and schema are comparable across utilities and years.  
**No-go** for causal estimation until treatment timing, a credible comparison group, sufficient pre-periods, and outcome measurement are established.  
**No-go** for feeder-level hosting-capacity estimation from EIA-861 alone.

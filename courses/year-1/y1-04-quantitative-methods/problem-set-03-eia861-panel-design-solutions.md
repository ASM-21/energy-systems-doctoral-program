# Solution Notes: EIA-861 Measurement, Panel Data, and Causal Identification

## Problem 1

Utility-year observations are tied to a named respondent and its EIA utility ID. State-sector-year aggregates describe a broader geography/sector and cannot be attributed to an individual EDC. A utility-level worksheet discovered in 2025 must be checked against every historical archive because schedules and workbook structures can change. The 2016 schedule rename/sector split and AC conversion adjustments, plus 2020 EIA-861S imputation changes, can create breaks in comparability. Blank sold-back fields may indicate unavailable reporting, not zero exports.

## Problem 2

The first difference is 2,500 installations. It can be interpreted as net additions only if both observations measure the same cumulative population under comparable definitions and coverage, the respondent is consistent, and revisions/reclassifications are accounted for. Negative differences can reflect respondent changes, survey corrections, technology reclassification, mergers, or changed reporting/estimation. Counts and MW differ because system sizes vary; capacity can rise with flat installation count and vice versa.

## Problem 3

MCAR means missingness is unrelated to observed or unobserved data; MAR means it is explainable by observed variables; MNAR means missingness depends on unobserved values or the missingness process itself. Form/reporting changes and schedule eligibility make MCAR implausible by default. Interpolation invents values and can conceal structural breaks. The coverage table should record every schedule-year, whether the utility ID field exists, whether the respondent frame indicates reporting, whether a PPL row is found, form type, and the reason for any absence. Comparability requires matching definitions, units, reporting form, aggregation level, respondent identity, and treatment of imputed/adjusted values.

## Problem 4

The proposed treatment is PPL exposure after the Second DER Management Plan; the statewide series is not a valid independent control because it includes PPL and shares statewide policies, market conditions, and macro shocks. DiD requires parallel trends, no anticipation, no spillovers, stable measurement, no differential concurrent intervention, and a well-defined treatment/outcome. A projected hosting-capacity increase is not a measured adoption, interconnection, or hosting-capacity outcome. A credible comparison would need untreated utilities with comparable data and policy exposure, a long pre-period, and documented treatment timing. If these are unavailable, do not estimate a causal effect.

## Problem 5

The completed 2015–2025 audit found exactly one PPL utility-level net-metering row in each annual archive. A PPL descriptive series is therefore feasible. Use the 2016–2025 AC-basis standard PV capacity series (92.915 to 505.746 MW) for comparable growth calculations; do not calculate the 2015–2016 change because 2015 does not separately report AC/DC basis. Retain the 2021 count-label change from Customers to Installations, and the virtual-capacity reporting change in 2023. A multi-utility panel remains conditional on peer coverage and comparable definitions. The memo must state that EIA-861 does not contain feeder engineering variables or project-level interconnection outcomes and therefore cannot estimate feeder hosting capacity or PPL interconnection performance.

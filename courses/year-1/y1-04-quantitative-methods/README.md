# Y1-04 — Applied Quantitative Methods for Energy Research

**Status:** Active Year 1 course

**Level:** Graduate methods foundation | **Duration:** 10–12 weeks | **Effort:** 35–45 hours  
**Prerequisites:** Calculus, linear algebra, probability/statistics, Python or R.

## Purpose
Establish a reproducible quantitative workflow for energy-sector analysis. This introduces empirical reasoning and regression; it does not claim to provide doctoral-level econometric mastery. Advanced causal inference, panel data, and time series belong in Year 2.

## Learning outcomes
Formulate a quantitative question and identify its unit of analysis; acquire, inspect, clean, and document public data; distinguish description, prediction, and causal inference; fit and interpret OLS; explain assumptions and failure modes; diagnose missingness, outliers, heteroskedasticity, multicollinearity, and serial dependence; use version control; communicate uncertainty without causal overclaiming.

## Weekly sequence
| Week | Topic | Work |
|---|---|---|
| 1 | Research questions, estimands, units, provenance | Design worksheet |
| 2 | Data acquisition, schemas, missingness, cleaning | Data audit |
| 3 | Descriptive statistics and visualization | Exploratory notebook |
| 4 | Probability, sampling, confidence intervals, tests | Problem set 1 |
| 5 | Simple and multiple OLS | Regression notebook |
| 6 | Functional form, interactions, interpretation | Problem set 2 |
| 7 | Diagnostics, robust errors, specification | Diagnostic report |
| 8 | Time-indexed data, seasonality, autocorrelation | Time-series exploration |
| 9 | Prediction versus causal inference | Identification memo |
| 10 | Reproducibility, Git, testing, documentation | Clean rerun |
| 11 | Sensitivity and uncertainty communication | Results review |
| 12 | Final empirical project | Paper and repository |

## References
Wooldridge, *Introductory Econometrics: A Modern Approach*, 8th ed. (2025; [publisher page](https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161)); Angrist & Pischke, *Mostly Harmless Econometrics* (selected chapters); [OpenIntro Statistics](https://www.openintro.org/book/os/); [NIST/SEMATECH Statistical Methods](https://www.itl.nist.gov/div898/handbook/); [EIA Open Data](https://www.eia.gov/opendata/); [FRED](https://fred.stlouisfed.org/).

## Assessments
Data provenance/quality audit; descriptive analysis with defensible plots; OLS derivation and interpretation; diagnostic/specification memo; final reproducible empirical analysis using public data.

## Final project
Select a narrow descriptive or associational question using public energy, economic, or infrastructure data. State clearly whether the design supports causal inference. Include question, data dictionary, cleaning and analysis scripts, exploratory figures, model and diagnostics, uncertainty, limitations, and concise interpretation.

A clean environment must reproduce tables and figures from raw or documented source data. Statistical significance is not proof of causality.

## Problem sets and worked checks
- [Problem Set 1](problem-set-01.md)
- [Solution notes](problem-set-01-solutions.md)

- [Problem Set 2](problem-set-02.md)
- [Problem Set 2 solution notes](problem-set-02-solutions.md)


## Computational and empirical workflows
- [OLS and robust inference on synthetic energy-demand data](../../../projects/econometrics/ols-energy-demand/README.md)
- [EIA-861 public-data ingestion and panel audit](../../../research/data-pipelines/eia861/README.md) — inspect source workbooks, schema changes, utility identity, coverage, exclusions, and panel limitations. The pipeline is a data-engineering and measurement exercise; it does not by itself identify causal effects.

## How to use the assessments

Attempt each problem set before opening the linked worked solution. For empirical work, define the unit of analysis, preserve data provenance, inspect missingness and measurement changes, and distinguish description from causal identification. Re-run the analysis from a clean environment and retain the code and data dictionary.

## Next step

Proceed to [Y1-03 — Electricity Markets, Utility Regulation, and PJM](../y1-03-markets-regulation-pjm/README.md), then complete the [Year 1 integration project](../README.md#integration-project).

# Y1-04 — Applied Quantitative Methods for Energy Research

**Status:** Active Year 1 course  
**Level:** Graduate methods foundation  
**Prerequisites:** Calculus, linear algebra, introductory probability/statistics, and Python or R. Basic Git is recommended; use the [software setup guide](../../../resources/software-setup.md) if needed.  
**Planned effort:** **40 hours** (35–45 hour planning range), normally 8–14 weeks at 3–5 hours per week.
**Position in sequence:** May begin after the basic quantitative prerequisites are comfortable. It can overlap with Y1-01/Y1-02 and should precede the Year 2 econometrics sequence.

## Purpose

Establish a reproducible quantitative workflow for energy-sector analysis. The course covers measurement, data provenance, descriptive statistics, OLS, uncertainty, diagnostics, and responsible interpretation. It deliberately stops short of advanced causal estimation: panel identification, difference-in-differences estimators, instrumental variables, regression discontinuity, and advanced time-series methods are developed in Year 2.

## Learning outcomes

By the end, the learner should be able to:

1. Translate a substantive energy question into a defined unit of analysis, outcome, explanatory variables, and estimand or descriptive target.
2. Acquire, inspect, clean, and document public data while preserving provenance and raw source files.
3. Audit schemas, missingness, units, respondent identity, aggregation levels, and changes in measurement definitions.
4. Calculate and interpret descriptive statistics, sampling uncertainty, confidence intervals, and basic hypothesis tests.
5. Derive and interpret simple and multiple OLS regression, including coefficients, fitted values, residuals, and uncertainty.
6. Explain omitted-variable bias, functional-form problems, heteroskedasticity, and multicollinearity at an introductory level.
7. Distinguish descriptive, predictive, and causal claims and identify why a proposed causal design may fail.
8. Build a reproducible analysis with documented software, version control, tests, data dictionary, and clean rerun instructions.

## Learning sequence

| Stage | Topic | Required evidence |
|---|---|---|
| 1 | Research questions, units, estimands, and data provenance | Design worksheet |
| 2 | Data acquisition, schemas, missingness, cleaning | Data audit |
| 3 | Descriptive statistics, sampling, and uncertainty | PS1 and exploratory notebook |
| 4 | Simple/multiple OLS, functional form, interpretation | PS2 and regression notebook |
| 5 | Diagnostics, robust standard errors, specification | Diagnostic memo |
| 6 | Public-data measurement and panel feasibility | PS3 and EIA-861 audit |
| 7 | Reproducibility, sensitivity, and communication | Clean rerun and final project |

## Core materials

- Wooldridge, Jeffrey M. *Introductory Econometrics: A Modern Approach*, 8th ed. Cengage, 2025. [Publisher page](https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161).
- Diez, David M., Christopher D. Barr, and Mine Çetinkaya-Rundel. *OpenIntro Statistics*. [Free online text](https://www.openintro.org/book/os/).
- NIST/SEMATECH, *e-Handbook of Statistical Methods*. [Online handbook](https://www.itl.nist.gov/div898/handbook/).
- Angrist, Joshua D., and Jörn-Steffen Pischke. *Mostly Harmless Econometrics*. Princeton University Press, 2009. Selected conceptual chapters; the full causal toolkit belongs to Year 2.
- U.S. Energy Information Administration, [Open Data](https://www.eia.gov/opendata/) and [Form EIA-861](https://www.eia.gov/electricity/data/eia861/).

## Required assessments

| ID | Assignment | Planned hours | Purpose |
|---|---|---:|---|
| PS1 | [Statistical reasoning and OLS](problem-set-01.md) / [solution notes](problem-set-01-solutions.md) | 3 | Sampling, regression derivation, inference |
| PS2 | [Multiple regression and model diagnostics](problem-set-02.md) / [solution notes](problem-set-02-solutions.md) | 3 | Specification and interpretation |
| PS3 | [EIA-861 measurement and panel feasibility](problem-set-03-eia861-panel-design.md) / [solution notes](problem-set-03-eia861-panel-design-solutions.md) | 4 | Data measurement and identification audit |
| LAB1 | [OLS and robust inference](../../../projects/econometrics/ols-energy-demand/README.md) | 4 | Reproducible regression workflow |
| LAB2 | [EIA-861 data audit and reproducible pipeline](../../../research/data-pipelines/eia861/README.md) | 5 | Source ingestion, schema, identity, coverage |
| COURSE | Empirical analysis and self-assessment | 21 | Integrated final project |

Total planned effort: **40 hours**. The course tracker is the planning baseline.

## Assessment structure

- Problem sets and derivations: 25%.
- Computational/data workflows: 25%.
- Final reproducible empirical project: 40%.
- Provenance, clean rerun, and self-assessment: 10%.

Use the [program rubric](../../../ACADEMIC_STANDARDS.md). These are internal self-assessment weights, not university grades.

## Required final project

Select a narrow descriptive or associational question using public energy, economic, or infrastructure data. The EIA-861 project may be used if the data feasibility review supports it. Submit:
- a research question and unit-of-analysis statement;
- a data dictionary and source register;
- raw-data provenance and documented cleaning scripts;
- exploratory figures and descriptive analysis;
- an OLS model where appropriate, with interpretation and diagnostics;
- uncertainty and sensitivity discussion;
- a limitations section explaining why causal language is or is not justified;
- clean rerun instructions and a concise written report.

A clean environment must reproduce tables and figures from raw or documented source data. Statistical significance is not proof of causality.

## Scope boundary

The EIA-861 panel exercise is primarily a measurement and feasibility assignment. It introduces treatment/control and parallel-trends concepts as a critique of research design, but it does not require the learner to estimate a difference-in-differences model. Advanced causal estimators belong to the Year 2 econometrics course. Do not promote a public aggregate series into a project-level or feeder-level outcome.

## Completion gate

Attempt and correct all three problem sets; reproduce and modify both computational/data workflows; submit the final reproducible analysis and self-assessment; and record actual hours and evidence in the progress tracker. Use the [program rubric](../../../ACADEMIC_STANDARDS.md). Reading a solution or running a prebuilt pipeline without explaining its measurement choices is not completion evidence.

## Next step

Proceed to [Y1-03 — Electricity Markets, Utility Regulation, and PJM](../y1-03-markets-regulation-pjm/README.md). Then complete the [Year 1 integration project](../README.md#integration-project) before entering the advanced Year 2 econometrics sequence.

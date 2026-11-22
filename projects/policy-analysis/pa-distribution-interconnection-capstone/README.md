# Research Capstone: Pennsylvania Distribution DER Interconnection

**Status:** Reproducible descriptive baseline and research design; not a causal evaluation  
**Data window:** PUC reporting years 2023–2025 (June 1 through May 31)  
**Unit:** Electric distribution company (EDC) service territory × reporting year  
**Data source:** Pennsylvania PUC, *Net-Metering and Interconnection Report 2023–2025*  
**Source data:** `research/casebooks/pa-der-interconnection/pa_edc_interconnection_2023_2025.csv`

## Research question

How did reported DER interconnection request volumes and their distribution across Pennsylvania EDC service territories evolve from reporting year 2023 through 2025, and what additional data would be required to evaluate whether process changes affected project outcomes?

This is a measurement-first study. It does not assume that high request volume means poor performance, that lower request volume means faster processing, or that differences between EDCs reflect utility effectiveness. It does not estimate a causal effect of PPL Rule 12, DERMS deployment, or any other intervention.

## Reproduce

From the repository root:

```bash
cd projects/policy-analysis/pa-distribution-interconnection-capstone
python -m unittest -v
python analyze.py --output-dir outputs
```

The analysis uses only Python's standard library. It reads the source panel from the casebook rather than maintaining a second copy of the data. Outputs:

- `summary.json`: annual summary, interpretation limits, and 2025 large-request composition.
- `annual_summary.csv`: statewide totals, PPL rank/share, request-count HHI, and top-three EDC share.
- `edc_year_panel.csv`: 33 EDC-year observations with request mix, statewide share, and prior-year change.

## Initial descriptive findings

The underlying PUC data report 19,202 requests in 2023, 18,582 in 2024, and 20,202 in 2025. All 11 EDC totals reconcile to the statewide totals in each year. PPL had the largest request count in all three reporting years: 7,567, 7,519, and 6,844, respectively. Its statewide request share was 39.41%, 40.46%, and 33.88%.

The HHI calculated from EDC shares of reported request counts was approximately 2,487, 2,496, and 2,073 across the three years. This is a concentration statistic for the distribution of applications across service territories. It is not the conventional product-market HHI and says nothing by itself about retail market power or utility competition. It is affected by customer base, territory size, load, installed DER, and reporting definitions.

In 2025, PPL reported 135 Level 2 requests at or above 500 kW out of 196 statewide, and 411 Level 3 requests at or above 500 kW out of 954 statewide. The 500 kW split is not reported on a comparable basis in the 2023 and 2024 tables.

## Empirical design

### 1. Measurement and data validation

- Reconcile Level 1–4 request counts to each EDC's reported total.
- Reconcile EDC totals to the PUC statewide total for every year.
- Verify a balanced panel of 11 EDC territories and 3 reporting years.
- Retain the PUC reporting-year definition (June 1–May 31).
- Keep 2025 500 kW subcategories separate from 2023–2024 measures.

### 2. Descriptive analysis

Report annual request totals, EDC shares, PPL rank, top-three share, and request-count HHI. Report year-over-year changes, while clearly distinguishing changes in counts from changes in rates. A rate requires an appropriate exposure denominator such as customer count, annual load, or DER applications eligible to enter the process. These denominators are not in this panel.

### 3. What not to estimate

Do not estimate approval rates from aggregate request counts. The PUC report's status categories are not a linked cohort table and do not provide project-level transitions. Do not divide approvals by requests submitted in the same reporting year and label the result a completion probability. Do not rank mean review times until definitions, zero values, project mix, and denominator rules have been independently reconciled. Do not run a causal panel regression on 33 EDC-year observations and interpret fixed effects as solving selection, policy timing, or measurement problems.

### 4. Follow-on identification design

A credible evaluation of a process change would require application-level records with, at minimum:

- application identifier and EDC/feeder identifiers (appropriately de-identified);
- received, completeness, study, approval, agreement, construction, and permission-to-operate dates;
- review level and every review-level transition;
- technology, nameplate capacity, inverter characteristics, export status, and storage pairing;
- study-required upgrades, cost estimates, actual upgrade scope, and cost responsibility;
- withdrawal, cancellation, denial, and completion reason codes;
- applicable tariff/rule version and the date each application became subject to it;
- relevant feeder/substation conditions or defensible public proxies;
- customer, project, and application cohorts to distinguish right-censoring from final outcomes.

Potential designs include survival analysis for time-to-decision with right-censoring, competing-risks models for approval/withdrawal/denial, and carefully justified difference-in-differences only if there is a defensible comparison group, stable measurement, credible parallel trends, and no material concurrent intervention. An aggregate annual EDC panel is not enough to establish those conditions.

## Economic and regulatory interpretation

Interconnection is a multi-stage process under engineering constraints and regulatory rules. A request count measures workload entering a reported process, not the amount of DER that can be safely accommodated, the amount ultimately installed, the cost of necessary upgrades, or the value of a project. Larger applications may create different study burdens, but review-level classifications and thresholds must be checked against the governing Pennsylvania code and tariff version.

A policy brief should distinguish:
1. the physical interconnection process;
2. utility distribution planning and operational limits;
3. state PUC tariff and regulatory oversight;
4. wholesale aggregation participation under PJM/FERC rules;
5. customer adoption and project economics.

Do not conflate the 60-day review for a DERA participation request under the proposed Pennsylvania Chapter 57 framework with physical interconnection study timelines under Rule 12.

## Required final deliverables

1. A 6,000–8,000 word research paper with abstract, literature review, institutional map, data section, descriptive results, limitations, and a future identification design.
2. Reproducible code and machine-readable outputs.
3. A data provenance and version register.
4. A 2-page policy brief with recommendations explicitly labeled as evidence-based, provisional, or requiring further data.
5. A 10-minute technical presentation and a defense of the unit of analysis, measurement choices, and rejected causal claims.

## Acceptance criteria

- Every reported total reconciles to the PUC source.
- Every derived metric can be regenerated from the committed source panel.
- No project-level outcome, rate, or causal effect is claimed from aggregate data.
- The difference between a request, an approval, an interconnected installation, and installed capacity is maintained throughout.
- The final paper explains how the data's reporting period relates to Rule 12's January 2026 applicability and implementation milestones.
- All employer-confidential, customer-identifiable, or nonpublic utility information is excluded.

## Primary sources

- Pennsylvania PUC, [Net-Metering and Interconnection Report 2023–2025](https://www.puc.pa.gov/media/3770/net-metering-interconnection-report-2023-2025_final.pdf).
- Pennsylvania Code, [52 Pa. Code Chapter 75](https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/052/chapter75/chap75toc.html).
- PPL, [Rule 12 DER Interconnection Service](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/2026/August/Rule-12---Distributed-Energy-Resource-Interconnection-Service.pdf).
- PPL, [DER Management Program](https://www.pplelectric.com/site/More/For-Construction/DER-Management).
- PJM, [DER Aggregator Participation Model materials](https://www.pjm.com/markets-and-operations/advanced-metering-infrastructure/der-aggregator-participation).

# Y2-03 — Infrastructure Economics and Utility Investment

**Status:** Planned; Problem Sets 1–5 and worked solutions/guidance are available. The computational companion and final course synthesis remain in development.  
**Level:** Graduate / applied regulatory economics  
**Prerequisites:** Y1-02 Energy Economics and Y1-03 Markets, Regulation, and PJM or equivalent; introductory corporate finance, calculus, and statistics.  
**Planned effort:** 30–40 hours over approximately 10–14 weeks at 2.5–3 hours per week, studied as the primary course within the total 3–5 hour weekly program budget.  
**Position in sequence:** Applied bridge between energy economics, utility regulation, infrastructure capital planning, and investment policy.

## Course question

How should a regulated utility evaluate, finance, propose, and operate long-lived infrastructure when costs, benefits, risks, and decision rights are distributed across customers, shareholders, regulators, and the wider power system?

This course treats the utility as both an engineering organization and a regulated investment institution. It does not assume that an accounting return is equivalent to economic value, that a proposed project is prudent because it is technically feasible, or that a lower unit cost necessarily produces a lower customer bill.

## Learning outcomes

By the end of the course, the learner should be able to:

1. Reconstruct a simplified revenue requirement from operating expenses, depreciation, taxes, rate base, and allowed return.
2. Explain how original cost, accumulated depreciation, construction work in progress, and used-and-useful standards affect regulated rate base.
3. Calculate WACC and distinguish the cost of capital from the allowed return established in a regulatory proceeding.
4. Explain the regulatory lag and incentive properties of cost-of-service regulation, formula rates, performance-based mechanisms, and multi-year rate plans.
5. Compare fixed, volumetric, demand, time-of-use, and dynamic rate designs using cost causation, efficiency, equity, and revenue adequacy.
6. Evaluate utility investment under uncertainty using discounted cash flow, scenario analysis, sensitivity analysis, and real-options reasoning.
7. Distinguish project costs, revenue requirements, customer bill impacts, societal benefits, and transfers between parties.
8. Analyze who bears construction, utilization, technology, regulatory, and stranded-asset risk.
9. Read a rate case or utility filing with a traceable evidence hierarchy, separating testimony, settlement proposals, commission findings, and operative orders.
10. Produce a transparent investment and regulatory analysis with reproducible calculations and a limitations statement.

## Course sequence

| Module | Topic | Approx. effort |
|---|---|---:|
| 1 | Utility financial statements and regulatory accounting | 4 h |
| 2 | Rate base, depreciation, and revenue requirement | 5 h |
| 3 | Capital structure, WACC, and allowed return | 4 h |
| 4 | Cost allocation and rate design | 5 h |
| 5 | Regulatory incentives, lag, and performance regulation | 4 h |
| 6 | Capital budgeting, uncertainty, and real options | 5 h |
| 7 | Distribution investment, DER, and cost recovery | 4 h |
| 8 | Regulatory filing analysis and synthesis | 5–9 h |

## Core analytical framework

A simplified annual revenue requirement can be written as:

`RR = OPEX + DEP + TAX + rB - REV_{other}`

where OPEX is allowed operating expense, DEP is depreciation, TAX is applicable tax expense, `r` is the allowed rate of return, `B` is the relevant rate base, and `REV_other` represents other revenues or credits recognized in the simplified model.

This identity is a teaching model, not a universal tariff formula. Actual jurisdictional accounting can include income-tax normalization, accumulated deferred income taxes, working capital, regulatory assets and liabilities, cost-of-service adjustments, riders, and other details. The learner must identify the accounting and legal treatment used in the actual proceeding.

The weighted average cost of capital is commonly represented as:

`WACC = w_d k_d (1-T) + w_e k_e`

for a simplified debt/equity capital structure with tax-deductible interest. Regulatory return methodologies and tax treatment vary. Do not substitute a textbook WACC for the commission-authorized return without examining the record and order.

## Problem sets and evidence

- [Problem Set 1: Revenue requirement, rate base, and WACC](problem-set-01-revenue-requirement.md)
- [Problem Set 1 solution notes](problem-set-01-revenue-requirement-solutions.md)\n- [Problem Set 2: Cost allocation and retail rate design](problem-set-02-cost-allocation-rate-design.md)\n- [Problem Set 2 solution notes](problem-set-02-cost-allocation-rate-design-solutions.md)\n- [Problem Set 3: Regulatory lag, incentives, and performance regulation](problem-set-03-regulatory-lag-incentives.md)\n- [Problem Set 3 solution notes](problem-set-03-regulatory-lag-incentives-solutions.md)\n- [Problem Set 4: Utility capital budgeting under uncertainty](problem-set-04-capital-budgeting-uncertainty.md)\n- [Problem Set 4 solution notes](problem-set-04-capital-budgeting-uncertainty-solutions.md)\n- [Problem Set 5: Pennsylvania distribution investment and DER integration case](problem-set-05-pennsylvania-distribution-investment-case.md)\n- [Problem Set 5 assessment guide](problem-set-05-pennsylvania-distribution-investment-case-guide.md)\n- [Computational companion: utility regulatory economics](../../../projects/energy-economics/utility-regulatory-economics/README.md)

The Pennsylvania distribution investment case is now specified with a detailed evidence rubric. A computational companion makes the cost-allocation, rate-design, incentive, and capital-budgeting calculations reproducible. The final course synthesis must integrate the case memo, source register, risk register, and tested model. Each assignment distinguishes accounting identities from economic welfare claims.

## Recommended references

- Kahn, Alfred E. *The Economics of Regulation: Principles and Institutions*. MIT Press, 1988 reprint. Foundational treatment of regulation, cost allocation, and incentives.
- Bonbright, James C., Albert L. Danielsen, and David R. Kamerschen. *Principles of Public Utility Rates*. Public Utilities Reports, 1988. Classic treatment of rate design and regulatory principles.
- Phillips, Charles F. *The Regulation of Public Utilities: Theory and Practice*. Public Utilities Reports, 1993.
- Joskow, Paul L. “Incentive Regulation in Theory and Practice: Electricity Distribution and Transmission Networks.” In *Economic Regulation and Its Reform: What Have We Learned?*, University of Chicago Press, 2014.
- FERC, *Uniform System of Accounts Prescribed for Public Utilities and Licensees*, 18 CFR Part 101: https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-101
- NARUC, *Electric Utility Cost Allocation Manual*, 1992. Use as a methodological reference, not as a substitute for the applicable state commission's rules.

## Research and practical relevance

The course's applied work should use public commission dockets, utility annual reports, FERC Form 1, EIA data, tariff sheets, and publicly available planning documents. A Pennsylvania case may examine how distribution investment is proposed, reviewed, allocated, and recovered, but must distinguish PPL's public filings from internal utility information. Never use confidential customer, operational, or employer data.

## Computational and empirical work

A standard-library Python companion now implements separate cost-pool allocation, three-part tariff arithmetic, representative bills, simplified regulatory-incentive comparisons, annuity factors, and scenario-weighted NPV. Unit tests check reconciliation and benchmark calculations. It is a synthetic teaching model, not a tariff engine or rate-case accounting system. Further work should add class-specific bill distributions, alternative allocators, and more detailed stochastic investment models using public data only.

Useful public sources include [FERC Form 1](https://www.ferc.gov/industries-data/electric/general-information/electric-industry-forms/form-1), [EIA electricity data](https://www.eia.gov/electricity/data/), and the [Pennsylvania PUC](https://www.puc.pa.gov/). The applied case must identify the proceeding's legal status and test year, and must not use confidential employer or customer records.

## Assessment architecture

| Assessment | Weight | Course modules |
|---|---:|---|
| Problem Set 1: Revenue requirement, rate base, and WACC | 15% | 1–3 |
| Problem Set 2: Cost allocation and rate design | 15% | 4 |
| Problem Set 3: Regulatory lag and performance regulation | 15% | 5 |
| Problem Set 4: Capital budgeting under uncertainty | 15% | 6 |
| Problem Set 5: Pennsylvania distribution investment case | 40% | 7–8 |
| **Total** | **100%** | |

The weights are the planned grading architecture for the complete course. Problem Sets 1–4 test transferable analytical methods; Problem Set 5 is the integrative applied case. A submission must meet the [program rubric](../../../ACADEMIC_STANDARDS.md), regardless of numerical score. The course is not activated until the case materials and computational companion pass review.

## Assessment standard

A strong submission:
- defines the regulatory jurisdiction and relevant test year;
- cites primary source documents and identifies their legal status;
- reconciles units, dollars, years, and nominal/real assumptions;
- makes each calculation reproducible;
- separates accounting treatment from economic interpretation;
- tests sensitivity to major assumptions;
- identifies who pays, who benefits, and who bears downside risk;
- states what the available evidence cannot establish.

## Completion evidence

Submit a revenue-requirement workbook or script, a short rate-design comparison, a source register for one public regulatory proceeding, and a 2,000–3,000 word investment memo consistent with Problem Set 5. A model without a clear institutional interpretation is incomplete.


## Completion gate

The course remains planned until the computational companion is independently reviewed, the Pennsylvania case has a completed exemplar or instructor-quality benchmark, and the final course synthesis and workload have been reviewed. When activated, completion should require:
- all required problem sets attempted and corrected;
- a reproducible revenue-requirement and rate-design model;
- a primary-source review of one public rate proceeding;
- a sensitivity analysis that identifies who bears material risks;
- a 2,000–3,000 word investment/regulatory memo;
- a self-assessment against the [program rubric](../../../ACADEMIC_STANDARDS.md).

The currently published Problem Sets 1–5 are assessed modules, not evidence that the full course is ready or complete.

## Next step

Complete the Pennsylvania case using a current public docket, then integrate the calculations into a single source-traceable investment memo. Then use the [Y2-04 market-design sequence](../electricity-market-design-optimization/README.md) or the Year 2 research capstone to integrate engineering constraints, market outcomes, and utility investment incentives. This course remains planned until its full assessment set and applied case have been reviewed.

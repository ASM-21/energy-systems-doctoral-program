# Problem Set 2: Cost Allocation and Retail Rate Design

**Level:** Graduate applied regulatory economics  
**Suggested effort:** 3–4 hours  
**Prerequisites:** Problem Set 1; introductory statistics and spreadsheet arithmetic

Show units, allocation factors, intermediate calculations, and assumptions. This is a stylized teaching case. It is not a cost-of-service study, tariff recommendation, or estimate for a named utility.

## Case: Two customer classes

A distribution utility has an approved annual distribution revenue requirement of $100 million for this exercise. A functional cost study assigns the requirement to three cost pools:

| Cost pool | Annual revenue requirement | Allocation basis |
|---|---:|---|
| Customer-related | $40 million | Number of active accounts |
| Demand-related | $35 million | Class coincident peak demand |
| Energy-related | $25 million | Annual energy delivered |
| **Total** | **$100 million** | |

The billing and allocation determinants are:

| Determinant | Residential | Commercial | Total |
|---|---:|---:|---:|
| Active accounts | 100,000 | 20,000 | 120,000 |
| Coincident peak demand | 200 MW | 100 MW | 300 MW |
| Annual energy delivered | 1.2 TWh | 0.8 TWh | 2.0 TWh |

Assume that each pool is allocated strictly in proportion to its stated determinant. Ignore taxes, riders, losses, uncollectibles, minimum bills, and intra-class differentiation unless a question asks you to discuss them.

## Problem 1 — Allocate class revenue responsibility

1. Calculate each class's allocation percentage for each of the three cost pools.
2. Allocate the customer-, demand-, and energy-related cost pools to each class.
3. Calculate each class's total allocated revenue responsibility and verify that the two class totals sum to $100 million.
4. Calculate each class's share of total revenue responsibility. Explain why this share need not equal its share of accounts, peak demand, or energy use.

## Problem 2 — Construct a simplified three-part tariff

Assume that the customer pool is recovered through a monthly fixed charge, the demand pool through a monthly billing-demand charge, and the energy pool through a volumetric charge. For this exercise, assume 12 months per year and no seasonal differentiation.

1. Calculate the uniform monthly customer charge implied by the customer pool.
2. Calculate the demand charge in dollars per kW-month implied by the demand pool. Use class coincident peak demand as the annual billing determinant only for this stylized calculation.
3. Calculate the volumetric charge in dollars per kWh implied by the energy pool.
4. Verify that applying the three charges to the aggregate determinants recovers the $100 million requirement.
5. Explain why the demand charge derived from coincident class peak is not automatically an appropriate tariff billing determinant for an individual customer.

## Problem 3 — Representative bill and tariff incidence

Consider a residential account with 10,000 kWh annual consumption and a 5 kW monthly billing demand in every month. Consider a commercial account with 100,000 kWh annual consumption and a 25 kW monthly billing demand in every month.

1. Calculate each account's annual bill under the stylized three-part tariff.
2. Calculate each account's average monthly bill.
3. Compare the fixed, demand, and energy components as shares of each bill.
4. Explain why these representative bills cannot establish class-wide affordability, cost causation, or distributional equity. Identify at least four additional data elements needed for a defensible incidence analysis.

## Problem 4 — Alternative rate designs

A regulator is considering three alternatives for recovering the same $100 million:

- **A: Volumetric-only:** recover the entire amount through a uniform $/kWh charge.
- **B: Fixed-plus-volumetric:** recover 40% through an equal monthly account charge and 60% through a uniform $/kWh charge.
- **C: Three-part:** use the cost-pool allocation in this problem set.

For each design:

1. Calculate the fixed and volumetric rates where applicable.
2. Explain which customers are likely to experience larger bill changes under each design, holding total class revenue constant only as a simplifying assumption.
3. Discuss conservation incentives, revenue stability, customer heterogeneity, and potential affordability effects.
4. Explain why recovering a greater share through fixed charges can weaken the marginal price signal for energy efficiency while increasing bills for low-use customers.

Do not claim that any one design is universally optimal. A defensible recommendation must identify the regulator's statutory objectives, cost study, customer data, and transition constraints.

## Problem 5 — Cost causation and allocation judgment

The utility proposes to allocate all distribution costs by annual kWh because those data are readily available.

1. Identify the analytical problem with using a single allocator for costs with different cost drivers.
2. Give examples of distribution assets or activities that may be more closely associated with customer count, non-coincident demand, coincident peak, energy throughput, location, or reliability requirements.
3. Explain why a functionalization/classification/allocation study requires engineering judgment and cannot be replaced by an arbitrary spreadsheet formula.
4. Discuss at least two plausible alternative allocation methods for demand-related costs and the information needed to evaluate them.

## Problem 6 — Evidence, uncertainty, and regulatory process

You are asked to review a proposed tariff change in a public commission docket.

1. Build an evidence hierarchy distinguishing the utility's cost-of-service study, testimony, intervenor analysis, settlement, commission order, tariff sheets, and customer bill-impact exhibits.
2. Identify which documents establish a proposal, which establish an approved disposition, and which establish the rates actually in effect.
3. Explain how forecast load, customer counts, coincident peak, load factor, and class migration can change the allocation and bill impacts.
4. State how you would document uncertainty and prevent a class-average result from being presented as a prediction for every customer.

## Submission

Submit a workbook or script with the full allocation model, a one-page rate-design comparison, and a 500–800 word regulatory analysis. Include:
- a determinant and unit register;
- allocation formulas visible in the workbook;
- a reconciliation to the $100 million total;
- a sensitivity case that changes at least one allocator;
- a clear distinction between allocated cost responsibility, tariff revenue, and an individual customer's bill.

## Evaluation

The assignment is assessed on mathematical correctness (30%), cost-causation reasoning (20%), tariff and incidence analysis (20%), institutional/evidence interpretation (15%), and reproducibility/limitations (15%).
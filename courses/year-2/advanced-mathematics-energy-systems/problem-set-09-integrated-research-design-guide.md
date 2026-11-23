# Problem Set 9: Instructor and Self-Assessment Guide

This is an open-ended synthesis project. There is no unique numerical optimization answer because the feeder parameters, application-level records, scenario probabilities, and reinforcement costs must be justified by the researcher. The guide defines a defensible minimum standard and records the descriptive checks that can be verified from the public PUC panel.

## Part A. Verified descriptive checks

The source panel has 33 observations: 11 EDCs in each of 2023, 2024, and 2025. Review-level counts reconcile to each EDC's total, and statewide totals reconcile as follows:

| Reporting year | Statewide requests | PPL requests | PPL share | PPL rank | Request-count HHI | Top-three share |
|---|---:|---:|---:|---:|---:|---:|
| 2023 | 19,202 | 7,567 | 39.41% | 1 | 2,487.17 | 76.68% |
| 2024 | 18,582 | 7,519 | 40.46% | 1 | 2,496.32 | 77.13% |
| 2025 | 20,202 | 6,844 | 33.88% | 1 | 2,072.92 | 70.68% |

PPL request counts changed by approximately -0.63% from 2023 to 2024, -8.98% from 2024 to 2025, and -9.55% from 2023 to 2025. These are changes in reported request counts, not changes in processing time, approval probability, installed DER, or utility performance.

The 2025 large-request split reports 135 PPL Level 2 requests at or above 500 kW out of 196 statewide (68.88%) and 411 PPL Level 3 requests at or above 500 kW out of 954 statewide (43.08%). Do not compare these size-band counts to 2023–2024 because the report does not provide the same split for those years.

The HHI is calculated as (10{,}000\sum_i s_i^2), where (s_i) is EDC i's share of statewide request counts. It describes concentration of applications across service territories. It is not an HHI for retail electricity sales, generation ownership, or a product market. Service-territory population, load, customer count, installed DER, and reporting practices are not controlled.

## Part B. Identification

The 2023–2025 panel ends May 31, 2025. It predates the January 2026 Rule 12 applicability/implementation milestones discussed in the casebook. Therefore, the panel contains no post-treatment observations for that change. It also contains no linked application-level receipt and completion dates, project outcomes, or treatment eligibility flags. No treatment effect is identified.

A plausible future estimand is the difference in restricted mean time from complete application to permission-to-operate over a pre-specified horizon among applications eligible under the new process, relative to a defensible counterfactual. Withdrawals and denials should be handled as competing events or explicitly modeled outcomes, not silently treated as independent censoring. Applications still open at the data cutoff are right-censored.

A survival dataset needs a well-defined time origin, event indicator, censoring time, treatment rule, eligibility, application attributes, EDC/feeder context, and a record of process transitions. The proportional-hazards assumption must be assessed if a Cox model is used. Competing-risks estimands are needed when approval, withdrawal, and denial are distinct terminal events. Clustering should reflect shared EDC/feeder processes and repeated projects or applicants where applicable.

Difference-in-differences would require a credible untreated or differently treated comparison group, stable outcome measurement, comparable eligibility, multiple pre-treatment periods to assess pre-trends, clear treatment timing, and no unmodeled concurrent reforms that differentially affect groups. Parallel trends cannot be proven from a non-significant pre-trend test alone.

## Part C. Network formulation

One valid convention is branch orientation (0\to1\to2), with positive branch flow from substation toward the feeder end. Let (A) be the node-edge incidence matrix with -1 at each sending node and +1 at each receiving node. Then nodal balance can be written (Af+p-d=0), with sign convention adjusted consistently for generation and demand. Removing the slack-bus row yields a reduced network balance system.

For a radial feeder, a first-order LinDistFlow approximation may express voltage differences as a linear function of branch active and reactive power:
[
v_i-v_j\approx 2(r_{ij}P_{ij}+x_{ij}Q_{ij})
]
under a consistent squared-voltage or per-unit convention and an explicitly stated flow direction. The approximation neglects or simplifies losses and higher-order voltage terms. It can be inaccurate for high R/X, unbalanced phases, substantial voltage deviations, reverse power flow outside the approximation's calibration range, regulator/capacitor controls, and strong nonlinearities.

Thermal constraints apply to apparent power or an appropriate linearized active/reactive envelope; an active-power-only bound is a simplification and must be labeled. Voltage bounds apply at each modeled node and scenario. DER output can be split into available generation, dispatched generation, and curtailment. Non-export constraints apply at the relevant meter or point of common coupling, not automatically at every upstream branch.

A max-flow model captures abstract capacity and topology but not Kirchhoff's laws or impedance-determined flow distribution. A balanced positive-sequence approximation also does not establish unbalanced three-phase feasibility. Final validation requires an appropriate AC distribution power-flow tool and engineering review.

## Part D. Optimization formulation

A generic two-stage model is:

[
\min_{x\in X}\; C^{\mathrm{cap}}(x)+
\sum_{s\in S}p_s Q(x,s)
]

where (x) is the common first-stage reinforcement decision and (Q(x,s)) is the scenario-specific operating problem. A representative recourse objective is:

[
Q(x,s)=\min_{y_s}\;
C^{\mathrm{energy}}(y_s,s)+
C^{\mathrm{curtail}}(y_s,s)+
C^{\mathrm{slack}}(y_s,s)
]

subject to nodal balances, branch limits adjusted by reinforcement, voltage constraints, DER availability, storage dynamics if included, and scenario-specific equipment states. The slack penalty should be treated as a modeling device unless calibrated to a defensible damage or reliability value.

For branch ℓ, a simple reinforcement capacity constraint might be
[
-F_ℓ^0-x_ℓ\leq f_{ℓ,s}\leq F_ℓ^0+x_ℓ,
quad x_ℓ\geq0.
]
A voltage constraint might be
[
\underline v_i-\epsilon^-_{i,s}\leq v_{i,s}
\leq\overline v_i+\epsilon^+_{i,s},
]
with explicit penalties or hard bounds for the violation variables. This formulation only captures reinforcement effects on thermal capacity. If reinforcement is intended to change impedance and voltage sensitivity, the model must represent that change consistently; simply increasing an MW limit does not reduce voltage rise.

The first-stage vector (x) must be common to all scenarios. Recourse (y_s) may differ after the scenario is observed. A model that selects a different reinforcement plan for each scenario gives the planner perfect information before the investment decision and understates the cost of uncertainty.

A budgeted robust set may constrain normalized deviations (z) by (0\leq z_i\leq1) and (sum_i z_i\leq\Gamma). A stochastic model weights scenarios by probabilities; the robust model protects against all realizations in its set. A robust model can be more conservative, but only relative to its chosen set. A poorly chosen set can be either too conservative or dangerously narrow. Scenario probabilities and uncertainty budgets need empirical or operational justification.

Duals on binding branch and voltage constraints can indicate local marginal values within the formulated optimization model. They are conditional on the model, units, objective coefficients, and active set. They are not automatically wholesale LMPs, tariff rates, avoided costs, or regulator-approved investment values.

## Part E. Verification and model risk

Useful tests include: (1) nodal balance residuals equal zero; (2) zero DER injection reproduces the base case; (3) no branch flow exceeds its enforced limit; (4) all voltage bounds hold when slack is zero; (5) increasing a thermal limit cannot worsen the minimum objective in a correctly nested minimization model; (6) a zero-probability scenario does not affect the stochastic objective; (7) scenario probabilities sum to one; (8) first-stage decisions are identical across scenarios; (9) all flows and voltages use consistent units and sign conventions; (10) the solver result is stable to reasonable scaling and tolerance changes.

A model-risk register should include at least: omitted phase imbalance; uncertain impedance; mismeasured DER availability; load/DER correlation; missing regulator controls; incorrect policy eligibility dates; right-censoring and competing outcomes; and scenario undercoverage. State whether each failure could overstate or understate hosting capacity, upgrade value, or processing effects, and how it will be tested.

## Part F. Institutional interpretation

The physical interconnection pathway is governed by applicable state rules and utility procedures under PUC oversight. Distribution operations and DERMS are utility operational functions subject to applicable tariffs and regulatory requirements. Wholesale aggregation participation is governed by PJM's market rules and FERC's jurisdictional framework, while state interconnection processes remain distinct. Customer adoption depends on project economics, financing, incentives, and site conditions.

A complete paper must cite the controlling tariff and order versions and distinguish the current rule from historical versions. Proposed regulations are not final rules. An informational PJM presentation is not a tariff. A utility's projected hosting-capacity benefit is not an independently measured outcome.

## Part G. Acceptance standard

A defensible project reports the verified public baseline, identifies what cannot be inferred, formulates a physically coherent planning model, tests numerical behavior, and proposes a feasible data collection and identification strategy. It does not manufacture an empirical treatment effect or present a synthetic model as an operational study.

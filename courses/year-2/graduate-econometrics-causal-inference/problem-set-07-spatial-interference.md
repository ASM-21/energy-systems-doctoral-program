# Problem Set 7: Spatial Exposure, Network Spillovers, and Interference

**Level:** Advanced graduate / doctoral preparation  
**Suggested time:** 5–7 hours  
**Prerequisites:** Potential outcomes, randomized experiments, panel data, linear algebra, graph theory, and basic spatial statistics.

## Learning objectives

Derive why conventional no-interference assumptions fail in electricity networks; define treatment and exposure mappings; distinguish direct, indirect, total, and spillover effects; identify what randomized saturation designs can estimate; diagnose network exposure measurement error; and explain why spatial correlation is not itself a causal spillover.

## Problem 1. Potential outcomes with interference

There are (N) projects on a distribution network. Let (Z_i\in\{0,1\}) indicate whether project (i) receives an incentive. Under no interference, potential outcomes are (Y_i(1)) and (Y_i(0)).

1. Explain why this notation may be inadequate when projects share a constrained feeder.
2. Define a general potential outcome (Y_i(\mathbf Z)), where \(\mathbf Z\) is the complete assignment vector.
3. Define an exposure mapping (G_i(\mathbf Z, W)), where (W) is a prespecified network matrix. Give one physically meaningful mapping for neighboring treated capacity.
4. State the assumption required for exposure sufficiency: assignments that produce the same own treatment and mapped exposure yield the same potential outcome.
5. Explain why an exposure mapping is a modeling restriction, not a fact established by estimating a regression.

## Problem 2. Direct, spillover, and total effects

Suppose exposure is binary, (E_i\in\{0,1\}), and potential outcomes are (Y_i(z,e)).

1. Define the direct effect at exposure (e).
2. Define the spillover effect among untreated units.
3. Define the total effect comparing treated/high-exposure and untreated/low-exposure states.
4. Using the table below, calculate all three effects.

| State | Mean potential outcome (days to interconnection) |
|---|---:|
| (Y(0,0)) | 90 |
| (Y(1,0)) | 78 |
| (Y(0,1)) | 105 |
| (Y(1,1)) | 88 |

5. Explain why the direct effect may differ by exposure and why the total effect is not generally the sum of a single direct and spillover effect.

## Problem 3. Two-stage randomized saturation design

A study has 20 independent service areas, each with 100 eligible customers. Service areas are randomized to low saturation (10% offer probability) or high saturation (60% offer probability). Within each area, offers are randomized at the assigned probability.

1. Identify the first-stage and second-stage randomization units.
2. Define the area-level saturation assignment and customer-level offer assignment.
3. State an estimand for the effect of high versus low saturation on untreated customers.
4. Explain how to estimate the direct offer effect at a fixed saturation level.
5. Why must standard errors reflect service-area assignment? Why are 20 clusters a serious inferential limitation?
6. Explain how noncompliance changes the interpretation of offer effects versus participation effects.

## Problem 4. Network exposure and capacity

A feeder has four projects with capacities (c=(100,80,60,40)) kW. The symmetric adjacency matrix is

[
W=\begin{bmatrix}
0&1&0&0\\
1&0&1&0\\
0&1&0&1\\
0&0&1&0
\end{bmatrix}.
]

Projects 1 and 3 are treated.

1. Compute the treated-neighbor count (e_i=\sum_j W_{ij}Z_j).
2. Compute treated neighboring capacity (q_i=\sum_j W_{ij}c_jZ_j).
3. Explain why row-standardizing (W) changes the estimand from total neighboring exposure toward average neighboring exposure.
4. Give two reasons this adjacency matrix may be physically inadequate for distribution-system spillovers.
5. Propose a directed or weighted exposure mapping using electrical distance, shared upstream impedance, or power-transfer sensitivity.

## Problem 5. Reflection and endogenous network formation

A researcher regresses project outcomes on the average outcome of neighboring projects and calls the coefficient a peer effect.

1. Explain the reflection problem.
2. Distinguish endogenous effects, contextual effects, and correlated effects.
3. Explain why feeder membership is not randomly assigned and why conditioning on observed network characteristics may not remove selection.
4. Propose one design that could identify a spillover effect, stating the exclusion or randomization assumptions.
5. Explain why a spatial lag model does not automatically solve the identification problem.

## Problem 6. Interference in difference-in-differences

A policy changes interconnection review rules in one utility territory. Adjacent territories share contractors, equipment suppliers, and some electrically connected facilities.

1. Explain how spillovers into nominal control territories can violate the standard DID comparison.
2. Define a treatment-exposure variable for controls based on proximity or shared contractors.
3. Describe how direct and spillover effects could be separated with multiple exposure groups.
4. Explain why adding a post-treatment exposure control may create bias.
5. State a design and data requirement that would improve credibility.

## Problem 7. Spatial dependence is not necessarily spillover

Let the outcome satisfy (Y=X\beta+u), where (u\) has spatial covariance \(\Sigma(W)\).

1. Distinguish spatially correlated errors from causal interference in the conditional mean.
2. Explain what happens to conventional standard errors if spatial dependence is ignored.
3. Explain why Conley-type spatial HAC or cluster-robust inference can address uncertainty but not omitted spatially lagged treatment effects.
4. Describe a diagnostic strategy using residual maps, network-distance correlograms, and alternative exposure definitions.
5. State the limitations of Moran's I as a causal diagnostic.

## Problem 8. Research design memo

Write a 1,000–1,500 word preregistration-style memo for evaluating a hypothetical flexible-interconnection program. It must specify:

- Target population, unit of assignment, unit of analysis, and treatment.
- Potential outcomes and exposure mapping.
- Primary direct and spillover estimands.
- Interference assumptions, including partial-interference boundaries.
- Identification design and inference unit.
- Primary outcome, timing, censoring, and measurement.
- Network data needed to construct exposure.
- Anticipation, displacement, reallocation, and concurrent-policy threats.
- Sensitivity analyses and a rule for downgrading causal claims if exposure is poorly measured.

**Data discipline:** This assignment is a design exercise. Do not use confidential utility, customer, or feeder data. A public aggregate dataset cannot identify project-level network spillovers unless its unit and exposure structure support that estimand.

## Submission standard

Show derivations, state the estimand before the estimator, and label every assumption that cannot be tested directly. A technically sophisticated spatial regression with an unidentified exposure mechanism does not earn causal-design credit.

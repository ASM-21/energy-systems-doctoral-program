# Problem Set 5: Worked Solutions and Identification Notes

## Problem 1. Estimator

The simplex constraints make the synthetic predictor a convex combination of donor predictors. It therefore lies inside the donors' convex hull and cannot extrapolate outside it. With fitted weights \(w\), the untreated counterfactual is \(\widehat Y_{1t}^{N}=\sum_jw_jY_{jt}\), and the estimated gap is the observed treated outcome less this counterfactual.

The predictor set and \(V\) matrix determine which dimensions receive emphasis. A low pre-treatment loss only shows that the selected observed predictors can be matched; it does not establish that unobserved determinants, outcome dynamics, or post-period shocks are comparable. Causal interpretation requires a stable untreated relationship, no relevant spillovers, a valid intervention date, and no unmodeled concurrent shock unique to the treated unit.

## Problem 2. Numerical geometry

The target is in the convex hull. One exact solution is \(w=(0.5,0.5,0)\), because \(0.5(10,20)+0.5(8,18)=(9,19)\), which does not equal the target. A correct exact solution is \(w=(0.375,0.25,0.375)\):
- first coordinate: \(10(0.375)+8(0.25)+12(0.375)=10.25\), not 9.5.
This demonstrates why numerical verification is required rather than guessing weights.

Solve the two equations plus the adding-up constraint. Let \(w_1+w_2+w_3=1\), \(10w_1+8w_2+12w_3=9.5\), and \(20w_1+18w_2+24w_3=20.5\). Subtracting twice the second-coordinate equation from the third gives \(-?\); the constraints are not independent in the way a casual inspection might suggest. In fact, the second coordinate is exactly twice the first for every donor, whereas the target's second coordinate 20.5 is not twice 9.5. Therefore no exact convex combination exists. The target lies outside the affine line containing the donors. This is a deliberate convex-hull diagnostic: an exact fit is impossible.

A model can match two predictors and miss a third. Always report the full predictor-balance table and standardized gaps, not a selected two-dimensional visualization.

## Problem 3. Fit and placebo interpretation

The treated post/pre RMSPE ratio is \(4.0/0.8=5\). The placebo ratio is \(1.0/0.2=5\). The same ratio does not imply identical causal evidence: the absolute fit quality and the placebo's pre-treatment comparability matter. Poorly fitted placebo units can generate large ratios mechanically and should be handled using a pre-specified fit threshold.

In-space placebo inference repeatedly assigns the intervention label to donor units, reconstructs a synthetic control, and compares post/pre fit statistics. Its rank-based reference distribution is only persuasive when treated and placebo units are plausibly exchangeable under the null. Utilities are not randomly assigned policies, so this is not automatically a design-based randomization test. Sampling-based confidence intervals require an explicit stochastic model or resampling scheme and are conceptually different.

## Problem 4. Donor design

Donors should be assessed on regulatory regime, RTO membership, tariff design, customer/project mix, climate, load growth, DER penetration, data definitions, and concurrent investments. Neighboring utilities may share weather, market, or policy shocks; that can help absorb common shocks but can also create interference. Define eligibility using pre-treatment institutional and data criteria, then freeze it before estimating effects. Report all eligible donors, exclusions with reasons, alternative pre-specified pools, and leave-one-out results. Do not remove a donor because it weakens the preferred estimate.

## Problem 5. Extensions

Generalized synthetic control and interactive fixed-effects methods estimate latent common factors and unit-specific factor loadings, supporting multiple treated units and richer panels. They trade the transparent convex-combination interpretation for additional model structure. Augmentation can reduce bias when the untreated outcome is not well represented by a convex combination, but extrapolation relies more heavily on the outcome model.

Traditional two-way fixed-effects regressions can be misleading under heterogeneous treatment effects and staggered timing. Group-time DID estimators make treatment timing and cohort-specific effects more explicit. Synthetic control is not automatically superior: with many treated/control units and credible parallel trends, DID may be simpler; with poor pre-fit, a short pre-period, unstable donors, or strong spillovers, SCM may not be credible.

## Problem 6. Design memo rubric

A defensible proposal must define the estimand and intervention timing; document a donor eligibility rule; report data frequency and consistent outcome definitions; pre-specify predictors, fit criteria, and optimization; show pre- and post-period gaps; use placebo and leave-one-out diagnostics; and discuss concurrent interventions, spillovers, donor instability, and inference. The design must be labeled not yet identified if the donor pool cannot reproduce the treated unit's pre-treatment outcome path.

# Problem Set 7: Worked Solutions and Instructor Notes

## Problem 1. Potential outcomes with interference

1. Projects on the same constrained feeder can affect voltage, thermal headroom, curtailment, upgrade timing, and review outcomes for other projects. The outcome for project (i) can depend on other projects' assignments.
2. Write (Y_i(\mathbf Z)), with one potential outcome for each feasible assignment vector.
3. One mapping is (G_i(\mathbf Z,W)=\sum_{j\ne i}W_{ij}c_jZ_j), treated neighboring nameplate capacity in kW. A more physical mapping could weight by electrical sensitivity rather than binary adjacency.
4. Exposure sufficiency requires (Y_i(\mathbf Z)=Y_i(\mathbf Z')) whenever (Z_i=Z'_i) and (G_i(\mathbf Z,W)=G_i(\mathbf Z',W)).
5. This restricts the enormous assignment space to a lower-dimensional exposure representation. The restriction must be defended from engineering and institutional knowledge; data fit cannot establish that omitted pathways do not matter.

## Problem 2. Direct, spillover, and total effects

Using outcome in days, a negative effect means fewer days.

- Direct effect at (e=0): (Y(1,0)-Y(0,0)=78-90=-12) days.
- Direct effect at (e=1): (Y(1,1)-Y(0,1)=88-105=-17) days.
- Spillover effect among untreated units: (Y(0,1)-Y(0,0)=105-90=15) days.
- Spillover effect among treated units: (Y(1,1)-Y(1,0)=88-78=10) days.
- Total effect from ((0,0)) to ((1,1)): (88-90=-2) days.

The direct effect is heterogeneous by exposure: -12 versus -17. The total contrast combines own treatment and exposure changes; it is not equal to one direct effect plus one universally applicable spillover effect. Here, using the low-exposure direct effect and untreated spillover gives ( -12+15=3), not -2, because the direct effect changes with exposure and the relevant decomposition path matters.

## Problem 3. Two-stage randomized saturation design

1. First-stage unit: service area. Second-stage unit: customer within area.
2. Let (S_g\in\{0.10,0.60\}) denote assigned saturation and (Z_{ig}) the individual randomized offer.
3. An untreated-spillover estimand is
   [
   \tau_{spill}=E[Y_{ig}(0;S_g=0.60)-Y_{ig}(0;S_g=0.10)].
   ]
   Assignment-based estimation compares non-offered customers across randomized saturation arms, accounting for the known assignment probabilities.
4. At a fixed saturation (s), estimate (E[Y\mid Z=1,S=s]-E[Y\mid Z=0,S=s]), with design-based weighting if assignment probabilities or response rates vary.
5. Saturation is randomized across only 20 service areas, so the independent first-stage information is 20 clusters, not 2,000 customers. Conventional large-cluster asymptotics are unreliable; use randomization inference at the area level, small-sample corrections, and transparent uncertainty. Precision may remain poor.
6. ITT estimates the effect of being offered. Participation effects require additional assumptions, such as exclusion and monotonicity for an instrumental-variable complier effect. Offer assignment does not automatically identify the effect of actual adoption.

## Problem 4. Network exposure and capacity

For (Z=(1,0,1,0)'):

- Treated-neighbor counts: (e=(0,2,0,1)').
- Treated neighboring capacity: (q=(0,160,0,60)') kW.

Row-standardizing divides each nonzero row by its degree. It changes the scale from a sum of neighboring treatment or capacity to an average across neighbors. This changes the substantive exposure contrast, not merely numerical presentation.

Binary adjacency ignores impedance, phase configuration, voltage level, topology changes, protection settings, and nonlinear operating state. A sensitivity-based mapping could use (q_i=\sum_j |\partial V_i/\partial P_j|c_jZ_j), or a PTDF-like transfer sensitivity when a suitable linearized network model is justified. The sign and operating point matter; absolute sensitivities discard direction and should be justified.

## Problem 5. Reflection and endogenous network formation

1. Neighbor outcomes and own outcomes may be jointly determined. It is difficult to distinguish whether neighbors affect the unit, the unit affects neighbors, or common shocks affect both.
2. Endogenous effects are effects of peers' outcomes; contextual effects arise from peers' predetermined characteristics; correlated effects arise from common environments or sorting.
3. Projects select locations based on land, load, customer type, available capacity, and expected upgrade cost. Network topology itself can be endogenous to prior investment. Observed controls may not capture unobserved constraints or historical decisions.
4. A randomized saturation design can identify assignment-based spillovers if saturation is randomized across independent groups, exposure is correctly mapped, and cross-group interference is negligible. An instrument for peer treatment requires a defensible exclusion restriction and no direct effect of the instrument on the focal outcome.
5. A spatial lag (WY) is endogenous because neighboring outcomes contain simultaneous shocks and feedback. Identification requires instruments or structural restrictions beyond estimating the spatial autoregressive coefficient.

## Problem 6. Interference in difference-in-differences

1. If nominal controls receive contractor learning, equipment reallocation, or electrical congestion displacement caused by treatment, their post-period outcomes are affected. The control group no longer represents the untreated counterfactual.
2. Define (E_{it}=\sum_j W_{ij}D_{jt}), where (W) encodes shared contractors, geographic proximity, or electrical connectivity. These are distinct mechanisms and should not be collapsed without justification.
3. Compare untreated low-exposure, untreated high-exposure, treated low-exposure, and treated high-exposure units, if there is sufficient overlap and credible assignment variation. Estimate direct and spillover contrasts separately.
4. Post-treatment exposure may be affected by treatment, project relocation, or endogenous network reconfiguration. Conditioning on it can block part of the treatment effect or induce collider bias.
5. Use pre-policy network and contractor links, multiple pre-periods, explicit exposure mapping, stable comparison groups, and cluster-level inference. If network exposure cannot be measured, report descriptive estimates and sensitivity bounds rather than causal effects.

## Problem 7. Spatial dependence is not necessarily spillover

1. Spatially correlated errors mean unobserved shocks co-move across nearby units; interference means one unit's treatment changes another unit's potential outcome. The former concerns covariance; the latter changes the conditional mean.
2. Ignoring dependence can understate standard errors and overstate precision. The direction and magnitude depend on covariance structure and design.
3. Spatial HAC or clustering adjusts the covariance estimate under assumptions about dependence range or cluster structure. It does not add omitted exposure terms, identify spillover coefficients, or repair endogenous treatment.
4. Map residuals; calculate correlograms by geographic and electrical distance; compare binary adjacency, impedance-weighted, and feeder-level exposure definitions; inspect sensitivity to boundary choices and influential units. Pre-specify plausible distances.
5. Moran's I tests a pattern of spatial autocorrelation under a chosen weights matrix. It does not distinguish common shocks, sorting, omitted variables, or causal spillovers and is sensitive to the weights matrix.

## Problem 8. Research design memo

A strong memo will:

- Define the intervention as an offer or eligibility rule, not simply observed enrollment.
- Separate customer, project, feeder, and service-territory units.
- State a potential-outcomes framework with own assignment and a physically defensible exposure mapping.
- Identify direct and spillover estimands before choosing an estimator.
- Define partial-interference groups only where cross-group pathways are plausibly negligible.
- Prefer randomized saturation or a defensible policy assignment mechanism; otherwise describe the assumptions required for quasi-experimental identification.
- Use pre-treatment network topology where possible and document topology changes.
- Treat application completion, withdrawal, approval, construction, and PTO as distinct events with competing risks and censoring.
- Address project relocation, queue displacement, upgrade allocation, contractor spillovers, and anticipation.
- Cluster inference at the assignment unit and acknowledge few-cluster limits.
- Downgrade to descriptive or associational language when exposure is not observed or the assumed mapping is not defensible.

**Grading emphasis:** estimand clarity (20%), exposure and interference assumptions (20%), identification (20%), measurement and event definitions (15%), inference (10%), threats and sensitivity (10%), reproducibility and communication (5%). No estimator can compensate for an unidentified treatment or exposure process.

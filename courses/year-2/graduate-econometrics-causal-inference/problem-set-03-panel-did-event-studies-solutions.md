# Problem Set 3: Worked Solutions and Identification Notes

## Problem 1. Two-group, two-period DID

The treated group's change is \(14-10=4\). The comparison group's change is \(10-8=2\). Therefore:
\[
\widehat{DID}=(14-10)-(10-8)=4-2=2.
\]

The regression is
\[
Y_{it}=\alpha+\beta Treat_i+\gamma Post_t+
\delta(Treat_i\times Post_t)+\epsilon_{it}.
\]
The coefficient \(\delta\) equals the 2×2 DID contrast. In a panel with unit and time fixed effects, the time-invariant group indicator is absorbed by unit fixed effects.

In potential-outcomes notation, a parallel-trends condition for the treated group is
\[
E[Y_{1}(0)-Y_{0}(0)\mid Treat=1]
=
E[Y_{1}(0)-Y_{0}(0)\mid Treat=0],
\]
where subscripts denote time and \(Y_t(0)\) is the untreated potential outcome. The assumption concerns the counterfactual trend, which is not directly observed after treatment. A significant DID coefficient tests an outcome contrast, not the validity of the counterfactual trend assumption.

## Problem 2. Parallel-trends violation

The treated group's counterfactual post outcome is 13 because its untreated trend would have been +3. The observed post outcome is 14, so the true effect is \(14-13=1\).

The DID estimate remains 2. The bias is \(2-1=1\), equal to the difference between the treated and comparison groups' untreated trends (3 versus 2). Group and time fixed effects remove time-invariant group differences and common period shocks; they do not remove group-specific counterfactual trend differences.

Credibility can improve with multiple pre-treatment periods, institutional justification for the comparison group, covariate balance, stable measurement, placebo dates, negative-control outcomes, and sensitivity analysis. None proves parallel trends. Pre-trend tests may have low power and should not be interpreted as proof of equivalence.

## Problem 3. Event studies and staggered adoption

A conventional event-study equation is
\[
Y_{it}=\alpha_i+\lambda_t+
\sum_{k\neq-1}\beta_k 1[t-G_i=k]+\epsilon_{it}.
\]
The omitted event time -1 is the reference period. Coefficients compare outcomes at relative time k with the omitted pre-treatment period, conditional on the model's fixed effects.

Pre-treatment coefficients can reveal patterns inconsistent with parallel trends, but insignificant estimates do not prove the assumption. Under staggered adoption and heterogeneous effects, conventional TWFE event-study coefficients may combine comparisons between newly treated and already-treated units. Leads and lags can be contaminated by effects from other relative periods; coefficients need not represent clean dynamic treatment effects.

Group-time ATT methods estimate effects for a treatment cohort g at time t using never-treated or not-yet-treated comparison units, subject to the design's assumptions. Interaction-weighted event studies aggregate cohort-specific relative-time effects rather than relying on potentially contaminated TWFE weights. Already-treated units may have outcomes affected by treatment and are therefore not untreated counterfactuals for later adopters.

## Problem 4. Clustered inference

The treatment is assigned at the EDC level, so outcomes for applications within an EDC may share policy exposure and correlated shocks. Clustering at the application level treats correlated observations as independent and can understate uncertainty. The natural cluster is EDC, subject to the actual assignment and error-correlation structure.

Ten clusters are few for conventional cluster-robust asymptotics. Wild cluster bootstrap and randomization inference may improve finite-sample inference when their assumptions are appropriate, but neither creates independent assignment units. More applications within the same ten EDCs increase within-cluster information but do not materially increase the number of independent policy assignments. A design with more independent EDCs or a different assignment unit may be necessary.

## Problem 5. Staggered adoption

Conventional TWFE can use not-yet-treated units and already-treated units as comparisons, depending on adoption timing and the fixed-effects residualization. If treatment effects differ by cohort or evolve over event time, comparisons with already-treated units can subtract one treatment effect from another. The resulting weights may be negative or non-convex, so the coefficient need not be a meaningful weighted average of cohort-specific effects.

A group-time ATT design estimates \(ATT(g,t)\) for cohort g at time t, comparing it with never-treated or not-yet-treated units that remain untreated at t. Dynamic effects can then be aggregated by event time using explicit weights. Credibility still requires a conditional parallel-trends assumption, overlap, stable outcome measurement, valid treatment timing, and no unaddressed anticipation or interference.

## Problem 6. Pennsylvania application

The PUC panel ends May 31, 2025, so it contains no post-January-2026 observations. It also contains aggregate request counts rather than linked application-level outcomes. It cannot estimate a post-policy effect.

A future design needs several pre-policy periods and enough post-policy follow-up for application cohorts to reach the chosen outcome. Application-level dates, review transitions, project attributes, tariff eligibility, withdrawal/denial/approval, agreement, and PTO are required for process outcomes. Another EDC is not automatically untreated: it may adopt a similar program, face different market conditions, have different review rules, or experience spillovers.

An application-level estimand could be a difference in restricted mean time to first utility decision over a fixed horizon among legally eligible projects. An EDC-level estimand could be a change in a properly normalized outcome rate, but requires credible denominators and sufficient independent EDCs. Overlapping interventions, project mix, changing definitions, and feeder spillovers must be recorded and modeled or treated as identification limitations.

## Problem 7. Research memo: minimum standard

A strong memo begins with the policy assignment mechanism and estimand, not a preferred regression. It identifies the comparison units and shows why their untreated outcomes could plausibly follow the treated units' counterfactual trend. It documents treatment dates, pre-periods, anticipation, concurrent changes, outcome measurement, and cluster structure. With staggered adoption and heterogeneous effects, it uses group-time or interaction-weighted estimators and avoids interpreting conventional TWFE coefficients as automatically causal. If there are too few assignment clusters or no credible comparison group, the correct conclusion may be that the causal design is infeasible with current data.

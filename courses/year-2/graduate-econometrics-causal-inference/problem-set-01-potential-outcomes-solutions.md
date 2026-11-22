# Problem Set 1: Worked Solutions and Identification Notes

## Problem 1. Potential outcomes and estimands

The individual effect is \(\tau_i=Y_i(1)-Y_i(0)\). The ATE is \(E[Y(1)-Y(0)]\). The ATT is \(E[Y(1)-Y(0)\mid D=1]\). The ATU is \(E[Y(1)-Y(0)\mid D=0]\).

Only one potential outcome is observed for each unit: \(Y_i=D_iY_i(1)+(1-D_i)Y_i(0)\). The unobserved potential outcome is the fundamental problem of causal inference.

The observed difference is
\[
E[Y\mid D=1]-E[Y\mid D=0]
=E[Y(1)\mid D=1]-E[Y(0)\mid D=0].
\]
Add and subtract \(E[Y(0)\mid D=1]\):
\[
=ATT+
\underbrace{E[Y(0)\mid D=1]-E[Y(0)\mid D=0]}_{\text{selection bias}}.
\]
It equals the ATT only when the selection-bias term is zero. It equals the ATE only under additional conditions such as random assignment and suitable treatment-effect aggregation.

ATT is useful when asking about the effect on applicants actually covered by a policy. ATE is useful when evaluating expansion to the entire eligible population, provided the target population and effect transport are defensible.

## Problem 2. Selection-bias decomposition

For treated applicants:
\[
ATT=0.72-0.60=0.12.
\]
For untreated applicants:
\[
ATU=0.66-0.56=0.10.
\]
With half treated:
\[
ATE=0.5(0.12)+0.5(0.10)=0.11.
\]
The observed difference is:
\[
0.72-0.56=0.16.
\]
Selection bias, using the untreated potential outcome means, is:
\[
0.60-0.56=0.04.
\]
Thus \(0.16=0.12+0.04\). The observed difference overstates ATT by four percentage points in this example.

Random assignment makes treatment independent of both potential outcomes in expectation, so the treatment/control mean difference identifies the ATE. It does not imply \(Y_i(1)-Y_i(0)\) is identical across applicants; treatment-effect heterogeneity can remain.

## Problem 3. Conditional independence

A sufficient conditional independence assumption is
\[
(Y(1),Y(0))\perp D\mid X.
\]
Overlap requires
\[
0<P(D=1\mid X=x)<1
\]
for covariate values in the target population.

The g-formula for the ATE is
\[
ATE=E_X\left[E(Y\mid D=1,X)-E(Y\mid D=0,X)\right].
\]
Identification depends on measuring the relevant pre-treatment confounders, consistent treatment/outcome definitions, and overlap. A regression with many controls does not establish these conditions. Variables measured after treatment may be mediators, colliders, or consequences of selection. Controlling for them can block part of the effect or open a noncausal path.

## Problem 4. DAG and selection

Plausible arrows include S→R, S→Y, F→R, F→Y, A→C, A→Y, C→Y, U→R, and U→Y. R may affect C and then Y if the policy changes completeness requirements or support. The exact graph must follow the institutional process and timing.

S, F, A, and U can create backdoor paths from policy exposure to outcome. Completeness C may mediate part of an assistance or process effect. Withdrawal W may be a collider if both applicant resources and expected study burden affect withdrawal; conditioning on W or only analyzing completed applications can induce selection. An EDC fixed effect removes time-invariant EDC differences, not time-varying workload, project mix, feeder constraints, or policy co-interventions.

## Problem 5. Randomized encouragement

Randomly assign an offer of optional application assistance among eligible applicants, while preserving ordinary access and engineering review standards. ITT is the difference in outcomes by randomized offer assignment, regardless of take-up.

The treatment-on-the-treated effect is the effect of actually receiving assistance among compliers under an instrumental-variable interpretation. Randomized offer can instrument receipt if relevance, exclusion, independence, and monotonicity are defensible. Exclusion may fail if merely receiving an offer changes applicant behavior even without using the assistance.

Withdrawals are outcomes or competing events, not automatically missing data. Open cases at the fixed follow-up date are administratively right-censored for time-to-event analysis. The protocol must pre-specify these treatments.

## Problem 6. Interference

SUTVA's no-interference condition is violated because one project's export or approval may alter another project's feasible export or study outcome. An exposure mapping might define each application’s exposure using cumulative queued DER capacity, approved capacity, and export profile on the same feeder at a specified date.

Application-level randomization may contaminate control units through shared feeder conditions. Cluster randomization at feeder level or a partial-interference design can define treatment effects at the feeder level, such as the effect of an assistance or operating-envelope program on total feeder-level hosting capacity or aggregate application outcomes. The estimand must specify whether direct, spillover, or total effects are targeted.

## Problem 7. Research memo: defensible answer

The 2023–2025 aggregate panel does not identify a causal effect of PPL's 2026 Rule 12 or DER Management changes. The reporting window ends May 31, 2025, before the relevant 2026 policy applicability and implementation milestones. The unit is EDC-year, not application, and the panel contains request counts rather than linked process outcomes. There are no post-treatment observations under the new process, no individual treatment eligibility, no receipt/completion dates, and no application-level status transitions.

The panel can describe statewide request volume, EDC shares, review-level counts, PPL's relative request volume, and selected reporting-period changes. It cannot establish processing time, approval probability, installation completion, hosting capacity, or policy effects.

A credible follow-on study would require de-identified application-level event histories, eligibility under the controlling tariff version, technology/size/export attributes, dates for each process milestone, feeder context, study/upgrade requirements, and withdrawal/denial/approval/PTO outcomes. The target estimand might be a difference in restricted mean time to first disposition or cumulative incidence of approval by a fixed horizon among legally eligible applications. Survival or competing-risks methods could describe event timing; a causal effect would still require a defensible comparison group or other identification strategy, stable measurement, and treatment of concurrent policy and investment changes.

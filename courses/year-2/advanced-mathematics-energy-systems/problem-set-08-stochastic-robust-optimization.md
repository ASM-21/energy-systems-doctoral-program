# Problem Set 8: Stochastic and Robust Optimization for Energy Systems

**Level:** Advanced graduate / doctoral preparation  
**Suggested effort:** 2–3 hours  
**Prerequisites:** Problem Sets 3, 5, and 6; linear programming, probability, duality, and numerical optimization  
**Deliverable:** Mathematical formulations, hand calculations, and a short modeling comparison

## Learning objectives

1. Formulate a two-stage stochastic linear program with first-stage decisions and scenario-dependent recourse.
2. Distinguish the stochastic optimum, expected-value solution, wait-and-see solution, value of the stochastic solution, and expected value of perfect information.
3. Construct a robust counterpart for a budgeted uncertainty set.
4. Formulate a chance constraint and explain its statistical and operational interpretation.
5. Use conditional value at risk (CVaR) to represent tail-risk preferences.
6. Explain nonanticipativity, scenario design, and the limits of uncertainty models.

## Problem 1. Two-stage capacity planning under uncertain demand

A planner must procure firm capacity (K) before a one-hour demand realization is known. Demand has two possible scenarios:

| Scenario | Demand (MW) | Probability |
|---|---:|---:|
| Low | 80 | 0.4 |
| High | 120 | 0.6 |

Capacity costs $70 per MW for the planning period. Dispatching one MW costs $5, and unserved demand incurs a penalty of $100 per MWh. Let (g_s) be generation and (u_s) unserved demand in scenario s. Capacity is bounded by (0\leq K\leq120).

1. Write the two-stage stochastic linear program. Clearly identify first-stage and recourse variables.
2. Solve for the optimal (K), (g_s), and (u_s). Show a piecewise objective or a marginal argument.
3. Calculate the optimal expected total cost.
4. Replace the uncertain demand with its expected value and solve the resulting deterministic problem. Evaluate that first-stage decision under the original two scenarios. This is the expected-value solution (EEV).
5. Calculate the wait-and-see expected cost, where capacity can be chosen after the scenario is known. Then calculate:
   - the value of the stochastic solution (VSS);
   - the expected value of perfect information (EVPI).
6. Explain why the deterministic expected-demand solution is not equivalent to the two-stage stochastic solution.

## Problem 2. Budgeted uncertainty and robust capacity constraints

Suppose a planner serves three load zones. Their nominal peak demands are \(\bar d=(40,30,20)\) MW, with maximum upward deviations \(\hat d=(8,6,4)\) MW. Let

\[
d_i=\bar d_i+\hat d_i z_i,\qquad
0\leq z_i\leq1,\qquad
\sum_i z_i\leq\Gamma.
\]

Here \(\Gamma\) controls how many zones can simultaneously approach their maximum deviation.

1. Derive the worst-case aggregate demand as a function of \(\Gamma\).
2. Calculate it for \(\Gamma=1\), \(1.5\), and \(3\).
3. If firm capacity must cover worst-case aggregate demand, state the robust capacity requirement for each case.
4. Explain how \(\Gamma\) changes the conservatism of the model and why it should be justified using evidence or a defensible uncertainty interpretation.
5. Compare this uncertainty set with a box uncertainty set that allows all three zones to reach their maximum deviations simultaneously.

## Problem 3. Chance constraints and tail probability

A one-hour net-load forecast error is modeled as normally distributed:

\[
D\sim\mathcal N(100,15^2)\text{ MW}.
\]

A planner wants firm capacity K to cover net load with at least 95% probability.

1. Write the chance constraint \(\Pr(D\leq K)\geq0.95\).
2. Convert it to a deterministic constraint using the standard normal quantile.
3. Calculate the minimum K.
4. Repeat for 99% coverage using \(z_{0.99}=2.3263\).
5. Explain why a one-hour 95% chance constraint does not imply that the system will satisfy a 95% reliability standard over a year.
6. Identify at least four assumptions or data issues that could invalidate the normal approximation or the resulting capacity number.

## Problem 4. CVaR and risk-sensitive planning

For a finite set of scenarios s with probabilities \(p_s\), let \(L_s(x)\) denote the loss associated with a planning decision x. For confidence level \(\alpha\), define

\[
\operatorname{CVaR}_\alpha(L)
=\min_\eta\left[
\eta+\frac{1}{1-\alpha}\sum_s p_s\max(L_s-\eta,0)
\right].
\]

1. Introduce auxiliary variables \(\xi_s\) and write a linear optimization representation of CVaR when each \(L_s(x)\) is linear.
2. Explain the role of \(\eta\) and \(\xi_s\).
3. Explain how an objective such as \(\mathbb E[L(x)]+\lambda\operatorname{CVaR}_{0.95}(L(x))\) changes the decision-maker's risk preference.
4. Distinguish expected cost, worst-case cost, and CVaR. Explain why CVaR is not simply the maximum scenario loss.
5. Describe a case in which a high renewable-forecast error or prolonged equipment outage could make a tail-risk measure useful.

## Problem 5. Nonanticipativity and scenario-tree formulation

A battery operator must choose an initial state of charge before observing tomorrow's renewable output. After the forecast error is observed, the operator can choose scenario-dependent dispatch.

1. Define first-stage and recourse variables for a two-scenario model.
2. Write the expected-cost objective and identify the constraints that apply in each scenario.
3. Explain why the initial state of charge and any other pre-observation decision must be identical across scenarios.
4. Explain how an incorrectly duplicated first-stage decision in each scenario creates perfect foresight and biases the objective.
5. Extend the explanation to a multistage scenario tree. Which decisions must be equal for scenarios sharing the same observed history?

## Problem 6. Research and model-risk note

Write a 500–700 word note comparing stochastic, robust, and chance-constrained approaches for one electricity infrastructure decision (for example, DER hosting capacity, storage procurement, distribution upgrade timing, or resource adequacy). Specify:

- the decision and time horizon;
- the uncertain quantities and their data sources;
- what is known when each decision is made;
- the uncertainty representation and why it is defensible;
- the risk metric or feasibility criterion;
- sensitivity to scenario probabilities, uncertainty-set size, or confidence level;
- how model misspecification and correlated uncertainty will be assessed;
- what empirical validation would be required before using the result operationally.

## Submission standard

A strong submission separates mathematical uncertainty from parameter uncertainty and model uncertainty. Report units, scenario probabilities, bounds, solver status, and feasibility residuals. Do not interpret a chosen confidence level or uncertainty budget as an externally mandated reliability standard unless an applicable source establishes that equivalence.

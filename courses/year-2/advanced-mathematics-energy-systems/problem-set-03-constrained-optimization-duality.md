# Problem Set 3: Constrained Optimization, KKT Conditions, and Electricity-Market Duality

**Course:** Advanced Mathematical Methods for Energy Systems and Infrastructure Research  
**Modules:** 5, Convex analysis and optimization  
**Suggested effort:** 7–9 hours  
**Prerequisites:** Problem Sets 1–2, multivariable derivatives, linear algebra, introductory economic dispatch

## Instructions

Derive the Lagrangian and state the sign convention for every multiplier. Distinguish equality multipliers from inequality multipliers. Show primal feasibility, dual feasibility, stationarity, and complementary slackness explicitly. Interpret shadow prices in the units implied by the objective and constraints.

## Problem 1. Convex quadratic dispatch and first-order optimality (15 points)

A system operator chooses outputs \(p_1,p_2\) to minimize the convex operating-cost proxy

\[
\min_{p_1,p_2}\quad \frac12p_1^2+p_2^2
\]

subject to

\[
p_1+p_2=10,\qquad p_1\geq0,\quad p_2\geq0.
\]

1. Establish convexity using the Hessian.
2. Form the Lagrangian using a free multiplier \(\lambda\) for the equality and nonnegative multipliers \(\alpha_1,\alpha_2\) for the lower-bound constraints written as \(-p_i\leq0\).
3. Derive the KKT conditions.
4. Solve for the optimum and all multipliers.
5. Explain why the KKT conditions are sufficient for global optimality in this problem.

## Problem 2. Linear economic dispatch and the dual problem (25 points)

Two generators serve demand \(D=80\) MW. Generator 1 has marginal cost $20/MWh and capacity 60 MW. Generator 2 has marginal cost $50/MWh and capacity 50 MW.

The dispatch problem is

\[
\begin{aligned}
\min_{p_1,p_2}\quad&20p_1+50p_2\\
\text{s.t.}\quad&p_1+p_2=80,\\
&0\leq p_1\leq60,\\
&0\leq p_2\leq50.
\end{aligned}
\]

1. Solve the primal problem graphically or by merit order.
2. Write the Lagrangian with free balance multiplier \(\lambda\), nonnegative upper-capacity multipliers \(\mu_1,\mu_2\), and nonnegative lower-bound multipliers \(\alpha_1,\alpha_2\).
3. Derive the dual feasibility inequalities and the dual objective. Your dual should be expressed as a maximization problem.
4. Find a dual-optimal solution and verify that its objective equals the primal objective.
5. State the economic interpretation and units of \(\lambda\), \(\mu_1\), and \(\mu_2\).

## Problem 3. Full KKT verification and complementary slackness (20 points)

Using the dispatch problem in Problem 2:

1. Write all KKT conditions: primal feasibility, dual feasibility, stationarity, and complementary slackness.
2. Verify each condition at the optimal primal and dual solution.
3. Explain why the capacity multiplier for generator 1 is positive while the capacity multiplier for generator 2 is zero.
4. What would it mean economically if both capacity constraints were binding? Would both capacity multipliers necessarily be strictly positive? Explain.

## Problem 4. Value functions and marginal system cost (20 points)

Let \(V(D)\) be the minimum dispatch cost as a function of demand, with the same two generators and constraints as Problem 2.

1. Derive \(V(D)\) for all feasible \(D\geq0\).
2. Identify the marginal cost of serving an additional MW below 60 MW and between 60 and 110 MW.
3. What happens at \(D=60\) MW? Explain the relationship between a kink in the value function and the set of optimal balance multipliers.
4. What happens for \(D>110\) MW? Why is it incorrect to report a finite marginal price from this optimization problem in that region?
5. Relate the derivative or subgradient of the value function to the dual multiplier on the energy-balance constraint.

## Problem 5. Model scope and market-price interpretation (20 points)

Write a concise technical memorandum (approximately 500–700 words) addressing the following:

- Under what assumptions can the balance multiplier be interpreted as a short-run marginal energy price?
- How would transmission constraints create different nodal balance multipliers?
- How could ramp limits, reserve requirements, losses, startup costs, and unit commitment alter the optimization problem or price interpretation?
- Why is a dual variable not automatically a forecast of an observed wholesale price?
- What is the difference between a mathematically valid shadow price and a regulatory or tariff-defined compensation rate for a DER?

Use at least one limitation from the simplified two-generator example to support your discussion.

## Submission standard

A complete submission includes the primal and dual formulations, a KKT verification table, the demand value function, and the technical memorandum. Do not report a multiplier without its constraint, sign convention, and units.


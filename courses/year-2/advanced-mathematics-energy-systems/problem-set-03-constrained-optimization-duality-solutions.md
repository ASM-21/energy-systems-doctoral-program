# Problem Set 3: Worked Solutions and Mathematical Notes

## Problem 1. Convex quadratic dispatch and first-order optimality

The Hessian of the objective is

\[
H=\begin{bmatrix}1&0\\0&2\end{bmatrix}\succ0,
\]

so the objective is strictly convex. The feasible set is an affine equality intersected with nonnegative half-spaces, hence convex.

Write the inequalities as \(-p_i\leq0\). The Lagrangian is

\[
\mathcal L=\tfrac12p_1^2+p_2^2
+\lambda(10-p_1-p_2)-\alpha_1p_1-\alpha_2p_2,
\]

with \(\alpha_i\geq0\) and free \(\lambda\). Stationarity gives

\[
p_1-\lambda-\alpha_1=0,
\qquad 2p_2-\lambda-\alpha_2=0.
\]

The remaining KKT conditions are primal feasibility \(p_1+p_2=10\), \(p_i\geq0\); dual feasibility \(\alpha_i\geq0\); and complementary slackness \(\alpha_ip_i=0\).

The optimum is interior, so \(\alpha_1=\alpha_2=0\). Then \(p_1=\lambda\), \(2p_2=\lambda\), and \(p_1+p_2=10\). Thus \(p_1=20/3\), \(p_2=10/3\), and \(\lambda=20/3\). The feasible set is convex and the objective is strictly convex, so this KKT point is the unique global minimizer.

## Problem 2. Linear economic dispatch and the dual problem

Merit order dispatches the cheaper generator to its 60 MW capacity, then supplies the remaining 20 MW from generator 2:

\[
(p_1^*,p_2^*)=(60,20),\qquad C^*=20(60)+50(20)=2200\text{ dollars/hour}.
\]

Use

\[
\mathcal L=20p_1+50p_2
+\lambda(80-p_1-p_2)
+\mu_1(p_1-60)+\mu_2(p_2-50)
-\alpha_1p_1-\alpha_2p_2.
\]

Here \(\mu_i,\alpha_i\geq0\), and \(\lambda\) is free. Stationarity is

\[
20-\lambda+\mu_1-\alpha_1=0,
\qquad
50-\lambda+\mu_2-\alpha_2=0.
\]

For the Lagrangian infimum over nonnegative \(p_i\) to be finite, the coefficients of \(p_i\) must be nonnegative:

\[
\lambda-\mu_1+\alpha_1\leq20,
\qquad
\lambda-\mu_2+\alpha_2\leq50.
\]

The dual can be written with the lower-bound multipliers absorbed into these inequalities (equivalently, optimize over \(p_i\geq0\) directly):

\[
\begin{aligned}
\max_{\lambda,\mu_1,\mu_2}\quad&
80\lambda-60\mu_1-50\mu_2\\
\text{s.t.}\quad&
\lambda-\mu_1\leq20,\\
&\lambda-\mu_2\leq50,\\
&\mu_1,\mu_2\geq0,\quad \lambda\text{ free}.
\end{aligned}
\]

One optimal dual solution is \(\lambda=50\), \(\mu_1=30\), \(\mu_2=0\). The dual objective is \(80(50)-60(30)=2200\), equal to the primal cost. This verifies zero duality gap.

The balance multiplier \(\lambda\) is the marginal value of relaxing the demand-balance requirement by one MW under the chosen sign convention; its units are dollars per MWh for a one-hour dispatch interval. The capacity multiplier \(\mu_1\) is the marginal reduction in objective from increasing generator 1's capacity by one MW for that interval, in dollars per hour per MW of capacity (numerically equivalent to dollars per MWh for a one-hour interval). Generator 2's capacity is not scarce at this optimum, so \(\mu_2=0\).

## Problem 3. Full KKT verification and complementary slackness

At the optimum,

\[
p_1=60,\quad p_2=20,\quad
\lambda=50,\quad\mu_1=30,\quad\mu_2=0,
\quad\alpha_1=\alpha_2=0.
\]

- **Primal feasibility:** \(p_1+p_2=80\); \(p_1=60\) satisfies its upper bound; \(p_2=20\) lies between 0 and 50.
- **Dual feasibility:** \(\mu_1=30\), \(\mu_2=0\), and both lower-bound multipliers are nonnegative.
- **Stationarity:** generator 1 gives \(20-50+30=0\); generator 2 gives \(50-50+0=0\).
- **Complementary slackness:** \(\mu_1(p_1-60)=30(0)=0\); \(\mu_2(p_2-50)=0(-30)=0\); \(\alpha_ip_i=0\).

Generator 1 is at its upper limit and relaxing that limit would allow replacement of more expensive generator 2 output, so its capacity multiplier is positive. Generator 2 has unused capacity, so its upper-bound multiplier is zero.

If both upper bounds bind, both multipliers are nonnegative but neither is required to be strictly positive. A binding constraint can have zero marginal value in degenerate or redundant cases. Binding describes the primal solution; a positive multiplier describes a strictly positive local marginal value under the model and regularity conditions.

## Problem 4. Value functions and marginal system cost

For \(0\leq D\leq60\), generator 1 alone serves demand:

\[
V(D)=20D.
\]

For \(60<D\leq110\), generator 1 is at capacity and generator 2 supplies the remainder:

\[
V(D)=20(60)+50(D-60)=50D-1800.
\]

For \(D>110\), the problem is infeasible. The marginal cost is $20/MWh below 60 MW and $50/MWh between 60 and 110 MW. At 60 MW the value function has a kink: its left derivative is 20 and its right derivative is 50. The set of supporting subgradients is the interval [20, 50], which corresponds to non-unique optimal balance multipliers at the transition.

Above 110 MW, no feasible dispatch exists. A finite marginal price cannot be inferred from this infeasible optimization problem; the model needs an additional supply, demand-response, storage, or load-shedding option with an explicit cost or value.

Away from kinks, the derivative of the optimal value with respect to demand equals the optimal multiplier on the balance constraint under the stated Lagrangian convention. At a kink, the multiplier can be set-valued.

## Problem 5. Model scope and market-price interpretation

The balance multiplier can be interpreted as a short-run marginal energy price when the optimization represents the relevant dispatch interval, the objective includes the relevant marginal operating costs, and the modeled constraints and feasible resources adequately represent the market-clearing problem. In the example, the marginal unit is generator 2, so the balance multiplier is $50/MWh when demand is strictly between 60 and 110 MW.

A network-constrained dispatch introduces nodal balance equations and line-flow constraints. The dual multipliers on nodal balances can differ because serving one additional MWh at one node may require redispatch or consume scarce transmission capability. The difference between nodal prices can reflect congestion and, in richer models, marginal losses.

Ramping and reserve requirements add intertemporal or reliability constraints with their own dual values. Losses change the relationship between injections and withdrawals. Startup costs and unit commitment introduce nonconvex, often mixed-integer decisions; ordinary convex duality no longer gives the same complete price-support interpretation for the nonconvex problem. Market rules may apply uplift or other settlement mechanisms.

A dual variable is conditional on the model, data, time resolution, constraint set, and objective. It is not automatically an observed wholesale price or a forecast of one. Actual prices depend on market software, offers, network topology, outages, market rules, settlement intervals, and operator actions.

Finally, a DER's mathematically estimated marginal system value is not automatically its tariff compensation rate. A tariff or regulatory mechanism may include eligibility rules, cost allocation, metering, avoided-cost methods, caps, and policy objectives that are outside the dispatch optimization. A defensible analysis must keep the modeled shadow price distinct from the legally applicable compensation rule.


# Problem Set 8: Worked Solutions and Mathematical Notes

## Problem 1. Two-stage capacity planning

The first-stage decision is capacity K. The recourse variables \(g_L,u_L,g_H,u_H\) are selected after the demand scenario is observed. The stochastic program is

\[
\min_{K,g_s,u_s}\;70K+
0.4(5g_L+100u_L)+0.6(5g_H+100u_H)
\]
subject to
\[
g_L+u_L\geq80,\quad g_H+u_H\geq120,
\]
\[
g_L\leq K,\quad g_H\leq K,
\]
\[
0\leq K\leq120,\quad g_s,u_s\geq0.
\]

For a fixed K, dispatch is \(g_s=\min(D_s,K)\) and unserved demand is \(u_s=\max(D_s-K,0)\), because generation costs 5 while unserved demand costs 100. The expected objective is

\[
C(K)=70K+\mathbb E[5\min(D,K)+100(D-K)^+].
\]

For \(0\leq K\leq80\), both scenarios are capacity-constrained, so

\[
C(K)=70K+5K+100(104-K)=10400-25K.
\]

This decreases with K. For \(80\leq K\leq120\),

\[
C(K)=70K+5(0.4\cdot80+0.6K)+100(0.6)(120-K)
=7360+13K.
\]

This increases with K. Therefore \(K^*=80\) MW. The recourse decisions are:

| Scenario | Generation | Unserved demand |
|---|---:|---:|
| Low | 80 MW | 0 MW |
| High | 80 MW | 40 MW |

The optimal expected cost is \(C(80)=8400\) dollars for the modeled planning period.

The expected demand is \(0.4(80)+0.6(120)=104\) MW. The deterministic expected-value model chooses K=104 MW, generation 104 MW, and no unserved demand. Evaluated under the original scenarios, this decision incurs capacity cost \(70(104)=7280\), expected generation cost \(5[0.4(80)+0.6(104)]=472\), and expected unserved-demand penalty \(0.6(100)(16)=960\). Thus EEV = \(8712\).

With perfect information, capacity is chosen after demand is known. Since the marginal capacity cost 70 is less than the avoided unserved-demand penalty net of generation cost (\(100-5=95\)), capacity equals realized demand in each scenario. The scenario cost is \(75D\), so the wait-and-see expected cost is \(75(104)=7800\).

For this minimization problem:

\[
\operatorname{VSS}=\operatorname{EEV}-\operatorname{RP}
=8712-8400=312,
\]
\[
\operatorname{EVPI}=\operatorname{RP}-\operatorname{WS}
=8400-7800=600.
\]

The stochastic program chooses one capacity decision before uncertainty is revealed, while allowing scenario-specific recourse. Replacing uncertain demand with its mean discards the distribution and the nonlinear cost of shortfall.

## Problem 2. Budgeted uncertainty

The worst-case aggregate demand solves

\[
\max_z\;40+30+20+8z_1+6z_2+4z_3
\]
subject to \(0\leq z_i\leq1\) and \(\sum_i z_i\leq\Gamma\).

The deviations are ordered 8, 6, and 4 MW. The maximizer allocates the uncertainty budget to the largest deviations first:

- \(\Gamma=1\): add 8 MW; total = 98 MW.
- \(\Gamma=1.5\): add \(8+0.5(6)=11\) MW; total = 101 MW.
- \(\Gamma=3\): add \(8+6+4=18\) MW; total = 108 MW.

The robust capacity requirement is at least the corresponding worst-case total. At \(\Gamma=1\), only one zone can reach its full deviation at a time; at \(\Gamma=1.5\), the second-largest deviation can reach half its bound after the largest reaches its bound; at \(\Gamma=3\), all zones may simultaneously reach their maximum. A box set permits \(z_i=1\) for every i and therefore gives 108 MW, equivalent to this full-budget case.

The uncertainty budget is a modeling choice, not a probability. It should be calibrated or stress-tested against observed forecast errors, dependence, and the decision-maker's risk tolerance. A smaller Γ can understate joint extremes if correlations or common drivers are ignored.

## Problem 3. Chance constraints

The chance constraint is

\[
\Pr(D\leq K)\geq0.95.
\]

For a normal random variable this is equivalent to

\[
K\geq\mu+z_{0.95}\sigma
=100+1.64485(15)=124.67\text{ MW}.
\]

At 99%,

\[
K\geq100+2.3263(15)=134.89\text{ MW}.
\]

The probability statement concerns one modeled hour under the assumed distribution. It does not establish annual LOLE, EUE, loss-of-load probability over all hours, or compliance with a planning criterion. Annual risk depends on temporal dependence, weather regimes, outage processes, correlated load and renewable output, transmission constraints, and the distribution of extreme events.

Potential weaknesses include non-normal/heavy-tailed errors, biased forecasts, heteroskedasticity, serial dependence, weather-driven correlation, small samples, regime changes, and omitted transmission or unit outages. A numerical quantile is only as credible as the distribution and data-generating assumptions.

## Problem 4. CVaR

Introduce \(\xi_s\geq0\) and impose

\[
\xi_s\geq L_s(x)-\eta\quad\forall s.
\]

Then minimize

\[
\eta+\frac{1}{1-\alpha}\sum_s p_s\xi_s.
\]

The variable η is a threshold associated with the value-at-risk quantile; ξ captures the amount by which scenario loss exceeds that threshold. If losses are linear in x, these constraints preserve linearity. The parameter λ controls the weight placed on tail risk relative to expected loss. λ=0 recovers expected-loss minimization; larger λ favors decisions with lower upper-tail losses, potentially at higher expected cost.

Worst-case loss focuses only on the single largest modeled scenario. CVaR averages losses in the upper tail beyond a quantile, accounting for both severity and probability. At finite scenario resolution, care is needed with quantile ties and probability mass at η. CVaR is not a guarantee against scenarios omitted from the model.

## Problem 5. Nonanticipativity

Let \(e_0\) be the initial state of charge selected before renewable output is observed. For scenario s, let charge \(c_s\), discharge \(d_s\), and later state of charge \(e_{1,s}\) be recourse decisions. An expected-cost model may be written

\[
\min_{e_0,c_s,d_s,e_{1,s}}\;C_0(e_0)+\sum_s p_s C_s(c_s,d_s,e_{1,s})
\]

subject to common initial bounds, scenario-specific power balance and storage dynamics, and

\[
e_{1,s}=e_0+\eta_c c_s-\frac{d_s}{\eta_d}.
\]

The same \(e_0\) must be used in every scenario because it is chosen before the scenario is known. If each scenario receives an independent initial state, the model lets the operator choose different pre-event actions with perfect knowledge of the future. This artificially enlarges the feasible set and generally understates expected cost.

In a multistage scenario tree, two scenarios sharing the same observed history must have identical decisions at every node before their paths diverge. Once new information separates them, later decisions may differ. These are nonanticipativity constraints.

## Problem 6. Research and model-risk note

There is no universal preferred method. A strong note explains why the uncertainty representation matches the decision and information structure. Stochastic optimization needs credible scenario probabilities; robust optimization needs a defensible uncertainty set; chance constraints need a validated distribution and meaningful probability target. Compare solutions across reasonable probability estimates, uncertainty budgets, and confidence levels. Identify whether correlations, temporal dependence, and structural breaks are represented. A result should not be used operationally without out-of-sample validation, engineering feasibility checks, and review of the applicable planning or regulatory criteria.

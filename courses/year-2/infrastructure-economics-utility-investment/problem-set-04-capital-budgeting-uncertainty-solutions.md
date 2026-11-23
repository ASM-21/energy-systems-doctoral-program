# Solution Notes: Utility Capital Budgeting Under Uncertainty

All values are hypothetical. The calculations use end-of-year annual net benefits and a real discount rate with real-dollar cash flows. The exercise is not a utility rate-case model or a complete benefit-cost analysis.

## Problem 1 — Base-case NPV

Annual net benefit is $6m - $1m = $5m.

The 10-year annuity factor at 7% is:

[1 - (1.07)^(-10)] / 0.07 = 7.02358

NPV:

-$30m + $5m × 7.02358 = +$5.118m

Simple payback is $30m / $5m = 6 years. This ignores the time value of money, cash flows after payback, uncertainty, and any residual value or decommissioning cost.

The break-even annual net benefit is:

$30m / 7.02358 = $4.271m/year

Positive NPV is not sufficient by itself for regulatory approval. The analysis must establish that benefits are incremental, avoid double counting, assess distributional effects and alternatives, test reliability and safety, examine prudence and procurement, and consider whether the relevant benefits accrue to the customers who bear the costs. The applicable statutory standard and commission record also matter.

## Problem 2 — Sensitivity

The NPV formula is NPV = -30 + B × AF(r,10), where B is annual net benefit in millions.

| Real discount rate | $3m/year | $5m/year | $7m/year |
|---|---:|---:|---:|
| 5% | -$6.835m | +$8.609m | +$24.052m |
| 7% | -$8.929m | +$5.118m | +$19.165m |
| 9% | -$10.747m | +$2.088m | +$14.924m |

Break-even annual net benefit:
- 5%: $30 / 7.72173 = $3.885m/year.
- 7%: $30 / 7.02358 = $4.271m/year.
- 9%: $30 / 6.41766 = $4.675m/year.

The decision is sensitive to annual net benefit and the discount rate. The gross-benefit estimate is especially uncertain because avoided outage damages require a credible interruption-cost methodology, customer mix, outage frequency/duration, and counterfactual. Capital cost and useful life also matter. A single NPV should be reported with a range and the assumptions that drive it.

## Problem 3 — Scenario-weighted benefits

Annual net benefits:
- Low: $4m - $1m = $3m.
- Base: $6m - $1m = $5m.
- High: $9m - $1m = $8m.

Expected annual net benefit:

0.25 × 3 + 0.50 × 5 + 0.25 × 8 = $5.25m

Expected NPV:

-$30m + $5.25m × 7.02358 = +$6.8738m

State NPVs:
- Low: -30 + 3 × 7.02358 = -$8.929m.
- Base: -30 + 5 × 7.02358 = +$5.118m.
- High: -30 + 8 × 7.02358 = +$26.189m.

Expected NPV does not describe the probability of loss, downside severity, or the possibility that low benefits persist across all years. It assumes the state is fixed and applies to each year's net benefit. If annual benefits are correlated, degrade over time, depend on weather or system conditions, or have a non-linear relationship with investment and reliability, a scenario tree or simulation is more appropriate. Probability estimates should be supported by engineering evidence and historical data, not selected to make the project pass.

Under the stated assumptions, present value is linear in annual benefit, so discounting the expected cash flow equals the expected present value. This equivalence does not remove the need to examine risk, option value, or non-linear constraints.

## Problem 4 — Perspectives and transfers

- Utility ledger: capital outlay, O&M, tax treatment, depreciation, financing costs, allowed revenue recovery, and any performance incentive or penalty.
- Customer ledger: rates and bills, payment timing, service reliability, outage experience, and distribution of benefits and costs across customer groups.
- Societal ledger: real construction and operating resources, avoided interruption damages, environmental externalities, and other incremental welfare effects.

Rate payments and allowed revenue are transfers from customers to the utility, not by themselves net societal benefits. The physical resources used to build and operate the project are real costs. Avoided outage damages may be societal benefits, but the analyst must ensure they are not also counted as a separate customer benefit in the same total. A customer bill reduction is a distributional outcome; it is not automatically a reduction in resource cost.

Regulatory accounting determines when and how the utility may recover investment. Construction work in progress treatment, in-service requirements, depreciation, and allowed return affect cash flow, bill timing, and risk allocation. They do not, by themselves, change the engineering performance of the installed equipment.

## Problem 5 — Real options

The pilot can have value because it reveals information before the utility commits the remaining capital. The option to stop can avoid a larger loss if the pilot indicates poor performance. To quantify the strategy, the analyst needs prior probabilities of technical/economic states, conditional probabilities of pilot outcomes given each state, posterior probabilities, remaining project cost, benefit streams after each outcome, discounting, and any delay or lost-benefit effects.

A one-year delay can reduce value because benefits are deferred, construction costs may rise, incentives or grants may expire, and system conditions may change. The pilot also has direct cost and may not provide sufficiently informative evidence. The value of information is greatest when uncertainty is decision-relevant and the decision can still be changed after learning.

A decision tree should explicitly show prior state probabilities, pilot signal likelihoods, posterior state probabilities using Bayes' rule, the decision to proceed or abandon, and discounted terminal values. No numeric expected value can be calculated from the information supplied because the probabilities and conditional outcomes are intentionally unspecified.

## Problem 6 — Risk allocation

Construction cost and schedule are often partly controllable through project management and procurement, but exposed to supply-chain and permitting shocks. Utilization and load-growth risks are shared with customers and depend on planning assumptions. Technology and performance risks depend on vendor maturity, integration, and operating practice. Regulatory risk arises from uncertain approval and recovery treatment. Stranded-asset risk is higher when the project is specialized, long-lived, or exposed to policy and technology changes.

A balanced approach can place controllable procurement and execution overruns on shareholders subject to defined exceptions, while allowing recovery of prudent and necessary investment that delivers verified service benefits. Exogenous costs may receive narrow, audited treatment. Performance metrics and post-investment review should test whether promised benefits materialized. Full automatic pass-through can weaken discipline; full shareholder exposure can deter prudent investments whose benefits are broad and long-lived.

A project can be prudent ex ante even if an unforeseeable event reduces realized benefits. Prudence review should evaluate information reasonably available when the decision was made, not simply judge the decision by hindsight. The regulator can still examine mitigation, ongoing operation, and whether future spending remains justified.
# Problem Set 4: Utility Capital Budgeting Under Uncertainty

**Level:** Graduate applied infrastructure economics  
**Suggested effort:** 3–4 hours  
**Prerequisites:** Problem Set 1 revenue requirement and WACC; introductory engineering economy and probability

All figures are hypothetical, in real dollars at Year 0 purchasing power unless stated otherwise. This is a societal/economic screening model unless a question explicitly asks for a utility cash-flow perspective. Do not combine customer benefits, utility cash flows, and transfers without identifying whose perspective is being modeled.

## Case: Distribution automation investment

A utility is evaluating a distribution automation project with an initial capital cost of $30 million at Year 0. The project has a 10-year evaluation life, no terminal salvage value, and no residual decommissioning cost in the base case. The real discount rate is 7%.

The project is expected to produce annual gross benefits of $6 million and incremental annual operating and maintenance expense of $1 million, both received or incurred at each year-end for Years 1–10. Treat annual net benefit as constant in the base case.

The gross benefit estimate includes avoided outage costs and operating efficiencies. It is not yet supported by a detailed customer interruption-cost study. Ignore taxes, depreciation tax shields, financing structure, construction delay, and rate recovery for the base NPV calculation.

## Problem 1 — Base-case net present value

1. Calculate annual net benefit.
2. Calculate the 10-year present-value annuity factor at 7%.
3. Calculate the project's NPV.
4. Calculate the simple undiscounted payback period. Explain why it is not a substitute for NPV.
5. Calculate the annual net benefit required for NPV = 0 at 7%.
6. Explain whether positive NPV alone establishes that the project should be approved by a regulator.

## Problem 2 — Sensitivity and break-even analysis

Calculate NPV for annual net benefits of $3m, $5m, and $7m at real discount rates of 5%, 7%, and 9%. Present a 3×3 sensitivity table.

1. Identify the combinations with positive and negative NPV.
2. Explain which assumptions have the greatest influence on the decision.
3. Calculate the break-even annual net benefit at each discount rate.
4. Explain why a single-point estimate can create false precision when benefit estimates are uncertain.

## Problem 3 — Scenario-weighted benefits

Suppose gross annual benefits have three possible states, with probabilities:

| State | Gross annual benefit | Probability |
|---|---:|---:|
| Low | $4m | 0.25 |
| Base | $6m | 0.50 |
| High | $9m | 0.25 |

Incremental annual O&M remains $1m in every state.

1. Calculate annual net benefit in each state.
2. Calculate expected annual net benefit.
3. Calculate expected NPV at 7%, using the expected annual net benefit and the base annuity timing.
4. Calculate NPV in each state.
5. Explain why expected NPV is not a complete risk assessment. Discuss correlation, tail risk, probability quality, and whether the benefits are genuinely additive across years.
6. Explain why discounting expected cash flows is valid under the stated linear assumptions, and identify conditions under which a more detailed stochastic model would be needed.

## Problem 4 — Utility, customer, and societal perspectives

Construct three separate conceptual cash-flow ledgers:

- Utility perspective: capital expenditure, incremental O&M, allowed revenue recovery, tax and financing effects where applicable.
- Customer perspective: rate changes, bill savings or increases, reliability improvements, and distribution of impacts.
- Societal perspective: real resource costs, avoided outage damages, externalities, and other incremental welfare effects.

1. Identify which items are transfers between parties and which represent changes in real resource use or welfare.
2. Explain why revenue recovery is not itself a societal benefit equal to the dollars collected.
3. Explain why avoided outage costs should not be counted twice if they already appear in a customer benefit estimate or a reliability valuation.
4. Describe how the regulatory treatment of construction work in progress, used-and-useful status, depreciation, and return can change timing and incidence without necessarily changing the underlying physical project benefits.

## Problem 5 — Real options and staged investment

The utility can either commit to the full project now or undertake a one-year pilot costing $3 million. The pilot provides information about equipment performance, customer interruption reduction, and integration costs. If the pilot is successful, the utility may proceed with the remaining investment; if unsuccessful, it may stop.

1. Explain the value of information and the option to abandon.
2. Identify the data needed to calculate the expected value of the pilot strategy.
3. Explain how a one-year delay could reduce project value through foregone benefits, changed costs, or lost incentives.
4. Explain why the pilot is not automatically preferable, even when it creates information.
5. Sketch a decision tree with prior probabilities, pilot outcomes, posterior probabilities, investment decisions, and terminal NPVs. Do not invent probabilities that are not supplied.

## Problem 6 — Risk allocation and regulatory prudence

1. Identify construction-cost, schedule, utilization, technology, performance, regulatory, and stranded-asset risks.
2. For each risk, explain whether it is principally controllable by management, externally driven, or shared.
3. Propose a risk-allocation approach between utility shareholders and customers. Explain why automatic full pass-through of all overruns can weaken cost discipline, while full shareholder exposure can discourage socially valuable investment.
4. Specify ex ante review, independent engineering, competitive procurement, contingency, post-investment review, and performance verification requirements.
5. Explain how a regulator should treat a project whose ex ante forecast was reasonable but whose realized benefits are lower because of an unforeseeable external change.

## Submission

Submit a reproducible workbook or script, a one-page sensitivity summary, a three-perspective cash-flow diagram, and a 700–1,000 word investment recommendation. Include an assumptions register, source/evidence classification, real-versus-nominal consistency check, and explicit treatment of uncertainty.

## Evaluation

Mathematical accuracy and reproducibility (25%), cash-flow perspective and transfer accounting (20%), uncertainty/sensitivity (20%), real-options reasoning (15%), risk allocation and prudence (15%), limitations (5%).
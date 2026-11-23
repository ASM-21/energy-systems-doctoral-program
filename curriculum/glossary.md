# Energy Systems and Research Methods Glossary

This glossary defines recurring terms and abbreviations used across the curriculum. Definitions are working explanations for study; controlling legal, tariff, technical-standard, and market-manual language takes precedence in a formal analysis. Follow the source links in the relevant course or casebook for authoritative detail.

## Units and physical quantities

| Term | Meaning | Important distinction |
|---|---|---|
| W, kW, MW | Watt, kilowatt, megawatt; units of power | Power is a rate, not an amount of energy. |
| Wh, kWh, MWh | Watt-hour, kilowatt-hour, megawatt-hour; units of energy | Energy is power integrated over time. A 1 MW load for 1 hour consumes 1 MWh. |
| kVA, MVA | Apparent-power units | Apparent power combines real and reactive power; it is not interchangeable with MW. |
| MW / MVAr | Active and reactive power | Active power performs net work; reactive power supports electric and magnetic fields and affects voltage. |
| Power factor | Ratio of active power to apparent power | A low magnitude can increase current for a given active-power transfer. |
| Per-unit (pu) | Normalized electrical quantity relative to selected base values | Always state base MVA/kVA and voltage bases before comparing per-unit quantities. |
| State of charge (SOC) | Stored energy relative to usable storage capacity | SOC is a state variable; power rating and energy capacity are different constraints. |
| AC / DC | Alternating current / direct current | Distribution systems are predominantly AC; many inverter resources and storage devices interface through power electronics. |

## Grid engineering and distributed energy

| Term | Meaning | Context |
|---|---|---|
| Transmission | High-voltage network moving bulk power over distance | Connects generators, substations, and load centers. |
| Distribution | Lower-voltage network delivering electricity to end users | Includes feeders, transformers, protection, and service connections. |
| Feeder | Distribution circuit serving a geographic or electrical area | Thermal, voltage, protection, and operational limits can constrain new connections. |
| DER | Distributed energy resource | A broad category including distributed generation, storage, controllable load, and other resources connected to distribution or customer systems. |
| EDC | Electric distribution company | A regulated entity responsible for distribution service in its territory; terminology varies by jurisdiction. |
| Interconnection | Process and technical/legal conditions for connecting a resource to the grid | Not the same as approval to participate in wholesale markets. |
| Point of interconnection (POI) | Defined electrical point where a facility connects to a network | The exact point and boundary matter for studies, metering, protection, and responsibility. |
| Hosting capacity | Amount or mix of DER that can be accommodated under specified network and operating assumptions | A screening result, not a universal guarantee or automatic right to interconnect. |
| DERMS | Distributed energy resource management system | Software and controls used to monitor, coordinate, or manage DER behavior. |
| Export limit / export envelope | Maximum permitted or dynamically controlled power export | A flexible limit may vary by time, network condition, or operating instruction. |
| Non-wires alternative | A non-traditional investment or operational solution that may defer or avoid a conventional network upgrade | Must be evaluated for reliability, duration, cost, control, and performance risk. |
| Power flow | Solution describing voltage magnitudes/angles and power flows under specified network conditions | AC power flow models real/reactive power, voltage, and losses; DC power flow is a linearized approximation. |
| Optimal power flow (OPF) | Optimization of power-system operation subject to network and operating constraints | Results depend on objective, network model, constraints, and formulation. |
| N-1 criterion | Planning/operating criterion requiring the system to withstand a specified single contingency | The applicable contingency set and performance standard must be stated. |

## Electricity markets and utility regulation

| Term | Meaning | Context |
|---|---|---|
| RTO / ISO | Regional Transmission Organization / Independent System Operator | Coordinates specified wholesale-market and transmission functions; jurisdiction and responsibilities vary. |
| PJM | Regional transmission organization coordinating the bulk power system and wholesale markets across its footprint | PJM is not the distribution utility and does not replace state distribution-interconnection processes. |
| FERC | Federal Energy Regulatory Commission | Regulates specified interstate wholesale electricity and transmission matters under federal law. |
| PUC / PUC commission | Public Utility Commission or equivalent state utility regulator | State commission authority and terminology depend on state law. |
| LMP | Locational marginal price | Marginal cost of serving an incremental unit of load at a location, reflecting modeled energy, congestion, and losses under the market formulation. |
| Merit order | Dispatch ordering based on incremental offer/cost under a simplified model | Real market dispatch also reflects network constraints, commitment, reserves, ramping, and market rules. |
| Energy market | Market for producing/consuming electricity over a defined operating interval | Energy compensation is distinct from capacity and ancillary-service products. |
| Capacity market | Mechanism intended to procure or compensate resource capability for future adequacy | Accreditation, performance obligations, and market design determine the meaning of procured capacity. |
| Resource adequacy | Ability of the system to meet demand at a defined reliability standard | It is a probabilistic planning question, not simply a comparison of nameplate MW and peak load. |
| UCAP | Unforced capacity | A capacity accreditation measure adjusted for resource unavailability under the applicable market rules. |
| ELCC | Effective load-carrying capability | Measures the additional load a resource or portfolio can support while maintaining a specified reliability level. |
| Ancillary services | Products that support reliable operation, such as frequency regulation and reserves | Product definitions and procurement rules are market-specific. |
| Scarcity pricing | Price formation reflecting tight supply or reserve conditions | Design choices affect incentives, market outcomes, and consumer exposure. |
| Revenue requirement | Regulated revenue a utility is authorized to recover under a specified regulatory framework | It is not identical to cash operating cost or total societal cost. |
| Rate base | Regulator-recognized investment base on which a utility may earn an authorized return | Treatment depends on prudence, used-and-useful standards, depreciation, and jurisdiction-specific rules. |
| Cost allocation | Assignment of system or project costs among customers, utilities, developers, or market participants | Cost causation, beneficiary pays, and policy objectives can produce different allocations. |

## Reliability and uncertainty

| Term | Meaning | Context |
|---|---|---|
| LOLE | Loss-of-load expectation | Expected frequency or duration of shortfall events under a defined metric and simulation method. |
| EUE | Expected unserved energy | Expected energy not served because available supply is insufficient. |
| LOLP | Loss-of-load probability | Probability of a shortfall in a defined time interval or state. |
| Monte Carlo simulation | Repeated sampling from a probabilistic model | Results depend on the assumed distributions, dependence, sample size, and model structure. |
| Markov chain | Stochastic process whose next state depends on the current state under the Markov assumption | Useful for weather regimes, outages, and operating states; transition probabilities require justification. |
| Robust optimization | Optimization against a defined uncertainty set | A worst-case result depends on the uncertainty set and can be conservative. |
| Stochastic optimization | Optimization over specified uncertain scenarios and probabilities | Scenario design and probability calibration are central assumptions. |

## Econometrics and causal inference

| Term | Meaning | Common mistake to avoid |
|---|---|---|
| Estimand | The precise quantity a study seeks to learn | Choosing an estimator before defining the estimand. |
| Estimator | A statistical procedure or formula used to estimate an estimand | A precise estimate does not prove the estimand is identified. |
| Identification | Conditions under which the target quantity is determined by the observed-data distribution and assumptions | Identification is not the same as estimation or statistical significance. |
| Potential outcomes | Outcomes each unit would experience under alternative treatment states | Only one treatment state is observed for a unit at a time. |
| SUTVA | Stable Unit Treatment Value Assumption, commonly including no interference and well-defined treatment versions | Network spillovers can violate no-interference assumptions. |
| Interference | One unit's treatment affects another unit's outcome | Requires explicit exposure definitions or a design that accommodates spillovers. |
| ITT | Intention-to-treat effect of assignment or offer | Not automatically the effect of actual participation. |
| LATE | Local average treatment effect for compliers under an instrumental-variable design and its assumptions | Does not generally equal the population average treatment effect. |
| Difference-in-differences (DID) | Comparison of outcome changes across treated and comparison groups | Causal interpretation requires a credible counterfactual trend and attention to timing/heterogeneity. |
| Parallel trends | Assumption that treated and comparison groups would have followed comparable untreated outcome trends | Pre-trend similarity is informative but cannot prove the assumption. |
| Event study | Dynamic estimation around an event or treatment time | Coefficients depend on treatment timing, comparison group, and estimator design. |
| Instrumental variable (IV) | Variable used to isolate exogenous treatment variation | Relevance alone is insufficient; exclusion and independence are also critical. |
| Regression discontinuity (RD) | Design using treatment assignment changes at a cutoff | Requires continuity near the cutoff and checks for manipulation and sorting. |
| Synthetic control | Weighted combination of comparison units used to approximate a treated unit's counterfactual | Donor-pool quality and pre-treatment fit are central; placebo ranks are not automatically randomization p-values. |
| Interrupted time series (ITS) | Time-series design estimating outcome level/trend changes after an intervention | Concurrent shocks, seasonality, autocorrelation, and counterfactual specification matter. |
| HAC standard errors | Heteroskedasticity- and autocorrelation-consistent covariance estimates | HAC changes estimated uncertainty; it does not remove serial correlation or fix a misspecified mean model. |
| GLS | Generalized least squares, which uses a specified or estimated error covariance structure | Efficiency and inference depend on the covariance model being adequate. |
| AR(1) | First-order autoregressive process in which the current error depends on the previous period's error | It is a model assumption, not a generic label for all time dependence. |
| Censoring | Event time is only partially observed for some units | Treating censored observations as if the event occurred at the censoring time biases analysis. |
| Competing risks | Multiple mutually exclusive event types can prevent the event of interest | Cause-specific hazards and cumulative incidence answer different questions. |
| Placebo test | Diagnostic analysis using a false treatment date, unit, or outcome | A placebo result is a diagnostic, not a substitute for identification. |

## Research quality and evidence

| Term | Meaning |
|---|---|
| Descriptive analysis | Summarizes observed patterns without claiming a causal effect. |
| Predictive model | Forecasts outcomes under a specified data-generating and validation setup; predictive accuracy is not causal identification. |
| Synthetic data | Artificially generated observations used to test methods or demonstrate model behavior; not evidence about actual utilities or customers. |
| Reproducibility | Ability to regenerate reported results from documented code, inputs, dependencies, and instructions. |
| External validity | Extent to which a result applies to other populations, places, periods, or institutional settings. |
| Model risk | Risk that assumptions, data, specification, implementation, or use cause misleading conclusions or decisions. |
| Primary source | Controlling or original material such as statutes, regulations, commission orders, tariffs, market manuals, official datasets, and standards. |

## Notation used in technical materials

| Symbol | Typical meaning | Check the local model for |
|---|---|---|
| (P) | Active power | MW/kW units and sign convention |
| (Q) | Reactive power | MVAr/kVAr units and sign convention |
| (V) | Voltage magnitude or voltage phasor | Line-to-line versus line-to-neutral base |
| (\theta) | Voltage phase angle | Radians/degrees and reference bus |
| (x) | Reactance or a generic decision variable | Context and units |
| (\beta) | Regression or model parameter | Parameterization and reference category |
| (SE(\hat\beta)) | Standard error of an estimated parameter | Covariance estimator and sampling assumptions |
| (CI) | Confidence interval | Confidence level and method |
| (W) | Network/spatial weights matrix | Construction, direction, normalization, and interpretation |
| (Z_i) | Treatment assignment for unit (i) | Offer, eligibility, or actual participation |
| (Y_i(z,e)) | Potential outcome under own treatment (z) and exposure (e) | Exposure mapping and interference assumptions |

When a term has a formal definition in a tariff, regulation, market manual, or technical standard, cite that controlling source in research work rather than relying on this glossary.

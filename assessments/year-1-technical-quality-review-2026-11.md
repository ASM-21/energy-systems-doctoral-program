# Year 1 Technical Quality Review — November 2026

**Review type:** Targeted mathematical, numerical, and instructional audit  
**Review scope:** Selected Year 1 worked solutions and the learner-facing power-systems course sequence  
**Disposition:** Corrections committed; broader course audit remains in progress

This is an internal quality review of selected materials, not an external peer review or a certification that every course artifact is error-free. The review separates mathematical correctness from instructional completeness and from whether a model is suitable for real operational decisions.

## Summary

Five material issues were identified and corrected:

1. A two-node congestion exercise had a generator-capacity limit that bound simultaneously with the line limit. This made the intended nodal-price comparison degenerate and contradicted the worked explanation. The generator capacity and comparison line limit were revised so the example isolates congestion and produces the intended locational price separation.
2. The worked solution for the scarcity/reserve co-optimization exercise contained an arithmetic error in the objective value. The initial 150 MW case was corrected to $3,720 for the interval, then a further dual-degeneracy audit moved the teaching case to 160 MW demand with a stable benchmark objective of **$4,270 for the one-hour interval**.
3. The demand-response solution correctly selected 100 MW but contained contradictory and economically incorrect prose about why additional demand response would be used. The explanation now correctly identifies the marginal substitution: demand response at $50/MWh displaces Unit C at $60/MWh for the first 100 MW, but further demand response would displace Unit B at $35/MWh and is not economic.
4. A three-bus DC power-flow explanation described a 7.5 MW flow as an export from bus 3 when it is an import to bus 3. The net balance is now stated correctly.
5. The reserve co-optimization example initially placed the energy demand exactly at a kink where Unit C's energy dispatch was zero. At that point the energy-balance dual was non-unique and the solver's selected dual did not equal the right-hand finite difference. Demand was raised from 150 to 160 MW so Unit C has positive energy dispatch and the reported USD 55/MWh dual is locally stable.

The Y1-01 power-systems course overview was also reorganized into a complete assignment table, with each of its five problem sets linked to its worked solution and estimated effort. The distinction between the simplified radial feeder screen and the unbalanced AC OpenDSS benchmark is explicit.

## Detailed correction record

### 1. Y1-03 Problem Set 1 — two-node congestion

**Files:** `problem-set-01.md`, `problem-set-01-solutions.md`

The original exercise assigned the low-cost generator a 150 MW capacity while node 1 demand was 100 MW and the line transfer limit was 50 MW. At the optimum, both the generator limit and the line limit bound. The resulting LP is degenerate for the intended nodal-price interpretation: the right-hand marginal cost of serving an additional MW at node 1 is not represented by the simplistic claim that the node 1 price must equal $20/MWh.

**Correction:** node 1 generation capacity is now 250 MW. At a 50 MW line limit, the dispatch is 150 MW at node 1, 50 MW at node 2, and 50 MW flow from node 1 to node 2. Node 1 can serve incremental demand locally at $20/MWh, while node 2's incremental demand is served by its $70/MWh generator because the line is binding. Increasing the line limit to 150 MW allows 100 MW of transfer, dispatches 200 MW at node 1 and zero at node 2, and produces a common $20/MWh marginal price at both nodes.

This is still a two-node, lossless, single-period teaching LP, not a full DC or AC optimal power flow.

### 2. Y1-03 Problem Set 5 — energy and reserve co-optimization

**File:** `problem-set-05-scarcity-resource-adequacy-solutions.md`

The initial arithmetic correction produced a 150 MW-demand case with A = 80 MW energy, B = 70 MW energy, and C = 20 MW reserve, at $3,720 for the interval. However, that point lies at a kink: Unit C has zero energy dispatch, so the left-hand marginal cost is $32/MWh while the right-hand marginal cost is $55/MWh. A solver may return a valid dual at the kink that does not equal the right-hand finite difference. The problem was therefore revised to 160 MW demand. The stable solution is A = 80 MW energy, B = 70 MW energy, C = 10 MW energy, and C = 20 MW reserve. The objective is `80 × 18 + 70 × 32 + 10 × 55 + 20 × 2 = $4,270` for the one-hour interval. The energy dual is $55/MWh and reserve marginal value is $2/(MW-h), both verified by one-MW finite differences. The new computational companion independently checks primal feasibility, capacity shadow values, duals, and finite-difference sensitivities.

### 3. Y1-02 Problem Set 3 — demand response

**File:** `problem-set-03-carbon-demand-response-solutions.md`

The optimal dispatch at zero carbon price is A = 500 MW, B = 400 MW, C = 0 MW, and demand response = 100 MW. Served demand is 900 MW. The first 100 MW of demand response displaces Unit C at $60/MWh because demand response costs $50/MWh. Beyond 100 MW, additional demand response would displace Unit B at $35/MWh, so the optimizer does not use the remaining capability. The corrected explanation distinguishes the $10/MWh savings from enabling the first 100 MW of demand response from the shadow value of increasing the stated 200 MW upper bound, which is zero because that bound is not binding.

### 4. Y1-01 Problem Set 2 — DC flow interpretation

**File:** `problem-set-02-solutions.md`

The numerical DC flow results remain: 32.5 MW from bus 1 to bus 2, 7.5 MW from bus 1 to bus 3, and 17.5 MW from bus 3 to bus 2. At bus 3, the 17.5 MW export to bus 2 is offset by the 7.5 MW import from bus 1, leaving a net export of 10 MW, consistent with 60 MW generation and 50 MW local load.

## Numerical checks retained

- Y1-03 PS5 revised co-optimization: 160 MW energy, 20 MW reserve; dispatch A 80 MW, B 70 MW, C 10 MW energy and C 20 MW reserve; objective $4,270 per one-hour interval; energy dual $55/MWh; reserve marginal value $2/(MW-h). One-MW finite differences reproduce both duals locally.

- Y1-01 PS1 three-phase apparent power at 0.90 power factor: 11.111 MVA; reactive power approximately 4.843 MVAr; line current approximately 464.9 A.
- At 0.98 power factor, line current falls to approximately 427.0 A for unchanged real power and voltage.
- Y1-01 PS1 approximate feeder voltage drop: approximately 285 V or 2.07%; three-phase real loss approximately 129.7 kW under the stated simplified assumptions.
- Y1-01 PS3 baseline branch apparent powers: approximately 0.431, 0.130, and 0.108 MVA for branches 1–2, 2–3, and 2–4 respectively.
- Y1-01 PS3 branch 2–4 at 900 kW PV: `sqrt(800^2 + 40^2) / 1000 ≈ 0.801 MVA`, just above its 0.80 MVA screening limit. The discrete sweep result is not a continuous hosting-capacity estimate.
- Y1-02 PS3 baseline generation cost: $30,000/hour and emissions 680 tCO2/hour. At $100/tCO2, emissions fall to 520 tCO2/hour under the synthetic fleet assumptions.
- Y1-03 PS5 planning reserve requirement: 11,500 MW; net accredited capacity 11,350 MW; shortfall 150 MW; hypothetical annual procurement cost $21 million at $140,000/MW-year.

These are calculations for the specified teaching cases, not measured system outcomes.

## Model and inference safeguards confirmed

- The radial feeder lab is explicitly a balanced, first-order static screen. It does not solve nonlinear AC DistFlow or model losses, phase imbalance, protection, regulators, or time-series coincidence.
- The IEEE 13-node OpenDSS benchmark is an unbalanced nonlinear AC simulation of a published test feeder. It is not a matched validation of the separate synthetic radial feeder.
- The OpenDSS assignment documents that the baseline maximum node voltage already exceeds the selected 1.05 pu threshold. This is correctly treated as a pre-existing benchmark condition, not a PV-caused violation.
- The EIA-861 quantitative-methods solution distinguishes utility-level respondents from state-sector aggregates, flags reporting-definition changes, and rejects unsupported causal inference from aggregate data.
- The Pennsylvania interconnection outcomes assignment explicitly identifies the 2025 status reconciliation gap and the Level 3 threshold inconsistency rather than inventing a completion rate or legal interpretation.

## Remaining review work

The following are not certified by this targeted pass:

- Full independent re-derivation of every Year 1 problem-set solution.
- Clean-environment execution of every computational lab and comparison against an analytical benchmark.
- Complete audit of all source URLs, effective dates, and current tariff/manual provisions.
- Full Year 2 course quality review, including advanced mathematical proof rigor and econometrics identification assumptions.
- Independent expert review of the OpenDSS model setup and its benchmark provenance.

## Review standard going forward

A worked solution is not considered verified merely because it is internally consistent or a CI test passes. For numerical models, retain an independent calculation or benchmark. For optimization, check primal feasibility, objective arithmetic, active constraints, and dual interpretation. For empirical work, check estimands, measurement, assignment mechanisms, and inference separately. For legal and regulatory analysis, cite the controlling document and distinguish binding authority from explanatory or proposed material.

The next review should prioritize the remaining Y1-03 market-clearing exercises and Y1-04 quantitative methods solutions, followed by the Year 2 advanced mathematics and econometrics problem sets.

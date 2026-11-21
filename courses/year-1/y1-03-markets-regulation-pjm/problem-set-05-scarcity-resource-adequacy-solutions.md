# Solution Notes — Scarcity Pricing, Resource Adequacy, and Ancillary-Service Co-Optimization

These notes provide calculation checks and a formulation guide. They do not replace independent derivation or the use of a solver for Problem 3.

## Problem 1 — Energy dispatch and scarcity conditions

The unconstrained merit order is A, B, C. Dispatch is:

- A: 400 MW
- B: 400 MW
- C: 200 MW

The marginal unit is C, so the simplified uniform energy price is $100/MWh. Total hourly production cost is:

\[
400(20)+400(50)+200(100)=48{,}000\text{ dollars/hour}.
\]

After the 30 MW Unit B outage, available B capacity is 370 MW. Dispatch becomes A = 400 MW, B = 370 MW, C = 230 MW. Demand remains fully served and C remains marginal, so the simplified energy price remains $100/MWh. Total cost becomes:

\[
400(20)+370(50)+230(100)=49{,}500\text{ dollars/hour}.
\]

The outage increases cost by $1,500/hour but does not, by itself, create a scarcity price above $100/MWh in this simplified energy-only model. Scarcity pricing reflects the marginal value of an additional unit of system capability when energy or operating reserves are scarce. In a more complete model, the reserve requirement and its scarcity curve can create a reserve shortage price component even when energy demand is fully served. If involuntary load shedding is marginal, the economic value of avoided interruption is related to VOLL, but actual settlement rules, demand curves, caps, and mitigation determine the market price.

A price cap can limit extreme wholesale settlements, but if it binds below the marginal value of scarce capacity it can suppress scarcity rents. Capacity mechanisms, long-term contracts, regulated procurement, demand response, and reliability obligations are examples of complementary resource-adequacy mechanisms. Their design can create separate risks, including over-procurement, poor accreditation, administrative error, and weak incentives for flexibility.

## Problem 2 — Planning reserve margin and capacity procurement

The planning-reserve requirement is:

\[
10{,}000(1+0.15)=11{,}500\text{ MW}.
\]

Net accredited capacity before procurement is:

\[
11{,}200+100-50+100=11{,}350\text{ MW}.
\]

The shortfall is:

\[
11{,}500-11{,}350=150\text{ MW}.
\]

At $140,000/MW-year, annual procurement cost is:

\[
150(140{,}000)=21{,}000{,}000\text{ dollars/year}.
\]

Without the 100 MW demand-response resource, net accredited capacity is 11,250 MW and the shortfall is 250 MW. At the same hypothetical price, annual procurement cost would be $35 million.

Accredited capacity attempts to represent a resource's contribution to reliability, not simply its nameplate rating. For example, solar capacity may have lower contribution during an evening peak; battery capacity depends on duration, state of charge, charging opportunity, and correlated system stress; demand response depends on availability, event duration, customer response, and rebound; thermal generation can be unavailable because of forced outages or fuel constraints. A reserve margin does not establish that resources are deliverable through the transmission system or capable of meeting every ramping, voltage, frequency, or local reliability need.

## Problem 3 — Energy and operating-reserve co-optimization

One valid linear program is:

\[
\min_{p_i,r_i}\sum_i(c_i p_i+q_i r_i)
\]

subject to:

\[
\sum_i p_i=150,
\qquad \sum_i r_i\geq20,
\]

\[
p_i+r_i\leq K_i,\quad p_i\geq0,\quad r_i\geq0.
\]

Here (c_i) is the energy offer, (q_i) the reserve offer, and (K_i) the unit capacity. This is a simplified single-period model: it omits ramp rates, minimum output, start costs, reserve response time, transmission constraints, reserve zones, and uncertainty.

A useful solution check is to recognize that total capacity is 200 MW, so 170 MW must be committed as energy plus reserve. The optimum is:

| Unit | Energy (p_i) (MW) | Reserve (r_i) (MW) | Total (MW) |
|---|---:|---:|---:|
| A | 80 | 0 | 80 |
| B | 70 | 0 | 70 |
| C | 0 | 20 | 20 |

The objective is (80(18)+70(32)+20(2)=4,840) dollars per hour. A and B capacity constraints bind, as do the energy-balance and reserve-requirement constraints. C supplies reserve because its reserve offer is lowest and it has sufficient unused capacity; displacing energy from A or B to hold reserve would require more expensive C energy. Under the stated LP and a conventional minimization-dual sign convention, the energy-balance marginal cost is $55/MWh and the reserve-requirement marginal cost is $2/MW-h over the local range where C has remaining headroom. Verify the dual sign and units in the selected solver.

The energy-balance dual is the marginal system cost of serving one additional MW of demand under the model's assumptions. The reserve-constraint dual is the marginal cost of increasing the reserve requirement by one MW. A sequential reserve process can fail if energy dispatch consumes all available headroom or can be more expensive if it ignores the opportunity cost of withholding capacity during energy dispatch.

**Solver audit:** report the objective, each variable, and which constraints bind. Check primal feasibility independently by recomputing total energy, total reserve, and each (p_i+r_i) against (K_i). Do not infer a dual price from a solver unless the solver reports duals for the exact formulation and sign convention used.

## Problem 4 — Memo evaluation guide

A strong response should distinguish three questions:

1. **Long-run resource adequacy:** are enough accredited resources expected to exist to meet forecast demand and a reliability criterion?
2. **Short-run operating reliability:** can the system balance supply and demand in real time while respecting transmission, reserve, ramping, voltage, frequency, and stability constraints?
3. **Market design and incentives:** do prices and procurement obligations reward the attributes needed, at the right location and time, without excessive cost or double compensation?

Energy-only markets rely more heavily on energy and scarcity rents. Capacity markets procure a forward quantity of accredited capability, but depend on demand-curve design, accreditation, performance obligations, and market power mitigation. Administrative resource-adequacy systems can coordinate procurement but risk political or forecast error and may weaken market-based entry and exit signals.

The memo should discuss how price caps, scarcity adders, operating-reserve demand curves, out-of-market commitments, and uplift can change the relationship between physical scarcity and observed prices. It should also explain why nameplate capacity and accredited capacity are different, why transmission deliverability matters, and why the same battery MW cannot be counted simultaneously as fully available energy, upward reserve, and capacity without accounting for state of charge and duration.

For a PJM public-data research question, examples include comparing scarcity intervals with reserve margins and price outcomes, examining the relationship between capacity accreditation and realized performance, or describing the geographic distribution of congestion and uplift. State the observation unit, public source, time coverage, variable definitions, and identification limits. Avoid causal claims based on correlations alone.

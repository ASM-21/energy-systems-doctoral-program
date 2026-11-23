# Computational Lab: Energy and Operating-Reserve Co-Optimization

**Course:** Y1-03 Electricity Markets, Utility Regulation, and PJM  
**Level:** Graduate linear-programming exercise  
**Data:** Fully synthetic three-generator example  
**Status:** Teaching model, not a PJM market-clearing implementation

## Research question

How does jointly procuring energy and upward operating reserve change generator dispatch, and what do the dual variables say about the marginal value of energy demand and the reserve requirement?

This lab is a computational companion to [Y1-03 Problem Set 5](../../../courses/year-1/y1-03-markets-regulation-pjm/problem-set-05-scarcity-resource-adequacy.md).

## Formulation

For generator \(i\), choose energy dispatch \(p_i\) in MW and upward reserve \(r_i\) in MW. Let \(c_i\) be its energy offer in USD/MWh, \(q_i\) its reserve offer in USD/(MW·h), and \(K_i\) its capacity in MW.

For a one-hour interval:

\[
\min_{p,r}\quad \sum_i(c_i p_i+q_i r_i)
\]

subject to

\[
\sum_i p_i=D,\qquad \sum_i r_i\ge R,
\]

\[
p_i+r_i\le K_i,\qquad p_i,r_i\ge0.
\]

The joint capacity constraint is the key coupling: a MW held as upward reserve cannot simultaneously be dispatched as energy.

## Run

```bash
python -m pip install -r requirements.txt
python cooptimization.py
python -m unittest discover -s . -p "test_*.py" -v
```

## Reproducible benchmark

| Unit | Energy offer (USD/MWh) | Reserve offer (USD/MW·h) | Capacity (MW) |
|---|---:|---:|---:|
| A | 18 | 8 | 80 |
| B | 32 | 5 | 70 |
| C | 55 | 2 | 50 |

Demand is 160 MW and upward reserve is 20 MW. The 160 MW demand avoids a kink at zero dispatch of Unit C and makes the reported energy dual locally unambiguous.

| Unit | Energy (MW) | Reserve (MW) | Total (MW) |
|---|---:|---:|---:|
| A | 80 | 0 | 80 |
| B | 70 | 0 | 70 |
| C | 10 | 20 | 30 |

The objective is **USD 4,270 for the one-hour interval**. The energy-balance dual is **USD 55/MWh** and the reserve-requirement marginal value is **USD 2/(MW·h)**. Capacity shadow values are USD 37/(MW·h) for A, USD 23/(MW·h) for B, and zero for C in this optimum.

The tests check the duals using finite differences: increasing demand by 1 MW raises cost by USD 55 for the interval; increasing reserve by 1 MW raises cost by USD 2 while the same optimal basis remains valid. At 150 MW demand, Unit C's energy dispatch is at its lower bound and the value function has a kink; the energy dual is then non-unique. This benchmark intentionally uses 160 MW.

## Required interpretation

1. Verify energy balance, reserve procurement, and every generator's joint energy-plus-reserve capacity.
2. Explain why A and B are fully committed while C provides reserve.
3. Interpret the energy and reserve duals, including units and sign conventions.
4. Explain why sequential energy-first procurement can miss opportunity costs or become infeasible.
5. Vary demand, reserve requirements, and offers. Identify where the optimal basis changes and dual values cease to apply.
6. Explain why these duals are not automatically PJM LMPs or ancillary-service clearing prices.

## Limitations

This is a single-period, single-node convex LP. It omits network constraints, losses, ramping, minimum output, start-up costs, reserve response times, reserve zones, uncertainty, unit commitment, nonconvex offers, market power, performance penalties, and settlement rules. It does not reproduce PJM's actual energy or reserve co-optimization. All offers and capacities are synthetic.

A dual is a local marginal value conditional on this formulation, data, optimal basis, and solver sign convention. Check finite differences and active constraints before interpreting it. Binding constraints can have zero marginal value, and duals can be non-unique in degenerate LPs.

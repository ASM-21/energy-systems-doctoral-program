# Computational Lab: Three-Bus DC Optimal Power Flow

**Course:** Y2-04 Electricity Market Design and Optimization  
**Model:** Lossless three-bus DC-OPF linear program  
**Inputs:** Synthetic network, offers, demand, and line ratings  
**Dependencies:** Python 3.10+, NumPy, SciPy

## Objective

Couple economic dispatch to a meshed network model. The lab solves for generator outputs and bus voltage angles subject to nodal balance, generator limits, and line thermal limits. It reports nodal balance duals and line-limit shadow values, then checks them with finite differences.

## Run

```bash
python -m pip install -r requirements.txt
python dc_opf.py
python dc_opf.py --line-12-limit 61
python -m unittest discover -s . -p "test_*.py" -v
```

## Base case

The model uses a 100 MVA base and a triangular network:
- Branch 1–2: x=0.10 pu, 60 MW limit.
- Branch 1–3: x=0.20 pu, 60 MW limit.
- Branch 2–3: x=0.10 pu, 60 MW limit.

Generators:
- Bus 1: $20/MWh, 150 MW maximum.
- Bus 2: $50/MWh, 100 MW maximum.
- Bus 3: $80/MWh, 100 MW maximum.

Demand is 100 MW at buses 2 and 3.

Expected benchmark:
- Dispatch: G1=113.333 MW, G2=86.667 MW, G3=0 MW.
- Angles: θ1=0, θ2=-0.060000, θ3=-0.106667 rad.
- Flows: 1→2=60.000 MW, 1→3=53.333 MW, 2→3=46.667 MW.
- Cost: $6,600/hour.
- LMPs: bus 1=$20/MWh, bus 2=$50/MWh, bus 3=$40/MWh.
- The 1–2 positive-direction line limit binds; its local shadow value is $40 per additional MW of transfer capability per hour.

## Validation

The test suite checks dispatch, angles, flows, nodal prices, the line shadow value, demand perturbations, and a one-MW relaxation of the binding line. Finite differences are valid only over the local range where the active set remains unchanged.

## Formulation and limitations

The implementation uses variables [g1, g2, g3, θ2, θ3] with θ1 fixed to zero. It applies the DC relation f_ij = S_base(θ_i-θ_j)/x_ij and nodal balance at each bus.

This is a synthetic lossless DC approximation. It omits voltage magnitude, reactive power, nonlinear losses, AC feasibility, contingencies, reserves, ramping, startup and commitment costs, market power, uplift, and settlement details. It is not a PJM dispatch model or an engineering approval study. Nodal duals and line shadow values are conditional on the exact LP, sign convention, objective units, and active constraints.

## Related curriculum

- [Y2-04 Problem Set 2: Three-Bus DC-OPF](../../../courses/year-2/electricity-market-design-optimization/problem-set-02-three-bus-dc-opf.md)
- [Y2-04 Problem Set 1: Economic dispatch and duality](../../../courses/year-2/electricity-market-design-optimization/problem-set-01-economic-dispatch-duality.md)
- [Three-bus DC power flow foundation lab](../three-bus-dc-power-flow/README.md)

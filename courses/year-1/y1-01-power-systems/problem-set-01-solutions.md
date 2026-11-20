# Y1-01 Problem Set 1 — Solution Notes

These are worked checks, not a substitute for showing the derivation.

## Problem 1

For a balanced three-phase system:

    S = P / pf
    Q = P tan(arccos(pf))
    I = P / (sqrt(3) V_LL pf)

With P = 10 MW, V_LL = 13.8 kV, and pf = 0.90 lagging:

- Apparent power: 11.111 MVA.
- Reactive power: approximately 4.843 MVAr.
- Line current: approximately 464.9 A.

At 0.98 power factor, apparent power falls to approximately 10.204 MVA and line current to approximately 427.0 A; reactive power falls to approximately 2.03 MVAr. Real power is unchanged. This can reduce current and associated I-squared-R losses, but it does not establish available feeder capacity, acceptable voltage, protection coordination, or operational feasibility.

## Problem 2

For a three-phase base expressed using line-to-line voltage and total three-phase apparent power:

    Z_base = V_LL_base^2 / S_3ph_base
    I_base = S_3ph_base / (sqrt(3) V_LL_base)

Therefore:

- Z_base = 13.8^2 / 100 = 1.9044 ohms.
- Z_pu = (0.5 + j1.5) / 1.9044 = approximately 0.2625 + j0.7872 pu.
- I_base = 100 MVA / (sqrt(3) * 13.8 kV) = approximately 4.184 kA.

Per-unit bases allow transformer impedances to be compared across voltage levels when base quantities are transformed consistently. State whether impedance is per phase and use consistent three-phase base conventions.

## Problem 3

Using the current from Problem 1, R = 0.2 ohm/phase, X = 0.4 ohm/phase, cos(phi) = 0.90, and sin(phi) = sqrt(1 - 0.9^2):

- Approximate line-to-line drop: 285.3 V.
- Percentage drop: approximately 2.07% of 13.8 kV.
- Three-phase real loss: 3 I^2 R = approximately 129.7 kW.

These are approximate balanced steady-state calculations using a simplified series model and receiving-end current. They omit shunt capacitance, detailed voltage phasors, voltage-dependent load behavior, unbalance, temperature effects, and network interactions. A feeder may satisfy a voltage criterion but violate a conductor/transformer thermal limit, or vice versa.

## Problem 4

Network: one-line diagram, conductor and transformer impedances/ratings, feeder topology, regulator/capacitor settings, existing constraints, fault levels.  
Load: time-series real/reactive demand, seasonal peaks, load composition, forecast growth.  
Protection/control: relay/fuse settings, recloser coordination, inverter functions, anti-islanding, voltage/reactive-power control, grounding.  
Operating data: voltage and current measurements, topology/status, existing DER output, switching configurations, contingency/abnormal operating practices.

The list is a starting point. A real interconnection assessment must follow the applicable utility process, technical standards, and jurisdictional requirements.
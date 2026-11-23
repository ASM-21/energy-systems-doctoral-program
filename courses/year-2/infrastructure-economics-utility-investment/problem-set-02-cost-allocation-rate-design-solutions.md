# Solution Notes: Cost Allocation and Retail Rate Design

These are benchmark calculations for the stylized assumptions. A correct submission must also explain why these assumptions are not a substitute for a jurisdiction-specific cost-of-service study.

## Problem 1 — Class allocation

Allocation factors:

| Cost pool | Residential | Commercial |
|---|---:|---:|
| Customer: accounts | 100,000 / 120,000 = 83.3333% | 20,000 / 120,000 = 16.6667% |
| Demand: coincident peak | 200 / 300 = 66.6667% | 100 / 300 = 33.3333% |
| Energy: annual kWh | 1.2 / 2.0 = 60% | 0.8 / 2.0 = 40% |

Allocated costs:

| Cost pool | Residential | Commercial |
|---|---:|---:|
| Customer | $33.333333m | $6.666667m |
| Demand | $23.333333m | $11.666667m |
| Energy | $15.000000m | $10.000000m |
| **Total** | **$71.666667m** | **$28.333333m** |

The totals reconcile to $100 million. Residential bears 71.6667% and commercial 28.3333% of the requirement under these stipulated allocators. Residential has 83.33% of accounts, 66.67% of coincident peak, and 60% of energy. Its cost share is a weighted combination of those three shares, with weights determined by the cost pools (40%, 35%, and 25%).

## Problem 2 — Three-part tariff

Customer charge:

`$40,000,000 / (120,000 accounts × 12 months) = $27.7778/account-month`

Demand charge:

`$35,000,000 / (300,000 kW × 12 months) = $9.7222/kW-month`

Energy charge:

`$25,000,000 / 2,000,000,000 kWh = $0.0125/kWh`

Aggregate reconciliation:
- Customer: $27.7778 × 120,000 × 12 = approximately $40 million.
- Demand: $9.7222 × 300,000 × 12 = approximately $35 million.
- Energy: $0.0125 × 2,000,000,000 = $25 million.

The unrounded rates reconcile exactly. Minor displayed differences are rounding. Coincident class peak is a class allocation determinant, not necessarily a directly measurable or suitable monthly billing demand for each account. A tariff may use non-coincident monthly peak, interval demand, seasonal peak, ratchets, or another determinant. Those choices affect incentives and revenue recovery.

## Problem 3 — Representative bills

Residential:
- Fixed: $27.7778 × 12 = $333.33/year.
- Demand: $9.7222 × 5 kW × 12 = $583.33/year.
- Energy: $0.0125 × 10,000 = $125.00/year.
- Total: $1,041.67/year, or $86.81/month.

Commercial:
- Fixed: $333.33/year.
- Demand: $9.7222 × 25 kW × 12 = $2,916.67/year.
- Energy: $0.0125 × 100,000 = $1,250/year.
- Total: $4,500/year, or $375/month.

Component shares:
- Residential: fixed 32.0%, demand 56.0%, energy 12.0%.
- Commercial: fixed 7.41%, demand 64.81%, energy 27.78%.

These accounts are hypothetical and the assumed billing demands are constant each month. The results do not describe actual class distributions. A defensible incidence study would need, at minimum, customer-level or representative-segment interval load shapes, seasonal consumption, monthly demand determinants, customer counts by tariff, income or affordability proxies where lawfully and appropriately available, and the current tariff/bill components. It should also consider distributed generation, arrears, weather, household size or business type, and class migration where relevant.

## Problem 4 — Alternative designs

Design A, volumetric only:

`$100m / 2.0bn kWh = $0.05/kWh`

Design B, 40% fixed and 60% volumetric:
- Fixed pool: $40m / (120,000 × 12) = $27.7778/account-month.
- Volumetric pool: $60m / 2.0bn kWh = $0.03/kWh.

Design C, three-part:
- $27.7778/account-month.
- $9.7222/kW-month.
- $0.0125/kWh.

Under A, customers with higher annual kWh contribute more. Under B, every account pays the same fixed component, while high-use customers contribute more through kWh. Under C, customers with greater billed demand and energy contribute more, alongside the fixed charge. The actual class and customer outcomes depend on tariff determinants and usage distributions. Revenue-neutral class assumptions do not imply every customer is held harmless.

Volumetric charges preserve a marginal kWh price signal but can expose revenue to weather, efficiency, and load changes. Fixed charges stabilize revenue per account but weaken the marginal signal and can be regressive relative to usage or income. Demand charges may better reflect some capacity drivers, but can create high bills for customers with brief peaks and may be difficult to manage without interval data or controllable loads. Time-of-use and dynamic rates can better reflect temporal system costs but require suitable metering, customer response, and protections for customers with limited flexibility.

## Problem 5 — Cost causation

A single kWh allocator assumes that all distribution costs vary with energy throughput. That assumption is generally implausible. Metering, billing, and service-drop activities may be customer-related; conductor, transformer, and substation capacity may be associated with demand, location, or peak coincidence; some losses and energy-dependent operations may vary with throughput. Reliability and resilience investments may have multiple drivers.

Demand-related allocation alternatives include non-coincident peak (each class's own maximum), coincident peak (class demand at the system peak), multiple coincident peaks, or an allocator based on a planning/design peak. Evaluating them requires interval load data, system and class peaks, weather normalization, engineering planning criteria, voltage level, asset utilization, and an explanation of how the selected allocator relates to the costs being assigned. There is no universal allocator independent of the cost study's purpose and governing commission practice.

## Problem 6 — Evidence and process

A utility study, testimony, and bill-impact exhibit describe the utility's proposal and supporting analysis. Intervenor evidence provides competing positions. A settlement records negotiated terms and proposed disposition, but is not itself an operative commission decision. The commission order controls the approved disposition, subject to its terms and effective-date instructions. The approved tariff sheets and their effective status must be checked to establish the rates actually in force.

Forecast load, customer counts, peak timing, load factor, and class migration affect allocator denominators and the resulting shares. A sound analysis should preserve source versions, test alternative determinants, report class averages and distributions separately, show sensitivity ranges, and avoid treating a representative account as a universal customer.
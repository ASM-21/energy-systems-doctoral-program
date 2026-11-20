# Pennsylvania DER Interconnection: Public-Data Feasibility Assessment

**Research setting:** PPL Electric service territory / Pennsylvania / PJM  
**Verification date:** 2026-11-20  
**Status:** Preliminary desktop assessment. This is not a completed records request or a finding about utility performance.

## Executive finding

A feeder-level empirical study of PPL interconnection outcomes is **not currently supported by the public data located in this review**. PPL states that it does not publish hosting-capacity maps or provide specific feeder hosting-capacity information. Its public FAQ identifies a narrower set of locational facts available during site-specific pre-application: substation name, feeder name and voltage, and certain line-distance information. That is not enough to reconstruct feeder headroom or estimate a feeder-level hosting-capacity panel.

The strongest near-term research design is therefore a **regulatory and institutional analysis with a transparent synthetic engineering model**, followed by a targeted search for public docket filings and aggregated interconnection statistics. Do not label a synthetic model output as measured PPL hosting capacity.

## 1. What the public record establishes

### PPL interconnection transparency

PPL's public FAQ explicitly states that it does not currently publish hosting-capacity maps or specific feeder hosting-capacity information. The FAQ says that a site-specific pre-application may provide the substation name, feeder name and voltage, and distances from the substation or line ends to the customer site. It also explains that an Interconnection Impact Review may identify required system reinforcements, including transformer/service upgrades, protective devices, line extensions/reconductoring, and customer relaying/SCADA.

Source: [PPL Electric, Customer-Owned Generation FAQ](https://pplelectric.com/site/More/About-Us/Electric-Rates-and-Rules/Customer-Owned-Generation/frequently-asked-questions), especially the general interconnection topics and costs sections.

### Current Rule 12 tariff

The current Rule 12 source located for this review is PPL Electric Utilities Corporation, Supplement No. 2 to Electric Pa. P.U.C. No. 202, issued June 30, 2026 and effective July 1, 2026. It retains January 3, 2026 as the applicability date for new DER interconnections and specifies smart-inverter and DER-management-device requirements. This later PUC No. 202 supplement should be used for current Rule 12 analysis rather than relying only on the earlier 2026 PUC No. 201 tariff supplement.

Source: [PPL Rule 12, Supplement No. 2 to Electric Pa. P.U.C. No. 202](https://www.pplelectric.com/site/-/media/PPLElectric/At-Your-Service/Docs/Current-Electric-Tariff/2026/August/Rule-12---Distributed-Energy-Resource-Interconnection-Service.pdf).

### Second DER Management Plan order

Prepared testimony by Pennsylvania PUC Chairman Stephen M. DeFrank before the House Energy Committee on March 16, 2026 identifies the Commission's approval of PPL's Second DER Management Plan at its November 20, 2025 public meeting and cites the order as entered December 3, 2025 in Docket P-2024-3049223. The testimony says the plan is projected to increase hosting capacity by **up to 258 MW** and that the Commission directed PPL to conduct an RFP for third-party aggregators.

This is a Commission Chairman's prepared testimony summarizing the order and its projected benefits. The 258 MW figure is a projection attributed to that testimony, not a measured ex-post increase in available feeder capacity. The original December 3, 2025 order and supporting record should be retrieved from the PUC document search before making detailed claims about its conditions, cost recovery, evaluation requirements, or RFP design.

Source: [Prepared Testimony of PUC Chairman Stephen M. DeFrank, March 16, 2026](https://www.palegis.us/house/committees/committee-archives/archive-file?file=2026_0572_0009_TSTMNY.pdf), page 3 and footnote 5.

### Proposed hosting-capacity-map legislation

Pennsylvania House Bill 2429, Printer's No. 3230, was introduced and referred to the House Energy Committee on April 20, 2026. As introduced, it would require EDC hosting-capacity maps by July 1, 2027, updated every two months, and would specify both DER and new-load hosting-capacity information, queued DER, constraints, feeder-level granularity, planned upgrades, voltage levels, and thermal/anti-islanding/voltage limiting criteria.

The bill text is a proposal, not current law. The version reviewed shows referral to committee, not enactment. Recheck the bill's current status before describing any duty as binding.

Source: [Pennsylvania HB 2429, PN 3230](https://www.palegis.us/legislation/bills/text/PDF/2025/0/HB2429/PN3230), introduced April 20, 2026.

## 2. Public-data feasibility matrix

| Research variable | Public status located | Feasibility | Next action |
|---|---|---|---|
| Current interconnection rules | Rule 12 tariff and REMSI materials are public | High for legal/institutional analysis | Maintain a versioned tariff crosswalk and capture later supplements |
| Utility DER-management architecture | PPL public program and tariff descriptions exist | Moderate; implementation detail is partial | Compare tariff obligations, published technical requirements, and Commission order |
| Hosting capacity by feeder | PPL says maps and specific feeder capacity are not published | Low at present | Do not infer or estimate actual feeder values from public materials |
| Site-specific locational pre-application facts | PPL identifies a limited set of fields available upon request | Low for broad empirical panel; potentially useful for a consenting project applicant | Record only applicant-authorized, non-confidential facts; do not collect employer/customer records |
| Application counts, queue age, completion, withdrawal | No comprehensive public PPL dataset established in this review | Unproven | Search docket attachments and annual filings; consider a narrowly scoped public-records request if legally appropriate |
| Upgrade type and cost | PPL FAQ explains categories and customer payment responsibilities; project-level cost data not established | Low to moderate | Extract public examples from adjudicated dockets only; avoid treating examples as representative |
| DER capacity by state/utility | Federal EIA reporting is a candidate aggregate source | Moderate for contextual trends, not feeder causality | Inspect EIA-861 files, definitions, revisions, and utility identifiers |
| PJM wholesale prices and market outcomes | PJM publishes market data at defined market/geographic levels | Moderate for wholesale context, not distribution feeder attribution | Use PJM Data Miner only for variables with a documented geographic and temporal match |
| Feeder loading, voltage, protection settings, DERMS telemetry | Not located as public operational datasets | Very low | Treat as unavailable absent explicit public release |
| Reliability outcomes | Public utility and regulatory reports may contain system-level metrics | Moderate at aggregate level; circuit granularity needs verification | Search PUC filings and any enacted HB 2429-related reporting requirements |

## 3. Recommended research design

### Phase A — Regulatory and institutional paper (feasible now)

Research question: How does Pennsylvania's regulatory framework allocate decision rights, costs, and operational responsibilities across distribution interconnection, utility DER management, third-party aggregation, and PJM wholesale-market participation?

Methods:
1. Build a docket chronology for P-2024-3049223, including petition, interventions, testimony, settlement or stipulations, December 3, 2025 order, tariff compliance filings, and implementation updates.
2. Retrieve and code the original Commission order. Record every directive, deadline, reporting requirement, cost-recovery decision, and RFP obligation.
3. Crosswalk Rule 12, REMSI, the Commission order, the Commission's wholesale DER participation rulemaking (L-2023-3044115), PJM's Order 2222 compliance filings, and applicable FERC orders.
4. Separate distribution-system objectives (voltage, thermal limits, protection, reliability) from wholesale-market objectives (aggregation, dispatch, capacity, energy, ancillary services).
5. Evaluate who bears costs and risks, what performance evidence is required, and how the Commission can assess whether projected benefits materialize.

### Phase B — Quantitative descriptive analysis (conditional)

Proceed only if an auditable public dataset is located. Potential outcomes include annual DER interconnection capacity, application counts, project-size distributions, queue duration, completion/withdrawal rates, upgrade incidence, or program enrollment. Define denominators and censoring rules before calculating rates. Do not combine annual utility-level totals with PJM nodal prices as if they were feeder-level observations.

### Phase C — Engineering model (available as a synthetic methods exercise)

Use the [radial feeder DER hosting-capacity lab](../../../projects/power-systems/radial-der-hosting-capacity/README.md) to demonstrate how DER location and penetration can affect approximate voltage and branch loading. It is not calibrated to PPL, and its outputs cannot be used as evidence of PPL hosting capacity. The next engineering extension should validate against an IEEE distribution test feeder in an AC-capable solver and then add time-series load and PV profiles.

## 4. Explicit hypotheses to test, not assume

- Active inverter management may increase the amount of DER that can be accommodated under specified operating criteria, but the magnitude depends on feeder conditions, control settings, and time coincidence.
- The value of DERMS-enabled flexibility may differ between feeders with voltage constraints and feeders with thermal or protection constraints.
- Hosting-capacity transparency may reduce siting uncertainty for developers, but maps alone do not replace site-specific studies or guarantee interconnection approval.
- Third-party aggregator services may provide distribution or wholesale value, but compensation, dispatch rights, non-performance risk, telemetry, and customer participation rules determine whether the value is realized.

Each hypothesis requires a measurable outcome and a plausible counterfactual or careful descriptive framing. The projected 258 MW figure should not be used as a realized treatment effect.

## 5. Data governance and research boundary

Use only public documents and datasets. Do not use PPL internal work products, nonpublic engineering models, feeder data, customer information, interconnection applications, operational telemetry, or recollections of internal processes. If a future role or project gives access to nonpublic data, keep it outside this independent research unless formal written authorization and institutional review are obtained.

## 6. Open evidence gaps

- Original PUC order entered December 3, 2025 in P-2024-3049223 and all ordering paragraphs.
- PPL's required third-party aggregator RFP, procurement results, contracts or award disclosures, and evaluation metrics.
- Any Commission-required DER orchestration plan or reporting under the Second DER Management Plan.
- Public aggregate interconnection application and outcome statistics.
- Whether HB 2429 advanced beyond committee referral after the version reviewed here.
- Current PJM/FERC compliance status and tariff/manual provisions for the DER Aggregator model.

## Preliminary conclusion

A publishable policy/institutional paper is feasible with the public record, subject to retrieval of the controlling PUC order and associated filings. A rigorous feeder-level econometric paper is not yet feasible on the evidence located. The appropriate response is to close the data gap transparently, not manufacture a panel from incompatible public aggregates.

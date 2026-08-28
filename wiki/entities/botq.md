---
title: BotQ
type: entity
subtype: facility
created: 2026-08-28
updated: 2026-08-28
sources: 4
tags: [figure, botq, manufacturing, humanoid, production, yield, vertical-integration]
---

**BotQ** — [Figure AI](figure.md)'s in-house high-volume humanoid manufacturing facility, announced 2025-03-15. First-generation line rated at **up to 12,000 humanoids per year**, with a stated goal of **100,000 robots over four years**. BotQ is the reason [Figure 03](figure-03.md) exists in the form it does: the robot was redesigned around what the factory can build.

## Why it matters

Most humanoids are, in Figure's words, "engineering prototypes which are time consuming and expensive to produce." BotQ is the first case in this wiki of a humanoid maker **designing the robot to suit a manufacturing process rather than the reverse** ([Figure 03 announcement](../sources/figure-03-announcement.md)):

- Figure 02 was "primarily designed to be manufactured with **CNC machining**."
- Figure 03 "relies heavily on **tooled processes such as die-casting, injection molding, and stamping**" — a large up-front tooling investment traded for per-unit cost that improves with volume.
- Aggressive reduction of part count, assembly steps, and non-critical components.

## Vertical integration

Figure builds **actuators, batteries, sensors, structures and electronics** in-house, all designed internally, and spent a year qualifying outside suppliers for individual components — because "an entirely new supply chain for an industry where one does not currently exist" had to be built. Explicitly **not** contract manufacturing: production of critical systems is in-house "to maintain tight control over quality, iteration, and speed."

## Measured output (April 2026)

From [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md):

| | |
|---|---|
| Figure 03 units delivered | **350+** |
| Production rate | **1/day → 1/hour** (**24×** in under 120 days) |
| Networked workstations | **150+** |
| End-of-line first-pass yield | **>80%**, improving weekly |
| Battery line first-pass yield | **99.3%**, 500+ packs shipped |
| Actuators produced | **9,000+** across **10+ SKUs** |
| In-process inspection points | **50+** |
| End-of-line tests per robot | **80+** functional verifications |

Plus **burn-in**: robots perform squats, shoulder presses and jogging at cycle counts in the thousands to surface early-cycle failures before sign-off.

> [!note] 1/hour is roughly nameplate
> 12,000 units/year is ~1.37/hour on a 24/7 basis. Reaching 1/hour means the 12,000/year claim has stopped being aspirational. No other humanoid maker in the [humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) has publicly claimed a comparable rate.

> [!note] 80% first-pass yield is candour, not a boast
> One robot in five fails end-of-line. Volunteering that — alongside burn-in testing and formal recall-campaign processes — reads as a company that has met real reliability problems at fleet scale, which is itself evidence the fleet is real.

## Software backbone

Custom **Manufacturing Execution System (MES)** with full traceability on every subassembly and final assembly, plus PLM, ERP and WMS integration ([battery post](../sources/figure-f03-battery.md)). Downstream of the line, Figure runs its own **Fleet Management System**, **OTA update infrastructure**, and **Field Service Management** tooling for servicing robots "from our HQ, to customer sites, to residential homes," with formal fleet-wide upgrade and **recall campaign** processes.

## Related

- [Figure 03](figure-03.md) — the product designed around this line.
- [Figure](figure.md) — the company.
- [Helix](helix.md) — fleet size is framed as the input to model capability.

## Mentioned in

- [Introducing Figure 03](../sources/figure-03-announcement.md) — 12,000/year, 100,000 over four years, tooled processes.
- [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md) — the measured ramp and yields.
- [F.03 Battery Development](../sources/figure-f03-battery.md) — in-house battery manufacturing at BotQ.

## Open questions

- **Location and headcount** — never stated in the primaries ingested here; Figure's original BotQ announcement (2025-03-15) is not yet ingested.
- **What is in the 20% that fails first pass?** Rework vs scrap is the economics.
- **Actual annualised output**, as opposed to demonstrated cycle time.

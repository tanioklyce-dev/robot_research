---
title: Ramping Figure 03 Production (Figure AI)
type: source
url: https://www.figure.ai/news/ramping-figure-03-production
author: Figure AI
affiliation: Figure AI
published: 2026-04-29
ingested: 2026-08-28
tags: [figure, figure-03, botq, manufacturing, yield, fleet-management, ota, system-0, perception-conditioned-control, sim-to-real, vendor-source]
---

> [!note] The one Figure post with numbers that behave like manufacturing numbers
> Yield percentages, part counts, inspection-point counts and cycle times are the kind of figures a company does not usually invent, because its own supply chain would notice. Still vendor-stated and unaudited, but this is the least marketing-shaped Figure primary in the wiki after the [battery post](figure-f03-battery.md).

## Summary

Figure's April 2026 manufacturing and fleet-operations update, four months after Figure 03's first shipments. Headline: **over 350 Figure 03 units delivered**, and production rate up **from 1 robot/day to 1 robot/hour — a 24× throughput improvement in under 120 days**. The post covers three things: how [BotQ](../entities/botq.md) scaled, how Figure operates a growing fleet (diagnostics, fallback ladders, field service, OTA), and a new capability that Figure explicitly attributes *to* the fleet's size: **perception-conditioned System 0**, i.e. whole-body control that can see the terrain it is stepping onto, transferring **zero-shot** from simulation to real stairs.

## Key claims

### Production

- **350+ Figure 03 robots delivered**; rate **1/day → 1/hour**, **24× in under 120 days**.
- **150+ networked workstations** running Figure's custom manufacturing execution software; dedicated lines for all critical modules.
- **End-of-line first-pass yield now over 80%** and improving weekly.
- **Battery line at 99.3% first-pass yield**, **500+ packs shipped**.
- **9,000+ actuators produced across 10+ distinct SKUs.**
- **50+ in-process inspection points**; hundreds of suppliers qualified against incoming-inspection criteria.
- **80+ functional verification tests per robot** at end-of-line, plus multi-limb stress testing and **"burn-in" sessions — squats, shoulder presses, jogging at cycle counts in the thousands** — to eliminate early-cycle failures.

### Fleet operations

- Robots are allocated to internal R&D, **data collection**, end-to-end housework, and commercial use-case development. *"The larger our fleet becomes the more data we are generating for Helix."*
- **Diagnostics**: alert system and failure analysis that "pinpoint the root cause of an issue in minutes."
- **Fallback ladders**: software that lets a robot "gracefully degrade its performance or safely recover from a non-critical fault, keeping the use case running."
- **The long tail**: high-frequency hardware/software failures already addressed; focus has shifted to edge cases — *"a stage of maturity that only comes with significant fleet hours."*
- In-house **Field Service Management** system and tooling to service Figure 03 "from our HQ, to customer sites, to residential homes"; formal processes for **fleet-wide upgrades and recall campaigns**.
- Custom **Fleet Management System** tracking real-time health, location and operational status, plus **OTA** update infrastructure to "deploy new behaviors and upgrades to the entire fleet simultaneously."

### Perception-conditioned System 0

- Before: S0 "reasoned only about the robot's own body — joint state, base motion, and proprioception. It walked confidently across flat ground but was blind to the world in front of it. Stairs, ramps, and uneven terrain required **hand-tuned mode switches and operator intervention**."
- Now: RGB from the head cameras goes through Figure's **stereo model** into a 3D representation, which is fed to the policy alongside proprioceptive state — *"S0 doesn't just feel the ground anymore, it sees it."*
- Trained **end-to-end with RL in simulation across thousands of randomised terrains**. The same weights that climb procedurally generated staircases in sim traverse real stairs.
- **Zero-shot transfer** — "no real-world fine-tuning, no domain-specific calibration, no operator-in-the-loop adjustments, and across varying lighting conditions."
- Claim: *"the sim-to-real gap that has historically gated perception-driven control is no longer the bottleneck for this class of behavior."*

## Assessment

> [!note] 1 robot/hour is the number that matters in this whole cluster
> 12,000 units/year at BotQ's stated line capacity is ~1.37/hour on a 24/7 basis, so "1/hour" means Figure is now within the same order as its own nameplate — the 12,000/year claim from the [Figure 03 announcement](figure-03-announcement.md) stops being aspirational. For scale, this is a rate no other humanoid maker in the [humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) has publicly claimed, including Unitree.

> [!note] 80% first-pass yield is a *disclosure*, not a boast
> Volunteering that one robot in five fails end-of-line is unusual candour. Read alongside "burn-in" testing and formal recall-campaign processes, the picture is a company that has met real reliability problems at fleet scale — which is itself evidence the fleet is real.

> [!warning] Delivered ≠ sold, and ≠ deployed
> "Delivered over 350" is unqualified. The operations section makes clear most units go to **internal** R&D and data collection. No customer count, no external deployment count, no revenue.

> [!note] Fleet size is framed as the input to capability, not the output of it
> The post's causal claim runs fleet → data → capability, and names perception-conditioned S0 as the result. This is the same thesis as [Index](../entities/figure-index.md), applied to robot data instead of human phone video — and here Figure at least identifies a concrete capability that arrived with the scale.

## Entities mentioned

- [Figure 03](../entities/figure-03.md) · [BotQ](../entities/botq.md) · [Figure](../entities/figure.md) · [Helix](../entities/helix.md)

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — perception-conditioned S0.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — zero-shot terrain transfer across thousands of randomised terrains.
- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — fallback ladders and graceful degradation.
- [Onboard robot service architecture](../concepts/robotics/onboard-robot-service-architecture.md) — fleet management, OTA, field service.

## Open questions

- **What is in the 20% that fails first pass?** Rework rate and scrap rate are the economics.
- **Actuator SKU count (10+) against 9,000 units** — how many actuators per robot? 9,000 actuators over 350 robots is ~26/robot, which is a plausible DOF-adjacent figure and the closest thing to a DOF disclosure Figure has published.
- **How many Figure 03 units are outside Figure's own buildings?** Never stated.
- **Is the stereo model learned or classical?** "Our stereo model" is all Figure says.

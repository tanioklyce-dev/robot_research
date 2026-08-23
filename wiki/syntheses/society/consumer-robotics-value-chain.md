---
title: Who benefits from consumer robotics in 2026–2027 (other than NVIDIA)
type: synthesis
created: 2026-08-17
updated: 2026-08-23
tags: [economics-of-ml, consumer-robotics, value-chain, actuators, edge-compute, business-models, market-analysis, synthesis]
---

# Who benefits from consumer robotics in 2026–2027 (other than NVIDIA)

A value-chain reading of the consumer-robot wave, built from the component costs, BOMs and business models this wiki already documents.

> [!warning] Read the epistemic status before the conclusions
> **This wiki holds no market data.** No revenue figures, no unit forecasts, no market sizing, no supply-chain sourcing, no financials for any private company here. Everything below is **inferred from the technology stack and published BOMs**, which is a legitimate but limited basis: it can tell you *where cost and dependency sit in the stack*, and therefore who is structurally positioned to capture value. It cannot tell you how much, or whether they will. Claims are grouped by evidence strength, and the groups are not decorative — the weakest tier is also the highest-leverage one.

## First: the premise needs adjusting

**The consumer "launch" documented in this wiki is mostly announcement, not shipment.**

| Product | Status in this wiki |
|---|---|
| **[NORI A3](../../entities/nori-a3.md) ($1,688)** | **The first exception.** Complete published price, no deposit, US assembly, **first unit shipped and >$300 K in sales within 6 weeks** ([YC profile](../../sources/nori-robotics-yc-profile.md)). Onboard compute is a **[Pi 5](../../entities/raspberry-pi-5.md) 4 GB** — disclosed on the YC page, never on the storefront ([product site](../../sources/nori-robotics-site.md)) |
| [Zeroth M1](../../entities/zeroth-m1.md) ($2,499) | Pre-order on a visibly unfinished storefront — placeholder meta description, `InStock` under a "Reserve Now" button, 404s on every company page ([product page](../../sources/zeroth-m1-product-page.md)) |
| [Sourccey](../../entities/sourccey.md) | **No published price**, store not live ([Vulcan Robotics](../../entities/vulcan-robotics.md)) |
| [Fauna Sprout](../../entities/fauna-robotics.md) | Creator Edition, developer-tier |
| [Reachy 2](../../entities/reachy.md) | ~$50k — research tier, not consumer |
| [K-Scale Labs](../../entities/k-scale-labs.md) | **Shut down late 2025** |

> [!note] Nori partially falsifies the premise above (added 2026-08-23)
> This page was written when nothing in the tier had a price *and* a shipment. Nori has both, at the **lowest price of any of them**, which moves the "installed base" clock off zero. It does not move it far — ~178 units at list, self-reported — but the argument should no longer be stated as "announcement, not shipment" without qualification.
>
> It also sharpens **Tier 2** (whoever serves the model). Nori's own thesis is that the robot is a **data-collection instrument** for training generalist policies, and its 4 GB Pi 5 means inference cannot run onboard. So the unit economics of every A3 sold include *someone* serving a model, on the owner's laptop today and plausibly in a datacentre later. That is Tier 2 exposure created by a Tier 1 sale — and it is retention-dependent, which is the split this page ends on.

That changes the answer materially. Value accruing at the **order and build** stage is happening now and is well-evidenced. Value accruing to an **installed base** — services, subscriptions, data — is a forecast resting on shipments that have not yet been demonstrated. Anyone reasoning about this should keep the two clocks separate.

---

## Tier 1 — Best evidenced: actuator vendors

**The single strongest number in the wiki on this question:** the [UME](../../entities/ume.md) exoskeleton's BOM is **86% quasi-direct-drive actuators** out of $1,900 ([UME paper](../../sources/ume-paper.md)).

Actuators are the cost that **scales with the product** in a way silicon does not. A robot needs one compute module regardless of complexity; it needs **one actuator per degree of freedom**. The [Zeroth M1](../../entities/zeroth-m1.md)'s advertised **20 DoF** is, from a supplier's perspective, a 20-actuator order per unit.

[FeeTech](../../entities/feetech.md) is the specific beneficiary in the affordable tier, and the wiki documents why:

- **~3× cheaper than [Dynamixel](../../entities/dynamixel.md)** at otherwise-comparable specs.
- That gap sets the platform price: [SO-ARM101](../../entities/so-arm101.md) at **€225 single / €550 bimanual** against **~€670** for the Dynamixel-based Koch-v1.1 ([LeRobot ICLR 2026 paper](../../sources/lerobot-iclr-2026-paper.md), Table 1a).
- Consequence: **SO-10X drives 50%+ of all community-contributed LeRobotDatasets** as of Sep 2025 — affordability compounding into ecosystem position.
- FeeTech appears in [XLeRobot](../../entities/xlerobot.md), [LeKiwi](../../entities/lekiwi.md), [Sourccey](../../entities/sourccey.md) (12 servos on one 1 Mbaud bus), and even [Stretch 4](../../entities/stretch.md)'s 24 V RS485 tool bus — i.e. across the community, commercial and research tiers simultaneously.

**Why this is the safest claim:** it does not depend on any product succeeding. Actuators are consumed by *building* robots, so the beneficiary is paid on the order-stage clock, which is the clock that is actually running.

> [!note] The counter-consideration
> FeeTech's position rests on being cheap, and cheap component positions are the easiest to displace. The wiki records a real technical liability — **"limited backdrivability due to high resistance under load"** ([Sourccey specs](../../sources/vulcan-robotics-sourccey-site.md)) — which matters for teleop feel and contact safety. A consumer wave that runs into contact-safety requirements could route around this tier rather than through it.

---

## Tier 2 — Highest leverage, thinnest evidence: whoever serves the model

**The consumer price point cannot carry the compute**, and the wiki documents this three independent ways:

1. **[Zeroth M1](../../entities/zeroth-m1.md)** publishes **no compute specification of any kind** — no SoC, no on-device/cloud split. Secondary CES coverage says it runs **Google Gemini**; no Zeroth page mentions Gemini, cloud, or connectivity ([product page](../../sources/zeroth-m1-product-page.md)).
2. **[Vulcan Robotics](../../entities/vulcan-robotics.md)** sells hardware **plus rented compute** — *"rented compute is planned for users who need stronger training or inference."* The wiki's entity page reads this as "a candid concession that the robot's advertised AI does not run on the robot, and turns that into a recurring-revenue surface."
3. **[Sourccey](../../entities/sourccey.md)** ships a **0.9 B [X-VLA](../../entities/x-vla.md) policy advertised beside a [Raspberry Pi 5](../../entities/raspberry-pi-5.md) that cannot run it** — reconciled only by that rental plan.

If the pattern holds, the consumer robot is a **subscription-acquisition device**, and durable revenue accrues to **model-serving providers on a per-robot-per-day basis** rather than to anyone at point of sale. That is a fundamentally different business from selling robots, with different margins, different defensibility, and a different winner.

> [!warning] This is one confirmed business model, one secondary report, and one inference
> It is the claim in this page most worth falsifying before anyone acts on it. **The decisive test is cheap**: establish what actually runs the M1's perception and dialogue. If inference is on-device, this tier collapses to a one-time silicon sale. If it is a network round-trip, then "fall detection" in a house with poor Wi-Fi is a materially different product — see the open question on [the M1 source page](../../sources/zeroth-m1-product-page.md).

---

## Tier 3 — Solid, but narrower than it looks

### Non-NVIDIA edge silicon

[Hailo](../../entities/hailo.md) (Hailo-8/8L vision, Hailo-10H generative) is the wiki's documented non-CUDA onboard option, and [Raspberry Pi 5](../../entities/raspberry-pi-5.md) is the host in [XLeRobot](../../entities/xlerobot.md), [LeKiwi](../../entities/lekiwi.md), Grievous and [Sourccey](../../entities/sourccey.md).

**Hedge it properly:** the wiki's own compute analysis still lands on Jetson for anything running a real VLA ([Hailo vs Jetson](../platforms/hailo-npu-vs-jetson-xlerobot.md), [onboard-compute comparison](../platforms/jetson-onboard-compute-xlerobot.md)). Hailo benefits at the **vision tier, not the policy tier**. If consumer robots stay in the sensing-and-alerting band the [M1](../../entities/zeroth-m1.md) actually occupies, that is a large market. If they move to manipulation, it is not their tier.

### Carrier boards and integration

[Seeed Studio](../../entities/seeed-studio.md) sells the reComputer carrier line, distributes [LeKiwi](../../entities/lekiwi.md), and co-organizes the ecosystem's hackathons.

**The 2026-08-17 Jetson sweep sharpened why this tier captures margin.** Seeed's own flash guide warns *"do not enable MAXN SUPER mode — the cooling capacity of the reComputer J401 carrier board is insufficient to support it"* ([Seeed flash guide](../../sources/seeed-j401-flash-jetpack.md)), while the Super J4012 is marketed at 157 TOPS Super MAXN. **That gap between "module" and "product" — thermals, carriers, connectors, BSP images — is exactly what the integration tier is paid to close**, and it does not shrink as silicon improves.

### Power and energy

The [XLeRobot](../../entities/xlerobot.md) BOM names a specific **Anker C300 at $159.99–$199.99**, and the wiki has a dedicated comparison page ([Anker power stations](../platforms/anker-portable-power-stations.md)). The M1's **~2 hour endurance** makes battery, dock and charge cycle a recurring design constraint rather than a one-time part — and [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) shows power topology is a first-order engineering problem at this price point, not an afterthought.

### Sensors

[Orbbec](../../entities/orbbec.md) (Gemini2 in the nvblox recipe), plus Hesai and Luxonis in [Stretch 4](../../entities/stretch.md). The [M1](../../entities/zeroth-m1.md) carries **LDS LIDAR + iTOF + camera + 3-mic array in a $2,499 device**, which is itself the evidence of how far this stack has commoditized — and commoditization means volume without margin.

---

## Where the obvious answer is probably wrong

### Hugging Face / LeRobot

[LeRobot](../../entities/lerobot.md) ([Hugging Face](../../entities/hugging-face.md)) is unambiguously the software substrate — it is the default in every affordable platform here, and [SO-10X](../../entities/so-arm101.md) drives half of all community dataset contributions.

But the wiki documents **mindshare, not monetization**. Open-source substrate position does not automatically convert into revenue from a consumer wave, and nothing in this wiki shows a mechanism by which it would. Naming LeRobot as a beneficiary is the *easy* answer and it needs an argument nobody here has made.

### The research-grade platforms

**A cheap consumer tier does not obviously validate the expensive one.** [Stretch](../../entities/stretch.md) is **$29,950** against the [M1](../../entities/zeroth-m1.md)'s **$2,499** for a device in a completely different capability band — the M1 publishes no payload, no reach, and no manipulation capability at all, which is why this wiki files it under **social/monitoring** rather than mobile manipulation ([assistive robotics](../../concepts/robotics/assistive-robotics.md)).

If buyers cannot distinguish those bands — and there is no reason to assume they can — the cheap tier makes the research tier look **overpriced rather than validated**.

---

## The split that matters most

The capability gap is documented and large: **RLBench 89.4% in controlled simulation vs [BEHAVIOR-1K](../../entities/behavior-benchmark.md) 12.4% full task success on realistic household tasks** ([Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md)), whose own verdict is that *"reliably executing household tasks in realistic environments is still beyond current capabilities."*

Consumer launches are therefore running **well ahead of demonstrated capability**. That splits the beneficiaries onto two different clocks:

| | Paid on | Exposure |
|---|---|---|
| **Component suppliers** — actuators, sensors, carriers, batteries, silicon | **Orders**, which are happening now | Low. Paid whether or not the product retains users |
| **Service layers** — model serving, compute rental, subscriptions | **Retention**, which requires shipments and satisfied users | High. Fully exposed to a return wave |

Nothing in this wiki gives grounds to rule out a return wave. The [M1](../../entities/zeroth-m1.md) markets fall detection for elder safety with **no accuracy figure, no trial, and no deployment evidence**, into a demand context ([aging in place](../../concepts/robotics/aging-in-place.md)) where the reliability bar is set by safety rather than throughput.

**Net:** the safest position in a consumer robotics wave is **selling parts to everyone building them**. The most valuable position — if the shipments materialize — is **serving the model the robot cannot run**. Those are not the same companies, and only the first is presently supported by evidence in this wiki.

---

## What would change this analysis

- **Establishing what actually runs the [M1](../../entities/zeroth-m1.md)'s inference.** Single highest-value fact; decides whether Tier 2 exists.
- **Any real shipment volume figure** for any consumer robot here. There is currently none.
- **A published consumer-robot BOM.** The wiki has BOMs for open platforms ([XLeRobot](../../entities/xlerobot.md) ~$660, [UME](../../entities/ume.md) $1,900) but **none for a commercial consumer product** — [Sourccey](../../entities/sourccey.md) publishes no BOM and no price. A single teardown would move most of this page from inference to evidence.
- **Evidence of a contact-safety or certification requirement** entering the consumer tier ([ISO 13482](../../concepts/robotics/robot-safety-standards.md)) — that would create a beneficiary class (test houses, certification, insurance) that currently has no wiki evidence at all.

## Related

- [Consumer / affordable platform comparisons](../platforms/sourccey-vs-xlerobot.md)
- [Assistive robotics](../../concepts/robotics/assistive-robotics.md) · [Aging in place](../../concepts/robotics/aging-in-place.md)
- [Collectivist AI](../../concepts/economics/collectivist-ai.md) — the wiki's other economics-of-ML thread; no robotics content, but the same question of who captures value from a shared artifact
- [Three critiques of the LLM-as-intelligence North Star](critiques-of-the-intelligence-north-star.md)

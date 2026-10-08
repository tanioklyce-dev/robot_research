---
title: Flourish 1
type: entity
subtype: robot
created: 2026-10-07
updated: 2026-10-07
sources: 5
tags: [flourish, flourish-1, home-robot, mobile-manipulator, bimanual, consumer-robotics, raspberry-pi, cloud-inference, subscription, phone-teleop, end-user-programming, pre-order]
---

**Flourish 1** is a **wheeled, two-armed home robot** from [Flourish Robots](flourish-robots.md). It sells as a **limited run of 50 numbered units at $3,555**, reserved with a **$1,555 refundable deposit**, shipping **December 2026** ([site](../sources/flourish-robots-website.md)). The owner teaches it a chore by laying out task steps in a phone app and then **driving it through the task from the phone for ~30 minutes**. A per-home, per-task model is fine-tuned in the cloud and is ready about an hour later. Launch press calls it a humanoid. It is a mobile manipulator in the [XLeRobot](xlerobot.md) / [Sourccey](sourccey.md) / [NORI A3](nori-a3.md) class.

## Specs

| | | Source |
|---|---|---|
| **Price** | **$3,555**; $1,555 deposit, refundable until shipping | [site](../sources/flourish-robots-website.md) |
| **Run** | **50 units**, numbered 01–50, built by Flourish in Paris | [site](../sources/flourish-robots-website.md), [Clubic](../sources/clubic-flourish-1.md) |
| **Ships** | December 2026, *"a good-faith estimate… not a guaranteed date"* | [Terms](../sources/flourish-robots-website.md) |
| **Height / mass** | 3'7" (≈109 cm) / 44 lb (≈20 kg) | [site](../sources/flourish-robots-website.md) |
| **Reach** | floor to 35" (≈89 cm), via a vertically moving torso | [site](../sources/flourish-robots-website.md), [CNET](../sources/cnet-flourish-1.md) |
| **Payload** | **3.3 lb / 1.5 kg**; per arm or total is **disputed** | [site](../sources/flourish-robots-website.md) vs [Robot Report](../sources/therobotreport-flourish-one.md) |
| **Runtime** | 12 h | [site](../sources/flourish-robots-website.md) |
| **Base** | six wheels | [Robot Report](../sources/therobotreport-flourish-one.md) |
| **Arms / hands** | two arms, two-finger grippers; **DOF not published** | [Robot Report](../sources/therobotreport-flourish-one.md) |
| **Sensors** | a camera on each wrist; small floor-level lidar on the base; "depth" data per the Privacy Policy | [Robot Report](../sources/therobotreport-flourish-one.md), [Privacy](../sources/flourish-robots-website.md) |
| **Onboard compute** | **"a Raspberry Pi"**, model unstated | [Robot Report](../sources/therobotreport-flourish-one.md) |
| **Off-board compute** | cloud GPUs for training and live decisions; **6 months included, then $50/month**, or the owner's GPU | [site](../sources/flourish-robots-website.md) |
| **Warranty / returns** | **none** (US); EU/UK statutory rights preserved | [Terms](../sources/flourish-robots-website.md) |

**Stated limits:** *"No water · Nothing over 1.5 kg · Nothing breakable · No stairs · Not perfect."* Also nothing sharp. It is not a childcare, eldercare, medical or security device ([site, Terms](../sources/flourish-robots-website.md)).

## How it is taught
1. **Task graph.** In the app, drag and drop steps such as *go to the entrance → pick up a shoe → put it in the cabinet → come back*. This takes about 5 minutes and needs no code ([site](../sources/flourish-robots-website.md)). The SDK exposes these steps as **nodes**, so the graph is the program and the learned skills are its leaves.
2. **Demonstrations.** Drive the robot through the task from your phone *"a few times, from different spots in the room,"* for about 30 minutes. [The Robot Report](../sources/therobotreport-flourish-one.md) says the arms **mirror the phone's IMU motion**. [CNET](../sources/cnet-flourish-1.md) describes the phone as a proxy object you move through the task.
3. **Fine-tune.** Flourish fine-tunes a pretrained model on those recordings, per task and per home, and notifies you about an hour later.

In this wiki's terms that is [end-user robot programming](../concepts/robotics/end-user-robot-programming.md) for structure plus [imitation learning](../concepts/learning/imitation-learning.md) for the skills. It resembles a hosted version of the community ACT-style workflow (tens of demos, then a per-task fine-tune). The model family is **not disclosed**, so that resemblance is a reading, not a fact.

> [!note] Why "from different spots in the room" is the important instruction
> Starting demonstrations from varied positions is how a small per-task dataset buys **coverage of initial states**. Without it a behaviour-cloned policy fails as soon as the robot starts somewhere new. It is the cheapest generalization lever available to a 30-minute dataset, and the founder's *"the shoes don't need to be in exactly the same place every day"* ([CNET](../sources/cnet-flourish-1.md)) depends on it. Object-position variation needs the same treatment, and the site does not ask for it.

## Reading the spec sheet

**Network dependence is part of the design.** The Privacy Policy says live camera and sensor data goes to Flourish's servers *"so the system can decide what to do next"*. The site's 10-02 claim that it *"runs on-device"* was **withdrawn by 10-07** ([edition history](../sources/flourish-robots-website.md#edition-history)). Without a subscription or an owner GPU, the founder says the robot still moves, obeys voice and **replays recorded gestures** ([Clubic](../sources/clubic-flourish-1.md)). That is the fixed-coordinate behaviour the CEO told CNET the product is *not*. So the learned, generalizing part of the product is a **$50/month service**, and the hardware is a thin client. This matches [NORI A3](nori-a3.md) (a Pi 5 that thinks on your laptop) and [Sourccey](sourccey.md) (a Pi 5 advertised beside a VLA it cannot run). Flourish is the first of the three to **put a price on** the off-board half.

**Reliability is stated without a protocol.** *"A year ago a taught task worked 60% of the time. Today it's 80%"* ([site](../sources/flourish-robots-website.md)). Per [Clubic](../sources/clubic-flourish-1.md) the 80% is for *simple* tasks such as shoes and plants, and no figure exists for harder ones. There is no N, no task list and no definition of success. By the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)'s standard it is an **unknown-N** claim. It is still more than [Figure 03](figure-03.md) or [1X NEO](1x-neo.md) published at their own launches. The "year ago" baseline predates the company's January 2026 founding ([Robot Report](../sources/therobotreport-flourish-one.md)).

**The candid limits are the credible part.** *"It works around your kids. It doesn't look after them."* The robot takes ~5 minutes to put shoes away ([Clubic](../sources/clubic-flourish-1.md)), and the Terms admit it *"will sometimes fail at tasks it performed correctly the day before."* Nothing else in this wiki's consumer tier writes its failure modes into the sale contract.

**Safety design is stated but not certified.** The CEO says it stops when a person or animal enters its working area, and argues that a wheeled base with low payload and low power limits the energy involved ([CNET](../sources/cnet-flourish-1.md)). No standard is named. An in-home mobile manipulator's natural certification path is ISO 13482 ([robot safety standards](../concepts/robotics/robot-safety-standards.md)). The Terms' clause on **cancelling orders where local certification is required** suggests none has been obtained.

## Comparison

| | Flourish 1 | [NORI A3](nori-a3.md) | [1X NEO](1x-neo.md) | Weave Isaac 1¹ |
|---|---|---|---|---|
| Price | **$3,555** + $50/mo after 6 mo | $1,688 | ~$20k or $499/mo | $7,999 or $449/mo |
| Form | wheeled, 2 arms, lift | wheeled, 2 × 7+1-DOF, lift | biped humanoid | wheeled |
| Payload | 1.5 kg (disputed) | 1.5 kg / arm | 25 kg carry | — |
| Compute | Raspberry Pi + cloud | Pi 5 4 GB + laptop | onboard (Redwood AI) | — |
| Teaching | phone teleop, 30 min | laptop app | 1X staff "Expert Mode" teleop | — |
| Remote human operator | **none, says CEO** | — | yes (Expert Mode) | yes, per CNET |
| Published success rate | **80%** (unknown N) | none | none | — |
| Status | 50-unit pre-order | shipping | pre-order, none delivered as of June | pre-order |

¹ CNET's figures. No Weave source is ingested.

## Open questions
- Is the robot safe and useful with the network down? Specifically, does the stop-on-intrusion behaviour run onboard?
- One phone, two arms, a base and a lift: what is the teleop mapping?
- What is a store "task": a graph, a checkpoint, or both? A checkpoint fine-tuned in one home would not transfer.
- Arm DOF, actuators, cameras and the Pi model are all unpublished. These are the specs any buyer with an SDK would need.

## Related
- [Flourish Robots](flourish-robots.md): the company.
- [NORI A3](nori-a3.md) · [Sourccey](sourccey.md) · [XLeRobot](xlerobot.md) · [Zeroth M1](zeroth-m1.md): the affordable home-manipulator tier.
- [1X NEO](1x-neo.md): the humanoid comparator.
- [Consumer robotics value chain](../syntheses/society/consumer-robotics-value-chain.md): the Tier 2 model-serving thesis, which Flourish prices explicitly.
- [Raspberry Pi 5](raspberry-pi-5.md)

## Mentioned in
- [Flourish Robots — product site, Terms, Privacy](../sources/flourish-robots-website.md)
- [The Robot Report — Meet Flourish One](../sources/therobotreport-flourish-one.md)
- [CNET — $3,555 humanoid learns chores in 30 minutes](../sources/cnet-flourish-1.md)
- [Clubic — un nouveau robot domestique français](../sources/clubic-flourish-1.md)
- [Flourish 1 launch press release](../sources/flourish-1-launch-press-release.md)

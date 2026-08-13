---
title: "Universal Manipulation Exoskeleton (UME) — project page (Liang, Xu et al., 2026)"
type: source
url: https://ume-exo.github.io/
author: "Litian Liang*, James (Jingxi) Xu*, Xinda Qi, Yujun Cai, Houzhu Ding, Luqi Wang, Zhixin Sun, Jyh-Herng Chow, Ming Yang, Mark Cutkosky"
affiliations: Ant Group; Stanford University
published: 2026 (arXiv 2606.14218)
ingested: 2026-08-13
tags: [ume, exoskeleton, teleoperation, force-torque, haptic-feedback, compliant-control, whole-body, data-collection, umi, openarm, low-cost, mobile-manipulation, primary-source]
---

## Summary

**UME (Universal Manipulation Exoskeleton)** — an upper-limb exoskeleton from **Ant Group + Stanford** that provides **real-time haptic torque feedback** to a human teleoperator while **recording whole-arm configurations and joint torque signals**. **$1,900** for the whole system. Its thesis is stated in one sentence that lands squarely on a gap this wiki has been circling all week:

> *"The majority of existing data collection pipelines still lack the ability to capture force and torque data for learning active compliant policies."*

That is the exact limitation recorded on [Sourccey](../entities/sourccey.md) (dataset is "positional only"), [XLeRobot](../entities/xlerobot.md) and [SO-ARM101](../entities/so-arm101.md) (no force sensing beyond servo current), [DimOS](../entities/dimos.md)'s `dataprep` (`color_image` + `coordinator_joint_state`), and the reason [OpenFT](../entities/openft-sensor.md) was filed. **UME is the first ingested source that solves it end-to-end rather than naming it.**

The demonstration that makes the capability legible: a **blindfolded operator unsheathing a metal sword** — a kinematically constrained task — *"relying purely on real-time haptic torque feedback."*

## Key claims

### The device

- **Upper-limb exoskeleton**, low-cost, lightweight, portable. **$1,900 total system cost** (breakdown in the paper).
- **Transparent real-time torque feedback** to the operator, plus **recording of whole-arm configuration and joint torques**.
- **Embedded IMU** → works for **mobile** manipulation teleoperation, not just a fixed rig.
- **Universal retargeting algorithm** drives multiple robots: **7-DoF OpenArm**, **7-DoF [Franka](../entities/franka-panda.md)**, **6-DoF [X-ARM](../entities/xarm-7.md)**.
- Gravity compensation and a documented range-of-motion study.

### The evaluation platform

A separately-built **$9,533 bimanual mobile manipulator**, itemized on the page:

| Component | Detail | Cost |
|---|---|---|
| **OpenArm 1.0** bimanual (WowRobo) | Damiao DM-J8009P / J4340P / J4340 / J4310 actuators, machined aluminium | $5,200 |
| **Hexfellow PCW-25** powered caster | *"improved compliance and precise odometry, while remaining fully holonomic"* | $900 |
| DJI Power 1000 | untethered operation | — |
| Jieruiweitong 2K HDR fisheye ×3 | head + wrists, **210° FoV**, low latency, HDR | $37.50 ea |

### The autonomous policies — and the demonstration counts

All policies trained **solely on UME-collected data**, run on that in-house dual-arm mobile manipulator:

| Task | Demos | Why it is hard |
|---|---:|---|
| **Visually occluded box pushing** | **26** | occluded; highly force-mediated |
| **Force-mediated box flipping** | **40** | push against a fixed surface to flip upright |
| **Space-constrained GPU picking** | **42** | reach between two desktops; whole-body |
| **Whole-body fridge drink retrieval** | **157** | long-horizon; mobile; two-gripper support |

Ablations named on the page: **Comparison with UMI** (on three of the four tasks) and **Comparison with No-torque** (on two).

## Analysis

> [!note] The demonstration counts are the number to take away
> **26 to 157 demos per task**, for contact-rich, occluded, whole-body, long-horizon behaviours. Set that against this wiki's other data points: [X-VLA](../entities/x-vla.md)'s cloth-folding dataset needed **1,200 episodes ≈ 50–60 operator-hours** and a DAgger loop; the standard [LeRobot](../entities/lerobot.md) recipe is ~50 per task for *tabletop pick-and-place*.
>
> UME is getting harder tasks at comparable or lower demo counts. If the **No-torque** ablation supports the causal reading — and that is the whole point of running it — then **force feedback is buying data efficiency, not just operator comfort**. That would be a strong claim, and it is exactly the claim the [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md)'s "~50 demos, 2–3 hours" budget is silently betting against.

> [!note] It is the direct rebuttal to UMI, and it says so
> **[UMI](../entities/umi.md)** (Universal Manipulation Interface, Chi/Song et al.) is the wiki's reference handheld-gripper data-collection device — cheap, portable, no robot in the loop. UME runs head-to-head against it on **box pushing, GPU picking, and fridge retrieval**, i.e. exactly the occluded and force-mediated cases where a gripper-mounted camera with no force channel should struggle.
>
> The two are the same *idea* — instrument the human, not the robot — with different bets about what the instrument must capture. **UMI bets on visual context and portability; UME bets on torque.** That the acknowledgements thank Stanford's **REAL Lab (Shuran Song)**, UMI's own lab, makes this a conversation rather than a drive-by.

> [!warning] What is not on this page
> **No success-rate numbers, no trial counts, no tables.** The page shows videos labelled "Comparison with UMI (2x)" and "Comparison with No-torque (1x)" without publishing the outcomes. Per this wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline, **nothing here is a measurement yet** — the demo counts and the cost breakdown are the hard facts. The arXiv paper (**2606.14218**) is where the ablations must be read before any of this is quoted as a result.

> [!note] Cost places it in a tier this wiki cares about
> **$1,900 exoskeleton + $9,533 robot ≈ $11.4 K** for a bimanual, holonomic, force-instrumented mobile manipulator. That is above the [XLeRobot](../entities/xlerobot.md) ($660) / [Sourccey](../entities/sourccey.md) tier and roughly **half a [Stretch](../entities/stretch.md)**, well under a [Yuri](../entities/yuri.md) or [Reachy 2](../entities/reachy.md). The **Hexfellow PCW-25 powered caster** is the interesting line item — *"improved compliance and precise odometry, while remaining fully holonomic"* — which is precisely the combination [Sourccey](../entities/sourccey.md) gave up with open-loop mecanum wheels and that [XLeRobot](../entities/xlerobot.md)'s differential base cannot offer.

> [!note] OpenArm, again
> The platform uses **"OpenArm 1.0 bimanual made by WowRobo."** This wiki already tracks **OpenArm+** as the open-hardware arm behind [Sensori Robotics](../entities/sensori-robotics.md)'s [Yuri](../entities/yuri.md) (docs.openarm.dev). Whether WowRobo's OpenArm 1.0 and Sensori's OpenArm+ are the same design lineage is **not established here** — but two independent research platforms sourcing "OpenArm" arms suggests an open-hardware arm standard forming above the [SO-ARM101](../entities/so-arm101.md) tier, which would be worth confirming.

## Entities mentioned

- [UME](../entities/ume.md) — the subject of this source
- [UMI](../entities/umi.md) — the comparison baseline · [Franka Panda](../entities/franka-panda.md) · [xArm 7](../entities/xarm-7.md)
- [Sensori Robotics](../entities/sensori-robotics.md) / [Yuri](../entities/yuri.md) — the wiki's other OpenArm platform
- [Sourccey](../entities/sourccey.md), [XLeRobot](../entities/xlerobot.md), [SO-ARM101](../entities/so-arm101.md), [OpenFT sensor](../entities/openft-sensor.md) — the position-only tier this addresses

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) · [Whole-body control](../concepts/robotics/whole-body-control.md) · [Collaborative robots](../concepts/robotics/collaborative-robots.md)
- [Optimal control](../concepts/robotics/optimal-control.md) — compliance and force-mediated behaviour

## Open questions

- **The paper is not ingested** (arXiv 2606.14218), and it holds everything that matters: the UMI and No-torque **ablation results**, the cost breakdown, the retargeting algorithm, and the user study.
- **Does torque feedback improve the policy, the operator, or both?** The No-torque ablation is the experiment; the outcome is unpublished on this page. This is the single most valuable number in the work for this wiki.
- **Is torque recorded into the training data, or only fed back to the human?** The abstract says both are recorded — but whether the learned policies *consume* torque as an input channel, or merely benefit from better demonstrations, is a completely different claim and is not resolved here.
- **Can any of this reach the $1k tier?** UME is $1,900 against a $660 [XLeRobot](../entities/xlerobot.md); [OpenFT](../entities/openft-sensor.md) is the cheap-but-unmaintained alternative. Nothing bridges them yet.
- **Is WowRobo's OpenArm 1.0 the same lineage as Sensori's OpenArm+?** Unresolved, and it bears on whether an open arm standard is actually consolidating.

---
title: UME (Universal Manipulation Exoskeleton)
type: entity
subtype: product
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [ume, exoskeleton, teleoperation, force-torque, haptic-feedback, compliant-control, data-collection, umi, ant-group, stanford, low-cost]
---

**UME (Universal Manipulation Exoskeleton)** — a **$1,900** upper-limb exoskeleton from **Ant Group + Stanford** (Liang, Xu et al., arXiv 2606.14218) that gives a teleoperator **real-time haptic torque feedback** while **recording whole-arm configuration and joint torques**. Primary source: [project page](../sources/ume-project-page.md).

Its thesis is the gap this wiki kept hitting: *"the majority of existing data collection pipelines still lack the ability to capture force and torque data for learning active compliant policies."*

## Why it matters here

**It is the first ingested source that closes the position-only recording gap rather than naming it.** The wiki records that limitation on [Sourccey](sourccey.md) ("positional only"), [XLeRobot](xlerobot.md) / [SO-ARM101](so-arm101.md) (servo current only), and [DimOS](dimos.md)'s dataset export — and filed [OpenFT](openft-sensor.md) as the cheap, unmaintained, unbenchmarked route out. UME is the researched route.

Legibility demo: a **blindfolded operator unsheathing a metal sword**, a kinematically constrained task, *"relying purely on real-time haptic torque feedback."*

## Specs

- **$1,900** total system. Low-cost, lightweight, portable.
- **Transparent real-time torque feedback**; records whole-arm configuration + joint torques.
- **Embedded IMU** → mobile-manipulation teleoperation, not a fixed rig.
- **Universal retargeting** to 7-DoF OpenArm, 7-DoF [Franka](franka-panda.md), 6-DoF [X-ARM](xarm-7.md).
- Gravity compensation; documented range-of-motion study.

## The evaluation robot ($9,533)

| Component | Cost |
|---|---|
| **OpenArm 1.0** bimanual (WowRobo), Damiao actuators, machined aluminium | $5,200 |
| **Hexfellow PCW-25** powered caster — *"improved compliance and precise odometry, while remaining fully holonomic"* | $900 |
| DJI Power 1000 (untethered) · 3× 2K HDR fisheye, 210° FoV | — / $37.50 ea |

## Demonstration counts — the number to take away

All policies trained **solely on UME data**:

| Task | Demos |
|---|---:|
| Visually occluded box pushing | **26** |
| Force-mediated box flipping | **40** |
| Space-constrained GPU picking | **42** |
| Whole-body fridge drink retrieval (long-horizon, mobile) | **157** |

> [!note] Contact-rich tasks at demo counts below tabletop pick-and-place
> Compare: [X-VLA](x-vla.md)'s cloth folding needed **1,200 episodes ≈ 50–60 operator-hours**; the standard [LeRobot](lerobot.md) recipe is ~50 per task for *tabletop pick-and-place*. UME reports harder tasks at comparable or lower counts. If the **No-torque** ablation supports the causal reading, **force feedback is buying data efficiency, not just operator comfort** — which is the bet the [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md)'s "~50 demos, 2–3 hours" budget is silently made against.

> [!warning] No success rates published on the project page
> Videos are labelled *"Comparison with UMI"* and *"Comparison with No-torque"* — **the outcomes are not shown**. Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), nothing here is a measurement yet. The demo counts and costs are the hard facts; the ablations must be read from arXiv **2606.14218** before any of it is quoted as a result.

## Position vs UMI

**[UMI](umi.md)** and UME are the same idea — *instrument the human, not the robot* — with different bets about what the instrument must capture. **UMI bets on visual context and portability; UME bets on torque.** UME runs head-to-head against UMI on box pushing, GPU picking, and fridge retrieval — precisely the occluded and force-mediated cases where a gripper-cam with no force channel should struggle. The acknowledgements thank Stanford's REAL Lab (Shuran Song), UMI's own lab, which makes it a conversation rather than a drive-by.

## Cost tier

**≈$11.4 K** for the exoskeleton plus a bimanual holonomic force-instrumented mobile manipulator — above [XLeRobot](xlerobot.md) ($660) / [Sourccey](sourccey.md), about **half a [Stretch](stretch.md)**, well under [Yuri](yuri.md) or [Reachy 2](reachy.md). The **powered caster** delivering compliance *and* precise odometry *and* holonomy is the line item worth noting: exactly the combination [Sourccey](sourccey.md) surrendered with open-loop mecanum and [XLeRobot](xlerobot.md)'s differential base cannot provide.

## Related

- [UMI](umi.md) — the baseline it argues against
- [OpenFT sensor](openft-sensor.md) — the DIY route to the same signal
- [Sourccey](sourccey.md), [XLeRobot](xlerobot.md), [SO-ARM101](so-arm101.md) — the position-only tier
- [Yuri](yuri.md) / [Sensori Robotics](sensori-robotics.md) — the wiki's other OpenArm platform, and the other rig shipping force-feedback teleop
- [Imitation learning](../concepts/learning/imitation-learning.md) · [Whole-body control](../concepts/robotics/whole-body-control.md)

## Open questions

- **Paper un-ingested** (arXiv 2606.14218) — it holds the UMI and No-torque ablation results, the cost breakdown, the retargeting algorithm, and the user study.
- **Do the learned policies consume torque as an input**, or only benefit from better demonstrations? Completely different claims; unresolved on the project page.
- **Nothing bridges $1,900 to the $660 tier.** [OpenFT](openft-sensor.md) is the only cheaper option and is unmaintained and unbenchmarked.
- **Is WowRobo's OpenArm 1.0 the same lineage as [Sensori](sensori-robotics.md)'s OpenArm+?** Two independent platforms sourcing "OpenArm" hints at a standard forming above the SO-ARM101 tier — unconfirmed.

## Mentioned in

- [UME project page](../sources/ume-project-page.md)

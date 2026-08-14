---
title: "Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback (Liang, Xu et al., Jun 2026)"
type: source
url: https://arxiv.org/abs/2606.14218
local_path: raw/2606.14218-ume.pdf
author: "Litian Liang*, Jingxi Xu*, Xinda Qi, Yujun Cai, Houzhu Ding, Luqi Wang, Zhixin Sun, Jyh-Herng Chow, Ming Yang, Mark Cutkosky"
affiliations: Ant Group; Stanford University
published: 2026-06-12
ingested: 2026-08-13
tags: [ume, exoskeleton, teleoperation, force-torque, haptic-feedback, compliant-control, whole-body, umi, act, quasi-direct-drive, damiao, ablation, primary-source]
---

## Summary

The paper behind the [UME project page](ume-project-page.md), and it carries everything that page withheld: **the No-torque and UMI ablation results, the bills of materials, and the throughput study.**

**UME** is a **$1,900** upper-limb exoskeleton that renders real-time haptic joint torque to the operator *and* records whole-arm configuration plus joint torques. Its argument is that both halves of the teleoperation literature are missing something: **ALOHA/GELLO-style leader arms don't expose joint torque** (so no compliant policies, and no force propagated back to the operator), while **UMI-style handheld grippers give the human implicit force feedback but record only end-effector pose** (so they rely on IK at inference and handle clutter badly, with a gripper-mounted camera that sees little global geometry).

Three capabilities, each mapped to a task designed to isolate it: **Cap1** real-time haptic torque feedback, **Cap2** universal whole-arm configuration capture, **Cap3** portability for mobile manipulation.

## The headline table — 20 trials per cell

| Task | No-torque | UMI | **UME** |
|---|---:|---:|---:|
| Box pushing (occluded, force-mediated) | 0.50 | 0.40 | **0.90** |
| **Box flipping (force-mediated)** | **0.00** | **0.00** | **0.85** |
| GPU picking (~5 mm clearance) | 0.75 | **0.00** | **0.95** |
| Fridge drink retrieval (long-horizon, mobile) | 0.90 | 0.00 | **0.95** |

**No-torque** = same dataset, torque dropped from the proprioception embedding. **UMI** = same dataset, trained on end-effector 6D pose only with UMI's input/output parameterization, plus a whole-body IK solver.

> [!warning] Applying this wiki's own audit: two of the four torque comparisons separate, two do not
> At **n = 20 per cell**, per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline, Fisher's exact test on UME vs **No-torque**:
>
> | Comparison | Result | p | Verdict |
> |---|---|---:|---|
> | Box flipping 17/20 vs 0/20 | +0.85 | <0.00001 | **separates** |
> | Box pushing 18/20 vs 10/20 | +0.40 | 0.014 | **separates** |
> | GPU picking 19/20 vs 15/20 | +0.20 | 0.18 | does **not** separate |
> | Fridge 19/20 vs 18/20 | +0.05 | 1.00 | does **not** separate |
>
> And UME vs **UMI**: box pushing p = 0.002, GPU picking p < 0.00001 — **both separate decisively**.
>
> So the defensible claims are: **torque is load-bearing on force-mediated tasks** (box flipping, box pushing), **whole-arm configuration is load-bearing in constrained space** (UMI's zeros), and **on the long-horizon mobile task torque buys essentially nothing** — No-torque reaches 0.90 against UME's 0.95. The paper reports that honestly rather than burying it.

### Box flipping is the cleanest result in the paper

Both baselines score **exactly zero**, and the mechanism is stated precisely: the task requires distinguishing **two states that are visually identical but demand opposite actions** — gripper in contact with insufficient pressing force (keep pushing) versus sufficient force established (begin the flip). *"Which can only be reliably distinguished through torque sensing."*

This is the strongest demonstration in the wiki that **torque is information vision cannot supply**, not merely a control convenience. Everything trained on pixels-plus-position is blind to that distinction by construction.

### The fridge stage-wise breakdown shows exactly where UMI dies

| Stage | No-torque | UMI | UME |
|---|---:|---:|---:|
| Turn around | 1.00 | 1.00 | 1.00 |
| Open fridge | 0.95 | 0.95 | 1.00 |
| **Take out drink** | 0.90 | **0.00** | 0.95 |
| Close fridge / transport / place | 0.90 | 0.00 | 0.95 |

**UMI goes 0.95 → 0.00 at a single stage.** It opens the fridge fine and then never once grasps and lifts the can out of the door holder — collisions from the wrist-mounted camera or the gripper itself. A clean isolation of Cap2: end-effector pose plus IK cannot express the whole-arm posture needed to reach around an obstacle.

## Data-collection throughput — the second, separable finding

Measured on box flipping, averaged over multiple users, reset time included:

**UME achieves a 3.3× improvement in demonstrations-per-minute over UME-without-torque-feedback, operating at 71% of unaided human speed.**

> [!note] Torque feedback pays twice, and the two payments are independent
> The ablation above shows torque in the *data* improves the *policy*. This shows torque in the *loop* improves the *operator* — 3.3× more demonstrations per minute on a force-mediated task. Those are different mechanisms and the paper measures them separately. For anyone budgeting a data-collection campaign, the throughput number may matter more: it compounds against every hour of teleoperation.

## Hardware — and where the money goes

**UME, $1,900 total** ("roughly the price of a MacBook"):

| Item | Cost |
|---|---|
| 8× **Damiao DM-J4340-2EC** (9 N·m) | $117 × 8 = $936 |
| 8× **Damiao DM-J4310-2EC** (3 N·m) | $88 × 8 = $704 |
| CAN-FD→USB adapter · DC supply · **Yahboom IMU ($9)** | $52 / $41 / $9 |
| 2020 extrusion, Bambu PLA, M3/M5 hardware, quick-detach belt | ~$150 |

**86% of the cost is actuators.** The enabling choice is stated explicitly: **quasi-direct-drive motors with substantially lower reduction ratios** (Damiao, Unitree) instead of the **multi-stage planetary gearboxes** in the Dynamixel actuators used by GELLO and similar. Low reduction is what makes the joints backdrivable enough for *transparent* feedback.

**Evaluation robot, $9,533**: WowRobo **OpenArm 1.0** bimanual ($5,200), 4× **Hexfellow PCW-25** powered casters ($900 ea — *"improved compliance and more accurate odometry due to its lower gear ratio and reduced backlash, while remaining fully holonomic"*), DJI Power 1000 ($386), 3× 2K 210° HDR fisheye ($37.50 ea).

**Policies are [ACT](../entities/act.md)** — ResNet18 backbone, 4 encoder / 7 decoder layers, hidden 512, batch 200, **40 k gradient steps on one RTX 4090 in 8 hours**.

## Analysis

> [!note] The demo counts and the training recipe are the transferable part
> 26 / 40 / 42 / 157 demonstrations, **[ACT](../entities/act.md)**, **one RTX 4090, eight hours**. That is not a frontier-lab recipe — it is within reach of anyone with the [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md)'s hardware, and it produces contact-rich whole-body behaviour. The gating resource is **the torque channel**, not compute or data volume.
>
> It also validates that plan's choice of ACT for the first policy, on harder tasks than the plan scopes.

> [!warning] A 12 kg exoskeleton, worn for up to two hours
> The limitations section is candid: PLA links make UME *"higher weight and lower payload compared to more expensive alternatives"* — **~12 kg**, comfortable *"for up to 2 hours"*, with CNC aluminium projected to reach ~8 kg. Link lengths are **fixed**, which the authors flag as an accessibility and ergonomics problem.
>
> Set against UMI's handheld gripper this is a real cost. **UME's data is better; UMI's data is easier to collect at scale and in the wild.** The 3.3× throughput result is measured against *UME without torque*, not against UMI — so the head-to-head throughput comparison that would settle the trade is **not run**.

> [!warning] Franka results are simulation-only
> *"Due to delays in Franka arm delivery, we only demonstrate Franka teleoperation in simulation"* (MuJoCo). Of the three retargeting targets, only **X-ARM** is demonstrated on real hardware for cross-embodiment teleoperation; OpenArm is the evaluation platform. The universality claim is therefore **two real embodiments and one simulated**.

> [!note] Where it sits against the wiki's compliance coverage
> The related-work section maps the alternatives cleanly: high-level position policy + **admittance/impedance** controller; learning the compliance parameters (**ACP** predicts stiffness alongside a diffusion policy); or **end-to-end torque policies** that map observations directly to torque commands, which *"requires a torque-controllable platform and places the full burden of stable, safe force control on the learned policy."* UME takes none of these — it feeds recorded torque in as an **observation modality** to an otherwise standard ACT policy. The cheapest possible intervention, which is part of why it transfers.

## Entities mentioned

- [UME](../entities/ume.md) — the subject · [UMI](../entities/umi.md) — the ablated baseline
- [ACT](../entities/act.md) — the policy architecture · [Franka Panda](../entities/franka-panda.md) · [xArm 7](../entities/xarm-7.md) · [MuJoCo](../entities/mujoco.md)
- [Sensori Robotics](../entities/sensori-robotics.md) / [Yuri](../entities/yuri.md) — the wiki's other OpenArm platform
- [Sourccey](../entities/sourccey.md), [XLeRobot](../entities/xlerobot.md), [SO-ARM101](../entities/so-arm101.md), [OpenFT sensor](../entities/openft-sensor.md) — the position-only tier
- [Dynamixel](../entities/dynamixel.md) — the high-reduction actuator lineage it argues against

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) · [Whole-body control](../concepts/robotics/whole-body-control.md) · [Optimal control](../concepts/robotics/optimal-control.md) · [Collaborative robots](../concepts/robotics/collaborative-robots.md)
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — n = 20 per cell

## Open questions

- **UME vs UMI on collection throughput is not measured.** The 3.3× is against torque-disabled UME. Given UME weighs 12 kg and UMI is handheld, this is the comparison that would decide which paradigm scales, and it is absent.
- **Does torque help on long-horizon mobile tasks at all?** Fridge retrieval is 0.95 vs 0.90 at n=20 — indistinguishable. Either the task is not force-mediated enough, or the benefit is real and n=20 cannot see it. A larger n on that task would settle it.
- **No cross-embodiment *policy* transfer.** Universal *teleoperation* across arms is shown; whether policies trained on UME data transfer across embodiments is untested.
- **Real Franka results** are promised once hardware arrives, with an expectation of *"similar or improved performance given Franka's more accurate joint torque sensing."*
- **Nothing bridges $1,900 to the $660 tier.** [OpenFT](../entities/openft-sensor.md) remains the only cheaper route to a torque signal and is unmaintained, unbenchmarked, and unlicensed.

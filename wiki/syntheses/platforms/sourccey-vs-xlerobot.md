---
title: Sourccey vs XLeRobot — two answers to the same $1k household manipulator
type: synthesis
created: 2026-08-13
updated: 2026-08-13
tags: [sourccey, xlerobot, lekiwi, platform-comparison, household-robot, lerobot, feetech, raspberry-pi-5, open-hardware, buying-decision]
---

[Sourccey](../../entities/sourccey.md) ([Vulcan Robotics](../../entities/vulcan-robotics.md), Aug 2026) and [XLeRobot](../../entities/xlerobot.md) ([Vector Wang](../../entities/vector-wang.md), Aug 2025) are the same idea a year apart: a dual-arm, mostly-3D-printed, [FeeTech](../../entities/feetech.md)-actuated, [Raspberry Pi](../../entities/raspberry-pi-5.md)-hosted, [LeRobot](../../entities/lerobot.md)-driven mobile manipulator, pitched at household chores for roughly the price of a laptop. They converge on the component list because that component list is the only one that closes at this price.

Where they diverge is instructive, and the divergences are not evenly distributed: **Sourccey is a product, XLeRobot is a build**, and almost every difference follows from that.

## Side by side

| | **Sourccey** | **XLeRobot** |
|---|---|---|
| Origin | [Vulcan Robotics](../../entities/vulcan-robotics.md), commercial startup | [Vector Wang](../../entities/vector-wang.md), open community project |
| Price | **undisclosed** (store "Coming Soon") | **$660** BOM |
| Availability | ships Sep 2026 | build it yourself, now |
| Height / mass | 1,030 mm / **15.88 kg** | ~fixed torso / ~12 kg |
| Base | **4 × mecanum**, open-loop PWM, **no encoders** | [LeKiwi](../../entities/lekiwi.md)-class: 3-wheel omni, mecanum, or 2-wheel differential variants |
| Vertical lift | **yes** — 12 V linear actuator, 100 N | **no** — fixed torso, 0.5–1.25 m workspace |
| Arms | 2 × 5 DOF + gripper, custom | 2 × [SO-ARM101](../../entities/so-arm101.md), 5 DOF + gripper |
| Reach | +622.5 mm extended | ~0.36 m from cart edge (~0.40 m arm) |
| Servos | FeeTech **STS3215 + STS3250** | 17 × FeeTech STS3215 |
| Compute | Raspberry Pi 5 | Pi 4/5 optional (data relay); [Jetson](../../entities/jetson-thor.md)/[Hailo](../../entities/hailo.md) upgrade paths documented |
| Cameras | 4 × 720p USB, 120° FOV, **360×240 default** | RGB stock; stereo +$30; RealSense D415 +$220 |
| LiDAR | **2D 360°, 12 m, 5–13 Hz** — included | not stock |
| Power | 12 V 10 Ah LiFePO4 ≈ **120 Wh**, runtime TBD | **288 Wh** Anker C300, **10+ hr** stock |
| UI | **7-inch onboard touchscreen** + desktop app | none |
| Teleop | leader arms **or Oculus Quest via IK** | leader arms / keyboard |
| Shipped policy | **4 × [X-VLA](../../entities/x-vla.md) laundry-folding micromodels** | none — bring your own |
| Hardware license | **CERN-OHL-S-2.0** (copyleft) | Apache 2.0 |
| Reproducibility | 115 STEP files; **no BOM, wiring, URDF, or STLs** | full BOM, assembly docs, readthedocs, URDF |
| Assembly | kit; docs "coming soon" | 2–4 hr from scratch, 1–2 hr with pre-built arms |

## Where Sourccey is genuinely ahead

**1. It ships a working policy.** Four [X-VLA](../../entities/x-vla.md) laundry-folding micromodels out of the box. No other platform in this tier does this — XLeRobot hands you a robot and a link to [LeRobot](../../entities/lerobot.md). The gap between "you could train a policy" and "here is a policy that folds your shirts" is the difference between a kit and a product, and it is the single most defensible thing about Sourccey.

**2. A vertical axis.** The 100 N linear actuator is a real functional advantage. XLeRobot's fixed torso confines it to a 0.5–1.25 m band; a household robot that cannot reach a countertop *and* a floor sock is doing half the job. This wiki's [assistive robotics](../../concepts/robotics/assistive-robotics.md) coverage repeatedly identifies vertical reach as the discriminator between demo and utility.

**3. LiDAR is standard.** 2D 360°, 12 m, 5–13 Hz, included rather than a $220 add-on. Whatever the SLAM caveat below, the sensor is on the robot.

**4. It is integrated.** Onboard touchscreen, desktop app, Oculus Quest IK teleoperation, autocalibration to mechanical limits via current feedback, per-arm JSON calibration split between robot and host. This is systems work XLeRobot's users do themselves.

**5. Manufactured, not sourced.** No IKEA cart, no BOM scavenger hunt, no calibration-by-forum-post.

## Where XLeRobot is ahead — and it is not close on some of these

**1. Power. 288 Wh vs ~120 Wh.** XLeRobot's Anker C300 is 2.4× the energy and gives a documented **10+ hours** stock; Sourccey publishes **no runtime at all** and marks consumption "TBD," while carrying a linear actuator, four wheel motors, twelve servos, a LiDAR, and a 7-inch display. This wiki has already done the arithmetic on what happens when compute is added to a 288 Wh pack ([XLeRobot + Thor power budget](../projects/xlerobot-thor-power-budget.md): 10 hr → 1.4–2.5 hr). Sourccey starts from less than half that budget. Suspect single-digit hours at best, and that is a guess because Vulcan has not said.

**2. Reproducibility.** XLeRobot publishes a BOM with part numbers, assembly documentation, readthedocs, and a URDF. Sourccey publishes **115 STEP files and nothing else** ([sourccey-hardware repo](../../sources/sourccey-hardware-repo.md)) — no BOM, no wiring, no assembly sequence, and **no URDF**, which blocks simulation outright and is a prerequisite for the Oculus IK that Vulcan advertises (so one exists internally and is unpublished). Both documentation pages read "will be available soon"; the advertised Electrical repository does not exist. For a project whose *name* is a pun on open source, this is the sharpest gap between claim and artifact.

**3. Licensing, if you intend to build on it.** Apache 2.0 vs **CERN-OHL-S-2.0**. Strongly reciprocal means distributing a modified Sourccey design obliges you to publish your sources under the same terms. Invisible to a hobbyist; decisive for anyone contemplating a derivative product. Note that Vulcan's *software* is Apache 2.0 — the copyleft is on the hardware only.

**4. Compute headroom.** XLeRobot's Pi is explicitly a relay, with documented onboard upgrade paths ([Jetson ladder](jetson-module-ladder-power-performance.md), [Hailo NPU](hailo-npu-vs-jetson-xlerobot.md)) if you want autonomy on the robot. Sourccey's Pi 5 is the compute story, and Vulcan's answer to wanting more is to **rent it from them**.

**5. It exists and has a price.** $660, buildable this afternoon.

## The two engineering tensions worth naming

> [!warning] Open-loop mecanum wheels vs. an October 2026 SLAM roadmap
> Sourccey's four mecanum wheels are driven **open-loop by PWM with no encoders**, so there is **no wheel odometry**. The roadmap's next feature after shipping is "improved SLAM tools — mapping, localization, and spatial understanding." Mecanum is the drive type *most* prone to unmodelled slip (each wheel's rollers slide laterally by design), which is exactly the regime where scan matching most needs a dead-reckoning prior. LiDAR-only 2D SLAM at 5–13 Hz with no odometry, on a slipping holonomic base, is a substantially harder problem than the roadmap wording implies — and adding encoders later is a mechanical change, not a software patch. XLeRobot's LeKiwi-derived bases are not obviously better here, but XLeRobot also isn't promising SLAM in eight weeks.

> [!warning] The advertised AI does not run on the advertised computer
> [X-VLA](../../entities/x-vla.md)-0.9B on a [Florence-2](../../entities/florence-2.md)-Large backbone will not run at control rate on a Raspberry Pi 5. Vulcan's spec page lists both under adjacent headings and never connects them; the reconciliation appears under "External AI" — *"capabilities scale with the host computer. Rented compute is planned."* So Sourccey is the **same PC-does-inference, Pi-relays architecture as XLeRobot**, with a subscription attached. That is a reasonable design and a reasonable business; presenting "Starting AI: XVLA" next to "Compute: Raspberry Pi 5" without comment is not.

## The interesting unknown: 5 DOF against a 6-DOF-trained prior

Both robots use **5-DOF arms plus a gripper** — no wrist yaw, so neither can realize arbitrary end-effector orientations. Their reachable poses form a lower-dimensional manifold inside SE(3).

That matters more for Sourccey because Sourccey ships [X-VLA](../../entities/x-vla.md), whose aligned action space is **absolute SE(3) EEF pose** (xyz + Rot6D + binary gripper) and whose pretraining embodiments are **all ≥6 DOF** — Franka 7, UR5 6, [AgileX](../../entities/agilex-piper.md) 6, AGIBOT 7 ([X-VLA paper](../../sources/xvla-paper.md)). [Soft prompts](../../concepts/learning/soft-prompt-cross-embodiment.md) are precisely the mechanism intended to absorb configuration differences like this, and the paper's own transfer experiment shows prompts exploiting kinematic similarity between UR5 and WidowX. But a **kinematically deficient** target is a different ask from a merely *different* one, and nothing published tests it.

The rest of the transfer story is more encouraging than it first looks. X-VLA pretrains at **224×224**, so Sourccey's 360×240 capture is adequate rather than marginal. X-VLA's flagship real-world result *is* cloth folding — ~100% success at 33 folds/hour on bimanual AgileX from 1,200 curated demonstrations — so Vulcan picked the model whose headline demo is its own headline demo. What it cannot borrow is the setup: AgileX has 6-DOF arms, better actuators, and wrist cameras, and those 1,200 episodes were DAgger-curated over roughly 50–60 operator-hours with per-100-episode retraining.

> [!note] Prediction worth checking in six months
> If Sourccey's folding works well on shipped units, the most interesting result will not be the robot — it will be the first real evidence that soft-prompt conditioning transfers a 6-DOF-pretrained VLA onto a cheaper, kinematically poorer arm. That is a research finding hiding inside a consumer product. If it works poorly, the likely culprits in order: no force/torque in the recorded data (positional only), limited backdrivability, and the DOF deficiency — not the camera resolution.

## Which one, for whom

- **Learning the stack, or want to modify it** → **XLeRobot**. Documented, cheap, permissively licensed, upgradeable, and every part is explainable. Nothing about Sourccey's current documentation supports learning from it.
- **Want a robot that folds laundry on day one, and $/hour matters more than $** → **Sourccey**, once the price appears. It is the only option in this tier that ships a working policy.
- **Building a derivative product** → **XLeRobot** on licensing alone, unless you are content under CERN-OHL-S.
- **Research on cheap embodiments** → **XLeRobot** today (URDF, sim, documented BOM). Revisit Sourccey when a URDF ships.
- **Undecided** → wait ~8 weeks. Sourccey's price, runtime, and open-source completeness all resolve between September and November 2026, and all three are currently unknown.

## Related

- [Sourccey](../../entities/sourccey.md) · [XLeRobot](../../entities/xlerobot.md) · [LeKiwi](../../entities/lekiwi.md) · [SO-ARM101](../../entities/so-arm101.md)
- [X-VLA](../../entities/x-vla.md) · [Soft-prompt cross-embodiment conditioning](../../concepts/learning/soft-prompt-cross-embodiment.md)
- [Robot platforms comparison](robot-platforms-comparison.md) · [Open-source robot AI projects](open-source-robot-ai-projects.md) · [VLA deployability landscape](vla-deployability-landscape.md)
- [XLeRobot + Thor power budget](../projects/xlerobot-thor-power-budget.md) · [Anker portable power stations](anker-portable-power-stations.md)

## Sources

- [Vulcan Robotics — Sourccey product site](../../sources/vulcan-robotics-sourccey-site.md)
- [sourccey-hardware GitHub repository](../../sources/sourccey-hardware-repo.md)
- [X-VLA paper](../../sources/xvla-paper.md)

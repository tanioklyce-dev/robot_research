---
title: Vulcan Robotics — Sourccey product site (home / specs / docs)
type: source
url: https://vulcanrobotics.ai/
author: Vulcan Robotics (founder Nick Maselli)
published: 2026 (rolling site; roadmap dated Aug 2026 – 2028)
ingested: 2026-08-13
tags: [vulcan-robotics, sourccey, open-source-hardware, mobile-manipulator, lerobot, xvla, feetech, raspberry-pi-5, mecanum, laundry-folding, household-robot, teleoperation]
---

## Summary

The product site for **Sourccey**, "the open-source personal robot for physical AI and robotics development" from US startup [Vulcan Robotics](../entities/vulcan-robotics.md), founded by [Nick Maselli](../entities/nick-maselli.md). Three pages ingested: the marketing home page, a genuinely detailed **specs** page, and a **docs** page that is currently empty.

Sourccey is a **1,030 mm tall, 15.88 kg, 4-mecanum-wheel dual-arm mobile manipulator**, ~90% PLA-printed on a desktop Bambu P1S, driven by [FeeTech](../entities/feetech.md) STS3215/STS3250 smart servos on a [Raspberry Pi 5](../entities/raspberry-pi-5.md), trained through a [LeRobot](../entities/lerobot.md) fork, and shipping with **[X-VLA](../entities/x-vla.md) laundry-folding micromodels** preinstalled. Platform open-sources **August 2026**; first units ship **September 2026**. **No price disclosed** — the store reads "Coming Soon."

Its closest relative in this wiki is [XLeRobot](../entities/xlerobot.md): same servo family, same compute, same framework, same household-manipulation pitch. The differences are the interesting part — see [Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md).

## Key claims — specifications

### Mechanical
- **Footprint** 414 mm diameter; handles +25 mm; arms at side +162.5 mm; arms extended **+622.5 mm**. **Height** 1,030 mm (40.5 in). **Mass** 15.88 kg.
- **Mobility**: 4 mecanum wheels, 96 mm diameter, 12 kg-cm torque, 60 rpm max. **Open-loop PWM, no encoders**; motor driver model TBD.
- **Linear actuator**: 12 V 2 A, 100 N load (vertical lift — an axis [XLeRobot](../entities/xlerobot.md) lacks).
- **Arms**: 2 × (**5 DOF + 1 DOF gripper**), 6 revolute joints each.
- **Joint torques**: shoulder yaw 30 kg-cm (2.9 N·m); shoulder pitch 50 kg-cm (4.9 N·m) **×1.5 effective via planetary gearbox**; elbow pitch 50 kg-cm; wrist pitch 30 kg-cm; wrist roll 30 kg-cm; gripper 30 kg-cm.
- **Link lengths**: base→shoulder yaw 50 mm, shoulder yaw 70, shoulder pitch 157.5, elbow pitch 160, wrist pitch 73, gripper 110 mm.

### Fabrication & service
- **Bambu P1S, 0.4 mm nozzle. PLA.** Cosmetic parts 10% infill crosshatch; load-bearing 20–40% gyroid; layer height 0.08–0.28 mm.
- Fasteners metric steel: M2 (wire clips), M2.5 (camera), M3 (everything else). **No adhesives in structural joints**; electric screwdriver only.
- "Public STLs allow replacements and open-source modifications." Servos "individually addressable and replaceable."

### Actuation & sensing
- **[FeeTech](../entities/feetech.md) STS3215 and STS3250** smart serial servos; **Waveshare Bus Servo Driver**; absolute position control with configurable velocity/torque limits.
- **Backdrivability: "limited due to high resistance under load."**
- Gripper: single actuated, PLA structure with **5% TPE pad**.
- Feedback: absolute encoder **0–4095** in each servo; velocity derived from position; servo-reported current/torque. **No external force/torque sensing.**
- **Motor data recorded is "positional only (observation and commanded position)"** — no current or torque in the dataset.

### Compute & I/O
- **Raspberry Pi 5**, 5.1 V regulated via Pi 5 power HAT; **PCIe-to-USB HAT** + cooling fan.
- I/O: USB carries **4 cameras, 1 speaker, 2 motor drivers, 1 LCD**; GPIO carries wheel motors, actuator sensing, battery detection.
- **Motor bus**: daisy-chained UART at **1,000,000 baud**, per-servo unique IDs (1–6 left arm, 7–12 right arm).
- Networking: local Wi-Fi or direct-to-Pi access point.

### Vision & navigation
- **Innomaker U20CAM-720p**, 30 fps, USB 2.0, **120° FOV**; default capture **360×240**, max 640×480.
- Mounts: fixed head angled **20° down**, plus end-effector mounts. Software timestamping against joint state.
- **2D 360° LiDAR**: 180° 2D omnidirectional scan coverage, configurable **5–13 Hz**, range **up to 12 m** on 70%-reflectivity white, **8,000 samples/s**. Positioned for "LiDAR-based SLAM workflows, localization, obstacle awareness."

### Power
- **12 V 10 Ah LiFePO4** (≈120 Wh), ~5,000 cycles. 2 A and 5 A 12 V DC chargers. Buck converter + central power rail with local regulation. PCB with fusing, overcurrent protection, power cutoff.
- **Power consumption: "Min and max TBD."** No runtime figure published.

### Software & AI
- Stack: **Sourccey desktop** app + **Lerobot-Vulcan** tooling ("details in progress").
- **Starting AI: "XVLA with 4 micromodels: folding T-shirts, shorts, jeans/pants, and long shirts."**
- **External AI: "Capabilities scale with the host computer. Rented compute is planned for users who need stronger training or inference."**
- Data: images 30 fps RGB at configurable resolution (default 360×240); motor data positional only; storage **`.mp4` for images, `.parquet` for motor data, JSON metadata** — i.e. the `LeRobotDataset` layout.

### Control interfaces
- **7-inch 1024×600 touchscreen** onboard with custom firmware; equivalent downloadable desktop app.
- **Teleoperators**: two leader arms with FeeTech motors (15 kg-cm), calibrated by zeroing from a set position.
- **Oculus Quest** supported via inverse kinematics mapping controller pose → end-effector pose.
- Calibration: autocalibration drives to mechanical limits detected by **current feedback**; absolute-encoder zeroing with homing and quick presets; JSON config per arm (robot calibration on the Pi, teleoperator calibration on the host).

### Environment & safety
- Even floor ideal; shallow/medium carpet works; hardwood or tile recommended. **0–50 °C** ambient.
- Fault handling: overcurrent protection, fuse, physical off switch. Torque/velocity/acceleration limits in software and servo firmware.
- Safety strategy is explicitly **material-based**: "low-mass PLA parts reduce injury risk," flexible TPE gripper pads, rounded edges.

## Key claims — roadmap

| Date | Item |
|---|---|
| **Aug 2026** | Open-source the platform and launch publicly |
| **Sep 2026** | First robots ship to early users |
| Oct 2026 | "Improved SLAM tools" — mapping, localization, spatial understanding |
| Nov 2026 | AI developer collaboration tools |
| Early 2027 | "Autonomous integrations with minimal human intervention" |
| 2028 | "Full autonomy across core household tasks" |

Marketed capabilities: **laundry** (fold, sort), **setting the table**, **cleaning**. Developer pitch is teleoperate → record → train → rollout via `lerobot-teleoperate` and friends.

## Analysis

> [!warning] Open-loop wheels vs. the SLAM roadmap
> The mecanum drive is **open-loop PWM with no encoders**, so there is **no wheel odometry** — while the October 2026 roadmap item is "improved SLAM tools." Mecanum bases slip more than most (each wheel's rollers slide laterally by design), which is exactly the case where scan-matching benefits most from an odometry prior. LiDAR-only SLAM on a 5–13 Hz 2D scanner with no dead-reckoning is a materially harder problem than the roadmap wording suggests. Adding encoders later is a mechanical change, not a software one.

> [!warning] Where does X-VLA actually run?
> The specs page advertises "XVLA with 4 micromodels" under **Software & AI** and lists the **Raspberry Pi 5** under **Compute** — with nothing connecting them. [X-VLA](../entities/x-vla.md) is **0.9 B parameters on a Florence-2-Large backbone**; it will not run at control rate on a Pi 5. The reconciliation is buried under "External AI": *"capabilities scale with the host computer. Rented compute is planned."* So Sourccey is a **PC-does-inference, Pi-relays** platform, the same arrangement as [XLeRobot](../entities/xlerobot.md) — a reasonable design, undersold clearly.

> [!note] Estimated payload — laundry-scale, by design
> Shoulder pitch is the limiting joint: 4.9 N·m × 1.5 gearbox ≈ **7.35 N·m stall**. Distance from shoulder pitch to gripper tip = 157.5 + 160 + 73 + 110 ≈ **0.5 m**. Subtracting a rough 1.5 N·m for the arm's own weight leaves ≈ 5.9 N·m → **~1.2 kg at full extension at stall**, and smart servos are typically run near a third of stall continuously → **~0.3–0.5 kg sustained**. That is consistent with the [SO-ARM101](../entities/so-arm101.md) class (600–1000 g at ~0.4 m) and consistent with the marketed tasks: cloth, cutlery, light dishes. Not consistent with anything heavy. *Wiki-derived estimate, not a vendor figure.*

> [!note] No force feedback in the recorded data
> The dataset schema is **positional only** — observed and commanded joint position. Servo current is used for calibration and limits but is not recorded. Combined with "limited backdrivability," this makes Sourccey a poor platform for contact-rich policy learning that needs force signals, and a fine one for the kinematically-dominated tasks it advertises. Folding cloth is a good match; opening a stiff drawer is not.

> [!note] Static stability is worth watching
> 1,030 mm tall on a 414 mm footprint, with arms that extend **622.5 mm** from centre. The 12 V 10 Ah LiFePO4 pack and the base plates presumably sit low enough to keep the CoM manageable, but no CoM, tipping-angle, or maximum-extension-with-payload figure is published, and the 100 N linear actuator raises mass further. Carpet is listed as acceptable, which is the worst case for a tall narrow base.

> [!warning] The docs page is empty
> Both entries read **"will be available soon"**: software setup/run docs, and hardware kit assembly/setup docs. It links four repositories — Hardware, Electrical, Software, LeRobot-compatible fork — but **no "Electrical" repository exists publicly in the `vulcan-forge` org** as of 2026-08-13 (see [sourccey-hardware repo](sourccey-hardware-repo.md)). "Wiring diagrams and board-level construction details" are advertised and not published.

## Entities mentioned

- [Vulcan Robotics](../entities/vulcan-robotics.md), [Nick Maselli](../entities/nick-maselli.md), [Sourccey](../entities/sourccey.md)
- [X-VLA](../entities/x-vla.md) · [LeRobot](../entities/lerobot.md) · [FeeTech](../entities/feetech.md) · [Raspberry Pi 5](../entities/raspberry-pi-5.md)
- Comparison: [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md), [SO-ARM101](../entities/so-arm101.md)

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) · [Imitation learning](../concepts/learning/imitation-learning.md) · [Assistive robotics](../concepts/robotics/assistive-robotics.md)
- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md)

## Open questions

- **Price.** Undisclosed at ingest. Without it, none of the value comparisons against [XLeRobot](../entities/xlerobot.md) ($660) or [LeKiwi](../entities/lekiwi.md) can be closed.
- **Runtime.** 120 Wh with a 100 N linear actuator, 12 servos, 4 wheel motors, a Pi 5, a LiDAR and a 7-inch display. Consumption is "TBD"; no runtime is claimed anywhere.
- **Which X-VLA checkpoint?** "4 micromodels" implies four task-specific finetunes, but from which base — X-VLA-0.9B, or something smaller distilled for the platform? Are the weights open, or is the "open source" claim scoped to hardware/electrical/software only?
- **How were the folding models trained on a 5-DOF arm** when X-VLA's aligned action space is full SE(3) EEF pose and every pretraining embodiment had ≥6 DOF? This is the single most interesting unanswered engineering question in the source.
- Is there a **URDF**? None is published, which blocks simulation and complicates the advertised Oculus IK path.
- The Aug 2026 "open source the platform" milestone is *this month*. Re-check the org for the Electrical repo, a BOM, and assembly docs.

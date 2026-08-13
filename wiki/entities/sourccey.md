---
title: Sourccey
type: entity
subtype: robot
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [sourccey, vulcan-robotics, mobile-manipulator, dual-arm, mecanum, lerobot, xvla, feetech, raspberry-pi-5, 3d-printed, household-robot, laundry-folding, open-hardware, cern-ohl]
---

**Sourccey** — the **open-source personal home robot** from [Vulcan Robotics](vulcan-robotics.md): a 1,030 mm, 15.88 kg dual-arm mobile manipulator on four mecanum wheels, ~90% PLA-printed, running [LeRobot](lerobot.md) on a [Raspberry Pi 5](raspberry-pi-5.md) and shipping with **[X-VLA](x-vla.md) laundry-folding micromodels** preinstalled. Platform open-sources **August 2026**; first units ship **September 2026**. **Price undisclosed** as of 2026-08-13.

Hardware: [github.com/vulcan-forge/sourccey-hardware](https://github.com/vulcan-forge/sourccey-hardware) (**CERN-OHL-S-2.0**). Software: `lerobot-vulcan`, `lerobot-robot-sourccey`, `sourccey-desktop` (Apache 2.0 where licensed).

## Why it matters in this wiki

Sourccey is the **first consumer robot product in this wiki's coverage to ship with a named research VLA preinstalled**. [XLeRobot](xlerobot.md) and [LeKiwi](lekiwi.md) hand you a platform and point at [LeRobot](lerobot.md); Sourccey hands you four working laundry-folding policies and a store page. Whether the policies survive contact with a 5-DOF PLA arm is the open question — but the *packaging* is a step nobody else in the sub-$2k tier has taken.

It also lands squarely in the wiki's [assistive robotics](../concepts/robotics/assistive-robotics.md) and household-manipulation themes with a task list — laundry, table setting, cleaning — that matches [π0](pi-zero.md)'s and [X-VLA](x-vla.md)'s flagship demos rather than a demo reel of pick-and-place.

## Specs

| | |
|---|---|
| **Height / mass / footprint** | 1,030 mm · 15.88 kg · 414 mm diameter |
| **Reach** | arms at side +162.5 mm; extended **+622.5 mm** |
| **Base** | 4 × mecanum, 96 mm, 12 kg-cm, 60 rpm — **open-loop PWM, no encoders** |
| **Lift** | 12 V 2 A linear actuator, 100 N |
| **Arms** | 2 × **5 DOF + 1 DOF gripper** (6 revolute joints each) |
| **Actuators** | [FeeTech](feetech.md) **STS3215 + STS3250**, Waveshare bus servo driver, daisy-chained UART @ **1 Mbaud**, IDs 1–6 left / 7–12 right |
| **Joint torque** | shoulder yaw 2.9 N·m · shoulder pitch 4.9 N·m **×1.5 planetary** · elbow 4.9 · wrist pitch/roll 2.9 · gripper 2.9 |
| **Link lengths** | 50 / 70 / 157.5 / 160 / 73 / 110 mm |
| **Compute** | [Raspberry Pi 5](raspberry-pi-5.md), 5.1 V via power HAT, PCIe-to-USB HAT, fan |
| **Cameras** | 4 × Innomaker U20CAM-720p, 30 fps, 120° FOV, USB 2.0 — default **360×240**, max 640×480; head mount at 20° down + end-effector mounts |
| **LiDAR** | 2D 360°, 5–13 Hz, 12 m @ 70% reflectivity, 8,000 samples/s |
| **Power** | 12 V 10 Ah LiFePO4 ≈ **120 Wh**, ~5,000 cycles; **consumption and runtime TBD** |
| **UI** | 7-inch 1024×600 onboard touchscreen + desktop app |
| **Teleop** | two leader arms (FeeTech, 15 kg-cm) or **Oculus Quest** via IK |
| **Materials** | PLA on Bambu P1S, 0.4 mm nozzle; M2/M2.5/M3 steel; 5% TPE gripper pad |
| **Environment** | even floor ideal, carpet tolerated, 0–50 °C |

All from the [Vulcan specs page](../sources/vulcan-robotics-sourccey-site.md).

## Software stack

- **`lerobot-vulcan`** — fork of [LeRobot](lerobot.md); the policy zoo includes `xvla` (upstream, not a Vulcan addition).
- **`lerobot-robot-sourccey`** — third-party LeRobot plugin registering robots `sourccey` / `sourccey_client` / `sourccey_follower` and teleoperators `sourccey_leader` / `bi_sourccey_leader` / `sourccey_teleoperator`. Requires Python 3.12–3.13, LeRobot 0.6.x.
- **`sourccey-desktop`** — Tauri + TypeScript kiosk app, with a Raspberry Pi autostart systemd unit for the onboard touchscreen.
- **Data format** — `.mp4` video + `.parquet` motor data + JSON metadata, i.e. `LeRobotDataset`. **Motor data is positional only** (observed + commanded position); no current, torque, or force is recorded.

## AI

Ships with **"XVLA with 4 micromodels"** — folding T-shirts, shorts, jeans/pants, and long shirts ([Vulcan specs](../sources/vulcan-robotics-sourccey-site.md)). See [X-VLA](x-vla.md) for the model and [the paper](../sources/xvla-paper.md) for the cloth-folding lineage: X-VLA's own flagship real-world result is bimanual cloth folding at ~100% success / 33 folds per hour, trained from 1,200 DAgger-curated demonstrations on an [AgileX](agilex-piper.md) platform.

> [!warning] Inference does not run on the robot
> [X-VLA](x-vla.md)-0.9B on a [Florence-2](florence-2.md)-Large backbone cannot run at control rate on a [Raspberry Pi 5](raspberry-pi-5.md). Vulcan's own spec page says so obliquely — *"capabilities scale with the host computer. Rented compute is planned for users who need stronger training or inference."* Sourccey is a **PC-does-inference, Pi-relays** platform, exactly like [XLeRobot](xlerobot.md), and the specs page never states it plainly.

> [!note] The position-only recording is the deeper limit
> Sourccey's dataset schema is **joint position only** — no current, torque, or force. That caps what any policy trained on Sourccey data can learn to the **kinematically dominated** tasks it advertises (cloth, cutlery, light dishes) and rules out contact-rich work. The cheapest published route out is **[OpenFT](openft-sensor.md)**, a Hall-effect 6-axis F/T sensor with open Gerbers and a JLCPCB-ready BOM — unbenchmarked, unmaintained, and the only thing in this wiki aimed squarely at this gap.

> [!warning] 5 DOF against a 6-DOF-trained prior
> X-VLA aligns all embodiments to **absolute SE(3) end-effector pose** (xyz + Rot6D + binary gripper), and every one of its pretraining embodiments has ≥6 arm DOF. Sourccey's 5-DOF arms — shoulder yaw, shoulder pitch, elbow pitch, wrist pitch, wrist roll, with **no wrist yaw** — cannot realize arbitrary orientations; their reachable poses are a lower-dimensional manifold in that action space. [Soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md) are precisely the mechanism meant to absorb such a configuration difference, so this is a genuinely interesting first field test rather than an obvious error. Nothing published tests it.

## Engineering notes

- **Payload ≈ 0.3–0.5 kg sustained.** Shoulder pitch at 4.9 N·m × 1.5 ≈ 7.35 N·m stall over a ~0.5 m distal chain, less ~1.5 N·m of arm weight, derated to continuous → a few hundred grams. Comparable to [SO-ARM101](so-arm101.md). Laundry- and cutlery-scale. *Wiki-derived estimate.*
- **No odometry.** Open-loop PWM wheels with no encoders, on a mecanum base (the drive type most prone to lateral roller slip), while the roadmap promises "improved SLAM tools" in Oct 2026. LiDAR-only SLAM without dead reckoning is the hard version of that problem.
- **Limited backdrivability** ("high resistance under load") — relevant to both leader-follower teleop feel and to contact safety.
- **Safety is material-based**, not sensor-based: low-mass PLA, TPE pads, rounded edges, software/firmware torque limits, fuse and physical cutoff. No compliance control, no external force sensing.
- **Tall and narrow** — 1,030 mm on a 414 mm footprint with 622 mm of arm extension. No published CoM or tipping figures.
- **A vertical lift**, which [XLeRobot](xlerobot.md) explicitly lacks (fixed-height torso, 0.5–1.25 m workspace). For household work this is a real functional advantage.

## Comparison

Head-to-head with the [XLeRobot](xlerobot.md) / [LeKiwi](lekiwi.md) line: [Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md).

## Roadmap

Aug 2026 open-source + launch · Sep 2026 first shipments · Oct 2026 SLAM tooling · Nov 2026 collaboration tools · early 2027 "autonomous integrations" · 2028 "full autonomy across core household tasks."

## Mentioned in

- [Vulcan Robotics — Sourccey product site](../sources/vulcan-robotics-sourccey-site.md)
- [sourccey-hardware GitHub repository](../sources/sourccey-hardware-repo.md)
- [Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md)

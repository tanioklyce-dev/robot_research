---
title: "OpenArm documentation — docs.openarm.dev (Enactic; 2.0, Sept 2026)"
type: source
url: https://docs.openarm.dev/
local_path: raw/2026-09-13-openarm-docs-snapshot.md
sha256: 69c5e4c30b916ad1e2340e994f4e51fe70c698c8b8174921dff9bf92d3b62b8d
author: "Enactic, Inc. (OpenArm team; docs contributors incl. abetomo, hiroyams, kou, otegami)"
affiliation: "Enactic, Inc., Japan"
published: 2026-09-09
venue: "Docusaurus documentation site; source in github.com/enactic/openarm/website (2.0 docs current; 1.0 docs versioned)"
format: docs site (JS-rendered; ingested from the MDX sources on the main branch, snapshot of 28 pages)
license: "docs and software Apache-2.0; hardware CAD CERN-OHL-S-2.0"
fetch_url: https://raw.githubusercontent.com/enactic/openarm/main/website/docs/overview/index.mdx
tags: [openarm, enactic, open-hardware, bimanual, 7-dof, quasi-direct-drive, damiao, bilateral-teleoperation, force-feedback, leader-follower, evaluation-cell, reproducibility, lerobot, dora, isaac-lab, mujoco, can-fd, vendor-docs, primary-source]
ingested: 2026-09-13
---

# OpenArm documentation (docs.openarm.dev)

## Summary

**The primary for OpenArm, the open-hardware 7-DOF humanoid-proportioned arm from Enactic (Japan) that two other wiki platforms had been sourcing without the wiki knowing where it came from.** The docs describe the 2.0 lineup released with the hardware repo's 2.0.0 tag on 2026-09-09: the **OpenArm 2.0 arm** (7 DOF, QDD backdrivable Damiao motors, **4.1 kg nominal / 6.0 kg peak payload including the end-effector**, CAN-FD, aluminium and stainless structure on a MISUMI frame, human-scale for a 160–165 cm person, now with an in-hand camera in a compact gripper), the **OpenArm Cell** (a ~100 kg, ~480 W standardized evaluation enclosure with fixed lighting, cameras, a 300 mm Z-axis, an area-sensor reach-in stop and a mechanical zero-position calibration jig), and the **OpenArm KER** (Kinematic Equivalent Replica: a 1.7 kg motorless, shoulder-mounted leader arm with identical joint structure at 70% link length and 16 absolute magnetic encoders, so teleoperation is 1:1 with no retargeting). A complete bimanual system is **$6,500 from the certified manufacturer WowRobo**; a DIY build is documented down to MISUMI part numbers, MEVIY-machined parts, JLCPCB boards and LCSC harnesses.

The project's stated purpose in 2.0 has shifted from "an open arm" to reproducible evaluation: *"Claims like 'Model A outperforms Model B' only hold meaning when results can be reproduced under identical conditions, so the project pairs the arm itself with a standardized evaluation environment and teaching tools."* The software stack is a **Dora** dataflow (observer → policy server over a Unix socket with Arrow IPC → action executor that Hermite-upsamples 30 → 250 Hz with a 15 Hz low-pass) with a documented policy-server contract, a native dataset format that converts to **LeRobot v2.1/v3.0**, an ACT training tutorial on a public HF dataset, **bilateral force-feedback teleoperation at ≥500 Hz** with a tanh friction model, and simulation in **Isaac Lab (official upstream integration)** and MuJoCo.

> [!note] What the docs do not contain
> No accuracy, repeatability or power figures (*"We're preparing the documentation"*); no success rates for any policy; no benchmark results from the Cell; the KER and the VR teleop on real hardware are marked not yet released or *"coming soon."* The manufacturer list is a vendor-maintained directory with self-reported prices. Everything here is Enactic's own description of its product.

## Key claims

### The arm (Hardware → OpenArm 2.0)

| Spec | Value |
|---|---|
| DOF | 7 per arm (+ gripper) |
| Payload | **4.1 kg nominal** (held 1 min, worst posture) / **6.0 kg peak** (3 s move + 1 s hold); *includes the end-effector* — a 1.5 kg tool leaves 2.6 / 4.5 kg |
| Motors | Damiao **DM-J4310-2EC** (3 / 7 Nm, 10:1), **DM4340** (9 / 27 Nm, 40:1 — *not* QDD, chosen for payload and compactness), **DM-J8009P-2EC** (20 / 40 Nm, 9:1, 24–48 V); 14-bit magnetic encoders, CAN |
| Bus | CAN-FD; recommended USB-CANFD adapters only (*"other CAN devices may result in unexpected behavior"*) |
| Structure | aluminium + stainless; MISUMI aluminium-frame pillars; M6-tapped base plate; mechanical joint limits on every axis |
| Gripper (2.0) | compact single-mechanism parallel gripper, **in-hand camera**, replaceable fingers; 1.0 gripper was a linkage design, 88 mm jaw opening, 60° rotor travel |
| End-effector interface | replace part `J8_B` |
| Scale | proportions of a 160–165 cm person |

Unchanged from 1.0: DOF, payload envelope, motor lineup, MISUMI base. Changed: gripper, camera, the Cell and KER, and the docs structure. A V1 → V2 upgrade kit exists.

### OpenArm Cell (Hardware → OpenArm Cell)

- Purpose: *"a standardized benchmark for accurately comparing and evaluating the performance of robotic foundation models"* by fixing *"lighting, cameras, and calibration procedures"* as part of the system.
- Off-the-shelf MISUMI enclosure and power system; **~100 kg, ~480 W** plus the PC; WowRobo's kit is 1100 × 926 × 1883 mm with a 300 mm Z-axis, top camera and controlled lighting.
- **Reach-in stop**: area sensors cut power on workspace intrusion.
- **Zero-position calibration jig**: mechanically constrains the gripper to CAD-defined angles, *"eliminating assembly tolerances from the dataset."*

### OpenArm KER (Hardware → OpenArm KER)

- Motorless leader arm, joint structure identical to OpenArm 2.0, links at **70%**, so *"high-precision 1:1 motion mapping without requiring any coordinate transformation or retargeting."*
- **1.7 kg** (CFRP pipes, machined aluminium, resin); shoulder-mounted backpack, on in 30 s, folds into a travel case.
- Common **encoder module** on every axis: magnetic encoder (Infineon TLE5012B, 15-bit absolute per WowRobo), bearings, hardware limit and driver in one body; daisy-chained with per-module IDs (7+1 DOF on minimal wiring); sold standalone at $49 for custom input devices.
- Docs say *"not yet released"*; WowRobo lists it from $2,599.

### Teleoperation (Teleop)

- **Unilateral** (position mirroring, no feedback) and **bilateral** (two-way force feedback) leader–follower modes from `openarm_teleop`; three threads (leader, follower, admin); per-joint Kp, Kd and a friction model **τ_f = Fc·tanh(k·dq) + Fv·dq + Fo**.
- Bilateral control *"requires a high control frequency (500 Hz or higher)"* and careful gain tuning; zero position is arm straight down, calibrated per arm.
- VR (Meta Quest 3) teleop exists in Isaac Lab at ~20 FPS; real-hardware VR is *"coming soon."*

### Software stack (Tutorial, API reference)

- **Dora dataflow** runtime: a 250 Hz timer, an observer bundling five cameras (ceiling, head left/right, wrist left/right at 960 × 600) plus two 8-D arm states into an Arrow StructArray, a policy server exchanging Arrow IPC files over `/dev/shm` and JSON over a Unix socket, an actions executor that **upsamples 30 → 250 Hz (Hermite) and low-pass filters at 15 Hz**, and a MuJoCo bridge so the same dataflow runs in simulation. Mock `dummy` nodes run without hardware.
- **Dataset format**: per-episode parquet for `qpos`/`qvel`/`qtorque` (note: torque is recorded), JPEG frames per camera, `metadata.yaml` with success flags and task prompts; `openarm-dataset-convert … --format lerobot_v3.0` (or v2.1).
- **Training tutorial**: LeRobot 0.6.1 ACT, 10k steps, on the public `enactic/openarm-2-cell-pick_up_cube_mujoco-lerobot` dataset.
- **Simulation**: `openarm_isaac_lab` (Isaac Sim 5.1, Isaac Lab 2.3; reach, lift-cube, open-drawer environments; *"officially integrated into NVIDIA's Isaac Sim / Isaac Lab ecosystem"*); `openarm_mujoco` (`v1/openarm_bimanual.xml`, torque-controlled actuators).

### Buying (Purchase)

| Vendor | Status | Price (USD, self-reported) | Lead time |
|---|---|---|---|
| **RT Corporation** (Tokyo) | Official manufacturing partner | by quotation; setup, testing, JP adapter, optional 1-yr warranty | arranged |
| **WowRobo** (Shenzhen) | **Certified ★★★** | **$5,400 (V1.1) / $6,500 (V2) / $6,200 (Cell) / $2,599 (KER) / $49 encoder unit** | 20–40 days, worldwide |
| VLAI Robotics, Cereboto, Soma, Anvil (Taipei, ships in 48 h), PowerZ, SVTRobotics, Muniu Liuma, MJTWO | evaluating / not evaluated | $4,699–$7,080 | 2 days – 6 weeks |

WowRobo describes itself as *"the official manufacturer of the SO-ARM101."* A warning flags **"OpenArmX Pro Max" as not affiliated or compatible**. The DIY BOM is priced in yen; motors are sold through the project.

### Safety guide

Fasten to a stable surface; nobody inside the range of motion while powered; goggles; stay within payload; *"true safety can only be ensured through sincere risk assessment"* — the standard open-hardware disclaimer, but written out.

## What this resolves in the wiki

- **The "two OpenArms" question.** [UME](../entities/ume.md) evaluated on a *"WowRobo OpenArm 1.0 bimanual ($5,200)"*; [Sensori Robotics](../entities/sensori-robotics.md) sells [Yuri](../entities/yuri.md) on *"OpenArm+"* and points at docs.openarm.dev. Both trace to **Enactic's OpenArm**: WowRobo is its certified manufacturer (its V1.1 is $5,400 today), and Sensori's OpenArm+ is a derivative — Sensori appears nowhere on Enactic's manufacturer list. So the wiki's hunch that a standard was forming above the SO-101 tier was right, and it has a name and an owner.
- **A second bilateral rig at the low-cost tier.** [FACTR](factr-paper.md)'s ~$1,230 actuated leader was the wiki's only bilateral force-feedback teleop rig; OpenArm ships bilateral control in its teleop package and records joint torque in its dataset format.
- **An evaluation cell as a product.** The [policy-evaluation](../concepts/robotics/robot-policy-evaluation.md) thread has argued that success rates are incomparable across labs because lighting, cameras and calibration drift; the Cell is a vendor building exactly that control into hardware. Whether anyone publishes comparable numbers on it is the open question.

## Entities mentioned

- [OpenArm](../entities/openarm.md) · [Enactic](../entities/enactic.md) · [WowRobo](../entities/wowrobo.md) · [Damiao](../entities/damiao.md) (motors; datasheets hosted at damiao.enactic.ai) · [Sensori Robotics](../entities/sensori-robotics.md) / [Yuri](../entities/yuri.md) (derivative) · [UME](../entities/ume.md) (evaluated on a WowRobo OpenArm 1.0) · [SO-ARM101](../entities/so-arm101.md) (WowRobo's other product) · [LeRobot](../entities/lerobot.md) · [MuJoCo](../entities/mujoco.md) · [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) · RT Corporation, Dora, MISUMI — no pages.

## Concepts touched

- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the Cell as a hardware answer to cross-lab drift.
- [Imitation learning](../concepts/learning/imitation-learning.md) — bilateral teleop data collection; LeRobot-format conversion; ACT tutorial.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — positioning claim ("deployment in contact-rich environments"); torque recorded in datasets.

## Open questions

- **Accuracy, repeatability, power draw** — the FAQ says documentation is being prepared.
- **Any published policy result** on OpenArm hardware or in the Cell; the tutorial trains in MuJoCo.
- **Actual bilateral loop rate achieved** and on what compute; the docs give a floor (500 Hz), not a measurement.
- **KER release** — listed by WowRobo for sale while the docs say the design is being finalized.
- **How derivative is OpenArm+?** Sensori's changes (extended reach) versus upstream are undocumented on either side.

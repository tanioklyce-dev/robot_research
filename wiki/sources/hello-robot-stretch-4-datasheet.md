---
title: "Hello Robot Stretch 4 Datasheet (Rev 5, As Launched)"
type: source
url: https://hello-robot.com/stretch-4/
fetch_url: https://hello-robot.com/wp-content/uploads/2026/05/HelloRobot-DataSheet-Stretch-4-Rev5_AsLaunched.pdf
url_superseded: https://hello-robot.com/HelloRobot-DataSheet-Stretch-4-Rev5_AsLaunched.pdf
url_rechecked: 2026-08-29
local_path: raw/HelloRobot-DataSheet-Stretch-4-Rev5_AsLaunched.pdf
sha256: fb3c5d9150b54d7240aaa46639d1ff7782f41edeb36daa879057af2a47261e81
author: Hello Robot, Inc.
published: 2026-05-12
ingested: 2026-05-25
tags: [stretch, stretch-4, hello-robot, datasheet, primary-source, mobile-manipulator, hesai-lidar, luxonis, jetson-orin-nx, feetech]
---

> [!note] The datasheet moved (2026-08-29) — same file, new URL
> The original root-level URL now returns **404**. Hello Robot relocated the PDF under `/wp-content/uploads/2026/05/`; `fetch_url` points there, and `url` now points at the Stretch 4 product page as the stabler landing target.
>
> **Nothing on this page changes.** The relocated file's SHA-256 is **identical** to the sealed hash of the archived copy in `raw/`, so this is confirmed link rot rather than a revision — every spec below stands on exactly the same bytes. Caught by `scripts/check_source_drift.py --check`, which reports link rot separately from drift because a moved file and a changed file need different responses.

> [!note] Provenance
> The [Stretch 4 launch source](hello-robot-stretch-4-launch.md) ingested 2026-05-17 explicitly flagged this PDF as **404 at the time** and asked the user to "drop it in `raw/` if it surfaces." It has now surfaced — Rev 5, "As Launched" — and is the canonical Stretch 4 spec sheet. This source page is the **datasheet-confirmed** layer; the launch page remains the canonical narrative + pricing reference.

## Summary

**Two-page Hello Robot product datasheet for Stretch 4**, version **Rev 5 ("As Launched")**, dated to the 2026-05-12 launch. Confirms and extends the partial spec list from the [launch announcement](hello-robot-stretch-4-launch.md) with the **exact sensor model numbers** (Hesai J128 LiDAR, Luxonis OAK-FFC AR0234 / IMX378 / OAK-D SR cameras), **specific compute SKUs** (Intel Core Ultra 5 225H + Jetson Orin NX 16 GB / 128 GB NVMe), the **active safety architecture** (motor-current force limiting, 100 Hz watchdog, IMU tilt avoidance, Runstop button, 6× Pixart laser-line cliff curtains), and **environmental ratings** (10–30 °C, IP20, 10–90% RH non-condensing, 12-month standard warranty). Datasheet is explicit that Stretch 4 is **not yet FCC Class A certified — research/lab/development only**.

## Key claims (verbatim from datasheet)

### 1. System at a glance
- **DOF: 9** — *"3-wheel omnidirectional base, 1 lift, 1 telescoping arm, 3-axis wrist (Yaw, Pitch, Roll), and optional end-of-arm tool"*. Range of motion: **120 cm lift, 55 cm arm extension**, **310° wrist Yaw / Pitch / Roll**. Dynamic speed: **50 cm/s lift, 70 cm/s arm**.

> [!warning] Contradiction with launch source
> The [Stretch 4 launch page](hello-robot-stretch-4-launch.md) reports **"8 redundant DOF + gripper"** based on the forum post; the datasheet reports **"9 DOF"** including the base + lift + arm + 3-axis wrist + optional tool. The numbers are countable differently (whether the base counts as DOF, whether the gripper counts, whether the optional tool counts). The datasheet's enumeration is the more concrete; treat 9-DOF as the canonical count when including the omni base, and 8-DOF when restricting to non-base joints + gripper.

### 2. Performance & manipulation
- **Reach**: 55 cm + 6 cm wrist.
- **Payload**: 2.5 kg (arm extended) / 4 kg (arm retracted).
- **Total weight**: 46 kg / **33 kg ballast off for transport**.
- **Runtime**: 8 h (light CPU load).
- **Height / footprint**: 160 cm / 43 cm diameter. *(Launch page reported 45 cm; datasheet says 43 cm — datasheet supersedes.)*

### Mobility & base
- 3-wheel **low gear-ratio omnidrive** wheels for "seamless 360° movement."
- **Top speed: 60 cm/s**.
- **Terrain**: up to **20 mm step/threshold clearance**; handles smooth floors to heavy-pile carpet.

### 3. Perception & intelligence (sensor model numbers)
- **Head LiDARs**: **Dual 3D hemispherical Hesai J128 LiDARs**, 360° × 187° H × 189° FOV.
- **Head wide-FOV cameras**: **Dual global-shutter 2.3 MP RGB cameras — Luxonis OAK-FFC AR0234**.
- **Head high-res**: **12 MP RGB — Luxonis OAK-FFC IMX378**.
- **Wrist depth**: **Luxonis OAK-D SR stereo depth camera with 4 TOPs processing**.
- **Hazard detection**: **6× Pixart laser-line sensor curtains** for cliff and hazard monitoring. *(Not previously surfaced in the launch page.)*
- **9-DOF IMU** in mobile base for tilt detection and odometry.

### 4. Compute & connectivity (specific SKUs)
- **Primary — Intel NUC 15**: **Intel Core Ultra 5 225H**, **32.0 GiB RAM**, **1.0 TB NVMe**.
- **Auxiliary — NVIDIA Jetson Orin NX**: **16 GB RAM**, **128 GB NVMe**, **WiFi 5.2 + Ethernet**.

### 5. Safety & human interaction
- **Active safety**: force limiting via **motor-current monitoring**; **100 Hz watchdog**; **tilt avoidance via IMU**.
- **Collision avoidance**: **100 Hz self-collision avoidance using MuJoCo + URDF**.
- **Physical safety**: manual override for the braked lift joint; **dedicated Runstop button in the head**.
- **Interaction**: **dual RGB Neopixel "eye" arrays**; **360° noise-reduction speakerphone (3W stereo)**.
- Headline framing: *"Stretch 4 is designed to operate safely around humans with fully backdriveable joints and reactive controllers."*

### 6. Developer ports & power
- **Power**: **512 Wh LiFePO4** battery, **quick-swap**, integrated charger and BMS.
- **Tooling**: **quick-release tool plate** with **24 V [Feetech](../entities/feetech.md) RS485 bus**.
- **Expansion ports**:
  - Base: HDMI, Ethernet, 3× USB 3.2 Type A.
  - Head: USB 3.2 Type A, Type C.
  - Wrist: USB 2.0 Type A.
- **End-of-arm tools**: includes **Stretch Gripper 4 (200 mm aperture)**; supports **Parallel Gripper 4** and **tablet mounts**.

### 7. Other specifications
| Category | Detail |
| --- | --- |
| Warranty | 12-month standard; optional 2-year service plan |
| Operating temp | 10 °C – 30 °C |
| Ingress protection | IP20 |
| Humidity | 10 % – 90 % RH (non-condensing) |
| Included accessories | Stretch Gripper 4, Gamepad, Wall Power Adapter, Aruco tags |

### FCC compliance
> *"This product is currently intended for research, development, and laboratory use only. It has not yet been certified for compliance with FCC Class A limits."*

## What this datasheet adds beyond the launch page

| New info | Source detail |
|---|---|
| **Exact LiDAR**: dual Hesai J128 | not in launch page |
| **Exact wide-FOV cam**: Luxonis OAK-FFC AR0234 (2.3 MP global-shutter) | launch page said "global-shutter fisheye" only |
| **Exact high-res cam**: Luxonis OAK-FFC IMX378 (12 MP) | launch page said "12 MP central RGB" only |
| **Wrist depth + TOPs**: OAK-D SR with 4 TOPs onboard | launch page named OAK-SR but not the TOPs figure |
| **6× Pixart cliff curtains** | not surfaced in launch page |
| **Intel Core Ultra 5 225H** (specific SKU) | launch page said "Intel Core Ultra 5 (15th gen) NUC" |
| **Jetson Orin NX**: 16 GB RAM / 128 GB NVMe / WiFi 5.2 + Ethernet | launch page only named the module |
| **24 V Feetech RS485 tool bus** | tool plate not detailed in launch page |
| **Stretch Gripper 4 = 200 mm aperture** | launch page said only "Compliant Gripper" |
| **Force limiting via motor-current monitoring** | safety mechanism not detailed in launch page |
| **Dedicated head Runstop button** | launch page didn't enumerate Runstop |
| **Neopixel "eye" arrays + 3W stereo speakerphone** | HRI hardware not detailed in launch page |
| **Operating temp / IP rating / humidity / warranty** | environmental envelope not in launch page |
| **Not FCC Class A certified** (explicit) | launch page noted "research/lab only" without the FCC-specific language |
| **Top base speed: 60 cm/s; 20 mm step clearance** | launch page said "~2× faster" without absolute number |
| **Lift 50 cm/s; arm 70 cm/s** | launch page said "~2× faster" without absolute number |
| **Footprint = 43 cm diameter** (not 45 cm) | minor correction to launch page |

## Entities mentioned

- [Stretch](../entities/stretch.md) — the platform; this is the canonical Stretch 4 spec source.
- [Hello Robot](../entities/hello-robot.md) — vendor.
- [Jetson Orin NX](../entities/jetson-thor.md) — confirmed as the auxiliary compute module.

## Concepts touched

- Compute split: primary CPU (Intel NUC 15 Core Ultra 5) for deterministic Stretch Body control + auxiliary NVIDIA Jetson Orin NX for AI/perception — the same **control-on-CPU, AI-on-accelerator** pattern documented across [Jetson Thor / DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) and the [PX4 + Jetson companion-computer model](../entities/px4-autopilot.md).
- Active safety in mobile manipulators: motor-current force limiting, 100 Hz watchdog, IMU tilt avoidance, hardware Runstop, MuJoCo self-collision avoidance.

## Open questions

- **Stretch Gripper 4 finger force**, max payload at full aperture, and compliant-vs-parallel performance comparison — datasheet gives aperture (200 mm) and the tool-bus (24 V Feetech RS485) but no force-limit specs.
- **AI workload performance** on the **Intel Core Ultra 5 225H NPU** specifically — the 225H carries Intel's AI Boost NPU but the datasheet treats it as a CPU only and routes AI to the Orin NX.
- **Stretch 4 LiDAR data path**: where the dual Hesai J128 streams are fused (NUC vs Orin NX) — datasheet doesn't say.
- **FCC certification roadmap**: the explicit "not yet" implies it's planned. No date given. This blocks any non-research / non-lab deployment, including the in-home assistive use that prior Stretch generations enabled under research protocols.
- **Whether Stretch 3 software is fully compatible** with the new sensor / tool-bus + NUC 15 + Orin NX combination — see the policy-transfer open question on the [launch source page](hello-robot-stretch-4-launch.md).

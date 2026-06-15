---
title: "Stretch 4 launch — Hello Robot purchase + product + forum announcement"
type: source
url: https://hello-robot.com/purchase/
secondary_urls:
  - https://hello-robot.com/stretch-4/
  - https://forum.hello-robot.com/t/introducing-stretch-4/1505
  - https://www.therobotreport.com/hello-robots-latest-stretch-4-is-bigger-faster-and-stronger-than-previous-versions/
author: Hello Robot (corporate site + forum); reporting via The Robot Report
published: 2026-05-12 (launch announcement)
ingested: 2026-05-17
tags: [stretch, stretch-4, hello-robot, mobile-manipulator, jetson-orin-nx, ros2-jazzy, holonomic-base, lidar, primary-source]
---

> [!note] Ingest depth and provenance
> User pointed at `hello-robot.com/purchase/` for **Stretch 4 details**. The purchase page is canonical for **pricing + accessories + availability** but light on technical specs. To make the wiki's Stretch 4 picture complete, this source page also pulls from:
>
> 1. The [Stretch 4 product page](https://hello-robot.com/stretch-4/) — primary specs.
> 2. The [Hello Robot forum launch post](https://forum.hello-robot.com/t/introducing-stretch-4/1505) (2026-05-12) — the most substantive published technical-spec writeup.
> 3. [The Robot Report's coverage](https://www.therobotreport.com/hello-robots-latest-stretch-4-is-bigger-faster-and-stronger-than-previous-versions/) — independent corroboration of the launch (HTTP 403 on direct fetch; key facts via search snippet).
>
> **Datasheet now ingested:** The [official Stretch 4 datasheet PDF (Rev 5, As Launched)](https://hello-robot.com/HelloRobot-DataSheet-Stretch-4-Rev5_AsLaunched.pdf) was 404 at the time of this page's first ingest, but surfaced on 2026-05-25 — see [Stretch 4 Datasheet source page](hello-robot-stretch-4-datasheet.md) for exact sensor SKUs (Hesai J128 LiDAR, Luxonis OAK-FFC AR0234 / IMX378 / OAK-D SR), the specific Intel NUC 15 + Jetson Orin NX configuration, the active-safety architecture, and the FCC-Class-A "not yet certified" caveat. This launch page remains the narrative + pricing reference; the datasheet is the canonical spec sheet.

## Summary

**Stretch 4** — Hello Robot's **fourth-generation single-arm mobile manipulator**, launched **2026-05-12**. Headline framing: "*a simply useful robot that puts people first.*" The most substantive generational jump in the Stretch line — **new omnidirectional holonomic base**, ~2× faster motion across arm / lift / base, +10% reach, 8 redundant DOF + gripper, dual hemispherical 3D LiDAR + global-shutter fisheye + 12 MP central + Luxonis OAK-SR wrist depth, and a new Intel Ultra 5 NUC compute with optional [Jetson Orin NX](../entities/jetson-thor.md) accessory. **Base price $29,950** (up from ~$20k for Stretch 3). **2–4 week ship; early customers June 2026.** Currently certified for **laboratory and research use only**.

## Pricing (verbatim, from purchase page)

| Item | Price |
| --- | --- |
| **Stretch 4 base unit** | **$29,950** |
| Docking Station (self-charging) | $1,495 |
| Parallel Gripper (quick-connect) | $1,495 |
| NVIDIA Jetson Orin NX (optional add-on) | $2,495 |
| Spare Battery & Ballast | $1,495 |
| Extended 3-Year Warranty | $2,495 |
| Full Robot Refurb | starting at $2,000 |

No academic discount tier is mentioned on the page. International distributors named: **Nihon Binary, Tegara/UNIPOS, Sogo Electronics** (Japan); **CN Best** (China); **ROAS, JPUBLICO** (Korea).

## What's in the box (verbatim, from purchase page)

> "Stretch Compliant Gripper, Battery & Ballast, Wall power supply, Reflective Aruco tag kit, Gamepad & Pistol Teleop controllers, Aruco Cube, Tools and cables"

The **Compliant Gripper** is included; the **Parallel Gripper** is an add-on. Both are quick-connect-compatible.

## Shipping & availability

Per purchase page:

> "Stretch 4 typically ships within 2–4 weeks from receipt of purchase order or pre-payment."

Per forum launch post:

> "Stretch 4 is available now [...] will start shipping to early customers next month" (i.e., **June 2026**).

Use cases listed in nav: **Assist**, **Research**, **Enterprise**. Certification scope (verbatim):

> "Stretch 4 is currently only certified for laboratory and research use."

## Key specs (product page + forum)

| Spec | Value |
| --- | --- |
| Reach | **55 cm + 6 cm wrist** (10% over Stretch 3 in both horizontal + vertical) |
| Payload (arm extended) | **2.5 kg** |
| Payload (arm retracted) | **4 kg** |
| Total weight | **46 kg** (33 kg with ballast removed for transport) |
| Height | **160 cm** |
| Footprint | **45 cm diameter** |
| Runtime | **8 hours** (light CPU load) — "more than double Stretch 3's 4–8 hr" |
| DOF | **8 redundant + gripper** (Stretch 3 was 7 + gripper) |

### Mobile base — fundamental change vs Stretch 3

- **Omnidirectional holonomic base** with **three 8" wheels** (Stretch 3 was differential-drive). Large wheels intended to handle carpets, rugs, and thresholds.
- **~2× faster** than Stretch 3 across arm, lift, and base.

### Wrist + gripper

- **New 3DOF cobot-style wrist** with no external cabling; **ambidextrous** (configurable left- or right-handed).
- **Integrated depth camera in the wrist** (Luxonis OAK-SR — RGB + stereo depth).
- Compliant Gripper standard; Parallel Gripper available via quick-connect.

### Sensor suite

- **Two hemispherical 3D LiDAR sensors** — combined output > **2M depth readings/sec**.
- **Global-shutter fisheye RGB cameras** with calibrated RGB-D point cloud at **10 Hz**. Hemispherical coverage minimizes blind spots while the arm is in use.
- **One central 12 MP high-resolution RGB camera** observing the gripper's workspace.
- **Luxonis OAK-SR** at wrist (RGB + stereo depth).
- Floor-hazard sensing (specifics not enumerated).

### Power

- **512 Wh LiFePO4** battery — claimed **10× cycle life** of the Stretch 3 pack.
- **Self-charging docking station** (separate $1,495 accessory).

### Compute

- **Primary**: **Intel Core Ultra 5 (15th gen) NUC**, **32 GB RAM**, **1 TB SSD**. Runs the Stretch Body stack at 100 Hz.
- **Optional**: **NVIDIA Jetson Orin NX** (the $2,495 add-on), pre-configured with **Docker + ROS 2 Jazzy + CUDA + PyTorch**.

> [!note] Compute change vs Stretch 3
> Stretch 3 shipped with a single NUC 12 as its compute. Stretch 4 splits compute: a **newer NUC for the body / control loop** and **Jetson Orin NX as an optional AI accelerator add-on**. This is a meaningful pricing change — Jetson is no longer bundled. Buyers running heavy on-board VLA / VLM workloads will pay the extra $2,495.

### Software stack

- **Stretch Body** with **100 Hz control loop**.
- **MuJoCo-based self-collision avoidance**; **IMU-based overtilt detection**.
- **ROS 2 Jazzy** (Stretch 3 was Humble).
- **Python SDK** open-source.
- **[Nav2](../entities/nav2.md)** for navigation autonomy.
- "Reference demos for autonomy and Embodied AI" — links to the [Hello Robot Develop page](https://hello-robot.com/develop/) (not separately ingested).

## Stretch 4 vs Stretch 3 — at a glance

| Axis | Stretch 3 | Stretch 4 |
| --- | --- | --- |
| Generation introduced | 2024 | 2026-05-12 |
| Base | differential-drive | **3-wheel omnidirectional holonomic** |
| Speed (arm / lift / base) | baseline | **~2× faster** |
| Reach | baseline | **+10% horizontal + vertical** |
| DOF | 7 + gripper | **8 redundant + gripper** |
| Wrist | DexWrist3 | **3DOF cobot-style, ambidextrous, no external cabling, integrated depth camera** |
| Runtime | 4–8 hr | **8 hr** + self-charging dock |
| Battery cycle life | baseline | **10×** (512 Wh LiFePO4) |
| LiDAR | single | **two hemispherical 3D LiDAR** (>2M readings/sec) |
| Workspace cameras | Stretch Gripper 3 D405 + head | **dual fisheye RGB + 12 MP central + OAK-SR wrist** |
| Compute (primary) | NUC 12 | **Intel Ultra 5 NUC, 32 GB / 1 TB** |
| GPU/AI compute | not bundled | **optional Jetson Orin NX** ($2,495 add-on) |
| ROS | ROS 2 Humble | **ROS 2 Jazzy** |
| Self-collision avoidance | — | **MuJoCo-based** |
| Base price | ~$20,000 | **$29,950** |
| Certification | research / lab | research / lab |
| Stretch 3 archive | — | redirected to hello-stretch3.com |

## Why it matters in this wiki

- **Generational jump, not point release.** The mobile-base architecture change (differential → holonomic) and the wrist redesign are mechanically significant — published policies trained on Stretch 3 won't necessarily transfer without retraining. The action-space + base-kinematics change is the issue.
- **Major downstream-policy implications.** This wiki tracks several published policies trained on Stretch 3 — [Robot Utility Models](../entities/robot-utility-models.md), [OK-Robot](../entities/ok-robot.md), [Dobb·E](../entities/dobb-e.md), [stretch_ai](../entities/stretch-ai.md). None of these have published Stretch 4 results yet. **Open question: do they transfer with retraining or with new data collection?**
- **Pricing repositioning.** $20k → $29,950 (+~50%) plus a $2,495 Jetson add-on changes the math vs the wiki's [household robot decision Stretch-vs-G1 synthesis](../syntheses/platforms/household-robot-decision-stretch-vs-g1.md). The G1 at $16k is now nearly half-price relative to a fully-equipped Stretch 4 + Jetson + dock.
- **Compute split (NUC + optional Jetson Orin NX)** is interesting: Hello Robot is decoupling the deterministic-control compute (NUC) from the AI-inference compute (Jetson Orin NX). This is the same pattern the [Jetson Thor / DGX Spark split](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) articulates at a different scale — control on a CPU, AI on an accelerator.
- **ROS 2 Jazzy + 100 Hz Stretch Body** suggests a stack-modernization pass alongside the hardware refresh. Worth checking how `stretch_ai` evolves to match.

## Entities mentioned

- [Stretch](../entities/stretch.md) — the platform; this source is the canonical Stretch 4 reference.
- [Hello Robot](../entities/hello-robot.md) — vendor.
- [stretch_ai](../entities/stretch-ai.md) — the open Python + LLM-agent stack; Stretch 4 compatibility per the launch announcement.
- [Jetson Orin NX](../entities/jetson-thor.md) — now sold as an optional Stretch 4 accessory.

## Concepts touched

- Holonomic vs differential-drive mobile bases (architectural change).
- Compute split between deterministic control (CPU) and AI inference (GPU/Jetson).

## Open questions / TBD

- **~~Datasheet PDF~~** — **resolved 2026-05-25**: datasheet surfaced and is now ingested as the [Stretch 4 Datasheet source page](hello-robot-stretch-4-datasheet.md). Spec table in [Stretch entity](../entities/stretch.md) is the merged view.
- **Stretch 3 policy transfer**: do [Robot Utility Models](../entities/robot-utility-models.md), [OK-Robot](../entities/ok-robot.md), and [Dobb·E](../entities/dobb-e.md) transfer to Stretch 4, or do they need retraining? The new base kinematics + wrist DOF make this nontrivial.
- **`stretch_ai` compatibility**: does the existing [stretch_ai](../entities/stretch-ai.md) stack work on Stretch 4 out of the box, or is there a Stretch-4-specific branch?
- **Enterprise tier specifics**: the use-case nav lists Assist / Research / Enterprise but the launch post doesn't elaborate on what "Enterprise" means in practice. Worth a separate ingest if Hello Robot publishes a deployment program page.
- **Home / clinical certification roadmap**: still lab-and-research-only as of launch. The wiki has many references to Stretch in long-term in-home deployments (Henry Evans, the Nanavati feeding study) — those were S3 / earlier under research protocols. Whether Stretch 4 changes the certification status is unclear.
- **Datasheet-level specs not yet captured**: gripper finger-force, opening width, max base speed in m/s, exact LiDAR model, exact RGB sensor models, network connectivity details, USB / accessory port specs.
- **Aaron Edsinger quotes from the launch** — none surfaced in the materials ingested; the forum post signs as "The Hello Robot Team." Worth chasing if Edsinger gave press interviews.

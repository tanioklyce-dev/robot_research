---
title: Stretch
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-25
sources: 15
tags: [stretch, stretch-3, stretch-4, mobile-manipulation, hello-robot, research-robot, holonomic-base, lidar, ros2-jazzy, hesai-lidar, luxonis, feetech]
---

**Vendor:** [hello-robot.com](https://hello-robot.com/) — current product is **Stretch 4** at [hello-robot.com/stretch-4](https://hello-robot.com/stretch-4/); purchase + accessories at [hello-robot.com/purchase](https://hello-robot.com/purchase/). The prior generation (Stretch 3) is archived at [hello-stretch3.com](https://hello-stretch3.com).

Mobile-manipulation robot from [Hello Robot](hello-robot.md). **Current generation: Stretch 4 (launched 2026-05-12, $29,950)** — see [Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md). The **de-facto research platform** for academic mobile-manipulation work in 2024–2026; nearly every wiki-tracked in-home robotics deployment runs on Stretch.

## Generations

| Gen | Launched | Headline form | Base | Compute |
| --- | --- | --- | --- | --- |
| Stretch 1–2 | 2020–2022 | telescoping single-arm | differential-drive | Intel NUC |
| Stretch 3 | 2024 | telescoping single-arm, RealSense gripper depth camera, DexWrist3 | differential-drive | NUC 12 |
| **Stretch 4** | **2026-05-12** | telescoping single-arm; **new omnidirectional holonomic base**; **3DOF ambidextrous cobot-style wrist**; integrated OAK-SR wrist depth | **3-wheel holonomic** | **Intel Ultra 5 NUC + 32 GB / 1 TB**; **optional Jetson Orin NX** ($2,495 add-on) |

## Stretch 4 specs

Spec sources: [Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md) (launch announcement) + [Stretch 4 datasheet (Rev 5)](../sources/hello-robot-stretch-4-datasheet.md) (canonical spec sheet). Datasheet supersedes the launch page where they disagree.

| Spec | Value | Source |
| --- | --- | --- |
| Reach | 55 cm + 6 cm wrist (+10% vs Stretch 3) | both |
| Payload (arm extended / retracted) | 2.5 kg / 4 kg | both |
| DOF | **9 by datasheet's enumeration** (omni base + lift + telescoping arm + 3-axis wrist + optional tool); **8 redundant + gripper** by launch-post framing | both — see contradiction note below |
| Total weight | 46 kg (33 kg ballast-off for transport) | both |
| Height | 160 cm | both |
| Footprint | **43 cm diameter** (launch page said 45 cm; datasheet supersedes) | datasheet |
| Runtime | 8 hr (light CPU load); self-charging dock available | both |
| Battery | 512 Wh LiFePO4; quick-swap; ~10× cycle life vs Stretch 3 | both |
| Mobile base | 3-wheel omnidirectional holonomic; **top speed 60 cm/s**; **up to 20 mm step/threshold clearance** | datasheet adds absolute numbers |
| Lift / arm dynamic speed | **50 cm/s lift, 70 cm/s arm** | datasheet |
| Wrist | 3DOF cobot-style (ambidextrous, no external cabling); **310° Yaw / Pitch / Roll** | both |
| Head LiDAR | **Dual Hesai J128** 3D hemispherical; 360° × 187° H × 189° FOV; >2M depth readings/sec | datasheet adds model number |
| Head wide-FOV camera | **Dual Luxonis OAK-FFC AR0234** (2.3 MP global-shutter RGB) | datasheet adds model number |
| Head high-res camera | **Luxonis OAK-FFC IMX378** (12 MP) | datasheet adds model number |
| Wrist depth | **Luxonis OAK-D SR** stereo depth, **4 TOPs onboard** | datasheet adds TOPs figure |
| Hazard sensing | **6× Pixart laser-line cliff curtains** | datasheet only |
| IMU | 9-DOF in mobile base (tilt detection + odometry) | datasheet |
| Compute (primary) | **Intel NUC 15: Core Ultra 5 225H, 32 GiB RAM, 1 TB NVMe** | datasheet adds exact SKU |
| Compute (AI accelerator, optional) | **NVIDIA Jetson Orin NX, 16 GB RAM, 128 GB NVMe, WiFi 5.2 + Ethernet** — pre-configured Docker + ROS 2 Jazzy + CUDA + PyTorch ($2,495 add-on) | datasheet adds RAM/storage/connectivity |
| Active safety | Motor-current force limiting; 100 Hz watchdog; IMU tilt avoidance; **dedicated head Runstop button** | datasheet only |
| Collision avoidance | 100 Hz self-collision avoidance via MuJoCo + URDF | both |
| HRI hardware | **Dual RGB Neopixel "eye" arrays; 360° noise-reduction speakerphone (3W stereo)** | datasheet only |
| Tooling | **Quick-release tool plate with 24 V Feetech RS485 bus**; supports Stretch Gripper 4 (200 mm aperture), Parallel Gripper 4, tablet mounts | datasheet adds bus + aperture |
| Expansion ports | Base: HDMI + Ethernet + 3× USB 3.2-A. Head: USB 3.2-A + Type C. Wrist: USB 2.0-A | datasheet only |
| Software | Stretch Body @ 100 Hz; ROS 2 **Jazzy**; Python SDK; MuJoCo self-collision avoidance; IMU overtilt detection; Nav2 | both |
| Operating temp / IP / humidity | **10–30 °C / IP20 / 10–90 % RH non-condensing** | datasheet only |
| Warranty | **12-month standard**; optional 2-year service plan | datasheet only |
| Base price | **$29,950** (S3 was ~$20,000) | launch |
| Certification | "laboratory and research use only"; **not yet FCC Class A certified** | datasheet adds FCC specifics |

> [!warning] DOF count: 9 (datasheet) vs 8 + gripper (launch post)
> The [datasheet](../sources/hello-robot-stretch-4-datasheet.md) enumerates DOF as: 3-wheel omnidirectional base + 1 lift + 1 telescoping arm + 3-axis wrist + optional end-of-arm tool = **9**. The [launch forum post](../sources/hello-robot-stretch-4-launch.md) describes **"8 redundant + gripper"**. These are different countings of the same hardware (whether the omni base counts as one DOF, whether the gripper is separate from the "redundant" arm/lift/wrist set). Both sentences are correct; the datasheet's enumeration is the more concrete and is reproduced verbatim.

> [!note] Stretch 3 → Stretch 4 is a generational jump, not a refresh
> The base architecture (differential-drive → holonomic), the wrist (DexWrist3 → 3DOF ambidextrous cobot), and the DOF count all change. Policies and skill libraries trained on Stretch 3 are not guaranteed to transfer without retraining. See [Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md) for the open-questions list on policy transfer.

> [!note] Stretch 3 → Stretch 4 is a generational jump, not a refresh
> The base architecture (differential-drive → holonomic), the wrist (DexWrist3 → 3DOF ambidextrous cobot), and the DOF count (7 → 8) all change. Policies and skill libraries trained on Stretch 3 are not guaranteed to transfer without retraining. See [Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md) for the open-questions list on policy transfer.

## Stretch 3 specs (historical)

- Single-arm mobile manipulator: telescoping arm, differential-drive base, gripper, RealSense cameras, single LiDAR.
- DexWrist3 with manual quick-connect tool changer.
- Stretch Gripper 3 with Intel RealSense D405 depth camera (40% wider opening than prior gens).
- Compute: NUC 12 (2–3× the compute of Stretch 2).
- Electronic brake on lift actuator (safety / slow-descent).
- $20,000 ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)) — a fraction of PR2's $400,000.
- Software stacks: ROS 2 **Humble** + [stretch_ai](stretch-ai.md) (Python; includes an LLM agent).
- Simulation: [MuJoCo](mujoco-playground.md) via "Stretch Mujoco" wrapper, plus Gazebo.

## Notable use cases (cumulative across generations)

These were all demonstrated on **Stretch 2 / 3**; whether they transfer to Stretch 4 unchanged is an open question.

- [Robot Utility Models](robot-utility-models.md) zero-shot generalist policies (NYU / Meta) — Stretch 3.
- [stretch_ai](stretch-ai.md) LLM agent for natural-language tasking — Stretch 3.
- Cross-embodiment transfer (RUM transferred Stretch-trained policies to xArm 7 zero-shot).
- **[Open Vocabulary Mobile Manipulation (OVMM)](../sources/ovmm-homerobot.md)** — baseline platform (20% real-world success rate).
- **[OK-Robot](ok-robot.md)** — zero-shot pick-and-drop (58.5% success, 10 NYC homes); 1.8× over OVMM.
- **[Assistive use](../concepts/robotics/assistive-robotics.md)** — documented in-home use by Henry Evans (quadriplegic); scratching, laundry, meals, social play ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)).
- **[HCR Lab](hcrlab.md) long-term deployments** — [Maya Cakmak](maya-cakmak.md)'s lab ran 4-week summer deployments with Henry Evans in 2021, 2022, and 2023, expanding the task set each year. A prototype end-user programming (EUP) tool was built specifically for Henry in summer 2022.
- **EUP transfer to Stretch SE2** — HCR Lab's end-user robot programming tools have been ported to the commercial Hello Robot Stretch SE2.

## Related
- [Hello Robot](hello-robot.md) — vendor.
- [stretch_ai](stretch-ai.md) — primary software stack.
- [Robot Utility Models](robot-utility-models.md) — flagship policy framework targeting Stretch.
- [Jetson Orin NX / Jetson Thor lineage](jetson-thor.md) — the optional Stretch 4 AI-accelerator accessory.

## Mentioned in
- [Stretch 4 Datasheet (Rev 5)](../sources/hello-robot-stretch-4-datasheet.md) — canonical Stretch 4 spec sheet.
- [Stretch 4 launch — Hello Robot purchase + product + forum announcement](../sources/hello-robot-stretch-4-launch.md) — launch announcement + pricing.
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md)
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md)
- [OK-Robot Project Page](../sources/ok-robot-project-page.md)
- [Sense of Agency — Yang et al. 2025](../sources/yang2025-sense-of-agency.md)
- [Grasping in Clutter IVFP — Murray et al. 2024](../sources/murray2024-grasping-clutter-ivfp.md)

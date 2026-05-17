---
title: Stretch
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-17
sources: 14
tags: [stretch, stretch-3, stretch-4, mobile-manipulation, hello-robot, research-robot, holonomic-base, lidar, ros2-jazzy]
---

**Vendor:** [hello-robot.com](https://hello-robot.com/) — current product is **Stretch 4** at [hello-robot.com/stretch-4](https://hello-robot.com/stretch-4/); purchase + accessories at [hello-robot.com/purchase](https://hello-robot.com/purchase/). The prior generation (Stretch 3) is archived at [hello-stretch3.com](https://hello-stretch3.com).

Mobile-manipulation robot from [Hello Robot](hello-robot.md). **Current generation: Stretch 4 (launched 2026-05-12, $29,950)** — see [Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md). The **de-facto research platform** for academic mobile-manipulation work in 2024–2026; nearly every wiki-tracked in-home robotics deployment runs on Stretch.

## Generations

| Gen | Launched | Headline form | Base | Compute |
| --- | --- | --- | --- | --- |
| Stretch 1–2 | 2020–2022 | telescoping single-arm | differential-drive | Intel NUC |
| Stretch 3 | 2024 | telescoping single-arm, RealSense gripper depth camera, DexWrist3 | differential-drive | NUC 12 |
| **Stretch 4** | **2026-05-12** | telescoping single-arm; **new omnidirectional holonomic base**; **3DOF ambidextrous cobot-style wrist**; integrated OAK-SR wrist depth | **3-wheel holonomic** | **Intel Ultra 5 NUC + 32 GB / 1 TB**; **optional Jetson Orin NX** ($2,495 add-on) |

## Stretch 4 specs ([Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md))

| Spec | Value |
| --- | --- |
| Reach | 55 cm + 6 cm wrist (+10% vs Stretch 3) |
| Payload (arm extended / retracted) | 2.5 kg / 4 kg |
| DOF | 8 redundant + gripper |
| Total weight | 46 kg (33 kg ballast-off for transport) |
| Height | 160 cm |
| Footprint | 45 cm diameter |
| Runtime | 8 hr (light CPU load); self-charging dock available |
| Battery | 512 Wh LiFePO4; ~10× cycle life vs Stretch 3 |
| Mobile base | 3-wheel omnidirectional holonomic; 8" wheels for carpets / rugs / thresholds |
| Sensors | 2× hemispherical 3D LiDAR (>2M depth readings/sec); global-shutter fisheye RGB + 10 Hz RGB-D point cloud; 12 MP central RGB; Luxonis OAK-SR at wrist |
| Speed vs Stretch 3 | ~2× faster across arm, lift, base |
| Compute (primary) | Intel Core Ultra 5 (15th gen) NUC, 32 GB RAM, 1 TB SSD |
| Compute (AI accelerator, optional) | NVIDIA Jetson Orin NX — pre-configured Docker + ROS 2 Jazzy + CUDA + PyTorch ($2,495 add-on) |
| Software | Stretch Body @ 100 Hz; ROS 2 **Jazzy**; Python SDK; MuJoCo self-collision avoidance; IMU overtilt detection; Nav2 |
| Base price | **$29,950** (S3 was ~$20,000) |
| Certification | "laboratory and research use only" |

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
- [Stretch 4 launch — Hello Robot purchase + product + forum announcement](../sources/hello-robot-stretch-4-launch.md) — canonical Stretch 4 reference.
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md)
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md)
- [OK-Robot Project Page](../sources/ok-robot-project-page.md)
- [Sense of Agency — Yang et al. 2025](../sources/yang2025-sense-of-agency.md)
- [Grasping in Clutter IVFP — Murray et al. 2024](../sources/murray2024-grasping-clutter-ivfp.md)

---
title: Hiwonder NexArm 6-Axis (product page)
type: source
url: https://www.hiwonder.com/products/nexarm6-axis
author: Hiwonder
published: 2026
ingested: 2026-06-14
local_path: null
venue: hiwonder.com (product page)
license: n/a (commercial product page)
format: Product/marketing page
tags: [hiwonder, nexarm, lerobot, leader-follower, teleoperation, imitation-learning, low-cost-arm, embodied-ai, act, diffusion-policy, pi0, vla]
---

## Summary

**NexArm 6-Axis** is [Hiwonder](../entities/hiwonder.md)'s **LeRobot-native leader–follower robotic arm** built specifically for **imitation-learning data collection and VLA training** — Hiwonder's direct entry into the same low-cost-arm niche as [SO-ARM101](../entities/so-arm101.md). It is sold as a leader/follower pair (plus bundled "Imitation Learning" kits), advertises native **[LeRobot](../entities/lerobot.md)** integration and out-of-the-box support for **[ACT](../entities/act.md), [Diffusion Policy](../entities/diffusion-policy.md), and [π0](../entities/pi-zero.md)**, and ships a dual-camera rig for visuomotor learning. Listed from **$279.99**. This is significant for the wiki: Hiwonder now spans **both** the LLM-agent educational tier (its [OpenClaw](../entities/openclaw.md)-based [ROSOrin Pro arm](../entities/rosorin-pro-arm.md)) **and** the LeRobot imitation-learning tier — a vendor-side convergence on the SO-ARM101 leader-follower playbook.

## Key claims

- **Positioning:** "Embodied AI" / imitation-learning arm; targets imitation learning, **VLA (Vision-Language-Action) model training**, and ESP32 development.
- **Price / variants:** from **$279.99**. Four variants: **NexArm (Follower Arm)**, **NexArm (Leader Arm)**, **Imitation Learning Standard Kit**, **Imitation Learning Advanced Kit**. *(Per-variant pricing beyond the $279.99 base not fully captured.)*
- **Mechanics:** **6 axes (6-DOF)**; reach **500 mm**; payload **500 g**; repeatability **±2 mm**; weight leader **1.2 kg** / follower **1.3 kg**.
- **Actuators:** magnetic-encoder **serial bus servos** with dual-output shafts.
  - Leader: **HX-10HM ×5 + HX-12H ×1**.
  - Follower: **HX-12H ×2 + HX-30HM ×3 + HX-65HM ×1**.
  - (The HX-series bus servos match the servo family already noted on the [Hiwonder](../entities/hiwonder.md) ROSOrin Pro arm.)
- **Controllers / power:** dedicated NexArm leader and follower controllers; **12 V 5 A**; Windows/Linux/macOS; programmable via **Arduino IDE** (ESP32-class).
- **Connectivity:** multi-mode control — **USB serial, Bluetooth, Wi-Fi**.
- **Vision + end-effector:** **dual-camera system** (gripper-mounted + external); **parallel-rail gripper** with silicone pads.
- **Software:** "fully integrated with the **LeRobot** framework" for community models, datasets, and simulations; supports **ACT, Diffusion Policy, π0**.
- **Teleoperation:** leader–follower **synchronous teleoperation** plus **offline drag teaching** for data collection.

## Entities mentioned

- [NexArm](../entities/nexarm.md) (this product)
- [Hiwonder](../entities/hiwonder.md) — vendor
- [SO-ARM101](../entities/so-arm101.md) — the incumbent low-cost LeRobot leader-follower arm it competes with
- [LeRobot](../entities/lerobot.md) — advertised native framework
- [ACT](../entities/act.md), [Diffusion Policy](../entities/diffusion-policy.md), [π0](../entities/pi-zero.md) — supported IL/VLA algorithms

## Concepts touched

- **Leader–follower teleoperation** as the data-collection mode for [imitation learning](../concepts/learning/imitation-learning.md) — the same pattern as SO-ARM101.
- **Vendor convergence on LeRobot** — an educational-robotics OEM shipping a LeRobot-first arm rather than its own SDK, signalling LeRobot's pull as the low-cost IL standard.
- Dual-camera visuomotor setup (wrist + external) for ACT/Diffusion-Policy/π0 training.

## Open questions

- True per-variant pricing (kit contents and total cost vs a two-SO-ARM101 build at ~€550).
- Servo torque/spec details (HX-10HM/12H/30HM/65HM) and how reach/payload compare to SO-ARM101 (~40 cm / 600–1000 g).
- Is the LeRobot integration upstreamed/maintained, or a Hiwonder fork? No repo linked on the page.
- Does NexArm share controllers/servos with the [ROSOrin Pro arm](../entities/rosorin-pro-arm.md), or is it a separate line?

---
title: NexArm (Hiwonder)
type: entity
subtype: robot
created: 2026-06-14
updated: 2026-06-14
sources: 1
tags: [hiwonder, nexarm, lerobot, leader-follower, teleoperation, imitation-learning, low-cost-arm, embodied-ai]
---

# NexArm (Hiwonder)

**NexArm 6-Axis** — [Hiwonder](hiwonder.md)'s **LeRobot-native leader–follower robotic arm** for imitation-learning data collection and VLA training. A 6-DOF arm sold as leader/follower pairs (plus bundled "Imitation Learning" kits) from **$279.99**, with native **[LeRobot](lerobot.md)** integration and out-of-the-box **[ACT](act.md) / [Diffusion Policy](diffusion-policy.md) / [π0](pi-zero.md)** support. It is Hiwonder's direct competitor to **[SO-ARM101](so-arm101.md)**.

## Why it matters in this wiki

NexArm marks **Hiwonder spanning two tiers at once**: its earlier [ROSOrin Pro arm](rosorin-pro-arm.md) sits in the **LLM-agent / [OpenClaw](openclaw.md)** educational tier, while NexArm targets the **LeRobot imitation-learning** tier dominated by [SO-ARM101](so-arm101.md). That an educational OEM ships a **LeRobot-first** arm (rather than its own SDK) is fresh evidence of LeRobot's gravitational pull as the low-cost IL standard. It widens the [SO-ARM101 comparison table](so-arm101.md) with a second commercial leader-follower option.

## Key facts

- **DOF / mechanics:** 6 axes; reach **500 mm**; payload **500 g**; repeatability **±2 mm**; leader 1.2 kg / follower 1.3 kg.
- **Servos:** magnetic-encoder serial bus servos (dual-output shaft). Leader HX-10HM×5 + HX-12H×1; follower HX-12H×2 + HX-30HM×3 + HX-65HM×1.
- **Controllers:** dedicated leader + follower controllers; 12 V 5 A; Win/Linux/macOS; Arduino IDE (ESP32-class).
- **Connectivity:** USB serial / Bluetooth / Wi-Fi.
- **Vision + gripper:** dual-camera (wrist + external); parallel-rail gripper with silicone pads.
- **Software:** LeRobot-integrated; ACT, Diffusion Policy, π0.
- **Data collection:** leader-follower synchronous teleop + offline drag teaching.
- **Price/variants:** from $279.99 — Follower Arm, Leader Arm, Imitation Learning Standard Kit, Imitation Learning Advanced Kit.

## Related

- [Hiwonder](hiwonder.md) — vendor.
- [SO-ARM101](so-arm101.md) — the incumbent low-cost LeRobot leader-follower arm.
- [ROSOrin Pro arm](rosorin-pro-arm.md) — Hiwonder's other arm (LLM-agent / OpenClaw tier).
- [LeRobot](lerobot.md) — advertised native framework.
- [ACT](act.md) / [Diffusion Policy](diffusion-policy.md) / [π0](pi-zero.md) — supported IL/VLA algorithms.
- [Imitation learning](../concepts/learning/imitation-learning.md).

## Open questions

- Per-variant pricing vs a two-SO-ARM101 build (~€550); servo torque specs; reach/payload vs SO-ARM101.
- Whether the LeRobot integration is upstreamed or a Hiwonder fork (no repo linked).

## Mentioned in

- [Hiwonder NexArm 6-Axis (product page)](../sources/hiwonder-nexarm-product-page.md) — primary product-page ingest.

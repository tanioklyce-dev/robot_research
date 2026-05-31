---
title: openclaw_controller (Hiwonder ROS 2 bridge for OpenClaw)
type: entity
subtype: software-module
created: 2026-05-07
updated: 2026-05-31
sources: 5
tags: [openclaw, openclaw-controller, hiwonder, ros2, manipulation, claw-ecosystem, rosorin-pro, bridge-module]
---

**`openclaw_controller`** — [Hiwonder](hiwonder.md)'s **ROS 2 module** that interfaces upstream [OpenClaw](openclaw.md) with the [ROSOrin Pro](rosorin-pro.md). It exposes the robot's ROS 2 services as skills that OpenClaw can dispatch, so a natural-language command like *"pick up a red block"* turns into the right sequence of ROS 2 service calls. **Not a fork or distribution of OpenClaw** — it's an extension that sits below OpenClaw, wrapping the robot side.

## What it does

- Translates OpenClaw skill invocations into ROS 2 service calls against a predefined library.
- Skills include arm primitives (`pick`, `place`, `voice_pick`, `voice_give`, `camera_up`, `init`), chassis primitives (`cmd_vel`, navigation goals), and vision (color tracking, AprilTag pickup, depth-based interactive grasping on Jetson Orin).
- LLM-as-orchestrator pattern: OpenClaw (LLM) → skill description → `openclaw_controller` → ROS 2 service dispatch → robot hardware. Same control architecture as [stretch_ai](stretch-ai.md). No VLA, no policy learning, no teleoperation.

## Why it matters

Concrete demonstration that the [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) scales from mobile-only ([ROSOrin](rosorin.md)) to manipulation-capable platforms in the same vendor's product line — the skill library expands, the architecture is unchanged. The bridge module is also the **only production path today for running OpenClaw on a robot**; equivalent bridges for other ROS 2 robots would have to be written from scratch. Educational-tier counterpart to [stretch_ai](stretch-ai.md)'s `PickupExecutor`.

## Notable demos (from chapter 13)

- Color-based pick-and-place (red block).
- Interactive grasping (user mouse-draws bounding box; depth-based).
- Smart-home assistant (navigate, observe, summarize).
- Package / fruit-basket delivery via AprilTag (ID 0 / ID 1).
- Factory warehouse → production line task chain.

## Related

- [OpenClaw](openclaw.md) — the upstream LLM-agent framework this module bridges to ROS 2.
- [Hiwonder](hiwonder.md) — vendor.
- [ROSOrin Pro](rosorin-pro.md) — target platform.
- [ROSOrin Pro 6-DOF arm](rosorin-pro-arm.md) — the hardware the bridge drives.
- [stretch_ai](stretch-ai.md) — sibling LLM-agent stack from Hello Robot, research tier.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — design pattern.

## Open questions

- Open-source status — the "Open" prefix in the parent OpenClaw suggests yes, but no GitHub URL for the controller module itself surfaced in chapter 13 docs.
- LLM version: `openai/gpt-5.4` is the model string in the docs. Real OpenAI release or placeholder? Worth verifying.
- Cross-vendor portability — could `openclaw_controller` drive other ROS 2 robots (e.g. Stretch), or is it tightly coupled to ROSOrin Pro's skill set?
- Extensibility — how hard is it to register new skills with the module?

## Mentioned in

- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)

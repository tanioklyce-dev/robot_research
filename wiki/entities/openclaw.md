---
title: OpenClaw (Hiwonder, robotics)
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-28
sources: 1
tags: [openclaw, hiwonder, llm-agent, manipulation, ros2, name-collision]
---

> [!warning] Disambiguation — three projects share the "OpenClaw / Claw" name
> | Project | What it is | Where it lives |
> |---|---|---|
> | **This page — Hiwonder OpenClaw** | Manipulation-aware ROS 2 LLM-agent framework on [ROSOrin Pro](rosorin-pro.md) | Hiwonder docs (likely closed source) |
> | [OpenClaw (Steinberger, personal AI)](openclaw-personal-ai.md) | 375K-star MIT personal AI assistant; "Molty space lobster" naming | `github.com/openclaw/openclaw` |
> | [NemoClaw](nemoclaw.md) | NVIDIA security wrapper around the Steinberger OpenClaw | `nvidia.com/ai/nemoclaw` |
> | [Hermes Agent](hermes-agent.md) | Sibling agent framework that imports *from* the Steinberger OpenClaw via `hermes claw migrate` | `github.com/nousresearch/hermes-agent` |
>
> This page is **only** about Hiwonder's robotics-specific OpenClaw. The three other projects are an unrelated name family and share no code or design with this one.

[Hiwonder](hiwonder.md)'s **manipulation-aware LLM-agent framework** that ships with [ROSOrin Pro](rosorin-pro.md). Despite the "Claw" suffix, OpenClaw is the *software* SDK — not a hardware gripper. Architecture: LLM (OpenAI GPT) → skill descriptions → ROS 2 service dispatch → robot hardware.

## What it does
- Translates natural-language commands ("pick up a red block", "deliver the package") into sequences of ROS 2 service calls against a predefined skill library.
- Skills include arm primitives (`pick`, `place`, `voice_pick`, `voice_give`, `camera_up`, `init`), chassis primitives (`cmd_vel`, navigation goals), and vision (color tracking, AprilTag pickup, depth-based interactive grasping on Jetson Orin).
- LLM-as-orchestrator pattern, same control architecture as [stretch_ai](stretch-ai.md). No VLA, no policy learning, no teleoperation.

## Why it matters
Concrete demonstration that the [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) scales from mobile-only ([ROSOrin](rosorin.md)) to manipulation-capable platforms in the same vendor's product line. The skill library expands; the architecture is unchanged. Educational-tier counterpart to [stretch_ai](stretch-ai.md)'s `PickupExecutor`.

## Notable demos (from chapter 13)
- Color-based pick-and-place (red block).
- Interactive grasping (user mouse-draws bounding box; depth-based).
- Smart-home assistant (navigate, observe, summarize).
- Package / fruit-basket delivery via AprilTag (ID 0 / ID 1).
- Factory warehouse → production line task chain.

## Related
- [ROSOrin Pro](rosorin-pro.md) — target platform.
- [Hiwonder](hiwonder.md) — vendor.
- [ROSOrin Pro 6-DOF arm](rosorin-pro-arm.md) — the hardware OpenClaw drives.
- [stretch_ai](stretch-ai.md) — sibling LLM-agent stack from Hello Robot, research tier.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — design pattern.

## Open questions
- Open-source status — the "Open" prefix suggests yes but no GitHub URL surfaced in the chapter 13 docs.
- LLM version: `openai/gpt-5.4` is the model string in the docs. Real OpenAI release or placeholder? Worth verifying.
- Cross-vendor portability — could OpenClaw drive other ROS 2 robots (e.g. Stretch), or is it tightly coupled to ROSOrin Pro's skill set?

## Mentioned in
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)

## See also (different projects, same name)
- [OpenClaw (Steinberger, personal AI)](openclaw-personal-ai.md) — the 375K-star MIT personal-AI-assistant framework.
- [NemoClaw](nemoclaw.md) — NVIDIA's security wrapper around the Steinberger OpenClaw.
- [Hermes Agent](hermes-agent.md) — Nous Research's competing agentic framework; ships `hermes claw migrate` to import from the Steinberger OpenClaw.

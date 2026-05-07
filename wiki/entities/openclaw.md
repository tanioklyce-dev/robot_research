---
title: OpenClaw
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [openclaw, hiwonder, llm-agent, manipulation, ros2]
---

[[hiwonder|Hiwonder]]'s **manipulation-aware LLM-agent framework** that ships with [[rosorin-pro|ROSOrin Pro]]. Despite the "Claw" suffix, OpenClaw is the *software* SDK — not a hardware gripper. Architecture: LLM (OpenAI GPT) → skill descriptions → ROS 2 service dispatch → robot hardware.

## What it does
- Translates natural-language commands ("pick up a red block", "deliver the package") into sequences of ROS 2 service calls against a predefined skill library.
- Skills include arm primitives (`pick`, `place`, `voice_pick`, `voice_give`, `camera_up`, `init`), chassis primitives (`cmd_vel`, navigation goals), and vision (color tracking, AprilTag pickup, depth-based interactive grasping on Jetson Orin).
- LLM-as-orchestrator pattern, same control architecture as [[stretch-ai|stretch_ai]]. No VLA, no policy learning, no teleoperation.

## Why it matters
Concrete demonstration that the [[llm-agent-architecture|LLM-agent pattern]] scales from mobile-only ([[rosorin|ROSOrin]]) to manipulation-capable platforms in the same vendor's product line. The skill library expands; the architecture is unchanged. Educational-tier counterpart to [[stretch-ai|stretch_ai]]'s `PickupExecutor`.

## Notable demos (from chapter 13)
- Color-based pick-and-place (red block).
- Interactive grasping (user mouse-draws bounding box; depth-based).
- Smart-home assistant (navigate, observe, summarize).
- Package / fruit-basket delivery via AprilTag (ID 0 / ID 1).
- Factory warehouse → production line task chain.

## Related
- [[rosorin-pro|ROSOrin Pro]] — target platform.
- [[hiwonder|Hiwonder]] — vendor.
- [[rosorin-pro-arm|ROSOrin Pro 6-DOF arm]] — the hardware OpenClaw drives.
- [[stretch-ai|stretch_ai]] — sibling LLM-agent stack from Hello Robot, research tier.
- [[llm-agent-architecture|LLM-agent architecture]] — design pattern.

## Open questions
- Open-source status — the "Open" prefix suggests yes but no GitHub URL surfaced in the chapter 13 docs.
- LLM version: `openai/gpt-5.4` is the model string in the docs. Real OpenAI release or placeholder? Worth verifying.
- Cross-vendor portability — could OpenClaw drive other ROS 2 robots (e.g. Stretch), or is it tightly coupled to ROSOrin Pro's skill set?

## Mentioned in
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]

---
title: Hiwonder OpenClaw Practical Tutorial
type: source
url: https://wiki.hiwonder.com/projects/rosorin-pro/en/latest/docs/13_OpenClaw_Practical_Tutorial.html
author: Hiwonder
published: 2024-2025
ingested: 2026-05-07
tags: [hiwonder, rosorin-pro, openclaw, openclaw-controller, llm-agent, manipulation, ros2]
---

## Summary
Chapter 13 of the [ROSOrin Pro](../entities/rosorin-pro.md) docs — Hiwonder's practical tutorial for driving the kit with [OpenClaw](../entities/openclaw.md) via [`openclaw_controller`](../entities/openclaw-controller.md), the ROS 2 bridge module Hiwonder ships to interface OpenClaw with the robot. OpenClaw orchestrates the kit's chassis + 6-DOF arm + vision via natural-language LLM commands; `openclaw_controller` translates those into the right ROS 2 service calls. **First example in the wiki of the [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) applied to manipulation on the educational tier** (alongside [stretch_ai](../entities/stretch-ai.md) on the research tier).

## Key claims

### What OpenClaw + openclaw_controller is
- **OpenClaw** is the upstream LLM-agent software framework; **`openclaw_controller`** is Hiwonder's ROS 2 module that bridges OpenClaw to the robot. Despite the "Claw" suffix, OpenClaw is software, not a hardware gripper.
- Architecture: LLM (OpenAI GPT) ↔ OpenClaw skill descriptions ↔ `openclaw_controller` ↔ ROS 2 services ↔ hardware. Same control pattern as [stretch_ai](../entities/stretch-ai.md) but with a richer manipulation skill library.
- Cloud LLM: doc references `openai/gpt-5.4` — unusual version string; likely a recent model or placeholder.

### Skill library (the LLM's tool surface)
ROS 2 services and topics:
- Chassis: `/controller/cmd_vel` (Twist), `~/chassis_command` (string), `~/move_status` (state query).
- Arm: `~/arm_group_control` (string commands), action groups `voice_pick`, `voice_give`, `init`, `camera_up`.
- Pick/place: `/start_pick`, `/place` (Trigger services).
- Color tracking: `/claw_track_and_grab/start`, `/claw_track_and_grab/set_color` (SetString).
- Functions: `parse_twist()`, `execute_command()`, `obj_track_proc()`, `proc()`, `pick()`, `place_function()`.
- Launch files: `robot_base_control.launch.py`, `navigation_manager.launch.py`, `smart_scene_navigation.launch.py`.

### Vision integration
- LAB color-space thresholding + erosion/dilation + contour selection (lowest contour preferred — assumes downward-tilt camera).
- PID visual servoing on pan-tilt to center the target.
- AprilTag pickup demos (ID 0 = package, ID 1 = fruit basket).
- **Depth-based interactive grasping** on Jetson Orin platforms only — user mouse-draws a bounding box.

### Demos covered
- 13.3.1: chassis movement via natural language.
- 13.3.2: arm movement (e.g. carrot-pulling action group, handover).
- 13.3.3: camera scene description.
- 13.4.1: color-based 3D grasping (red block).
- 13.4.2: interactive 3D tracking + grasping.
- 13.4.3: navigation-based smart-home assistant.
- 13.4.4: multi-point delivery (package, fruit basket).
- 13.4.5: factory scenario (warehouse → production line → home).

### Notable exclusions
- **No VLA models** (no OpenVLA, GR00T, RT-X, Pi).
- **No imitation learning, teleoperation, or demonstration collection.**
- **No LeRobot, ACT, Diffusion Policy.**
- The framework is purely skill-based — LLM emits high-level intents; deterministic ROS skills do the work. Same `eval`-on-action-strings spirit as the base ROSOrin's embodied-AI demos.

## Entities mentioned
- [Hiwonder](../entities/hiwonder.md)
- [ROSOrin Pro](../entities/rosorin-pro.md)
- [OpenClaw](../entities/openclaw.md)
- [openclaw_controller](../entities/openclaw-controller.md) — Hiwonder's ROS 2 bridge module covered by this tutorial.
- [ROSOrin Pro 6-DOF arm](../entities/rosorin-pro-arm.md)

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — manipulation-capable variant.

## Open questions
- `openai/gpt-5.4` — real model release or doc placeholder?
- Is `openclaw_controller` published as open source? Upstream OpenClaw is MIT (`github.com/openclaw/openclaw`, 375K stars); no separate GitHub URL for the controller bridge module surfaced in the chapter 13 text.
- Cross-vendor portability — could `openclaw_controller` drive a Stretch or other ROS 2 robot, or is it tightly coupled to ROSOrin Pro's skill set?
- Closed-loop replanning on skill failure — same open question I have about [stretch_ai](../entities/stretch-ai.md).

---
title: Hiwonder
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-28
sources: 3
tags: [hiwonder, china, robot-kit, education, jetson, openclaw-controller, ros2]
status: stub
---

Educational-robotics vendor that builds [ROSOrin](rosorin.md) and other Jetson-based robot kits. Targets STEM education and ROS curricula. Country / founding details not extracted from the docs (Hiwonder is widely known to be a Chinese vendor, but the docs don't confirm).

## What we know
- Two parallel Sphinx documentation sites:
  - `docs.hiwonder.com` — base [ROSOrin](rosorin.md) kit ([Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)).
  - `wiki.hiwonder.com` — [ROSOrin Pro](rosorin-pro.md) arm + base variant ([Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md), [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)).
- Product line: mobile-only ([ROSOrin](rosorin.md)) plus 6-DOF arm + base ([ROSOrin Pro](rosorin-pro.md)); ships [`openclaw_controller`](openclaw-controller.md) — a ROS 2 bridge module that exposes the Pro's skills (arm, chassis, vision) to upstream [OpenClaw](openclaw.md) — as the manipulation-aware LLM-agent integration on the Pro variant.
- Custom hardware accessories: WonderEcho Pro voice module + 6-microphone circular array; HX-12H bus servos for the arm.
- Curriculum spans cloud LLMs (OpenAI / OpenRouter) and offline runtimes ([Ollama](ollama.md) + [Qwen](qwen.md) + sherpa-onnx).

## Why it matters
Represents the **educational tier** of the agentic-robotics ecosystem — distinct from research platforms like [Stretch](stretch.md). Hiwonder ships a complete LLM-agent demo on its kits, which is meaningful evidence that the [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) (not VLA) is the dominant accessible-robotics approach in 2026.

## Related
- [ROSOrin](rosorin.md) — base mobile-only kit.
- [ROSOrin Pro](rosorin-pro.md) — manipulation-capable sibling.
- [openclaw_controller](openclaw-controller.md) — Hiwonder's ROS 2 bridge that puts upstream [OpenClaw](openclaw.md) on the ROSOrin Pro.
- [Hello Robot](hello-robot.md) — research-tier counterpart vendor.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)

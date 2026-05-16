---
title: Hiwonder
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-07
sources: 3
tags: [hiwonder, china, robot-kit, education, jetson]
status: stub
---

Educational-robotics vendor that builds [ROSOrin](rosorin.md) and other Jetson-based robot kits. Targets STEM education and ROS curricula. Country / founding details not extracted from the docs (Hiwonder is widely known to be a Chinese vendor, but the docs don't confirm).

## What we know
- Two parallel Sphinx documentation sites:
  - `docs.hiwonder.com` — base [ROSOrin](rosorin.md) kit ([Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)).
  - `wiki.hiwonder.com` — [ROSOrin Pro](rosorin-pro.md) arm + base variant ([Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md), [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)).
- Product line: mobile-only ([ROSOrin](rosorin.md)) plus 6-DOF arm + base ([ROSOrin Pro](rosorin-pro.md)); ships [OpenClaw](openclaw.md) as the manipulation-aware LLM-agent framework on the Pro variant.
- Custom hardware accessories: WonderEcho Pro voice module + 6-microphone circular array; HX-12H bus servos for the arm.
- Curriculum spans cloud LLMs (OpenAI / OpenRouter) and offline runtimes ([Ollama](ollama.md) + [Qwen](qwen.md) + sherpa-onnx).

## Why it matters
Represents the **educational tier** of the agentic-robotics ecosystem — distinct from research platforms like [Stretch](stretch.md). Hiwonder ships a complete LLM-agent demo on its kits, which is meaningful evidence that the [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) (not VLA) is the dominant accessible-robotics approach in 2026.

## Related
- [ROSOrin](rosorin.md) — base mobile-only kit.
- [ROSOrin Pro](rosorin-pro.md) — manipulation-capable sibling.
- [OpenClaw](openclaw.md) — Hiwonder's manipulation LLM-agent framework.
- [Hello Robot](hello-robot.md) — research-tier counterpart vendor.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)

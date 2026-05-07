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

Educational-robotics vendor that builds [[rosorin|ROSOrin]] and other Jetson-based robot kits. Targets STEM education and ROS curricula. Country / founding details not extracted from the docs (Hiwonder is widely known to be a Chinese vendor, but the docs don't confirm).

## What we know
- Two parallel Sphinx documentation sites:
  - `docs.hiwonder.com` — base [[rosorin|ROSOrin]] kit ([[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]).
  - `wiki.hiwonder.com` — [[rosorin-pro|ROSOrin Pro]] arm + base variant ([[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]], [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]).
- Product line: mobile-only ([[rosorin|ROSOrin]]) plus 6-DOF arm + base ([[rosorin-pro|ROSOrin Pro]]); ships [[openclaw|OpenClaw]] as the manipulation-aware LLM-agent framework on the Pro variant.
- Custom hardware accessories: WonderEcho Pro voice module + 6-microphone circular array; HX-12H bus servos for the arm.
- Curriculum spans cloud LLMs (OpenAI / OpenRouter) and offline runtimes ([[ollama|Ollama]] + [[qwen|Qwen]] + sherpa-onnx).

## Why it matters
Represents the **educational tier** of the agentic-robotics ecosystem — distinct from research platforms like [[stretch|Stretch]]. Hiwonder ships a complete LLM-agent demo on its kits, which is meaningful evidence that the [[llm-agent-architecture|LLM-agent pattern]] (not VLA) is the dominant accessible-robotics approach in 2026.

## Related
- [[rosorin|ROSOrin]] — base mobile-only kit.
- [[rosorin-pro|ROSOrin Pro]] — manipulation-capable sibling.
- [[openclaw|OpenClaw]] — Hiwonder's manipulation LLM-agent framework.
- [[hello-robot|Hello Robot]] — research-tier counterpart vendor.

## Mentioned in
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]
- [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]]
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]

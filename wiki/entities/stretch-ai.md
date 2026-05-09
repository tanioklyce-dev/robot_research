---
title: stretch_ai
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-08
sources: 5
tags: [stretch-ai, hello-robot, llm-agent, open-source, mapping]
---

Open-source Python software stack from [Hello Robot](hello-robot.md) for the [Stretch](stretch.md) robot. Layers perception, mapping, navigation, manipulation, and an LLM agent on top of the lower-level `stretch_body` API. GitHub: hello-robot/stretch_ai.

## Capabilities
- **Mapping/exploration**: `stretch.app.mapping` with A*, RRT, and RRT-Connect motion planners.
- **Perception**: head + gripper RealSense cameras with vision-based object detection.
- **Manipulation**: `GraspObjectOperation` via visual servoing.
- **LLM agent** (the agentic centerpiece — see [stretch_ai LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)): turns natural-language goals into tool-call sequences. Backends: Qwen2.5-3B-Instruct (default local), Google Gemma, OpenAI GPT-4o-mini.
- **Tool primitives** the LLM can call: `pickup`, `explore`, `place`, `say`, `wave`, `nod_head`, `find`, `go_home`, etc.

## Why it matters
Most concrete public example of an **LLM-controlled real-robot stack**. Unlike [VLA models](../concepts/vla-models.md) (which learn end-to-end action prediction) or [world-model simulators](../concepts/world-model-simulators.md) (which provide training environments), stretch_ai's LLM agent invokes deterministic perception/manipulation primitives on hardware. This is the "[LLM-agent architecture](../concepts/llm-agent-architecture.md)" pattern in shipped form.

## Related
- [Hello Robot](hello-robot.md) — maintainer.
- [Stretch](stretch.md) — target platform.
- [LLM-agent architecture](../concepts/llm-agent-architecture.md) — design pattern.
- [VLA models](../concepts/vla-models.md) — competing paradigm.

## Mentioned in
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)

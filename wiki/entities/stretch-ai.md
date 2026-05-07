---
title: stretch_ai
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [stretch-ai, hello-robot, llm-agent, open-source, mapping]
---

Open-source Python software stack from [[hello-robot|Hello Robot]] for the [[stretch|Stretch]] robot. Layers perception, mapping, navigation, manipulation, and an LLM agent on top of the lower-level `stretch_body` API. GitHub: hello-robot/stretch_ai.

## Capabilities
- **Mapping/exploration**: `stretch.app.mapping` with A*, RRT, and RRT-Connect motion planners.
- **Perception**: head + gripper RealSense cameras with vision-based object detection.
- **Manipulation**: `GraspObjectOperation` via visual servoing.
- **LLM agent** (the agentic centerpiece — see [[stretch-ai-llm-agent-docs|stretch_ai LLM Agent Documentation]]): turns natural-language goals into tool-call sequences. Backends: Qwen2.5-3B-Instruct (default local), Google Gemma, OpenAI GPT-4o-mini.
- **Tool primitives** the LLM can call: `pickup`, `explore`, `place`, `say`, `wave`, `nod_head`, `find`, `go_home`, etc.

## Why it matters
Most concrete public example of an **LLM-controlled real-robot stack**. Unlike [[vla-models|VLA models]] (which learn end-to-end action prediction) or [[world-model-simulators|world-model simulators]] (which provide training environments), stretch_ai's LLM agent invokes deterministic perception/manipulation primitives on hardware. This is the "[[llm-agent-architecture|LLM-agent architecture]]" pattern in shipped form.

## Related
- [[hello-robot|Hello Robot]] — maintainer.
- [[stretch|Stretch]] — target platform.
- [[llm-agent-architecture|LLM-agent architecture]] — design pattern.
- [[vla-models|VLA models]] — competing paradigm.

## Mentioned in
- [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]

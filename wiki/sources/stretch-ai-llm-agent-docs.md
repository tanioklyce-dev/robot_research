---
title: Stretch AI LLM Agent Documentation
type: source
url: https://github.com/hello-robot/stretch_ai/blob/main/docs/llm_agent.md
author: Hello Robot
published: 2024-2025
ingested: 2026-05-07
tags: [stretch-ai, llm-agent, hello-robot, agentic-robotics, qwen, gpt-4o]
---

## Summary
Documentation for the LLM agent component of [stretch_ai](../entities/stretch-ai.md) — [Hello Robot](../entities/hello-robot.md)'s open-source software stack. Concrete agentic pattern: an LLM converts natural-language goals into a sequence of robot tool calls executed by a deterministic state machine.

## Key claims
- Entry point: `python -m stretch.app.ai_pickup --use_llm`. Internal classes: `PickupExecutor`, `PickupTask` (FSM), `GraspObjectOperation`.
- **Three LLM backends supported**:
  - [qwen25-3B-Instruct](../entities/qwen.md) (default, local, permissively-licensed Alibaba/Qwen model).
  - Google `gemma`.
  - OpenAI GPT-4o-mini (proprietary, via API).
  - **No Anthropic / Claude support listed.**
- Tool interface exposed to the LLM: `pickup(object_name)`, `explore(int)`, `place(location_name)`, `say(text)`, `wave()`, `nod_head()`, `shake_head()`, `avert_gaze()`, `find(object_name)`, `go_home()`, `quit()`.
- Built on the rest of [stretch_ai](../entities/stretch-ai.md): mapping/exploration (A*, RRT, RRT-Connect), grasping via visual servoing, head + gripper RealSense perception.
- Sample task input: "pick up the toy chicken and put it in the white laundry basket."
- Other commands: `python -m stretch.app.grasp_object --target_object "pink plastic cup"`, `python -m stretch.app.mapping --explore-iter 10`, `python -m stretch.app.chat --voice --talk`.
- Hardware reqs: Stretch + GPU computer (RTX 4090-class for local LLMs); ports 4401–4404; Ethernet recommended for ~10 GB model downloads.
- **No VLA, world-model, or simulator integration** — this is a real-robot LLM-agent stack, not a simulation training pipeline.

## Entities mentioned
- [Hello Robot](../entities/hello-robot.md)
- [Stretch](../entities/stretch.md)
- [stretch_ai](../entities/stretch-ai.md)

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md): LLM emits tool calls, deterministic executor runs them.
- [VLA models](../concepts/learning/vla-models.md) (contrast: this is NOT a VLA — it wraps classical perception/manipulation rather than learning end-to-end action prediction).

## Open questions
- Why no Claude / Anthropic backend?
- Closed-loop replanning: does the LLM see skill failures and re-plan, or are tool-call sequences strictly one-shot?
- Comparative success rates across Qwen2.5-3B vs. Gemma vs. GPT-4o-mini on the same tasks?

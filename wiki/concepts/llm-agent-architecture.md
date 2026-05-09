---
title: LLM-agent architecture
type: concept
created: 2026-05-07
updated: 2026-05-09
sources: 5
tags: [llm-agent, tool-use, agentic-robotics, planning, mcp, a2a]
---

**LLM-agent architecture for robots** — a control pattern in which a large language model converts natural-language goals into sequences of tool calls that a deterministic executor runs against perception/manipulation primitives. Distinct from end-to-end [VLA models](vla-models.md) (which output low-level actions directly) and from [world-model simulators](world-model-simulators.md) (which generate the training environment).

## Pattern
1. User states a goal in natural language ("pick up the toy chicken and put it in the basket").
2. LLM is prompted with the goal plus a tool-call schema.
3. LLM emits a sequence of structured calls: `find(toy_chicken)`, `pickup(toy_chicken)`, `place(basket)`, etc.
4. Executor (often a finite-state machine) dispatches each call to a deterministic skill module: navigation, grasping, perception.
5. Skills run on real hardware or in simulation; failures bubble back as observations the LLM can re-plan over.

## Concrete examples
- **[stretch_ai](../entities/stretch-ai.md)'s LLM agent** ([Hello Robot](../entities/hello-robot.md), research tier) — `PickupExecutor` + `PickupTask` FSM, with [Qwen2.5-3B-Instruct](../entities/qwen.md) / Gemma / GPT-4o-mini as the planner ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)). Tool primitives: `pickup`, `explore`, `place`, `say`, `find`, `go_home`, etc.
- **[Hiwonder ROSOrin](../entities/rosorin.md)'s embodied-AI demos** ([Hiwonder](../entities/hiwonder.md), educational tier, mobile-only) — same JSON tool-call pattern: LLM emits `{action: [...], response: ...}`, executor dispatches each call via `eval(f'self.{a}')`. Both cloud (GPT-4o, [Qwen-plus](../entities/qwen.md), StepFun VLM) and offline ([Ollama](../entities/ollama.md) + [qwen3:1.7b](../entities/qwen.md) + sherpa-onnx) variants ([Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)).
- **[OpenClaw](../entities/openclaw.md) on [ROSOrin Pro](../entities/rosorin-pro.md)** ([Hiwonder](../entities/hiwonder.md), educational tier, mobile + 6-DOF arm) — same architecture, manipulation-capable. Skill library expands to include `pick`, `place`, `voice_pick`, `voice_give`, plus AprilTag pickup and depth-based interactive grasping. ROS 2 services like `/start_pick`, `/place`, `/claw_track_and_grab/start` ([Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)).

The pattern is **converging across tiers and capabilities** — research-grade (stretch_ai) and educational (ROSOrin / OpenClaw) stacks adopt the same architecture; mobile-only and arm-equipped variants adopt the same architecture; the only difference is the size and contents of the skill library.

## Inter-agent communication protocols

As LLM agents proliferate, two complementary protocols have emerged to connect them to external resources and to each other:

### MCP — Model Context Protocol
- Developed by **Anthropic**.
- Standard interface for LLMs to access external tools, data sources, cloud storage, financial systems, IoT, and enterprise services.
- **>1,000 community-built connectors** available (as of 2025).
- In a robotics context, MCP is the natural connector layer for an LLM-agent robot to call external APIs (maps, object databases, smart-home systems) without custom integration per tool.

### A2A — Agent-to-Agent Protocol
- Backed by **Google**; **50+ corporate supporters** including Microsoft, Salesforce, and SAP.
- Enables AI agents to discover each other and coordinate — one agent can delegate subtasks to another agent via a standardized handoff.
- Relevant to multi-robot or heterogeneous-fleet architectures where a high-level planner (cloud LLM) delegates to a low-level executor (on-device LLM agent on the robot).

These protocols represent the infrastructure layer that makes "networked AI" — multiple cooperating agents — practical at scale. Primary source: [Are We Building Skynet? (Medium, 2025)](../sources/medium-are-we-building-skynet.md) (secondary journalism; MCP and A2A facts corroborated by Anthropic and Google public documentation).

## Trade-offs vs. VLA
- **Pro**: composes with battle-tested classical perception/manipulation; LLM only needs symbolic-level reasoning.
- **Pro**: easy to swap LLMs (just change the API); easier to debug than end-to-end policies.
- **Con**: action vocabulary is hand-engineered; new skills require new primitives.
- **Con**: closed-loop replanning depends on how cleanly skill failures surface to the LLM.

## Related
- [VLA models](vla-models.md) — competing paradigm (end-to-end action prediction).
- [stretch_ai](../entities/stretch-ai.md) — concrete implementation.
- [World-model simulators](world-model-simulators.md) — orthogonal (training-environment paradigm, not control paradigm).

## Mentioned in
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)
- [Are We Building Skynet? (Medium, 2025)](../sources/medium-are-we-building-skynet.md)

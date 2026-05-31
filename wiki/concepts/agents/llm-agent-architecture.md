---
title: LLM-agent architecture
type: concept
created: 2026-05-07
updated: 2026-05-31
sources: 18
tags: [llm-agent, tool-use, agentic-robotics, planning, mcp, a2a]
---

**LLM-agent architecture for robots** — a control pattern in which a large language model converts natural-language goals into sequences of tool calls that a deterministic executor runs against perception/manipulation primitives. Distinct from end-to-end [VLA models](../learning/vla-models.md) (which output low-level actions directly) and from [world-model simulators](../world-models/world-model-simulators.md) (which generate the training environment).

## Pattern
1. User states a goal in natural language ("pick up the toy chicken and put it in the basket").
2. LLM is prompted with the goal plus a tool-call schema.
3. LLM emits a sequence of structured calls: `find(toy_chicken)`, `pickup(toy_chicken)`, `place(basket)`, etc.
4. Executor (often a finite-state machine) dispatches each call to a deterministic skill module: navigation, grasping, perception.
5. Skills run on real hardware or in simulation; failures bubble back as observations the LLM can re-plan over.

## Concrete examples
- **[stretch_ai](../../entities/stretch-ai.md)'s LLM agent** ([Hello Robot](../../entities/hello-robot.md), research tier) — `PickupExecutor` + `PickupTask` FSM, with [Qwen2.5-3B-Instruct](../../entities/qwen.md) / Gemma / GPT-4o-mini as the planner ([Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md)). Tool primitives: `pickup`, `explore`, `place`, `say`, `find`, `go_home`, etc.
- **[Hiwonder ROSOrin](../../entities/rosorin.md)'s embodied-AI demos** ([Hiwonder](../../entities/hiwonder.md), educational tier, mobile-only) — same JSON tool-call pattern: LLM emits `{action: [...], response: ...}`, executor dispatches each call via `eval(f'self.{a}')`. Both cloud (GPT-4o, [Qwen-plus](../../entities/qwen.md), StepFun VLM) and offline ([Ollama](../../entities/ollama.md) + [qwen3:1.7b](../../entities/qwen.md) + sherpa-onnx) variants ([Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md)).
- **[OpenClaw](../../entities/openclaw.md) on [ROSOrin Pro](../../entities/rosorin-pro.md)** (educational tier, mobile + 6-DOF arm; upstream OpenClaw plus [Hiwonder](../../entities/hiwonder.md)'s [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 bridge module) — same architecture, manipulation-capable. Skill library expands to include `pick`, `place`, `voice_pick`, `voice_give`, plus AprilTag pickup and depth-based interactive grasping. ROS 2 services like `/start_pick`, `/place`, `/claw_track_and_grab/start` ([Hiwonder OpenClaw Practical Tutorial](../../sources/hiwonder-openclaw-tutorial.md)).
- **[Gemini Robotics-ER 1.5](../../entities/gemini-robotics.md) on [Spot](../../entities/spot.md)** ([Boston Dynamics](../../entities/boston-dynamics.md), commercial quadruped tier) — same architecture using a *frontier-grade* multimodal model from [Google DeepMind](../../entities/google-deepmind.md). A thin layer over the Spot SDK exposes `GoTo`, `TakePicture`, object identification, `Pickup`, `PutDown`. Demonstrated cleaning a residential living room from handwritten task lists ("make sure all the shoes at the front door are on the shoe rack") ([Spot + Gemini Robotics blog](../../sources/bostondynamics-spot-gemini-robotics.md)). Productized as Boston Dynamics' AIVI-Learning with ER 1.6.

The pattern is **converging across tiers, capabilities, and price points** — research-grade (stretch_ai), educational (ROSOrin / OpenClaw), and commercial-quadruped-grade (Spot + Gemini Robotics) stacks adopt the same architecture; mobile-only and arm-equipped variants adopt the same architecture; open-weights small LLMs ([Qwen](../../entities/qwen.md) 1.7B / 3B local) and frontier closed-weights VLMs (Gemini Robotics-ER, GPT-4o) plug into the same slot. The only differences are the size and contents of the skill library and the planner model.

> [!note] On naming: Google calls this "embodied reasoning" (Gemini Robotics-**ER**). Functionally it is the LLM-agent / planner-emits-tool-calls pattern documented above. The framing is a vendor branding choice, not a new architecture.

## Non-robotics example: agent-driven ML research

The same control pattern works outside robotics. **[Karpathy's autoresearch (March 2026)](../../sources/karpathy-autoresearch.md)** is the most distilled example in the wiki: an AI coding agent ([Claude Code](../../entities/anthropic.md) or Codex) is pointed at a `program.md` instruction file and given a small but real LLM training pipeline (a simplified [nanochat](../../sources/karpathy-nanochat.md)). The "tool calls" the agent makes are `edit train.py`, `run 5-minute experiment`, `compare val_bpb`, `keep or revert`. Over ~100 overnight iterations, this loop produced **two leaderboard improvements on the nanochat GPT-2 speedrun** (rows 5–6: 2.02 → 1.80 → 1.65 hours wall-clock), the first public evidence that a coding-agent loop can produce measurable improvements on a frontier ML training pipeline.

The robotics variant of the pattern uses `find / pickup / place` tool primitives over a perception+manipulation skill library; autoresearch uses `edit / train / measure / commit` tool primitives over a training pipeline. **Same control flow, different action vocabulary.** The pattern's robustness across these very different domains is one of the strongest signals that "LLM-emits-actions-against-a-skill-library" is a load-bearing architectural primitive of 2026 AI systems, not a robotics-specific trick.

The [Onchain AI Garage LeWM reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md) is an independent occurrence of the same pattern applied to a different ML target (reproducing a JEPA world model), supporting the same generality claim.

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

These protocols represent the infrastructure layer that makes "networked AI" — multiple cooperating agents — practical at scale. Primary source: [Are We Building Skynet? (Medium, 2025)](../../sources/medium-are-we-building-skynet.md) (secondary journalism; MCP and A2A facts corroborated by Anthropic and Google public documentation).

## Trade-offs vs. VLA
- **Pro**: composes with battle-tested classical perception/manipulation; LLM only needs symbolic-level reasoning.
- **Pro**: easy to swap LLMs (just change the API); easier to debug than end-to-end policies.
- **Con**: action vocabulary is hand-engineered; new skills require new primitives.
- **Con**: closed-loop replanning depends on how cleanly skill failures surface to the LLM.

## Related
- [VLA models](../learning/vla-models.md) — competing paradigm (end-to-end action prediction).
- [stretch_ai](../../entities/stretch-ai.md) — concrete implementation.
- [World-model simulators](../world-models/world-model-simulators.md) — orthogonal (training-environment paradigm, not control paradigm).
- [AI safety and alignment](../safety/ai-safety-alignment.md) — safety properties of the LLM brain matter when it has real-world tool access via MCP.

## Mentioned in
- [Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md)
- [Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md)
- [Hiwonder OpenClaw Practical Tutorial](../../sources/hiwonder-openclaw-tutorial.md)
- [Are We Building Skynet? (Medium, 2025)](../../sources/medium-are-we-building-skynet.md)
- [Tools for Your To Do List with Spot and Gemini Robotics (Boston Dynamics blog)](../../sources/bostondynamics-spot-gemini-robotics.md)

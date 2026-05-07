---
title: LLM-agent architecture
type: concept
created: 2026-05-07
updated: 2026-05-07
sources: 3
tags: [llm-agent, tool-use, agentic-robotics, planning]
---

**LLM-agent architecture for robots** — a control pattern in which a large language model converts natural-language goals into sequences of tool calls that a deterministic executor runs against perception/manipulation primitives. Distinct from end-to-end [[vla-models|VLA models]] (which output low-level actions directly) and from [[world-model-simulators|world-model simulators]] (which generate the training environment).

## Pattern
1. User states a goal in natural language ("pick up the toy chicken and put it in the basket").
2. LLM is prompted with the goal plus a tool-call schema.
3. LLM emits a sequence of structured calls: `find(toy_chicken)`, `pickup(toy_chicken)`, `place(basket)`, etc.
4. Executor (often a finite-state machine) dispatches each call to a deterministic skill module: navigation, grasping, perception.
5. Skills run on real hardware or in simulation; failures bubble back as observations the LLM can re-plan over.

## Concrete examples
- **[[stretch-ai|stretch_ai]]'s LLM agent** ([[hello-robot|Hello Robot]], research tier) — `PickupExecutor` + `PickupTask` FSM, with [[qwen|Qwen2.5-3B-Instruct]] / Gemma / GPT-4o-mini as the planner ([[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]). Tool primitives: `pickup`, `explore`, `place`, `say`, `find`, `go_home`, etc.
- **[[rosorin|Hiwonder ROSOrin]]'s embodied-AI demos** ([[hiwonder|Hiwonder]], educational tier, mobile-only) — same JSON tool-call pattern: LLM emits `{action: [...], response: ...}`, executor dispatches each call via `eval(f'self.{a}')`. Both cloud (GPT-4o, [[qwen|Qwen-plus]], StepFun VLM) and offline ([[ollama|Ollama]] + [[qwen|qwen3:1.7b]] + sherpa-onnx) variants ([[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]).
- **[[openclaw|OpenClaw]] on [[rosorin-pro|ROSOrin Pro]]** ([[hiwonder|Hiwonder]], educational tier, mobile + 6-DOF arm) — same architecture, manipulation-capable. Skill library expands to include `pick`, `place`, `voice_pick`, `voice_give`, plus AprilTag pickup and depth-based interactive grasping. ROS 2 services like `/start_pick`, `/place`, `/claw_track_and_grab/start` ([[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]).

The pattern is **converging across tiers and capabilities** — research-grade (stretch_ai) and educational (ROSOrin / OpenClaw) stacks adopt the same architecture; mobile-only and arm-equipped variants adopt the same architecture; the only difference is the size and contents of the skill library.

## Trade-offs vs. VLA
- **Pro**: composes with battle-tested classical perception/manipulation; LLM only needs symbolic-level reasoning.
- **Pro**: easy to swap LLMs (just change the API); easier to debug than end-to-end policies.
- **Con**: action vocabulary is hand-engineered; new skills require new primitives.
- **Con**: closed-loop replanning depends on how cleanly skill failures surface to the LLM.

## Related
- [[vla-models|VLA models]] — competing paradigm (end-to-end action prediction).
- [[stretch-ai|stretch_ai]] — concrete implementation.
- [[world-model-simulators|World-model simulators]] — orthogonal (training-environment paradigm, not control paradigm).

## Mentioned in
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]

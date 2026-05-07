---
title: LLM-agent architecture across stacks — a converged pattern
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [llm-agent, agentic-robotics, stretch-ai, rosorin, openclaw, qwen]
---

# LLM-agent architecture across stacks — a converged pattern

Three independent agentic-robotics stacks ingested into this wiki — [[stretch-ai|stretch_ai]] (research tier, [[hello-robot|Hello Robot]]), [[rosorin|ROSOrin]] (educational tier, [[hiwonder|Hiwonder]], mobile-only), and [[openclaw|OpenClaw]] (educational tier, Hiwonder, mobile + 6-DOF arm) — converge on the same control architecture: **a small LLM emits structured tool calls; a deterministic executor dispatches each call to a hand-written perception/manipulation skill**. Same shape across two vendors, two price points, and two capability classes. This page consolidates the evidence and draws the structural implications.

The umbrella concept is on [[llm-agent-architecture|LLM-agent architecture]]; this synthesis is the comparative cross-section.

## The shared shape

```
natural language goal
        │
        ▼
   ┌─────────┐    tool-call schema (JSON / Python signature)
   │   LLM   │◀────────────────────────────────────────────
   └─────────┘
        │
        ▼
[{action: "pickup", args: {...}}, {action: "place", args: {...}}, ...]
        │
        ▼
   ┌─────────────┐
   │  Executor   │  (FSM in stretch_ai; eval(f'self.{a}') in ROSOrin / OpenClaw)
   └─────────────┘
        │
        ▼
   skill library  →  ROS 2 / direct hardware  →  robot
```

What every stack ships:
1. A **prompt template** describing available skills as the LLM's tool surface.
2. A **deterministic dispatcher** that consumes structured LLM output and runs skills in order.
3. A **skill library** of classical perception, navigation, and (sometimes) manipulation primitives.
4. A **failure path** where skill outcomes are observable to the LLM for re-planning — though in practice this is the weakest, most under-documented part of every stack.

## Three implementations side by side

| Dimension | [[stretch-ai|stretch_ai]] | [[rosorin|ROSOrin]] | [[openclaw|OpenClaw]] |
|---|---|---|---|
| Vendor | [[hello-robot|Hello Robot]] | [[hiwonder|Hiwonder]] | [[hiwonder|Hiwonder]] |
| Tier | Research | Educational | Educational |
| Hardware | [[stretch|Stretch 3]] mobile manipulator | Jetson Orin Nano + diff-drive base | Jetson Orin Nano + 6-DOF arm + base |
| Default local LLM | [[qwen|Qwen2.5-3B-Instruct]] | [[qwen|qwen3:1.7b]] via [[ollama|Ollama]] | (cloud-first; OpenAI GPT) |
| Cloud LLMs supported | GPT-4o-mini, Gemma | GPT-4o, GPT-4o-mini, Qwen-plus, StepFun VLM | OpenAI GPT (`openai/gpt-5.4` per docs) |
| ASR / TTS | Whisper / OS TTS | OpenAI ASR + sherpa-onnx (offline) | (inherits ROSOrin stack) |
| Tool-call format | Python function signatures (`pickup(object_name)`, `place(location_name)`, ...) | JSON `{action: [...], response: ...}` | JSON over ROS 2 services |
| Executor | `PickupExecutor` + `PickupTask` FSM | `eval(f'self.{a}')` per action | `eval`-style dispatch + ROS 2 services |
| Skill primitives | `pickup`, `place`, `find`, `explore`, `say`, `wave`, `nod_head`, `go_home` | `move`, `vision(query)`, chassis controls | `voice_pick`, `voice_give`, `/start_pick`, `/place`, `/claw_track_and_grab/start`, AprilTag pickup, depth-based grasping |
| Manipulation? | Visual-servoing grasp | None (mobile-only) | Yes — full pick/place + tracking |
| Simulation integrated? | None — real robot only | Gazebo (separate curriculum) | Gazebo (separate curriculum) |
| Source | [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]] | [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]] | [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]] |

## What converges (and why it matters)

**1. Small open-weights Qwen as the default planner.** stretch_ai defaults to Qwen2.5-3B-Instruct; ROSOrin's offline curriculum defaults to qwen3:1.7b. Two unrelated vendors, two unrelated codebases — same model family. The convergence is consistent with the fact that small Qwen variants are the only open-weights LLMs that fit a Jetson-class device while still being competent at structured output. **Implication:** a robotics stack that wants offline / on-device LLM agency in 2026 has effectively one practical default.

**2. JSON-shaped tool-call schemas, not native function-calling APIs.** Every stack hand-rolls its tool schema (Python signatures or JSON `{action, response}`) rather than relying on any specific provider's function-calling syntax. This buys provider-portability — swapping GPT-4o-mini for Qwen for Gemma costs only a prompt edit. **Implication:** robotics LLM-agent stacks are insulated from vendor-specific tool-calling APIs and treat the LLM as fungible.

**3. Skills live below the LLM, not inside it.** None of the three stacks asks the LLM to do perception or low-level control — vision is YOLO/MediaPipe/AprilTag/visual-servoing, navigation is Nav2/A*/RRT, grasping is classical or learned BC. The LLM is constrained to symbolic reasoning over a fixed action vocabulary. **Implication:** these are not VLA stacks (see "What's notably absent" below); they are classical robotics with an LLM dispatcher bolted on top.

**4. The pattern scales from mobile-only to mobile + arm without architectural change.** Comparing ROSOrin to OpenClaw: same vendor, same compute, same dispatcher pattern; OpenClaw simply adds manipulation primitives to the skill library. **Implication:** the architecture absorbs new capabilities by extending the skill library rather than re-architecting the controller.

## What's notably absent across all three stacks

- **No VLA models.** No OpenVLA, no [[nvidia-groot|GR00T]], no Pi π0, no RT-X. The LLM-agent path and the [[vla-models|VLA]] path do not coexist in any of these stacks.
- **No imitation learning, teleoperation, or demonstration collection** in stretch_ai's LLM agent or in either Hiwonder stack. (stretch_ai's *broader* repo includes BC and dexterous-teleop work, but the LLM agent doesn't touch it.)
- **No LeRobot, ACT, or Diffusion Policy** anywhere in the deployed agent flow.
- **No simulator in the agent loop.** Gazebo curricula exist alongside the LLM-agent demos in Hiwonder docs but are taught as separate chapters; the agent itself runs on real hardware.

This absence is the most important structural fact this synthesis can offer: **there is a clear bifurcation in 2026 between research VLA work and deployed agentic robotics**. VLA happens in NVIDIA / Meta / Pi / Skild research stacks running on simulators ([[nvidia-isaac-lab|Isaac Lab]], [[mujoco-playground|MuJoCo Playground]], [[agibot-genie-sim|Genie Sim]], [[robocasa|RoboCasa]]). Deployed agentic stacks running on real customers' robots use LLM-orchestrated classical skill libraries. The two paths do not yet meet in any stack ingested here.

## Trade-offs vs VLA

| Axis | LLM-agent pattern | VLA |
|---|---|---|
| Action vocabulary | Hand-engineered, symbolic | Learned, continuous |
| New skills | Add primitives + update prompt | Re-train policy |
| Failure debugging | Inspect tool calls and skill logs | Opaque end-to-end |
| Compute (inference) | LLM call + classical skills (modest) | Large policy forward pass + sim/real loop |
| Closed-loop reactivity | Limited by prompt-cycle latency | Frame-rate possible |
| Generalization to unseen objects | Bounded by skill library | Can transfer with right pretraining |
| Sim-to-real burden | None (no policy to transfer) | High (the entire sim category 1 stack exists for this) |
| Production readiness | Shipping today (stretch_ai, OpenClaw) | Mostly research |

The LLM-agent pattern wins on shippability and debuggability today. VLAs win on data-driven generalization in the limit — but only if the training pipeline (sim, data, evaluation) is in place.

## Implementation hazards visible in the sources

> [!warning] `eval`-on-LLM-output as a dispatch mechanism
> Both Hiwonder stacks dispatch via `eval(f'self.{a}')` on LLM-emitted strings ([[hiwonder-rosorin-docs|ROSOrin docs]], [[hiwonder-openclaw-tutorial|OpenClaw tutorial]]). This is fine for an educational kit on a closed local network, but it is a remote-code-execution vector if the LLM endpoint is ever attacker-influenced. stretch_ai's FSM dispatcher does not have this property. Worth flagging if any of these patterns are copied into production.

> [!note] Closed-loop replanning is under-documented everywhere
> All three sources describe how the LLM emits a plan. None describe in detail how skill failures (grasp failure, person blocking the path, AprilTag occluded) surface back to the LLM for re-planning. This is the most consequential gap between published demo behavior and robust deployment.

## Open questions

- **Why does no stack support Claude as an LLM backend?** stretch_ai lists Qwen, Gemma, GPT-4o-mini explicitly with no Anthropic option ([[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]). Worth investigating whether this is licensing, pricing, or simply that the Hello Robot team hasn't gotten to it.
- **Cross-vendor portability**: could OpenClaw's skill library run on a Stretch, or vice versa? Both expose ROS 2 surfaces in principle. No source addresses this.
- **What does the `voice_pick` / `voice_give` action group actually contain in OpenClaw?** The doc names them but does not list the joint trajectories — implementation is opaque without the source repo.
- **Will this pattern hold once VLAs ship into deployed products?** A VLA could in principle replace several skills in the library while leaving the LLM dispatcher above. This synthesis predicts the LLM-as-orchestrator-over-classical-skills pattern survives, with VLAs gradually moving in as individual primitives.

## Sources used in this synthesis

- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]
- [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]] (hardware context for OpenClaw)

## Related

- [[llm-agent-architecture|LLM-agent architecture]] — the umbrella concept page.
- [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] — section 6 covers the same real-robot stacks at a survey level; this page is the deeper comparison.
- [[vla-models|VLA models]] — the contrasting paradigm.

---
title: LLM-agent architecture across stacks — a converged pattern, and where it diverges
type: synthesis
created: 2026-05-07
updated: 2026-08-13
tags: [llm-agent, agentic-robotics, stretch-ai, rosorin, openclaw, qwen, dimos, mcp, langgraph]
---

# LLM-agent architecture across stacks — a converged pattern, and where it diverges

Three independent agentic-robotics stacks ingested into this wiki — [stretch_ai](../../entities/stretch-ai.md) (research tier, [Hello Robot](../../entities/hello-robot.md)), [ROSOrin](../../entities/rosorin.md) (educational tier, [Hiwonder](../../entities/hiwonder.md), mobile-only), and [OpenClaw](../../entities/openclaw.md) on the [ROSOrin Pro](../../entities/rosorin-pro.md) (educational tier; upstream OpenClaw plus Hiwonder's [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 bridge module, mobile + 6-DOF arm) — converge on the same control architecture: **a small LLM emits structured tool calls; a deterministic executor dispatches each call to a hand-written perception/manipulation skill**. Same shape across two vendors, two price points, and two capability classes. This page consolidates the evidence and draws the structural implications.

The umbrella concept is on [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md); this synthesis is the comparative cross-section.

> [!warning] Revised 2026-08-13 — a fourth stack, and two convergences that don't hold
> **[DimOS](../../entities/dimos.md)** ([Dimensional Inc.](../../entities/dimensional-inc.md), [repo](../../sources/dimos-github.md)) is the same architecture at **3,874 stars and 12+ contributors** — an order of magnitude larger than anything above, and the first industrial-scale instance of the pattern. It confirms the shared shape and **falsifies two of the four convergences below** (small-Qwen default; hand-rolled JSON tool schemas). It also **partly closes the bifurcation** this page called its most important structural finding. Original three-stack analysis retained below; DimOS is added to the table and each affected claim is annotated inline.

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

| Dimension | [stretch_ai](../../entities/stretch-ai.md) | [ROSOrin](../../entities/rosorin.md) | [OpenClaw](../../entities/openclaw.md) on ROSOrin Pro |
|---|---|---|---|
| Vendor / origin | [Hello Robot](../../entities/hello-robot.md) | [Hiwonder](../../entities/hiwonder.md) | OpenClaw: Steinberger / community; ROS 2 bridge ([`openclaw_controller`](../../entities/openclaw-controller.md)): [Hiwonder](../../entities/hiwonder.md) |
| Tier | Research | Educational | Educational |
| Hardware | [Stretch 3](../../entities/stretch.md) mobile manipulator | Jetson Orin Nano + diff-drive base | Jetson Orin Nano + 6-DOF arm + base |
| Default local LLM | [Qwen2.5-3B-Instruct](../../entities/qwen.md) | [qwen3:1.7b](../../entities/qwen.md) via [Ollama](../../entities/ollama.md) | (cloud-first; OpenAI GPT) |
| Cloud LLMs supported | GPT-4o-mini, Gemma | GPT-4o, GPT-4o-mini, Qwen-plus, StepFun VLM | OpenAI GPT (`openai/gpt-5.4` per docs) |
| ASR / TTS | Whisper / OS TTS | OpenAI ASR + sherpa-onnx (offline) | (inherits ROSOrin stack) |
| Tool-call format | Python function signatures (`pickup(object_name)`, `place(location_name)`, ...) | JSON `{action: [...], response: ...}` | JSON over ROS 2 services |
| Executor | `PickupExecutor` + `PickupTask` FSM | `eval(f'self.{a}')` per action | `eval`-style dispatch + ROS 2 services |
| Skill primitives | `pickup`, `place`, `find`, `explore`, `say`, `wave`, `nod_head`, `go_home` | `move`, `vision(query)`, chassis controls | `voice_pick`, `voice_give`, `/start_pick`, `/place`, `/claw_track_and_grab/start`, AprilTag pickup, depth-based grasping |
| Manipulation? | Visual-servoing grasp | None (mobile-only) | Yes — full pick/place + tracking |
| Simulation integrated? | None — real robot only | Gazebo (separate curriculum) | Gazebo (separate curriculum) |
| Source | [Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md) | [Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md) | [Hiwonder OpenClaw Practical Tutorial](../../sources/hiwonder-openclaw-tutorial.md) |

### The fourth stack: DimOS

| Dimension | [DimOS](../../entities/dimos.md) |
|---|---|
| Vendor / origin | [Dimensional Inc.](../../entities/dimensional-inc.md); Apache 2.0; 3,874★ / 788 forks / 12+ contributors |
| Tier | Commercial open-core, pre-release beta (`0.0.14b1`) |
| Hardware | [Unitree Go2](../../entities/unitree-go2.md) 🟩, [G1](../../entities/unitree-g1.md) 🟨, [xArm](../../entities/xarm-7.md) 🟨, [AgileX Piper](../../entities/agilex-piper.md) 🟨, MAVLink/DJI 🟧, Unitree B1 🟥 |
| Default LLM | **`gpt-5.6-luna` (cloud)** — [Ollama](../../entities/ollama.md) as an alternate blueprint |
| Tool-call format | **MCP** (`McpServer` / `McpClient`) over **LangGraph** |
| Executor | Skills dispatched as RPC calls on deployed Modules |
| Skill definition | **`@skill` decorator; discovered automatically by RPC introspection at agent startup, docstring becomes the tool description** |
| Skill primitives | `relative_move`, `execute_sport_command`, `observe`, `navigate_with_text`, `tag_location`, `follow_person`, `speak`, `where_am_i`, `set_gps_travel_points`, `map_query` |
| Manipulation? | Yes — Drake planning, xArm + Piper, Quest VR teleop |
| Simulation integrated? | **Yes — [MuJoCo](../../entities/mujoco.md) in the same CLI** (`dimos --simulation run ...`), plus a replay mode that runs the full stack on recorded data |
| Imitation learning? | **Yes — Quest teleop → `dimos dataprep` → [LeRobot](../../entities/lerobot.md) v3.0 / HDF5** |
| Source | [DimOS GitHub repository](../../sources/dimos-github.md) |

## What converges (and why it matters)

> [!warning] Convergences 1 and 2 do not survive DimOS
> Both were inferences from three stacks that shared a constraint — Jetson-class hardware and no protocol standard to lean on. DimOS has neither constraint (it wants an RTX 4070 or an AGX Orin, and MCP now exists), and it makes the opposite choice on both. Read 1 and 2 below as **true of the on-device educational/research tier, not of the pattern**. Convergences 3 and 4 hold across all four stacks.

**1. Small open-weights Qwen as the default planner.** stretch_ai defaults to Qwen2.5-3B-Instruct; ROSOrin's offline curriculum defaults to qwen3:1.7b. Two unrelated vendors, two unrelated codebases — same model family. The convergence is consistent with the fact that small Qwen variants are the only open-weights LLMs that fit a Jetson-class device while still being competent at structured output. **Implication:** a robotics stack that wants offline / on-device LLM agency in 2026 has effectively one practical default. **Revision (2026-08-13):** the implication is intact but its scope is narrower than stated — it holds for stacks *targeting on-device inference*. [DimOS](../../entities/dimos.md) defaults to cloud `gpt-5.6-luna`, treats [Ollama](../../entities/ollama.md) as an alternate blueprint, and lists an **RTX 3000+ / 8 GB VRAM minimum with Orin Nano marked experimental**. Stacks that assume a workstation or an AGX Orin are not forced into small-Qwen at all.

**2. JSON-shaped tool-call schemas, not native function-calling APIs.** Every stack hand-rolls its tool schema (Python signatures or JSON `{action, response}`) rather than relying on any specific provider's function-calling syntax. This buys provider-portability — swapping GPT-4o-mini for Qwen for Gemma costs only a prompt edit. **Implication:** robotics LLM-agent stacks are insulated from vendor-specific tool-calling APIs and treat the LLM as fungible. **Revision (2026-08-13):** [DimOS](../../entities/dimos.md) reaches the same goal by the opposite route — it standardizes on **MCP**, an open protocol, with LangGraph above it. The 2026 answer to provider lock-in turns out to be *adopt the open standard*, not *avoid all standards*. The underlying property (LLM is fungible) survives; the mechanism does not generalize.

**3. Skills live below the LLM, not inside it.** *(Holds in DimOS too — perception is Ultralytics/Moondream/[Florence-2](../../entities/florence-2.md), navigation is voxel-map + A* + GTSAM pose-graph optimization, manipulation is Drake. The LLM only calls skills.)* None of the three stacks asks the LLM to do perception or low-level control — vision is YOLO/MediaPipe/AprilTag/visual-servoing, navigation is Nav2/A*/RRT, grasping is classical or learned BC. The LLM is constrained to symbolic reasoning over a fixed action vocabulary. **Implication:** these are not VLA stacks (see "What's notably absent" below); they are classical robotics with an LLM dispatcher bolted on top.

**4. The pattern scales from mobile-only to mobile + arm without architectural change.** *(DimOS is the strongest evidence yet: one module/blueprint abstraction spans quadruped, humanoid, two arm families, and drones, with new capability added as decorated methods.)* Comparing ROSOrin to the ROSOrin Pro's OpenClaw + `openclaw_controller` setup: same vendor packaging the kit, same compute, same dispatcher pattern; the Pro simply adds manipulation primitives to the skill library (via `openclaw_controller`). **Implication:** the architecture absorbs new capabilities by extending the skill library rather than re-architecting the controller.

## What's notably absent across all three stacks

- **No VLA models.** No OpenVLA, no [GR00T](../../entities/nvidia-groot.md), no Pi π0, no RT-X. The LLM-agent path and the [VLA](../../concepts/learning/vla-models.md) path do not coexist in any of these stacks.
- **No imitation learning, teleoperation, or demonstration collection** in stretch_ai's LLM agent or in either Hiwonder stack. (stretch_ai's *broader* repo includes BC and dexterous-teleop work, but the LLM agent doesn't touch it.)
- **No LeRobot, ACT, or Diffusion Policy** anywhere in the deployed agent flow.
- **No simulator in the agent loop.** Gazebo curricula exist alongside the LLM-agent demos in Hiwonder docs but are taught as separate chapters; the agent itself runs on real hardware.

> [!warning] DimOS breaks three of these four absences — but not the load-bearing one
> - **Imitation learning / teleoperation / demonstration collection**: present. `dimos/imitation` records Quest-teleop episodes to a session DB with hold-to-engage, toggle-record, and discard controls.
> - **LeRobot**: present. **`dimos dataprep` exports to [LeRobot](../../entities/lerobot.md) v3.0** (`data/episodes` parquet + task-indexed `tasks.parquet`) or HDF5.
> - **Simulator in the loop**: present. [MuJoCo](../../entities/mujoco.md) runs from the same CLI as hardware (`dimos --simulation run unitree-g1-sim`), plus a replay mode that drives the full SLAM/costmap/planning stack from recorded sessions.
> - **VLA models**: **still absent.** No π0, GR00T, OpenVLA, ACT, or SmolVLA anywhere in the repository. Nothing learned runs in the control path.
>
> So the correct 2026-08 statement is narrower and more interesting than the original: **the two paths now share a data format, not a control path.** DimOS is a *producer* for the VLA pipeline — it manufactures LeRobot datasets — while its own robot is driven by an LLM calling classical skills. The bifurcation moved from "these worlds do not touch" to "these worlds exchange data and not policies."

This absence is the most important structural fact this synthesis can offer: **there is a clear bifurcation in 2026 between research VLA work and deployed agentic robotics**. VLA happens in NVIDIA / Meta / Pi / Skild research stacks running on simulators ([Isaac Lab](../../entities/nvidia-isaac-lab.md), [MuJoCo Playground](../../entities/mujoco-playground.md), [Genie Sim](../../entities/agibot-genie-sim.md), [RoboCasa](../../entities/robocasa.md)). Deployed agentic stacks running on real customers' robots use LLM-orchestrated classical skill libraries. The two paths do not yet meet in any stack ingested here.

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
| Production readiness | Shipping today (stretch_ai, OpenClaw + `openclaw_controller`) | Mostly research |

The LLM-agent pattern wins on shippability and debuggability today. VLAs win on data-driven generalization in the limit — but only if the training pipeline (sim, data, evaluation) is in place.

## Implementation hazards visible in the sources

> [!warning] `eval`-on-LLM-output as a dispatch mechanism
> Both Hiwonder kits dispatch via `eval(f'self.{a}')` on LLM-emitted strings ([ROSOrin docs](../../sources/hiwonder-rosorin-docs.md), [OpenClaw tutorial](../../sources/hiwonder-openclaw-tutorial.md)) — on the ROSOrin Pro this dispatch sits inside `openclaw_controller`. This is fine for an educational kit on a closed local network, but it is a remote-code-execution vector if the LLM endpoint is ever attacker-influenced. stretch_ai's FSM dispatcher does not have this property. Worth flagging if any of these patterns are copied into production.

> [!note] DimOS avoids the `eval` hazard by construction
> Skills are RPC calls to typed methods whose parameters must be JSON-serializable primitives, dispatched through MCP — there is no string that gets `eval`'d. This is what the educational kits should be copying. It does introduce a different surface: `McpServer` exposes every `@skill` on the robot to any MCP client that can reach it, so the security question moves from *code injection* to *network exposure and authentication of the MCP endpoint*, which the docs do not discuss.

> [!note] Closed-loop replanning is under-documented everywhere
> All four stacks describe how the LLM emits a plan. None describe in detail how skill failures (grasp failure, person blocking the path, AprilTag occluded) surface back to the LLM for re-planning. This is the most consequential gap between published demo behavior and robust deployment.

## Open questions

- **Why does no stack support Claude as an LLM backend?** stretch_ai lists Qwen, Gemma, GPT-4o-mini explicitly with no Anthropic option ([Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md)). Worth investigating whether this is licensing, pricing, or simply that the Hello Robot team hasn't gotten to it.
- **Cross-vendor portability**: could `openclaw_controller`'s skill library run on a Stretch, or vice versa? Both expose ROS 2 surfaces in principle. No source addresses this.
- **What do the `voice_pick` / `voice_give` action groups actually contain in `openclaw_controller`?** The doc names them but does not list the joint trajectories — implementation is opaque without the source repo.
- **Does anything measure any of this?** Four stacks, zero published success rates. DimOS is the starkest case: 3,874 stars, ten built-in skills, five hardware classes, and **no benchmark, latency, or success-rate number anywhere in the repository**. The pattern's shippability advantage over VLAs (below) rests entirely on the absence of measurement on both sides.
- **Does skill discovery scale past a handful of skills?** DimOS's `@skill`-by-RPC-introspection removes manifest drift, but it also means the agent's tool list is whatever happens to be deployed. With ten skills that is a feature; at a hundred it becomes a context-window and tool-selection problem that none of these stacks has hit yet.
- **Will this pattern hold once VLAs ship into deployed products?** A VLA could in principle replace several skills in the library while leaving the LLM dispatcher above. This synthesis predicts the LLM-as-orchestrator-over-classical-skills pattern survives, with VLAs gradually moving in as individual primitives.

## Sources used in this synthesis

- [Stretch AI LLM Agent Documentation](../../sources/stretch-ai-llm-agent-docs.md)
- [Hiwonder ROSOrin Documentation](../../sources/hiwonder-rosorin-docs.md)
- [Hiwonder OpenClaw Practical Tutorial](../../sources/hiwonder-openclaw-tutorial.md)
- [Hiwonder ROSOrin Pro User Manual](../../sources/hiwonder-rosorin-pro-user-manual.md) (hardware context for OpenClaw)
- [DimOS GitHub repository](../../sources/dimos-github.md) (added 2026-08-13)

## Related

- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — the umbrella concept page.
- [Simulators for agentic robotics — 2026 landscape](../simulators/simulators-for-agentic-robotics-2026.md) — section 6 covers the same real-robot stacks at a survey level; this page is the deeper comparison.
- [VLA models](../../concepts/learning/vla-models.md) — the contrasting paradigm.
- [DimOS](../../entities/dimos.md) / [Dimensional Inc.](../../entities/dimensional-inc.md) — the fourth stack.
- [Waddle Labs](../../entities/waddle-labs.md) — the same thesis as DimOS, argued without a codebase.

---
title: Fleet agentic control framework — LeRobot + ROS 2 + on-edge Gemma + DGX Spark master control
type: synthesis
created: 2026-07-04
updated: 2026-07-05
tags: [project-scope, fleet, agentic-robotics, lerobot, ros2, rosetta, gemma4, dgx-spark, mcp, a2a, async-inference, hil-serl, xlerobot, lekiwi, rosorin-pro, stt-tts, multi-robot]
---

# Fleet agentic control framework — LeRobot + ROS 2 + on-edge Gemma + DGX Spark master control

> [!note] Reference architecture (public)
> This page is the **general reference architecture**. The detailed, fleet-specific
> execution plan — device configs, network topology, calibration, build sequencing —
> is maintained separately.

A concrete scope for **one framework deployed across a heterogeneous robot fleet**, integrated with both **[ROS 2](../../entities/ros2.md)** and **[LeRobot](../../entities/lerobot.md)**, that (a) collects demonstrations and streams them to Hugging Face, (b) trains on a central **[DGX Spark](../../entities/dgx-spark.md)** with minimal human interaction, (c) lets the robots coordinate under a **master control AI on the Spark**, and (d) does on-device speech I/O. Target model family: **[Gemma 4](../../entities/gemma4.md)** (E4B on the edge, larger variants on the Spark).

## The fleet

| Node | Base | Arm(s) | Compute | Class |
|---|---|---|---|---|
| **[XLeRobot](../../entities/xlerobot.md)** | 2-wheel differential‡ | 2× [SO-ARM101](../../entities/so-arm101.md) (FeeTech STS3215) | Jetson **Orin NX 16 GB** | LeRobot-native |
| **[LeKiwi](../../entities/lekiwi.md)** | 3-wheel holonomic Kiwi | 1× [SO-ARM101](../../entities/so-arm101.md) (FeeTech STS3215) | Jetson **Orin NX 16 GB** (planned; supersedes RPi5+Hailo) | LeRobot-native |
| **[ROSOrin Pro](../../entities/rosorin-pro.md)** | mecanum (holonomic)† | 1× [SO-ARM101](../../entities/so-arm101.md) *(swapped from HX-12H — see below)* | Jetson **Orin Nano Super 8 GB** | LeRobot-native (post-swap) |
| **[DGX Spark](../../entities/dgx-spark.md)** | — | — | GB10, 128 GB unified | Central hub |

> [!note] The Orin NX upgrade homogenizes the edge
> With an Orin NX 16 GB on the LeKiwi, **all three robots are first-class CUDA policy nodes** and the earlier hard constraint — **[Hailo NPUs cannot run LeRobot control policies](../../entities/hailo.md#relevance-in-this-wiki-npu-vs-jetson-for-xlerobot)** — no longer blocks anything. The RPi5 + Hailo-10H can stay on the LeKiwi as an **optional speech/vision coprocessor** (its `gen_ai_apps` do STT/VLM well) or be retired; the Orin NX is now the LeKiwi's AI brain.

> [!note] ‡ Three different base drives — and it doesn't matter for the policy
> The fleet's bases are **all different**: XLeRobot **2-wheel differential** (non-holonomic), LeKiwi **3-wheel holonomic Kiwi**, ROSOrin Pro **4-wheel mecanum** (holonomic). This is **irrelevant to the shared manipulation policy** — base drive is the [Nav2](../../entities/nav2.md) layer, below the policy line; the policy sees arm joints + camera views, not base kinematics, and Nav2 is per-robot regardless. The *one* consequence is **pre-grasp positioning**: the holonomic bases can strafe sideways to fine-align before a grasp, whereas the differential XLeRobot must turn-then-approach — so its MCP `navigate_to` should target a grasp-ready pose head-on rather than "get close then align." A behavior/config difference, not a blocker.
>
> A dual-arm XLeRobot build carries **2 wrist cams + a mast/head cam** — already the
> [camera-parity](fleet-framework-implementation-notes.md#camera-parity-spec) layout — on a
> 2-wheel differential base (the [XLeRobot entity](../../entities/xlerobot.md) lists a 2-wheel variant).

> [!tip] Arm-swap homogenization — the decision that collapses the fleet to one embodiment
> Rather than solve **[SO-ARM101↔HX-12H cross-embodiment transfer](fleet-framework-implementation-notes.md#cross-embodiment-shortcut)** (an open ML problem), **replace the ROSOrin Pro's HX-12H arm with an [SO-ARM101](../../entities/so-arm101.md)**. Then *all three robots share the same arm* → **the two single-arm robots (LeKiwi + ROSOrin) share one checkpoint, and XLeRobot co-trains a dual-arm checkpoint off the same pooled SO-ARM101 data** (dual-arm ⇒ 2× the joints + a second wrist cam, so it can't be the *same* checkpoint — see [camera parity](fleet-framework-implementation-notes.md#camera-parity-spec)). The [servo-lineage gap](lerobot-on-rosorin-pro.md#gap-1-motor-sdk-lineage-feetech-dynamixel-hx-12h) disappears and the ROSOrin Pro moves into the LeRobot-native class. You keep its genuinely valuable part — the **finished Nav2 + SLAM + LiDAR nav stack** — and retire only the arm.
>
> The SO-101 is the **same reach class** as the HX-12H arm — no meaningful reach loss for tabletop/floor tidy — and its **5-DOF + gripper matches XLeRobot/LeKiwi exactly**. Bounded catches: a 3D-printed **adapter plate** (both CADs open); **12 V STS3215 servos** run fine off the ROSOrin's [11.1 V 3S pack](../../entities/rosorin-pro.md); drive the arm **directly from the Jetson via a FeeTech USB bus adapter** (bypassing the STM32/`openclaw_controller`, base only); and — the one load-bearing detail — **put a wrist camera on the SO-101 to match the fleet observation space**. **†A mecanum ROSOrin base is holonomic** — same motion class as LeKiwi.

## Headline: you assemble this, you don't adopt it

The wiki's sharpest structural finding is a **bifurcation** — every *deployed* agentic-robot stack uses an LLM-orchestrator over classical/learned skills, while LeRobot/VLA work lives in training stacks, and [the two don't coexist in any single shipped stack](../agents/llm-agent-architecture-across-stacks.md#what-s-notably-absent-across-all-three-stacks). So there is no off-the-shelf product that does all of the above. The framework is an **assembly**:

> **[LeRobot](../../entities/lerobot.md)** (data + policies) + **[Rosetta](../../entities/rosetta.md)** (LeRobot↔ROS 2 bridge) + a per-robot **[LLM-agent orchestrator](../../concepts/agents/llm-agent-architecture.md)** + a **ROS 2↔MCP server you write** + a **master control agent on the DGX Spark**.

## Two integration classes (this fleet splits cleanly)

- **LeRobot-native (XLeRobot, LeKiwi).** FeeTech STS3215 + [SO-ARM101](../../entities/so-arm101.md) is [one of LeRobot's 8 supported platforms](../../sources/lerobot-iclr-2026-paper.md) — LeRobot drives the motors directly, no ROS 2 required for the policy. You *add* ROS 2 (for Nav2 + the agent + coordination) and bridge the two.
- **ROSOrin Pro (after the arm swap).** With the HX-12H replaced by an [SO-ARM101](../../entities/so-arm101.md), the arm is **LeRobot-native** (driven directly over a FeeTech USB bus), and only the **base** stays on ROS 2 — but that base is the ROSOrin Pro's strongest asset (Nav2 + SLAM + LiDAR, already wired). So it joins the LeRobot-native class, and the [servo-lineage gap](lerobot-on-rosorin-pro.md#gap-1-motor-sdk-lineage-feetech-dynamixel-hx-12h) that made it the outlier simply goes away. *(Had you kept the HX-12H, this would be the ROS 2-native / bridge-via-Rosetta case — preserved as the [LeRobot-on-ROSOrin-Pro plan](lerobot-on-rosorin-pro.md).)*

Both classes converge on the same runtime shape — **LeRobot policies for manipulation + ROS 2 for orchestration + nav, bridged by [Rosetta](../../entities/rosetta.md)** — which is why one framework can span the fleet. Rosetta is the right bridge because it is **distro-agnostic and YAML-contract-based**; the alternatives can't span a mixed fleet ([lerobot-ros](../../entities/lerobot-ros.md) is Jazzy-only; [so101-ros2](../../entities/so101-ros2.md) is Humble + SO-101-only).

## Three-layer reference architecture

```
                    ┌───────────────────────────────────────────┐
   DGX SPARK  ─────▶│  LAYER 3 — Master control (fleet brain)    │
   (hub)            │  • Gemma-4-31B  or  Hermes/NemoClaw agent  │
                    │  • task decomposition + robot assignment   │
                    │  • lerobot-train jobs (scheduled)          │
                    │  • async policy server (heavy policies)    │
                    │  • HF Hub dataset sync                      │
                    └───────────────▲──────────────┬─────────────┘
                       network MCP  │ delegate     │ new checkpoints
                       (+ A2A later)│              ▼
   ┌───────────────────────────────┴──────────────────────────────┐
   │  PER ROBOT                                                     │
   │  ┌──────────────────────────────────────────────────────┐     │
   │  │ LAYER 2 — On-edge agent (Gemma-4-E4B) + STT/TTS       │     │
   │  │  emits tool calls  →  ROS 2↔MCP server (you write)    │     │
   │  └───────────────────────────┬──────────────────────────┘     │
   │  ┌───────────────────────────▼──────────────────────────┐     │
   │  │ LAYER 1 — Real-time control (ROS 2)                   │     │
   │  │  Nav2 (navigation)  +  LeRobot policy via Rosetta     │     │
   │  │  ACT onboard / SmolVLA async  →  hardware             │     │
   │  └──────────────────────────────────────────────────────┘     │
   └───────────────────────────────────────────────────────────────┘
```

### Layer 1 — real-time control
Nav2 handles navigation (ROSOrin Pro already has SLAM + Nav2 wired; XLeRobot/LeKiwi add it). Manipulation is a **LeRobot policy** exposed through [Rosetta](../../entities/rosetta.md). **Start every robot on [ACT](../../entities/act.md)** — it is the only policy that runs real-time on a Jetson (**27.8 Hz on an Orin Nano** per [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md); Diffusion Policy 1.8 Hz, SmolVLA 1.4 Hz). Graduate to [SmolVLA](../../entities/smolvla.md) via async offload once ACT plateaus.

### Layer 2 — per-robot on-edge agent
A **[Gemma 4](../../entities/gemma4.md) E4B** (4.5 B effective, multimodal, native function-calling) as the on-robot planner in the [converged LLM-agent pattern](../../concepts/agents/llm-agent-architecture.md): it emits structured tool calls that a **deterministic dispatcher** runs against Layer-1 skills. STT/TTS lives here. Fits the Orin NX 16 GB comfortably; E2B on the ROSOrin Pro's 8 GB.

### Layer 3 — DGX Spark master control
The [local-AI-server tier](../agents/on-device-and-on-robot-agents.md): master control model, training jobs, async policy server for policies too heavy for the edge, and the HF dataset hub.

## The key piece you build: a ROS 2 ↔ MCP server

This is the highest-value new code. It *was* also a standing gap across the whole Claw ecosystem — none of Hermes/OpenClaw/NemoClaw ships one first-party, and until 2026-07-05 no community bridge was known either. That second half is now stale: **[AgenticROS](../../entities/agenticros.md)** is a community Apache-2.0 ROS 2↔agent bridge covering OpenClaw + NemoClaw + Claude/Codex/Hermes + Gemini — but it is **nav-first with no manipulation/LeRobot path**, so this server remains the load-bearing build (see [AgenticROS vs the fleet framework](agenticros-vs-fleet-framework.md), including the fleet-coordination patterns worth copying: `robot_info` heartbeat, `find_robots_for` capability routing, mission step-graphs, `blocks_base` flag). **Design doc + skeleton now exist**: see [ROS 2 ↔ MCP server — design doc](ros2-mcp-server-design.md) and the [`ros2-mcp-server` repo](../../entities/ros2-mcp-server.md) ([GitHub](../../sources/ros2-mcp-server-github.md), MIT — config-driven tool filtering, structured-result envelope, deterministic dispatch, out-of-band stop; `rclpy` lifecycle + fleet heartbeat wired; the Nav2/policy/detector action calls still stubbed). Design in brief:

- **Exposes each robot's ROS 2 action/service surface as [MCP](../../concepts/agents/llm-agent-architecture.md#mcp-model-context-protocol) tools** — one tool per skill: `goto(location)`, `find(object)`, `pick(object)`, `place(target)`, `say(text)`, `explore()`, `get_state()`, `record_episode(task)`. The tool set *is* the robot's capability contract.
- **Runs as an MCP server** on the robot (local agent) and is also reachable over the network (so the Spark master is an MCP client of every robot).
- **Deterministic dispatch, not `eval`.** Each tool validates arguments and calls a ROS 2 action — never `eval()` on model output. This closes the [RCE hazard](../agents/llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources) both Hiwonder kits have.
- **Structured failure returns.** Every tool returns `{status, observation}` so the agent can re-plan on grasp failure / blocked path / occluded tag. Designing this path explicitly is the single biggest lever on robustness — it is [under-documented in every deployed stack](../agents/llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources).
- **The allowlist is the safety surface.** Same property as [Gemini Robotics-ER on Spot](../../entities/gemini-robotics.md): the agent "can't invent capabilities beyond the API." Keep dangerous primitives out of the tool set or gate them behind confirmation.

One MCP server implementation, parameterized per robot by its Rosetta contract + skill launch files, deploys to all three.

## Master control + multi-robot coordination

**v1 (recommended first): centralized MCP, no A2A.** The master agent on the Spark holds every robot's MCP toolset over the network and delegates directly — a **fleet orchestrator** one level above the per-robot orchestrator: decompose the goal → assign each subtask to a robot by capability + location → monitor progress via each robot's `get_state` → reallocate on failure. This needs nothing beyond the MCP servers you already built.

- **Model choice**: **Gemma-4-31B** (BF16 on the Spark's 128 GB, or NVFP4) for a pure function-calling planner; or a **[Hermes](../../entities/hermes-agent.md)** agent, whose **sub-agents** map naturally onto per-robot delegation and whose self-evolving skills + Honcho memory add fleet-level learning. **[NemoClaw](../../entities/nemoclaw.md)** if you want OpenShell policy-guardrails + sandboxing around it.

**v2 (when the fleet grows / robots must negotiate peer-to-peer): [A2A](../../concepts/agents/llm-agent-architecture.md#a2a-agent-to-agent-protocol).** The wiki names A2A (Google, 50+ supporters) as the agent-to-agent discovery/delegation protocol — **but there is no robotics instance of A2A anywhere in the wiki, so this is greenfield.** Reach for it only when direct central-MCP delegation stops scaling (robots handing off subtasks to each other without round-tripping the master).

## Model placement — Gemma 4 across the fleet

| Slot | Model | Where |
|---|---|---|
| On-robot System-2 agent | **Gemma-4-E4B** (4.5 B eff, multimodal) | XLeRobot / LeKiwi (Orin NX 16 GB) |
| On-robot System-2 agent | **Gemma-4-E2B** (2.3 B eff) | ROSOrin Pro (Orin Nano 8 GB) |
| Fleet master control | **Gemma-4-31B** (BF16 / NVFP4) or Hermes 120B-MoE | DGX Spark |
| Heavy manipulation policy server | [SmolVLA](../../entities/smolvla.md) / [π0](../../entities/pi-zero.md) / [GR00T](../../entities/nvidia-groot.md) | DGX Spark (async) |
| Low-level manipulation policy | [ACT](../../entities/act.md) (52 M) | onboard, every robot |

Gemma 4's native function-calling means the same prompt/tool schema drives the edge agent and the master — swap models with a config change, matching the [provider-fungibility finding](../agents/llm-agent-architecture-across-stacks.md#what-converges-and-why-it-matters).

## Speech I/O

Commodity layer in Layer 2: **Whisper** or **sherpa-onnx** (offline) for STT + sherpa/OS TTS — the same stack [ROSOrin's offline curriculum](../../concepts/agents/llm-agent-architecture.md) uses. If the Hailo-10H stays on the LeKiwi, its **Voice2Action** runs speech on the NPU, freeing the Orin NX.

## The data flywheel (collect → HF → train → redeploy, minimal humans)

LeRobot supplies most of the loop:

1. **Collect** — Rosetta's `episode_recorder` → MCAP → **[`LeRobotDataset`](../../entities/lerobot.md)** (Parquet). Teleop via an [SO-ARM101](../../entities/so-arm101.md) leader (XLeRobot/LeKiwi are native; ROSOrin Pro needs a leader + retargeting).
2. **Stream** — push to the **HF Hub** (per-robot dataset repos).
3. **Train** — **scheduled `lerobot-train` on the DGX Spark** (a cron/routine gives the "minimal human" property).
4. **Redeploy** — LeRobot's **async producer-consumer inference** (policy server on the Spark, robot client onboard) pushes new checkpoints out.
5. **Close the loop with less teleop** — **[HIL-SERL](../../entities/lerobot.md)** (human-in-the-loop RL, in LeRobot) plus Rosetta's **HIL contract** (intervention buttons + reward) turns autonomous rollouts + occasional human corrections into training data — the lowest-human-effort path to continual improvement.

> [!warning] Async over consumer WiFi is untested
> LeRobot's async stack assumes a network; home-WiFi jitter can destabilize the producer-consumer queue. Bench-test per robot before relying on Spark-hosted policies for anything reactive. On-edge ACT avoids this entirely.

## Gaps, risks, and hazards (be clear-eyed)

1. **ROS 2↔MCP server = DIY** (above) — the load-bearing new code.
2. **Multi-robot A2A is greenfield** — no robotics precedent in the wiki; start with central MCP.
3. **Cross-embodiment — designed out by the arm swap.** With all three robots on the [SO-ARM101](../../entities/so-arm101.md) (5-DOF + gripper), the cross-arm transfer problem is avoided by hardware homogenization rather than solved by ML: **LeKiwi + ROSOrin share one single-arm checkpoint; XLeRobot co-trains a dual-arm checkpoint off the same pooled data** (dual-arm has a different action dimensionality, so it's a separate checkpoint, not a separate *embodiment*). (Had you kept the HX-12H, you'd face three embodiments and need per-embodiment data or a cross-embodiment recipe — the [GR00T lesson](../../entities/nvidia-groot.md).) The one residual that makes or breaks the shared checkpoint: **[camera parity](fleet-framework-implementation-notes.md#camera-parity-spec)** — the observation space must line up across robots.
4. **ROSOrin Pro specifics** — HX-12H servo lineage (Rosetta wraps ROS 2 services to sidestep) + the [Aurora930 12 fps camera cap](lerobot-on-rosorin-pro.md#gap-2-cameras-and-sampling-rate) (LeRobot default is 30 Hz).
5. **Closed-loop replanning** — design the failure→observation→replan path deliberately; it's the demo-vs-deployment gap.
6. **`eval`-dispatch RCE** — never dispatch LeRobot/agent actions via `eval` on model output; the MCP allowlist replaces it.
7. **Fleet data governance** — HF Hub repo privacy, per-robot dataset naming, and dataset versioning so scheduled training pulls the right splits.

## Build ladder (de-risk cheapest first)

| Step | Goal | Stop condition |
|---|---|---|
| **0.** One LeRobot-native robot (XLeRobot **or** LeKiwi — identical Orin NX) end-to-end: record → HF → train **ACT** on the Spark → async deploy. | Prove the data flywheel on the easiest robot. | A learned pick works on-robot. |
| **1.** Add ROS 2 + a **Rosetta** contract on that robot; wrap Nav2 + the learned pick as skills. | ROS 2 orchestration over a LeRobot policy. | Nav-to-object-then-pick runs under ROS 2. |
| **2.** Write the **ROS 2↔MCP server**; put a **Gemma-4-E4B** agent onboard with STT/TTS. | Single-robot natural-language autonomy. | "Pick up the sock and put it in the basket" works spoken. |
| **3.** Stand up **master control (Gemma-4-31B / Hermes) on the Spark**; command that one robot over network MCP. | Central brain drives one robot. | Master decomposes a 3-step task and monitors it. |
| **4.** Fan out to the **second Orin NX robot** — near-identical; reuse the SO-ARM101 policy + MCP server. | Two-robot fleet, shared policy. | Both robots run the same stack. |
| **5.** Integrate **ROSOrin Pro**: swap in the SO-ARM101 (adapter plate + wrist cam + FeeTech USB, per the [camera-parity spec](fleet-framework-implementation-notes.md#camera-parity-spec)), reuse its Nav2/SLAM base, deploy the **shared single-arm checkpoint** (identical to LeKiwi's); E2B agent. | Homogeneous fleet. | LeKiwi + ROSOrin run the same checkpoint; XLeRobot the co-trained dual-arm one. |
| **6.** **Master coordinates all three** (assign by capability/location); add **A2A** only if peer negotiation is needed. | Fleet coordination. | "Tidy the living room" is split across robots. |
| **7.** **HIL-SERL + scheduled retraining** → the minimal-human continual-improvement flywheel. | Autonomy target. | Policies improve week-over-week with occasional interventions only. |

## What this does NOT solve
- **Navigation** — already Nav2 + SLAM; the framework adds nothing there.
- **Room-scale memory / object permanence** — an agent-memory problem (Hermes Honcho, or a vector store in the master), not a policy problem.
- **A real-time whole-fleet safety layer** — the MCP allowlist covers per-action safety; physical-safety interlocks (e-stop, collision limits) stay in Layer 1.

## Related
- [Fleet framework — implementation notes](fleet-framework-implementation-notes.md) — the code-level appendix: the concrete MCP tool schema (JSON) for the SO-ARM101 robots + the scheduled-training pipeline on the Spark (systemd units, promotion-gate script).
- [Where the compute lives — agents on the robot vs on a local AI server](../agents/on-device-and-on-robot-agents.md) — the deployment-tier framing behind Layers 2/3.
- [LLM-agent architecture across stacks](../agents/llm-agent-architecture-across-stacks.md) — the converged orchestrator pattern + the hazards.
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — umbrella concept; MCP + A2A.
- [LeRobot on ROSOrin Pro](lerobot-on-rosorin-pro.md) — the reusable per-robot adaptation recipe (Rosetta contract, servo gap, compute budget).
- [OpenClaw vs Hermes as a robot brain](../agents/openclaw-vs-hermes-as-robot-brain.md) — the agent-framework choice for Layer 2/3.
- [Onboard compute for XLeRobot — Orin Nano vs NX vs AGX](../platforms/jetson-onboard-compute-xlerobot.md) — the Jetson-tier detail behind the policy-latency numbers.
- [Hailo NPU vs Jetson for an onboard XLeRobot brain](../platforms/hailo-npu-vs-jetson-xlerobot.md) — why the Orin NX (not the Hailo) runs the policy.

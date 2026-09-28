---
title: XLeRobot on Jetson AGX Thor — model stack for speech, reasoning, navigation and manipulation
type: synthesis
created: 2026-09-28
updated: 2026-09-28
tags: [xlerobot, jetson-thor, model-selection, speech, asr, tts, wake-word, gemma4, molmo2-er, nav2, rtab-map, act, smolvla, groot, molmoact2, so-arm101, power-budget, projects]
---

# XLeRobot on Jetson AGX Thor — model stack

Which models should an [XLeRobot](../../entities/xlerobot.md) run onboard a [Jetson AGX Thor](../../entities/jetson-thor.md) so that it can **take spoken commands, reason about them, navigate, and manipulate**? The platform is 2× [SO-ARM101](../../entities/so-arm101.md) (5 DoF + gripper) on a 2-wheel differential base, with a D435i RGB-D camera and a 288 Wh pack.

**Thesis.** Moving from an Orin NX to Thor changes where the constraint sits. **Memory stops binding**: 128 GB holds every model below at once, including 5B-class VLAs that the [Orin NX could not fit](../platforms/jetson-onboard-compute-xlerobot.md). **GPU time at the battery power mode now binds instead.** The recommended `nvpmodel` Mode 3 (70 W) drops the GPU from 10 to 6 TPC, about **−40% GPU throughput** ([Thor power modes](../../sources/nvidia-jetson-thor-platform-power-performance.md), [XLeRobot + Thor power budget](xlerobot-thor-power-budget.md)). The job is therefore to **stagger the models in time**, not to find one best model. The task naturally does this: a command arrives, the robot plans, drives, then manipulates. The heavy GPU consumers rarely need to run at the same moment.

## The stack

```
 mic array ─► wake word + VAD ─► ASR ─────────┐        (CPU, always on)
                    │                          ▼
                    └──► "stop" keyword ─► halt topic    ◄── bypasses the LLM
                                               │
                           ┌───────────────────┘
                           ▼
   planner LLM (Gemma 4) ──tool calls──► ROS 2 ↔ MCP server
        ▲       │                            │
        │       └── point_at(obj) ─► Molmo2-ER-4B (on demand)
        │                            │
   TTS ◄┘ (confirm / report)         ├─► goto(pose)  ─► Nav2 + RTAB-Map + D435i   (CPU)
                                     └─► pick(obj)   ─► ACT / SmolVLA / GR00T N1.7 (GPU)
```

| Layer | Recommendation | Rate / duty | Compute | Status in the wiki |
|---|---|---|---|---|
| **Speech in** | Wake word + VAD always on; ASR only after the wake word. **[sherpa-onnx](#1-speech-io)** (offline; KWS, VAD, ASR and TTS in one toolkit) or **Whisper** | Event-driven | CPU for KWS/VAD; ASR briefly on the GPU or CPU | Named in two sources, **no measurements** |
| **Emergency stop by voice** | A dedicated keyword spotter publishing directly to a halt topic, **never routed through the LLM** | Always on | CPU | Design argument (§1) |
| **Planner** | **[Gemma 4](../../entities/gemma4.md) E4B** or **12B**. These are the sizes with **native audio input**. Emits tool calls to the [ROS 2↔MCP server](../../sources/ros2-mcp-server-github.md) | Between skills (≪1 Hz) | GPU, bursty | Sized; **no Thor tok/s** |
| **Spatial grounding** | **[Molmo2-ER-4B](../../entities/molmo2-er.md)** as a planner tool (`point_at`, `where_to_stand`) | On demand | GPU, bursty | Benchmarked, **not on Jetson** |
| **Navigation** | **[Nav2](../../entities/nav2.md) + [RTAB-Map](../../entities/rtab-map.md) (localization mode) + D435i + wheel odometry** | 10–20 Hz | Mostly CPU | **Measured on a weaker board** |
| **Manipulation** | **[ACT](../../entities/act.md) → [SmolVLA](../../entities/smolvla.md) → [GR00T N1.7](../../entities/nvidia-groot.md)**; **[MolmoAct2-SO100_101](../../entities/molmoact2.md)** as an experiment | 10–25 Hz while manipulating | GPU, sustained | GR00T only has **Thor numbers** |
| **Speech out** | sherpa-onnx TTS (or Parler-TTS) | Event-driven | CPU / brief GPU | Named only |

## 1. Speech I/O

### The design choice: separate ASR, or native audio into the planner?

[Gemma 4](../../entities/gemma4.md) splits cleanly on this. **E2B, E4B and 12B carry a ~300M audio encoder; 26B-A4B and 31B have no audio input at all** ([Gemma 4 model card](../../sources/gemma-4-e2b-model-card.md)). Those two larger variants are the ones the [fleet framework](fleet-agentic-framework.md) puts on the Spark as the fleet-level planner. So:

- **Pipeline A — separate ASR → text → planner.** Works with any planner, including 26B/31B. Produces an explicit **transcript**, which you can log, read back ("I heard: put the sock in the basket"), and use to debug a failed command after the fact. It costs one extra model and one extra hop of latency.
- **Pipeline B — audio straight into Gemma-4-E4B/12B.** One model and one hop fewer, and the model hears tone and emphasis rather than a flattened transcript. But it gives no transcript unless you prompt for one, and it ties you to the audio-capable sizes.

**Recommendation: build A first, and try B as an experiment.** For a robot that acts physically on what it heard, the transcript is a safety and debugging feature, not overhead. It is also what makes *confirm-before-acting* cheap. Test B against A on your own recorded commands, measuring word error rate and time from end of speech to first tool call. That comparison would be new data: **the wiki has no measured latency or accuracy for Gemma 4's audio path**, and the model card itself says the audio and vision encoder costs are unmeasured.

> [!note] Thin sourcing for this section
> The wiki names the speech tools but has measured none of them. The [fleet framework](fleet-agentic-framework.md) specifies "**Whisper** or **sherpa-onnx** (offline) for STT + sherpa/OS TTS", after [Hiwonder's offline curriculum](../../sources/hiwonder-rosorin-docs.md) (Ollama + Qwen + sherpa-onnx). [Seeed's jetson-examples](../../sources/seeed-jetson-examples.md) ships one-command `whisper` (ASR) and `parler-tts` (TTS) recipes for Jetson. There is no ingested primary for Whisper, sherpa-onnx, a wake-word engine, a VAD, or NVIDIA's own speech stack, and no Thor measurement of any of them. Model names in this section beyond those three are general knowledge, not wiki-sourced.

### Front end: wake word, VAD, and the microphone

- **Always-on work must be cheap.** A keyword spotter and a voice-activity detector run continuously on the CPU. ASR wakes only for the utterance that follows. This keeps speech off the GPU while a VLA is running, and at 70 W the CPU has barely been clocked down ([power budget §0](xlerobot-thor-power-budget.md)).
- **The robot is its own worst noise source.** Mechanical noise from 17 STS3215 servos, drive-wheel noise, and Thor's active cooling fan all sit next to the microphone. Use a **USB far-field mic array** with onboard beamforming and echo cancellation, and mount it **away from the Thor heatsink and the base motors**, at the top of the mast if possible. Hiwonder ships the same pattern (a WonderEcho Pro module plus a 6-mic circular array) on its ROSOrin kits ([Hiwonder](../../entities/hiwonder.md)). The wiki has no source comparing arrays.
- **Echo cancellation matters once the robot talks back.** Without it, the robot's own TTS can trigger its wake word.

### A voice "stop" must not go through the planner

The [control-rate ladder](../platforms/control-rate-ladder.md) puts language models in **Band D (0.2–0.4 Hz for a served frontier model; 15–180 s with reasoning)**, two orders of magnitude slower than a reactive policy. A "stop!" that has to be transcribed, reasoned about, and turned into a tool call arrives seconds late. **Wire a dedicated keyword spotter for a small stop vocabulary straight to a halt topic** that both the base controller and the VLA runner obey, with no LLM in the path. The general rule is the [control-rate ladder](../platforms/control-rate-ladder.md)'s: a safety response has to live in a band at least as fast as the hazard. The [prevention / detection / intervention](../platforms/prevention-detection-intervention.md) page covers the policy-side runtime checks. A voice halt is the operator-side complement to them, not a replacement.

### Confirm before acting, but only where it matters

Read back commands that **move the robot somewhere new or grasp something**. Don't read back queries ("what's on the table?"). The planner's tool schema is the natural place to mark which calls need confirmation. Accepting a bare "yes" is the easy case for a keyword spotter.

## 2. Reasoning: planner + spatial grounding

- **Planner: Gemma-4-E4B (4.5B effective) by default, 12B if the GPU budget allows.** It has native function-calling and is multimodal, which makes it the [fleet framework](fleet-agentic-framework.md)'s Layer-2 on-robot agent. Both sizes have audio (§1). NVIDIA lists vLLM, Ollama, llama.cpp and NIM as runtimes on Jetson ([NVIDIA Gemma 4 edge blog](../../sources/nvidia-gemma-4-edge-blog.md)). **There are no Thor tokens/sec figures anywhere in the wiki** ([Gemma 4 open questions](../../entities/gemma4.md)). On Thor, 26B-A4B (3.8B active, MoE) is also plausible for text-only planning if you take Pipeline A.
- **Spatial grounding: [Molmo2-ER-4B](../../entities/molmo2-er.md) as a tool, not the planner.** General VLMs are weak at the metric questions a robot asks. Embodied-reasoning post-training fixes that, and Molmo2-ER leads the open 4B class on **video** spatial reasoning (VSI-Bench 74.5 vs UnifoLM-ER-1's 54.2) ([embodied-reasoning VLMs](../../concepts/learning/embodied-reasoning-vlms.md)). Expose it as `point_at(object)`, returning pixel coordinates. Combined with D435i depth, that gives a 3-D target for both Nav2 and grasp pre-positioning. There is **no Jetson measurement**; it is 4B, the same class as GR00T's backbone.

## 3. Navigation

**Nav2 + RTAB-Map in localization-only mode + D435i + STS3215 wheel-encoder odometry.** No learned model is needed. [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) ran this recipe on an XLeRobot with an Orin Nano, a much weaker board. The [bring-up plan](xlerobot-nav-manip-teleop-bringup.md) covers the D435i bracket and the non-holonomic consequence: the base must **turn and then approach a grasp-ready pose head-on**, because it cannot strafe. At 70 W this is almost free, since it is CPU-bound and the CPU is barely capped.

**Language-conditioned navigation is handled by composition, not by a VLN model.** "Go to the kitchen table" becomes a planner call `goto("kitchen table")` against a named-pose map. "Go to the red chair" becomes `point_at("red chair")` → depth → a Nav2 goal. That second path is an open-parts approximation of what [Robostral Navigate](../../sources/robostral-navigate-paper.md) does end to end: pointing at the next waypoint in image space. Robostral itself is **closed**, and its benchmark numbers use a map-based oracle planner, so it isn't an option here. The point → depth → Nav2 composition is **untested**.

## 4. Manipulation — a four-step ladder

| Step | Policy | Why at this step | Evidence |
|---|---|---|---|
| 1 | **[ACT](../../entities/act.md)**, one task, ~50 demos | The only policy measured at control rate on any Jetson | 36 ms / **27.8 Hz** on an Orin Nano ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)) |
| 2 | **[SmolVLA](../../entities/smolvla.md)** (450M), multi-task | Trained and validated on the SO-100/101, this exact arm; language-conditioned, so the planner's `pick(object)` maps directly onto it | **78.3%** real multi-task vs ACT 48.3% ([bring-up plan](xlerobot-nav-manip-teleop-bringup.md)); 1.4 Hz on an Orin Nano, **unmeasured on Thor** |
| 3 | **[GR00T N1.7](../../entities/nvidia-groot.md)** (3B), when SmolVLA stops generalizing | Native LeRobot policy with an SO-101 walkthrough ([GR00T 1.7 in LeRobot](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)); **the only 3B-class policy with Thor numbers** | N1.6 on Thor: **10.9 Hz** official TensorRT, **22–24 Hz** community kernels ([GR00T on Jetson](../platforms/gr00t-inference-on-jetson.md)); power mode unstated |
| 4 (exp.) | **[MolmoAct2-SO100_101](../../entities/molmoact2.md)** (5B, ~16 GB bf16) | Best open real-world SO-100 result; Thor is the first tier it fits on | **56.7%** zero-shot real SO-100 ([MolmoAct2](../../entities/molmoact2.md)); **no Jetson support or numbers**; the repo expects a FastAPI server, which can run on Thor itself |

> [!note] What 70 W probably does to step 3
> Taking the official 10.9 Hz and applying the ~40% GPU cut suggests **~6–7 Hz** at Mode 3. That is **an extrapolation, not a measurement**: the official benchmark's power mode is unstated, and the relationship isn't necessarily linear. GR00T emits action chunks (the LeRobot rollout executes 8–16 actions per call), so this is still workable for tabletop picks. What suffers is reactivity. If it isn't enough, the choice is Mode 2 (90 W: same GPU cut, full CPU; no help) or Mode 1 (120 W, full GPU) during manipulation only. `nvpmodel` switches at runtime, so power mode can follow the task phase.

**Bimanual caveat.** The public SO-101 checkpoints (SmolVLA base, MolmoAct2-SO100_101) are **single-arm**. XLeRobot's two arms need fine-tuning on your own two-arm demonstrations. Every step above starts with data collection, not a download.

### Considered and set aside

- **[UnifoLM-WLA-1.0](../../entities/unifolm.md)**: now Apache-2.0 with released policy weights, but its 54-D action space is shaped around a Unitree G1's RL whole-body controller (legs, waist, base height). Wrong embodiment.
- **[Cosmos 3 Edge](../../entities/nvidia-cosmos.md) policy**: the "15 Hz on Thor" headline is action playback. Actual inference is **1.53 s per 32-action chunk (~0.65 Hz)** ([control-rate ladder](../platforms/control-rate-ladder.md)), trained on DROID (a Franka dataset).
- **[TurboVLA](../../entities/turbovla.md)**: 0.9 GB and 32 Hz on an RTX 4090, but no Jetson measurement and no verified checkpoint.
- **Robostral Navigate**: closed; see §3.

## 5. Scheduling on a 70 W GPU budget

The task sequence is also the GPU schedule:

| Phase | GPU load | Everything else |
|---|---|---|
| Idle / listening | ~none | KWS + VAD on the CPU |
| Command received | ASR burst → planner burst (→ Molmo2-ER burst) | TTS readback |
| Driving | ~none (Nav2 is CPU) | Stop keyword armed |
| Manipulating | **VLA, sustained** | Planner idle; stop keyword armed |
| Reporting | planner + TTS burst | — |

Only one GPU-heavy model is active in any phase. Keep all models **resident** (128 GB allows it) so no phase pays a load cost. The one real contention case is the planner re-planning *while* a VLA is running, for example on a new spoken command mid-grasp. Handle it by making a new command **pre-empt** the current skill, or by queuing it, rather than running both.

## 6. What Thor does not fix

1. **Demonstration data.** Every manipulation step above starts with teleoperated demos, and bimanual ones for XLeRobot ([bring-up plan](xlerobot-nav-manip-teleop-bringup.md)).
2. **Serial-bus ownership.** A ROS 2 joint-state reader and LeRobot cannot both hold the FeeTech bus. That is the [Rosetta](../../entities/rosetta.md) dependency, and it is unchanged by compute.
3. **Runtime.** At 70 W the whole robot gets **~1.4–3.0 h** on the 288 Wh pack, down from 10+ h ([power budget](xlerobot-thor-power-budget.md)).
4. **The Spark's role changes rather than disappears.** It is no longer needed for inference. It stays the training box, and the fleet-level planner under the [fleet framework](fleet-agentic-framework.md).

## 7. Experiments that would fill wiki gaps

Each of these produces a number the wiki does not have:

1. **Camera-to-action latency for SmolVLA and GR00T N1.7 on Thor, at Mode 3 (70 W) vs Mode 1 (120 W).** Four empty cells, and it answers whether 70 W is livable for manipulation.
2. **Speech Pipeline A vs B** (§1): word error rate and end-of-speech → first-tool-call latency, on commands recorded *on the robot with the servos and fan running*.
3. **Gemma-4-E4B / 12B / 26B-A4B tokens/sec on Thor.** No Thor figure exists for any Gemma 4 size.
4. **MolmoAct2-SO100_101 on Thor**: the first Jetson number for any MolmoAct2 checkpoint.
5. **The point → depth → Nav2 composition** (§3) on 20 named objects: does ER-VLM pointing give usable navigation goals?

## Related

- [XLeRobot on AGX Orin 64 GB — model stack](xlerobot-agx-orin-model-stack.md) — the middle tier: everything fits onboard and runs offline, at about half Thor's VLA throughput; the Spark becomes an optional accelerator. Has the three-tier comparison table.
- [XLeRobot on Orin NX 16 GB — model stack](xlerobot-orin-nx-model-stack.md) — the same requirements with the Orin NX: memory binds, the heavy models move to the Spark, and the design is organized around what still works when Wi-Fi drops. Includes a side-by-side comparison with this page.
- [Onboard compute for XLeRobot](../platforms/jetson-onboard-compute-xlerobot.md) — why Thor is over budget on the stock pack, and the capping that makes it viable.
- [XLeRobot + Thor power budget](xlerobot-thor-power-budget.md) — `nvpmodel` modes, rails and runtime.
- [XLeRobot bring-up plan](xlerobot-nav-manip-teleop-bringup.md) — the Orin NX-era plan this page updates for Thor.
- [Fleet agentic framework](fleet-agentic-framework.md) — the agent, MCP and speech layers this stack instantiates for one robot.
- [GR00T inference on Jetson](../platforms/gr00t-inference-on-jetson.md), [Control-rate ladder](../platforms/control-rate-ladder.md), [VLA deployability landscape](../platforms/vla-deployability-landscape.md).
- [Visual navigation policies](../../concepts/robotics/visual-navigation-policies.md), [Embodied-reasoning VLMs](../../concepts/learning/embodied-reasoning-vlms.md), [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md).

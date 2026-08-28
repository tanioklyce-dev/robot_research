---
title: Where the compute lives — agents on the robot vs on a local AI server
type: synthesis
created: 2026-07-04
updated: 2026-08-27
tags: [edge-ai, on-device, on-robot, local-server, agents, jetson, dgx-spark, ollama, hermes, nemoclaw, gemma4, vla, deployment-topology]
---

# Where the compute lives — agents on the robot vs on a local AI server

The wiki's other two agent syntheses answer *which framework* ([OpenClaw vs Hermes as a robot brain](openclaw-vs-hermes-as-robot-brain.md)) and *what shape* ([LLM-agent architecture across stacks](llm-agent-architecture-across-stacks.md)). This one answers a third, orthogonal question: **where does the model inference physically run?** As of 2026 there are three answers, and a capable robot usually uses more than one at once.

## The three tiers

| Tier | Hardware | Runs what | Latency | Privacy | Wiki instances |
|---|---|---|---|---|---|
| **On-robot (edge)** | [Jetson Orin Nano](../../entities/jetson-orin-nano.md) / NX / [Thor](../../entities/jetson-thor.md), onboard | the real-time **policy** (VLA/ACT/DP) + a small LLM/VLM | µs–ms control loop; small-LLM tokens on-board | full (nothing leaves the robot) | [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) (on-edge VLA), [Helix](../../sources/helix-blog.md) (onboard S1/S2), [Taking Flight drone](../../sources/taking-flight-with-dialogue-px4-drone-agent.md) ([Ollama](../../entities/ollama.md) on Orin Nano), [ROSOrin offline curriculum](../../sources/hiwonder-rosorin-docs.md) (Ollama qwen3:1.7b) |
| **Local AI server (LAN)** | [DGX Spark](../../entities/dgx-spark.md) / RTX PRO workstation on the same network | a **big reasoning brain** (30B–120B) serving the robot over an API | network round-trip (ms), no WAN | high (stays on-premises) | [Hermes Agent](../../entities/hermes-agent.md) on DGX Spark (120B-MoE "all day"); [NemoClaw](../../entities/nemoclaw.md) local-Nemotron pitch; SmolVLA's [RobotClient/PolicyServer](../../entities/smolvla.md) async split |
| **Cloud endpoint** | NVIDIA inference endpoints / OpenRouter / vendor APIs | frontier models, or a hosted Nemotron | WAN latency; rate limits | lowest (data leaves premises) | [NemoClaw Hermes quickstart](../../sources/nvidia-nemoclaw-hermes-quickstart.md) default (`nemotron-3-super-120b-a12b` via NVIDIA Endpoints); Hermes' 200+ OpenRouter models |

## The split-brain pattern is the norm, not the exception

No single tier does everything well, so capable systems **split by time-constant**:

- **Fast loop stays on the robot.** A 10–200 Hz visuomotor policy cannot tolerate a network hop. Every on-robot deployment in the wiki keeps the policy local: [Helix](../../sources/helix-blog.md)'s 80M System-1 at 200 Hz runs onboard even when its 7B System-2 also does; [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) measures the *reason it must* — on a [Jetson Orin Nano](../../entities/jetson-orin-nano.md), ACT hits 27.8 Hz, Diffusion Policy 1.8 Hz, SmolVLA 1.4 Hz; anything heavier stalls the loop.
- **Slow reasoning can be offloaded.** Symbolic planning, language understanding, and tool-selection run at human conversational cadence (seconds), which tolerates a LAN round-trip. This is exactly the [System-1 / System-2 split](../../concepts/learning/vla-models.md) ([GR00T](../../entities/nvidia-groot.md), Helix) re-expressed as a *hardware placement* decision: put System-2 on a [DGX Spark](../../entities/dgx-spark.md) if the robot's onboard GPU can't hold it.
- **SmolVLA already ships the mechanism.** Its **RobotClient/PolicyServer** async stack with physical/logical decoupling ([SmolVLA](../../entities/smolvla.md)) is precisely "policy on the robot, inference wherever you point it" — the general form of the tier-1/tier-2 split.

## The model-fits-hardware ladder

What you can run on-robot vs on-server is set by memory, and 2026's small-model families are explicitly built for the low rungs:

- **[Gemma 4](../../entities/gemma4.md)** ([edge blog](../../sources/nvidia-gemma-4-edge-blog.md)) is the clearest example: the multimodal **E2B (2.3B effective) / E4B (4.5B effective)** variants target [Jetson Orin Nano](../../entities/jetson-orin-nano.md) *on the robot*, while the **31B** (NVFP4 4-bit) wants a **[DGX Spark](../../entities/dgx-spark.md)** (128 GB unified) as the *local server*. Same family, two tiers.
- **[Hermes Agent](../../entities/hermes-agent.md)** spans the same range from the agent side — 8B–35B via [Ollama](../../entities/ollama.md)/llama.cpp locally, up to a 120B-MoE on a DGX Spark serving as the brain.
> [!note] The rung is the backend, not the board — with numbers
> [Google's own LiteRT benchmarks](../../sources/gemma-4-e2b-model-card.md) for **Gemma 4 E2B** put hard figures on this ladder for the first time in the wiki:
>
> | Device | Backend | Prefill (tok/s) | Decode (tok/s) | TTFT (s) |
> |---|---|---|---|---|
> | Raspberry Pi 5 | CPU | 133 | **7.6** | 7.8 |
> | [Jetson Orin Nano](../../entities/jetson-orin-nano.md) | CPU | 109 | 12.2 | 9.4 |
> | [Jetson Orin Nano](../../entities/jetson-orin-nano.md) | **GPU** | 1,142 | **24.2** | **0.9** |
> | Qualcomm Dragonwing IQ8 | **NPU** | 3,747 | 31.7 | 0.3 |
>
> Two lessons the "targets Orin Nano" framing hides. **The same board spans a 10× range** depending on whether you reach the GPU. And **decode rate, not TTFT, is what a conversational robot lives on** — it is independent of prompt length, so a 45-token spoken answer costs ~6 s on a Pi 5 and under 2 s on an Orin GPU. The [Open Duck Mini](../../entities/open-duck-mini.md) demo at Google I/O 2026 ran one duck on each, and the [secondary coverage](../../sources/explainx-gemma-4-open-duck-mini.md) called both "very snappy."

- **Runtimes** are the enabling layer: [Ollama](../../entities/ollama.md) / llama.cpp for the edge + workstation, vLLM / NIM for the server, all of which [Gemma 4](../../entities/gemma4.md) and Nemotron support.

## Why a robot wants a local server at all

Cloud endpoints are the easy default ([NemoClaw Hermes quickstart](../../sources/nvidia-nemoclaw-hermes-quickstart.md) ships one), but three forces push reasoning onto a **local** AI server rather than the cloud:

1. **Privacy** — a home robot's camera feed and a factory's floor data shouldn't leave the premises; on-prem inference (NemoClaw's OpenShell-sandboxed Nemotron, Hermes on DGX Spark) keeps it local.
2. **Latency + availability** — a WAN hop plus rate limits is a poor foundation for an always-on household agent; a LAN server is predictable and offline-capable (the explicit design point of the [ROSOrin offline curriculum](../../sources/hiwonder-rosorin-docs.md)).
3. **Cost** — continuous agent loops are token-hungry; amortized local hardware beats per-token API billing for always-on use.

The remaining gap is the same one flagged across the Claw ecosystem: **none of these agent stacks has a native robot integration** — bridging them to a physical robot still means writing an MCP-server-over-ROS-2 that exposes the robot's skills as tools ([OpenClaw vs Hermes](openclaw-vs-hermes-as-robot-brain.md), [Hermes Agent](../../entities/hermes-agent.md#robot-platform-fit)). Once that bridge exists, the tier question — edge vs local-server vs cloud for the *reasoning* half — is a deployment knob, not an architecture rewrite.

## Related
- [Fleet agentic control framework](../projects/fleet-agentic-framework.md) — a concrete build applying these three tiers across a real XLeRobot / LeKiwi / ROSOrin Pro + DGX Spark fleet.
- [OpenClaw vs Hermes as a robot brain](openclaw-vs-hermes-as-robot-brain.md) — *which* agent framework.
- [LLM-agent architecture across stacks](llm-agent-architecture-across-stacks.md) — the *shared shape* (LLM emits tool calls).
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — umbrella concept.
- [VLA models](../../concepts/learning/vla-models.md) — the System-1/System-2 split this synthesis re-casts as a placement decision.
- [Jetson onboard-compute comparison](../platforms/jetson-onboard-compute-xlerobot.md) — the edge-tier hardware detail.

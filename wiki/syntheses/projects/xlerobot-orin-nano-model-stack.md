---
title: XLeRobot on Jetson Orin Nano 8 GB — model stack for speech, reasoning, navigation and manipulation
type: synthesis
created: 2026-09-28
updated: 2026-09-28
tags: [xlerobot, orin-nano, dgx-spark, model-selection, speech, asr, wake-word, keyword-spotting, gemma4, nav2, rtab-map, act, smolvla, groot, off-board-inference, graceful-degradation, memory-budget, pricing, projects]
---

# XLeRobot on Jetson Orin Nano 8 GB — model stack

The entry tier for the same requirements (**spoken commands, reasoning, navigation and manipulation**) on an [XLeRobot](../../entities/xlerobot.md): 2× [SO-ARM101](../../entities/so-arm101.md), 2-wheel differential base, D435i, 288 Wh pack. The counterparts are the [Orin NX](xlerobot-orin-nx-model-stack.md), [AGX Orin](xlerobot-agx-orin-model-stack.md) and [Thor](xlerobot-thor-model-stack.md) stacks.

**Thesis: the Nano is a body controller, not a brain.** It is the **only tier with a published, measured XLeRobot build**: [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) ran exactly this board untethered, with ACT at 27.8 Hz and RTAB-Map + Nav2 localization. It is also the only tier where **even the smallest LLM planner doesn't comfortably fit** beside navigation. With 8 GB of unified memory, the onboard set is reduced to what a robot needs to **move, stop, and execute learned skills**. Everything involving *understanding language* moves to the [DGX Spark](../../entities/dgx-spark.md).

That changes what "offline" means. On the Orin NX, a Wi-Fi drop degraded the robot to a small LLM planner. On the Nano, the right offline mode has **no LLM at all**: a **fixed spoken-command vocabulary** (a keyword spotter mapping ~20 phrases directly to skills) is deterministic, fits in megabytes, and can't hallucinate a tool call.

## The stack

```
 ONBOARD (Orin Nano 8 GB) — move, stop, execute                   OFF-BOARD (DGX Spark) — understand
 ───────────────────────────────────────────────                   ──────────────────────────────────
 mic array ─► wake word + VAD ─┬─► "stop" KWS ─► halt topic         (CPU; no network, no LLM)
                               ├─► command KWS ─► skill table        (CPU; offline fallback)
                               └─► audio after wake word ─────────► ASR (Whisper-class)
                                                                      │
                                                                     Gemma-4-31B / 26B-A4B planner
                                                                      │  (tool calls, over network MCP)
      ROS 2↔MCP server ◄──────────────────────────────────────────────┘
        ├─► goto(pose)   ─► Nav2 + RTAB-Map (localization) + D435i   (onboard)
        ├─► pick(obj)    ─► ACT, per skill                          (onboard, GPU)
        │                    └─ or ─────────── async / ZMQ ────────► SmolVLA → GR00T N1.7
        ├─► point_at(obj) ─────────────────────────────────────────► Molmo2-ER-4B
        └─► say(text)    ─► TTS (CPU)
```

| Layer | Onboard | Off-board (Spark) | Offline fallback |
|---|---|---|---|
| **Speech in** | Wake word + VAD + **stop KWS** + **command KWS** (fixed vocabulary), all on the CPU | **ASR** on audio streamed after the wake word | Fixed commands only |
| **Planner** | — (see §1) | **Gemma-4-31B** or 26B-A4B | Skill table (no LLM) |
| **Spatial grounding** | — | Molmo2-ER-4B | Named poses only |
| **Navigation** | **Nav2 + RTAB-Map localization + D435i + wheel odometry** | — | Works |
| **Manipulation** | **ACT**, one checkpoint per skill | **SmolVLA → GR00T N1.7** | ACT skills |
| **Speech out** | TTS on the CPU | — | Works |

## 1. The memory budget: why the planner leaves

| Resident | Estimate | Basis |
|---|---|---|
| OS (headless) + ROS 2 + drivers | ~1.5–2 GB | **Estimate** |
| RTAB-Map (localization) + Nav2 | ~1–2 GB | **Estimate**; runs on this board ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)) |
| D435i + 2 wrist cameras, buffers | ~0.5–1 GB | **Estimate** |
| KWS + VAD + TTS | ~0.1–0.3 GB | **Estimate** |
| ACT (one skill) | <0.5 GB | **Estimate**; ran at 36 ms on this board |
| **Subtotal** | **~3.5–5.5 GB** | ~2.5–4.5 GB headroom |
| *+ Gemma-4-E2B planner (GPU)* | *2.7 GB* | **Measured** on this board: 2,739 MB, LiteRT-LM ([Gemma 4 card](../../sources/gemma-4-e2b-model-card.md)) |
| *With the planner* | *~6–8 GB of 8* | Headroom gone at the high end |

**Gemma-4-E2B is measured on exactly this board**: GPU decode **24.2 tok/s**, **0.9 s** to first token, **2.7 GB**. It's fast enough to be a planner, but it doesn't fit comfortably alongside navigation. At the high end of the estimates the board runs out of memory, and on a Jetson, running out of *unified* memory stalls the camera and navigation stack along with the model. The CPU path is worse on both axes (12.2 tok/s, 3.7 GB). Hence the default: **the planner lives on the Spark**.

> [!note] If you do want an onboard planner
> It's possible with discipline: measure the real subtotal with `tegrastats` first (every row but one is an estimate), then run E2B only while navigation is idle, i.e. unload or pause RTAB-Map during planning. That's the kind of scheduling the [Thor](xlerobot-thor-model-stack.md#5-scheduling-on-a-70-w-gpu-budget) and [AGX Orin](xlerobot-agx-orin-model-stack.md) stacks apply to GPU time, applied here to memory. It works, but it's fragile. The Orin NX module ($999, below) is the clean fix, and it drops onto this same carrier.

## 2. Speech I/O

Same front end as the other tiers ([Thor §1](xlerobot-thor-model-stack.md#1-speech-io)): far-field mic array away from the servos, wheels and fan, with echo cancellation. **Wake word, VAD and the voice-stop keyword are always on, on the CPU, and the stop goes straight to a halt topic.** What differs:

- **Two keyword spotters, not one.** Beside the stop spotter, a **command spotter** with a small fixed vocabulary ("go to the kitchen", "go to the dock", "pick up the cup", "put it in the basket", "come here", ~20 phrases) mapped **directly to skills** through a lookup table. This is the offline mode. sherpa-onnx, one of the wiki's named options, ships keyword spotting as well as ASR ([fleet framework speech I/O](fleet-agentic-framework.md)). Keyword models are tiny compared with any ASR model.
- **Open-vocabulary ASR runs on the Spark by default.** After the wake word, stream the utterance to the Spark, and run ASR there beside the planner. That frees the Nano's **6 CPU cores**, which RTAB-Map and Nav2 already use, and puts the better ASR model where the memory is. The alternative, a small streaming ASR onboard, is plausible and is the first experiment below. It's a trade between CPU load and offline capability.
- **Offline behavior is explicit.** When the Spark is unreachable, the robot says so ("I can only do simple commands right now") and listens only for the fixed vocabulary.

As on every tier: **the wiki names these speech tools but has measured none of them on a Jetson.**

## 3. Reasoning: all off-board

- **Planner: Gemma-4-31B** (BF16 on the Spark's 128 GB), or **26B-A4B** (3.8B active, MoE) if latency matters more ([NVIDIA Gemma 4 edge blog](../../sources/nvidia-gemma-4-edge-blog.md), [Gemma 4](../../entities/gemma4.md)). Neither has audio input, so the Spark-side ASR transcript is their input. The planner calls the robot's [ROS 2↔MCP server](../../sources/ros2-mcp-server-github.md) over the network, which is the [fleet framework](fleet-agentic-framework.md)'s v1 centralized-MCP design with the per-robot edge agent removed.
- **Spatial grounding: Molmo2-ER-4B on the Spark**, the same `point_at` tool as on the [Orin NX](xlerobot-orin-nx-model-stack.md#3-reasoning-a-small-planner-that-can-escalate). One frame goes up and pixel coordinates come back.
- **Latency.** Every spoken command now makes several network hops: audio up, tool calls down, possibly a frame up for pointing. Each is small next to the planner's own time. That is the [control-rate ladder](../platforms/control-rate-ladder.md)'s Band D (seconds). None of it sits in a control loop, so Wi-Fi jitter is an annoyance here, not a hazard.

## 4. Manipulation: measured on this board

| Step | Policy | Where | Rate | Evidence |
|---|---|---|---|---|
| 1 | **[ACT](../../entities/act.md)**, per skill | **Onboard** | **27.8 Hz** (36 ms) | **Measured on this board, on this robot** ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)) |
| — | Diffusion Policy | (onboard) | 1.8 Hz (540 ms) | Measured; too slow for reactive control |
| 2 | **[SmolVLA](../../entities/smolvla.md)** (450M) | **Spark, LeRobot async** | 1.4 Hz *onboard* (714 ms, measured) | The bottleneck is the iterative action expert, not memory, so it goes to the Spark |
| 3 | **[GR00T N1.7](../../entities/nvidia-groot.md)** (3B) | **Spark** | ~6–9 Hz Wi-Fi, ~8–10 Hz wired (est.) | [GR00T over ZMQ](gr00t-spark-zmq-xlerobot.md); no Jetson below AGX Orin is benchmarked |

**ACT is the workhorse here.** It's the only learned policy that runs at control rate on this board, and a library of per-skill ACT checkpoints is what the offline command vocabulary maps onto: each fixed phrase maps to one ACT checkpoint. The [bring-up plan](xlerobot-nav-manip-teleop-bringup.md) sequences this: ~50 demos per top-down task, ACT first, then SmolVLA off-board.

**Bimanual caveat, as on every tier:** public SO-101 checkpoints are single-arm, so every step starts with your own two-arm demos.

## 5. Navigation

Nav2 + RTAB-Map **in localization-only mode** + D435i + STS3215 wheel odometry, onboard. This is the configuration [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) measured on this board. **Build the map ahead of time**: full SLAM mapping is heavier than localization and is the thing most likely to crowd the 8 GB. You can build the map with the robot tethered, or from a laptop. Language goals use named poses, and with the Spark reachable, `point_at` → depth → Nav2 goal.

## 6. Platform settings

- **Power mode: 15 W or 25 W; not 7 W.** Jetson Linux r39.2 known issue **6236259** (reboot crashes after dropping memory clock at boot) names the **Orin Nano 8 GB at 7 W** ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)). The 67 TOPS figure is a **Super Mode** number, and a JetPack 7.2 **ISO update does not switch to Super Mode**. You have to flash from a Linux host or SDK Manager to get it (issue 6279443).
- **Flashing.** From JetPack 7.2 the dev kit has **no SD-card image**: a unified ISO on a USB stick installs to microSD or NVMe. Answer `y` to the QSPI capsule-update prompt, and apply the **PCIe boot-bug overlay**, because a battery robot power-cycles daily ([JetPack 7.2 release](../../sources/nvidia-jetpack-7-2-release.md), [flash how-to](jetson-orin-nano-flash-howto.md)).
- **Power draw is the Nano's strength.** 7–25 W, and [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) measured **5% battery discharge over 30 minutes of full functional load** for the whole robot, and no thermal throttling after 30 minutes of continuous SmolVLA. That is the longest runtime of any tier.

## 7. Price, and the upgrade path

After NVIDIA's [2026-07 price increase](../../sources/nvidia-jetson-faq-pricing.md), the **Orin Nano Super dev kit is $399** (was $249). That puts the Cutting the Cord build near **$1,352**, up from $1,202. The upgrade path is unusually cheap in effort: the **Orin NX 16 GB module ($999 at 1KU, was $699) is pin-compatible with this dev kit's carrier**, so the upgrade is a module swap, not a rebuild ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)). The swap buys what §1 lacks: 16 GB, room for an onboard E2B/E4B planner, and a real offline mode. Starting on the Nano loses nothing, except that you end up paying for both boards.

## 8. The four tiers side by side

| | **Orin Nano 8 GB** (this page) | **Orin NX 16 GB** ([page](xlerobot-orin-nx-model-stack.md)) | **AGX Orin 64 GB** ([page](xlerobot-agx-orin-model-stack.md)) | **Thor T5000** ([page](xlerobot-thor-model-stack.md)) |
|---|---|---|---|---|
| Binding constraint | **Memory**: no room for an LLM beside nav | Memory + network | GPU throughput at battery modes | GPU time at 70 W |
| Onboard planner | **None** (skill table offline) | E2B / E4B | E4B / 12B | E4B / 12B |
| Open-vocabulary ASR | **Spark** | Onboard (CPU) | Onboard | Onboard |
| Pointing (Molmo2-ER) | Spark | Spark | Onboard | Onboard |
| Manipulation onboard | **ACT, 27.8 Hz measured** | ACT | ACT, SmolVLA, GR00T (5.8 Hz measured, mode unstated) | All (GR00T 10.9–24 Hz) |
| Works with no network | Stop, **fixed commands**, nav, ACT | + small LLM planner | Everything, slower | Everything |
| Compute power | **7–25 W** | 10–40 W | 15–60 W | 70 W cap |
| NVIDIA list price (2026-09) | **$399** dev kit | $999 module | $3,499 dev kit | $5,499 dev kit |
| Measured on an XLeRobot | **Yes** | No | No | No |

## 9. Experiments that would fill wiki gaps

1. **Onboard streaming ASR on the Nano's CPU while RTAB-Map + Nav2 run**: real-time factor and CPU headroom. Decides whether open-vocabulary speech can stay onboard.
2. **The real memory subtotal** (§1) via `tegrastats`, with navigation, cameras and ACT running. Decides whether E2B can come aboard.
3. **Command-KWS accuracy** on ~20 phrases, recorded with the servos and fan running: false accepts matter more than misses for a robot that moves on them.
4. **End-to-end spoken command → first motion**, with the planner on the Spark over Wi-Fi.

## Related

- [Orin NX](xlerobot-orin-nx-model-stack.md), [AGX Orin](xlerobot-agx-orin-model-stack.md), [Thor](xlerobot-thor-model-stack.md) model stacks.
- [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md): the measured build this page rests on.
- [Onboard compute for XLeRobot](../platforms/jetson-onboard-compute-xlerobot.md), [Jetson module ladder](../platforms/jetson-module-ladder-power-performance.md), [NVIDIA Jetson FAQ pricing](../../sources/nvidia-jetson-faq-pricing.md).
- [XLeRobot bring-up plan](xlerobot-nav-manip-teleop-bringup.md), [Fleet agentic framework](fleet-agentic-framework.md), [GR00T over ZMQ](gr00t-spark-zmq-xlerobot.md), [Orin Nano flash how-to](jetson-orin-nano-flash-howto.md).

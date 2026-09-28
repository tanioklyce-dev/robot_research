---
title: XLeRobot on Jetson Orin NX 16 GB — model stack for speech, reasoning, navigation and manipulation
type: synthesis
created: 2026-09-28
updated: 2026-09-28
tags: [xlerobot, orin-nx, dgx-spark, model-selection, speech, asr, tts, wake-word, gemma4, molmo2-er, nav2, rtab-map, act, smolvla, groot, off-board-inference, graceful-degradation, memory-budget, projects]
---

# XLeRobot on Jetson Orin NX 16 GB — model stack

The same requirements as the [Thor model stack](xlerobot-thor-model-stack.md): **spoken commands, reasoning, navigation and manipulation** on an [XLeRobot](../../entities/xlerobot.md) (2× [SO-ARM101](../../entities/so-arm101.md), 2-wheel differential base, D435i, 288 Wh pack). The difference is a **[Jetson Orin NX 16 GB](../platforms/jetson-onboard-compute-xlerobot.md)** onboard and a **[DGX Spark](../../entities/dgx-spark.md)** on the network.

**Thesis.** On Thor, all models fit on the robot and the problem was scheduling GPU time. On the Orin NX, **16 GB of memory shared with the OS is the binding constraint**, and the heavy models (multi-task VLAs, the ER pointing model, a large planner) **have to live on the Spark**. That makes the network part of the robot. The design question changes from "which model is best" to **"what must still work when Wi-Fi drops?"** The answer sets the split:

- **Onboard: everything needed to be safe and useful on its own.** That is listening, stopping, a small planner, navigation, and single-task learned skills.
- **On the Spark: everything that makes it *better*.** That is multi-task and generalist manipulation, spatial grounding, and a stronger planner.

This is the per-robot instance of the [fleet agentic framework](fleet-agentic-framework.md) (Layer 2 on the edge, Layer 1 on the Spark), and it extends the [Orin NX bring-up plan](xlerobot-nav-manip-teleop-bringup.md) with the speech and reasoning layers that plan left out of scope.

## The stack

```
 ONBOARD (Orin NX 16 GB) — must survive a Wi-Fi drop            OFF-BOARD (DGX Spark)
 ───────────────────────────────────────────────────            ─────────────────────
 mic array ─► wake word + VAD ─► ASR ──┐       (CPU)
                  │                    ▼
                  └─► "stop" KWS ─► halt topic   (CPU, no network, no LLM)
                                       │
            Gemma-4-E2B/E4B planner ◄──┘ ──── escalate hard requests ──► Gemma-4-31B / 26B-A4B
                  │   (tool calls → ROS 2↔MCP server)                    
                  ├─► goto(pose) ──► Nav2 + RTAB-Map + D435i  (CPU)
                  ├─► point_at(obj) ────────────────────────────────────► Molmo2-ER-4B
                  ├─► pick(obj) ──► ACT, per task (onboard, GPU)
                  │                  └─ or ─────────── async / ZMQ ─────► SmolVLA → GR00T N1.7
                  └─► say(text) ─► TTS (CPU)
```

| Layer | Onboard | Off-board (Spark) | Offline fallback |
|---|---|---|---|
| **Speech in** | Wake word + VAD + stop keyword (CPU, always on); **small ASR on the CPU** | — | Fully onboard: works |
| **Planner** | **Gemma-4-E2B** (measured class) or **E4B** | Gemma-4-31B / 26B-A4B for requests the small planner can't handle | Small planner only |
| **Spatial grounding** | — (doesn't fit alongside the rest) | **Molmo2-ER-4B** (`point_at`) | Named-pose goals only |
| **Navigation** | **Nav2 + RTAB-Map + D435i + wheel odometry** | — | Fully onboard: works |
| **Manipulation** | **ACT**, one checkpoint per skill | **SmolVLA**, then **GR00T N1.7** (LeRobot async or ZMQ) | ACT skills only |
| **Speech out** | TTS on the CPU | — | Works |

## 1. The memory budget

The Orin NX's 16 GB is **unified memory**: the CPU, OS, ROS 2, camera buffers and every model share one pool. [GR00T-3B's stated 16 GB floor](../platforms/gr00t-inference-on-jetson.md) equals the whole module, and [MolmoAct2-SO100_101 at ~16 GB bf16](../platforms/jetson-onboard-compute-xlerobot.md) rules itself out the same way. The onboard set has to fit with headroom:

| Resident | Estimate | Basis |
|---|---|---|
| OS (headless) + ROS 2 + drivers | ~2 GB | **Estimate** |
| RTAB-Map (localization) + Nav2 | ~1–2 GB | **Estimate**; grows with map size |
| D435i + 2 wrist cameras, buffers | ~0.5–1 GB | **Estimate** |
| KWS + VAD + small ASR + TTS | ~0.5 GB | **Estimate** |
| **Gemma-4-E2B** planner | **~2.7 GB** | **Measured**: 2,739 MB on an Orin Nano GPU under LiteRT-LM ([Gemma 4 card](../../sources/gemma-4-e2b-model-card.md)) |
| *or* Gemma-4-E4B planner | ~4–5 GB | **Estimate** (~2× E2B's effective parameters) |
| ACT policy (one skill loaded) | <0.5 GB | **Estimate**; ACT is small |
| **Total** | **~7–10 GB** | Leaves ~6 GB headroom |

What does *not* go on the list: a second multi-billion-parameter model. That is why Molmo2-ER-4B (~8 GB bf16) and every 3B+ VLA go off-board. SmolVLA (450M) would *fit*, but it runs too slowly onboard (§4).

> [!warning] Most rows are estimates
> Only the Gemma-4-E2B figure is measured, and on an Orin *Nano*, whose GPU (1024 CUDA / 32 Tensor cores) matches the Orin NX's. Measure `tegrastats` with everything running before trusting the headroom.

## 2. Speech I/O

The front end is the same as on Thor ([Thor stack §1](xlerobot-thor-model-stack.md#1-speech-io)). Wake word, VAD and the **stop keyword run always-on on the CPU**. The **voice stop publishes straight to a halt topic**, with no LLM and no network in the path. Use a far-field mic array away from the servos, wheels and fan, with echo cancellation so the robot's own TTS doesn't wake it.

What changes on the Orin NX:

- **ASR must be onboard and on the CPU.** Onboard, because speech has to survive a Wi-Fi drop: "stop", "go back to the dock" and "what are you doing?" can't depend on the Spark being reachable. On the CPU, because the one GPU is shared by the planner and ACT. The Orin NX has **8 Cortex-A78AE cores**, and a small streaming ASR model on the CPU is the standard way to use them. The wiki's named options are **sherpa-onnx** (offline; has KWS, VAD, ASR and TTS in one toolkit) and **Whisper** (small sizes) ([fleet framework speech I/O](fleet-agentic-framework.md), [Seeed jetson-examples](../../sources/seeed-jetson-examples.md)). **None are measured on any Jetson in the wiki.**
- **Native audio into the planner looks more attractive here, and still isn't the default.** Gemma-4-E2B/E4B carry a ~300M audio encoder ([Gemma 4 card](../../sources/gemma-4-e2b-model-card.md)), so Pipeline B would save the ASR model's memory. But that saving is small (a few hundred MB), while B moves speech onto the **shared GPU** and loses the transcript. Keep Pipeline A (separate ASR → text) and test B as an experiment.
- **Offline behavior should be explicit.** When the Spark is unreachable, the planner's tool list should shrink to the onboard tools (`goto`, ACT skills, `say`), and the robot should *say* that it's in reduced mode rather than failing silently on a `point_at` call.

## 3. Reasoning: a small planner that can escalate

- **Onboard planner: start with [Gemma-4-E2B](../../entities/gemma4.md), move to E4B if tool-call accuracy demands it.** E2B is the only Gemma 4 size with a measured Jetson number: on an Orin Nano GPU, **24.2 tok/s decode, 0.9 s to first token, 2.7 GB** (LiteRT-LM, 1024-token prefill). A 40-token tool call is ~2–3 s end to end. The Orin NX's GPU has the same core count at higher clocks, so expect similar or slightly better. That is an inference, not a measurement. E4B, the [fleet framework](fleet-agentic-framework.md)'s pick, has roughly twice the effective parameters. My unmeasured guess is ~half the decode speed and twice the memory.
- **Escalate to the Spark for hard requests.** Multi-step, ambiguous, or long-context commands ("tidy the living room") go to **Gemma-4-31B** (BF16 on the Spark's 128 GB, per the [NVIDIA Gemma 4 edge blog](../../sources/nvidia-gemma-4-edge-blog.md)). It returns a plan the onboard planner executes step by step. That is the fleet framework's master-agent tier used per robot. 31B has **no audio input**, so the ASR transcript is what gets sent, which is another reason for Pipeline A.
- **Spatial grounding runs off-board.** [Molmo2-ER-4B](../../entities/molmo2-er.md) as a `point_at` tool on the Spark: the Orin NX sends one frame and gets pixel coordinates back. This is the same role it plays on [Thor](xlerobot-thor-model-stack.md#2-reasoning-planner--spatial-grounding), paying a network round trip instead of onboard memory. It's a one-shot call, so Wi-Fi jitter barely matters.

## 4. Manipulation — the ladder, split across the network

| Step | Policy | Where | Rate | Evidence |
|---|---|---|---|---|
| 1 | **[ACT](../../entities/act.md)**, one checkpoint per skill | **Onboard** | ≥27.8 Hz | 36 ms on an Orin Nano ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)); the Orin NX is the stronger board |
| 2 | **[SmolVLA](../../entities/smolvla.md)** (450M), multi-task | **Spark, LeRobot async** | Unmeasured; well above onboard | 1.4 Hz on an Orin Nano, where the bottleneck is the iterative action expert, not memory ([bring-up plan](xlerobot-nav-manip-teleop-bringup.md)) |
| 3 | **[GR00T N1.7](../../entities/nvidia-groot.md)** (3B) | **Spark, ZMQ or async** | **~6–9 Hz on good Wi-Fi**, ~8–10 Hz wired (estimate) | [GR00T on Spark over ZMQ](gr00t-spark-zmq-xlerobot.md); below the memory floor onboard ([GR00T on Jetson](../platforms/gr00t-inference-on-jetson.md)) |
| — | [MolmoAct2-SO100_101](../../entities/molmoact2.md) (5B) | Spark only | — | ~16 GB bf16; the repo's own design is off-robot behind a FastAPI server |

**Why ACT remains the onboard workhorse:** it is the only manipulation layer that works without the network. A library of per-skill ACT checkpoints ("pick sock", "place in basket", "open drawer"), each trained on ~50 demos, is a cheap offline fallback. It's also a good baseline for judging whether SmolVLA and GR00T are worth their network dependency. Keep one checkpoint resident and hot-swap per skill.

> [!warning] Off-board policies over home Wi-Fi are untested
> The [fleet framework](fleet-agentic-framework.md) flags LeRobot's async stack over consumer Wi-Fi as untested. [The ZMQ estimate](gr00t-spark-zmq-xlerobot.md) shows jitter spikes past 100 ms, and the synchronous REQ/REP client stalls on a lost packet. Mitigations: a dedicated 5 GHz access point (or the Spark's own Wi-Fi 7 radio), resizing images on the Orin NX before sending, and RTC (real-time chunking) in LeRobot to mask latency. **Bench-test the round-trip distribution on your actual network before relying on it.**

**Bimanual caveat, as on Thor:** public SO-101 checkpoints are single-arm, so every step starts with your own two-arm demonstrations.

## 5. Navigation

Nav2 + RTAB-Map in localization-only mode + D435i + STS3215 wheel-encoder odometry, entirely onboard. This is the part of the stack with the most evidence: [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) ran it on a *weaker* Orin Nano on this robot. Language goals compose the same way as on Thor: named poses for "the kitchen table", and `point_at` → depth → Nav2 goal for "the red chair", which on the Orin NX needs the Spark for the pointing step. The [bring-up plan](xlerobot-nav-manip-teleop-bringup.md) covers the D435i bracket and the turn-then-approach constraint of a non-holonomic base.

## 6. Platform settings that matter

- **Power mode: avoid the 10 W mode, and don't assume Super Mode.** Known issue **6236259** on Jetson Linux r39.2: dropping EMC below max during boot "can cause system crashes upon reboot," and Orin NX 16 GB at **10 W** is named. Seeed's J401 carrier guide says **not to enable MAXN SUPER** on the Orin NX because the carrier can't cool it, so the 157 TOPS headline depends on the carrier ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md), [Jetson ladder](../platforms/jetson-module-ladder-power-performance.md)). The 25 W or 40 W modes are the working range.
- **Power draw is the Orin NX's advantage.** The compute budget is 10–40 W vs Thor's 70 W cap, a much smaller share of the 288 Wh pack. Running the heavy models on the Spark means the robot's battery doesn't pay for them.
- **JetPack / Isaac ROS:** either stay on **JetPack 6.2 + Isaac ROS 3.2 (Humble)**, or reflash to **JetPack 7.2 + Isaac ROS 4.6 (Jazzy) / 5.0 (Lyrical)**. The Orin NX isn't individually named in Isaac ROS's platform table ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)).

## 7. Orin NX vs Thor for this robot

| | **Orin NX 16 GB + Spark** (this page) | **Thor, all onboard** ([page](xlerobot-thor-model-stack.md)) |
|---|---|---|
| Binding constraint | **Memory** (16 GB unified) + network | **GPU time** at the 70 W mode |
| Where the VLA runs | Spark (~6–9 Hz GR00T est. on Wi-Fi) | Onboard (~6–7 Hz GR00T est. at 70 W; 10.9 Hz at 120 W) |
| Planner | E2B/E4B onboard, escalates to 31B | E4B/12B onboard |
| Spatial grounding | Spark | Onboard |
| Works with no network | Speech, stop, small planner, nav, **ACT skills** | Everything |
| Compute power | **10–40 W** | 70 W cap (40–130 W range) |
| Compute cost | ~$600 module (+ the Spark you already have) | $3,499 dev kit |

The [GR00T-over-ZMQ page](gr00t-spark-zmq-xlerobot.md) made the key observation: **the Orin NX + Spark gets roughly the same VLA replan rate as a Thor**, on hardware that stays on the desk and serves the whole fleet. What Thor buys is **independence from the network**. That matters most for a robot that leaves Wi-Fi range or has to be dependable in a home. It matters little on a bench.

## 8. Experiments that would fill wiki gaps

1. **Measured memory budget:** `tegrastats` with the full onboard set running (§1). Replaces six estimates with one number.
2. **Gemma-4-E2B vs E4B on the Orin NX:** tokens/sec, time to first token, and tool-call accuracy on a fixed set of 50 spoken commands. There's no Orin NX figure for any Gemma 4 size.
3. **CPU ASR on the Orin NX** (sherpa-onnx vs Whisper small): real-time factor and word error rate with the servos and fan running.
4. **Wi-Fi round-trip distribution to the Spark** for GR00T and SmolVLA: the number that decides whether off-board manipulation is reliable enough.
5. **SmolVLA onboard on the Orin NX:** confirms or refutes the extrapolation that it's still too slow (1.4 Hz on the Nano).

## Related

- [XLeRobot on Thor — model stack](xlerobot-thor-model-stack.md) — the all-onboard counterpart; speech design detail lives there.
- [XLeRobot bring-up plan](xlerobot-nav-manip-teleop-bringup.md) — the Orin NX nav, manipulation and teleop plan this page extends.
- [Fleet agentic framework](fleet-agentic-framework.md) — the edge-agent + Spark-hub architecture this instantiates.
- [GR00T on Spark over ZMQ](gr00t-spark-zmq-xlerobot.md) — the off-board policy latency estimate.
- [Onboard compute for XLeRobot](../platforms/jetson-onboard-compute-xlerobot.md), [Jetson module ladder](../platforms/jetson-module-ladder-power-performance.md), [GR00T inference on Jetson](../platforms/gr00t-inference-on-jetson.md), [Hailo vs Jetson](../platforms/hailo-npu-vs-jetson-xlerobot.md).
- [Gemma 4](../../entities/gemma4.md), [Embodied-reasoning VLMs](../../concepts/learning/embodied-reasoning-vlms.md), [Control-rate ladder](../platforms/control-rate-ladder.md).

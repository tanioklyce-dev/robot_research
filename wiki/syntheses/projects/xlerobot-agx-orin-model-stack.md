---
title: XLeRobot on Jetson AGX Orin 64 GB — model stack for speech, reasoning, navigation and manipulation
type: synthesis
created: 2026-09-28
updated: 2026-09-28
tags: [xlerobot, agx-orin, dgx-spark, model-selection, speech, asr, tts, wake-word, gemma4, molmo2-er, nav2, rtab-map, act, smolvla, groot, molmoact2, hybrid-inference, memory-budget, power-modes, projects]
---

# XLeRobot on Jetson AGX Orin 64 GB — model stack

The third tier for the same requirements: **spoken commands, reasoning, navigation and manipulation** on an [XLeRobot](../../entities/xlerobot.md) (2× [SO-ARM101](../../entities/so-arm101.md), 2-wheel differential base, D435i, 288 Wh pack). The counterparts are the [Orin NX 16 GB + Spark stack](xlerobot-orin-nx-model-stack.md) and the [Thor stack](xlerobot-thor-model-stack.md).

**Thesis: everything fits, and nothing is fast.** The AGX Orin 64 GB is the cheapest tier where **the whole stack runs onboard with no network**, including a 3B VLA, the ER pointing model and a 12B-class planner. It is the Orin NX's memory problem solved. But its GPU gives roughly **half of Thor's measured VLA throughput**: GR00T N1.6 at **173 ms / 5.8 Hz** vs Thor's 92 ms / 10.9 Hz, both official TensorRT ([GR00T on Jetson](../platforms/gr00t-inference-on-jetson.md)). The battery power modes then cut GPU clock further. Over good Wi-Fi, a [Spark-served GR00T](gr00t-spark-zmq-xlerobot.md) (~6–9 Hz estimated) is probably **faster than running it onboard** at a battery mode.

So the natural design is a **hybrid where each side is optional**, the inverse of the Orin NX:

- **On the Orin NX**, the Spark is *required* for anything beyond ACT.
- **On the AGX Orin**, the robot is **fully capable offline**, and the Spark is an **accelerator** it uses when reachable.
- **On Thor**, the Spark is unnecessary for inference.

## The stack

```
 ONBOARD (AGX Orin 64 GB) — the complete stack                       OPTIONAL (DGX Spark)
 ──────────────────────────────────────────────                       ────────────────────
 mic array ─► wake word + VAD ─► ASR ──┐                  (CPU)
                  │                    ▼
                  └─► "stop" KWS ─► halt topic            (CPU, no network, no LLM)
                                       │
         Gemma-4-E4B / 12B planner ◄───┘ ─── escalate (optional) ───► Gemma-4-31B
                  │  (tool calls → ROS 2↔MCP server)
                  ├─► point_at(obj) ─► Molmo2-ER-4B                    (onboard)
                  ├─► goto(pose)    ─► Nav2 + RTAB-Map + D435i         (CPU)
                  ├─► pick(obj)     ─► ACT / SmolVLA / GR00T N1.7      (onboard)
                  │                     └── if Spark reachable ──────► GR00T N1.7 (faster)
                  └─► say(text)     ─► TTS                             (CPU)
```

| Layer | Onboard | Spark (optional) | Status in the wiki |
|---|---|---|---|
| **Speech in** | Wake word + VAD + voice-stop (CPU, always on); ASR on the CPU or a brief GPU burst | — | Tools named, **none measured** |
| **Planner** | **Gemma-4-E4B**; **12B** if you want native audio *and* more reasoning | 31B for escalation | E2B measured on Orin Nano; **AGX Orin rates extrapolated** (§3) |
| **Spatial grounding** | **Molmo2-ER-4B** | — | **Not measured on Jetson** |
| **Navigation** | Nav2 + RTAB-Map + D435i + wheel odometry | — | Measured on a weaker board |
| **Manipulation** | **ACT → SmolVLA → GR00T N1.7**, all onboard | GR00T N1.7 when faster | **GR00T 5.8 Hz measured** (N1.6, power mode unstated) |
| **Speech out** | TTS on the CPU | — | Named only |

## 1. Memory: the constraint that went away

At 64 GB, the question is whether everything can stay **resident**, so no phase pays a model-load delay. It can:

| Resident | Estimate | Basis |
|---|---|---|
| OS + ROS 2 + RTAB-Map + Nav2 + 3 cameras | ~4–5 GB | **Estimate** (same as the [Orin NX budget](xlerobot-orin-nx-model-stack.md#1-the-memory-budget)) |
| KWS + VAD + ASR + TTS | ~0.5 GB | **Estimate** |
| Gemma-4-E4B planner | ~4–5 GB | **Estimate**; E2B measured at 2.7 GB on an Orin Nano ([Gemma 4 card](../../sources/gemma-4-e2b-model-card.md)) |
| *or* Gemma-4-12B (4-bit) | ~7–8 GB | **Estimate** |
| Molmo2-ER-4B (bf16) | ~8–9 GB | **Estimate** from parameter count |
| GR00T N1.7-3B | ≤16 GB | The repo's stated **inference floor of 16 GB** ([Isaac-GR00T repo](../../sources/isaac-gr00t-github.md)); a floor, not the resident size |
| SmolVLA + one ACT checkpoint | ~1.5 GB | **Estimate** |
| **Total, everything resident** | **~35–40 GB** | ~25 GB headroom |

MolmoAct2-SO100_101 (~16 GB bf16; [model card](../../sources/molmoact2-so100-101-model-card.md)) would fit as well, in place of GR00T or alongside it. AGX Orin 64 GB is one of the two tiers the wiki names as plausible for 5B-class VLAs ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)).

## 2. Power modes: memory clock survives, GPU clock doesn't

The AGX Orin 64 GB's `nvpmodel` table ([Jetson module ladder](../platforms/jetson-module-ladder-power-performance.md), from NVIDIA's [Orin power chapter](../../sources/nvidia-jetson-platform-power-performance-orin.md)):

| Mode | Budget | CPU | GPU max | Memory max |
|---|---|---|---|---|
| MAXN (default) | ~60 W | 12 cores @ 2202 MHz | **1301 MHz** | 3200 MHz |
| **50 W** | 50 W | 12 @ 1498 | **816 MHz** (−37%) | **3200** |
| 30 W | 30 W | 8 @ 1728 | 612 MHz (−53%) | **3200** |
| 15 W | 15 W | 4 @ 1114 | 408 MHz | 2133 — ⚠️ **avoid** |

Two readings:

- **The memory clock holds at full speed down to 30 W.** Batch-1 VLA inference and LLM decoding are largely memory-bandwidth-bound ([GR00T-over-ZMQ §1](gr00t-spark-zmq-xlerobot.md) makes that argument), so the **−37% GPU clock at 50 W probably costs less than −37% throughput**. How much less is unmeasured. The Thor-vs-AGX gap (1.9× slower on 0.75× the bandwidth) shows compute also matters, so it is not purely bandwidth.
- **Avoid 15 W.** Jetson Linux r39.2 known issue **6236259** (reboot crashes after dropping memory clock below max at boot) names **AGX Orin at 15 W**. It also halves memory clock, the one resource the other modes preserve.

**Recommendation: 50 W as the working mode.** It keeps full CPU core count and full memory clock, and has the best chance of holding a usable VLA rate. Drop to 30 W for long idle or navigation-only stretches; `nvpmodel` switches at runtime. On the 288 Wh pack, the AGX Orin's 15–60 W envelope is **feasible but shortens runtime** ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)). That is roughly a third less compute draw than a Thor capped at 70 W, and several times an Orin NX.

## 3. Speech and reasoning

**Speech** follows the [Thor design](xlerobot-thor-model-stack.md#1-speech-io) unchanged:

- The wake word, VAD and **voice-stop keyword run always-on on the CPU**, and the stop goes **straight to a halt topic**.
- Use a far-field mic array away from the servos and fan, with echo cancellation.
- Default to **Pipeline A** (separate ASR → text), so every command has a transcript to confirm and log. Gemma's native audio input is the experiment.
- The AGX Orin's **12 A78AE cores** (8 at 30 W) give ASR plenty of CPU room.

As on every tier, the wiki names the speech tools (sherpa-onnx, Whisper, Parler-TTS) but has measured none of them.

**Planner speed, estimated.** The only measured Gemma 4 number on a Jetson is **E2B on an Orin Nano GPU: 24.2 tok/s decode, 0.9 s to first token, 2.7 GB** ([Gemma 4 card](../../sources/gemma-4-e2b-model-card.md)). Decode is bandwidth-bound, and the AGX Orin has **2× the Orin Nano's memory bandwidth** (204.8 vs 102 GB/s) and 2× the GPU cores. Scaling by bandwidth alone:

| Model | Estimated decode on AGX Orin | 40-token tool call |
|---|---|---|
| Gemma-4-E2B | ~45 tok/s | ~1–1.5 s |
| **Gemma-4-E4B** | ~20–25 tok/s | ~2–3 s |
| Gemma-4-12B (4-bit) | ~10–15 tok/s | ~3–5 s |

> [!warning] Extrapolated from one measurement on a different board
> Every row is the Orin Nano E2B figure scaled by the bandwidth ratio and weight size. The runtime (LiteRT-LM vs llama.cpp vs vLLM), quantization and power mode will each move these numbers.

- **Gemma-4-E4B** is the default: fast enough for turn-by-turn tool calls, and it has audio.
- **Gemma-4-12B** is the reason to prefer this tier over the Orin NX for reasoning. It is the **largest Gemma 4 with native audio**, and it fits comfortably. The cost is 2× slower decode.
- **Escalating to 31B on the Spark** is optional here, not structural as on the Orin NX.

**Spatial grounding: [Molmo2-ER-4B](../../entities/molmo2-er.md) onboard**, as a `point_at` tool (see [embodied-reasoning VLMs](../../concepts/learning/embodied-reasoning-vlms.md)). There is no Jetson measurement. It is GR00T-backbone-sized, so expect a pointing call to take a noticeable fraction of a second to a few seconds. That is fine for a one-shot query.

## 4. Manipulation — onboard by default, Spark when faster

| Step | Policy | Onboard rate | With the Spark | Evidence |
|---|---|---|---|---|
| 1 | **[ACT](../../entities/act.md)**, per skill | ≥27.8 Hz | — | 36 ms on an Orin Nano ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)) |
| 2 | **[SmolVLA](../../entities/smolvla.md)** (450M) | **Unmeasured**; a few Hz plausible | Faster | 1.4 Hz on an Orin Nano, bottlenecked by the iterative action expert; AGX Orin has ~2× the GPU cores and bandwidth |
| 3 | **[GR00T N1.7](../../entities/nvidia-groot.md)** (3B) | **5.8 Hz** official TensorRT (N1.6, mode unstated); **~3.5–5 Hz at 50 W** (est.) | ~6–9 Hz Wi-Fi, ~8–10 Hz wired (est.) | [GR00T on Jetson](../platforms/gr00t-inference-on-jetson.md), [GR00T over ZMQ](gr00t-spark-zmq-xlerobot.md) |
| exp. | **[MolmoAct2-SO100_101](../../entities/molmoact2.md)** (5B) | **Unmeasured**; fits in memory | — | No Jetson support in the repo; runs as a FastAPI server, here onboard |

- **ACT stays the reflex layer.** It's fast on every tier, and it's the baseline for judging whether the bigger policies are worth their latency.
- **SmolVLA onboard is plausible here and not on the Orin NX.** Run it through LeRobot's async inference so the arm keeps executing the current chunk while the next one computes. Measure before relying on it.
- **GR00T onboard is slow but works.** With chunked execution (the LeRobot rollout executes 8–16 actions per call), ~4–6 Hz is adequate for tabletop picks. The cost is reactivity, not smoothness. When the Spark is reachable, route GR00T there. Keep the onboard copy loaded, so a Wi-Fi drop mid-task degrades speed but doesn't stop the robot.
- **One unmeasured upside.** The [Seeed × NVIDIA DLI course](../../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) documents a **seven-engine full-graph TensorRT build of GR00T 1.7 on AGX Orin under JetPack 7.2**. The official path compiles only the action head. No latency was published, but it's the likeliest route to beating 5.8 Hz on this board ([GR00T on Jetson](../platforms/gr00t-inference-on-jetson.md#a-full-graph-tensorrt-path-exists-unbenchmarked)).

**Bimanual caveat, as on the other tiers:** public SO-101 checkpoints are single-arm, so every step starts with your own two-arm demos.

## 5. Navigation and scheduling

**Navigation** is identical to the other tiers: Nav2 + RTAB-Map in localization mode + D435i + STS3215 wheel odometry, CPU-bound, proven on a weaker board ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md), [bring-up plan](xlerobot-nav-manip-teleop-bringup.md)). Language goals compose through named poses or `point_at` → depth → Nav2, and here the pointing step stays onboard.

**Scheduling matters more than on Thor.** It is the same by-phase schedule as the [Thor stack](xlerobot-thor-model-stack.md#5-scheduling-on-a-70-w-gpu-budget): listen on the CPU, then ASR and planner bursts, then driving on the CPU, then the VLA sustained. But at half Thor's throughput, **a planner decoding while GR00T runs would slow both noticeably**. A new spoken command mid-grasp should **pre-empt** the skill, or queue, rather than run concurrently.

## 6. Platform notes

- **Form factor.** The dev kit is larger than the Orin NX module and uses an active heatsink-fan, and the AGX tier needs its own carrier. It is not the Nano's drop-in upgrade path ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)). The fan also puts the robot's loudest noise source near wherever the dev kit sits, so plan the mic mount around it.
- **Software.** Isaac ROS 4.6+/5.0 supports Jetson Orin on **JetPack 7.2**, and AGX Orin is one of the boards NVIDIA explicitly verifies ([Isaac ROS release notes](../../sources/isaac-ros-release-notes-and-platforms.md)). The GR00T full-graph TensorRT recipe above is also JetPack 7.2.
- **Price.** **$3,499** dev kit (was $1,999; +75% in NVIDIA's [2026-07 increase](../../sources/nvidia-jetson-faq-pricing.md), the largest in the line), or **$2,999** for the bare 64 GB module (1KU) on a third-party carrier. That is between the Orin NX ($999 module) and Thor ($5,499).

## 7. The three tiers side by side

| | **Orin NX 16 GB + Spark** ([page](xlerobot-orin-nx-model-stack.md)) | **AGX Orin 64 GB** (this page) | **Thor T5000** ([page](xlerobot-thor-model-stack.md)) |
|---|---|---|---|
| Binding constraint | **Memory** + network | **GPU throughput** at battery modes | GPU time at the 70 W mode |
| Spark's role | **Required** beyond ACT | **Optional accelerator** | Training only |
| GR00T N1.7 rate | ~6–9 Hz (Spark, Wi-Fi est.) | **5.8 Hz** measured (mode unstated); ~3.5–5 Hz at 50 W est.; Spark when faster | 10.9 Hz official, 22–24 Hz community; ~6–7 Hz at 70 W est. |
| Planner onboard | E2B/E4B | **E4B / 12B** | E4B / 12B |
| Pointing (Molmo2-ER) | Spark | **Onboard** | Onboard |
| Works with no network | Speech, stop, small planner, nav, ACT | **Everything, slower** | Everything |
| Compute power | 10–40 W | **15–60 W** (50 W working) | 70 W cap (40–130 W) |
| Price (NVIDIA list, 2026-09) | $999 module | **$3,499** dev kit | $5,499 dev kit |

**Which to pick.** If the robot always runs near a Spark, the **Orin NX** gets about the same VLA rate for under a third of the price ($999 vs $3,499) and much less power. If the robot has to be **fully capable offline** (a home deployment, Wi-Fi dead zones, demos away from the lab), the **AGX Orin** is the cheapest way to get there. **Thor** buys speed on top of independence. The AGX Orin is the right answer when offline capability matters more than VLA speed, which is plausible for an assistive robot doing tabletop tasks at human pace.

## 8. Experiments that would fill wiki gaps

1. **GR00T N1.7 on AGX Orin at MAXN, 50 W and 30 W, official vs full-graph TensorRT.** Six cells. Tests the "memory clock survives" argument (§2) and the full-graph upside.
2. **Onboard GR00T vs Spark over Wi-Fi, head to head** on the same task and network. Decides whether the hybrid routing in §4 is worth building.
3. **SmolVLA onboard with async inference**: the unmeasured middle step.
4. **Gemma-4-E4B and 12B tokens/sec on AGX Orin**: replaces §3's extrapolated table.
5. **MolmoAct2-SO100_101 onboard**: the first Jetson number for any MolmoAct2 checkpoint, on the smallest board it fits.

## Related

- [XLeRobot on Orin Nano 8 GB — model stack](xlerobot-orin-nano-model-stack.md) — the entry tier, and the only one measured on an XLeRobot. 8 GB leaves no comfortable room for even the 2.7 GB E2B planner beside navigation, so language understanding (ASR, planner, pointing) moves to the Spark. Offline mode is a **fixed spoken-command vocabulary mapped to ACT skills**, with no LLM. Has the four-tier table.
- [XLeRobot on Orin NX 16 GB — model stack](xlerobot-orin-nx-model-stack.md) and [XLeRobot on Thor — model stack](xlerobot-thor-model-stack.md): the other two tiers.
- [Onboard compute for XLeRobot](../platforms/jetson-onboard-compute-xlerobot.md), [Jetson module ladder](../platforms/jetson-module-ladder-power-performance.md), [GR00T inference on Jetson](../platforms/gr00t-inference-on-jetson.md), [GR00T over ZMQ from a Spark](gr00t-spark-zmq-xlerobot.md).
- [XLeRobot bring-up plan](xlerobot-nav-manip-teleop-bringup.md), [Fleet agentic framework](fleet-agentic-framework.md).
- [Gemma 4](../../entities/gemma4.md), [Embodied-reasoning VLMs](../../concepts/learning/embodied-reasoning-vlms.md), [Control-rate ladder](../platforms/control-rate-ladder.md).

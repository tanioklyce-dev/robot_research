---
title: GR00T inference on Jetson — Orin NX 16 GB vs AGX Orin 64 GB vs AGX Thor
type: synthesis
created: 2026-07-08
updated: 2026-08-27
tags: [gr00t, jetson, jetson-thor, agx-orin, orin-nx, inference, tensorrt, vla, edge-ai, platforms]
---

# GR00T inference on Jetson — Orin NX 16 GB vs AGX Orin 64 GB vs AGX Thor

How fast does [GR00T](../../entities/nvidia-groot.md) actually run on the three Jetson tiers people ask about? Short version: **Thor is real-time-usable (~11 Hz official TensorRT, ~23 Hz community-optimized), AGX Orin 64 GB is marginal (~6 Hz), and Orin NX 16 GB has no published numbers and sits below the model's stated memory floor** — plan on off-board inference there.

This page answers the open question previously flagged on [Jetson Thor](../../entities/jetson-thor.md) ("real measured GR00T throughput on Thor").

## The numbers

End-to-end camera→action-chunk latency, `nvidia/GR00T-N1.6-3B`, batch 1 ([Isaac GR00T TensorRT docs](../../sources/isaac-gr00t-tensorrt-deployment-docs.md)); community numbers from [NVIDIA forums, May 2026](../../sources/nvidia-forum-thor-realtime-vla-inference.md):

| Platform | PyTorch eager | Official TensorRT | Community (custom CUDA) |
|---|---|---|---|
| **AGX Thor** | 117 ms (8.6 Hz) | **92 ms (10.9 Hz)** | **41–45 ms (22–24 Hz)** |
| **AGX Orin 64 GB** | 300 ms (3.3 Hz) | **173 ms (5.8 Hz)** | — |
| **Orin NX 16 GB** | not published | not published | — |
| RTX 5090 (reference) | 58 ms (17.3 Hz) | 31 ms (32.1 Hz) | 12.5–13 ms (76–80 Hz) |

> [!warning] These are N1.6 numbers, not N1.7
> The official table benchmarks **GR00T-N1.6-3B** (export script `export_onnx_n1d6.py`); the forum thread covers "N1.6/1.7". N1.7 keeps the 3B dual-system shape but expands **action horizon 16 → 40 and state/action dims 29 → 132** ([Isaac-GR00T repo](../../sources/isaac-gr00t-github.md)), which plausibly raises action-head cost. No N1.7-specific latency has been published anywhere the wiki has seen (as of 2026-07-08).

## Reading the table

**Replan rate ≠ control rate.** GR00T emits action *chunks* (N1.7 horizon 40; LeRobot rollout executes 8–16 actions per call, optionally with RTC — [GR00T 1.7 LeRobot blog](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)). A 10.9 Hz replan loop therefore supports smooth manipulation; the number that suffers at low Hz is *reactivity* (how stale the current chunk is when the world changes).

**Thor** — the only comfortable tier. Official TensorRT gives 10.9 Hz, but the official path only compiles the DiT action head (VLM stays eager) and achieves an anomalously weak 1.27× speedup on Thor (vs 1.73–2.14× on other GPUs), with no NVFP4/FP8 path — so the [community 22–24 Hz result](../../sources/nvidia-forum-thor-realtime-vla-inference.md) is credible as the real ceiling-so-far, and Thor likely has more headroom once NVIDIA ships a Blackwell-tuned engine. 128 GB also fits multiple models concurrently ([Jetson Thor](../../entities/jetson-thor.md)).

**AGX Orin 64 GB** — officially supported ([Isaac-GR00T repo](../../sources/isaac-gr00t-github.md): inference 16 GB+ VRAM, Orin listed) and officially benchmarked: 5.8 Hz TensorRT / 3.3 Hz eager. With chunked execution that's workable for slow, non-reactive tabletop tasks; it is not comfortable for anything closed-loop. Memory is a non-issue (64 GB).

**Orin NX 16 GB** — the gap tier. Not in the repo's supported-inference list, not in the docs benchmark, no community numbers found. Two independent strikes:
1. **Memory**: the stated 16 GB+ VRAM floor equals the module's *entire* shared RAM — OS, ROS 2, and camera pipeline all compete for it.
2. **Compute**: 157 vs AGX Orin's 275 INT8 TOPS (~57%; [Jetson onboard-compute comparison](jetson-onboard-compute-xlerobot.md)) — naively scaling AGX Orin's 5.8 Hz gives **~2–3 Hz best case**, before memory pressure.

> [!note] Extrapolation, not measurement
> The ~2–3 Hz Orin NX figure is the wiki's inference from the AGX Orin benchmark and the TOPS ratio, not a sourced number.

The realistic Orin NX pattern is the one the stack is built for anyway: **run GR00T off-board and serve actions over the repo's ZMQ REQ/REP service (port 5555)** ([Isaac-GR00T repo](../../sources/isaac-gr00t-github.md), [ZeroMQ](../../entities/zeromq.md)), or run a smaller policy (ACT / SmolVLA-class) onboard — the same conclusion the [XLeRobot onboard-compute analysis](jetson-onboard-compute-xlerobot.md) reached from the power-budget side.

## A full-graph TensorRT path exists, unbenchmarked

Everything above measures the **official** recipe, which compiles only the DiT action head and leaves the VLM in PyTorch eager. The [Seeed × NVIDIA DLI course](../../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) (2026-08) documents a **seven-engine full-graph** alternative for GR00T 1.7 — `vit`, `llm_bf16`, `vl_self_attention`, `state_encoder`, `action_encoder`, `dit_bf16`, `action_decoder` — built at bf16/batch-1 on **both AGX Thor and AGX Orin under JetPack 7.2**, via a third-party fork pinned to a commit (`jjjadand/Isaac-GR00T-Orin-JP72` @ `dcf5f6b`).

**It publishes no latency number.** The `benchmark` step runs and the results appear only inside screenshots in the course text, so this changes nothing in the table above yet. What it does establish: compiling the VLM is not blocked, and the recipe is reproducible on both Orin and Thor. If someone runs it and it beats 10.9 Hz, that is a new row here — and it would partly explain the 1.27× Thor speedup anomaly, since a DiT-only compile leaves most of a 3B model uncompiled.

Two operational constraints from that source, both hard: **engines are strictly target-specific** (never copy Orin↔Thor; rebuild on any change to checkpoint, backbone, TensorRT version, precision, batch size, action horizon, or graph shapes), and **JetPack 7.2 ships no working USB-CAN kernel modules** — a CAN-bus robot arm will not enumerate on a stock Thor without out-of-tree `gs_usb.ko` / `peak_usb.ko`.

## Bottom line

| Want to run GR00T… | Verdict |
|---|---|
| on **AGX Thor** | ✅ Yes — 10.9 Hz official, ~23 Hz demonstrated; the intended deploy target with headroom left. |
| on **AGX Orin 64 GB** | ⚠️ Works, slowly — 5.8 Hz TensorRT; fine for chunked, non-reactive tasks. |
| on **Orin NX 16 GB** | ❌ Not onboard — below the memory floor, ~2–3 Hz extrapolated. Serve the policy over ZMQ from a desktop GPU / [DGX Spark](../../entities/dgx-spark.md) instead. |

## Related
- [Control-rate ladder](control-rate-ladder.md) — where GR00T's 5.8 / 10.9 / 22–24 Hz sit relative to every other rate in the wiki, from LLM planners at 0.2–0.4 Hz to servo loops at 1 kHz.

- [Isaac GR00T docs — TensorRT optimization](../../sources/isaac-gr00t-tensorrt-deployment-docs.md) — the official benchmark table (N1.6).
- [NVIDIA forums — real-time VLA inference on Thor & RTX](../../sources/nvidia-forum-thor-realtime-vla-inference.md) — the 22–24 Hz community result.
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the seven-engine full-graph build on Thor + AGX Orin, JetPack 7.2.
- [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md) — the same four tiers from the power-budget side.
- [Jetson module ladder — performance and power](jetson-module-ladder-power-performance.md) — the full-line spec/nvpmodel reference these tiers sit in; relevant to the open question below, since it shows Thor's sub-120 W modes cut the GPU 10 → 6 TPC (~−40 %), so the benchmark's power mode would materially move the 10.9 Hz figure.
- [GR00T on DGX Spark over ZMQ to XLeRobot](../projects/gr00t-spark-zmq-xlerobot.md) — the off-board serving path for the Orin NX, quantified (~7–10 Hz wired, ~5–8 Hz Wi-Fi).
- [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md) — where fine-tuning happens.
- [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) — the Orin *Nano* measured baseline for smaller policies (ACT 27.8 Hz, SmolVLA 1.4 Hz).

## Open questions

- N1.7-specific latency (horizon-40 action head) on any hardware.
- **What the seven-engine full-graph pipeline actually achieves on Thor.** The likeliest single source of a step change in this table, and the numbers exist — they were just never typed out.
- An NVFP4/FP8 GR00T engine for Thor — would likely close the 1.27×-speedup anomaly.
- Whether the community CUDA kernels get released or upstreamed.
- Power mode used in the official Jetson benchmarks (MAXN vs capped — matters for battery robots).

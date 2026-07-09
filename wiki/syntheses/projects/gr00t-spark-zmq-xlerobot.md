---
title: GR00T on DGX Spark, served over ZMQ to XLeRobot (Orin NX 16 GB) — performance estimate
type: synthesis
created: 2026-07-08
updated: 2026-07-08
tags: [gr00t, dgx-spark, zmq, xlerobot, orin-nx, off-board-inference, latency, vla, fleet, projects]
---

# GR00T on DGX Spark, served over ZMQ to XLeRobot (Orin NX 16 GB) — performance estimate

**Estimate (no published GR00T-on-Spark benchmark exists as of 2026-07-08): the [DGX Spark](../../entities/dgx-spark.md) should run GR00T-3B inference at roughly Thor-class latency (~90–120 ms per call), plus 10–40 ms of ZMQ/network overhead — an end-to-end replan loop of ~7–10 Hz wired, ~5–8 Hz over Wi-Fi.** With chunked action execution that is fully usable for [XLeRobot](../../entities/xlerobot.md)-class tabletop manipulation, and it matches the replan rate of putting a $3,499 [Thor](../../entities/jetson-thor.md) on the robot.

This is the off-board serving path recommended for the Orin NX 16 GB in [GR00T inference on Jetson](../platforms/gr00t-inference-on-jetson.md), and the policy-serving leg of the [fleet agentic framework](fleet-agentic-framework.md) (Spark hub + Orin NX robots).

## 1. Spark inference: ≈ Thor, not ≈ RTX 5090

Batch-1 inference of a 3B VLA is **memory-bandwidth-bound**, and Spark has the **same 273 GB/s LPDDR5X as Thor** ([DGX Spark](../../entities/dgx-spark.md), [Jetson Thor](../../entities/jetson-thor.md)). The [official GR00T benchmark table](../../sources/isaac-gr00t-tensorrt-deployment-docs.md) tracks bandwidth almost perfectly:

| Device | Mem BW | TensorRT latency |
|---|---|---|
| Jetson Thor | 273 GB/s | 92 ms (10.9 Hz) |
| RTX 4090 | ~1008 GB/s | 43 ms (23.3 Hz) |
| RTX 5090 | ~1792 GB/s | 31 ms (32.1 Hz) |

Spark's 2.4× CUDA-core count over Thor doesn't change this — its FP4 tensor throughput is actually about **half** of Thor's (1,000 vs 2,070 TOPS sparse; [DGX Spark](../../entities/dgx-spark.md)).

> [!note] Sanity check
> One N1.6 forward pass moves ~10–12 GB of BF16 weights (VLM pass + 4 DiT denoising steps) → ~36 ms theoretical floor at 273 GB/s. Thor measures 2.5× that floor (92 ms). Assuming Spark lands in the same 2.5–3× band gives **~90–120 ms (8–11 Hz)** with a TensorRT BF16 engine.

Practical notes: TensorRT engines are per-architecture — **build on the Spark itself** (~5–10 min, ~2 GB cache). Spark is ARM64 + CUDA 13; the [Isaac-GR00T repo](../../sources/isaac-gr00t-github.md) lists Spark in its inference matrix, and the [LeRobot GA blog](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) documents the `torch==2.11.0+cu130` pin.

## 2. The ZMQ hop: small if wired, the wildcard on Wi-Fi

The repo's service is **synchronous REQ/REP over TCP (port 5555), msgpack-numpy** ([Isaac-GR00T repo](../../sources/isaac-gr00t-github.md), [ZeroMQ](../../entities/zeromq.md)). The request carries the camera frames; the reply (an action chunk) is a few KB.

**Payload sizing matters**: at GR00T input resolution (~224–256², 2–3 cameras) a request is ~0.5 MB; raw 640×480 frames would be ~2.7 MB — **resize on the Orin NX before sending.**

| Cost | Wired GbE | Wi-Fi (5 GHz/6) |
|---|---|---|
| Capture + resize + msgpack on Orin NX | ~5 ms | ~5 ms |
| Uplink (~0.5 MB) | ~5 ms | ~10–25 ms typical; **jitter spikes to 100+ ms** |
| Action-chunk reply | ~1 ms | ~2 ms |

Because REQ/REP is synchronous, a stalled packet stalls the whole replan cycle (the client re-inits its socket only at the 15 s timeout). A dedicated 5 GHz AP — or the Spark's own Wi-Fi 7 radio — is the cheap mitigation.

## 3. End-to-end estimate

| Link | Round trip | Replan rate |
|---|---|---|
| Wired GbE | ~100–130 ms | **~8–10 Hz** |
| Good Wi-Fi | ~110–160 ms | **~6–9 Hz** |
| Congested Wi-Fi | 150–400 ms w/ spikes | 3–6 Hz, jittery |

## Is that enough?

**Yes, for what this robot does.** GR00T executes action *chunks* (LeRobot rollout runs 8–16 actions per call). At the STS3215 servos' ~30 Hz control rate, an 8-action chunk lasts ~270 ms — comfortably longer than the ~100–160 ms round trip, so the pipeline keeps up and the arm never waits.

What you pay is **reactivity**: actions execute ~150–250 ms after the observation they were computed from. Fast-moving targets and perturbation recovery suffer; LeRobot's **RTC (real-time chunking)** inference mode ([GR00T LeRobot blog](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)) exists to mask exactly this latency.

**The economic punchline**: this setup delivers essentially the same replan rate as mounting a Thor on the robot (10.9 Hz official TensorRT) — using hardware that stays on the desk, serves the whole fleet, and doesn't touch the XLeRobot's 288 Wh power budget ([onboard-compute analysis](../platforms/jetson-onboard-compute-xlerobot.md)). The only cost is Wi-Fi jitter risk.

## Uncertainties

- **No measured GR00T-on-Spark data exists** — the ±30% band on the inference estimate is real. (Also flagged as an open question on [DGX Spark](../../entities/dgx-spark.md).)
- **All anchors are N1.6** — N1.7's horizon-40 action head may cost more ([GR00T inference on Jetson](../platforms/gr00t-inference-on-jetson.md)).
- TensorRT-for-GR00T maturity on Spark's ARM64/CUDA-13 stack is unverified.
- Wi-Fi numbers assume a clean 5 GHz channel; congested-spectrum behavior is workload-dependent.

## Related

- [GR00T inference on Jetson](../platforms/gr00t-inference-on-jetson.md) — the measured on-Jetson numbers this extrapolates from.
- [Fleet agentic framework](fleet-agentic-framework.md) — the architecture this serving leg belongs to (Spark hub + Orin NX robots).
- [Isaac GR00T docs — TensorRT optimization](../../sources/isaac-gr00t-tensorrt-deployment-docs.md) — the bandwidth-tracking benchmark table.
- [ZeroMQ](../../entities/zeromq.md) — the transport (and the wiki's robot-transport map).
- [Jetson onboard compute for XLeRobot](../platforms/jetson-onboard-compute-xlerobot.md) — why nothing GR00T-sized rides on this robot.

## Open questions

- Actual GR00T latency on a DGX Spark (someone will publish it eventually; verify the ~90–120 ms band).
- Whether LeRobot's async/gRPC serving path (used by [Rosetta](../../entities/rosetta.md)) beats sync ZMQ REQ/REP under Wi-Fi jitter — architecturally it should (no head-of-line blocking).
- Measured Wi-Fi round-trip distribution on the actual fleet network.

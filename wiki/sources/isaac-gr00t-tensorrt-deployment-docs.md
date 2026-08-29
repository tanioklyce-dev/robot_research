---
title: Isaac GR00T docs — TensorRT optimization (deployment)
type: source
url: https://nvidia-isaac-gr00t.mintlify.app/deployment/tensorrt
author: NVIDIA (Isaac GR00T documentation)
published: rolling (living docs; snapshot 2026-07-08)
ingested: 2026-07-08
format: web (docs page)
tags: [gr00t, tensorrt, inference, deployment, jetson, thor, orin, benchmark, edge-ai]
---

# Isaac GR00T docs — TensorRT optimization (deployment)

## Summary

The official deployment-docs page for TensorRT-accelerating [GR00T](../entities/nvidia-groot.md) inference — and the first NVIDIA-published **measured GR00T latency table that includes Jetson hardware** ([Jetson Thor](../entities/jetson-thor.md) and Jetson AGX Orin). The recipe compiles **only the flow-matching DiT action head** to a TensorRT engine; the Cosmos-Reason VLM backbone (vision encoder + LM) stays in PyTorch eager. End-to-end result on Jetson: **Thor 117 → 92 ms (8.6 → 10.9 Hz, 1.27× speedup)** and **Orin 300 → 173 ms (3.3 → 5.8 Hz, 1.73×)**, versus ~31 ms (32.1 Hz) on an RTX 5090. Notably, the page benchmarks **`nvidia/GR00T-N1.6-3B`**, not N1.7 — the export script is literally `export_onnx_n1d6.py`.

## Key claims

- **Scope**: TensorRT compilation applies to the **DiT action head only**; vision encoder + language model remain PyTorch eager. So the "TensorRT speedup" is bounded by the action-expert share of end-to-end latency.
- **Benchmark table** (end-to-end, `nvidia/GR00T-N1.6-3B`, batch 1):

  | Device | PyTorch eager | TensorRT | Speedup | TRT rate |
  |---|---|---|---|---|
  | RTX 5090 | 58 ms (17.3 Hz) | 31 ms | 1.86× | 32.1 Hz |
  | H100 | 77 ms (13.0 Hz) | 36 ms | 2.14× | 27.9 Hz |
  | RTX 4090 | 82 ms (12.2 Hz) | 43 ms | 1.92× | 23.3 Hz |
  | **Jetson Thor** | 117 ms (8.6 Hz) | **92 ms** | 1.27× | **10.9 Hz** |
  | **Jetson Orin** | 300 ms (3.3 Hz) | **173 ms** | 1.73× | **5.8 Hz** |

- **Thor's speedup is the smallest in the table** (1.27× vs 1.73–2.14× everywhere else) — the engine looks under-tuned for Blackwell-on-Jetson relative to desktop GPUs; no NVFP4 path is offered despite it being Thor's headline format ([JetPack 7 reference](nvidia-jetpack-7-thor-whitepaper.md)).
- **Precision**: BF16 (recommended), FP16, FP32, FP8 — FP8 stated as "requires RTX 40-series or newer GPUs" (no explicit Jetson FP8/FP4 guidance).
- **Jetson support**: "Orin" (the 64 GB AGX variant, tested with reduced workspace) and Thor are the tested Jetson platforms, using Jetson AI Lab PyTorch builds. **Orin NX / Orin Nano are not mentioned.**
- **Mechanics**: `export_onnx_n1d6.py` → `build_tensorrt_engine.py` → `standalone_inference_script.py` / `benchmark_inference.py`. Workspace default 8192 MB (2048–16384 MB range); ~2 GB disk for engine cache; engines are **GPU-architecture-specific** (rebuild per target); 5–10 min build; first-inference warmup overhead.

## Entities mentioned

- [Jetson AGX Orin](../entities/jetson-agx-orin.md) — the platform behind the 173 ms / 5.8 Hz GR00T measurement.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — the model being deployed (N1.6-3B benchmarked).
- [Jetson Thor](../entities/jetson-thor.md), Jetson AGX Orin — the edge deploy targets with first official numbers.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — the VLM backbone left in eager mode.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — System-1/System-2 latency split made concrete: the compiled part is System 1 (DiT), the eager part is System 2 (VLM).
- [Flow matching](../concepts/learning/flow-matching.md) — the DiT action head being compiled.

## Open questions

- **The table is N1.6, not N1.7** — N1.7's action-horizon 16→40 and state/action-dim 29→132 expansion ([Isaac-GR00T repo](isaac-gr00t-github.md)) plausibly changes action-head cost; no N1.7 latency numbers published anywhere official yet.
- Whether "Orin" numbers used MAXN or a capped power mode — not stated; same for Thor's nvpmodel mode ([Thor power modes](nvidia-jetson-thor-platform-power-performance.md)).
- Why no NVFP4/FP8 path for Thor, and whether one is coming (would likely close the weak 1.27× gap).
- VLM-vs-action-head latency breakdown — not published, but decisive for what further optimization can buy.

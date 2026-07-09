---
title: NVIDIA Developer Forums — Real-time VLA inference on Thor & RTX (π0.5 / GR00T N1.6–1.7)
type: source
url: https://forums.developer.nvidia.com/t/real-time-inference-on-thor-rtx-pi0-5-gr00t-n1-6-1-7-thor-23-hz-rtx-5090-50-80hz/368788
author: "\"7thuniversels\" (community developer, NVIDIA Developer Forums)"
published: 2026-05-02
ingested: 2026-07-08
format: web (forum thread)
tags: [gr00t, pi0, jetson-thor, inference, cuda, real-time, community-benchmark, edge-ai]
---

# NVIDIA Developer Forums — Real-time VLA inference on Thor & RTX (π0.5 / GR00T N1.6–1.7)

## Summary

A community developer ("7thuniversels") reports **hand-optimized VLA inference numbers on [Jetson Thor](../entities/jetson-thor.md) and RTX 5090** using hand-written CUDA kernels tuned for small-batch, real-time execution — roughly **2× faster on Thor than the official TensorRT path** ([Isaac GR00T TensorRT docs](isaac-gr00t-tensorrt-deployment-docs.md): 92 ms / 10.9 Hz). Headline: **GR00T N1.6 at 41–45 ms (22–24 Hz) and π0.5 at 44 ms (23 Hz) on Thor**; 50–80 Hz on RTX 5090. Thread title covers "GR00T N1.6/1.7". Community-reported and unreplicated — treat as an existence proof of Thor headroom, not a vendor benchmark.

## Key claims

- **GR00T N1.6** (reported 2026-05-02):

  | Hardware | Latency | Rate | Config |
  |---|---|---|---|
  | Jetson AGX Thor | 45 ms | 22 Hz | T=50 |
  | Jetson AGX Thor | 41 ms | 24 Hz | T=16 |
  | RTX 5090 | 13.08 ms | 76 Hz | T=50 |
  | RTX 5090 | 12.53 ms | 80 Hz | T=16 |

- **π0.5** ([Physical Intelligence](../entities/physical-intelligence.md)): Thor (SM110) 44 ms / 23 Hz; RTX 5090 (SM120) 17.58 ms / 57 Hz.
- Approach: **hand-written CUDA kernels**, small-batch / real-time focus (vs the official path that only TRT-compiles the DiT head). A separate MLIR-TRT implementation reportedly reached ~70 ms on π0.5 (hardware unstated).
- Implication: Thor's practical GR00T ceiling is **~2× the official TensorRT number** — consistent with the official path's anomalously low 1.27× speedup on Thor.

> [!note] Confidence
> Single community reporter, no published code or replication in the thread as captured. The T=50/T=16 parameter (likely action horizon or denoising-step count) is not fully specified.

## Entities mentioned

- [Jetson Thor](../entities/jetson-thor.md) — deploy target; first >20 Hz GR00T-class numbers the wiki tracks on it.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — N1.6/1.7.
- [Physical Intelligence](../entities/physical-intelligence.md) — π0.5.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — edge real-time inference.

## Open questions

- What exactly T=50 vs T=16 denotes (action horizon vs denoising steps); precision used; whether the kernels will be released.
- Whether the same treatment lifts N1.7 (horizon 40, dims 132) to similar rates.

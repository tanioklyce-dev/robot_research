---
title: LiteRT
type: entity
subtype: product
created: 2026-08-27
updated: 2026-08-27
sources: 0
tags: [litert, tensorflow-lite, google, on-device, edge-ai, inference-runtime, xnnpack, npu, gemma4, quantization]
---

**Repos:** [`google-ai-edge/LiteRT`](https://github.com/google-ai-edge/LiteRT) (3,342★) · [`google-ai-edge/LiteRT-LM`](https://github.com/google-ai-edge/LiteRT-LM) (6,303★) — both Apache-2.0 · **Docs:** [ai.google.dev/edge/litert](https://ai.google.dev/edge/litert)

**LiteRT** — Google's on-device inference runtime, and the **direct successor to TensorFlow Lite**: *"LiteRT continues the legacy of TensorFlow Lite as the trusted, high-performance runtime for on-device AI."* **LiteRT-LM** is the layer above it for running LLMs on edge hardware. In this wiki LiteRT matters as **the runtime behind every measured on-device LLM number** — the [Gemma 4 E2B](gemma4.md) benchmarks on Raspberry Pi, [Jetson Orin Nano](jetson-orin-nano.md) and Qualcomm NPUs all come from it ([model card](../sources/gemma-4-e2b-model-card.md)).

## The two layers

- **LiteRT** provides the hardware acceleration: **XNNPack for CPU**, **ML Drift for GPU**, plus NPU delegates. Nightly builds; stable releases on a 6–8 week cadence. Also ships **LiteRT.js** (WebGPU/WASM in the browser), a C++ Tensor API, and a CLI.
- **LiteRT-LM** adds the GenAI-specific orchestration on top: **KV-cache management, prompt templating, and function calling**, in a `.litertlm` model format. It is the stack behind the Google AI Edge Gallery app.

> [!note] XNNPACK is a CPU backend, not an Apple thing
> Worth stating because a [secondary source](../sources/explainx-gemma-4-open-duck-mini.md) in this wiki described a LiteRT memory figure as measured *"on XNNPACK (Apple CPUs)."* XNNPack is Google's optimized **CPU** inference library for ARM and x86 generally — it is what runs when there is no GPU or NPU delegate available, which on a Raspberry Pi 5 is always.

## What it does to a model

Deployment through LiteRT-LM is not a pass-through — the model is converted and quantized ahead of time, which is why "same model, different runtime" changes the numbers:

- **Mixed-precision QAT.** Gemma 4's mobile scheme mixes **2-bit, 4-bit and 8-bit** weights. Text-only weight footprint drops to **~0.8 GB**, with **1.12 GB of embeddings memory-mapped** rather than resident, and the vision/audio encoders **loaded on demand**.
- **Runtime context limits bite before architectural ones.** Gemma 4 E2B is a 128K-context model; under LiteRT-LM it supports **32K**. The runtime's limit is the one that applies in the field.
- **Speculative decoding** is supported on CPU and GPU, mobile and desktop.

## Measured throughput ([Gemma 4 E2B](../sources/gemma-4-e2b-model-card.md))

| Device | Backend | Prefill (tok/s) | Decode (tok/s) | TTFT (s) | Memory (MB) |
|---|---|---|---|---|---|
| Raspberry Pi 5 16GB | **CPU** (XNNPack) | 133 | 7.6 | 7.8 | 1546 |
| [Jetson Orin Nano](jetson-orin-nano.md) | CPU | 109 | 12.2 | 9.4 | 3681 |
| [Jetson Orin Nano](jetson-orin-nano.md) | **GPU** (ML Drift) | 1,142 | 24.2 | 0.9 | 2739 |
| Qualcomm Dragonwing IQ8 | **NPU** | 3,747 | 31.7 | 0.3 | 1869 |

The spread across backends on the *same* model is the reason this page exists: LiteRT is where "runs on the edge" becomes a specific number, and the delegate you land on decides it. See [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md).

## Position vs the wiki's other runtimes

| | Target | Typical use here |
|---|---|---|
| **LiteRT / LiteRT-LM** | mobile + embedded Linux; CPU/GPU/NPU delegates | Google's edge models ([Gemma 4](gemma4.md)) on phones, Pi, Jetson |
| [Ollama](ollama.md) / llama.cpp | desktop + workstation, GGUF | the wiki's local-LLM-agent projects |
| ONNX Runtime | cross-framework, CPU/CUDA/TensorRT | [Microduck](microduck.md)'s 50 Hz control policies |
| TensorRT | NVIDIA only, ahead-of-time engines | [GR00T](nvidia-groot.md) on Jetson |

## Related

- [Gemma 4](gemma4.md) — the model family whose edge deployment runs on it
- [Jetson Orin Nano](jetson-orin-nano.md) — the board where its CPU/GPU gap is measured
- [Open Duck Mini](open-duck-mini.md) — ran Gemma 4 E2B on LiteRT at Google I/O 2026
- [Ollama](ollama.md) — the workstation-tier alternative
- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)

## Mentioned in

- [Gemma 4 E2B model card + LiteRT benchmarks](../sources/gemma-4-e2b-model-card.md) — the quantization scheme, the per-device table, and the 32K runtime context limit.
- [Gemma 4 Powers Open Duck Mini (explainx.ai)](../sources/explainx-gemma-4-open-duck-mini.md) — LiteRT as the duck's inference layer; also the source of the XNNPACK misdescription corrected above.

## Open questions

- **No robotics-specific latency figures.** Everything measured is text generation. A robot that listens, sees and answers pays ASR, vision-encoder and TTS costs that no published LiteRT benchmark covers.
- **NPU delegate coverage is unclear** beyond the Qualcomm row — nothing states whether a Rockchip [NPU](../glossary.md) like [Microduck](microduck.md)'s is reachable from LiteRT at all, or whether that path is vendor-toolchain-only.

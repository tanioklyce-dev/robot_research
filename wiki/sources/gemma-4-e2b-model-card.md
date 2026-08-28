---
title: "Gemma 4 E2B — Google model card + LiteRT-LM edge benchmarks (HF primaries)"
type: source
url: https://huggingface.co/google/gemma-4-E2B-it
author: Google DeepMind
affiliation: Google
published: 2026-03-02
ingested: 2026-08-27
venue: Hugging Face Hub
license: Apache-2.0
format: two model cards — google/gemma-4-E2B-it (architecture) + litert-community/gemma-4-E2B-it-litert-lm (on-device benchmarks)
tags: [gemma4, google, edge-ai, on-device, litert, xnnpack, quantization, raspberry-pi-5, jetson-orin-nano, benchmarks, multimodal]
---

# Gemma 4 E2B — the primaries

> [!note] Why this page exists
> Ingested to settle claims made by a [secondary article](explainx-gemma-4-open-duck-mini.md) about the Google I/O 2026 Open Duck Mini demo, and to close two standing open questions on the [Gemma 4](../entities/gemma4.md) entity page: *"primary Google Gemma 4 release/paper not ingested"* and *"no tokens/sec benchmarks per Jetson/Spark tier."* Both are answered here. Companion primaries: the Gemma 4 tech report is **arXiv 2607.02770** (not yet ingested).

## Architecture ([google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it))

**Five sizes**, not four: **E2B, E4B, 12B, 26B A4B, 31B**. Apache-2.0. HF repo created **2026-03-02**.

| Property | E2B | E4B | 12B Unified | 26B A4B | 31B Dense |
|---|---|---|---|---|---|
| Parameters | **2.3B effective** (5.1B with embeddings) | 4.5B effective (8B w/ emb) | 11.95B | 25.2B total / **3.8B active** | 30.7B |
| Context | **128K** | 128K | 256K | 256K | 256K |
| Sliding window | 512 | 512 | 1024 | 1024 | 1024 |
| Vision encoder | ~150M | ~150M | — | — | ~550M |
| Audio encoder | ~300M | ~300M | — | — | **no audio** |

Verified against the repo's own `safetensors` metadata: **5,123,178,051 BF16 parameters** for E2B.

Two naming conventions that are routinely misread, and the card states both explicitly:

> "The **'E' in E2B and E4B stands for 'effective' parameters.** The smaller models incorporate **Per-Layer Embeddings (PLE)** to maximize parameter efficiency in on-device deployments. Rather than adding more layers or parameters to the model, PLE gives each decoder layer its own small embedding for every token. These embedding tables are large but are only used for quick lookups, which is why the effective parameter count is much smaller than the total."

> "The **'A' in 26B A4B stands for 'active parameters'**… By only activating a 4B subset during inference, the MoE runs much faster than its 26B total might suggest."

Other architecture notes: hybrid attention interleaving local sliding-window with full global attention, final layer always global; global layers use unified K/V and Proportional RoPE (p-RoPE) to cut long-context memory. Modalities are **text, image (variable aspect ratio/resolution), video, and audio** — **audio on E2B, E4B and 12B only**. 140+ languages.

## On-device benchmarks ([litert-community/gemma-4-E2B-it-litert-lm](https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm))

This is the number set the wiki was missing. **IoT tier**, measured at 1024 prefill / 256 decode tokens, 2048 context:

| Device | Backend | Prefill (tok/s) | Decode (tok/s) | TTFT (s) | Model size (MB) | Memory (MB) |
|---|---|---|---|---|---|---|
| **Raspberry Pi 5 16GB** | CPU | 133 | **7.6** | **7.8** | 2583 | **1546** |
| **[Jetson Orin Nano](../entities/jetson-orin-nano.md)** | CPU | 109 | 12.2 | 9.4 | 2583 | 3681 |
| **Jetson Orin Nano** | **GPU** | **1,142** | **24.2** | **0.9** | 2583 | 2739 |
| Qualcomm Dragonwing IQ8 | **NPU** | **3,747** | **31.7** | **0.3** | 2967 | 1869 |

> [!note] The backend, not the board, is the story
> The same Orin Nano goes from **109 → 1,142 tok/s prefill** and **9.4 s → 0.9 s** time-to-first-token by moving off the CPU. And the Pi 5 has **no GPU row at all** — there is no usable accelerated backend for it here, so a Pi 5 deployment *is* the 7.6 tok/s / 7.8 s configuration. Treating "Pi 5" and "Orin Nano" as interchangeable edge targets for this model is a **~3× decode and ~9× TTFT** error.
>
> The NPU row is the sharper version of the same point: a Dragonwing IQ8 beats an Orin Nano's GPU on both prefill and decode while using **less memory than the Pi 5 uses on CPU**.

**Quantization.** LiteRT-LM uses a QAT scheme mixing **2-bit, 4-bit and 8-bit weights**: *"for text only use cases the weight footprint in memory can be as low as 0.8 GB while the runtime uses memory mapping to support the 1.12 GB of embedding parameters… Additionally the Vision and Audio models are loaded on demand to further reduce memory consumption."* That on-demand loading is why a multimodal run costs more than the text-only floor.

**Context on-device is 32K, not 128K:** *"The model can support up to 32k context length"* under LiteRT-LM — a runtime limit below the architecture's 128K.

**Runtime stack.** LiteRT provides hardware acceleration via **XNNPack for CPU** and **ML Drift for GPU**; LiteRT-LM adds KV-cache management, prompt templating and function calling. Memory measured with `rusage::ru_maxrss` on Android/Linux/Pi, `task_vm_info::phys_footprint` on iOS/macOS.

## Why it matters here

- It gives the wiki's [on-device/on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) ladder its **first measured rungs** rather than "targets Orin Nano."
- It sets a hard floor for **conversational** robot agents: at 7.6 tok/s decode, a 45-token spoken reply takes **~6 seconds** on a Pi 5 regardless of prompt length. Decode rate, not TTFT, is what a talking robot lives on.
- It confirms the E2B/E4B naming is about **effective** parameters — the single most-misquoted fact about this family.

## Entities mentioned

- [Gemma 4](../entities/gemma4.md) · [Jetson Orin Nano](../entities/jetson-orin-nano.md) · [Open Duck Mini](../entities/open-duck-mini.md)

## Concepts touched

- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)

## Open questions

- **The tech report (arXiv 2607.02770) is not ingested.** Training data, RL recipe and the PLE ablation live there.
- **No robot-relevant latency figures** — these are text-generation benchmarks. A duck that listens, looks and answers pays ASR + vision-encoder + TTS on top, and none of that is in the table.
- **Vision/audio encoder cost is unmeasured.** The cards say the encoders load on demand; nothing states what a multimodal turn costs in time or memory.

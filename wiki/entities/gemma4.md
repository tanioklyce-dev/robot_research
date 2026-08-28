---
title: Gemma 4
type: entity
subtype: model
created: 2026-07-04
updated: 2026-08-27
sources: 4
tags: [gemma4, vlm, google, multimodal, moe, edge-ai, on-device, vla-backbone-candidate]
---

**Gemma 4** — Google's 2026 open multimodal + multilingual model family; successor to [Gemma3](gemma3.md). Introduces the family's **first Mixture-of-Experts variant** and a size ladder spanning cloud to on-device, with native reasoning, code generation, **structured tool use (function calling)**, and interleaved multimodal input. Apache 2.0. In this wiki it matters as an **edge/on-robot reasoning-layer candidate** — the concrete model behind NVIDIA's on-device pitch ([edge blog](../sources/nvidia-gemma-4-edge-blog.md)).

## Variants
| Variant | Type | Params | Context | Multimodal |
|---|---|---|---|---|
| Gemma-4-31B | dense | 31B (256K ctx, 1024 sliding window) | 256K | — |
| Gemma-4-26B-A4B | **MoE (128 experts)** | 26B total / 3.8B active | 256K | — |
| Gemma-4-E4B | dense | 7.9B w/ emb / 4.5B effective | 128K | ✅ |
| Gemma-4-12B | dense | 11.95B | 256K | ✅ (incl. audio) |
| Gemma-4-E4B | dense | 8B w/ emb / 4.5B effective | 128K | ✅ |
| Gemma-4-E2B | dense | 5.1B w/ emb / 2.3B effective | 128K | ✅ |

## Edge deployment (via NVIDIA)
- **[Jetson Orin Nano](jetson-orin-nano.md)**: E2B + E4B; **[Jetson Thor](jetson-thor.md)** scales up; **[DGX Spark](dgx-spark.md)** runs the 31B in BF16; RTX/RTX PRO for desktop.
- Runtimes: [Ollama](ollama.md), vLLM, llama.cpp, NVIDIA NIM. **NVFP4** 4-bit quantization for the 31B via NVIDIA Model Optimizer.

## Measured on-device throughput ([LiteRT-LM card](../sources/gemma-4-e2b-model-card.md))

E2B under LiteRT-LM, 1024 prefill / 256 decode:

| Device | Backend | Prefill (tok/s) | Decode (tok/s) | TTFT (s) | Memory (MB) |
|---|---|---|---|---|---|
| Raspberry Pi 5 16GB | CPU | 133 | **7.6** | 7.8 | 1546 |
| [Jetson Orin Nano](jetson-orin-nano.md) | CPU | 109 | 12.2 | 9.4 | 3681 |
| [Jetson Orin Nano](jetson-orin-nano.md) | **GPU** | 1,142 | **24.2** | **0.9** | 2739 |
| Qualcomm Dragonwing IQ8 | **NPU** | 3,747 | 31.7 | 0.3 | 1869 |

Model size 2583 MB. Quantization is a QAT mix of **2/4/8-bit** weights — text-only weight footprint as low as **0.8 GB**, with 1.12 GB of embeddings memory-mapped and the vision/audio encoders loaded on demand. **On-device context is 32K** under LiteRT-LM, below the architecture's 128K.

The gap between the CPU and GPU rows on the *same* Orin Nano — ~10× prefill, ~9× TTFT — is the number to carry into any edge-agent sizing. And a Pi 5 has no GPU row: its 7.6 tok/s decode means a 45-token spoken reply takes ~6 s.

## Why it matters in this wiki
- **On-robot System-2 candidate**: the multimodal E2B/E4B variants + native function-calling fit the edge-agent-brain slot the wiki tracks ([Taking Flight drone](../sources/taking-flight-with-dialogue-px4-drone-agent.md) on [Ollama](ollama.md); [ROSOrin offline curriculum](../sources/hiwonder-rosorin-docs.md)). See the [on-device/on-robot agents synthesis](../syntheses/agents/on-device-and-on-robot-agents.md).
- **Backbone-lineage note**: [Gemma3](gemma3.md) 4B is the [π0.7](pi07.md) VLA backbone; Gemma 4 is the natural next candidate, though no wiki-tracked VLA uses it yet.

## Related
- [Gemma3](gemma3.md) — predecessor; [PaliGemma](paligemma.md) — earlier Gemma-based VLM.
- [VLA models](../concepts/learning/vla-models.md) — VLM-as-System-2 pattern.
- [DGX Spark](dgx-spark.md), [Jetson Orin Nano](jetson-orin-nano.md), [Ollama](ollama.md) — deployment substrate.

## Mentioned in
- [Gemma 4 edge blog (NVIDIA)](../sources/nvidia-gemma-4-edge-blog.md) — primary source (edge/on-device angle).
- [Gemma 4 E2B model card + LiteRT benchmarks](../sources/gemma-4-e2b-model-card.md) — **the Google primary**: five sizes, the "effective parameters" naming, and the first per-device tok/s figures in this wiki.
- [Gemma 4 Powers Open Duck Mini (explainx.ai)](../sources/explainx-gemma-4-open-duck-mini.md) — a secondary that gets E2B's parameter count and context window wrong; corrections tabulated there.
- [Gemini Robotics On-Device 2 model card](../sources/gemini-robotics-on-device-2-model-card.md) — GRoD 2 is built on "our on-device Gemma models", putting the Gemma line under DeepMind's edge VLA (size class unstated).

## Open questions
- ~~**Primary Google Gemma 4 release/paper not ingested**~~ — **done**: the [HF model card](../sources/gemma-4-e2b-model-card.md) is ingested and confirms the NVIDIA-sourced sizes, adds the **12B Unified** variant this page was missing, and settles that audio is E2B/E4B/**12B**. The tech report (**arXiv 2607.02770**) is still not ingested.
- ~~No tokens/sec benchmarks per Jetson/Spark tier.~~ **Partly done** — Pi 5 / Orin Nano / Dragonwing figures are above. Still nothing for **Thor**, **DGX Spark**, or the 31B tier.
- Whether any VLA adopts a Gemma 4 backbone.

---
title: Gemma 4
type: entity
subtype: model
created: 2026-07-04
updated: 2026-08-03
sources: 3
tags: [gemma4, vlm, google, multimodal, moe, edge-ai, on-device, vla-backbone-candidate]
---

**Gemma 4** — Google's 2026 open multimodal + multilingual model family; successor to [Gemma3](gemma3.md). Introduces the family's **first Mixture-of-Experts variant** and a size ladder spanning cloud to on-device, with native reasoning, code generation, **structured tool use (function calling)**, and interleaved multimodal input. Apache 2.0. In this wiki it matters as an **edge/on-robot reasoning-layer candidate** — the concrete model behind NVIDIA's on-device pitch ([edge blog](../sources/nvidia-gemma-4-edge-blog.md)).

## Variants
| Variant | Type | Params | Context | Multimodal |
|---|---|---|---|---|
| Gemma-4-31B | dense | 31B (256K ctx, 1024 sliding window) | 256K | — |
| Gemma-4-26B-A4B | **MoE (128 experts)** | 26B total / 3.8B active | 256K | — |
| Gemma-4-E4B | dense | 7.9B w/ emb / 4.5B effective | 128K | ✅ |
| Gemma-4-E2B | dense | 5.1B w/ emb / 2.3B effective | 128K | ✅ |

## Edge deployment (via NVIDIA)
- **[Jetson Orin Nano](jetson-orin-nano.md)**: E2B + E4B; **[Jetson Thor](jetson-thor.md)** scales up; **[DGX Spark](dgx-spark.md)** runs the 31B in BF16; RTX/RTX PRO for desktop.
- Runtimes: [Ollama](ollama.md), vLLM, llama.cpp, NVIDIA NIM. **NVFP4** 4-bit quantization for the 31B via NVIDIA Model Optimizer.

## Why it matters in this wiki
- **On-robot System-2 candidate**: the multimodal E2B/E4B variants + native function-calling fit the edge-agent-brain slot the wiki tracks ([Taking Flight drone](../sources/taking-flight-with-dialogue-px4-drone-agent.md) on [Ollama](ollama.md); [ROSOrin offline curriculum](../sources/hiwonder-rosorin-docs.md)). See the [on-device/on-robot agents synthesis](../syntheses/agents/on-device-and-on-robot-agents.md).
- **Backbone-lineage note**: [Gemma3](gemma3.md) 4B is the [π0.7](pi07.md) VLA backbone; Gemma 4 is the natural next candidate, though no wiki-tracked VLA uses it yet.

## Related
- [Gemma3](gemma3.md) — predecessor; [PaliGemma](paligemma.md) — earlier Gemma-based VLM.
- [VLA models](../concepts/learning/vla-models.md) — VLM-as-System-2 pattern.
- [DGX Spark](dgx-spark.md), [Jetson Orin Nano](jetson-orin-nano.md), [Ollama](ollama.md) — deployment substrate.

## Mentioned in
- [Gemma 4 edge blog (NVIDIA)](../sources/nvidia-gemma-4-edge-blog.md) — primary source (edge/on-device angle).
- [Gemini Robotics On-Device 2 model card](../sources/gemini-robotics-on-device-2-model-card.md) — GRoD 2 is built on "our on-device Gemma models", putting the Gemma line under DeepMind's edge VLA (size class unstated).

## Open questions
- **Primary Google Gemma 4 release/paper not ingested** — sizes confirmed via the NVIDIA blog; deepen with the model card when filed.
- No tokens/sec benchmarks per Jetson/Spark tier.
- Whether any VLA adopts a Gemma 4 backbone.

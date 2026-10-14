---
title: EmbeddingGemma 2
type: entity
subtype: model
created: 2026-10-13
updated: 2026-10-13
sources: 1
tags: [embeddinggemma-2, gemma4, google-deepmind, embeddings, multimodal, on-device, rag, matryoshka, apache-2.0]
---

**EmbeddingGemma 2** is Google DeepMind's open (Apache-2.0) **740M-parameter multimodal embedding model**, released 2026-10-06 and built on the [Gemma 4](gemma4.md) architecture. It puts text, code, images, video and audio into one vector space and is sized for on-device use ([launch blog](../sources/embeddinggemma-2-blog.md)).

## Specs (vendor-stated)

| | |
|---|---|
| Parameters | 740M = **270M text** + 170M vision + 300M audio (encoders optional) |
| Output dims | 768, Matryoshka-truncatable to 512 / 256 / 128 |
| Context | 8K tokens: ~5.5 min audio, 29 images or 58 video frames |
| RAM (quantised, Pixel 11 Pro) | **~191 MB** text-only · **~567 MB** full multimodal |
| Shares with Gemma 4 | text tokenizer and audio encoder, for a lower combined footprint |
| MTEB Code | 78.68 (v1: 68.76) |
| Licence | Apache 2.0 |

Runtimes: [LiteRT](litert.md), MediaPipe (including a Decision Task API), transformers / sentence-transformers, MLX, vLLM, llama.cpp, SGLang, [Ollama](ollama.md), transformers.js/WebGPU.

## Why it matters in this wiki

It is the on-device **memory index** for an agent whose generator is already on-device. With Gemma 4 E2B as the planner, the pair gives a robot multimodal recall of its own camera and audio history without a network. That is the gap in the [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) picture: the generator was sized and the retriever was not.

## Related
- [Gemma 4](gemma4.md) — the base architecture and intended generator pair.
- [Decision models](../concepts/agents/decision-models.md) — the MediaPipe Decision Task API on top of embeddings.

## Mentioned in
- [EmbeddingGemma 2 launch blog](../sources/embeddinggemma-2-blog.md)

## Open questions
- Model card (the actual benchmark tables) not ingested.
- No throughput figures (ms per frame or per audio second); none on Jetson / Pi / RK3588.
- Quality on egocentric robot video.

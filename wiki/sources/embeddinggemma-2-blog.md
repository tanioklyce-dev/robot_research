---
title: "EmbeddingGemma 2: an open, lightweight multimodal embedding model (Google blog)"
type: source
url: https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/
local_path: raw/2026-10-06-google-blog-embeddinggemma-2.md
sha256: 5d8b70110db227d895484ce5367d48222f43ce5d30144a1caea25992d351d343
author: Sahil Dua, Henrique Schechter Vera (Google DeepMind)
published: 2026-10-06
ingested: 2026-10-13
venue: Google Keyword blog (Developer tools)
format: "launch blog post, captured 2026-10-13 via curl with article-text extraction. The model card it links to was not ingested."
tags: [embeddinggemma-2, gemma4, google-deepmind, embeddings, multimodal, on-device, rag, retrieval, matryoshka, litert, mediapipe, apache-2.0, vendor-source, primary]
---

# EmbeddingGemma 2: an open, lightweight multimodal embedding model (Google blog)

## Summary

Google DeepMind released **[EmbeddingGemma 2](../entities/embeddinggemma-2.md)**, a **740M-parameter, Apache-2.0** embedding model built on the **[Gemma 4](../entities/gemma4.md) architecture**. It maps text, code, images, video and audio, alone or interleaved, into **one shared vector space**, and it is sized for phones. It is modular: a **270M** text core, with optional **170M vision** and **300M audio** encoders. **Matryoshka** truncation takes vectors from 768 down to 128 dimensions. The context window is **8K tokens**, about 5.5 min of audio, 29 images or 58 video frames. Quantised on a Pixel 11 Pro it needs **~191 MB** of RAM for text only and **~567 MB** for the full multimodal model. It shares Gemma 4's **text tokenizer and audio encoder**, so the embedder and the generator can run together in less memory than two separate models would need. For a robot, this is the missing **retrieval half of an on-device agent**: the component that answers "where did I last see the red mug?" from the robot's own camera and microphone history without leaving the device.

## Key claims

- **Scale and licence**: 740M parameters; Gemma 4 architecture; Apache 2.0. Its predecessor EmbeddingGemma (text-only) had **>20M downloads**.
- **Modular footprint**: text 270M + vision 170M + audio 300M (these sum to the 740M). "As little as 270M parameters for text-only workloads."
- **Matryoshka Representation Learning**: outputs at 768, 512, 256 or 128 dimensions, for "up to 6x storage reduction" in a local vector DB.
- **On-device memory** (quantised, Pixel 11 Pro): **~191 MB** text-only active RAM, **~567 MB** full multimodal.
- **Context**: **8K tokens**, 4× EmbeddingGemma 1. That is 5.5 min audio, 29 images, 58 video frames, or a mix.
- **Quality** (vendor-stated): "leading scores among sub-1B multimodal embedders" on **MTEB Code** and **MAEB** (audio). Text multilingual quality matches v1. **MTEB Code 68.76 → 78.68 (+9.92)** over v1. Outperforms "some specialist models more than twice its size." No comparison table is in the post; it points to the model card.
- **Pairing with Gemma 4**: shared text tokenizer and audio encoder mean a **lower combined memory footprint** for on-device RAG.
- **Deployment surface**: Hugging Face, Kaggle (Model Garden "coming soon"); [LiteRT](../entities/litert.md) and **MediaPipe** (embedding, retrieval and a **Decision Task API** for "classification, routing, and predictive capabilities"); transformers.js / WebGPU; transformers, sentence-transformers, MLX, vLLM, llama.cpp, SGLang, [Ollama](../entities/ollama.md), LMStudio; Qdrant; Unsloth fine-tuning guides.
- **Demo apps** in Google AI Edge Gallery: text/image → media search; text/audio → **moments in video**; an "AI Edge Foresight" app pairing it with Gemma 4.

## Why it matters here

- **Robot memory is a retrieval problem, and the retriever now fits.** The wiki's [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) synthesis sizes the *generator* (Gemma 4 E2B on an Orin Nano, a Pi 5). It had no on-device answer for **multimodal memory**, meaning indexing what the robot saw and heard so the planner can query it later. A 567 MB embedder that puts video frames, audio clips and text in one space fills that slot. "Locate specific moments in video using text or audio queries" is, on a robot, the query "when did someone last open the fridge?"
- **The memory budget composes.** The Gemma 4 E2B text weights (~0.8 GB) and the full EmbeddingGemma 2 (~567 MB) together fit inside an 8 GB Orin Nano with room left over, and the shared encoders cut that further. That is our arithmetic from two vendor figures measured on different devices, not something Google states.
- **The MediaPipe "Decision Task API"** points the same way as [Liquid AI's d1](liquid-ai-d1-decision-model-blog.md): structured decisions taken from embeddings or a single forward pass, not from generated text. See [decision models](../concepts/agents/decision-models.md).

## Entities mentioned
- [EmbeddingGemma 2](../entities/embeddinggemma-2.md) · [Gemma 4](../entities/gemma4.md) · [Google DeepMind](../entities/google-deepmind.md) · [LiteRT](../entities/litert.md) · [Ollama](../entities/ollama.md)

## Concepts touched
- [Decision models](../concepts/agents/decision-models.md) — the MediaPipe Decision Task API.
- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) — the retrieval slot.

## Open questions
- The **model card** holds the actual benchmark tables and per-modality scores. Not yet ingested.
- No latency per embedding (ms per image or per second of audio) on any device is given. RAM is given; throughput is not.
- How well does it embed **robot-egocentric** video (low, moving, cluttered views), as opposed to phone media libraries?
- Is there an Orin, Pi 5 or RK3588 figure like the Gemma 4 LiteRT table?

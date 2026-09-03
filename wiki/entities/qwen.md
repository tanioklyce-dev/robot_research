---
title: Qwen
type: entity
subtype: product
created: 2026-05-07
updated: 2026-08-28
sources: 12
tags: [qwen, llm, alibaba, open-weights]
status: stub
---

Open-weights LLM family from Alibaba (Tongyi Qianwen). Frequently deployed in robotics agent stacks because the smaller Qwen variants (1.5–3B params) fit on edge compute.

## Qwen 3.8 27B as a local-agent model (Aug 2026)

The 27B member is the wiki's best-measured local agent model. NVIDIA claims **131 tok/s on a single RTX 5090** — though the config qualifies it: **Q4_K_M on llama.cpp with multi-token-prediction speculative decoding** (`MTP n_max=3`), not a raw figure ([source](../sources/nvidia-local-ai-blog-series-2026-08.md)).

More useful, because it is task-level: [Perplexity](../sources/perplexity-local-first-agent-research.md) runs it on a [DGX Spark](dgx-spark.md) as the local model for [Portable Computer](perplexity-portable-computer.md), scoring **82.6%** on their 53-task knowledge-work benchmark and **59.6%** on Terminal Bench 2.1 (rising to 73.0% with a frontier advisor, against 82.4% frontier-only). Their post-trained variant, **PPLX 27B**, reaches 85.4% for ~30% more tokens.

One measurement worth carrying beyond Qwen: they report a **260K advertised context window** but that the model *"begins to struggle beyond 100K tokens."*

## Versions seen in this wiki
- **`qwen3:1.7b`** — used by [ROSOrin](rosorin.md)'s offline curriculum via [Ollama](ollama.md) ([Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)).
- **`qwen25-3B-Instruct`** — default local LLM in [stretch_ai](stretch-ai.md)'s LLM agent ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)).
- **`Qwen-plus-latest`** — cloud variant accessed via OpenRouter in ROSOrin's chapter 10 cloud curriculum.
- **`Qwen2.5-VL-3B`** — the unmodified VLM backbone of **[VLA-0](vla-0.md)**, NVIDIA's action-as-text VLA ([VLA-0 paper](../sources/vla-0-paper.md)). A robotics use of Qwen's *vision-language* variant (vs. the text-only variants above).

## Why it matters
Qwen has become a default open-weights LLM for agentic robotics on edge devices because of (a) permissive license, (b) small variants that fit on Jetson-class hardware, (c) good multilingual support including Chinese. The fact that two unrelated robot stacks ([stretch_ai](stretch-ai.md) and [ROSOrin](rosorin.md)) independently default to Qwen 1.5–3B variants is itself a signal.

## Related
- [Ollama](ollama.md) — common runtime.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the dominant use pattern.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [VLA-0 paper](../sources/vla-0-paper.md) — Qwen2.5-VL-3B as the VLA backbone.

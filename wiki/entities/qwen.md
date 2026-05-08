---
title: Qwen
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [qwen, llm, alibaba, open-weights]
status: stub
---

Open-weights LLM family from Alibaba (Tongyi Qianwen). Frequently deployed in robotics agent stacks because the smaller Qwen variants (1.5–3B params) fit on edge compute.

## Versions seen in this wiki
- **`qwen3:1.7b`** — used by [ROSOrin](rosorin.md)'s offline curriculum via [Ollama](ollama.md) ([Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)).
- **`qwen25-3B-Instruct`** — default local LLM in [stretch_ai](stretch-ai.md)'s LLM agent ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)).
- **`Qwen-plus-latest`** — cloud variant accessed via OpenRouter in ROSOrin's chapter 10 cloud curriculum.

## Why it matters
Qwen has become a default open-weights LLM for agentic robotics on edge devices because of (a) permissive license, (b) small variants that fit on Jetson-class hardware, (c) good multilingual support including Chinese. The fact that two unrelated robot stacks ([stretch_ai](stretch-ai.md) and [ROSOrin](rosorin.md)) independently default to Qwen 1.5–3B variants is itself a signal.

## Related
- [Ollama](ollama.md) — common runtime.
- [LLM-agent architecture](../concepts/llm-agent-architecture.md) — the dominant use pattern.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)

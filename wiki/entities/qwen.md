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
- **`qwen3:1.7b`** — used by [[rosorin|ROSOrin]]'s offline curriculum via [[ollama|Ollama]] ([[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]).
- **`qwen25-3B-Instruct`** — default local LLM in [[stretch-ai|stretch_ai]]'s LLM agent ([[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]).
- **`Qwen-plus-latest`** — cloud variant accessed via OpenRouter in ROSOrin's chapter 10 cloud curriculum.

## Why it matters
Qwen has become a default open-weights LLM for agentic robotics on edge devices because of (a) permissive license, (b) small variants that fit on Jetson-class hardware, (c) good multilingual support including Chinese. The fact that two unrelated robot stacks ([[stretch-ai|stretch_ai]] and [[rosorin|ROSOrin]]) independently default to Qwen 1.5–3B variants is itself a signal.

## Related
- [[ollama|Ollama]] — common runtime.
- [[llm-agent-architecture|LLM-agent architecture]] — the dominant use pattern.

## Mentioned in
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]

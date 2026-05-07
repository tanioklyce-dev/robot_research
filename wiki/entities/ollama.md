---
title: Ollama
type: entity
subtype: tool
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [ollama, llm-runtime, local-llm, edge-inference]
status: stub
---

Open-source local-LLM runtime / server (ollama.com). Used by [[rosorin|ROSOrin]]'s offline curriculum (chapter 10.5) to run [[qwen|qwen3:1.7b]] on a Jetson Orin Nano. Invocation pattern: `ollama serve` starts the local HTTP server; client code wraps it via a thin class (`speech.OllamaAPI`).

## Why it matters
The dominant on-device LLM runtime for hobbyist / educational robotics in 2026. Bridges the cloud-LLM agent pattern down to edge devices without requiring custom inference engineering — `ollama pull qwen3:1.7b && ollama serve` is essentially the whole story.

## Related
- [[qwen|Qwen]] — common model family served via Ollama.
- [[llm-agent-architecture|LLM-agent architecture]] — Ollama is one of several runtimes that support this pattern locally.

## Mentioned in
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]

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

Open-source local-LLM runtime / server (ollama.com). Used by [ROSOrin](rosorin.md)'s offline curriculum (chapter 10.5) to run [qwen3:1.7b](qwen.md) on a Jetson Orin Nano. Invocation pattern: `ollama serve` starts the local HTTP server; client code wraps it via a thin class (`speech.OllamaAPI`).

## Why it matters
The dominant on-device LLM runtime for hobbyist / educational robotics in 2026. Bridges the cloud-LLM agent pattern down to edge devices without requiring custom inference engineering — `ollama pull qwen3:1.7b && ollama serve` is essentially the whole story.

## Related
- [Qwen](qwen.md) — common model family served via Ollama.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Ollama is one of several runtimes that support this pattern locally.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)

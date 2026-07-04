---
title: Ollama
type: entity
subtype: tool
created: 2026-05-07
updated: 2026-07-04
sources: 5
tags: [ollama, llm-runtime, local-llm, edge-inference, uav]
---

Open-source local-LLM runtime / server (ollama.com). Used by [ROSOrin](rosorin.md)'s offline curriculum (chapter 10.5) to run [qwen3:1.7b](qwen.md) on a Jetson Orin Nano. Invocation pattern: `ollama serve` starts the local HTTP server; client code wraps it via a thin class (`speech.OllamaAPI`).

## Why it matters
The dominant on-device LLM runtime for hobbyist / educational robotics in 2026. Bridges the cloud-LLM agent pattern down to edge devices without requiring custom inference engineering — `ollama pull qwen3:1.7b && ollama serve` is essentially the whole story.

## Related
- [Qwen](qwen.md) — common model family served via Ollama.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Ollama is one of several runtimes that support this pattern locally.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Taking Flight with Dialogue (Lim et al. 2025)](../sources/taking-flight-with-dialogue-px4-drone-agent.md) — a ROS 2 wrapper encapsulates Ollama to serve interchangeable LLMs + VLMs for onboard drone control on a Jetson Orin Nano.
- [Seeed jetson-examples](../sources/seeed-jetson-examples.md) — Ollama as one of the LLM-serving recipes.
- [NVIDIA RTX AI Garage — Hermes Agent](../sources/nvidia-rtx-ai-garage-hermes-agent.md) — supported runtime (via NVIDIA blog).
- [Hermes Agent GitHub README](../sources/hermes-agent-github.md) — supported runtime.

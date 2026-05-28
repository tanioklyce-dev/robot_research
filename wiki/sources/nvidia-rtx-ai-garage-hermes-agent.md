---
title: "RTX AI Garage — Run Open Source Hermes Agent on DGX Spark for Reliable AI Self-Improvement (NVIDIA Blog, May 2026)"
type: source
url: https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/
author: Abhishek Gore (NVIDIA)
published: 2026-05-13
ingested: 2026-05-28
tags: [hermes-agent, nous-research, dgx-spark, rtx-ai-garage, agentic-ai, self-improvement, qwen-3-6, local-llm, mcp, openrouter]
---

## Summary

NVIDIA RTX AI Garage post (May 13 2026, Abhishek Gore) profiling **[Hermes Agent](../entities/hermes-agent.md)** — an open-source agentic framework from **[Nous Research](../entities/nous-research.md)** — and showcasing it running on **[DGX Spark](../entities/dgx-spark.md)**. The article positions Hermes Agent as the standout entry in the post-2025 "autonomous agent on local hardware" wave: **>140K GitHub stars in under three months**, *"the most used agent in the world according to OpenRouter."* The DGX Spark angle: 128 GB unified memory + 1 PFLOP AI throughput is the local-hardware tier where a 120B-MoE model can serve as the agent's brain "all day."

## Key claims

### What makes Hermes Agent distinctive (NVIDIA's framing)

The blog calls out **four distinguishing features** vs other agent frameworks:

1. **Self-Evolving Skills** — "agents write and refine their own skills over time" (in-the-loop skill creation, not just pre-written tool use).
2. **Contained Sub-Agents** — isolated workers spawned for specific sub-tasks (parallel decomposition with bounded blast radius).
3. **Reliability by design** — curated and stress-tested components rather than experimental glue.
4. **Same model, better results** — Hermes Agent functions as *active orchestration*, not a passive wrapper around a chat completion. Same base model produces higher-quality outcomes when used through Hermes Agent's loop.

### DGX Spark pairing (the article's headline)

- **128 GB unified memory + 1 PFLOP AI performance** ([DGX Spark](../entities/dgx-spark.md)) → can serve a **120B-parameter mixture-of-experts model all day** as the agent's brain.
- Recommended model pairing: **Qwen 3.6** at the 27B and 35B parameter scales (from Alibaba).
- Compatible runtimes: **llama.cpp**, **LM Studio**, **Ollama**.

### Adoption signal

- **140K+ GitHub stars in under three months** of public availability.
- *"The most used agent in the world according to OpenRouter"* — a non-NVIDIA-controlled measurement.

## Entities mentioned

- [Hermes Agent](../entities/hermes-agent.md) — the framework profiled.
- [Nous Research](../entities/nous-research.md) — author.
- [NVIDIA DGX Spark](../entities/dgx-spark.md) — featured hardware.
- [Qwen](../entities/qwen.md) — recommended LLM (Qwen 3.6 27B / 35B).
- [Ollama](../entities/ollama.md) — supported runtime.

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Hermes Agent is a higher-tier instance of the same pattern.

## Notable absences from the blog

- **No robotics integration discussed.** The blog and NVIDIA's framing position Hermes Agent as a *desktop / cloud-services* agent — not a robot-platform planner. Robot use would require a custom MCP-server bridge.
- **No comparison to other agent frameworks** (LangGraph, AutoGen, Claude Code, Codex, OpenDevin, etc.).
- **No latency or throughput benchmarks** beyond "120B MoE all day" (which is a capacity claim, not a throughput claim).

## Open questions

- The 140K-stars-in-3-months figure is striking — what's the user base composition (researchers, developers, end-users)?
- "Most used agent in the world according to OpenRouter" — which version of OpenRouter's metric? Token volume, conversation count, distinct callers?
- How does the "self-evolving skills" mechanism work concretely — write new Python tools? Modify prompts? Generate sub-agent configs? The blog is high-level.
- Is Hermes Agent designed to be embeddable in another system (as a planner LLM for a robot), or is it primarily an end-user application?

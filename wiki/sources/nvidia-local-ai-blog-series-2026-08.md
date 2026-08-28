---
title: "NVIDIA and Local AI Community Fuel Open Source Models and Intelligent Agents (rolling series, Aug 2026)"
type: source
url: https://blogs.nvidia.com/blog/local-ai-open-source-models-agents-nemotron/
author: NVIDIA Writers
affiliation: NVIDIA
published: 2026-08-11
ingested: 2026-08-28
venue: NVIDIA Blog — "special-edition NVIDIA Local AI blog series"
format: rolling multi-entry blog post; entries dated 2026-08-11 through 2026-08-25
tags: [nvidia, local-ai, dgx-spark, nemotron, nemo-switchyard, perplexity, jetson, edge-agents, open-weights, llama-cpp, ollama, vllm, nvfp4, marketing-source]
---

# NVIDIA Local AI series, August 2026

> [!warning] Vendor marketing roundup — read as a landscape snapshot, not evidence
> This is NVIDIA's own promotional series, updated in place across August 2026. Nearly every number is vendor-stated with no independent verification, several headline items are **"coming soon"**, and the benchmarks that *are* specified mix quantization and speculative decoding into the throughput figures. Its value to this wiki is as a **dated snapshot of the local-agent stack** — which models, which runtimes, which boxes — not as a source for any performance claim. Individual items with real technical substance ([Cosmos 3 Edge](nvidia-cosmos3-edge-hf-blog.md)) already have their own primary-sourced pages here.

## Summary

A month-long roundup of the "local AI" push: run capable agents on hardware you own, with open-weight models, rather than against a cloud API. The organising hardware tier is **[DGX Spark](../entities/dgx-spark.md)** — with [Jetson](../entities/jetson-thor.md) named as the edge extension on nearly every item — and the recurring pitch is *always-on, 24×7, private, no token limits*.

For this wiki the series is useful in one specific way: it is the clearest single statement of **what NVIDIA expects an on-desk/on-robot agent stack to look like in late 2026**, and it lands directly on the [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) synthesis.

## The items that matter here

### Nemotron 3.5 Lightning (Aug 11)

An open-weights **30B mixture-of-experts** model for always-on agents ([entity](../entities/nemotron.md)). Claimed **up to 4× faster token generation and 30% faster time-to-completion "compared to open models in its class"** — no comparators named, no benchmark named.

Deployment breadth is the substantive part: **vLLM, Ollama, llama.cpp, LM Studio**, in both **NVFP4 and GGUF**, with Unsloth day-one support. Runs on RTX PCs, **DGX Spark and OEM GB10 systems, and Jetson**, scaling up to RTX PRO, DGX Station, GB300 deskside, datacentre and cloud. Fine-tuning is pitched as the point — style, domain vocabulary, coding conventions.

### NeMo Switchyard (Aug 11)

An **open-source routing library** that *"automatically directs each step of an agent workflow to the best-fit model based on accuracy, speed and cost."* See [entity](../entities/nemo-switchyard.md).

> [!note] The cost claim is real if true, and unfalsifiable as stated
> *"Internal benchmarks show that NeMo Switchyard, by routing each step across a system of models, helped maintain frontier-level task completion while reducing benchmark completion cost to roughly **one-third of Opus 4.8 alone**."*
>
> Unnamed benchmark, unnamed model pool, "internal," no task-completion delta quantified beyond "maintain frontier-level," and a named competitor in the denominator. This is the most consequential claim in the series and the least checkable. Worth tracking because **per-step model routing is a genuine architectural pattern** for robot agent stacks — reactive control local, planning escalated — not because the 3× number means anything yet.

### Perplexity "Portable Computer" (Aug 25)

> [!note] The primaries are ingested separately, and this account is lossy
> See [Perplexity's announcement](perplexity-portable-computer.md) and its [research post](perplexity-local-first-agent-research.md). NVIDIA's item **omits** that it is **Pro/Max subscribers only**, **Linux-first**, that the local stack includes an **orchestrator, planner, tool router, scheduler, durable task queue and search index**, that a **PII classifier and per-transfer user consent** gate every escalation, that execution is **sandboxed fail-closed**, and that the whole thing has **published benchmarks**. It also says *"a specially post-trained Qwen 3.8 27B"* where the primary offers **stock Qwen 3.8 27B *or* PPLX 27B**, and *"token limits"* where the primary says **credits**.

[Perplexity](https://www.perplexity.ai)'s local agent app, optimised for DGX Spark: connectors for Google Drive, Gmail, Slack and GitHub, and **switching between local and cloud models** — cloud for complex work, local for everyday tasks. Pitched on DGX Spark's *"fast LLM inference and 24×7 always-on operation, perfect for long-running autonomous agents."*

Runs a **specially post-trained Qwen 3.8 27B** locally, with a fine-tuned **Nemotron 3.5 Lightning** variant *"coming soon"*. RTX / RTX PRO support, Windows, and DGX Station are all also coming soon — so as published this is **DGX Spark only**.

The economic framing is the interesting bit: local runs *"don't count towards token limits."* A subscription agent product that offloads inference to hardware the customer already bought is a different unit-economics story from a pure API product, and it is the first instance of that pattern in this wiki.

### Qwen3.8-27B (Aug 14)

Positioned as the local companion to Qwen3.8-Max, *"sized for a single GPU"* for agentic coding ([Qwen](../entities/qwen.md)). **131 tokens/sec on a single GeForce RTX 5090** — and unusually for this series, the configuration is given:

> RTX 5090 + Intel Core Ultra 9 285K, 64 GB RAM, Windows 11, driver 610.43, **Q4_K_M checkpoint on llama.cpp**, speedbench, **MTP n_max = 3**.

So the number is 4-bit quantized *with* multi-token-prediction speculative decoding — not a raw BF16 figure, and not comparable to one. Day-zero support on RTX, DGX Spark/Station and **Jetson**; NVFP4 "coming soon" for all local AI devices.

### Meta Muse Glimmer (Aug 11)

A **30B dense** open-weight model, **120K+ context**, purpose-built for coding and local agentic AI. *"Over 200 tokens per second on RTX 5090"* — **no configuration given at all**, so weaker evidence than the Qwen row above. vLLM or llama.cpp (BF16 and quantized GGUF), with **DFlash speculative decoding**. Fine-tunable locally via **NVIDIA NeMo Automodel**, buildable with [NemoClaw](../entities/nemoclaw.md).

The listed design targets read as a decent spec for a robot's high-level agent: custom agents, private data processing, **credential handling on-device**, multistep tool calls with error recovery, and long-running workflows that resume with context intact.

### DGX Spark clustering and updates (Aug 11)

**NVIDIA Sync Cluster Assistant** configures two or more DGX Sparks as a high-speed cluster over **ConnectX-7**, with **Tailscale** for remote access, automatic node detection, workload routing and health monitoring. Also announced: a **Resource Monitor** (real-time and historical CPU/GPU across a cluster) and **Google Chrome as a native ARM64 Linux build** — both *"arriving later in August."*

Agentic-AI entry points named: playbooks for [NemoClaw](../entities/nemoclaw.md), [OpenClaw](../entities/openclaw.md), [Hermes Agent](../entities/hermes-agent.md) and OpenShell.

### The model roster, as a memory ladder

The clearest thing the series gives the wiki: which models NVIDIA claims fit which box.

| Model | Size | Claimed to run on |
|---|---|---|
| **[Cosmos 3 Edge](nvidia-cosmos3-edge-hf-blog.md)** | 4B | DGX Spark and **Jetson** — *"a quarter the size of Cosmos 3 Nano"* |
| Nemotron 3.5 Lightning | 30B MoE | RTX PC, DGX Spark, GB10, **Jetson** |
| Meta Muse Glimmer | 30B dense | RTX 5090, DGX Spark/Station, **Jetson** |
| Qwen3.8-27B | 27B | single RTX 5090, DGX Spark/Station, **Jetson** |
| Poolside Laguna S 2.1 | 118B | single DGX Spark, via **NVFP4** |
| Thinking Machines Inkling-Small | 276B MoE / 12B active | one DGX Station **or two DGX Sparks** |
| DeepSeek-V4-Flash | 284B MoE / 13B active, 1M ctx | DGX Station, community GGUF |

Also mentioned: MiniMax-H3 (33B video+audio), LTX-2.5 (video; its prompt enhancer uses **[Gemma 4](../entities/gemma4.md) E2B and a custom Gemma 4 12B text encoder**), Wan-Animate-2 (14B), and **Unsloth Desktop**, claimed as *"the first desktop app that both trains and runs AI models locally."*

## Entities mentioned

- [DGX Spark](../entities/dgx-spark.md) · [Nemotron](../entities/nemotron.md) · [NeMo Switchyard](../entities/nemo-switchyard.md) · [Jetson Thor](../entities/jetson-thor.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [Qwen](../entities/qwen.md) · [Gemma 4](../entities/gemma4.md) · [NemoClaw](../entities/nemoclaw.md) · [OpenClaw](../entities/openclaw.md) · [Hermes Agent](../entities/hermes-agent.md) · [Ollama](../entities/ollama.md) · [NVIDIA](../entities/nvidia.md)

## Concepts touched

- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md)

## Open questions

- **Nothing here is robotics except Cosmos 3 Edge.** Jetson is named on nearly every item, but every named application is a *desktop* one — coding, email, Slack, documents. The series is about personal-computer agents that happen to also run on robot compute, and the wiki should not read Jetson support as robot validation.
- **How do these throughput numbers behave under a control loop?** All figures are single-stream text generation on an idle machine. A robot agent shares its box with perception and control, and none of these numbers are measured under contention. Compare the [LiteRT figures](gemma-4-e2b-model-card.md), which at least publish per-backend memory.
- **Is NeMo Switchyard's routing claim reproducible?** Unnamed benchmark, unnamed model pool. If per-step routing really holds frontier task completion at a third of the cost, that is the most useful item in the series for robot agent stacks — and it needs an external replication before it is quotable.
- **"Coming soon" inventory to re-check**: NVFP4 across all local AI devices, Perplexity on RTX / Windows / DGX Station, the fine-tuned Nemotron Lightning variant, DGX Spark Chrome and Resource Monitor.
- **No Nemotron 3.5 Lightning model card ingested** — the 4×/30% claims should be checked against the card or a benchmark before being repeated.

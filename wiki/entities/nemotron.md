---
title: Nemotron
type: entity
subtype: model
created: 2026-08-28
updated: 2026-08-28
sources: 2
tags: [nemotron, nvidia, open-weights, moe, edge-agents, dgx-spark, jetson, asr, nvfp4]
---

**Nemotron** — NVIDIA's family of **open-weights** models, positioned for local and agentic deployment across the RTX / [DGX Spark](dgx-spark.md) / [Jetson](jetson-thor.md) hardware line. In this wiki it appears mostly as **the model NVIDIA bundles into its own agent stacks** — [NemoClaw](nemoclaw.md) ships it — rather than as a subject in its own right.

> [!note] Thin page, blog-sourced
> Created as a citation target during the [NVIDIA Local AI series](../sources/nvidia-local-ai-blog-series-2026-08.md) ingest. **No Nemotron model card, paper or benchmark has been ingested**, so the performance claims below are vendor marketing and should be checked before reuse.

## Nemotron 3.5 Lightning (announced 2026-08-11)

A **30B mixture-of-experts** open-weights model for *"always-on agents."*

- Claimed **up to 4× faster token generation** and **30% faster time to completion** *"compared to open models in its class"* — **no comparators or benchmark named**.
- Runtimes: **vLLM, Ollama, llama.cpp, LM Studio**; formats **NVFP4 and GGUF**; Unsloth day-one support.
- Hardware: RTX PCs, **DGX Spark and OEM GB10**, **Jetson**, scaling to RTX PRO, DGX Station, GB300 deskside, datacentre and cloud.
- Fine-tuning is the pitch — writing style, domain specialty, coding conventions.

Independent corroboration of its class, from a third party: Perplexity's research post lists it alongside Qwen 3.6 (35B) and Qwen 3.8 (27B) as *"very small and efficient models… now capable of complex agentic workflows"*, and has it **coming to Portable Computer's model picker** ([source](../sources/perplexity-local-first-agent-research.md)).

## Nemotron 3.5 ASR

A speech-recognition model in the same family. Runs **[Portable Computer](perplexity-portable-computer.md)'s local dictation** — *"the transcription and actions on files all stay on the machine… without the audio touching the cloud"* ([Perplexity](../sources/perplexity-portable-computer.md)). The wiki's only instance of an on-device ASR model named in an agent stack.

## Why it matters here

- **It is the default model in NVIDIA's own agent scaffolding.** [NemoClaw](nemoclaw.md) bundles Nemotron alongside the NVIDIA Agent Toolkit and OpenShell guardrails, so anyone adopting NVIDIA's agent stack inherits it.
- **Jetson support is claimed on every release**, which makes it a nominal candidate for an on-robot high-level agent — though every application NVIDIA names is a desktop one. See [on-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md).

## Related

- [NemoClaw](nemoclaw.md) — NVIDIA's agent wrapper that bundles it
- [NeMo Switchyard](nemo-switchyard.md) — routes agent steps across models including this family
- [DGX Spark](dgx-spark.md) · [Jetson Thor](jetson-thor.md) — deployment targets
- [Qwen](qwen.md) · [Gemma 4](gemma4.md) — the comparable open-weights edge families
- [Perplexity Portable Computer](perplexity-portable-computer.md) — ships the ASR model, adding Lightning

## Mentioned in

- [NVIDIA Local AI blog series, Aug 2026](../sources/nvidia-local-ai-blog-series-2026-08.md) — the 3.5 Lightning launch and its deployment matrix.
- [A Local-First Agent for Private and Cost-Effective Knowledge Work](../sources/perplexity-local-first-agent-research.md) — third-party placement of Lightning in the capable-small-model class.

## Open questions

- **No model card ingested.** The 4× / 30% claims have no named baseline and no benchmark.
- **Nemotron 3 vs 3.5 vs earlier generations** are not disentangled here; this page covers only what the August 2026 sources state.
- **Is Nemotron 3.5 ASR open-weights** like Lightning, or NVIDIA-hosted? Unstated.

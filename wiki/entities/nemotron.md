---
title: Nemotron
type: entity
subtype: model
created: 2026-08-28
updated: 2026-11-17
sources: 7
tags: [nemotron, nvidia, open-weights, moe, vlm, edge-agents, dgx-spark, jetson, asr, nvfp4, mamba, speculative-decoding]
---

**Nemotron** — NVIDIA's family of **open-weights** models, positioned for local and agentic deployment across the RTX / [DGX Spark](dgx-spark.md) / [Jetson](jetson-thor.md) hardware line. In this wiki it appears mostly as **the model NVIDIA bundles into its own agent stacks** — [NemoClaw](nemoclaw.md) ships it — rather than as a subject in its own right.

> [!note] Thin page, blog-sourced
> Created as a citation target during the [NVIDIA Local AI series](../sources/nvidia-local-ai-blog-series-2026-08.md) ingest. **No Nemotron model card, paper or technical report has been ingested**, so the performance claims below are vendor-stated. The [Super VL launch post](../sources/nvidia-nemotron-3-5-super-vl-blog.md) (ingested 2026-11-17) is the first source here with charts and comparators, and it is still a vendor blog.

## The family, as far as the wiki can place it

| Model | Size | Role NVIDIA gives it | Source |
|---|---|---|---|
| Nemotron 3 Nano Omni | not stated | small multimodal model; CharXiv 63% | [Super VL post](../sources/nvidia-nemotron-3-5-super-vl-blog.md) |
| Nemotron 3.5 Lightning | 30B MoE | "high-volume text tasks" | Local AI series; Super VL post |
| Nemotron 3.5 Bolt | 74B, 9B active (from the checkpoint name) | local planner in the Microduck tutorial | Microduck post |
| **Nemotron 3.5 Super VL** | **120B, 12B active** | specialised multimodal agent work | Super VL post |
| Nemotron 3 Super | not stated | predecessor of Super VL | Super VL post |
| Nemotron 3 Ultra | not stated | "frontier"; "complex planning and orchestration"; Super VL's distillation teacher | Super VL post |

## Nemotron 3.5 Super VL (2026-10-15)

A **120B mixture-of-experts with 12B parameters active per token**, taking text, images, documents and video, with open weights and post-training recipes ([launch post](../sources/nvidia-nemotron-3-5-super-vl-blog.md)). The backbone is a hybrid of attention and Mamba layers, distilled from Nemotron 3 Ultra.

- **Fast, and mid-pack on capability.** On the Artificial Analysis index chart NVIDIA published, it scores about 27 at about 625 output tokens/s; several open models score 34 to 42 at 60 to 225 tokens/s. On SWE-bench Pro it is plotted at about 51% against 56 to 60% for three comparators, finishing 10,000 tasks in about 10 hours on four B200s where they take 50 to 118.
- **It outscores the family's own "frontier" model** on the two agent benchmarks NVIDIA tabulates: Hermes Bench 63.44% against 56.33% for Nemotron 3 Ultra, LangChain evals 87.05% against 84.3%.
- **Post-training is the product.** In five partner workflows the base model is below the frontier model it is compared with, and the post-trained one is above it (for example security analysis, about 35% to 76%, against 66%). The frontier models were not adapted.
- **On a [DGX Spark](dgx-spark.md)** it sits on the accuracy-versus-time frontier in a partner-run evaluation at roughly 6.5 minutes per agentic task; Nemotron 3.5 Lightning is at about 2 minutes with a lower score.
- **Inference stack**: NVFP4 4-bit weights with quantization-aware distillation, LiLiCorr speculative decoding (up to 2.3x on DGX Spark), multi-token prediction, and attention-plus-Mamba state caching across agent turns.
- **Harnesses named**: Hermes, LangChain, OpenClaw, OpenCode, Pi, Codex and Claude.
- **Not in the post**: robotics, embodied-reasoning benchmarks, or Jetson.

## Nemotron 3.5 Lightning (announced 2026-08-11)

A **30B mixture-of-experts** open-weights model for *"always-on agents."*

- Claimed **up to 4× faster token generation** and **30% faster time to completion** *"compared to open models in its class"* — **no comparators or benchmark named**.
- Runtimes: **vLLM, Ollama, llama.cpp, LM Studio**; formats **NVFP4 and GGUF**; Unsloth day-one support.
- Hardware: RTX PCs, **DGX Spark and OEM GB10**, **Jetson**, scaling to RTX PRO, DGX Station, GB300 deskside, datacentre and cloud.
- Fine-tuning is the pitch — writing style, domain specialty, coding conventions.

Independent corroboration of its class, from a third party: Perplexity's research post lists it alongside Qwen 3.6 (35B) and Qwen 3.8 (27B) as *"very small and efficient models… now capable of complex agentic workflows"*, and has it **coming to Portable Computer's model picker** ([source](../sources/perplexity-local-first-agent-research.md)).

## Nemotron 3.5 Bolt (seen 2026-10-23)

Named in NVIDIA's [Microduck tutorial](../sources/nvidia-microduck-ai-agents-sim-blog.md) as the local planning model behind [Hermes Agent](hermes-agent.md) on [RTX Spark](nvidia-rtx-spark.md). The linked checkpoint is **`nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB`**. Read from the name, that is a **74B-total / 9B-active MoE packaged to fit 24 GB**. No model card has been ingested, so treat the parameter reading as inferred from the repo name.

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
- [Nemotron 3.5 Super VL launch post](../sources/nvidia-nemotron-3-5-super-vl-blog.md) — the 120B-A12B multimodal model, its speed and accuracy charts, post-training results and inference engineering.
- [A Local-First Agent for Private and Cost-Effective Knowledge Work](../sources/perplexity-local-first-agent-research.md) — third-party placement of Lightning in the capable-small-model class.
- [Post-train Cosmos 3 Edge](../sources/nvidia-cosmos3-edge-post-training-blog.md) — Cosmos 3 Edge's reasoner tower is stated as a **2B Nemotron-based** model, where the Cosmos 3 report described the family's reasoner as Qwen3-VL-initialised; unresolved.
- [NVIDIA Isaac ROS 5.0 blog](../sources/nvidia-isaac-ros-5-0-blog.md) — AgenticROS connects Isaac ROS to Nemotron models.
- [Using AI agents to teach Microduck to walk in simulation (NVIDIA)](../sources/nvidia-microduck-ai-agents-sim-blog.md) — Nemotron 3.5 Bolt (74B-A9B, 24 GB) as Hermes's planner on RTX Spark.

## Open questions

- **No model card or technical report ingested.** Lightning's 4× / 30% claims have no named baseline. Super VL's have named comparators and no trial counts; the linked Nemotron 3.5 technical report is the primary to ingest.
- **How Bolt (74B-A9B) relates to Super VL (120B-A12B)**: neither post mentions the other.
- **Does anything above Lightning run on Jetson?** The Super VL post lists DGX Spark as its smallest target.
- **Nemotron 3 vs 3.5 vs earlier generations** are not disentangled here; this page covers only what the August 2026 sources state.
- **Is Nemotron 3.5 ASR open-weights** like Lightning, or NVIDIA-hosted? Unstated.

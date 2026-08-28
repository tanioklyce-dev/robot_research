---
title: Perplexity Portable Computer
type: entity
subtype: product
created: 2026-08-28
updated: 2026-08-28
sources: 2
tags: [perplexity, portable-computer, local-first, dgx-spark, qwen, pplx-27b, agent-harness, escalation, sandboxing, edge-agents]
---

**Announced 2026-08-25** · [announcement](../sources/perplexity-portable-computer.md) · [research post](../sources/perplexity-local-first-agent-research.md)

**Portable Computer** — a **local-first** version of Perplexity Computer that runs its whole agent stack on the user's machine, escalating to the cloud only with permission. Built with NVIDIA for the **[DGX Spark](dgx-spark.md)**. The wiki's first shipped example of a **co-designed model and harness** for capacity-limited local inference.

## What is actually local

Not just the model — the runtime:

> "The **orchestrator, planner, tool router, scheduler, durable task queue, and local search index** all run on device."

Models: **Qwen 3.8 27B** or **PPLX 27B** (Perplexity's post-trained variant), with **[Nemotron 3.5 Lightning](nemotron.md)** *"coming soon to the model picker."* Dictation runs locally on the **Nemotron 3.5 ASR** model. Connectors for Google Drive, Gmail, Slack and GitHub, converted from MCP servers into **compact CLI tools** to save context.

## Design (see [harness design for capacity-limited models](../concepts/agents/local-model-harness-design.md))

- **Deterministic orchestrator** — harness code, not an LLM, holds the loop and policy; the model only proposes actions.
- **Context budgeted at ~100K**, not the 260K the model advertises; capabilities load as **on-demand [skills](../concepts/agents/agent-skills.md)**; stale context is compacted.
- **Sandbox fails closed** — *"if the sandbox is unavailable, the harness disables itself before any tool calls rather than degrading to unsandboxed execution."*
- **Advisor escalation** — the local model asks, the orchestrator decides what leaves, a **PII classifier** flags sensitive content, the user sees it first, and the advisor **returns text guidance only** with no access to files, tools, or the conversation.

## Measured (vendor-run)

| Benchmark | Result |
|---|---|
| Local Knowledge Work Bench (53 tasks, Perplexity's own) | **85.4%** with PPLX 27B; 82.6% with Qwen 3.8 27B vs Pi 77.6%, [Hermes](hermes-agent.md) 74.0% |
| ParseBench-100 (multimodal docs) | **65.1%** vs Hermes 34.6%, Pi 13.9% — and **41× fewer tokens** than Pi |
| BrowseComp (1,266 tasks) | 66.7% vs 50.2% / 43.9% — **confounded**: Computer uses Perplexity search, baselines use Brave |
| Terminal Bench 2.1 (89 tasks) | local 59.6% → **73.0%** with a Claude Opus 5 advisor at $0.415/rollout; Opus 5 alone 82.4% at $0.65 |

## Availability

**Pro and Max subscribers**, on DGX Spark, **Linux first** (Windows "coming soon"). RTX / RTX PRO and DGX Station also flagged as coming. One-click install from the Perplexity app. On-device work **consumes no credits** — the product thesis, since it moves inference onto hardware the customer already bought.

## Why it is in a robotics wiki

Nothing here is robotic; the workloads are documents, email, code and research. It earns a page because **a robot's high-level agent is the same engineering problem** — a small model on fixed hardware needing long-horizon reliability — and this is the most detailed public account of building for it. Two properties transfer directly: the **deterministic-orchestrator authority split** (which [Microduck's runtime](../sources/microduck-runtime-repo.md) reaches independently, at 50 Hz over motors), and the **advisor-never-actor** escalation boundary, which is what a cloud model touching a robot would need.

## Related

- [DGX Spark](dgx-spark.md) — the only supported hardware at launch
- [Hermes Agent](hermes-agent.md) — benchmarked baseline
- [Qwen](qwen.md) · [Nemotron](nemotron.md) — the local models
- [Harness design for capacity-limited models](../concepts/agents/local-model-harness-design.md)

## Mentioned in

- [Introducing Portable Computer for local-first AI](../sources/perplexity-portable-computer.md)
- [A Local-First Agent for Private and Cost-Effective Knowledge Work](../sources/perplexity-local-first-agent-research.md)
- [NVIDIA Local AI blog series, Aug 2026](../sources/nvidia-local-ai-blog-series-2026-08.md) — the secondary account, which drops the subscription gate and the consent model.

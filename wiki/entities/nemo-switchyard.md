---
title: NeMo Switchyard
type: entity
subtype: software-framework
created: 2026-08-28
updated: 2026-08-28
sources: 1
tags: [nemo-switchyard, nvidia, model-routing, agent-orchestration, cost-optimization, open-source, unverified]
---

**NeMo Switchyard** — NVIDIA's **open-source routing library** that *"automatically directs each step of an agent workflow to the best-fit model based on accuracy, speed and cost,"* with the flexibility to mix models and providers within one workflow. Announced 2026-08-11; available on GitHub ([source](../sources/nvidia-local-ai-blog-series-2026-08.md)).

> [!warning] One vendor claim, unfalsifiable as published
> *"Internal benchmarks show that NeMo Switchyard, by routing each step across a system of models, helped maintain frontier-level task completion while reducing benchmark completion cost to **roughly one-third of Opus 4.8 alone**."*
>
> Unnamed benchmark, unnamed model pool, "internal," no quantified task-completion delta behind *"maintain frontier-level"*, and a named competitor in the denominator. **Not quotable as evidence.** The page exists because the *pattern* is worth tracking, not the number.

## Why the pattern matters here

**Per-step model routing** is a plausible architecture for robot agent stacks, and it generalises a split the wiki already documents from two directions:

- The [on-device/on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md) synthesis argues that LLM latency forces a **high-level agent / local reactive control** split.
- [Perplexity's Portable Computer](perplexity-portable-computer.md) implements a **two-tier** version — a local model that escalates to a frontier *advisor* — and prices it: three-fifths of the frontier gap recovered for two-thirds of the cost ([research post](../sources/perplexity-local-first-agent-research.md)).

Switchyard is the **N-tier generalisation** of that same idea: not one escalation boundary but a router choosing per step. The comparison is instructive — Perplexity's version puts the escalation decision **inside the local model** as post-trained behaviour, with the harness controlling what context leaves; Switchyard is described as an **external router** deciding on accuracy/speed/cost. Those are different trust boundaries, and only the first has a published privacy story.

## Related

- [Perplexity Portable Computer](perplexity-portable-computer.md) — the two-tier, privacy-gated version, with numbers
- [Harness design for capacity-limited models](../concepts/agents/local-model-harness-design.md) — where escalation policy lives
- [Nemotron](nemotron.md) — NVIDIA's own models in the routable pool
- [NemoClaw](nemoclaw.md) — NVIDIA's agent wrapper

## Mentioned in

- [NVIDIA Local AI blog series, Aug 2026](../sources/nvidia-local-ai-blog-series-2026-08.md)

## Open questions

- **Repo not ingested.** No routing policy, no interface, no supported-provider list examined here.
- **What is the routing signal?** Static per-step rules, a learned router, or a cost model — unstated.
- **Any robot use?** None known. The latency budget of a router that may select a remote model is the obvious obstacle for anything reactive.

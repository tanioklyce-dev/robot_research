---
title: "A Local-First Agent for Private and Cost-Effective Knowledge Work (Perplexity Research)"
type: source
url: https://www.perplexity.ai/hub/blog/a-local-first-agent-for-private-and-cost-effective-knowledge-work
author: Perplexity Research
affiliation: Perplexity AI
published: 2026-08-25
ingested: 2026-08-28
venue: Perplexity Blog (Research)
format: research blog post with five sections, seven figures, two tables
tags: [perplexity, portable-computer, local-first, harness-design, dgx-spark, qwen, pplx-27b, hermes-agent, benchmarks, browsecomp, terminal-bench, advisor-escalation, sandboxing, agent-skills]
---

# A Local-First Agent for Private and Cost-Effective Knowledge Work

> [!note] Provenance
> `perplexity.ai` returns **403** to every automated fetch path available here (curl with varied user agents, WebFetch, text proxies). **The full text of this post was supplied by the user**; the [companion announcement](perplexity-portable-computer.md) was recovered from the Wayback Machine. Treated as primary, but note that no independent retrieval was possible from this session.

> [!warning] All benchmarks are self-run by the vendor against competitors it configured
> Perplexity built the harness, chose the baselines, ran every evaluation, and invented one of the four benchmarks. No third-party replication exists. The **BrowseComp comparison is additionally confounded** — see below. The engineering principles are the durable content; the win rates are not evidence in the way an independent evaluation would be.

## Summary

The design document behind **[Portable Computer](../entities/perplexity-portable-computer.md)**, and much the most substantive of the three sources in this cluster. Its thesis is that a local-first agent requires **co-designing the harness and the model**:

> "General-purpose harnesses assume a frontier model that can absorb long contexts, navigate a broad tool surface, and plan over long horizons. Local models are less reliable under those demands. Rather than asking a small model to manage a harness built for a large one, we shaped the two around each other."

That is the transferable claim, and it is directly relevant to on-robot agents, which face the same constraint for the same reason. See [harness design for capacity-limited models](../concepts/agents/local-model-harness-design.md).

## The harness design principles

**Context efficiency is the organising constraint.** The empirical finding worth extracting:

> "Although on-device models such as Qwen 3.8 27B offer context windows of **260K tokens**, we found empirically that they **begin to struggle beyond 100K tokens**."

So the usable context is roughly **40% of the advertised window**. The response: a minimal system prompt, a small core toolset, and everything else modularised into **on-demand [skills](../concepts/agents/agent-skills.md) that load and unload through the trajectory**, plus **context compaction** that summarises stale context as a trajectory grows.

**Connectors as CLI tools, not MCP servers.** A pointed design choice:

> "These are usually exposed to a harness as MCP servers, whose **large tool definitions consume a substantial share of the context**. Instead, we converted the most-used MCPs into compact, easy-to-use command-line tools."

**Self-verification**, triggered by the model *or* by **hooks that monitor trajectory health** and request verification when something goes wrong. Claimed to *"substantially narrow the gap to frontier models"* — unquantified in isolation.

**Sandboxing is unconditional, and fails closed.** The strongest safety statement in the cluster:

> "The harness executes tools in an **OS-level sandbox**… restricts processes, filesystem paths, and network access according to policy… **If the sandbox is unavailable, the harness disables itself before any tool calls rather than degrading to unsandboxed execution.**"
>
> Explicitly contrasted with the baselines: *"[Hermes](../entities/hermes-agent.md) and Pi… run commands directly with the user's permissions by default. In Computer, isolation is always on, requires no configuration, and tools cannot run without it."*

**The orchestrator is deterministic code, not a model.** *"The orchestrator is deterministic harness code, not an LLM: it maintains the loop, assembles context, and enforces policy. The local model proposes the next action; the orchestrator executes approved tool calls in the sandbox."* This is the same authority split the wiki records in [Microduck's runtime](microduck-runtime-repo.md) — clients send *intents*, a deterministic layer decides what executes.

## Advisor escalation

The local model may consult a frontier model, but **the harness keeps tool authority**:

- The local model decides *when* to ask; the orchestrator controls *what context is sent*.
- Before an advisor call, the harness **selects relevant context, applies a PII classifier to flag sensitive information, and shows the user what would leave the device**.
- The advisor **returns text guidance only** — *"no direct access to the device's files, tools, or conversations."*
- Per-call approval is manual or automatic, at the user's choice.

That is a cleanly specified trust boundary: the remote model is an *advisor*, never an actor.

## Results

### Local Knowledge Work Bench — Perplexity's own benchmark

53 held-out tasks across 7 categories, 3 trials each, 95% CIs. **To be open-sourced**, per the post.

| Harness + model | Score | Tokens/task | Wall time |
|---|---|---|---|
| **Computer + PPLX 27B** | **85.4%** | 678k | 250 s |
| Computer + Qwen 3.8 27B | 82.6% | **520k** | 218 s |
| Pi + Qwen 3.8 27B | 77.6% | 681k | **176 s** |
| Hermes + Qwen 3.8 27B | 74.0% | 634k | 292 s |

Category mix is worth noting because it defines what "knowledge work" means here: **deep research 37.7%**, data/finance/procurement 17.0%, documents/presentations 13.2%, engineering/IT/incidents 9.4%, contracts/compliance 9.4%, dashboards/visualisation 7.5%, people/projects/meetings 5.7%.

**Pi is fastest**, and the post says so — a reported loss, which counts for something.

### ParseBench-100 — on-device multimodal document understanding

100 tasks, 20 each across charts, layout, tables, text content, formatting.

| Harness | Mean | Chart | Layout | Table | Text | Format | Time | Tokens |
|---|---|---|---|---|---|---|---|---|
| **Computer** | **65.1%** | 76.5 | 16.2 | 72.7 | 87.9 | 72.4 | **60.6 s** | **20.1k** |
| Hermes | 34.6% | 29.3 | 2.9 | 44.1 | 61.5 | 35.2 | 108.3 s | 32.1k |
| Pi | 13.9% | 2.5 | 0.1 | 11.0 | 29.7 | 26.1 | 410.5 s | 829.1k |

The **41× token gap** between Computer (20.1k) and Pi (829.1k) on the same model and tasks is the clearest single demonstration of what harness design costs or saves. **Layout is bad for everyone** — 16.2% at best — and the post says so plainly.

### BrowseComp — 1,266 tasks

Computer **66.7%**, Pi 50.2%, Hermes 43.9%. Computer also fastest (402.1 s vs 826.0 / 1,020.9) and lowest-token (852k vs 2.82M / 1.01M).

> [!warning] This comparison does not isolate the harness
> *"Computer uses **Perplexity's search infrastructure** along with our local harness, while Pi and Hermes rely on **Brave**, their recommended search provider."*
>
> BrowseComp is a *web research* benchmark. Perplexity's core product is a search engine, and the post states its search *"has achieved top rankings in independent evaluations."* So a 16.5-point lead over Pi conflates **harness quality with search-backend quality**, with no ablation separating them. The post is transparent about the setup and draws the harness conclusion anyway. The ParseBench and LKWB numbers, which involve no search, are the defensible ones.

### Terminal Bench 2.1 — advisor escalation, priced

89 coding tasks, all in the Computer harness:

| Configuration | Score | API cost/rollout |
|---|---|---|
| Qwen 3.8 27B, fully local | 59.6% | ~$0 |
| Qwen 3.8 27B + **Claude Opus 5 advisor** | **73.0%** | $0.415 |
| **Claude Opus 5** alone | **82.4%** | $0.65 |

> "Escalation thus recovers roughly **three-fifths of the gap** to the frontier at about **two-thirds of the frontier's cost**."

The honest reading: escalation is a real but **sub-linear** trade — you pay 64% of frontier cost for 58% of the frontier gap, and you still end up 9.4 points short. The post says so: *"Advisor escalation narrows but does not fully close the gap."* Neither Pi nor Hermes was tested with escalation, because neither has an equivalent advisor tool.

## Post-training (PPLX 27B)

Post-trained **inside the Computer harness** on synthesised RL environments derived from real Perplexity Computer usage patterns. Each task is an **instruction + a Docker environment + a verifier**; tasks are **synthetic, containing no real user documents**. Two stages: **rejection fine-tuning** on best-scoring rollouts, then **reinforcement learning**.

Gains are modest and not free: **+2.8 points (82.6 → 85.4)** for **+30% tokens (520k → 678k)** and +32 s wall time.

> [!note] The held-out set shares a generator with the training set
> LKWB is *"a subset of tasks held out from training."* Held out, but drawn from the same synthesis pipeline and the same usage-derived distribution — a weaker control than an independently authored benchmark. That the base-model comparison (82.6 vs 77.6 vs 74.0) is also run on this benchmark means **the harness comparison inherits the same caveat**. Publishing the benchmark, as promised, would fix this.

## Entities mentioned

- [Portable Computer](../entities/perplexity-portable-computer.md) · [Hermes Agent](../entities/hermes-agent.md) · [DGX Spark](../entities/dgx-spark.md) · [Qwen](../entities/qwen.md) · [Nemotron](../entities/nemotron.md)

## Concepts touched

- [Harness design for capacity-limited models](../concepts/agents/local-model-harness-design.md)
- [Agent skills](../concepts/agents/agent-skills.md) · [LLM agent architecture](../concepts/agents/llm-agent-architecture.md)
- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)

## Open questions

- **How much of the BrowseComp lead is the search engine?** An ablation running Computer on Brave would settle it in one row. It is not reported.
- **Does the 100K effective-context finding generalise?** It is stated for Qwen 3.8 27B without supporting measurement. If the usable fraction of an advertised window is roughly 40% for small models generally, that is a planning number worth having — and nothing else in this wiki measures it.
- **No robot anywhere.** Every task is documents, research, email, code. The relevance is architectural: a robot's high-level agent faces the same small-model-on-fixed-hardware constraint, and this is the most detailed public account of designing for it.
- **Nothing measures the harness under contention.** Wall times assume the box is doing only this. A robot shares its compute with perception and control.
- **The technical report on model training is promised, not published.**

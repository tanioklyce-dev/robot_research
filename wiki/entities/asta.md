---
title: Asta (Ai2)
type: entity
subtype: platform
created: 2026-07-26
updated: 2026-07-26
sources: 1
tags: [asta, ai2, allen-institute, ai-for-science, scientific-discovery, llm-agents, agent-benchmark, autodiscovery, semantic-scholar, open-source]
---

# Asta (Ai2)

**Asta** is [Ai2](ai2.md)'s **agentic ecosystem for scientific discovery** — the flagship of its **AI for Science** mission pillar ([Ai2 homepage](../sources/ai2-homepage.md)). Where Ai2's [OLMo](olmo.md)/[Molmo](molmo.md) work builds open *foundation models*, Asta builds open *agents that do science on top of them*: framing research questions, tracing ideas to evidence, and distinguishing what's established from what's unresolved in a field. Live at asta.allen.ai.

## Why it matters in this wiki

Asta is the wiki's first **science-specific LLM-agent platform** — an application of the [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) aimed at scholarly research rather than robot control or software tasks. It also marks the point where Ai2's radical-openness stance extends from models to **agents and their evaluation**: AstaBench is an open leaderboard for science agents, mirroring what the OLMES eval suite did for open LLMs. It's the clearest signal in the wiki that Ai2 is a **three-pillar org** (Science / Planet / Embodied), not just the open-LLM lab.

## Three components

- **Asta Agents** — research assistants for "your most difficult scholarly research tasks"; mirror the scientific workflow (frame questions → trace ideas to evidence → identify established vs. unresolved).
- **AstaBench** — "a rigorous evaluation framework for AI agents, with leaderboards"; real-world scientific tasks for testing and comparing agent implementations.
- **Asta Resources** — tools, baseline agents, templates, and APIs for developers to build, test, and refine scientific AI agents.

## AutoDiscovery

A component (offered via **AstaLabs**) that **"autonomously generates hypotheses, runs experiments,"** using **Bayesian surprise** to flag discoveries. Free access was noted through **June 2026** ([Ai2 homepage](../sources/ai2-homepage.md)).

## Related

- [Ai2](ai2.md) — the org; Asta is its AI-for-Science pillar.
- **Semantic Scholar** — Ai2's research-paper discovery platform, the adjacent AI-for-Science product (no dedicated page yet).
- [OlmoEarth](olmoearth.md) — the sibling AI-for-the-Planet flagship.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Asta Agents are domain-specialized instances.

## Open questions

- **No primary ingested** beyond the homepage — the agent capabilities, AstaBench leaderboard methodology, and AutoDiscovery's Bayesian-surprise mechanism need a paper or the asta.allen.ai docs to deepen.
- How does AstaBench relate to general agent benchmarks (e.g. the software/tool-use leaderboards)? Is it science-task-specific end-to-end, or a harness others can reuse?

## Mentioned in

- [Ai2 homepage (allenai.org)](../sources/ai2-homepage.md) — the source that surfaced Asta.

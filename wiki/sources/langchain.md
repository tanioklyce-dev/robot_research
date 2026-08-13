---
title: LangChain — repository and docs (langchain-ai/langchain)
type: source
url: https://github.com/langchain-ai/langchain
author: LangChain (langchain-ai)
published: 2022-10-17 (repo created; read 2026-08-13)
ingested: 2026-08-13
license: MIT
tags: [langchain, langgraph, agent-framework, llm-application, integrations, dimos, transitive-dependency, primary-source]
---

## Summary

**LangChain** — *"the agent engineering platform."* MIT, **144,179★ / 24,005 forks**, created Oct 2022, pushed daily. *"A framework for building agents and LLM-powered applications… chain together interoperable components and third-party integrations… all while future-proofing decisions as the underlying technology evolves."*

Ingested because it was the last thing in this wiki's agent coverage held only by implication: it is the substrate under [LangGraph](../entities/langgraph.md), and it supplies the two functions [DimOS](../entities/dimos.md)'s robot agent actually calls — `create_agent` and `init_chat_model`.

## Key claims

- **Positioning is now "platform," not "chains."** The 2022-era chain-composition framing has been superseded: the README's quickstart is two lines (`init_chat_model` → `.invoke`), and it routes anything more ambitious elsewhere — **[LangGraph](../entities/langgraph.md)** for *"more advanced customization or agent orchestration,"* **Deep Agents** for planning/subagents/filesystem patterns, **LangSmith** for debugging and deployment.
- **The durable value proposition is integrations, not architecture.** *"Interoperable components and third-party integrations… future-proofing decisions as the underlying technology evolves."* Swapping model providers is a string change (`init_chat_model("openai:gpt-5.5")`).
- Ecosystem split: LangChain (components + integrations) → LangGraph (stateful orchestration) → Deep Agents (opinionated patterns) → LangSmith (observability + deployment).
- **408 open issues against 144 K stars** — a very low ratio for a project this size, and far below [DimOS](../entities/dimos.md)'s 16%.

## Analysis

> [!note] Why this wiki had it uncovered — a methodology miss, not a judgment call
> LangChain appears in **12 pages here**, which is above the threshold the [lint](../backlog.md) uses to flag a missing entity. It was not flagged, and the reason is worth recording: **the lint's "frequently mentioned, no page" check was a hand-written candidate list**, not a systematic extraction. I chose the terms to grep for — and picked `LangGraph` while omitting `LangChain`. The check found what it was told to look for.
>
> That is a real defect in the lint rather than in the wiki, and it generalizes: every term *not on the list* was invisible to it. Recorded on the [backlog](../backlog.md) as a check to automate.

> [!note] It reaches this wiki almost entirely as a transitive dependency
> The 12 mentions cluster in three unrelated places — [DimOS](../entities/dimos.md)'s agent layer, [NeMo Guardrails](../entities/nemo-guardrails.md)'s integration surface, and passing references in [XLeRobot](../entities/xlerobot.md) and Raspberry Pi AI-HAT material. **No ingested robotics source treats LangChain as a subject.** Which is the honest reason it stayed uncovered: this is a robotics wiki, and LangChain is infrastructure that robotics happens to sit on rather than a robotics artifact.
>
> The counter-argument for covering it anyway is the one this session kept hitting: **DimOS's agent calls `langchain.agents.create_agent`, not a LangGraph graph constructor** ([LangGraph source](langgraph.md)). The thing the largest agentic-robotics stack in the wiki actually invokes lives in *this* package.

> [!warning] "Framework churn" is a live risk for anything built on it
> Between 2022 and 2026 LangChain's own README moved from chains → agents → "agent engineering platform," and now defers orchestration to a sibling package that did not exist at the start. [DimOS](../entities/dimos.md) pins against this surface. Nothing here is evidence of instability *today* — but a robot stack whose agent layer tracks a fast-moving application framework inherits its migration cost, and the wiki has already seen one instance of that shape in the [Jetson AI Lab LeRobot tutorial](nvidia-jetson-ai-lab-lerobot.md), deprecated by a CLI refactor.

## Entities mentioned

- [LangChain](../entities/langchain.md) — the subject of this source
- [LangGraph](../entities/langgraph.md) — the orchestration sibling it defers to
- [DimOS](../entities/dimos.md) — calls `create_agent` and `init_chat_model` directly
- [NeMo Guardrails](../entities/nemo-guardrails.md) — integrates with it

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Agent skills](../concepts/agents/agent-skills.md)

## Open questions

- **No robotics-specific evidence read.** Nothing here establishes how well LangChain's abstractions suit a robot control path versus a chat application — which is the only question this wiki should care about.
- **LangSmith and Deep Agents** are both uncovered, and Deep Agents (planning, subagents, filesystem) is closer to what a robot task-planner needs than bare LangChain.
- What does DimOS's version pinning look like, and how exposed is it to the churn above?

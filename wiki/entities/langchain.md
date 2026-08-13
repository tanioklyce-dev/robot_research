---
title: LangChain
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [langchain, langgraph, agent-framework, llm-application, integrations, mit, dimos]
---

**LangChain** — *"the agent engineering platform."* MIT, **144,179★ / 24,005 forks**, created Oct 2022, pushed daily. A framework for building agents and LLM applications by **chaining interoperable components and third-party integrations**, pitched on *"future-proofing decisions as the underlying technology evolves."* Primary source: [LangChain repo + docs](../sources/langchain.md).

## The ecosystem split

| Layer | Package | Role |
|---|---|---|
| Components + integrations | **LangChain** | model/tool/retriever abstractions; `init_chat_model`, `create_agent` |
| Stateful orchestration | **[LangGraph](langgraph.md)** | graphs, durable execution, interrupts |
| Opinionated patterns | **Deep Agents** | planning, subagents, filesystem |
| Observability + deploy | **LangSmith** | tracing, evals, hosting |

The README's quickstart is now two lines and routes anything ambitious to the siblings — **the 2022-era "chains" framing is gone.**

## Why it matters in this wiki

Almost entirely as a **transitive dependency**, and one that turns out to be load-bearing:

- **[DimOS](dimos.md)**'s robot agent calls `langchain.agents.create_agent` and `langchain.chat_models.init_chat_model` **directly** — verified by [code read](../sources/langgraph.md). So the function the wiki's largest agentic-robotics stack actually invokes lives in *this* package, not in [LangGraph](langgraph.md), despite DimOS being described (by me, earlier) as "a LangGraph stack."
- **[NeMo Guardrails](nemo-guardrails.md)** integrates with it.
- Passing mentions in [XLeRobot](xlerobot.md) and Raspberry Pi AI-HAT material.

> [!note] Why it stayed uncovered — a lint defect, not a judgment
> LangChain appears in **12 pages**, above the threshold the [lint](../backlog.md) uses to flag missing entities. It was not flagged because that check was a **hand-written candidate list**, not a systematic extraction — I picked `LangGraph` and omitted `LangChain`. The check found exactly what it was told to look for, and everything off the list was invisible. Filed as a lint improvement.
>
> The substantive reason is defensible though: **no ingested robotics source treats LangChain as a subject.** This is a robotics wiki, and LangChain is infrastructure robotics happens to sit on.

> [!warning] Framework churn is the real risk for a robot stack
> 2022 → 2026 the README moved chains → agents → "agent engineering platform," and now defers orchestration to a package that did not exist at the start. [DimOS](dimos.md) pins against that surface. Not evidence of instability today, but a robot stack whose agent layer tracks a fast-moving application framework inherits its migration cost — the shape that already deprecated the [Jetson AI Lab LeRobot tutorial](../sources/nvidia-jetson-ai-lab-lerobot.md).

## Related

- [LangGraph](langgraph.md) — the orchestration sibling; see it for what DimOS actually uses
- [DimOS](dimos.md) · [NeMo Guardrails](nemo-guardrails.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md)

## Open questions

- **Nothing here establishes fitness for a robot control path** versus a chat application — the only question this wiki should care about.
- **Deep Agents is uncovered** and is closer to a robot task-planner's needs (planning, subagents, filesystem) than bare LangChain.
- **LangSmith** uncovered; it is the observability layer a deployed robot agent would actually want.

## Mentioned in

- [LangChain repo + docs](../sources/langchain.md)

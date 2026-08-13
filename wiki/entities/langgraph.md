---
title: LangGraph
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [langgraph, langchain, agent-framework, state-machine, tool-calling, dimos, llm-agent]
---

**LangGraph** — LangChain's *"low-level orchestration framework for building, managing, and deploying long-running, stateful agents."* Models an agent as a **graph of nodes over shared state** rather than a linear chain, adding cycles, branching, **durable execution (checkpointing)**, and **human-in-the-loop interrupts**. [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — **39,624★ / 6,652 forks**, MIT, created Aug 2023. Cited production users: Klarna, Replit, Elastic. Primary source: [LangGraph repo + docs](../sources/langgraph.md).

Positioning worth catching: it describes itself as **low-level infrastructure**, and points people who want to *"quickly build agents"* at **Deep Agents**, a higher-level package on top.

## The five pillars

| Pillar | What it is |
|---|---|
| **Durable execution** | agents that *"persist through failures… automatically resuming from exactly where they left off"* |
| **Human-in-the-loop** | `interrupt` — inspect and modify agent state mid-execution |
| **Comprehensive memory** | short-term working memory **and** long-term across sessions |
| **Debugging (LangSmith)** | execution-path tracing, state transitions |
| **Production deployment** | platform for long-running stateful workflows |

## Why it matters in this wiki

It is the agent runtime inside **[DimOS](dimos.md)**'s `McpClient` ([source](../sources/dimos-github.md)): the module holds a LangGraph agent that discovers every `@skill`-decorated method across deployed robot modules over RPC and exposes them as LangChain tools, served over **MCP**.

That makes LangGraph the concrete answer to a question the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) raised. Three of its four stacks hand-roll a dispatcher — a `PickupExecutor` FSM, `eval(f'self.{a}')`, ROS 2 services. **DimOS uses an off-the-shelf agent graph instead**, which is why it also breaks that synthesis's "everyone hand-rolls their tool schema" convergence.

> [!warning] What DimOS actually uses — verified by reading the code, 2026-08-13
> An earlier version of this page inferred that LangGraph's cycles and interrupts were *"the machinery for"* closed-loop replanning in DimOS. **A direct read of [`mcp_client.py`](https://github.com/dimensionalOS/dimos/blob/main/dimos/agents/mcp/mcp_client.py) shows DimOS uses almost none of it.**
>
> | Feature | Used? | Evidence |
> |---|---|---|
> | Tool-calling / ReAct loop | **yes** | `create_agent(model, tools, system_prompt)` — the prebuilt agent |
> | Cycles | yes, implicitly | the ReAct loop's own model↔tool cycle |
> | Custom graph topology | **no** | zero `StateGraph(`, `add_node`, `add_edge` |
> | **Checkpointing / durable execution** | **no** | no `checkpointer=`, `MemorySaver`, `thread_id`, or `config=` on `.stream()` |
> | **Human-in-the-loop interrupts** | **no** | zero `interrupt(` |
> | **Persistent memory** | **no** | history is a plain `list[BaseMessage]`, appended by hand |
>
> Verified across every `.py` in `dimos/agents/`: **zero** `MemorySaver`, `checkpointer`, `interrupt(`, or `thread_id`.
>
> **So the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md)'s "most consequential gap" — how skill failures surface back for re-planning — is *not* closed by DimOS.** All four stacks still fail it. This is now verification rather than assumption.

> [!note] The fix is a dependency they already have
> DimOS is **one constructor argument** from durable execution (`create_agent(..., checkpointer=...)`) and **one call** from human-in-the-loop (`interrupt()`). The capability is installed, imported, and unused.
>
> That reframes the wiki's critique of this category. The machinery for robust replanning is not missing or hard to obtain — it ships in the framework the largest stack in the space already depends on. **Nobody has needed it yet**, which is what you would expect where four stacks publish zero success rates between them. Durable execution pays off when runs are long and failures costly; demos are neither.
>
> Concrete consequence: **DimOS's agent has no memory across a crash.** History lives in a Python list on the module instance — kill the process and the conversation is gone, with no resume or replay. For a robot meant to run a household task over minutes to hours, that is a real limitation, and exactly what the durable-execution pillar is for.

> [!note] It rhymes with behavior trees, and the difference is auditability
> Both replace a linear plan with an explicitly re-enterable structure. But a [behavior tree](../concepts/robotics/behavior-trees.md)'s structure is **authored and inspectable** while a LangGraph agent's traversal is **model-driven** — precisely the trade the [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) says nobody has addressed. Note also that DimOS uses LangGraph's *highest*-level entry point (`create_agent`) rather than its low-level graph API, so "DimOS chose a graph runtime" overstates the design intent: what it chose was **a maintained ReAct loop with MCP tool binding**, which is the pragmatic call.

## Related

- [DimOS](dimos.md) — the robot stack that embeds it · [DimOS repo](../sources/dimos-github.md) · [LangGraph source page](../sources/langgraph.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md)
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the authored-structure alternative
- [OpenClaw](openclaw.md), [Hermes Agent](hermes-agent.md) — the other agent frameworks tracked here

## Open questions

- ~~No primary source; unknown whether DimOS uses cycles, checkpointing, or interrupts~~ — **both closed 2026-08-13** ([source](../sources/langgraph.md)): it uses the **tool-calling loop only**.
- **LangChain itself is still uncovered**, despite being the substrate and supplying `create_agent`.
- **Does *any* robot stack use LangGraph's durable execution?** DimOS does not. If none does, that is a stronger version of the finding above.
- **`interrupt()` as a robot safety rail** — the [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) argues the execution rail ships empty; human-in-the-loop interrupts are a ready-made mechanism and nothing here uses them. A design proposal, not an ingest.

## Mentioned in

- [LangGraph — repository and docs, read against DimOS's actual usage](../sources/langgraph.md)
- [DimOS GitHub repository](../sources/dimos-github.md)

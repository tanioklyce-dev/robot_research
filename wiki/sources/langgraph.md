---
title: LangGraph — repository and docs, read against DimOS's actual usage
type: source
url: https://github.com/langchain-ai/langgraph
author: LangChain (langchain-ai); DimOS usage read from dimensionalOS/dimos at main
published: 2023-08-09 (repo created; read at 2026-08-13)
ingested: 2026-08-13
license: MIT
tags: [langgraph, langchain, agent-framework, durable-execution, human-in-the-loop, checkpointing, state-machine, dimos, code-read, primary-source]
---

## Summary

**LangGraph** — *"low-level orchestration framework for building, managing, and deploying long-running, stateful agents."* MIT, **39,624★ / 6,652 forks**, created Aug 2023, pushed daily. Cited production users: Klarna, Replit, Elastic. `pip install -U langgraph`.

Ingested for a specific reason. The wiki's [LangGraph entity](../entities/langgraph.md) was written **secondhand from [DimOS](../entities/dimos.md)'s usage**, and it hung a load-bearing inference on the framework's capabilities: that its **cycles and human-in-the-loop interrupts are the machinery the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) found missing everywhere** — *"None describe in detail how skill failures surface back to the LLM for re-planning… the most consequential gap between published demo behavior and robust deployment."*

This source establishes what LangGraph actually offers, and a **direct read of DimOS's `mcp_client.py`** establishes how much of it DimOS uses. **The answer is: almost none of it.**

## Key claims — what LangGraph provides

Five pillars, per the README:

| Pillar | What it is |
|---|---|
| **Durable execution** | *"Agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off."* |
| **Human-in-the-loop** | *"Inspecting and modifying agent state at any point during execution"* — the `interrupt` mechanism |
| **Comprehensive memory** | Short-term working memory **and** long-term memory across sessions |
| **Debugging (LangSmith)** | Trace execution paths, capture state transitions, runtime metrics |
| **Production deployment** | Purpose-built platform for long-running stateful workflows |

Positioning note worth catching: LangGraph explicitly describes itself as **low-level infrastructure**, and the README points people who *"want to quickly build agents"* at **Deep Agents**, a higher-level package built on top. LangGraph is the substrate, not the batteries-included path.

## Key claims — what DimOS actually uses

Read directly from [`dimos/agents/mcp/mcp_client.py`](https://github.com/dimensionalOS/dimos/blob/main/dimos/agents/mcp/mcp_client.py) at `main`, 2026-08-13 (367 lines):

```python
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
...
self._state_graph = create_agent(
    model=model,
    tools=tools,
    system_prompt=self.config.system_prompt,
)
...
for update in state_graph.stream({"messages": self._history}, stream_mode="updates"):
```

| LangGraph feature | Used by DimOS? | Evidence |
|---|---|---|
| Tool-calling / ReAct loop | **Yes** | `create_agent(model, tools, system_prompt)` — the prebuilt agent |
| Cycles | **Yes, implicitly** | the ReAct loop's internal model↔tool cycle |
| **Custom graph topology** | **No** | zero `StateGraph(`, `add_node`, `add_edge` |
| **Checkpointing / durable execution** | **No** | no `checkpointer=`, no `MemorySaver`, no `thread_id`, no `config=` on `.stream()` |
| **Human-in-the-loop interrupts** | **No** | zero `interrupt(` |
| **Persistent memory** | **No** | history is a plain `self._history: list[BaseMessage]`, appended by hand |

Verified across **every `.py` in `dimos/agents/`**: **zero** occurrences of `MemorySaver`, `checkpointer`, `interrupt(`, or `thread_id`.

## Analysis

> [!warning] Correction to this wiki's own inference
> The [LangGraph entity](../entities/langgraph.md) argued that a graph runtime with checkpointing and interrupts *"is the machinery for"* closed-loop replanning, *"whether or not DimOS uses it that way."* The hedge was right and the emphasis was wrong. **DimOS uses LangGraph as a prebuilt ReAct agent runner and nothing more.**
>
> So the across-stacks synthesis's most consequential gap — **how skill failures surface back to the planner for re-planning** — is **not closed by DimOS**, and this source is the verification rather than a guess. All four stacks in that comparison still fail it.

> [!note] The interesting part: the fix is a dependency they already have
> DimOS is one constructor argument from durable execution (`create_agent(..., checkpointer=...)`) and one call from human-in-the-loop (`interrupt()`). **The capability is installed, imported, and unused.**
>
> That reframes the wiki's standing critique of the agentic-robotics category. The problem is not that the machinery for robust replanning doesn't exist or is hard to get — it ships in the framework the largest stack in this space already depends on. The problem is that **nobody has needed it yet**, which is what you would expect of a category where, as the same synthesis notes, **four stacks publish zero success rates between them**. Durable execution matters when runs are long enough and failures costly enough to be worth resuming; demos are neither.

> [!note] A concrete consequence: DimOS's agent has no memory across a crash
> History lives in a Python list on the module instance. **Kill the process and the conversation is gone** — no resume, no replay, no inspection of prior state. For a robot that is supposed to run a household task over minutes-to-hours, that is a real limitation, and it is the exact thing LangGraph's durable-execution pillar is for. Worth knowing before building on `McpClient`.

> [!note] Why "low-level" is the right description, and why that matters here
> The README steers quick-agent builders to **Deep Agents** instead. DimOS ends up using LangGraph's *highest*-level entry point (`create_agent`) rather than its low-level graph API — so it is paying for a low-level framework and consuming a convenience wrapper. Nothing wrong with that, but it means **the "DimOS chose a graph runtime" framing overstates the design intent**: what it chose was a maintained ReAct loop with MCP tool binding, which is the pragmatic call.

## Entities mentioned

- [LangGraph](../entities/langgraph.md) — the subject of this source
- [DimOS](../entities/dimos.md) — the usage this source was read against
- [OpenClaw](../entities/openclaw.md), [Hermes Agent](../entities/hermes-agent.md) — the other agent frameworks tracked here

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Agent skills](../concepts/agents/agent-skills.md)
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the authored-structure alternative to a model-driven graph

## Open questions

- **LangChain itself is still uncovered** by this wiki, despite being the substrate under LangGraph and supplying `create_agent`.
- **Does anything in robotics use LangGraph's durable execution?** DimOS does not. If no robot stack uses checkpointed agents, that is a stronger version of the finding above.
- **`interrupt()` as a robot safety rail.** The [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) argues the execution rail ships empty; human-in-the-loop interrupts are a ready-made mechanism for exactly that, and nothing in the wiki uses them. Worth a look as a design proposal rather than an ingest.
- No performance characteristics were read — graph overhead per step, streaming latency, memory cost of checkpointing.

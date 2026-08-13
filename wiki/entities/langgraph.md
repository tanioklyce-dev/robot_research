---
title: LangGraph
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [langgraph, langchain, agent-framework, state-machine, tool-calling, dimos, llm-agent]
---

**LangGraph** — LangChain's agent framework, tagline *"build resilient agents."* Models an agent as a **graph of nodes over shared state** rather than a linear chain, which gives it cycles, branching, checkpointing, and human-in-the-loop interrupts. [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — **39,624★ / 6,652 forks**, MIT, Python, created Aug 2023.

## Why it matters in this wiki

It is the agent runtime inside **[DimOS](dimos.md)**'s `McpClient` ([source](../sources/dimos-github.md)): the module holds a LangGraph agent that discovers every `@skill`-decorated method across deployed robot modules over RPC and exposes them as LangChain tools, served over **MCP**.

That makes LangGraph the concrete answer to a question the [across-stacks synthesis](../syntheses/agents/llm-agent-architecture-across-stacks.md) raised. Three of its four stacks hand-roll a dispatcher — a `PickupExecutor` FSM, `eval(f'self.{a}')`, ROS 2 services. **DimOS uses an off-the-shelf agent graph instead**, which is why it also breaks that synthesis's "everyone hand-rolls their tool schema" convergence.

> [!note] A graph is the right shape for a robot agent, and the wiki already knew it
> Cycles and interrupts are exactly what the synthesis found missing everywhere: *"None describe in detail how skill failures surface back to the LLM for re-planning… the most consequential gap between published demo behavior and robust deployment."* A graph runtime with checkpointing and human-in-the-loop interrupts is the machinery for that, whether or not DimOS uses it that way.
>
> It also rhymes with the wiki's [behavior-tree](../concepts/robotics/behavior-trees.md) coverage: both replace a linear plan with an explicitly re-enterable structure. The difference is that a BT's structure is **authored and auditable** while a LangGraph agent's traversal is **model-driven** — which is precisely the trade the [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) says is unaddressed.

## Related

- [DimOS](dimos.md) — the robot stack that embeds it · [DimOS repo](../sources/dimos-github.md)
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md)
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the authored-structure alternative
- [OpenClaw](openclaw.md), [Hermes Agent](hermes-agent.md) — the other agent frameworks tracked here

## Open questions

- **No primary source ingested** — everything is via DimOS's usage. No LangGraph documentation, and no evidence about whether DimOS actually uses its **cycles, checkpointing, or interrupts**, or just its tool-calling loop.
- The wiki has **no page for LangChain** itself, despite it being the substrate.

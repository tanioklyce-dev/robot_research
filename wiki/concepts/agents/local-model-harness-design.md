---
title: Harness design for capacity-limited models
type: concept
created: 2026-08-28
updated: 2026-08-28
sources: 1
tags: [agent-harness, local-models, context-efficiency, agent-skills, sandboxing, escalation, edge-agents, on-robot-agents, mcp]
---

**A harness** is the scaffold around a model in an agent system: the loop that assembles context, exposes tools, executes calls, and enforces policy. **Harness design for capacity-limited models** is the observation that a scaffold built for a frontier model is the wrong scaffold for a small one — and that the two should be designed together.

The framing, from the one ingested instance:

> "General-purpose harnesses assume a frontier model that can absorb long contexts, navigate a broad tool surface, and plan over long horizons. Local models are less reliable under those demands. Rather than asking a small model to manage a harness built for a large one, we shaped the two around each other." ([Perplexity Research](../../sources/perplexity-local-first-agent-research.md))

> [!note] One vendor-run instance, and it is about documents, not robots
> Everything below comes from [Perplexity's Portable Computer](../../entities/perplexity-portable-computer.md) research post, self-benchmarked against competitors it configured. It is filed here because **an on-robot agent is a capacity-limited model on fixed hardware** — the same constraint for the same reason — and this is the most detailed public account of engineering for it. No robot appears in the source.

## Why this is a distinct problem

A frontier model absorbs a bad harness. It tolerates a 200-tool surface, a bloated system prompt, and a trajectory that wanders, because it has capacity to spare. A 27–30B model on a desk or a robot does not, and the failure is not graceful: it loses the thread, forgets the goal, or picks the wrong tool.

So the harness stops being plumbing and becomes **the place where the capability gap is closed or lost**. The measured version of that claim, on the same model and tasks, is stark — three harnesses running Qwen 3.8 27B on identical document-understanding tasks scored **65.1% / 34.6% / 13.9%**, and the worst used **41× more tokens** than the best. Same model. The harness was the whole difference.

## The design moves

### 1. Treat the usable context as much smaller than the advertised one

> "Although on-device models such as Qwen 3.8 27B offer context windows of **260K tokens**, we found empirically that they **begin to struggle beyond 100K tokens**."

Roughly **40% of the spec sheet**. Everything else follows from budgeting against the real number: a minimal system prompt, a small core toolset, and **context compaction** that summarises stale trajectory as it grows.

### 2. Load capability on demand, not up front

Capabilities beyond the core become **[skills](agent-skills.md) that load and unload during the trajectory** — research, data science, visualisation, document creation, software engineering. The context cost of a capability is paid only while it is in use. This is the same move as demand-paging, and for the same reason: the working set is much smaller than the address space.

### 3. Compress the tool surface — MCP is not free

> "These are usually exposed to a harness as MCP servers, whose **large tool definitions consume a substantial share of the context**. Instead, we converted the most-used MCPs into compact command-line tools."

A protocol optimised for *discoverability* is a poor fit when context is the binding constraint. A CLI tool the model already knows how to use costs a line; an MCP server advertising its schema costs hundreds. Worth weighing against MCP's genuine advantages — this is a trade, not a verdict.

### 4. Make the orchestrator deterministic

> "The orchestrator is **deterministic harness code, not an LLM**: it maintains the loop, assembles context, and enforces policy. The local model proposes the next action; the orchestrator executes approved tool calls in the sandbox."

The model **proposes**; code **disposes**. This is the same authority split the wiki records at the opposite end of the stack — [Microduck's runtime](../../sources/microduck-runtime-repo.md) takes *intents* from clients and lets a deterministic safety layer decide what reaches a motor. Both rest on the same argument: a component you cannot bound should not hold the authority.

### 5. Verify, and monitor trajectory health

Self-verification triggered by the model *or* by **hooks watching the trajectory** that request verification when something looks wrong. It costs steps and is claimed to *"substantially narrow the gap to frontier models."* Compare [runtime failure detection](../robotics/runtime-failure-detection.md) — same instinct, applied to an agent trajectory rather than a policy rollout.

### 6. Fail closed on the sandbox

> "The harness executes tools in an **OS-level sandbox**… restricts processes, filesystem paths, and network access according to policy… **If the sandbox is unavailable, the harness disables itself before any tool calls rather than degrading to unsandboxed execution.**"

The failure *mode* is the design, not the sandbox. The alternative — degrade to unsandboxed and keep working — is what most harnesses do by default, and it converts an infrastructure problem into an arbitrary-code-execution problem at exactly the moment nobody is watching.

## Escalation as an architecture, not a fallback

When the local model is not enough, the harness exposes an **advisor**: a frontier model the local model may consult. The trust boundary is the interesting part.

- The **local model decides when to ask**; the **orchestrator decides what is sent**.
- A **PII classifier** flags sensitive content, and the user is **shown what would leave the device** before it does.
- The advisor **returns text guidance only** — *"no direct access to the device's files, tools, or conversations."*

So the remote model is an **advisor, never an actor**. Nothing it says executes without passing back through the local orchestrator and its sandbox. That is a cleaner property than "route hard tasks to the big model," and it is the version a robot would need — a cloud model that can *suggest* but never *actuate*.

Priced, on 89 coding tasks: local-only **59.6%**, with advisor **73.0%** at $0.415/rollout, frontier-only **82.4%** at $0.65. Escalation buys about **three-fifths of the gap for two-thirds of the cost** — real, sub-linear, and still 9.4 points short.

## Why this belongs in a robotics wiki

A robot's high-level agent is exactly this problem: a small model, on fixed hardware, sharing a box with perception and control, needing long-horizon reliability. Every constraint above applies, and two apply *harder*:

- **Context is scarcer**, because the robot's state stream competes for it.
- **The authority split is safety-critical**, not merely prudent. The [Microduck](../../entities/microduck.md) runtime and this harness independently arrive at *deterministic code holds authority, the model proposes* — from opposite directions, one at 50 Hz over motors and one over a filesystem.

The wiki's [on-device and on-robot agents](../../syntheses/agents/on-device-and-on-robot-agents.md) synthesis already argues that LLM latency makes the agent a **high-level** controller with reactive control staying local. This adds the layer below that: *given* you have a small local model, here is how the scaffold should be built.

## Related concepts

- [Agent skills](agent-skills.md) — the load-on-demand mechanism
- [LLM agent architecture](llm-agent-architecture.md) — the general pattern this specialises
- [On-device and on-robot agents](../../syntheses/agents/on-device-and-on-robot-agents.md) — the hardware tiers
- [Runtime failure detection](../robotics/runtime-failure-detection.md) — trajectory-health monitoring, policy-side
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — what "propose" versus "execute" means downstream

## Current state

**One source, vendor-run, document-domain.** The principles are engineering judgements with one worked example behind them, not established practice — and the benchmark that most cleanly demonstrates the harness effect (ParseBench-100) is also the one with the least at stake commercially, while the most impressive one (BrowseComp) is confounded by Perplexity's own search backend.

The number most worth someone independently checking: **usable context ≈ 40% of the advertised window** for a small model. If that holds generally, it changes how every on-robot agent should be budgeted, and nothing else in this wiki measures it.

## Mentioned in

- [A Local-First Agent for Private and Cost-Effective Knowledge Work](../../sources/perplexity-local-first-agent-research.md) — the six design moves, the advisor trust boundary, and the harness-only comparisons.

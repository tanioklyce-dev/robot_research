---
title: Agent–hardware abstraction
type: concept
created: 2026-08-30
updated: 2026-08-30
sources: 1
tags: [hardware-abstraction, device-drivers, mcp, mhs, capability-manifest, agentic-robotics, discovery, standards]
---

**Agent–hardware abstraction** — the interface layer that lets a language-model agent *discover* an unfamiliar physical device, learn what it can do, and operate it, without a human writing a bespoke integration for that device first. Distinct from the [LLM-agent architecture](llm-agent-architecture.md) above it (which assumes a skill library already exists) and from the device's own driver below it.

It is the layer this wiki has been implicitly assuming for two years, and the one the evidence says is the actual bottleneck.

## Why it is the bottleneck

- **[Project Fetch](../../sources/anthropic-project-fetch-robot-dog.md)** measured human teams with and without Claude on a quadruped, and the **largest single gap was connecting to unfamiliar hardware and reading its sensors** — not planning, not control theory. The [uplift](../safety/ai-uplift.md) came from the integration layer.
- Every practitioner account in the [MHS preview](../../sources/anthropic-model-hardware-standard-preview.md) independently describes the same tax: **weeks to months** of glue code per rig; a UW researcher who had already abandoned one automation attempt after "weeks spent evaluating platforms, chasing vendor support, learning and building glue code"; a Janelia rig needing **seven vendor programs launched in a fixed order**, where getting the order wrong cost the session.
- The cost is **quadratic in devices, not linear**, because integrations are pairwise. The stated goal of every system below is to make it linear: Ruetten's formulation — *"the cost of hardware integration stops scaling with the number of devices."*

## The common shape

Independently-derived systems in this wiki converge on four elements:

1. **A minimal primitive set.** [MHS](../../entities/model-hardware-standard.md): `read` / `write`. ROS 2: topics, services, actions. The primitives are deliberately weaker than the device's full API, because a small vocabulary is what makes heterogeneous devices comparable.
2. **A capability manifest the agent enumerates at runtime.** MHS's **states + procedures** reference file; [DimOS](../../entities/dimos.md)'s `@skill` decorator, where the docstring *becomes* the tool description and so cannot drift from the code; [AgenticROS](../../entities/agenticros.md)'s typed capability manifests serving six agent platforms from one robot; [ros2-mcp-server](../../entities/ros2-mcp-server.md)'s deterministic `name → handler` dispatch.
3. **Discovery.** Devices and agents find each other over the network in a standard format, rather than being wired together in a config file. This is what turns "the arm cannot fix bubbles" into "query the network for a device that can" — [Tetsuwan](../../entities/tetsuwan-scientific.md)'s centrifuge recovery.
4. **Out-of-band knowledge, in prose.** MHS's natural-language tags are the novel element: fields for what code cannot express — the weight of an arm, the fact that a well is fouled — filled in by the user or by an agent interviewing them, and compiled into the file the agent reads. The explicit target is knowledge currently held in paper manuals and tacit expertise.

## The instances

| System | Domain | Manifest source | Status |
|---|---|---|---|
| **[MHS](../../entities/model-hardware-standard.md)** ([Anthropic](../../entities/anthropic.md)) | lab + manufacturing instruments | auto-generated from driver tags | closed research preview, 2026-08 |
| **[MCP](llm-agent-architecture.md#mcp--model-context-protocol)** (Anthropic) | software services | server-declared tools | open, >1,000 connectors |
| **[ros2-mcp-server](../../entities/ros2-mcp-server.md)** | ROS 2 manipulation | hand-written tool set | first-party, [design notes](../../syntheses/projects/ros2-mcp-server-design.md) |
| **[AgenticROS](../../entities/agenticros.md)** | ROS 2 navigation | typed capability manifests | open source |
| **[DimOS](../../entities/dimos.md)** | mobile manipulation | `@skill` decoration | Apache 2.0 |
| **Strands Robots** (AWS) | agent↔device | unpublished | pre-release |

## Where they differ, and why it matters

- **Manifest authorship is the security boundary.** DimOS's `@skill` is **allow-by-decoration** — exposure is a property of the code, globally, to any attaching MCP client — which the [home-AI trust synthesis](../../syntheses/agents/home-ai-platform-trust-and-authority.md) contrasts against Matter's vendor-authored, deny-by-default ARL. MHS auto-generates the manifest *including the enforced safety limits*, putting it on the deny-by-default side, but from the device author rather than the ecosystem.
- **Only MHS reports preconditions on world state.** CMU induced six fault conditions — missing plate, rotated plate, reader busy, disconnected camera, unreachable device, active e-stop — and **all six were blocked before any device moved**. Every other system in the table enforces at the level of *tool names*, which is exactly the gap [guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) names: `pick(knife)` passes any name-level allowlist.
- **Nobody addresses semantic intent.** Blocking a rotated plate is a physical precondition, not a judgment about whether the action should happen. That remains unenforced everywhere in this wiki.

## The prose channel is an unexamined attack surface

MHS's natural-language tags are **untrusted text written by users (or elicited by an agent) that is compiled into the reference file the agent trusts to operate hardware**. This is the [prompt-injection-through-the-environment](../safety/ai-red-teaming.md) problem the [LLM-agent architecture](llm-agent-architecture.md) page flags for perception, relocated to device metadata — and it is arguably worse, because metadata is read once and believed thereafter, while perception is re-read. No ingested source examines it.

## Open questions

- **Does device abstraction subsume ROS, sit under it, or ignore it?** MHS's announcement never mentions ROS despite substantial functional overlap. Two ROS↔MCP bridges in this wiki arrived at capability manifests independently, which suggests the layers compose — but nobody has said how.
- **Does a standardized interface transfer capability, or just access?** MHS removes the integration work; it does not give the model physical intuition, which is what [Genentech](../../entities/genentech.md)'s bubbles and [QuEra](../../entities/quera-computing.md)'s "programmatic rather than physical" both ran into. The abstraction makes the model's *remaining* deficit more visible, not smaller.
- **What is the counterfactual?** No study compares the same agent loop over a standardized interface versus a bespoke API. The integration-time numbers are real; the capability numbers are confounded with the loop that produced them.

## Related concepts

- [LLM-agent architecture](llm-agent-architecture.md) — the pattern that consumes this layer.
- [Code as policy](code-as-policy.md) — what agents do *once* they have access: explore, then compile to a deterministic script.
- [Agent skills](agent-skills.md) — the durable artifact of that exploration.
- [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) — the execution rail this layer is the natural home for.
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — which rung the agent operates at once it has an interface.
- [Onboard robot service architecture](../robotics/onboard-robot-service-architecture.md) — the on-robot equivalent of the same normalization problem.

## Current state

**Access is being standardized faster than authority is.** As of August 2026 there are at least six independent capability-manifest systems, one of them from the vendor that also authored MCP, and the integration-cost reductions they report are large and consistent (weeks → hours). What none of them has is a policy layer that reasons about whether an enumerated capability *should* be invoked given the world state and the request — with the partial exception of MHS's device-state preconditions, demonstrated once, on six conditions, at one site.

## Mentioned in

- [Previewing the Model Hardware Standard](../../sources/anthropic-model-hardware-standard-preview.md)
- [Project Fetch: Can Claude train a robot dog?](../../sources/anthropic-project-fetch-robot-dog.md)
- [AgenticROS GitHub](../../sources/agenticros-github.md)
- [DimOS GitHub](../../sources/dimos-github.md)

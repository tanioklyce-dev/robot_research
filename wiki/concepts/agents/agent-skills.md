---
title: Agent skills (portable SKILL.md)
type: concept
created: 2026-07-16
updated: 2026-08-13
sources: 10
tags: [agent-skills, claude-code, skill-md, llm-agents, tooling, jetson, halos, frc, deployment]
---

# Agent skills (portable SKILL.md)

## Definition

An **agent skill** is a **portable, discoverable capability package** for an AI coding/agent tool — canonically a **`SKILL.md`** file (frontmatter metadata so the agent can *discover* when it applies) bundled with **helper scripts** the agent invokes to gather live data or perform an action. The agent reads the skill's instructions, runs the scripts, and reasons over the output. Skills are typically dropped into per-agent directories (`~/.claude/skills`, `~/.cursor/skills`, `~/.codex/skills`, `~/.agents/skills`) and are **cross-agent portable** — the same skill works across Claude Code, Cursor, and Codex.

Skills differ from raw **tool calls** and from **[MCP](llm-agent-architecture.md) servers**: an MCP server exposes tools over a protocol at runtime; a skill is a *filesystem-local instruction+script bundle* that encodes domain procedures ("how to inspect a Jetson," "how to deploy this safety blueprint") the base model doesn't know. They're the "give the agent a runbook" pattern.

## Why the pattern matters for robotics

Robotics vendors are shipping skills so that agents give **domain-correct** rather than **generic** advice, and so that **deployment is agent-drivable**:

- **[Jetson Device Skills](../../entities/jetson-device-skills.md)** — 8 skills teaching an agent to inspect/tune a live Jetson (diagnostics, memory audit, LLM-serving, benchmarking). Rationale: without them, agents give "generic Linux or dGPU advice that does not apply to Jetson" ([repo](../../sources/jetson-device-skills-github.md); [JetsonHacks demo](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md)).
- **[NVIDIA Halos](../../entities/nvidia-halos.md)** — ships LLM deploy skills (**`warehouse-deploy`**, **`halos-deploy`**, and the Outside-In blueprint's **Claude Code deploy skill**) that automate prerequisites, NGC downloads, config, and VSS integration for a functional-safety deployment ([Halos blog](../../sources/nvidia-halos-robotics-blog.md), [Outside-In repo](../../sources/halos-outside-in-safety-github.md)).
- **FRC** — championship teams ship **agent skill files** alongside their codebase so an agent can drive a repo-specific workflow ([Team 4414 HighTide binder](../../sources/team-4414-hightide-2026-binder.md); [Team 254's wpilib-agent-tools](../../sources/team-254-ai-in-frc-presentation.md)).

The common thread: as robots and their toolchains become agent-operated, **the vendor's operational knowledge ships as skills** rather than as PDFs a human reads.

> [!note] A third sense of "skill" — the robot's own, exposed to agents
> This page covers the *filesystem runbook* sense (`SKILL.md` + scripts). **[DimOS](../../entities/dimos.md)** uses the word for a third thing: a **`@skill`-decorated method on a running robot module**, discovered by RPC introspection at agent startup and republished as an **MCP** tool ([repo](../../sources/dimos-github.md)). Its docstring plays exactly the role a `SKILL.md` description plays — it is what the LLM reads to decide whether the capability applies — but the artifact is live code on hardware, not a file in `~/.claude/skills`.
>
> The convergence is worth noting: **all three senses (runbook bundle, MCP server, robot method) are solving the same problem** — how does a model learn what it can do here, in enough detail to do it correctly. DimOS's answer is the one with no separate artifact to maintain. DimOS also closes the loop the other way: its README directs *coding agents* ([OpenClaw](../../entities/openclaw.md), Claude Code) at an `AGENTS.md` and the `dimos` CLI, so an agent-skill in the runbook sense drives a stack whose robot capabilities are agent-skills in the MCP sense.

## Practitioner caution

The [JetsonHacks demo](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md) frames the governing rule: *"The agent works for you. You do not work for it."* Skills accelerate an agent that's already well-directed — but an undirected agent "can build slop an order of magnitude faster than you can throw it out." Skills raise the ceiling, not the floor; upfront specification still dominates outcomes.

## Related concepts

- [LLM-agent architecture](llm-agent-architecture.md) — the agent runtime skills plug into (tools, MCP, memory)
- [Robot security](../robotics/robot-security.md) — agent-drivable deployment expands the trust surface (a skill runs scripts on real hardware); DimOS moves the surface from `eval`-injection to **authentication of an MCP endpoint that exposes every robot skill**
- [DimOS](../../entities/dimos.md) — `@skill` methods discovered by RPC and served over MCP

## Mentioned in

- [Jetson Device Skills GitHub](../../sources/jetson-device-skills-github.md), [JetsonHacks AI-coding-on-Jetson](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md)
- [NVIDIA Halos blog](../../sources/nvidia-halos-robotics-blog.md), [Halos Outside-In GitHub](../../sources/halos-outside-in-safety-github.md)
- [DimOS GitHub repository](../../sources/dimos-github.md)
- [Team 4414 HighTide binder](../../sources/team-4414-hightide-2026-binder.md), [Team 254 AI-in-FRC](../../sources/team-254-ai-in-frc-presentation.md)
- [CaP-X paper](../../sources/cap-x-paper.md) — a skill library **mined automatically** from successful rollouts (9 task-agnostic primitives, pooled across 12 models) rather than hand-authored.
- [ASPIRE paper](../../sources/aspire-paper.md) — the strongest contrast with SKILL.md bundles: skills are induced from *diagnosed failures* (failure signature + when-to-apply + repair), the taxonomy emerges rather than being designed, and a coordinator audits admissions. Measured to compound: zero-shot success rises with library size.

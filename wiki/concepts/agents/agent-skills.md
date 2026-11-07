---
title: Agent skills (portable SKILL.md)
type: concept
created: 2026-07-16
updated: 2026-11-07
sources: 22
tags: [agent-skills, claude-code, skill-md, llm-agents, tooling, jetson, halos, frc, deployment]
---

# Agent skills (portable SKILL.md)

## Definition

An **agent skill** is a **portable, discoverable capability package** for an AI coding/agent tool — canonically a **`SKILL.md`** file (frontmatter metadata so the agent can *discover* when it applies) bundled with **helper scripts** the agent invokes to gather live data or perform an action. The agent reads the skill's instructions, runs the scripts, and reasons over the output. Skills are typically dropped into per-agent directories (`~/.claude/skills`, `~/.cursor/skills`, `~/.codex/skills`, `~/.agents/skills`) and are **cross-agent portable** — the same skill works across Claude Code, Cursor, and Codex.

Skills differ from raw **tool calls** and from **[MCP](llm-agent-architecture.md) servers**: an MCP server exposes tools over a protocol at runtime; a skill is a *filesystem-local instruction+script bundle* that encodes domain procedures ("how to inspect a Jetson," "how to deploy this safety blueprint") the base model doesn't know. They're the "give the agent a runbook" pattern.

## Why the pattern matters for robotics

Robotics vendors are shipping skills so that agents give **domain-correct** rather than **generic** advice, and so that **deployment is agent-drivable**:

- **[Jetson Device Skills](../../entities/jetson-device-skills.md)** — 8 skills teaching an agent to inspect/tune a live Jetson (diagnostics, memory audit, LLM-serving, benchmarking). Rationale: without them, agents give "generic Linux or dGPU advice that does not apply to Jetson" ([repo](../../sources/jetson-device-skills-github.md); [JetsonHacks demo](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md)).
- **[Isaac ROS](../../entities/isaac-ros.md) 5.0** (Sep 2026) — ships skills in the open Agent Skills format: `isaac-ros-activate`, an early-access **`migrate-node-to-rosidl-buffer`** (an agent to help port code off NITROS, which the same release removes), setup and manipulation skills, a standalone **pick-and-place** skill, and a **FoundationStereo fine-tuning skill** — the first skill in the wiki whose job is *adapting a model* to a user's cameras rather than calling one. More Isaac skills sit in the `nvidia/skills` catalog under "Physical AI," plus "agent-ready documentation" ([5.0 blog](../../sources/nvidia-isaac-ros-5-0-blog.md), [release notes](../../sources/isaac-ros-release-notes-and-platforms.md)).
- **[NVIDIA Halos](../../entities/nvidia-halos.md)** — ships LLM deploy skills (**`warehouse-deploy`**, **`halos-deploy`**, and the Outside-In blueprint's **Claude Code deploy skill**) that automate prerequisites, NGC downloads, config, and VSS integration for a functional-safety deployment ([Halos blog](../../sources/nvidia-halos-robotics-blog.md), [Outside-In repo](../../sources/halos-outside-in-safety-github.md)).
- **FRC** — championship teams ship **agent skill files** alongside their codebase so an agent can drive a repo-specific workflow ([Team 4414 HighTide binder](../../sources/team-4414-hightide-2026-binder.md); [Team 254's wpilib-agent-tools](../../sources/team-254-ai-in-frc-presentation.md)).

The common thread: as robots and their toolchains become agent-operated, **the vendor's operational knowledge ships as skills** rather than as PDFs a human reads.

> [!note] A third sense of "skill" — the robot's own, exposed to agents
> This page covers the *filesystem runbook* sense (`SKILL.md` + scripts). **[DimOS](../../entities/dimos.md)** uses the word for a third thing: a **`@skill`-decorated method on a running robot module**, discovered by RPC introspection at agent startup and republished as an **MCP** tool ([repo](../../sources/dimos-github.md)). Its docstring plays exactly the role a `SKILL.md` description plays — it is what the LLM reads to decide whether the capability applies — but the artifact is live code on hardware, not a file in `~/.claude/skills`.
>
> The convergence is worth noting: **all three senses (runbook bundle, MCP server, robot method) are solving the same problem** — how does a model learn what it can do here, in enough detail to do it correctly. DimOS's answer is the one with no separate artifact to maintain. DimOS also closes the loop the other way: its README directs *coding agents* ([OpenClaw](../../entities/openclaw.md), Claude Code) at an `AGENTS.md` and the `dimos` CLI, so an agent-skill in the runbook sense drives a stack whose robot capabilities are agent-skills in the MCP sense.

## Practitioner caution

The [JetsonHacks demo](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md) frames the governing rule: *"The agent works for you. You do not work for it."* Skills accelerate an agent that's already well-directed — but an undirected agent "can build slop an order of magnitude faster than you can throw it out." Skills raise the ceiling, not the floor; upfront specification still dominates outcomes.

## Skills as a context budget, not just an abstraction

The [Perplexity local harness](../../sources/perplexity-local-first-agent-research.md) uses skills for a reason that is quantitative rather than architectural: on a small local model, **context is the binding constraint**, so capability has to be paged in.

Their finding is that Qwen 3.8 27B advertises a **260K** context window but *"begins to struggle beyond **100K** tokens"* — roughly 40% usable. The response is a minimal core (small system prompt, small core toolset) with everything else as **skills that load and unload through the trajectory**, plus compaction of stale context.

The same reasoning drove them to convert connectors from **MCP servers into compact CLI tools**, *"whose large tool definitions consume a substantial share of the context."* Read alongside [harness design for capacity-limited models](local-model-harness-design.md): skills are demand paging, and MCP's discoverability is a cost you pay in the working set.

## Skills that repair themselves (2026-10-24)
[RPG](../../sources/rpg-guided-self-improvement-paper.md) treats a robot skill library as **persistent, versioned code under a regression gate**. An agent proposes new skills and edits; each must load, pass interface checks and use only deploy-time observations, then improve mean success across 22 tasks without dropping any one by more than 20 pp. Over 15 rounds the library went from 15 to 38 entries, with 23 additions and **66 modifications**. Most gains came from making skills **verify their effects**: actual lift height, grasp retention, final placement. The robotics version of the portable-skill caution above is that a skill's *return value* is part of its contract, and it can lie.

## Skills whose descriptions the agent writes (2026-11-07)

In [ToyBlocks](../../entities/toyblocks.md), Ai2 exposes robot skills (pick, flip, rotate, each targeted by pointing at a pixel) to a Claude Opus 5.5 agent over MCP. It then lets the agent **experiment on its own skills** (form a hypothesis about unexpected behaviour, design a small test, revise) and **rewrite the skill descriptions** from what it found. Success rose from **24% with the default descriptions to 63%**, against **36% with descriptions written by a human expert** ([ToyBlocks (Ai2 blog)](../../sources/ai2-toyblocks-blog.md); method credited to a linked OpenReview paper not yet ingested). RPG edits the skill code and ASPIRE adds new skills to the library. This changes only the **documentation**. Here the skill is fixed and its description was the bottleneck. In this case the agent's empirical model of the skills was better than the expert's.

### The mechanism: LEAP ([allenai/agentic_robotics](../../sources/allenai-agentic-robotics-github.md))

The code makes the setup explicit. In an **experimentation phase**, an agent has the motor skills plus simulator get/set state, a file workspace and `update_tool_docstring`. It explores either by spawning subagents (**Naive**) or through `plan_experiment`/`run_experiment`, which forces a hypothesis, success criteria and labelled trials before anything runs (**Harness**). The phase is capped by a **dollar budget**, and the prompt quotes token prices and warns that each docstring edit invalidates the prompt cache. A *fresh* agent is then evaluated with only the motor and image tools and the learned docstrings. It is compared against Control (the declared docstrings) and Oracle (expert-written ones that state failure rates: stack drops the block 10% of the time, rotate goes the wrong way 25%, flip has no effect 10% and goes the wrong direction 20%, and so on). The design treats a skill's description as a **learned, transferable artifact**, separate from the agent that learned it. The repo's rule that *"a skill's docstring is a prompt"* comes out of the same view.

## Skills that encode a project's contribution standard (2026-11-07)

[XPolicyLab](../../entities/xpolicylab.md) ships two skills in `.agents/skills/`, symlinked from `.claude/skills` and `.cursor/skills` so Claude Code, Cursor and Codex all load them ([XPolicyLab GitHub](../../sources/xpolicylab-github.md)).
- `xpolicylab-model-integration` turns *"Integrate <POLICY> into XPolicyLab"* into a scaffold → `model.py` → debug-loop workflow.
- `xpolicylab-adapter-check` is a nine-point pre-PR audit.

`AGENTS.md` is the always-on layer, and the root `CLAUDE.md` is just `@AGENTS.md`. The interesting feature is the writing style. Each rule carries its reason. For example, a hand-added `COLOR_BGR2RGB` is called *"always a bug"* because two JPEG byte formats coexist and only an in-buffer marker tells them apart. The authors seem to have found that agents re-derive and "fix" rules they are given without reasons. These skills are about a project's conventions, not robot control, but they are what produces the adapters that robot benchmarks score.

## Related concepts

- [LLM-agent architecture](llm-agent-architecture.md) — the agent runtime skills plug into (tools, MCP, memory)
- [Robot security](../robotics/robot-security.md) — agent-drivable deployment expands the trust surface (a skill runs scripts on real hardware); DimOS moves the surface from `eval`-injection to **authentication of an MCP endpoint that exposes every robot skill**
- [DimOS](../../entities/dimos.md) — `@skill` methods discovered by RPC and served over MCP

## Mentioned in

- [Jetson Device Skills GitHub](../../sources/jetson-device-skills-github.md), [JetsonHacks AI-coding-on-Jetson](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md)
- [NVIDIA Halos blog](../../sources/nvidia-halos-robotics-blog.md), [Halos Outside-In GitHub](../../sources/halos-outside-in-safety-github.md)
- [DimOS GitHub repository](../../sources/dimos-github.md)
- [NVIDIA Isaac ROS 5.0 blog](../../sources/nvidia-isaac-ros-5-0-blog.md) — Isaac skills, FoundationStereo fine-tuning skill, NITROS-migration skill.
- [Team 4414 HighTide binder](../../sources/team-4414-hightide-2026-binder.md), [Team 254 AI-in-FRC](../../sources/team-254-ai-in-frc-presentation.md)
- [CaP-X paper](../../sources/cap-x-paper.md) — a skill library **mined automatically** from successful rollouts (9 task-agnostic primitives, pooled across 12 models) rather than hand-authored.
- [ASPIRE paper](../../sources/aspire-paper.md) — the strongest contrast with SKILL.md bundles: skills are induced from *diagnosed failures* (failure signature + when-to-apply + repair), the taxonomy emerges rather than being designed, and a coordinator audits admissions. Measured to compound: zero-shot success rises with library size.
- [RPG](../../sources/rpg-guided-self-improvement-paper.md) — regression-gated self-repairing robot skill library.
- [AW-0 paper](../../sources/agentic-world-action-models-aw0-paper.md) — a 50-skill library distilled by a Claude Code coordinator and then **frozen** as the *label vocabulary* for training a WAM; skills are supervision targets, not runtime tools.
- [ToyBlocks (Ai2 blog)](../../sources/ai2-toyblocks-blog.md) — agent-authored skill descriptions from self-run experiments: 24% → 63% vs 36% for expert-written.
- [allenai/agentic_robotics](../../sources/allenai-agentic-robotics-github.md) — LEAP: Control / Naive / Harness / Oracle description sets; dollar-budgeted experimentation; the learned docstrings transfer to a fresh evaluation agent.
- [XPolicyLab GitHub](../../sources/xpolicylab-github.md) — repo-shipped integration and audit skills for Claude Code, Codex and Cursor; rules written with their reasons attached.

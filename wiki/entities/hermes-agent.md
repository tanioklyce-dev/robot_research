---
title: Hermes Agent
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 2
tags: [hermes-agent, nous-research, agentic-framework, self-improvement, mcp, sub-agents, skills, openrouter, multi-platform, qwen-3-6, dgx-spark, claw-ecosystem]
---

**Hermes Agent** — open-source **self-improving autonomous AI agent framework** from **Nous Research**. MIT-licensed; **171K stars / 28.7K forks** (May 2026); Python 89% / TypeScript 8%; latest release v0.14.0 (May 16 2026). Repo: [github.com/nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent). Featured in NVIDIA's RTX AI Garage as a flagship [DGX Spark](dgx-spark.md) workload ([blog](../sources/nvidia-rtx-ai-garage-hermes-agent.md)), and reportedly *"the most used agent in the world according to OpenRouter"* as of May 2026.

## What makes it distinctive

Four features the NVIDIA blog highlights:

1. **Self-Evolving Skills** — agents write and refine their own skills over time.
2. **Contained Sub-Agents** — isolated parallel workers spawned for sub-tasks.
3. **Reliability by design** — curated and stress-tested components.
4. **Same model, better results** — active orchestration loop, not a passive LLM wrapper.

## Architecture (per [GitHub README](../sources/hermes-agent-github.md))

| Layer | Path | Role |
|---|---|---|
| Agent Core | `/agent` | Main reasoning loop |
| Terminal Backends | — | Local / Docker / SSH / Singularity / Modal / Daytona |
| Gateway | `/gateway` | Telegram / Discord / Slack / WhatsApp / Signal / CLI / email |
| Skills System | `/skills` | Procedural memory; **agentskills.io** standard compatible |
| Tools | `/tools` | 40+ built-in tools |
| MCP Integration | — | Connect external [MCP](../concepts/agents/llm-agent-architecture.md) servers |
| Memory | — | Persistent + user profiling via **Honcho** dialectic modeling |

## Model flexibility

**200+ models** via OpenRouter / Nous Portal / NovitaAI / NVIDIA NIM / Xiaomi MiMo / z.ai/GLM / Kimi-Moonshot / MiniMax / Hugging Face / OpenAI / custom endpoints. Model-agnostic. NVIDIA blog specifically pairs it with **[Qwen](qwen.md) 3.6 27B / 35B** on DGX Spark.

## Position in the Claw ecosystem

Hermes Agent is the **Nous Research entry** in a 3-project landscape of open-source personal-AI-agent frameworks that share "Claw" naming (the lineage trades on a "Molty space lobster" pun + the Claude homophone):

| Project | Author | Role | License | Stars |
|---|---|---|---|---|
| [OpenClaw (personal AI)](openclaw-personal-ai.md) | Peter Steinberger + community | Foundational personal-AI-assistant framework | MIT | **375K** |
| [NemoClaw](nemoclaw.md) | NVIDIA | Security + Nemotron + DGX-aware wrapper over OpenClaw | (early preview) | — |
| **Hermes Agent** | Nous Research | Self-improving sibling; offers `hermes claw migrate` import-from-OpenClaw path | MIT | 171K |

> [!note] OpenClaw migration covers the whole Claw family
> Hermes Agent's `hermes claw migrate` command imports from the [Steinberger OpenClaw personal AI assistant](openclaw-personal-ai.md). Per user (2026-05-28; pending primary-source confirmation), [Hiwonder's robotics OpenClaw](openclaw.md) is a downstream distribution of the same upstream — so a `hermes claw migrate` from a Hiwonder ROSOrin Pro install should plausibly carry over (settings, skills, API keys) **even though the robot-specific ROS 2 extensions won't have Hermes-Agent equivalents** until someone writes a ros-mcp-server bridge.

## Robot-platform fit

**Hermes Agent has no native robot integration.** The closest analogue is the community **`computer-use-linux` MCP server** for desktop automation (AT-SPI accessibility trees, X11/Wayland input, screenshots) — the same architectural pattern a robot integration would follow: **write an MCP server that wraps ROS 2 actions / topics / services as MCP tools, register with Hermes**.

Would-be advantages over a per-robot LLM-agent stack like [Hiwonder OpenClaw](openclaw.md) or [stretch_ai](stretch-ai.md):

- **Self-evolving skill library** — robot would gain new manipulation primitives from experience, not just from hand-coded ROS skills.
- **Sub-agent decomposition** — long tidy tasks could be decomposed into isolated sub-agents (find-objects, navigate, manipulate, verify) running in parallel.
- **Persistent user model** — over time, the robot remembers user preferences ("the laundry basket is in the closet, not the bedroom").
- **Multi-platform messaging gateway** — control the robot from Telegram / Signal / etc. without writing custom UIs.

What's missing:
- **Robot-specific safety guardrails** — Hermes Agent's "reliability by design" addresses LLM reliability, not actuator safety. A safety layer between Hermes and physical actuators would still be needed.
- **Real-time control loop** — Hermes Agent is async / cron-driven, not 10 Hz visuomotor.
- **Visuomotor skill substrate** — Hermes orchestrates symbolic skills; it doesn't replace a LeRobot-trained policy for low-level grasping.

## Compute requirements

Sized for the [DGX Spark](dgx-spark.md) tier per NVIDIA's positioning — 128 GB unified memory + 1 PFLOP AI can serve a **120B-MoE model all day** as the brain. Lower-tier hardware works with smaller models (8B–35B class via [Ollama](ollama.md) / llama.cpp / LM Studio).

## Related

- [OpenClaw (Steinberger)](openclaw-personal-ai.md) — foundational sibling; offers migration path TO Hermes.
- [NemoClaw](nemoclaw.md) — NVIDIA-secured sibling stack.
- [OpenClaw (Hiwonder)](openclaw.md) — downstream robotics distribution of Steinberger OpenClaw; same upstream family (per user; pending primary-source confirmation).
- [DGX Spark](dgx-spark.md) — flagship local-hardware target.
- [Qwen](qwen.md) — recommended LLM family.
- [Ollama](ollama.md) — supported runtime.
- [stretch_ai](stretch-ai.md) — closest in spirit on the robot side; LLM-agent stack but robot-specific.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — concept page.

## Mentioned in

- [NVIDIA RTX AI Garage — Hermes Agent on DGX Spark](../sources/nvidia-rtx-ai-garage-hermes-agent.md) — Gore, May 13 2026.
- [Hermes Agent GitHub README](../sources/hermes-agent-github.md) — primary source.

## Open questions

- **No native robot integration** — has anyone in the community built a ROS-MCP server for Hermes? Would be high-value.
- **Self-evolving skills mechanism** — concrete details not in the README; how does it actually generate new tools?
- **"Most used agent in the world" claim** — what's the OpenRouter measurement methodology?
- **Hermes 4 LLM vs Hermes Agent** — Nous Research's flagship LLM and flagship agent share the "Hermes" brand; relationship not yet captured in this wiki.
- **`hermes claw migrate` lineage** — Steinberger OpenClaw → Hermes migration path is built-in. Is there a competitive/cooperative relationship between the two projects?

---
title: Hermes Agent
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-07-05
sources: 4
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
| [OpenClaw](openclaw.md) | Peter Steinberger + community | Foundational personal-AI-assistant framework | MIT | **375K** |
| [NemoClaw](nemoclaw.md) | NVIDIA | Security + Nemotron + DGX-aware wrapper over OpenClaw | (early preview) | — |
| **Hermes Agent** | Nous Research | Self-improving sibling; offers `hermes claw migrate` import-from-OpenClaw path | MIT | 171K |
| [openclaw_controller](openclaw-controller.md) | Hiwonder | ROS 2 bridge module that puts OpenClaw on the [ROSOrin Pro](rosorin-pro.md) — not a fork; sits below OpenClaw as an extension | — | — |

> [!note] OpenClaw migration on a ROSOrin Pro
> Hermes Agent's `hermes claw migrate` command imports an existing [OpenClaw](openclaw.md) install (settings, skills, API keys). On a ROSOrin Pro running OpenClaw via Hiwonder's [`openclaw_controller`](openclaw-controller.md) bridge, that migration should carry the OpenClaw side cleanly **but the robot-specific ROS 2 services exposed by `openclaw_controller` won't have Hermes-Agent equivalents** until someone writes a ros-mcp-server that wraps the same services.

## Robot-platform fit

**Hermes Agent has no native robot integration**, but the community bridge now exists: **[AgenticROS](agenticros.md)** ships an MCP server (`@agenticros/claude-code`, shared with Claude Code/Desktop and Codex) that Hermes registers as a standard MCP client via `.hermes/config.yaml`, exposing missions, follow-me, find-object, memory, and the full ROS command surface ([AgenticROS GitHub](../sources/agenticros-github.md)). This is exactly the "write an MCP server that wraps ROS 2 actions/topics/services, register with Hermes" pattern this page previously predicted — though AgenticROS covers nav/camera skills only, no manipulation (see [ros2-mcp-server](ros2-mcp-server.md) for that layer).

Would-be advantages over the current OpenClaw + [`openclaw_controller`](openclaw-controller.md) stack on the ROSOrin Pro or [stretch_ai](stretch-ai.md):

- **Self-evolving skill library** — robot would gain new manipulation primitives from experience, not just from hand-coded ROS skills.
- **Sub-agent decomposition** — long tidy tasks could be decomposed into isolated sub-agents (find-objects, navigate, manipulate, verify) running in parallel.
- **Persistent user model** — over time, the robot remembers user preferences ("the laundry basket is in the closet, not the bedroom").
- **Multi-platform messaging gateway** — control the robot from Telegram / Signal / etc. without writing custom UIs.

What's missing:
- **Robot-specific safety guardrails** — Hermes Agent's "reliability by design" addresses LLM reliability, not actuator safety. A safety layer between Hermes and physical actuators would still be needed.
- **Real-time control loop** — Hermes Agent is async / cron-driven, not 10 Hz visuomotor.
- **Visuomotor skill substrate** — Hermes orchestrates symbolic skills; it doesn't replace a LeRobot-trained policy for low-level grasping.

## Compute requirements

Sized for the [DGX Spark](dgx-spark.md) tier per NVIDIA's positioning — 128 GB unified memory + 1 PFLOP AI can serve a **120B-MoE model all day** as the brain. Lower-tier hardware works with smaller models (8B–35B class via [Ollama](ollama.md) / llama.cpp / LM Studio). See the [on-device / on-robot / local-server agents synthesis](../syntheses/agents/on-device-and-on-robot-agents.md) for the deployment-tier framing.

## Running Hermes inside NemoClaw

NVIDIA ships Hermes as a **selectable agent variant in [NemoClaw](nemoclaw.md)** ([quickstart](../sources/nvidia-nemoclaw-hermes-quickstart.md)): `export NEMOCLAW_AGENT=hermes` (the `nemohermes` alias) creates an **OpenShell sandbox** running Hermes instead of the default OpenClaw agent — dashboard on port 18789, OpenAI-compatible API on port 8642, default model `nvidia/nemotron-3-super-120b-a12b` via NVIDIA inference endpoints, with OpenShell network-policy tiers gating egress. Hermes and OpenClaw sandboxes can run side by side. This is the concrete NVIDIA-blessed local-deployment path (contrast the raw [GitHub](../sources/hermes-agent-github.md) install).

## Related

- [OpenClaw](openclaw.md) — foundational sibling; offers migration path TO Hermes.
- [NemoClaw](nemoclaw.md) — NVIDIA-secured sibling stack.
- [openclaw_controller](openclaw-controller.md) — Hiwonder's ROS 2 bridge module that runs OpenClaw on the ROSOrin Pro.
- [DGX Spark](dgx-spark.md) — flagship local-hardware target.
- [Qwen](qwen.md) — recommended LLM family.
- [Ollama](ollama.md) — supported runtime.
- [stretch_ai](stretch-ai.md) — closest in spirit on the robot side; LLM-agent stack but robot-specific.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — concept page.

## Mentioned in

- [NVIDIA RTX AI Garage — Hermes Agent on DGX Spark](../sources/nvidia-rtx-ai-garage-hermes-agent.md) — Gore, May 13 2026.
- [Hermes Agent GitHub README](../sources/hermes-agent-github.md) — primary source.
- [NemoClaw Quickstart with Hermes](../sources/nvidia-nemoclaw-hermes-quickstart.md) — the NemoClaw deployment path (`nemohermes` + OpenShell sandbox).
- [AgenticROS GitHub](../sources/agenticros-github.md) — community ROS 2 MCP server that registers with Hermes.

## Open questions

- ~~**No native robot integration** — has anyone in the community built a ROS-MCP server for Hermes? Would be high-value.~~ **Resolved 2026-07-05**: [AgenticROS](agenticros.md) is exactly this (nav/camera skills; no manipulation yet).
- **Self-evolving skills mechanism** — concrete details not in the README; how does it actually generate new tools?
- **"Most used agent in the world" claim** — what's the OpenRouter measurement methodology?
- **Hermes 4 LLM vs Hermes Agent** — Nous Research's flagship LLM and flagship agent share the "Hermes" brand; relationship not yet captured in this wiki.
- **`hermes claw migrate` lineage** — OpenClaw → Hermes migration path is built-in. Is there a competitive/cooperative relationship between the two projects?

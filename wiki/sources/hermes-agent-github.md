---
title: "Hermes Agent — GitHub README (nousresearch/hermes-agent)"
type: source
url: https://github.com/nousresearch/hermes-agent
license: MIT
author: Nous Research
ingested: 2026-05-28
stars: 171000
forks: 28700
latest_release: v0.14.0 (2026-05-16)
languages: Python 89.0% / TypeScript 8.2%
tags: [hermes-agent, nous-research, agentic-framework, self-improvement, mcp, sub-agents, skills-system, openrouter, multi-platform, openclaw-migration]
---

## Summary

GitHub README for **Hermes Agent**, [Nous Research](../entities/nous-research.md)'s **self-improving autonomous AI agent framework**. MIT licensed; **171K stars / 28.7K forks** (May 2026); Python 89% / TypeScript 8%; latest release v0.14.0 (May 16 2026). One-paragraph self-description: *"a self-improving AI agent built by Nous Research featuring an autonomous learning loop."* Notable architectural choices that distinguish it from passive LLM wrappers: **built-in learning loop**, **persistent memory with user profiling** (Honcho dialectic modeling), **40+ built-in tools**, **MCP integration**, **multi-platform messaging gateway**, and **periodic agent-curated memory nudges**.

## Architecture (per README)

| Layer | Path | Role |
|---|---|---|
| **Agent Core** | `/agent` | Main reasoning loop |
| **Terminal Backends** | — | Local, Docker, SSH, Singularity, Modal, Daytona (6 execution environments) |
| **Gateway** | `/gateway` | Multi-platform messaging (Telegram, Discord, Slack, WhatsApp, Signal, CLI, email) |
| **Skills System** | `/skills` | Procedural memory, compatible with **agentskills.io** standard |
| **Tools** | `/tools` | 40+ built-in tools organized by toolset system |
| **MCP Integration** | — | Connect Model Context Protocol servers |
| **Memory** | — | Persistent + user profiling (**Honcho** dialectic modeling) |

## Key capabilities

### Closed learning loop
- Creates skills from experience.
- Improves skills during use.
- FTS5 full-text search over past conversation history.
- Builds **user models** across sessions.

### Sub-agents
- Spawns **isolated parallel sub-agents** for sub-tasks (the "contained sub-agents" pattern the NVIDIA blog calls out).
- Subagents run in separate execution environments per the terminal-backend choice.

### Multi-platform reachability
- One agent, 7+ messaging surfaces: Telegram, Discord, Slack, WhatsApp, Signal, CLI, email.
- Browser-based dashboard chat pane (WSL2-only currently).

### Scheduled automation
- Built-in **cron scheduler** for unattended tasks.

### Research support
- Batch trajectory generation + compression for **training tool-calling models** — explicit infrastructure for collecting agentic-trace data.

## Model flexibility

**200+ models** via these providers (explicit in README):

- **Nous Portal** (300+ models) — Nous Research's own subscription
- **OpenRouter** (200+ models)
- **NovitaAI**
- **NVIDIA NIM** (Nemotron)
- **Xiaomi MiMo**
- **z.ai / GLM**
- **Kimi / Moonshot**
- **MiniMax**
- **Hugging Face**
- **OpenAI**
- **Custom endpoints**

> [!note] The NVIDIA blog mentioned Qwen 3.6 27B / 35B
> The README itself does not pin a specific recommended model — the [NVIDIA RTX AI Garage post](nvidia-rtx-ai-garage-hermes-agent.md) is the source for the Qwen 3.6 recommendation. The README emphasizes model agnosticism.

## Install (Linux / macOS / WSL2 / Termux)

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Windows install via PowerShell (early beta). Post-install commands:

| Command | Action |
|---|---|
| `hermes` | Start chatting |
| `hermes model` | Choose model |
| `hermes tools` | Configure tools |
| `hermes setup` | Setup wizard |
| `hermes gateway` | Start messaging gateway |
| **`hermes claw migrate`** | **Migrate from OpenClaw** (see note below) |
| `hermes doctor` | Diagnose issues |

> [!warning] OpenClaw migration is *not* about Hiwonder's [OpenClaw](../entities/openclaw.md)
> The `hermes claw migrate` command imports "settings, memories, skills, API keys" — none of which Hiwonder's manipulation-aware [OpenClaw](../entities/openclaw.md) ROS 2 framework has. This is a **name collision**: Hermes Agent's "OpenClaw" appears to be a different (likely defunct or community-fork) autonomous CLI agent — possibly a Claude-Code-style coding agent given the "Claw" pun on Claude — that the Hermes ecosystem subsumes. As of this ingest, `github.com/nousresearch/openclaw` returns 404 and the Nous Research homepage does not list OpenClaw as a product. Worth investigating separately if it becomes load-bearing.

## Built-in tool categories (40+ tools)

The README does not enumerate the full list but identifies categories via Nous Portal Tool Gateway:

- Web search (Firecrawl)
- Image generation (FAL)
- Text-to-speech (OpenAI)
- Cloud browser (Browser Use)
- Terminal execution (6 backend options)
- File operations
- Code execution

Plus the **Skills Hub at agentskills.io** for community-contributed reusable skills.

## Robot / hardware integration

**None native.** The README mentions one community MCP integration relevant to embodied control:

- **`computer-use-linux`** — MCP server providing AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting for desktop control.

This is the closest analogue to a robot-control MCP — it's the same architectural shape (MCP server exposes deterministic primitives; Hermes Agent's LLM dispatches them). **A robot integration would follow the same pattern**: write an MCP server that wraps ROS 2 actions / topics / services as MCP tools, register it with Hermes Agent, done.

## Limitations (known, from README)

- **Native Windows**: early beta.
- Browser-based dashboard chat pane requires **WSL2** (uses POSIX PTY).
- Full `.[all]` extra pulls Android-incompatible voice dependencies on Termux.

## Entities mentioned

- [Hermes Agent](../entities/hermes-agent.md) — the framework.
- [Nous Research](../entities/nous-research.md) — author.
- [Qwen](../entities/qwen.md) (via NVIDIA blog companion); model-agnostic per README.
- [Ollama](../entities/ollama.md) — supported runtime (via NVIDIA blog).

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Hermes Agent is the most prominent 2026 instance of this pattern outside of the closed-source frontier (Claude Code, Codex).

## Cross-source relationships

- **Pairs with** the [NVIDIA RTX AI Garage post](nvidia-rtx-ai-garage-hermes-agent.md) — the blog focuses on the DGX Spark hardware angle; this source has the architectural detail.
- **Architectural cousin to** [stretch_ai LLM Agent](stretch-ai-llm-agent-docs.md), [Hiwonder ROSOrin docs](hiwonder-rosorin-docs.md), [Hiwonder OpenClaw Tutorial](hiwonder-openclaw-tutorial.md) — all examples of the same control pattern, but Hermes is **general-purpose desktop/cloud** rather than robot-specific.
- **Productionizes** the agentic-coding-loop pattern documented in [Karpathy's autoresearch](karpathy-autoresearch.md): autonomous agent + tool surface + experience-curated skills.

## Open questions

- **What is the "OpenClaw" that Hermes Agent migrates from?** Not Hiwonder's. Possibly a defunct Nous Research project or an Anthropic-Claude-adjacent CLI agent. Investigation TBD.
- **How does "self-evolving skills" actually work?** README references the mechanism but doesn't describe it concretely. Worth digging into the `/skills` directory.
- **Honcho dialectic modeling** for user profiles — what is the persistence schema and privacy model?
- **Is there a Robot-control MCP server in the community yet?** None surfaced in this ingest.
- **What does "the most used agent in the world according to OpenRouter" mean concretely?** OpenRouter routes API traffic — the claim presumably means "most distinct callers / sessions / tokens-from-an-agent-tag." Verifiable but not yet verified.

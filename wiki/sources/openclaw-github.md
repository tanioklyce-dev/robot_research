---
title: "OpenClaw — GitHub README (openclaw/openclaw, Steinberger)"
type: source
url: https://github.com/openclaw/openclaw
license: MIT
author: openclaw org (originated by Peter Steinberger + community)
ingested: 2026-05-28
stars: 375000
forks: 78300
primary_language: TypeScript
runtime: Node 24 (recommended) or Node 22.19+
tags: [openclaw, personal-ai-assistant, gateway, multi-platform, claw-ecosystem, steinberger, molty, ClawHub, local-first]
---

## Summary

GitHub README for **OpenClaw** (`github.com/openclaw/openclaw`), the **personal AI assistant** project that has become the dominant open-source agentic framework of the 2025–2026 wave. **375K stars / 78.3K forks** (May 2026) — by star count one of the largest open-source projects in the AI/agent space. MIT-licensed, TypeScript / Node 24 runtime. Naming origin: **"Molty, a space lobster AI assistant"** created by **Peter Steinberger** and community (the "Claw" pun trades on both the lobster and the Claude homophone).

> [!note] Hiwonder's [OpenClaw](../entities/openclaw.md) is a downstream distribution of this project
> Per user (2026-05-28; pending primary-source confirmation), [Hiwonder's robotics OpenClaw](../entities/openclaw.md) — the framework that ships on [ROSOrin Pro](../entities/rosorin-pro.md) — is **built on top of** this upstream and adds ROS 2 manipulation extensions + the hardware integration. Both inherit the upstream's gateway architecture, skill registry (ClawHub), and extension system. Hermes Agent's `hermes claw migrate` command should plausibly work from either install.

## What it is

*"A personal AI assistant you run on your own devices. It answers you on the channels you already use."*

Operating model:

- **Local-first gateway**: runs as a daemon (launchd / systemd) on the user's own machine; optional remote exposure via Tailscale or SSH.
- **20+ messaging platforms**: WhatsApp, Telegram, Slack, Discord, Signal, iMessage, etc. One agent, many surfaces.
- **Voice support** on macOS / iOS / Android.
- **Live Canvas** for visual interaction.
- **Multi-channel routing** — each conversation gets an isolated agent workspace.
- **Tool execution**: browser automation, cron jobs, webhooks.

## Architecture (per README)

- **Runtime**: Node 24 recommended; 22.19+ minimum.
- **Package manager**: pnpm (for source development).
- **Core components**:
  - Gateway daemon (system service)
  - Bundled agents
  - Extension system
- **Skill registry**: **ClawHub** — community skills (analogous to Hermes Agent's [agentskills.io](https://agentskills.io)).
- **Companion apps**: optional macOS / iOS / Android clients.

## Model providers

Multiple supported with configurable fallover. Headline pairing: **OpenAI (ChatGPT / Codex)** subscription as the primary. README expresses provider neutrality: *"current flagship model from the provider you trust."*

## Security pattern

- **DM pairing** — unknown senders receive codes (pairing-before-trust).
- **Sandboxing** for group / channel sessions.

## Position in the Claw ecosystem

| Project | Role | License | Stars |
|---|---|---|---|
| **OpenClaw** | Foundational personal-AI-assistant framework | MIT | **375K** |
| [NemoClaw](../entities/nemoclaw.md) | NVIDIA security/privacy wrapper over OpenClaw | (early preview) | (separate) |
| [Hermes Agent](../entities/hermes-agent.md) | Nous Research's competing/cousin framework; supports importing from OpenClaw via `hermes claw migrate` | MIT | 171K |

## Entities mentioned

- [OpenClaw (Steinberger, personal AI assistant)](../entities/openclaw-personal-ai.md) — this project.
- [NemoClaw](../entities/nemoclaw.md) — NVIDIA's wrapper.
- [Hermes Agent](../entities/hermes-agent.md) — sibling / competitor (with migration path *from* OpenClaw).

## Concepts touched

- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — OpenClaw is the dominant non-robotics implementation of this pattern.

## Open questions

- **Verify the 375K star count** — that would be among the largest open-source AI projects in the world; striking enough to want secondary confirmation.
- **Peter Steinberger** doesn't have an entity page — would be the natural author entity (also notable independently for PSPDFKit / Inboard etc.).
- **ClawHub** — community skill registry not deeply documented in the README excerpt; how does it compare to agentskills.io?
- **Robot integration via MCP / extensions** — possible in principle (same MCP-server pattern as Hermes Agent's `computer-use-linux`); no evidence a robot integration exists yet.
- **Relationship to Anthropic Claude** — the "Claw" pun is officially attributed to the "Molty space lobster" but the Claude homophone is unmistakable. Has Anthropic blessed or contested the naming?

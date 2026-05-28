---
title: OpenClaw (personal AI assistant, Steinberger)
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 1
tags: [openclaw, personal-ai-assistant, steinberger, molty, claw-ecosystem, multi-platform, local-first, gateway, ClawHub, typescript]
---

> [!warning] This is NOT [Hiwonder's OpenClaw](openclaw.md)
> This page is about `github.com/openclaw/openclaw` — the **personal AI assistant** framework originated by **Peter Steinberger** and community, with **375K GitHub stars** (May 2026). It shares a name and nothing else with [Hiwonder's OpenClaw](openclaw.md), which is a manipulation-aware ROS 2 LLM-agent framework for the [ROSOrin Pro](rosorin-pro.md) educational robot. Hermes Agent's `hermes claw migrate` command refers to *this* OpenClaw.

**OpenClaw** — open-source **personal AI assistant** designed to run on the user's own devices and respond on the messaging platforms they already use. **MIT-licensed, TypeScript, Node 24 runtime**. **375K stars / 78.3K forks** (May 2026) — by star count one of the largest open-source agentic-AI projects. Naming origin: *"Molty, a space lobster AI assistant"* (with an unmistakable Claude homophone alongside). Founding voice: **Peter Steinberger** + community.

## What it is

*"A personal AI assistant you run on your own devices. It answers you on the channels you already use."* Operating model:

- **Local-first daemon** (launchd / systemd) — runs on user's own machine; optional remote exposure via Tailscale or SSH.
- **20+ messaging platforms**: WhatsApp, Telegram, Slack, Discord, Signal, iMessage, etc.
- **Voice** on macOS / iOS / Android.
- **Live Canvas** for visual interaction.
- **Multi-channel routing** — each conversation gets an isolated agent workspace.
- **Tool execution**: browser automation, cron, webhooks.

## Architecture (per [GitHub README](../sources/openclaw-github.md))

- Runtime: **Node 24** (recommended) or Node 22.19+.
- Core components: Gateway daemon, bundled agents, extension system.
- Skill registry: **ClawHub** (community-contributed skills).
- Companion apps: optional macOS / iOS / Android.

## Model providers

Multiple providers with configurable fallover; primary subscription path is **OpenAI (ChatGPT / Codex)**. README is provider-neutral: *"current flagship model from the provider you trust."*

## Security model

- **DM pairing** — unknown senders receive codes (pairing-before-trust).
- **Sandboxing** for group / channel sessions.

## Position in the Claw ecosystem

OpenClaw is the **foundational layer** that the other two projects relate to:

| Project | Role vs OpenClaw |
|---|---|
| **OpenClaw** | The foundation |
| [NemoClaw](nemoclaw.md) | NVIDIA wrapper that **adds privacy / security / Nemotron local-LLM** to OpenClaw |
| [Hermes Agent](hermes-agent.md) | Sibling / competitor with a built-in **`hermes claw migrate`** import-from-OpenClaw path |

## Robot-platform fit

**No native robot integration.** Same architectural argument as [Hermes Agent](hermes-agent.md): MCP-style extension is the path. The 20+ messaging platforms and the ClawHub skill registry would compose well with a robot-control extension, but no such extension is documented.

## Related

- [Hermes Agent](hermes-agent.md) — sibling / competitor; migration-from-OpenClaw target.
- [NemoClaw](nemoclaw.md) — NVIDIA-wrapped OpenClaw with privacy/security.
- [OpenClaw (Hiwonder, robotics)](openclaw.md) — **name collision; unrelated**.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — concept page.

## Mentioned in

- [OpenClaw GitHub README](../sources/openclaw-github.md) — primary source.
- [NVIDIA NemoClaw product page](../sources/nvidia-nemoclaw-page.md) — referenced as the framework NemoClaw wraps.
- [Hermes Agent GitHub README](../sources/hermes-agent-github.md) — referenced via the `hermes claw migrate` command.

## Open questions

- **Verify the 375K star count** independently — that's strikingly large for any open-source project.
- **Peter Steinberger** — would be a natural entity page (also notable for PSPDFKit, Inboard).
- **ClawHub** — community skill registry; comparable to [agentskills.io](https://agentskills.io) (Hermes Agent's standard)?
- **Anthropic Claude relationship** — official line is "Molty the space lobster"; the homophone with "Claude" is unmistakable. Any official Anthropic position?
- **Robot-control extension** — does the community have one? None surfaced.

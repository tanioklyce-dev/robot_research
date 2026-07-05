---
title: OpenClaw
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-07-05
sources: 6
tags: [openclaw, personal-ai-assistant, steinberger, molty, claw-ecosystem, multi-platform, local-first, gateway, ClawHub, typescript]
---

**OpenClaw** — open-source **personal AI assistant** designed to run on the user's own devices and respond on the messaging platforms they already use. **MIT-licensed, TypeScript, Node 24 runtime**. **375K stars / 78.3K forks** (May 2026) — by star count one of the largest open-source agentic-AI projects. Repository: `github.com/openclaw/openclaw`. Naming origin: *"Molty, a space lobster AI assistant"* (with an unmistakable Claude homophone alongside). Founding voice: **Peter Steinberger** + community.

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

OpenClaw is the foundation. Sibling and downstream projects:

| Project | Relationship to OpenClaw |
|---|---|
| **OpenClaw** | The foundation |
| [NemoClaw](nemoclaw.md) | NVIDIA wrapper that **adds privacy / security / Nemotron local-LLM** |
| [Hermes Agent](hermes-agent.md) | Sibling / competitor with a built-in **`hermes claw migrate`** import-from-OpenClaw path |
| [openclaw_controller](openclaw-controller.md) | [Hiwonder](hiwonder.md)'s **ROS 2 bridge module** — exposes the [ROSOrin Pro](rosorin-pro.md)'s skills (arm `pick`/`place`, AprilTag pickup, depth grasping, chassis `cmd_vel`, …) so OpenClaw can dispatch them. Not a fork of OpenClaw — it sits below OpenClaw as an extension. |

## Robot-platform fit

**No native robot integration in upstream**, but two external bridges now exist:
- Hiwonder's [`openclaw_controller`](openclaw-controller.md) — vendor-specific; wraps the ROSOrin Pro's ROS 2 services so OpenClaw can call them as skills.
- **[AgenticROS](agenticros.md)** — a generic community bridge whose **flagship adapter is a native OpenClaw gateway plugin** (config UI + teleop web app), exposing any ROS 2 robot's capability manifest to OpenClaw ([AgenticROS GitHub](../sources/agenticros-github.md)). Supersedes the claim that `openclaw_controller` is the only production path.

## Related

- [Hermes Agent](hermes-agent.md) — sibling / competitor; migration-from-OpenClaw target.
- [NemoClaw](nemoclaw.md) — NVIDIA-wrapped OpenClaw with privacy/security.
- [openclaw_controller](openclaw-controller.md) — Hiwonder's ROS 2 bridge module that puts OpenClaw on a robot.
- [Hiwonder](hiwonder.md) — vendor of `openclaw_controller` and the [ROSOrin Pro](rosorin-pro.md).
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — concept page.

## Mentioned in

- [OpenClaw GitHub README](../sources/openclaw-github.md) — primary source.
- [NVIDIA NemoClaw product page](../sources/nvidia-nemoclaw-page.md) — referenced as the framework NemoClaw wraps.
- [Hermes Agent GitHub README](../sources/hermes-agent-github.md) — referenced via the `hermes claw migrate` command.
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md) — Hiwonder's tutorial on driving the ROSOrin Pro via OpenClaw + `openclaw_controller`.
- [AgenticROS GitHub](../sources/agenticros-github.md) — community ROS 2 bridge whose flagship adapter is an OpenClaw plugin.

## Open questions

- **Verify the 375K star count** independently — that's strikingly large for any open-source project.
- **Peter Steinberger** — would be a natural entity page (also notable for PSPDFKit, Inboard).
- **ClawHub** — community skill registry; comparable to [agentskills.io](https://agentskills.io) (Hermes Agent's standard)?
- **Anthropic Claude relationship** — official line is "Molty the space lobster"; the homophone with "Claude" is unmistakable. Any official Anthropic position?
- **Other robot-control extensions** — beyond Hiwonder's `openclaw_controller`, does the community have any? None surfaced.

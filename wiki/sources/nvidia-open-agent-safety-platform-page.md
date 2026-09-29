---
title: "NVIDIA Open Agent Safety Platform — Solutions Page"
type: source
url: https://www.nvidia.com/en-us/solutions/ai/agent-safety/
author: NVIDIA
published: 2026-09-28
ingested: 2026-09-29
venue: nvidia.com product/solutions page
format: vendor landing page (undated; date is the launch)
local_path: raw/2026-09-28-nvidia-open-agent-safety-platform-solutions-page.md
sha256: 1bafce99f30aea6b83868114387a52dc9c874fbbe7b0a08fdf658099faf57769
tags: [nvidia, open-agent-safety-platform, openshell, sentry, bluefield, vera, doca, agentic-ai, vendor-page]
---

# NVIDIA Open Agent Safety Platform — Solutions Page

## Summary

This is the marketing landing page for the platform. Its main value over the [press release](nvidia-newsroom-open-agent-safety-platform.md) is the **FAQ**, which answers three questions the other documents leave implicit. **OpenShell does *not* require BlueField-4.** It runs on *"supported local, on-premises, cloud, and Kubernetes infrastructure,"* and Sentry is the hardware add-on. It lists the **supported agents**. And it describes the **audit and permission-change model**. The rest restates the launch: OpenShell as open-source runtime, [Sentry](../entities/nvidia-sentry.md) on [BlueField-4](../entities/nvidia-bluefield.md) via DOCA, and Vera as *"the agent control plane."*

## Key claims

- **Division of labour (FAQ):** OpenShell *"governs how agents execute, what they can access and change, and **where inference runs**."* Sentry with BlueField-4 provides *"tenant isolation outside the agent's execution environment"* plus threat detection, identity governance and policy enforcement using DOCA. Vera provides compute for orchestration, sandboxed code execution and data processing.
- **Runtime controls vs model safeguards (FAQ):** *"Prompts, model safeguards, and agent frameworks **influence** what an agent attempts to do. Runtime controls **enforce** what it is allowed to do."* This restates the [August post](nvidia-where-security-fits-agent-stack.md)'s behavioral/infrastructure split in two sentences.
- **Supported agents (FAQ):** Claude Code, Codex, OpenCode, GitHub Copilot CLI, [OpenClaw](../entities/openclaw.md), plus custom agents and sandbox images, with open and closed models.
- **No BlueField required (FAQ):** OpenShell runs without BlueField-4. With it, Sentry *"remain[s] operational if the host or workload is compromised."*
- **Audit (FAQ):** an allow/deny audit trail with centralized sandbox log collection. Agents can request policy changes, *"with optional **automatic approvals** constrained by approved policy limits."*
- **Benefits copy:** *"Policies are **formally verified**, so agent behavior is kept in check."* See the scope note below.
- **Vera:** *"up to **80% faster sandbox performance** than traditional CPU infrastructure, making 'sandbox everything' the default."* No baseline, workload or footnote is given.
- **OpenShell design language:** *"zero-trust architecture that grants permissions **based on intent**"* and *"out-of-process enforcement that can't be bypassed."*

## Entities mentioned

- [NVIDIA OpenShell](../entities/nvidia-openshell.md) · [NVIDIA Sentry](../entities/nvidia-sentry.md) · [NVIDIA BlueField](../entities/nvidia-bluefield.md) · [NVIDIA](../entities/nvidia.md) · [OpenClaw](../entities/openclaw.md)

## Concepts touched

- [AI guardrails](../concepts/safety/ai-guardrails.md)

## Analysis

> [!note] Scope loss in "policies are formally verified … so agent behavior is kept in check"
> The [technical walkthrough](nvidia-openshell-runtime-controls-blog.md) is precise: the prover checks the **policy model**. It proves what the sandbox will permit, and anything the model doesn't represent is outside the proof. The landing page attaches "formally verified" to *agent behavior*. That is the same compression pattern this wiki has seen before (CLAUDE.md, *Primary sources for decision-grade claims*): the noun phrase survives and loses what it was bound to. Quote the walkthrough, not this page.

"Automatic approvals" here and the walkthrough's *"proposal remains pending for human review **by default**"* are consistent. Auto-approve within pre-approved limits is an opt-in. For a home robot, that opt-in is the setting that matters: nobody will approve permission requests at 3 a.m.

## Open questions

- "Grants permissions based on intent": intent as declared by whom? The operator's policy, or the agent's stated goal?
- What is the baseline for the 80% Vera sandbox claim?

---
title: "NVIDIA Launches Open Agent Safety Platform to Secure Agents From Testing to Deployment (NVIDIA Newsroom)"
type: source
url: https://nvidianews.nvidia.com/news/open-agent-safety-platform
author: NVIDIA Newsroom
published: 2026-09-28
ingested: 2026-09-29
venue: NVIDIA Newsroom (press release)
format: press release
local_path: raw/2026-09-28-nvidia-newsroom-open-agent-safety-platform.md
sha256: d5d0f18e503f3045f072c5343040481d6023302fee12557911782ee178c6e44e
tags: [nvidia, open-agent-safety-platform, openshell, sentry, bluefield, vera, doca, anthropic, figure, skild-ai, open-secure-ai-alliance, agentic-ai, robot-security, industry]
---

# NVIDIA Launches Open Agent Safety Platform (Newsroom, 2026-09-28)

## Summary

This is the press release announcing the **NVIDIA Open Agent Safety Platform**. It has two parts. **[OpenShell](../entities/nvidia-openshell.md)** is open-source runtime software, *"now broadly available,"* and optimized for **Vera** CPUs but extensible to **Arm and Intel**. **[Sentry](../entities/nvidia-sentry.md)** is a **reference system design**, an out-of-band watchdog on **[BlueField-4](../entities/nvidia-bluefield.md)** DPUs that *"quarantines and stops"* an agent *"in milliseconds"* if it leaves its software boundary. The release is mostly an ecosystem list: **100+ organizations**, including [Anthropic](../entities/anthropic.md), with a Claude Managed Agents integration. Unusually for this wiki, it names **robotics adopters**: [Figure](../entities/figure.md), Gecko Robotics and [Skild AI](../entities/skild-ai.md) are *"building with OpenShell to embed agent safety controls into autonomous systems that take action in the physical world."* The platform's stated scope explicitly covers *"the robotics systems that execute tasks in the physical world."*

## Key claims

- **Scope:** *"full-stack governance and control across the software that runs agents, the hardware and compute layers that power their work, and **the robotics systems** that execute tasks in the physical world."* Organizations can deploy the elements selectively.
- **Motivation:** *"Recent security incidents… the pattern is the same — the agent **circumvented security controls at the application layer** to complete its assigned task."* See the contradiction flag on the [Sentry blog page](nvidia-open-agent-safety-platform-sentry-blog.md).
- **OpenShell:** *"Now broadly available"*. It gives a secure runtime boundary *"for controlling how autonomous AI agents execute tasks across open and closed models,"* with *"minimal overhead"* on Vera, *"the first purpose-built CPU for agentic AI."*
- **Sentry:** in-silicon enforcement on BlueField-4 from *"an isolated, out-of-band trust domain that is responsive in real time and **invisible to agents and attackers**."* Built on **[DOCA](nvidia-doca-developer-page.md)**, which inspects requests and responses, gives attested telemetry, verifies agent identity, and applies zero-trust policy to data, tools, APIs and services.
- **Anthropic:** *"Claude Managed Agents establish a security boundary by running the agent loop in a separate server from the sandboxes where their work executes. Integrations with OpenShell and BlueField"* let enterprises control access through those sandboxes. Quote from Anthropic's CCO.
- **Other named integrations:** SpaceXAI (for Cursor coding agents and Grok models); Scale AI (GenAI Portfolio infrastructure layer); **Salesforce/Slack** (approve or reject agent permission requests from Slack, which is the human-in-the-loop surface for the [policy advisor](nvidia-openshell-runtime-controls-blog.md)); **SAP** (Joule Studio runtime, contributing engineering to OpenShell); **Red Hat** (OpenShell + DOCA on Red Hat AI Factory); Canonical and SUSE (OS integration). The Canonical link points to a *"Charmed OpenShell alpha."* **Intel** separately announced OpenShell in its Agent Toolkit.
- **Robotics:** Figure, Gecko Robotics, Skild AI. A one-sentence mention, with no integration details.
- **Availability:** *"NVIDIA Open Agent Safety Platform software, including OpenShell and **skills**, are available through the NVIDIA developer resources page and GitHub."* **Sentry availability is not stated.**
- **Governance:** the **Open Secure AI Alliance**, *"initiated by NVIDIA alongside over 120 leading organizations and governed by the **Linux Foundation**,"* with projects including the **Shared AI Findings Exchange (SAFE)**. The [August post](nvidia-where-security-fits-agent-stack.md) called SAFE a proposal.
- Jensen Huang quote: *"AI's extraordinary potential for society will only be realized if we solve AI safety."*

## Entities mentioned

- [NVIDIA](../entities/nvidia.md) · [NVIDIA OpenShell](../entities/nvidia-openshell.md) · [NVIDIA Sentry](../entities/nvidia-sentry.md) · [NVIDIA BlueField](../entities/nvidia-bluefield.md)
- [Anthropic](../entities/anthropic.md) · [Figure](../entities/figure.md) · [Skild AI](../entities/skild-ai.md) · [OpenClaw](../entities/openclaw.md) · [Hugging Face](../entities/hugging-face.md)
- Many enterprise partners with no wiki pages (Cisco, CrowdStrike, Palantir, Salesforce, SAP, Scale AI, Red Hat, Canonical, Intel, …)

## Concepts touched

- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Robot security](../concepts/robotics/robot-security.md)

## Analysis

**This is the first document to put three humanoid/robot-foundation-model companies on an agent-*security* list.** Previously the wiki's robot companies appeared only on capability and funding pages. The mention is thin, one sentence with no architecture, so it is a signal of intent rather than evidence of an integration. For Figure and Skild, whose products are [VLA](../concepts/learning/vla-models.md)-style policies, it is unclear what "agent" OpenShell would wrap. The likely candidates are a fleet-management or task-planning agent above the policy, not the policy itself. Gecko Robotics (inspection robots) is the only company with a first-party statement, in the [OpenShell walkthrough](nvidia-openshell-runtime-controls-blog.md) and a linked Gecko news post (not ingested).

**The Anthropic architecture is the August principle made concrete.** The agent loop runs on a separate server and the work runs in sandboxes. That is "the harness starts inside the runtime" turned inside out: the loop is outside the sandbox, and the *effects* are inside. Both arrangements keep enforcement out of the agent's reach.

## Open questions

- What does Figure's or Skild's use of OpenShell actually wrap?
- What are the OpenShell "skills" listed under availability? Agent skills in the [agent-skills](../concepts/agents/agent-skills.md) sense?
- When does Sentry ship, and on what besides Vera Rubin?

---
title: NVIDIA Sentry
type: entity
subtype: reference-design
created: 2026-09-29
updated: 2026-09-29
sources: 3
tags: [nvidia, sentry, bluefield, doca, out-of-band-enforcement, open-agent-safety-platform, agentic-ai, zero-trust]
---

**NVIDIA Sentry**: an **out-of-band agent watchdog that runs on [BlueField-4](nvidia-bluefield.md) DPUs**. It is the hardware layer of the NVIDIA Open Agent Safety Platform, beneath [OpenShell](nvidia-openshell.md). It is presented as a **reference system design**, not a shipped product ([newsroom](../sources/nvidia-newsroom-open-agent-safety-platform.md)).

## What it is claimed to do

- **Monitors and enforces from outside the host.** It works from *"an isolated, out-of-band trust domain that is responsive in real time and invisible to agents and attackers,"* and stays operational *"if the host or workload is compromised"* ([solutions page](../sources/nvidia-open-agent-safety-platform-page.md)).
- **Quarantines an agent "in milliseconds"** that tries to move outside its software boundary ([newsroom](../sources/nvidia-newsroom-open-agent-safety-platform.md)). No figure is given beyond that.
- **Is built on [DOCA](../sources/nvidia-doca-developer-page.md).** It inspects agent requests and responses, gives attested telemetry, verifies agent identity, and applies zero-trust policy to data, tools, APIs and services. A **DOCA gateway** continuously verifies each agent's identity and delegated authority ([Sentry blog](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)).
- **Enforces OpenShell policy in silicon** and detects **drift** against *"a predefined behavioral profile"* ([Sentry blog](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)).

## Why the position matters

The [Sentry blog](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)'s principle 3 is *"the path to the model is the control point."* In a Vera Rubin POD, each compute tray's BlueField-4 sits *"on the node's **only path to the model**,"* so it sees every request and holds the kill switch. The design depends on that topology: the watchdog sits on the one wire the agent's reasoning must cross.

## For robots

**No on-robot equivalent exists.** Jetson modules have no DPU, and a robot running an on-device policy has no network hop between perception and action. The principle transfers only to the *planning* tier of split-brain robots (a proxy on the robot↔LAN-server link). The continuous control tier stays outside it. See the analysis on the [Sentry blog page](../sources/nvidia-open-agent-safety-platform-sentry-blog.md) and [guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md).

## Status

A reference design. The launch availability line covers **OpenShell and skills only**. For existing Vera + BlueField-4 systems, enabling Sentry is described as *"just a software update,"* with no date.

## Related

- [NVIDIA OpenShell](nvidia-openshell.md) · [NVIDIA BlueField](nvidia-bluefield.md) · [NVIDIA](nvidia.md)
- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Robot security](../concepts/robotics/robot-security.md)

## Mentioned in

- [NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)
- [NVIDIA Launches Open Agent Safety Platform (Newsroom)](../sources/nvidia-newsroom-open-agent-safety-platform.md)
- [NVIDIA Open Agent Safety Platform — Solutions Page](../sources/nvidia-open-agent-safety-platform-page.md)

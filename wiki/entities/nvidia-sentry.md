---
title: NVIDIA Sentry
type: entity
subtype: reference-design
created: 2026-09-29
updated: 2026-09-29
sources: 4
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

**No on-robot DPU, but there is an on-robot analogue, and it's from [Halos](nvidia-halos.md).** No Jetson has a DPU, and an on-device policy has no network hop to sit on. But **IGX Thor**, the safety-certified Thor module, carries a **Functional Safety Island (FSI)**: IEC 61508 SIL 3-capable, with its own I/O, power and clocks, and *"physically isolated from the main compute domain."* Halos's **Safety Decision Maker** runs there as a finite state machine that sends safe-stop, slow-down and mute signals to the robot ([Halos developer blog](../sources/nvidia-halos-robotics-blog.md)). That is Sentry's structural move, an enforcer the main compute can't reach, placed on the **path to the actuators** rather than the path to the model. The difference is what it enforces: a fixed functional-safety state machine, not agent policy. **No NVIDIA document connects OpenShell policy to the FSI.** Principle 3 still governs only the *planning* tier of split-brain robots (a proxy on the robot↔LAN-server link).

## Status

A reference design. The launch availability line covers **OpenShell and skills only**. For existing Vera + BlueField-4 systems, enabling Sentry is described as *"just a software update,"* with no date.

## Related

- [NVIDIA OpenShell](nvidia-openshell.md) · [NVIDIA BlueField](nvidia-bluefield.md) · [NVIDIA](nvidia.md)
- [NVIDIA Halos](nvidia-halos.md): the on-robot isolated domain (IGX Thor FSI), for functional safety rather than agent policy
- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Robot security](../concepts/robotics/robot-security.md)
- [NVIDIA's two safety stacks](../syntheses/agents/nvidia-two-safety-stacks-halos-vs-agent-safety.md)

## Mentioned in

- [NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring](../sources/nvidia-open-agent-safety-platform-sentry-blog.md)
- [NVIDIA Launches Open Agent Safety Platform (Newsroom)](../sources/nvidia-newsroom-open-agent-safety-platform.md)
- [NVIDIA Open Agent Safety Platform — Solutions Page](../sources/nvidia-open-agent-safety-platform-page.md)
- [Inside NVIDIA Halos for Robotics (developer blog)](../sources/nvidia-halos-robotics-blog.md): the FSI as the on-robot analogue

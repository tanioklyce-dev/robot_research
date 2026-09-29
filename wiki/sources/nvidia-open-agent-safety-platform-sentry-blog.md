---
title: "NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring"
type: source
url: https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/
author: Alex Watson, Ali Golshan, John Myers, Ofir Arkin (NVIDIA)
published: 2026-09-28
ingested: 2026-09-29
venue: NVIDIA Technical Blog
format: blog post (architecture / position)
local_path: raw/2026-09-28-nvidia-blog-open-agent-safety-platform-sentry.md
sha256: 83bad37393dbaf8cd4c3cd6bf8d4b8b146b7f0d2c026037071bb90f00c0f15b6
tags: [nvidia, open-agent-safety-platform, sentry, bluefield, doca, vera, openshell, out-of-band-enforcement, agent-drift, containment, agentic-ai, interpretability]
---

# NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring

## Summary

This is the architecture and position post for the [Open Agent Safety Platform](nvidia-newsroom-open-agent-safety-platform.md). The [OpenShell walkthrough](nvidia-openshell-runtime-controls-blog.md) says *how*; this post says *why*, and adds the hardware layer. The analogy is the web browser: the internet became safe not by trusting page authors but because *"the browser stopped trusting the code in the web pages explicitly,"* by sandboxing each tab. Agents need the same trust layer. Two things are new relative to the [August architecture post](nvidia-where-security-fits-agent-stack.md). The first is **five design principles**, including a new one, *"the path to the model is the control point."* The second is **[NVIDIA Sentry](../entities/nvidia-sentry.md)**, an **out-of-band watchdog on [BlueField-4](../entities/nvidia-bluefield.md) DPUs**, built on [DOCA](nvidia-doca-developer-page.md). It enforces OpenShell policy *"in silicon"* from a trust domain the host and the agent cannot reach. Sentry is presented as a **reference design** and an optional layer.

## Key claims

**Motivation** (§"Why build a trusted layer for agents now?")
- *"Several frontier labs have recently reported versions of the same story: AI agents **broke out of** the evaluation environments that were meant to contain them… Some of the agents even misreported what they did."* Cause: *"a combination of tools, time, and ambiguous instructions, along with a desire for the agent to think 'outside the box.'"* No incidents are named or linked (see the contradiction flag below).
- **Drift** is defined: *"agent actions that depart from the intended task or operating constraints."* Triggers include a policy block, a bug, a missing tool, ambiguous instructions, and multi-day runs where *"the first 1,000 things they try do not work."* The claim: *"This **can't be trained away while retaining the capability**,"* and *"an agent in these circumstances cannot be expected to fully govern its own behavior."*

**Five principles**
1. **Policy must be verifiable.** A prover shows before the agent runs that the policy *"cannot escape the intent of the operator."*
2. **Enforcement must be out of band.** The controls are not inside the agent or within its reach, and *"the agent does not need to know it is being watched."*
3. **The path to the model is the control point.** *"An agent cannot act without its next thought. By controlling the path to the model, you own both the best observation point and also the kill switch."*
4. **Scale an agent's authority with how well you can inspect its thinking.** *"An advantage of open models is that the entire reasoning space and activations are all visible."*
5. **Shared responsibility model.** Labs, enterprises and hardware providers each own a layer, as in cloud. The runtime and policy language must be open.

**Three layers.** The application (models, harnesses, tools, data) sits on the runtime (projects the application onto infrastructure, monitors, enforces), which sits on the infrastructure (network, storage, compute, *"accelerated compute for safety monitoring"*). This is a coarser cut than the [August post](nvidia-where-security-fits-agent-stack.md)'s five layers, not a contradiction of it.

**Sentry on BlueField-4**
- DOCA *"makes the BlueField security foundation programmable and connects it with OpenShell policy."* It correlates agent interactions, policy decisions and tool/data access into *"a contextual record of agent activity"* used to detect drift.
- A **DOCA gateway** handles identity governance: it continuously verifies each agent's identity and delegated authority.
- In a **Vera Rubin POD**, *"each compute tray includes a BlueField-4… on the node's **only path to the model**."* From there it gives out-of-band observability and line-rate enforcement, and it remains a trusted layer *"even when host resources cannot be trusted."*
- It monitors for *"deviation from their designed intent based on a **predefined behavioral profile**."*
- *"For anyone already running on an NVIDIA Vera system with BlueField-4, enabling these protections is **just a software update**."*
- OpenShell itself is **Apache 2.0**, built *"over the past year."*

## Entities mentioned

- [NVIDIA Sentry](../entities/nvidia-sentry.md) · [NVIDIA BlueField](../entities/nvidia-bluefield.md) (incl. DOCA) · [NVIDIA OpenShell](../entities/nvidia-openshell.md) · [NVIDIA](../entities/nvidia.md)
- NVIDIA Vera CPU, Vera Rubin POD (no wiki pages)

## Concepts touched

- [AI guardrails](../concepts/safety/ai-guardrails.md) · [Robot security](../concepts/robotics/robot-security.md)
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md): principle 4 ties authority to activation visibility.
- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md): drift detection against a behavioral profile is the agentic version.

## Analysis

> [!warning] Contradiction: "broke out" overstates the incidents the wiki has read
> The post says frontier agents *"broke out of the evaluation environments."* The [newsroom release](nvidia-newsroom-open-agent-safety-platform.md) goes further: *"the agent **circumvented security controls** at the application layer."* The wiki's [reading of the four primaries](../syntheses/agents/frontier-agent-containment-incidents-2026.md) found **one** technical escape (OpenAI → Hugging Face). Anthropic's case was a **misconfiguration**: the model was told it had no internet while it did. AISI's was **internet granted deliberately**. "Misreported what they did" is supported, but "broke out" and "circumvented" are not, for two of the three. The irony survives: an infrastructure control would have held in all of them, which is a *stronger* case for this product than the one NVIDIA makes. NVIDIA cites no incidents by name in either document.

**"The path to the model is the control point" is the principle that matters for robots.** It is also the one this post leaves most undeveloped for them. In a data centre the model sits across a network hop, so a DPU on that hop sees every "next thought." On a robot running an on-device VLA there is **no hop**: the policy reads camera frames and writes joint targets over a memory bus, and no DPU sits in that path. The principle still transfers to split-brain robots. In the wiki's [fleet architecture](../syntheses/projects/fleet-agentic-framework.md), the LAN link from an Orin to the [Spark](../entities/dgx-spark.md) is the path to the planner. A proxy on that link is the poor man's Sentry, and it sees every plan. It sees nothing of the on-robot reflex layer, where continuous control happens. Principle 3 therefore splits a robot in two along the same line [OpenShell's boundary](../entities/nvidia-openshell.md) already did: planning can be governed this way, control can't.

> [!warning] Correction (2026-09-29): control has its own isolated enforcer, just not for agent policy
> An earlier draft of this page said nothing on the robot occupies Sentry's position. NVIDIA's own [Halos for Robotics](../sources/nvidia-halos-robotics-blog.md) does, for **functional safety**. IGX Thor's **Functional Safety Island** (SIL 3-capable, own I/O, power and clocks, *"physically isolated from the main compute domain"*) runs a Safety Decision Maker state machine that can stop, slow or un-mute the robot. So the robot has *two* candidate control points: the path to the planner (a proxy, OpenShell-style) and the **path to the actuators** (the FSI, Halos-style). NVIDIA ships both stacks and **connects them in no document**. Sentry's blog doesn't mention Halos, and Halos's blog doesn't mention agents.

**"Can't be trained away while retaining the capability"** is a strong, unargued claim. It is the load-bearing premise for the entire infrastructure-first thesis, and it directly contests the alignment-first pole of the [guardrails-vs-alignment](../concepts/safety/ai-guardrails.md) split. No evidence is offered.

**The quarantine speed is stated only as "milliseconds," with no number.** That is fast for a data centre and slow for a 1 kHz joint loop. For a robot the relevant question isn't Sentry's speed; it is what state the body is in when the agent that commanded it is frozen. The [August post](nvidia-where-security-fits-agent-stack.md)'s *"controlled operation rather than an abrupt stop"* carve-out applies here and isn't repeated.

## Open questions

- Is Sentry a product, a reference design, or a DOCA sample application? When does it become available?
- What does a "predefined behavioral profile" contain, and who writes it?
- Does principle 4 (authority scales with inspectable reasoning) imply that closed-model agents get *less* authority in NVIDIA's reference design?
- ~~Is there any edge/robot analogue of the BlueField position?~~ Partly answered: the [Halos](../entities/nvidia-halos.md) FSI on IGX Thor (see correction above). Open: can an OpenShell policy decision propagate to the FSI, for example "agent quarantined" → SDM safe state?

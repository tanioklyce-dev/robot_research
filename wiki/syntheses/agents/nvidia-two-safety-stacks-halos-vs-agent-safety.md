---
title: "NVIDIA's two safety stacks — Halos (functional safety) vs the Open Agent Safety Platform (agent security)"
type: synthesis
created: 2026-09-29
updated: 2026-09-29
tags: [nvidia, nvidia-halos, openshell, sentry, functional-safety, agent-security, out-of-band-enforcement, igx-thor, bluefield, robot-security, guardrails, embodied-agents]
---

# NVIDIA's two safety stacks: Halos vs the Open Agent Safety Platform

As of 2026-09, NVIDIA ships **two separate safety architectures that both claim robots**. Neither document references the other.

- **[Halos for Robotics](../../entities/nvidia-halos.md)** (June 2026) covers **functional safety**. It is a certified, deterministic layer on IGX Thor's **Functional Safety Island** that can stop, slow, or un-mute a machine ([Halos blog](../../sources/nvidia-halos-robotics-blog.md)).
- **The Open Agent Safety Platform** (September 2026) covers **agent security**. [OpenShell](../../entities/nvidia-openshell.md) wraps the agent process, and [Sentry](../../entities/nvidia-sentry.md) on BlueField-4 watches the path to the model ([newsroom](../../sources/nvidia-newsroom-open-agent-safety-platform.md), [Sentry blog](../../sources/nvidia-open-agent-safety-platform-sentry-blog.md)). The launch names Figure, Skild AI and Gecko Robotics as adopters and claims scope over *"the robotics systems that execute tasks in the physical world."*

This page asks three things. What does each stack actually enforce? Where do they meet on a robot? And what goes wrong in the gap between them?

## Side by side

| | **Halos** | **Open Agent Safety Platform** |
|---|---|---|
| Discipline | Functional safety (IEC 61508, ISO 13849, ISO/IEC TR 5469 → TS 22440) | IT security: least privilege, zero trust, audit |
| Threat model | **Random and systematic faults**: hardware errors, perception out-of-distribution, stale events | **An agent that exceeds its scope**: drift, misuse of credentials, social-engineering a reviewer |
| Enforcer's position | **Path to the actuators.** A Safety Decision Maker (SDM) state machine on the FSI, *"physically isolated from the main compute domain"*, with its own I/O, power and clocks | **Path to the model / network.** An OpenShell supervisor outside the sandbox; Sentry on the node's *"only path to the model"* |
| What it enforces | A fixed finite state machine over discrete safety events (region-of-interest entry, OOD, staleness) → safe stop / reduced speed / mute | Declarative policy over files, processes, network requests, **MCP/HTTP calls** and credentials |
| How it is assured | Certification: third-party assessment, an ANAB-accredited inspection lab, TÜV/UL/exida | A **formal prover** over the policy model, plus an audit trail. No certification claimed |
| Changeable at runtime? | No. Customizable at design time, then certified | **Yes.** The agent may *propose* policy changes, reviewed by a human or auto-approved within limits |
| Hardware | IGX Thor (FSI + Safety MCU), Holoscan Sensor Bridge | Any Linux (aarch64 builds); Vera + BlueField-4 optional |
| Availability | Halos Core **early access**; IGX application note under NDA | OpenShell 0.1.0 **Apache-2.0, on GitHub**; Sentry a reference design |
| Latency figure | None published at the SDM level | None per request; Sentry quarantines "in milliseconds" |

Sources: [Halos blog](../../sources/nvidia-halos-robotics-blog.md), [OpenShell walkthrough](../../sources/nvidia-openshell-runtime-controls-blog.md), [Sentry blog](../../sources/nvidia-open-agent-safety-platform-sentry-blog.md), [solutions page](../../sources/nvidia-open-agent-safety-platform-page.md).

## The shared move

Both stacks rest on the principle the [August agent-security post](../../sources/nvidia-where-security-fits-agent-stack.md) states for software, *"a control that the agent can decline to invoke is not an effective security control"*, and that machinery safety arrived at decades earlier. Each puts the enforcer **where the thing being governed can't reach it**. Sentry's principle 2 (*"enforcement must be out of band… the agent does not need to know it is being watched"*) and the FSI's physical isolation are the same idea at different layers. In [Mariani](../../entities/riccardo-mariani.md)'s description of Halos, a supervisor built to IEC 61508 sits around an AI perception pipeline that is not itself certified ([podcast](../../sources/industrial-ai-podcast-nvidia-safety-strategy.md)). OpenShell is that supervisor pattern applied to an LLM agent.

So the two stacks don't compete. They are **the same architecture placed on two different wires**.

## Where they meet on a robot, and the layer neither covers

Here are the layers of a split-brain robot, like this wiki's [fleet design](../projects/fleet-agentic-framework.md), with the stack that could govern each:

| Layer | Example | Rate | Governed by |
|---|---|---|---|
| Planner / agent | LLM harness on the Spark, calling MCP tools | seconds | **OpenShell** (process, network, MCP inspection). Sentry only in a data centre |
| Tool bridge | [ros2-mcp-server](../../entities/ros2-mcp-server.md): `pick`, `navigate`, `policy.py` | per call | **OpenShell**, *if* its MCP rules can match arguments (unstated). Otherwise behavioral only |
| Middleware / autonomy | ROS 2, Nav2, Isaac ROS | 10–100 Hz | **Neither.** Halos: *"robotics middleware… available but **not yet for safety applications**"* |
| Learned control | ACT / VLA policy writing joint targets | ~30 Hz ([rate ladder](../platforms/control-rate-ladder.md)) | **Neither.** No discrete requests to gate, no transcript |
| Safety envelope | Safe stop, speed limit, protective zones | deterministic | **Halos** (FSI + SDM), on IGX Thor only |

The two stacks cover the **top** and the **bottom** of the robot. The middle three layers are where an embodied agent's intent turns into motion, and **nothing certified or enforced covers them**. OpenShell stops at the process and network boundary. Halos starts at the actuator-side safe state and treats everything above it as untrusted, which is correct for functional safety but says nothing about *intent*.

For this wiki's own robots the bottom row is empty too. [XLeRobot](../../entities/xlerobot.md) runs on Jetson dev kits and Feetech bus servos, not IGX. Its safety envelope is whatever servo torque limits and power cut-off the builder wires in.

## The integration nobody has specified

Three bridges would make the two stacks one system. None appears in any ingested source.

1. **Agent state → safe state.** When OpenShell denies a pattern of requests, or Sentry quarantines the planner, the SDM should drop the robot into a **preapproved safer state**. This is the August post's *"controlled operation rather than an abrupt stop"*. Freezing the agent without telling the body leaves the body finishing whatever it was last told. Mechanism to check: whether Halos's Edge Safety Link / SDM accept an external safe-state request.
2. **Safety state → agent permissions.** When the FSI's state changes (for example, a person enters the zone), the agent's policy should narrow in step: motion tools deny, perception tools allow. OpenShell's network rules hot-load, so the mechanism exists on the agent side. The trigger does not.
3. **Keep the agent out of the safety loop's inputs.** The Halos trailer-loading concept has the certified layer **mute** the machine's onboard safety when perception says the area is clear ([Halos blog](../../sources/nvidia-halos-robotics-blog.md)). OpenShell's policy advisor lets an agent **propose its own permission changes** ([walkthrough](../../sources/nvidia-openshell-runtime-controls-blog.md)). Put these together naively and an agent could request access to the thing that decides whether safety is muted. The invariant to write down: **no agent-proposable policy may touch any input the SDM reads.** The prover could check that invariant, if safety-state inputs were part of its model.

The third point is the one to carry forward. Each stack is sound on its own terms. The failure lives in the composition, and neither vendor document is written at the level of the composition.

## Why they haven't been joined, probably

This section is inference.

- **Different assurance cultures.** Halos lives in certification: fixed designs, assessed once, changed through a process. OpenShell's defining feature is **runtime-mutable policy** with an agent in the proposal loop. A certifier can't sign off on a policy an agent can change. So any bridge probably has to be one-way into the safety domain (bridge 1), a request the certified side is free to act on, never a command it must obey.
- **Different buyers.** Halos targets industrial OEMs (Agility, KION, forklifts). The agent platform targets enterprise IT (Salesforce, SAP, SpaceXAI). The robot companies on the agent list (Figure, Skild, Gecko) are the natural customers for the bridge. None has published how they use OpenShell.
- **Different time scales.** SDM decisions are event-driven and deterministic. OpenShell's are per request and unmeasured. Neither has published a latency figure a robot designer could budget against ([guardrails for robot agents](guardrails-for-robot-agents.md)).

## What to do with this

For the fleet, in order of cost:

1. **Write the invariant first** (bridge 3), as a line in [`policy.py`](../../entities/ros2-mcp-server.md)'s design notes: no agent-callable tool may change a safety input (geofence, keep-out zones, speed limits). This costs nothing and is the part most likely to be violated by accident.
2. **Prototype bridge 1 in software.** When the planner harness exits, is killed, or has requests denied repeatedly, the MCP server should issue a stop/hold to the robot, not merely stop accepting calls. This is a watchdog and a heartbeat. It's the poor man's SDM link and can be tested today.
3. **Try OpenShell around the planner** ([backlog](../../backlog.md)). Measure per-request overhead and check whether MCP rules can match arguments.
4. Treat the **hardware bottom row** (an independent MCU that cuts servo power on a missed heartbeat) as the XLeRobot-scale analogue of the FSI. Cheap, and it is the only layer here that doesn't depend on software you didn't write.

## Open questions

- Does Halos's SDM or Edge Safety Link accept safe-state requests from a non-safety partition? The IGX safety brief is registration-gated.
- What do Figure, Skild and Gecko wrap with OpenShell, and do any of them run IGX?
- Can the OpenShell prover model **external state** (a safety-zone flag), or only its own policy grants?
- Could an agent-level decision ever be *certified* as a safety function under TS 22440, or will agent security always sit outside the safety case?

## Sources

- [Inside NVIDIA Halos for Robotics (developer blog)](../../sources/nvidia-halos-robotics-blog.md)
- [NVIDIA Halos for Robotics (AI Trust Center)](../../sources/nvidia-halos-robotics.md)
- [Industrial AI Podcast #352 — NVIDIA's safety strategy](../../sources/industrial-ai-podcast-nvidia-safety-strategy.md)
- [Add Runtime Controls to AI Agents with NVIDIA OpenShell](../../sources/nvidia-openshell-runtime-controls-blog.md)
- [NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring](../../sources/nvidia-open-agent-safety-platform-sentry-blog.md)
- [NVIDIA Launches Open Agent Safety Platform (Newsroom)](../../sources/nvidia-newsroom-open-agent-safety-platform.md)
- [Where Security Fits in an AI Agent Stack](../../sources/nvidia-where-security-fits-agent-stack.md)

## Related

- [NVIDIA Halos](../../entities/nvidia-halos.md) · [NVIDIA OpenShell](../../entities/nvidia-openshell.md) · [NVIDIA Sentry](../../entities/nvidia-sentry.md)
- [Guardrails for robot agents](guardrails-for-robot-agents.md): the five-layer cake and the latency problem
- [Robot security](../../concepts/robotics/robot-security.md) · [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) · [AI guardrails](../../concepts/safety/ai-guardrails.md)
- [Frontier-agent containment incidents, summer 2026](frontier-agent-containment-incidents-2026.md)

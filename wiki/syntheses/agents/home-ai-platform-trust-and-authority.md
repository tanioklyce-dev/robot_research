---
title: The home AI platform — agentic robot AI meets home automation, and where trust and authority separate
type: synthesis
created: 2026-08-17
updated: 2026-08-17
tags: [agents, home-ai, smart-home, mcp, capability-manifest, trust-boundary, authority, multi-homing, liability, world-model, platforms, synthesis]
---

# The home AI platform — agentic robot AI meets home automation, and where trust and authority separate

The commercial category forming in 2026–2027 is **agentic robot AI fused with home-automation AI**, sold as an extension of the Nest / Ring / Google Home / Apple Home relationship. This page works out what that fusion actually requires: how a robot supports several competing ecosystems, whether it can live in more than one at once, and where the boundaries of authority and liability fall.

> [!warning] Half of this page rests on wiki evidence and half does not
> The **agentic-robotics half is well grounded** — abstraction levels, both MCP bridges, capability manifests, the guardrails gap, the governance argument. The **home-automation half is not covered by this wiki at all**: there is no page on Matter, Thread, HomeKit, SmartThings, Alexa, or any smart-home platform, and no source has been ingested on any of them. Claims about smart-home architecture below are **marked and uncited**, and should be treated as framing to test rather than findings. See the [consumer-robotics value chain](../society/consumer-robotics-value-chain.md) for the same caveat applied to the market side.

## Naming

Call the consumer category **"home AI platform"** — plain, and legible as an extension of "smart home."

But the load-bearing name is different. What is actually being sold and fought over is a **persistent world model of a household**: floorplan, objects, routines, people, and state over time. The **household world model** is the asset; the robot, speaker and doorbell are sensor endpoints feeding it.

**"Personal AI" is the wrong name.** The unit is the household, not the person — spouses, children, an elderly parent, a houseguest, a cleaner, each with different permissions and asymmetric consent. That multi-tenancy is both the hardest technical problem and the whole privacy exposure, and a name containing "personal" conceals it.

The naming matters because it relocates the moat. Device-level lock-in is weak — cameras can be re-bought. **World-model lock-in is historical**: years of learned routines and per-person preferences cannot be re-bought or exported. It also relocates the regulation: [world-model governance](../../concepts/safety/world-model-governance.md) argues the object to reach is not the sensor feed but "the downstream creation of **persistent spatial profiles**," which puts the compliance burden on whoever holds the model, not whoever sells the hardware.

## What actually merges — and the two things that don't

### Rate: solved, and the wiki says how

[Control abstraction levels](../../concepts/robotics/control-abstraction-levels.md) gives the [Frontier Red Team](../../entities/frontier-red-team.md) taxonomy:

| Level | The model emits | Frequency demanded |
|---|---|---|
| 1. Direct control | motor torques every timestep | **~83 Hz** for real-time legged control |
| 2. Programmatic control | a Python controller mapping observations → actions | once; the code then runs at native rate |
| 3. Policy control | high-level commands to a **pretrained** policy | per decision |
| 4. RL supervision | a training setup | offline |

Home automation is declarative and event-driven — sub-Hz, comfortably above all four. The fusion is feasible **because levels 2 and 4 sidestep the frequency problem by making the model write the controller rather than be the controller** ([Anthropic robotics evaluation](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md): 83 Hz needed vs 0.2–0.4 Hz inference, a ~100× gap that reasoning budget does not close).

### Idempotency: unsolved, and it breaks the obvious analogy

*(Smart-home side uncited.)* Matter's multi-admin model works because device state is effectively **a lattice with a well-defined join**: two controllers both asking a bulb to be on yields *on*. Conflicts resolve by construction.

**Robot state has no such join.** Two ecosystems asking the robot to be in different rooms is undefined — and "undefined" here denotes a physical object in motion. Every multi-homing question below inherits this.

The wiki already shows the primitive that acknowledges it: [AgenticROS](../../entities/agenticros.md) capability manifests carry a **`blocks_base`** flag, so a mission occupying the base cannot be interleaved with another. That flag exists because the arbitration problem is real at hobbyist scale, long before any commercial platform meets it.

## How players will support multiple ecosystems

**The open layer has already converged on the answer, twice, independently.**

**[AgenticROS](../../entities/agenticros.md)** ([repo](../../sources/agenticros-github.md)) serves **six agent platforms** from one robot — an [OpenClaw](../../entities/openclaw.md) native plugin, a single MCP server covering Claude / Codex / [Hermes](../../entities/hermes-agent.md), Gemini CLI, and sandboxed [NemoClaw](../../entities/nemoclaw.md) — through **typed capability manifests** with `interruptible` and `blocks_base` flags, mission step-graphs with `{{step.outputs}}` templating, a deterministic NL→mission compiler, and **`/estop` bypassing the AI**.

**[ros2-mcp-server](../../entities/ros2-mcp-server.md)** ([repo](../../sources/ros2-mcp-server-github.md)) reaches the same shape from a different starting point: config-driven tool filtering, a structured `{status, reason, observation}` envelope, deterministic dispatch, out-of-band stop, and a `find_robots_for` capability query at the fleet layer.

**The pattern, stated generally: the integration surface is a typed capability manifest exposed over [MCP](../../concepts/agents/llm-agent-architecture.md), and the robot vendor authors it.** Ecosystems compete above that line and do not reach below it.

Expect the commercial version to take the same shape, for an unglamorous reason: it is the only structure that lets a vendor support Google *and* Amazon *and* Apple without shipping three firmwares and three safety cases. The manifest is also the natural place to put the certification boundary — what is declared is what was tested.

> [!note] Two independent implementations is a weak convergence, not a standard
> Both are small projects; AgenticROS has anonymous maintainers and no releases, and is **nav-first with no manipulation path**. What they demonstrate is that the *shape* is discoverable by anyone who tries, not that the industry will adopt it. A vendor consortium could just as easily produce something worse and mandatory.

## Can a robot live in several ecosystems at once?

**Yes at the agent layer. No at the world-model layer. The second is where the value is.**

**Agent-layer multi-homing is demonstrated** — AgenticROS is six platforms against one robot. Nothing prevents a household robot from accepting goal-level requests from two or more assistants.

**World-model multi-homing is uneconomic and semantically broken.** Two ecosystems each maintaining a persistent household model means duplicated sensing, divergent state, and two different answers to "where are my keys." The model is expensive to build, improves with exclusivity, and — unlike a light's on/off — **has no merge semantics**.

So the expected equilibrium:

| Layer | Multi-homed? | Why |
|---|---|---|
| Command surface (goals, queries) | **Yes, shallow** | Cheap; a manifest can serve many callers |
| Skill / policy execution | Vendor-owned | Not portable; safety case attaches here |
| **Household world model** | **No** | No merge semantics; exclusivity compounds; this is the asset |
| Preemption / arbitration | **Unsolved** | `blocks_base` is a primitive, not a protocol |

**Consequence for the platform fight:** it is not about the robot. Vendors will support every assistant, because that is cheap and it is not the asset. The contest is over **which ecosystem's model the robot reports its observations into**.

## Where trust and authority separate — three boundaries, not one

The reframing comes from the [Anthropic robotics evaluation](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md)'s conclusion, recorded on [control abstraction levels](../../concepts/robotics/control-abstraction-levels.md):

> A VLM's real-world influence can change by **orders of magnitude** depending on the information it has access to — so evaluations and deployments need to treat **access level as a core part of the system**.

**Authority is therefore not a permission flag. It is a position in the stack.**

### Boundary 1 — Authority: which abstraction level the ecosystem may reach

The commercially plausible split is: **the ecosystem gets Level 3** (goal-level commands to pretrained policies); **the vendor keeps Levels 1–2 and the constrained controller beneath**. The wiki's note on Level 3's unnamed dependency is exactly why — "high-level commands to a pretrained policy" is only safe because a constrained controller stands between the policy and the actuators (a diff-IK QP at ~1 kHz enforcing collision, clearance, keep-out and joint limits).

> [!warning] This boundary is load-bearing by accident, and it has a deadline
> The wiki states it plainly: the pretrained-policy layer is a de-facto safety boundary because "models cannot reliably drive joints, but can competently supervise controllers" — and **"it erodes as level-1 capability improves."** A platform whose safety boundary is the incapacity of the model on the other side of it is running on a clock, not on a design.

Note also that **perceptual access is an authority decision**: a compass (heading in degrees) was the most consistent performance lever across every model tested, larger than most reasoning-budget effects. What the ecosystem is allowed to *see* moves capability as much as what it is allowed to *command*.

### Boundary 2 — Trust: who is liable, and why it cannot yet be assigned

[World-model governance](../../concepts/safety/world-model-governance.md) calls for a time-stamped record of "what the system perceived, the state it inferred, and the action it took," so a physical incident can be reconstructed and **duty of care assigned across developer, deployer, operator, and integrator**.

The wiki's own callout on that requirement is the most important sentence on this page:

> For an end-to-end learned policy the inferred state is a **latent vector with no committed semantics** — logging it is easy; **reading it after an incident is the unsolved part.** This requirement is written as though the state were an inspectable object.

**So authority can be partitioned cleanly today, and liability cannot.** That asymmetry is the central unsolved problem of the category, and it produces a concrete prediction: **incumbents with legal departments will insist on Level-3-and-above access — not primarily for safety, but for defensibility.** An ecosystem that only ever emitted goals has a cleaner story after an incident than one that touched the controller, regardless of which was technically safer.

### Boundary 3 — Consent: household-level, not user-level

*(Uncited; no ingested source addresses this.)* A light responds to whoever asks. A robot that follows a child's instruction into a parent's bedroom, or a houseguest's instruction to open a door, is a different class of problem. Home automation's identity model is per-account; a household world model needs per-person, per-space, per-time-of-day authority — and the people it observes most (children, elderly relatives, visitors) are the least likely to have consented.

This is where [world-model governance](../../concepts/safety/world-model-governance.md)'s framing bites hardest: **the harm is inference, not collection.** A model that can find your keys can also infer that a gait has changed or that two people stopped sharing a bedroom. It is also where the [assistive robotics](../../concepts/robotics/assistive-robotics.md) thread stops being abstract, because the deployment environment *is* someone's home.

### The anchor beneath all three: the e-stop must bypass every ecosystem

[AgenticROS](../../entities/agenticros.md) already routes **`/estop` around the AI**, and [ros2-mcp-server](../../entities/ros2-mcp-server.md) has an out-of-band stop. There is no smart-home precedent for this, because nothing in that world ever needed one — which is the most compact statement of why this category is *not* simply an extension of Nest and Ring.

## The load-bearing caveat: the enforcement layer is mostly aspirational

Everything above assumes boundaries can be *enforced*. The wiki's finding is that they largely cannot yet:

- [Guardrails for robot agents](guardrails-for-robot-agents.md) — **the execution rail ships empty**; the MCP allowlist is "the only thing playing that role in any ingested robot stack."
- [Nav2 behavior trees](../../sources/nav2-behavior-trees-docs.md) qualify this — a real execution rail *does* ship, **scoped to navigation** ([Nav2](../../entities/nav2.md) + [BehaviorTree.CPP](../../entities/behaviortree-cpp.md)). Nothing equivalent exists for manipulation.
- [NemoClaw](../../entities/nemoclaw.md) ([product page](../../sources/nvidia-nemoclaw-page.md)) is the one shipped commercial attempt at the wrapper — OpenShell policy guardrails, local Nemotron, network-policy tiers — and it is an **early preview** targeting RTX PCs and DGX Station, i.e. the local-first bet.
- [NVIDIA's agentic safety recipe](../../sources/nvidia-safety-recipe-agentic-ai.md) has the right build→deploy→run architecture and its artifact was **deprecated 2026-04-22**.

**Local-first vs cloud is the falsifiable predictor of trust** — architectural, visible in a teardown, hard to fake. The wiki's own consumer evidence says the cheap tier structurally cannot do it: the [Zeroth M1](../../entities/zeroth-m1.md) publishes **no compute spec at all** and reportedly runs Gemini, and [Vulcan](../../entities/vulcan-robotics.md) sells hardware **plus rented compute**, conceding the advertised AI does not run on the robot.

## Open questions

- **Does anyone ship a capability manifest commercially?** Both wiki instances are hobbyist-scale and nav-first. A vendor manifest with a certification boundary attached would be the strongest signal this analysis is right.
- **What is the arbitration protocol** when two ecosystems issue conflicting goals? `blocks_base` is a flag, not a protocol, and nothing in the wiki addresses cross-ecosystem preemption.
- **Can incident reconstruction be made to work** for an end-to-end policy at all, or does liability force the whole category up to Level 3 permanently? This decides the architecture, not just the paperwork.
- **What does Matter's multi-admin model actually guarantee**, and is any of it salvageable for non-idempotent state? Needs the specification ingested — the strongest single source that would ground the smart-home half of this page.
- **Household multi-tenancy**: no ingested source covers per-person authority in a shared space. This is a genuine literature gap, not just a wiki gap.

## Related

- [Consumer robotics value chain](../society/consumer-robotics-value-chain.md) — the market-structure companion to this page
- [Control abstraction levels](../../concepts/robotics/control-abstraction-levels.md) · [World-model governance](../../concepts/safety/world-model-governance.md)
- [Guardrails for robot agents](guardrails-for-robot-agents.md) · [Where the compute lives](on-device-and-on-robot-agents.md) · [LLM-agent architecture across stacks](llm-agent-architecture-across-stacks.md)
- [Fleet agentic framework](../projects/fleet-agentic-framework.md) — the wiki's own manifest-and-bridge design
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) — ISO 13482, the certification path a home platform must eventually meet

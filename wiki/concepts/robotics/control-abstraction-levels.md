---
title: Control abstraction levels
type: concept
created: 2026-07-27
updated: 2026-08-03
sources: 25
tags: [robotics, control, llm-agent, evaluation, vla, safety, access-control, frontier-red-team, code-as-policy]
---

**Control abstraction level** — *where* in the stack a controller is allowed to act, from emitting raw joint torques to issuing goals at a pretrained policy. It is usually treated as an implementation detail. [Anthropic's robotics evaluation](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) is the wiki's argument that it should be treated as a **first-class variable of both capability and safety**, because the same model's real-world influence changes by *orders of magnitude* across levels.

## The four levels

From the [Frontier Red Team](../../entities/frontier-red-team.md)'s taxonomy:

| Level | The model emits | Frequency demanded |
|---|---|---|
| **1. Direct control** | Low-level motor torques/forces, every timestep | ~83 Hz for real-time legged control |
| **2. Programmatic control** | A Python controller mapping observations → actions | Once (then the code runs at native rate) |
| **3. Policy control** | High-level commands to a **pretrained** policy | Per decision, not per timestep |
| **4. RL supervision** | A training setup; an RL policy is learned from scratch | Offline |

Levels 2 and 4 sidestep the frequency problem entirely by making the model **write the controller rather than be the controller**.

> [!note] Level 3 has an unnamed dependency
> *"High-level commands to a pretrained policy"* is only safe because a **constrained controller** stands between the policy and the actuators. In the MIT/TRI stack that is a diff-IK QP at ~1 kHz enforcing arm–arm collision, table clearance, an end-effector keep-out region, and joint limits — *"particularly valuable for safeguarding the learned policy during hardware deployment"* ([Diffusion Policy](../../sources/diffusion-policy-paper.md) App. D.1). The taxonomy scores **how far up the model sits**; it does not score **how tightly the bottom is bounded**, and those are independent axes of real-world influence. A level-1 model with a hard constraint envelope may be far less dangerous than a level-3 model without one. See [operational space control](operational-space-control.md).

## Level 2 is not one level — it is eight

[CaP-X](../../sources/cap-x-paper.md) (ICML 2026) subdivides "programmatic control" into a measured ladder, and the span *within* this single level is larger than some gaps *between* levels:

| Axis | Rungs |
|---|---|
| **Primitive abstraction** | **S1** human macros + privileged state → **S2** macros + real perception → **S3** low-level primitives + usage examples → **S4** low-level, signatures only |
| **Temporal interaction** | single-turn → **M1** `stdout`/`stderr` feedback → multi-turn with grounding |
| **Perceptual grounding** | none → **M2** raw RGB → **M3** Visual Differencing Module (observations rendered as structured text) → **M4** VDM + low-level primitives |

Three findings that qualify everything this page says about level 2:

- **Success rises monotonically S4 → S1.** The prior literature's strong "code-as-policy works" results were largely measured at **S2**, where human-designed macros like `stack_objs_in_order()` do much of the work. See [code as policy](../agents/code-as-policy.md) for what that does to the lineage.
- **Raw pixels hurt.** Feeding RGB back each turn (M2) *degrades* performance relative to text-only execution traces (M1) — a cross-modal alignment gap. Converting observations to structured language (M3) beats both. **The grounding modality matters more than grounding quantity.**
- **Test-time compute substitutes for abstraction.** Multi-turn over low-level primitives (M4) reaches parity with multi-turn over human macros (M3), and beats single-turn over macros (S2).

> [!note] What this does to "an eval result is meaningless without its abstraction level"
> The claim below survives and gets sharper. It is not enough to say a result is "level 2 / programmatic control" — **which primitives, how many turns, and what feedback format** move the number by tens of points. A code-as-policy success rate without its tier is close to uninterpretable.

The measured example: a Gemini-3-Pro agent goes from **24%** at single-turn low-level (S3) to **68%** with the full [CaP-Agent0](../../entities/cap-x.md) harness — same model, same robot, same tasks, different rung.

## Capability is not monotonic in the level — it inverts

The measured pattern: **frontier models get worse the lower they reach.**

- **Direct control** is where they fail. No model in the evaluation stood a 29-DoF humanoid from a collapsed pose *even once*; the best quadruped balance was ~2 seconds; end-to-end LIBERO pick-and-place tops out around **5.5%**.
- **Programmatic control substantially outperforms direct control** for essentially every model tested — the same intelligence, routed through code, does far better than the same intelligence emitting numbers.
- **Policy control** is where the gains live. Given a pretrained policy to command, models navigate mazes and complete multi-step tasks.

The [Project Fetch](../../sources/anthropic-project-fetch-robot-dog.md) line confirms this from the other direction: Claude in Claude Code — **level 2** — went from 2× human uplift to [19× faster than the assisted humans](../../sources/anthropic-project-fetch-phase-two.md) in ten months, while the one thing it still could not do was the **closed-loop retrieval** that requires level-1-style continuous feedback.

> [!note] The blunt version
> Today's frontier models are **good at writing robot software and bad at being robot software.** Every strong result in this line comes from a level where the model's output is consumed by something slower than physics.

## Why the ceiling is structural: the 83 Hz gap

Real-time legged control needs roughly **83 Hz**. Non-reasoning inference runs at **~0.2–0.4 Hz** — 2–8 s text-only, 5–15 s with images, 15–180 s with reasoning. That is a **~100× gap**, and it is why the evaluation had to **pause the simulator** between calls to measure direct control at all.

This is not a gap that better reasoning closes. The evaluation found extra reasoning budget produced **no** general robotics gain and sometimes *hurt* — improvement across model generations came from better vision, numerical consistency, and 3D understanding instead. Nor is it obviously a gap that smaller models close: the wiki's edge-inference numbers put on-Jetson VLAs at **1.4–27.8 Hz** ([XLeRobot onboard compute](../../syntheses/platforms/jetson-onboard-compute-xlerobot.md)) — better, but those are purpose-built action models, not general LLMs, and still short of 83 Hz for the hardest cases.

Every frequency in this paragraph, plus the wiki's other ~30 rate numbers, is tabulated on one axis in the [Control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) — which shows the 83 Hz figure sits at the bottom of a band **nothing in this wiki deploys into**, and that the comparison worth tracking is the LLM's 0.2–0.4 Hz against the VLA planner tier's 1.4–27.8 Hz.

## Supervision: knowing when *not* to intervene

Level 3 has its own failure mode, and it is the most transferable finding in this cluster. Given [MolmoAct](../../entities/molmoact.md) as a pretrained manipulation policy on LIBERO-40 with the freedom to override its actions:

- **On tasks the VLA already handles, supervision makes things worse** — every model tested scored below MolmoAct running alone. Better models hurt less.
- **On tasks the VLA cannot do, supervision helps** — the same models beat MolmoAct-alone.
- The variable is **deference calibration**: Opus 4.5/4.6 copy the policy's action most often and do best in-distribution; a model that overrides more often loses in-distribution and wins out-of-distribution; the weakest models **defer indiscriminately**, unable to tell a competent action from an incompetent one.

So the supervisor's skill is not "can I do better than the policy" but **"can I tell when I can do better than the policy."** This is exactly the [LLM-agent architecture](../agents/llm-agent-architecture.md) pattern — a language model above a lower-level controller — with the override decision finally measured rather than assumed.

## The safety consequence: access level is part of the system

The evaluation's own conclusion:

> A VLM's real-world influence can change by **orders of magnitude** depending on the information it has access to — so evaluations and deployments need to treat **access level as a core part of the system**, because small changes in tools or control can produce large changes in capability.

Three practical implications:

1. **An eval result is meaningless without its abstraction level.** "Claude can/can't control a robot" is not a claim; "Claude at level 1 can't and at level 3 can" is.
2. **The pretrained-policy layer is a de-facto safety boundary** — models cannot reliably drive joints, but can competently supervise controllers. That boundary is load-bearing *by accident*, and it erodes as level-1 capability improves.
3. **The stated deployment direction is scoped physical access** — granting a system the ability to affect certain objects while blocking others. Compare the wiki's [guardrails](../safety/ai-guardrails.md) thread, where the **execution rail** that would enforce exactly this ships **empty**, and the [MCP allowlist](../../syntheses/agents/guardrails-for-robot-agents.md) is currently the only thing playing that role in any ingested robot stack.

Perceptual access moves capability as much as control access does: a **compass** (heading in degrees) was the most consistent performance lever across every model tested — larger than most reasoning-budget effects — while depth heatmaps and crosshairs were roughly neutral. What the model can *see* is an access-level decision too.

## Related concepts
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — the companion axis: this page is *where* a controller acts, that one is *what it says* at that level, and whether it can be human-readable.
- [Code as policy](../agents/code-as-policy.md) — level 2 as an architecture rather than an evaluation condition; the source of the eight-rung subdivision above.
- [Control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) — every rate in the wiki on one axis; the four bands, and the two mechanisms (hierarchy, action chunking) that bridge them.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — level 3, as an architecture rather than an evaluation condition.
- [VLA models](../learning/vla-models.md) — the pretrained-policy layer being supervised; VLAs *are* the level-1/2 solution that works.
- [AI uplift studies](../safety/ai-uplift.md) — level 2 measured as human assistance rather than autonomy.
- [AI guardrails](../safety/ai-guardrails.md) — where scoped physical access would be enforced, and currently isn't.
- [Whole-body control](whole-body-control.md) — the classical answer to what level 1 demands, and why learned WBC policies exist.

## Mentioned in
- [How Claude Performs on Robotics Tasks](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — the source of the taxonomy and every number here.
- [Project Fetch: Phase Two](../../sources/anthropic-project-fetch-phase-two.md) — level-2 control (Claude Code writing controllers) taken to near-autonomy.
- [CaP-X paper](../../sources/cap-x-paper.md) — the eight-tier subdivision of level 2; abstraction, iteration, and grounding as independently controllable axes.
- [Gemini Robotics 2: Safety Evaluations](../../sources/gemini-robotics-2-safety-report.md) — the same level-inversion from the safety side: agents score **100%** acting on a safety signal handed to them as structured text, but cannot reliably **produce** that signal from perception (human-proximity FNR >40% at low FPR).

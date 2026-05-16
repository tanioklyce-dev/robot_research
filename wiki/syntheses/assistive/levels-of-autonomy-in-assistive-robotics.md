---
title: Levels of autonomy in assistive robotics
type: synthesis
created: 2026-05-09
updated: 2026-05-09
tags: [assistive-robotics, autonomy, sense-of-agency, eup, hcrlab, variable-loc, hri]
---

What is the right level of autonomy for an assistive robot? The default assumption in robot-learning research — *more autonomy is the goal* — does not survive contact with the empirical record on disabled users. Five sources in this wiki, mostly from [HCR Lab](../../entities/hcrlab.md) and adjacent groups, converge on a different picture: autonomy is **multi-dimensional**, **task-conditional**, and the **right design target is user-controlled variability, not maximal autonomy**.

> [!note] TL;DR
> "Autonomy" is at least three orthogonal axes: who *executes* actions, who *programs* the behavior, and who *infers intent*. Empirical studies show user preference depends on all three. The practical design pattern that emerges — **variable levels of control with end-user programming as the default** — is converging across HCR Lab's full research arc (HRI 2020 → Walker 2024 → Yang 2025 → Nanavati 2025).

---

## What the systematic review says

[Nanavati, Ranganeni & Cakmak 2024](../../sources/nanavati2024-physically-assistive-robots-review.md) — the canonical PRISMA review of physically assistive robots (87 papers from 1,981 screened) — identifies **levels of autonomy** as one of three research themes structuring the field, alongside interaction interfaces and adaptation. The review treats autonomy as a *design choice*, not a *target*: different points on the autonomy spectrum suit different tasks, users, and contexts. This is the field-level baseline.

---

## Three orthogonal axes of "autonomy"

Most robotics papers conflate these. The HCR Lab work pulls them apart:

| Axis | Question | Where it shows up |
|---|---|---|
| **Execution autonomy** | Who moves the robot? Direct teleoperation ↔ autonomous policy. | All assistive HRI studies. |
| **Programming autonomy** | Who specifies the *behavior*? Engineer ↔ third-party operator ↔ end user (EUP). | [Yang et al. 2025](../../sources/yang2025-sense-of-agency.md); [End-user robot programming](../../concepts/robotics/end-user-robot-programming.md). |
| **Intent inference** | Does the robot guess what the user wants, or does the user say so explicitly? | [Walker et al. IROS 2024](../../sources/walker2024-explicit-input-teleoperation.md). |

The headline finding from Yang et al. 2025: **execution autonomy and programming autonomy affect sense of agency independently**. A fully autonomous robot acting on a program the user wrote themselves preserves agency. A teleoperated robot controlled by a third party reduces agency *more than* full autonomy alone. This is not derivable from a one-dimensional autonomy spectrum.

---

## Five empirical findings

### 1. People with severe motor impairments do NOT always prefer more autonomous robots
HCR Lab, **HRI 2020**. Cited via [Maya Cakmak's research overview](../../sources/maya-cakmak-research.md) and the [HCR Lab publications page](../../sources/hcrlab-publications.md). The autonomy–control tradeoff is **user-specific and context-specific** — it is not a universal preference for more autonomy. This is the foundational finding the rest of this synthesis builds on.

### 2. Sense of agency is preserved when the user is the *programmer*, even at high execution autonomy
[Yang et al., RO-MAN 2025](../../sources/yang2025-sense-of-agency.md). Two-part survey study using [Stretch](../../entities/stretch.md) 3 illustrations across four robot autonomy levels:

- (A) Fully autonomous
- (B) **End-user programmed** (highly preserves agency)
- (C) Third-party teleoperated
- (D) Fully user-controlled

End-user programmed robots highly preserved agency *even when acting autonomously*. **Third-party involvement reduced agency more than autonomy alone**. The model: "Sense of agency can be preserved if the robot is programmed by the user, instead of relying on a third party to control the robot."

### 3. High-risk tasks drive preference for user control
Same study ([Yang et al. 2025](../../sources/yang2025-sense-of-agency.md)). In high-risk scenarios (e.g., preparing a snack for a child with allergies, medication tasks), participants strongly preferred robots that prioritize user control. In low-risk contexts, higher autonomy was acceptable. Risk is a moderator, not a confound.

### 4. Variable level-of-control is essential for real-world deployment
[Nanavati et al., HRI 2025 — Lessons Learned from Out-of-Lab Feeding](../../sources/nanavati2025-feeding-out-of-lab.md). The open-source Kinova-JACO feeding system implements three operating modes the user can switch between mid-meal:

- **Supervisory** — pause when needed
- **Decision support** — robot offers multiple options; user picks
- **Teleoperation** — direct Cartesian/joint control

Lesson 2 of the paper: *"off-nominals will arise."* Variable autonomy lets users escalate or de-escalate to overcome unexpected events without ending the session. This is the operational rationale for not picking a single autonomy level.

### 5. Explicit user input beats implicit intent inference in clutter
[Walker et al., IROS 2024](../../sources/walker2024-explicit-input-teleoperation.md). N=20 within-subjects study on cluttered pick-and-place. Operators preferred an interface where they *point* the end-effector toward the target (explicit) over a system that *predicts* their intent from trajectory history (implicit). Fewer pick failures, lower NASA-TLX cognitive workload, no significant speed penalty.

The mechanism: in cluttered scenes, intent prediction is ambiguous; bad predictions confuse operators or force them to "signal" intent through unnatural motion, compounding errors. The paper's framing: "transparent state, smooth assistance, pose-as-suggestion not command."

---

## What the practical design pattern looks like

The sources converge on **end-user-programmed variable-LoC with explicit user input** as the architecture for assistive robots. Concretely:

1. **End user (or someone close to the user) programs the behavior.** Not engineers and not remote third parties. This preserves agency by making the user the author. EUP tools — visual programming, programming-by-demonstration, multimodal sketches, NL — are the substrate. See [End-user robot programming](../../concepts/robotics/end-user-robot-programming.md).
2. **Variable level of control at runtime.** User can pause, take over, hand back. Default to the autonomy level appropriate to the current task and risk; let the user shift up or down as off-nominals arise.
3. **Explicit input where intent is ambiguous.** When the robot needs to know what the user wants, ask explicitly (point at the object, click, voice command) rather than inferring from history.
4. **Risk-aware defaults.** Routine tasks (fetching a known object) can default high-autonomy. High-stakes tasks (medication, food allergies, body contact) should default low-autonomy.

This design pattern is what HCR Lab actually ships. The EUP toolchain has been transferred to commercial Hello Robot Stretch SE2 ([Maya Cakmak Research](../../sources/maya-cakmak-research.md)). The feeding system Nanavati et al. deployed implements all four properties.

---

## Tension with mainstream robot-learning research

Mainstream robot-learning aims for **fully autonomous, language-conditioned policies** — VLAs, RUMs, OK-Robot's open-vocabulary fetching. The Yang 2025 result implies that for assistive use, *handing a fully autonomous policy a verbal command from a third party* (the typical research deployment shape) is exactly the case that **reduces** sense of agency the most: the user is neither programming nor operating.

This does not mean the policies are useless — RUM-class policies can become *primitives* a user-programmed behavior calls. But the deployment shape needs a layer between the user and the policy that the user owns: their own program, expressed via EUP, calling RUM/OK-Robot/etc. as low-level skills.

> [!note] Open question
> No ingested source actually demonstrates this stack — *user-programmed EUP behaviors calling general-purpose policies as primitives*. It is the natural integration shape implied by this synthesis but unbuilt. It is the most concrete unimplemented architectural target this wiki points to.

---

## Counter-evidence and caveats

- **Yang 2025's sample**: not yet confirmed whether the survey included people with motor impairments or only non-disabled participants. The headline finding may not generalize evenly across disability categories ([open question in source](../../sources/yang2025-sense-of-agency.md)).
- **Walker 2024's operators**: described as "operators" — likely non-disabled users in simulation. Whether explicit pointing transfers to users who *cannot* easily point (severe motor impairment, low motor bandwidth) is an open question.
- **HRI 2020 sample size**: the autonomy-preference finding is repeatedly cited but the original study's sample was small and specific to feeding. Its generality should be hedged.

---

## What an independent researcher could test

1. **Replicate Yang 2025 with users with motor impairments.** The four-level autonomy survey adapted for a sample with the actual target disability would either generalize the finding or produce a more nuanced version.
2. **Build the user-EUP-over-RUM stack and measure agency.** A Stretch running [stretch_ai](../../entities/stretch-ai.md) where the LLM-agent skills are *user-authored* via an EUP layer, rather than engineer-authored. Measure sense of agency under Yang 2025's instrument. Plausibly publishable systems work.
3. **Measure agency cost of intent inference.** Run Walker 2024 under Yang 2025's lens: does explicit pointing preserve agency more than implicit inference, holding execution autonomy constant?
4. **Risk-conditional defaults experiment.** Same task, two policies: one defaults autonomy by user history, one by user-defined risk tags. Does risk tagging meaningfully reduce errors on high-risk subtasks?

---

## Sources used in this synthesis

- [Physically Assistive Robots — Systematic Review (Nanavati et al. 2024)](../../sources/nanavati2024-physically-assistive-robots-review.md)
- [Sense of Agency (Yang et al. 2025)](../../sources/yang2025-sense-of-agency.md)
- [Feeding System Out-of-lab (Nanavati et al. 2025)](../../sources/nanavati2025-feeding-out-of-lab.md)
- [Explicit-Input Teleoperation (Walker et al. 2024)](../../sources/walker2024-explicit-input-teleoperation.md)
- [Maya Cakmak Research Overview](../../sources/maya-cakmak-research.md)
- [HCR Lab Publications](../../sources/hcrlab-publications.md)
- [End-user robot programming concept](../../concepts/robotics/end-user-robot-programming.md)

## Related

- [Assistive robotics — R&D landscape and JEPA applicability](assistive-robotics-research-landscape.md) — broader R&D context; this synthesis zooms in on autonomy alone.
- [End-user robot programming](../../concepts/robotics/end-user-robot-programming.md) — the practical design lever this synthesis recommends.
- [Assistive robotics](../../concepts/robotics/assistive-robotics.md) — concept overview.
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — the layer between user-authored programs and low-level skills.

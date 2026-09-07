---
title: Impedance and admittance control
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [impedance-control, admittance-control, variable-impedance, compliance, passivity, energy-tanks, force-control, contact-rich, action-space, safe-execution]
---

# Impedance and admittance control

## Definition

**Impedance control** regulates the dynamic relationship between the robot's motion and the forces it experiences, making the arm behave like a virtual **mass–spring–damper**. You command a reference pose and a stiffness/damping/inertia; the robot deviates from the reference in proportion to external force. **Admittance control** is the dual: measure the external force and command a motion in response. Impedance suits stiff robots with torque control; admittance suits position-controlled robots facing large environmental forces ([Zhang et al.](../../sources/safe-learning-contact-rich-survey.md), §3.1.2).

Both are **compliant control**: the robot absorbs impact energy and maintains stable contact with surfaces whose pose and shape it does not know exactly. This is the workhorse of **safe execution** in [contact-rich manipulation](contact-rich-manipulation.md) — the single most-used mechanism in the literature the survey reviews.

## Why it is a safety mechanism and not just a control choice

A position-controlled arm commanded into a surface it thinks is 2 mm further away will apply whatever force its gains and its structure permit. A compliant arm applies **K·Δx** — a force you chose in advance by choosing K. Compliance converts a *position error* into a *bounded force*, which is why it appears in every layer of the safe-execution stack:

- **Impact absorption at contact onset**, the phase where force transients peak.
- **Stable sustained contact** with uncertain or moving surfaces.
- **Bounded force by construction** rather than by runtime intervention — no filter has to fire.
- **Physically interpretable parameters**, so a safety argument can be written about them.

## Variable impedance, and impedance as a learned action space

Fixed gains are a compromise: stiff enough to track, soft enough not to damage, right in neither regime. **Variable impedance control (VIC)** adapts stiffness and damping online. The dominant safe-execution pattern in the learning literature is to make **the impedance parameters the policy's action space**:

> A major research direction in safe execution for contact-rich tasks is the use of RL to automatically tune the parameters of compliant controllers — stiffness, damping, and inertia — enabling the robot to adapt its compliance to varying task requirements and contact conditions. (§3.1.2)

The policy outputs **pose targets, force targets, and stiffness/damping gains**; a classical controller turns those into torques at kHz rates. The survey's repeated recommendation is that a learned policy should emit exactly this and **never raw torques**, for three reasons:

1. **Stability margins are preserved by construction** — the inner controller's passivity argument still holds.
2. **The safety layer gets an interpretable hook.** "Reduce commanded stiffness" and "cap the force target" are modifications a filter can make and a human can audit; "perturb this torque vector" is not.
3. **Sim-to-real transfers better**, because the abstraction absorbs dynamics mismatch that raw torques expose.

> [!note] The same recommendation, from an unrelated literature
> [Control abstraction levels](control-abstraction-levels.md) treats the choice of what a model emits as an axis of **capability and access** — frontier models are bad at emitting torques and good at commanding policies. This page's literature reaches the same layering from a **physical-safety** argument that has nothing to do with model capability. Two independent reasons to put an interpretable reference interface between the learned thing and the actuators.

## Passivity and energy tanks

Force limits bound the *instantaneous* interaction. **Passivity** bounds the *cumulative* one: design the closed loop so the robot cannot generate energy, and stable interaction with any passive environment follows regardless of the environment's parameters. This matters because the environment in a contact-rich task is exactly the thing you do not have a model of.

**Energy tanks** implement it practically — a finite reservoir the controller draws from to perform non-passive actions, refilled by dissipated energy. When the tank empties, the behavior degrades to passive instead of running away. **Passivity indices and energy tanks cap impact energy and prevent force runaway under delays, unmodeled compliance, or high-gain settings** (§2.2.1), which are precisely the conditions where a learned policy's commanded stiffness can destabilize a real arm.

Passivity is the Lyapunov-family certificate for interaction; see [safety certificates](safety-certificates.md).

## Where it falls short

- **Parameter tuning is the classical bottleneck** — stiffness, damping, and inertia are hand-tuned by expert trial-and-error, do not generalize across tasks, and get it wrong in either direction: too stiff gives excessive contact force and instability, too soft fails the task.
- **Stability under rapid re-tuning is rarely quantified.** The survey is blunt that variable-impedance policies "modulate compliance adaptively, **yet stability margins under rapid re-tuning are seldom quantified**" (§4.5). A learned gain schedule can be unstable in a way a fixed gain is not, and almost nobody measures it.
- **Compliance is not a constraint.** It makes large forces unlikely, not impossible. Hard limits still need a barrier or reachability layer on top — which is why the recommended stack has both.
- **Precision costs compliance.** Tight-tolerance insertion wants stiffness; safety wants softness. This is the concrete form of the safety/performance trade-off in §4.5.

## Related concepts

- [Contact-rich manipulation](contact-rich-manipulation.md) — the task class this controller family exists for.
- [Safety certificates](safety-certificates.md) — passivity as a Lyapunov-family guarantee; barriers as the hard-constraint complement.
- [Safe reinforcement learning](../learning/safe-reinforcement-learning.md) — how the gains get learned.
- [Operational space control](operational-space-control.md) — the task-space formulation these controllers are usually written in; Khatib's framework is the shared ancestor.
- [Safety filters for learned policies](safety-filters.md) — the layer above, which projects whatever the policy emits onto the admissible set.
- [Control abstraction levels](control-abstraction-levels.md) — impedance references as an action space, and what that buys.
- [Whole-body control](whole-body-control.md) — the same compliance idea at humanoid scale.

## Current state

Mature as classical control, actively researched as a learned action space. RL-tuned impedance is demonstrated across assembly, insertion, surface interaction, massage, and bathing assistance; passivity-aware and energy-tank formulations are the standard way of keeping learned gain schedules from destabilizing hardware. The named open problems are **quantified stability margins under online re-tuning**, and the composition question: how a passivity argument survives being wrapped around a large expressive policy is, per the survey's §4.1, *"technically challenging, especially when contact conditions change rapidly or unpredictably."*

The frontier the survey bets on is **a VLM setting the gains** — its own group's OmniVIC (2510.17150) and CompliantVLA-adaptor (2601.15541) are the concrete instances, neither yet ingested here.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — the source for everything on this page.

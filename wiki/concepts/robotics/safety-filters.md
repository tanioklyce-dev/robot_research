---
title: Safety filters for learned policies
type: concept
created: 2026-08-16
updated: 2026-08-27
sources: 7
tags: [safety-filter, control-barrier-functions, reachability-analysis, path-consistency, out-of-distribution, diffusion-policy, constraint-enforcement, iso-ts-15066, runtime-safety, human-robot-interaction]
---

**A safety filter** is a mechanism that sits between a policy and the actuators, takes the policy's proposed action, and emits the nearest action it can certify as safe. It is the standard answer to a problem this wiki has been circling for a year: **learned policies are black boxes with no safety property**, and the deployment environments people want them in are ones where a physical guarantee is required.

The wiki has three ingested instances, and comparing them yields a result that none of them states alone: **the axis that predicts whether a filter destroys the policy is not how strong its guarantee is — it is whether the filter keeps the robot on the path the policy intended.**

## The three instances

| | [Constrained diff-IK QP](operational-space-control.md) | [OSCBF](../../sources/oscbf-paper.md) | [PACS](../../sources/pacs-paper.md) |
|---|---|---|---|
| Who | TRI / MIT (deployed) | Morton & [Pavone](../../entities/marco-pavone.md), Stanford | Römer, Balletshofer, Thumm, **Pavone**, Schoellig, Althoff (TUM + Stanford) |
| Guarantee | **None claimed** — per-tick feasibility | **Forward invariance** via CBFs | **Reachability-verified failsafe**, safe by induction |
| Intervention | Nearest feasible joint velocity | Nearest task-consistent acceleration | **Braking along the intended path** |
| Hazard model | Static, modelled: arms, table, keep-out box | Static, modelled: up to 1000+ sphere pairs, singularity | **Dynamic**: moving objects and humans, with bounded-error state estimates |
| Constraint source | Hand-authored from a URDF | Hand-authored barrier functions | **ISO/TS 15066** SSM and PFL energy thresholds |
| Rate | ~1 kHz | ~1–10 kHz (168 constraints at ~3 kHz) | 1 kHz (0.20 ms/step) |
| Tested on a learned policy | **Yes** — real LBM/DP rollouts, no measurement of the filter's cost | **No** — teleop only | **Yes, with numbers** |

## The finding: path consistency beats guarantee strength

[PACS](../../sources/pacs-paper.md) measured what a filter costs a diffusion policy, and the spread is enormous:

- A **control-barrier-function** filter on robomimic: average task success **0.04** — zero on two of three tasks.
- **PACS**, enforcing the same constraints by braking along the intended path: **0.72**, against **0.70** for the identical pipeline with the failsafe switched off.

Same robot, same tasks, same constraints, same class of formal guarantee. The difference is *where the filter moves the robot*. A reactive filter enforces safety by **deviating from the path** — and a behavior-cloned policy that finds itself off the demonstration manifold is in an **out-of-distribution state it cannot recover from**. The paper shows this directly, plotting end-effector traces against the training distribution: the CBF pushes the robot into unvisited regions and the policy flails; PACS slows down without leaving the path.

> [!note] Why this is a distribution-shift result, not a control result
> Every classical safety filter is designed against a *dynamics* criterion — will the system remain in the safe set. None of them is designed against the criterion that actually decides task success here: **will the policy still recognize the state it is in.** Those come apart exactly when the controlled object is a learned policy, and the safety literature's default objective ("minimally invasive in the control input") does not measure the thing that matters.
>
> Both refinements the wiki has ingested are answers to *"minimal in what?"*, at different scopes:
> - **[Task consistency](../../sources/oscbf-paper.md)** (OSCBF): filter the *task-hierarchy output* — operational-space and null-space accelerations — not the raw control input. Prevents excess motion at a given instant.
> - **[Path consistency](../../sources/pacs-paper.md)** (PACS): filter the robot's *speed along its intended trajectory*, never its direction. Prevents leaving the training distribution over a trajectory.
>
> They are not alternatives, and a task-consistent CBF is still path-deviating.
>
> **And a third line reaches the same constraint from outside safety.** [FOREWARN](../../sources/forewarn-paper.md) steers a policy by **selecting among the samples it already drew** rather than editing its output — in-distribution by construction, no manifold to fall off. Generalized: *a runtime intervention that stays inside the policy's own output distribution costs nothing; one that leaves it costs almost everything.*

## The taxonomy, as the literature has it

PACS's related-work section is the cleanest map available, and it splits along two axes:

**Where the intervention happens.**
- **Post-hoc filters** — the policy runs, the filter edits the output. Everything in the table above. Cheap, model-agnostic, and the source of the distribution-shift problem.
- **Inside the denoising process** — steer generation toward safe regions with cost gradients, classifier-free guidance, iterative projection onto a safe set, or CBFs injected into the diffusion steps. Keeps the action in-distribution by construction, but *"these approaches still change the policy, and their high computational costs limit their applicability to low-dimensional systems or offline planning."*

**How safety is verified.**
- **Optimization-based** (CBFs, model-predictive safety filters) — compute the safe input nearest the desired one. Reactive, path-deviating.
- **Reachability-based** — keep a provably correct **failsafe trajectory** available at all times; execute the nominal motion only while the failsafe is still verified. Can be **path-consistent** (brake along the path) or not.

Path-consistent reachability filtering is the corner PACS occupies, and its enabling contribution is making it work for **action chunks** — earlier path-consistent filters accepted a single goal with zero terminal velocity, so a chunked policy either stops at every waypoint or has waypoints skipped (worth **+28%** task success to fix).

## What none of them does

- **Perception.** All three consume a hazard geometry they do not produce: keep-out boxes, sphere decompositions, or object poses with bounded measurement error. In an unstructured home the hazards are the things nobody modelled.
  - **Correction (2026-08-16):** this was previously called *"the single shared blocker"*, which overstated it. **Latent Safety Filters** (Nakamura, Bajcsy et al., arXiv 2502.00935, **uningested**) run **Hamilton–Jacobi reachability in a generative world model's latent space**, turning constraint specification into latent-space classification over raw RGB — demonstrated preventing a Franka from **spilling a bag** and **toppling clutter**, hazards nobody can write down. It is a shared blocker *for the three filters compared here*, not for the field.
- **Semantic safety.** Every filter here prevents the robot from colliding or exceeding an impact energy. None prevents it from doing the wrong thing gently — throwing away the medication, as the [guardrails](../safety/ai-guardrails.md) thread puts it. Physical and semantic safety remain disjoint stacks.
- **Certification.** A reachability-verified failsafe against ISO/TS 15066 thresholds is the closest artifact the wiki has to conformity evidence, and it is still a research prototype ([robot safety standards](robot-safety-standards.md)).
- **The two hazard classes at once.** [OSCBF](../../sources/oscbf-paper.md) handles hundreds of static collision constraints and never faces distribution shift; [PACS](../../sources/pacs-paper.md) handles moving humans and defers *"(semi-)static obstacles via constraint-aware online replanning"* to future work. Nothing covers both.

## The metric this thread introduces

**Safe success** — the fraction of rollouts that complete the task *while never violating a safety constraint*. PACS's hardware table is the argument for it: unsafeguarded policies score **0.79 task success and 0.00 safe success**, violating constraints in **56% of all timesteps** and in **every rollout**. Task success and safety are close to independent, so a benchmark that reports only the former describes behavior nobody would deploy. Nothing else in the wiki's [policy-evaluation](robot-policy-evaluation.md) coverage measures this.

> [!note] A filter cannot see the failure mode it was never about
> Every mechanism on this page answers *"will this action hurt someone or break something?"* None answers *"is this rollout going to succeed?"* — the policy confidently placing the object in the wrong location passes every constraint. That question belongs to [runtime failure detection](runtime-failure-detection.md), which is a separate mechanism with separate signals (temporal action consistency, density in a learned flow, a VLM watching the video) and separate guarantees (conformal bounds on **false alarms**, not on misses).
>
> A deployed system needs both, and nothing in this wiki's corpus runs both at once.

## A shipped counterpoint: the filter as a floor, not an arbiter

Every instance above is a research filter that *decides* — it takes the policy's action and emits the nearest certifiably-safe one. [Microduck](../../entities/microduck.md)'s shipped safety layer ([runtime repo](../../sources/microduck-runtime-repo.md)) is built on the opposite premise, and the contrast is instructive because this one is in production on a consumer robot.

**What it enforces is deliberately tiny**: refuse non-finite targets (a `NaN` is refused, not clamped), clamp to *actuator* range — explicitly not per-joint anatomical limits — and a deadman that zeroes velocity when intents stop arriving. Note the deadman's semantics: *"stop is not limp… losing comms makes the robot **stand still**, because standing is the safe state for a biped."*

**What it refuses to enforce is the interesting part.** Fall detection runs every tick and is *published, not enforced*: a fallen robot is enabled, driven and sent skills exactly as an upright one is. Earlier revisions had a fall-limp gate and an auto-stand-up **inside** the safety layer, and both were deleted:

> "A safety rule that recovery has to bypass in order to work is not one."

Two structural properties make that safe rather than reckless:

- **The layer is unbypassable by construction.** It owns the only motor-bus write handle, so *"the borrow checker is the enforcement"* — nothing above it *can* command a motor, including the fall-recovery sequence, which reaches the actuators through the same clamp as everything else. There is no exemption and no back door.
- **The judgment moved up, not away.** Predictive fall mitigation (a second detector on gravity's *rate*, `ġ = −ω × g`, extrapolated ~0.3 s) runs above the filter and takes the robot away from the policy during a fall — but it proposes targets like any other client.

> [!note] This bears on the page's own finding
> The finding above is that **path consistency** predicts whether a filter destroys the policy. Microduck's design suggests a prior question: *how much should the filter be deciding at all?* A minimal floor cannot be path-inconsistent because it almost never intervenes — and everything the robot needs in order to recover is free to live above it. Whether that scales to a filter with a real guarantee (CBF, reachability) is untested; those exist precisely to intervene. But it is a reminder that the deployed answer to "learned policies have no safety property" is currently **clamp, refuse NaN, deadman, and put the cleverness elsewhere**.

## Related concepts

- [Prevention, detection, intervention](../../syntheses/platforms/prevention-detection-intervention.md) — the synthesis this page is layer 1 of.
- [Runtime failure detection](runtime-failure-detection.md) — the detection half of deployment; complementary, not competing.

- [Operational space control](operational-space-control.md) — the control formulation all three filters are built on.
- [Robot safety standards](robot-safety-standards.md) — SSM/PFL, and the certification gap.
- [Robot policy evaluation](robot-policy-evaluation.md) — where "safe success" belongs.
- [Imitation learning](../learning/imitation-learning.md) — OOD recovery is the failure mechanism.
- [Assistive robotics](assistive-robotics.md) — PACS's FEEDING task; a **0.001 J** head/eye impact limit is what "safe near a person" means numerically.
- [AI guardrails](../safety/ai-guardrails.md) — the semantic-harm stack these are disjoint from.

## Key references

- [PACS — Path-Consistent Safety Filtering for Diffusion Policies](../../sources/pacs-paper.md) (ICRA 2026) — **the primary source for this page**; the measurement, the OOD mechanism, and the ISO-grounded constraints.
- [OSCBF](../../sources/oscbf-paper.md) (IROS 2025) — CBFs inside an operational space controller; task consistency; 168 constraints at ~3 kHz.
- [Diffusion Policy](../../sources/diffusion-policy-paper.md) App. D.1 / [TRI LBM](../../sources/tri-lbm-paper.md) — the un-formal envelope that is actually deployed under real policies.
- [Safely learning dynamical systems](../../sources/safely-learning-dynamical-systems-paper.md) — the adjacent formal line: certificates for safe *exploration*, linear/polynomial systems only.

## Mentioned in

- [`pollen-robotics/microduck` — the onboard runtime](../../sources/microduck-runtime-repo.md) — the shipped minimal-floor counterpoint; the safety layer that gates nothing it does not have to.

- [PACS paper](../../sources/pacs-paper.md)
- [OSCBF paper](../../sources/oscbf-paper.md)
- [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) — Appendix D.1.

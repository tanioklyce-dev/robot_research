---
title: "From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies (PACS)"
type: source
url: https://arxiv.org/abs/2511.06385
local_path: raw/PACS_PathConsistentSafetyFiltering_2511.06385.pdf
sha256: 21868d56374237ec4e3d911852e28cabad8f7f03e42a2cf7474ff4195a32d532
project_page: https://tum-lsy.github.io/pacs
author: "Ralf Römer*, Julian Balletshofer*, Jakob Thumm, Marco Pavone, Angela P. Schoellig, Matthias Althoff (TUM MIRMI + Stanford)"
published: 2025-11-09
ingested: 2026-08-16
venue: arXiv 2511.06385 (v2, 2026-03-10); IEEE ICRA 2026
format: pdf
tags: [safety-filter, diffusion-policy, smolvla, reachability-analysis, out-of-distribution, path-consistency, control-barrier-functions, iso-ts-15066, power-and-force-limiting, speed-and-separation-monitoring, human-robot-interaction, assistive-feeding, franka-fr3, action-chunking, tum, stanford]
---

# PACS — Path-Consistent Safety Filtering for Diffusion Policies

## Summary

**The measurement the wiki filed as missing, taken this morning.** [Operational space control](../concepts/robotics/operational-space-control.md) recorded that nobody had run a learned policy through a formal safety filter and reported what it costs. PACS does exactly that, and the answer has a shape nobody would have guessed from the safety literature alone:

**A safety filter's cost to task success depends almost entirely on whether it keeps the policy inside its training distribution.** Reactive filters — control barrier functions among them — enforce safety by pushing the robot *off its intended path*, which lands a diffusion policy in **out-of-distribution states it cannot recover from**. On robomimic, a CBF safety filter drops average task success to **0.04**. PACS, which enforces the same constraints by **braking along the intended path instead of deviating from it**, holds **0.72** — statistically indistinguishable from the *unfiltered* joint-space baseline (0.70).

On hardware — three human-robot-interaction tasks on a Franka FR3, including **putting a fork of food into a person's mouth** — unsafeguarded policies violate their safety constraints **56% of all timesteps** and achieve a **0% safe-success rate**, while PACS achieves **0.80 success with 0.80 safe success and zero violations**. Safety verification is set-based **reachability analysis** at **1 kHz** (0.20 ms per safety step).

> [!note] The result reframes a distinction the wiki had been drawing at the wrong place
> The [OSCBF ingest](oscbf-paper.md) framed the axis as **guarantee vs no guarantee** — hand-written constraints versus forward invariance. PACS says that axis is not the one that predicts task success. **Path-consistent vs path-deviating is.** A filter with an impeccable invariance proof that moves the robot sideways off the demonstration manifold destroys the policy; a filter that merely slows the robot along the path it already intended costs nothing measurable.
>
> This is a **distribution-shift argument dressed as a control argument**, and it connects the safety literature to the [imitation-learning](../concepts/learning/imitation-learning.md) literature in a way neither usually does.

## The mechanism

**1. Turn the action chunk into an intended trajectory.** Diffusion policies and VLAs emit *chunks* of `H` consecutive actions at a low rate. PACS integrates the chunk's delta-joint-positions forward into a sequence of waypoints, then solves a **time-optimal trajectory problem** through those waypoints subject to the robot's position, velocity, acceleration and jerk limits (Ruckig). This intermediate step is a contribution in itself — prior path-consistent filters accept only *one* goal with zero terminal velocity, so applied to a chunk they either stop at every waypoint or skip intermediate ones.

**2. Monitor a two-part trajectory.** At each safety tick, concatenate the **intended** trajectory with a **failsafe** (stopping) trajectory and verify the whole thing by reachability analysis. If verification passes, execute the intended motion; if not, fall back to the **last successfully verified failsafe**. Safety follows by induction, from the prior TUM line.

**3. Verify with set-based reachability, not distance heuristics.** Reachable occupancies of both robot and moving objects — including bounded measurement error, sensor delay, and velocity/acceleration limits on the objects — are computed with SaRA; a collision event is defined as their intersection being non-empty. The safety constraint is over *everything the object could do*, not where it is now.

**4. Design the policy so that braking is not itself OOD.** The subtlest part, and easy to miss: observations are **RGB images and joint angles only — no velocity**. If the policy could see its own speed, slowing it down would itself be an unseen state. **The safety mechanism imposes a requirement on how the policy is trained**, which is a kind of coupling the "bolt a filter on afterwards" framing does not admit.

### Constraints are ISO-grounded, with numbers

The two safety modes come straight from **ISO/TS 15066** — the collaborative-robot modes the wiki's [safety-standards page](../concepts/robotics/robot-safety-standards.md) names but has never seen instantiated on a learned policy:

- **SSM (speed and separation monitoring)** — coexistence, no contact permitted; if a collision is reachable, the robot must be at a **complete stop** (`T_safe = 0`).
- **PFL (power and force limiting)** — collaboration; contact allowed while kinetic energy stays below pain/injury thresholds.

| Task | Mode | Body part | Energy threshold |
|---|---|---|---|
| SORTING | SSM | hand | **0 J** (no contact) |
| HANDOVER | PFL | hand, constrained | **0.014 J** |
| HANDOVER | PFL | hand, unconstrained | **0.265 J** |
| **FEEDING** | PFL | **head (eye)** | **0.001 J** |

**0.001 J for a fork near an eye** is the most concrete safety number in this wiki, and the thresholds come from a surrogate-injury literature (Kirschner et al.), not from a tuned parameter.

## Key claims

**Simulation — robomimic (LIFT / CAN / SQUARE), 100 rollouts per cell, with a moving spherical obstacle added:**

| Method | Safe? | LIFT | CAN | SQUARE | Avg |
|---|:---:|---|---|---|---|
| Operational space controller (unsafe, Cartesian) | ✗ | 1.00 | 0.99 | 0.74 | **0.91** |
| Shield OFF (same joint-space pipeline, no failsafe) | ✗ | 0.92 | 0.83 | 0.34 | **0.70** |
| **Control barrier function** [Singletary et al. 2022] | ✓ | 0.11 | 0.00 | 0.00 | **0.04** |
| Single-action — SSM | ✓ | 0.97 | 0.26 | 0.00 | 0.41 |
| Single-action — PFL | ✓ | 0.94 | 0.33 | 0.04 | 0.44 |
| **PACS — SSM** | ✓ | 0.97 | 0.80 | 0.30 | **0.69** |
| **PACS — PFL** | ✓ | 0.93 | 0.85 | 0.38 | **0.72** |

- **The abstract's "68%" is 68 *percentage points*** — 0.72 versus 0.04 — not a relative improvement. The CBF baseline does not degrade; it **collapses**, scoring zero on two of three tasks.
- **PACS is free.** 0.72 (PFL) and 0.69 (SSM) against 0.70 for the same pipeline with the failsafe disabled. The paper's H2 (success within ±5% of unsafe) is met.
- **Action chunks matter: +28%** over treating each action in the chunk individually (0.72 vs 0.44). Reachability-based path-consistent filtering existed; making it work with **chunked** policies is what this paper adds.
- The honest read of the OFF-vs-Cartesian gap (0.70 vs 0.91, concentrated in SQUARE) is that **the inverse-kinematics translation to joint space costs more than the safety filter does** — a cost the paper attributes to accuracy loss, not safety.

**Hardware — Franka FR3, three HRI tasks, 30 rollouts each:**

| Task | Policy | Filter | Success | **Safe success** | Safety violations |
|---|---|---|---|---|---|
| SORTING | DP | OFF | 0.77 | **0.00** | 0.67 ± 0.12 |
| SORTING | DP | PACS | 0.80 | **0.80** | 0.00 |
| HANDOVER | DP | OFF | 1.00 | **0.00** | 0.32 ± 0.07 |
| HANDOVER | DP | PACS | 0.97 | **0.97** | 0.00 |
| HANDOVER | **[SmolVLA](../entities/smolvla.md)** | OFF | 0.77 | **0.00** | 0.41 ± 0.15 |
| HANDOVER | **SmolVLA** | PACS | 0.80 | **0.80** | 0.00 |
| FEEDING | DP | OFF | 0.63 | **0.00** | 0.85 ± 0.04 |
| FEEDING | DP | PACS | 0.63 | **0.63** | 0.00 |
| **Average** | | OFF | 0.79 | **0.00** | **0.56 ± 0.21** |
| **Average** | | PACS | **0.80** | **0.80** | **0.00** |

- **The zero column is the paper.** Unsafeguarded policies complete tasks at a respectable 0.79 and are in a constraint-violating state **56% of the time**, with *every* rollout containing a violation — so their **safe** success rate is **0.00**. Task success and safety are close to statistically independent here, which is the argument for an external mechanism in one table.
- **It works on a VLA, not just a diffusion policy.** [SmolVLA](../entities/smolvla.md) (flow matching) behaves the same as the U-Net DP under the filter. The method needs only *action chunks*, so it applies to the whole generative-policy family.
- **Hardware CBF comparison: 0.80 vs 0.43** on SORTING (+37 points), and the mechanism is *shown*, not asserted — end-effector traces plotted against the training distribution show the CBF pushing the robot into OOD regions from which the policy cannot recover, while PACS slows down without leaving the path.
- **Real-time, and cheaper than the baseline**: safety step **0.20 ms** (vs **0.64 ms** for the CBF), intended-trajectory recompute ~**5 ms**, deployment at **1 kHz**.
- **The filter made the robot faster.** Ablating the intended-trajectory module without a human present: task duration **25.2 s → 21.7 s (−14%)** and mean end-effector speed **+13%**, at identical success. Time-parameterizing the chunk under real kinematic limits beats streaming raw actions at 30 Hz.

## Caveats worth carrying

> [!warning] The CBF baseline is one particular CBF, and one of PACS's own authors wrote a better one
> The baseline is **Singletary et al. 2022** — a reactive, path-deviating collision-avoidance CBF. The paper cites [OSCBF](oscbf-paper.md) (Morton & **Pavone**) in the same related-work list, and **Pavone is a co-author of PACS**. So this is not one camp refuting another; it is the same senior author showing that the *reactive* class of filters, his own included, has a distribution-shift problem when the thing being filtered is a behavior-cloned policy.
>
> The two "consistency" ideas are also different, and both are needed: OSCBF's **task consistency** is about not injecting excess null-space motion *at a given instant*; PACS's **path consistency** is about not leaving the demonstration manifold *over a trajectory*. A task-consistent CBF still deviates from the path.

- **`n = 30` per hardware cell.** Per the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), 0.77-vs-0.80 differences at that sample size are noise. What survives is not the success comparison but the **0.00 vs 0.80 safe-success** and **0.56 vs 0.00 violation** columns, which are far too large to be sampling artifacts.
- **The FEEDING quantitative runs use a printed AI-generated face with a cut-out mouth**; the real human appears only in qualitative tests. Correct and conservative, and it means the headline assistive result is a mannequin study.
- **Perception is still assumed.** Object poses are measured with bounded error and objects are given bounded velocity/acceleration sets. The reachability machinery consumes a state estimate it does not produce — the same standing gap as [OSCBF](oscbf-paper.md) and the [TRI envelope](diffusion-policy-paper.md).
- **Dynamic obstacles are the design target; static clutter is future work** — *"handling (semi-)static obstacles via constraint-aware online replanning is an interesting avenue."* This is the mirror image of OSCBF, which handles hundreds of static collision pairs and never faces distribution shift. Neither method covers the other's case.
- Code release is promised on acceptance; not available at ingest.

## Entities mentioned

- [Marco Pavone](../entities/marco-pavone.md) — co-author, and now on **both sides** of the reactive-filter question.
- [Diffusion Policy](../entities/diffusion-policy.md) — the policy class being safeguarded (Chi et al., ref [3]).
- [SmolVLA](../entities/smolvla.md) — the second policy tested; flow matching, 50 demos, chunk length 50.
- [Franka Panda](../entities/franka-panda.md) — FR3 hardware.
- [Open X-Embodiment](../entities/open-x-embodiment.md) — cited for the scale of demonstration data collected without any safety mechanism in place, which is the paper's framing premise.
- Without pages: **Matthias Althoff** (TUM; the CORA/reachability lineage), **Angela Schoellig**, Ralf Römer, Julian Balletshofer, Jakob Thumm; **SaRA** (reachability tooling), **Ruckig** (jerk-limited trajectory generation), **CRISP** (compliant ROS 2 controllers for learned policies), **human-robot-gym**, **robomimic**.

## Concepts touched

- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — **new concept page from this ingest**; PACS is the source that makes the taxonomy necessary.
- [Operational space control](../concepts/robotics/operational-space-control.md) — the layer this sits in, and the page whose open question this closes.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — **ISO/TS 15066 SSM and PFL, numerically instantiated on a learned policy**; the wiki's first such instance.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the FEEDING task is robot-assisted feeding with a **0.001 J** head/eye energy limit.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the OOD-recovery failure is the mechanism behind every number here.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — "safe success" is a metric the wiki's evaluation coverage does not otherwise contain.

## Open questions

- **"Safe success" should probably be standard.** Every policy benchmark in this wiki reports task success; this paper shows a policy family that scores 0.79 on success and **0.00** on success-while-safe. If that gap is typical, most reported numbers describe behavior nobody would deploy.
- **Does path consistency generalize past braking?** Slowing along the intended path is the one intervention that provably keeps you on the manifold. Anything richer — detours, regrasps, recovery motions — reintroduces the OOD problem. Is braking the only safe edit to a behavior-cloned trajectory?
- **The runtime-monitoring cluster this cites is entirely uningested**: Agia, Sinha, Pavone & Bohg (CoRL 2025, failure modes of generative policies); Xu et al. (RSS 2025, **TRI** — detecting failures without failure data); Römer et al. (NeurIPS 2025, failure prediction at runtime). Three 2025 papers on *knowing when a generative policy is going wrong*, adjacent to this wiki's evaluation thread and absent from it.
- **Static-obstacle path consistency** is the obvious next result, and it is the case the deployed [TRI stack](diffusion-policy-paper.md) and [OSCBF](oscbf-paper.md) both cover.

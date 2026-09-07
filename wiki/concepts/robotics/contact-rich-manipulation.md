---
title: Contact-rich manipulation
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 6
tags: [contact-rich, manipulation, force-control, assembly, insertion, surface-interaction, physical-hri, deformable-objects, task-taxonomy]
---

# Contact-rich manipulation

## Definition

A task is **contact-rich** when its successful execution requires **dynamic and sustained physical contact** with the environment, where **motion and force are tightly coupled through contact constraints** ([Zhang et al. survey](../../sources/safe-learning-contact-rich-survey.md), §2.1).

The literature also calls this *physical interaction*, *manipulation in contact*, or *multi-contact* manipulation. The survey's definition is the sharpest available because of what it rules **out**:

| Not contact-rich | Why |
|---|---|
| Obstacle avoidance | contact may happen, but the task is achievable without it |
| Simple pick-and-place | contacts are **fixed** after the grasp closes; nothing further couples force to motion |
| Throwing, hitting, catching | contact is **momentary or sparse**, not extended — dynamic, but not contact-rich |
| Free-space reaching, most navigation | no purposeful contact at all |

| Contact-rich | Why |
|---|---|
| Peg-in-hole insertion, bolt threading, assembly | tight-tolerance force/motion coupling; jamming is the failure mode |
| Grinding, sanding, polishing, wiping, stirring, cutting | sustained surface contact with a force profile to hold |
| In-hand manipulation, multi-finger reorientation | the robot–object contact set **moves** during the task |
| Tool use where the tool touches the world | the grasped object becomes the contact interface |
| Massage, dressing, bathing, ultrasound scanning | sustained contact, with a human as the contacted body |

> [!warning] This boundary cuts through the middle of the wiki's benchmark coverage
> LIBERO, most of RoboCasa, and the large majority of tasks behind the [VLA success-rate tables](../../syntheses/platforms/vla-success-rate-audit.md) are **not contact-rich** under this definition — they are pick-and-place with a fixed post-grasp contact set. The consequence is not that those results are wrong; it is that **the generalist-policy literature has been evaluated almost entirely outside the regime where compliance, force control, and physical-safety guarantees decide the outcome.** A policy can be excellent at LIBERO and have never been tested on anything where a wrong force damages the workpiece.
>
> This is the manipulation-side analogue of the [policy-evaluation](robot-policy-evaluation.md) critique: the numbers are real, the regime they were measured in is narrower than the claims made from them.

## The four task families

The survey sorts ~400 papers into four non-exclusive categories, ordered by how much attention each gets:

**1. Assembly and insertion** — the most-studied class, and the oldest (studied in the control literature since well before learning). The classical **peg-in-hole** is a single securely-grasped peg into a single upright hole; the literature makes it harder along independent axes — noisy/limited sensing (uncertain peg and hole pose), varied peg shape and size, restricted control authority (rigid position control only), multi-peg simultaneous insertion, obstructed environments that also need path planning, bimanual insertion (both peg *and* hole move), multi-stage insertion of L-shaped parts, deformable holes, reverse insertion (ring-on-pole), and bolt threading. **Disassembly** inverts the goal — extract a tight-fit part, slide a bolt along a groove, remove batteries — and has *tighter* constraints, because jamming is easier on the way out.

Vision is structurally weak here: **occlusion at the moment of contact is maximal**, which is why this class is force-first.

**2. Surface interaction** — continuous purposeful contact with a surface, maintaining a force profile while tracking a trajectory. Three sub-kinds:
- **surface-altering** — grinding, sanding: geometry is removed;
- **non-altering** — wiping, polishing: no permanent change;
- **particle interaction** — stirring granular media, scooping soft tissue: the tool goes *through* the surface.

Difficulty scales with surface curvature, trajectory complexity, and tool vibration (a powered polisher injects its own disturbance). Deformable and elastic surfaces (sponge) are called out as under-explored. A distinct sub-case is **surface exploration** — blind maze navigation by touch — where contact is the *sensing* channel rather than the goal.

The distinguishing feature versus object manipulation: **the object is supposed to stay put.** Wiping an *unconstrained* object such as a vase therefore requires bimanual coordination just to hold it steady.

**3. Object manipulation** — long-term dynamic contact with a moved object, split **prehensile** (grasped: at least two contacts; simple grippers permit only pick-and-place or tool use, bimanual and multi-fingered hands permit real reorientation) versus **non-prehensile** (pushing, sliding, pivoting: one contact, simpler hardware, much less control authority — so safety becomes a question about *where the object goes*, e.g. pushing through a narrow gap or over a bridge with a fall risk). Also sorted by object nature: **constrained/articulated** (doors, drawers, levers — strict kinematic constraints that generate large forces if the controller is stiff) and **deformable** (under-explored; sensing and modelling are both hard).

**4. Physical HRI** — contact *with a person*, as distinct from human-robot coexistence where the safety goal is to avoid the human. Traditionally the robot is passive and follows human intent through compliance. The safety-critical cases are the inverse: **the robot is active and the human is passive** — feeding, dressing, bathing, ultrasound scanning, massage. See [collaborative robots](collaborative-robots.md) and [assistive robotics](assistive-robotics.md).

## Why this class is hard, specifically

- **Discontinuous dynamics.** Contact modes (free / sticking / sliding / impact) switch, and the dynamics are different in each. Standard Lyapunov theory does not directly apply to hybrid systems; multiple Lyapunov functions may be needed ([safety certificates](safety-certificates.md)).
- **Force constraints are high relative degree.** They depend on higher derivatives of the state, which is the case control-barrier-function design handles worst.
- **Models are inaccurate exactly where it matters.** Friction (stick-slip), material deformation, small-clearance contact, and compliant components are the named failure list for simulators — see [sim-to-real transfer](../learning/sim-to-real-transfer.md).
- **Exploration is physically destructive.** Unlike a game, a bad rollout wears a tool, jams a part, scars a surface, or injures somebody. This is why [safe RL](../learning/safe-reinforcement-learning.md)'s exploration branch exists as a distinct problem.
- **Vision degrades at the moment of contact** — occlusion by the manipulator and the workpiece, at exactly the instant precision matters.

## The data problem, which is structural

> Unlike the vast text and image corpora scraped from the Internet to train LLMs and VLAs, **physical interaction data — specifically high-fidelity contact forces, torques, and safety-critical failure modes — cannot be obtained from the web.**
> — [Zhang et al.](../../sources/safe-learning-contact-rich-survey.md), §3.4

The survey's data pyramid puts internet and shared datasets at the base (abundant, indirect), simulation in the middle (contact under controllable but imperfect dynamics), and **real contact data at the apex** — scarce, irreplaceable, ordered internally from execution logs up to explicit failure and near-miss episodes.

Public datasets are reported to rarely contain high-frequency wrench traces aligned with failure annotations, near-miss episodes, or semantic safety labels (forbidden regions, fragile surfaces) — and those are precisely the three inputs a layered safety architecture consumes.

> [!note] The strongest available bound on video pretraining
> This wiki's [world-model evaluation](../world-models/world-model-evaluation.md) and [synthetic data flywheel](../learning/synthetic-data-flywheel.md) threads keep asking what video-scale pretraining cannot reach. **Force is a concrete answer.** A wrench is not recoverable from pixels, so no quantity of internet video and no generative video model trained on it supplies the signal this task class is defined by. Whether a *learned observer* estimating wrench from proprioception closes enough of that gap — and whether a predicted wrench is admissible in a safety argument — is open.

> [!warning] The field's flagship VLA-safety result is not in this regime either
> [SafeVLA](../../sources/safevla-paper.md) (NeurIPS 2025 Spotlight) is the most-cited external anchor of the [contact-rich survey](../../sources/safe-learning-contact-rich-survey.md)'s foundation-model chapter. Its tasks are **object navigation, pick-up, and fetch** in AI2-THOR, and its five safety predicates are all **discrete collision or interaction events** — corners, blind spots, fragile collections, critical points, dangerous equipment. There is no force, no wrench, no compliance anywhere in it.
>
> By the definition at the top of this page, none of those tasks is contact-rich. So the survey's own headline chapter rests on work from a different regime with a different hazard model — and, taken together, the two papers make the gap concrete rather than rhetorical: **the safe-VLA literature measures collisions because collisions have a simulator oracle and forces do not.**

## The first deployment, and it does not look like the literature

Everything above is drawn from a survey of research. [FLUX-mimic](../../sources/flux-3-launch.md) is a **production deployment**, at **Audi**, on this task class:

> kitting parts into structured trays, **inserting electronic control units into tight-fitting fixtures**, assembling components together, and **handling soft, flexible materials like seals and cables that conventional automation has never been able to touch.**

Tight-tolerance insertion is family 1 above — the most-studied class. Seals and cables are the **deformable** corner of family 3, which the survey calls under-explored. So the industrial frontier landed on the hardest two categories at once.

**And the architecture is not what the literature predicts.** No impedance control, no force envelope, no compliant action space is described: camera → **video-prediction backbone** → intermediate features → lightweight action decoder → robot, at a **101 ms** system reaction time. Neither source post mentions force/torque sensing, tactile sensing or compliance anywhere.

> [!warning] Narrowed, not closed — and the missing document is now specific
> **The sensing question is answered for the published system.** [mimic-video](../../sources/mimic-video-paper.md) states the observation as `oₜ = [images, language, proprioceptive state]`, with a real rig of *"a global workspace view, four wrist cameras, and full proprioception."* **No force, no tactile, no impedance, no compliance** — on a platform with 16-DoF dexterous hands.
>
> **But that paper never does a contact-rich task.** Its real-world evaluations are pick-handover-place and pick-stow; the Audi insertion and seal/cable work appears only in a vendor blog, on a **different backbone**, with **no publication**. So the published record contains a vision-and-proprioception system that has not been shown doing this task class, plus a marketing claim that it does.
>
> The honest state: *"force is not recoverable from pixels"* still stands as written, and whether it **bounds acting or only measuring** is untested either way.
>
> **And there is a cheap experiment that would settle it.** mimic-video's oracle study finds that conditioning the action decoder on *ground-truth future video latents* yields **near-perfect success** — *"control effectively reduces to visual prediction."* On pick-and-place. Run that same oracle study on a **tight-clearance insertion** task: if oracle video still gives near-perfect control, the decisive information really is visible and the force-first consensus is over-stated; if it does not, the gap is exactly the part of contact that pixels never had.

The Audi framing also names the economics, and it is not about capability: these tasks *"have stayed manual, largely for economic reasons: the **variant diversity** of premium production makes conventionally programmed robot cells too costly to re-engineer for each case."* The competitor to a learned policy here is not a better robot cell — it is a human who needs no re-engineering.

## Related concepts

- [Impedance and admittance control](impedance-control.md) — the controller family this task class is built on.
- [Safety certificates](safety-certificates.md) — what "provably safe" means here, and why contact is the hard case for each certificate family.
- [Safe reinforcement learning](../learning/safe-reinforcement-learning.md) — learning in this regime without breaking things.
- [Tactile sensing](tactile-sensing.md) — the modality that sees contact directly.
- [Safety filters for learned policies](safety-filters.md) — runtime enforcement; note that its measured results come from tasks that are *not* contact-rich by the definition above.
- [Dexterous tool manipulation](dexterous-tool-manipulation.md) — the in-hand and tool-use corner of the third family.
- [Robot safety standards](robot-safety-standards.md) — ISO 10218 / ISO/TS 15066 govern the pHRI family.
- [VLA models](../learning/vla-models.md) — the generalist policies that have mostly not been evaluated here.

## Current state

Well-developed as a *control* problem and thin as a *learning* problem. Force/torque-conditioned policies with learned compliance dominate the literature ([Zhang et al.](../../sources/safe-learning-contact-rich-survey.md) Table 1 lists ~60 force/torque works against **four** language-conditioned ones), assembly and insertion absorb most of the attention, and deformable objects, multi-stage processes, tool use, and human-adjacent tasks are all named as under-covered. There is **no standardized contact-force evaluation protocol** — the survey's first-listed future direction, and the most concrete unclaimed piece of work in the area.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — the definition, the exclusions, the four families, and the data argument.
- [SafeVLA](../../sources/safevla-paper.md) — the counter-instance: the flagship safe-VLA result, working outside this task class on a collision-based cost.
- [FLUX 3 and FLUX-mimic](../../sources/flux-3-launch.md) — **the first claimed deployment in this regime**: ECU insertion and seal/cable handling at Audi, from a video backbone with no force sensing described.
- [mimic-video](../../sources/mimic-video-paper.md) — the architecture's paper: vision + proprioception only, and **no contact-rich task in its own evaluations**. Also the source of the *oracle* experiment that would settle the question.

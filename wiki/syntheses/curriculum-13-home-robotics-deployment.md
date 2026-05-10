---
title: Curriculum Module 13 — Home robotics deployment reality
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-13, home-robotics, deployment, stretch, par, eup, assistive-robotics, behavior-1k, rum, ok-robot, lewm-on-stretch]
prereqs: [curriculum-06, curriculum-09]
status: draft
---

> [!note] Curriculum context
> This is **Module 13** of the [Robot-learning curriculum](robot-learning-curriculum.md). It can be read after [Module 6](curriculum-06-imitation-learning.md) (BC) and [Module 9](curriculum-09-vla.md) (VLA), but lands harder if you've also done Tier 4 ([Modules 10](curriculum-10-world-models.md) → [11](curriculum-11-jepa-deep.md) → [12](curriculum-12-lewm-deep-dive.md)).
>
> Module 13 places everything from Modules 6–12 against **deployment reality**. The point is to be honest about what the techniques in this curriculum can plausibly do in a real home in 2026, and what they can't.
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there. This module leans heavily on existing wiki syntheses and serves mostly as a curriculum-shaped framing of work already done — pointers below.
>
> Relevant pre-existing syntheses (read these *with* this module, not after):
> - [Assistive robotics — R&D landscape](assistive-robotics-research-landscape.md)
> - [Stretch as the de-facto assistive-robotics platform](stretch-as-assistive-platform.md)
> - [Levels of autonomy in assistive robotics](levels-of-autonomy-in-assistive-robotics.md)
> - [Long-term in-home robot deployments](long-term-in-home-robot-deployments.md)
> - [Underserved PAR domains — dressing, bathing, medication](underserved-par-domains.md)
> - [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md)
> - [DINO-WM-on-Stretch experiment plan](dino-wm-on-stretch-experiment.md)

## What this module is

The deployment-reality module. Module 13 names what the curriculum-bound technical work has actually moved (and not moved) in real-home robotics, identifies the barriers LeWM-class techniques could plausibly attack vs the ones they can't, and ends by pointing at the single highest-value experiment a wiki-bound researcher could run with current artifacts.

By the end of the module you should be able to:

1. Recite the **89.4% vs 12.4% gap** ([Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md)) between [RLBench](https://github.com/stepjam/RLBench) and [BEHAVIOR-1K](../glossary.md#behavior-1k) success rates and explain why the gap is meaningful.
2. Name [Stretch](../entities/stretch.md) as the de-facto assistive-robotics research platform and articulate the eight features that cause every wiki-relevant in-home deployment to converge on it ([synthesis](stretch-as-assistive-platform.md)).
3. Distinguish [Physically Assistive Robotics (PAR)](../glossary.md#par) and [End-User Programming (EUP)](../glossary.md#eup) and explain the **autonomy-preference finding** ([levels-of-autonomy synthesis](levels-of-autonomy-in-assistive-robotics.md)).
4. Identify the **three underserved PAR domains** (dressing, bathing, medication) and name the most-tractable researcher target among them.
5. Place LeWM-class techniques inside this deployment reality — name two barriers they plausibly move (data efficiency, planning speed) and three they don't (whole-body manipulation, dressing/bathing, real-world robustness).
6. Pick **the one experiment most worth running** out of the [LeWM-on-Stretch](lewm-on-stretch-feasibility.md) and [DINO-WM-on-Stretch](dino-wm-on-stretch-experiment.md) plans and defend the choice in one paragraph.

## The 89.4% / 12.4% gap

The curriculum's most concrete deployment-reality datum, from the [Stanford HAI AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md):

- **89.4%** — best success rate on [RLBench](https://github.com/stepjam/RLBench) (curated tabletop manipulation with controlled lighting, fixed cameras, scripted resets).
- **12.4%** — best success rate on [BEHAVIOR-1K](../glossary.md#behavior-1k) (Stanford household-task benchmark — cooking, cleaning, putting items away).

That's a 7× gap on tasks that look superficially similar from outside the field. The interpretation: **the field has solved tabletop manipulation in laboratory conditions; it has not solved household tasks in any meaningful sense.**

What changes between RLBench and BEHAVIOR-1K:

- **Scene clutter** — household scenes contain unmodelled objects, unmodelled textures, unmodelled lighting.
- **Long horizons** — household tasks are dozens-of-minutes; RLBench tasks are seconds.
- **Robust sub-tasks** — opening a door requires *robust* opening across hinge styles; tabletop pick-and-place lets you re-try a single grasp.
- **Object diversity** — household objects vary in mass, friction, deformability, fragility.

Every other section of this module exists to help you understand which barriers from this list your favorite curriculum technique can plausibly move.

## [Stretch](../entities/stretch.md) as the de-facto research platform

[Hello Robot](../entities/hello-robot.md)'s Stretch is the platform every wiki-relevant in-home deployment uses. Why — eight features compounding (per the [Stretch-as-platform synthesis](stretch-as-assistive-platform.md)):

1. **Mobile manipulation in one chassis** — wheels + a vertically-extending arm.
2. **Reasonable price** — ~$25K, an order of magnitude cheaper than research humanoids.
3. **Open Python API** — ROS 2 + pure-Python control; not locked to a closed SDK.
4. **Quiet enough for homes** — ~22 dB; doesn't disturb residents during long deployments.
5. **Safe enough** — low payloads, gentle motion profiles; the user doesn't have to leave the room.
6. **MuJoCo / Gazebo simulators** ship with the official docs.
7. **`stretch_ai` LLM-agent stack** maintained by the manufacturer.
8. **Active research community** — UW HCR Lab + NYU + Hello Robot publish co-design work; [Henry Evans](https://en.wikipedia.org/wiki/Henry_Evans_(quadriplegic)) summer deployments are the canonical longitudinal record.

The **convergence** matters: every long-running in-home deployment in the wiki is on Stretch. That makes "could LeWM run on Stretch?" an actually-answerable question rather than a hypothetical. ([LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md), [DINO-WM-on-Stretch experiment](dino-wm-on-stretch-experiment.md), and the [LeWM hello-world scope](lewm-hello-world-project-scope.md) are concrete artifacts of this.)

What Stretch *doesn't* solve: bimanual manipulation, fine dexterous control of fingers, whole-body motion (it's a single-arm wheeled platform, not a humanoid). Those constraints are real and will set up the LeWM-class-fits-here-doesn't-fit-there discussion.

## The "real-data" path — [RUM](../entities/robot-utility-models.md) + [OK-Robot](../entities/ok-robot.md)

The most concrete success stories in this curriculum's deployment scope. Both NYU/Meta. Both on Stretch.

- **[Robot Utility Models](../entities/robot-utility-models.md)** (Etukuru et al., 2024) — five zero-shot generalist BC policies. Trained on diverse demos via the **Stick-v2** hand-held data collector (UMI-line). Cross-environment generalization headline: ~90% success on novel environments **without** language conditioning. Methodological lesson: **data diversity > data quantity.**
- **[OK-Robot](../entities/ok-robot.md)** (NYU, 2024) — zero-shot pick-and-drop in **10 NYC homes**; **58.5%** success rate. Combines a VLM + classical perception/manipulation primitives. Zero-shot on environments the team had never seen.

These are the wiki's strongest published "robots actually doing things in homes" data points. They don't use LeWM, JEPA, or world models. They're BC + cross-environment data + classical pipeline. **The strongest 2026 home-robotics result is BC, not WM.** That's a real fact worth holding while reading the rest of this module.

The implicit research bet across the JEPA / WM lineage of this curriculum: **maybe** WM-class techniques can do better, **eventually**, on tasks BC handles well-but-not-perfectly *and* on long-horizon tasks BC fails on. That bet is not yet vindicated empirically. Module 13 is honest about this; the rest of the module discusses where the bet might pay off.

## Physically Assistive Robotics (PAR) and what users actually need

The user-side framing. From the [Nanavati et al. 2024 systematic review](../sources/nanavati2024-physically-assistive-robots-review.md) of the [PAR](../glossary.md#par) literature: **1,981 papers screened, 87 included**. Three themes; nine sub-categories. The relevant headline findings (per the [assistive-robotics R&D landscape synthesis](assistive-robotics-research-landscape.md)):

- **Three underserved domains** receive disproportionately less research attention than their importance to disabled users would justify: **dressing, bathing, medication management** (per the [Underserved PAR domains synthesis](underserved-par-domains.md)).
- **Half of PAR papers involve no PwD (Person with Disability)** — the user community is systematically excluded from the design loop.
- **Henry Evans summer deployments** (with [Maya Cakmak](../entities/maya-cakmak.md)'s [HCR Lab](../entities/hcrlab.md), UW) are the longest published longitudinal deployment record in the wiki — multi-week with a quadriplegic user using Stretch.
- **The autonomy-preference finding** ([Yang et al. 2025](../sources/yang2025-sense-of-agency.md)): EUP-style user-customizable robots **preserve sense of agency even when acting autonomously.** Users prefer high-control on high-risk tasks; autonomous behaviors that respect this preference are usable.

The [levels-of-autonomy synthesis](levels-of-autonomy-in-assistive-robotics.md) decomposes "autonomy" into three orthogonal axes (execution, programming, intent inference). The curriculum-relevant lesson: the question isn't "should the robot be autonomous?" — it's "**what kind of autonomy on what task at what user-control level?**" Different answers for cooking vs feeding vs dressing.

## End-User Programming ([EUP](../glossary.md#eup))

[End-user programming](../concepts/end-user-robot-programming.md) — letting non-experts (the disabled user, a family member, a care assistant) **customize** robot behavior. The HCR Lab has been the most consistent wiki-cited EUP research thread (8 sources from the lab's publication record).

Why it matters here: **EUP is the natural home for any policy-learning technique that's data-efficient enough to be retrained with a few user demonstrations.** A LeWM-class JEPA on a small action dataset is, in principle, a candidate substrate for an EUP-style "show the robot once, it adapts" loop. Whether that's empirically true at LeWM's current scale is an open research question; [Module 14](robot-learning-curriculum.md)'s capstone phase B is the experiment.

## Underserved PAR domains — the most-tractable target

Per the [underserved-domains synthesis](underserved-par-domains.md), three under-researched areas: dressing, bathing, medication management. Sub-capability decomposition for each, plus a recommended target:

| Domain | Why it's underserved | Most-tractable researcher target |
| --- | --- | --- |
| **Dressing** | Multi-step; deformable; safety-critical; bimanual | not within current single-arm-Stretch scope |
| **Bathing** | Wet environments; multi-region; very safety-critical | requires custom hardware beyond research-Stretch scope |
| **Medication management** | Sub-tasks decompose: **fetching** vs counting vs dispensing | **medication-fetcher** is most tractable |

The curriculum-relevant target is the **medication fetcher** — a Stretch can navigate to a pill bottle, pick it up, and bring it to a person who self-administers. This decomposes to navigate + pick + carry + place — sub-tasks that are individually solved (RUM does pick-and-drop) and the hard part is *the integration plus reliability*. A LeWM-class WM that lets the robot **plan** a multi-room navigation + manipulation sequence, then re-plan when the world drifts, is plausibly useful here. (See [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) for the concrete sketch.)

## Where LeWM-class techniques fit

Curriculum-bound honesty: what LeWM-class JEPAs can plausibly move in this deployment landscape, and what they can't.

### Plausibly move

- **Data efficiency.** JEPA's two-stage recipe (action-free pretraining + small-action post-training) maps onto the home-robotics data scarcity story. A robot doing tasks in a new home has near-zero teleop demos for *that home*; pretraining on cross-environment video + small per-home fine-tuning is a credible workflow.
- **Planning speed.** [LeWM's 48× speedup over DINO-WM](../sources/leworldmodel-paper.md) puts latent-space MPC in range of real-time on consumer hardware. That makes WM-MPC a credible on-robot algorithm, not just a research demonstration.
- **Modeling action consequences for safety / pre-emption.** A WM that can predict "does this action sequence collide with the user?" is potentially useful for the autonomy-preference finding's high-risk tasks. (No published WM-on-Stretch result yet; this is bet, not vindication.)

### Plausibly does *not* move

- **Whole-body humanoid manipulation.** Stretch is wheeled + single-arm. LeWM doesn't change that. Bimanual / dressing / bathing remain hardware-bound problems.
- **Long-horizon multi-stage tasks.** WM rollouts compound error past the predictor's horizon — see [Module 10](curriculum-10-world-models.md). A "make breakfast" task is way past any current WM's horizon. BC + classical pipelines (the OK-Robot recipe) currently scale better here.
- **Robustness to lighting / object diversity / unmodelled scene clutter.** A small task-shaped end-to-end JEPA is *less* robust to these than a frozen-DINOv2 encoder ([DINO-WM](../entities/dino-wm.md)) that inherits broad pretraining. The Module 11 LeWM-vs-V-JEPA-2 comparison applies here too.

The honest read: **LeWM-class techniques are a candidate ingredient in future home-robotics stacks, not a turnkey solution.** The interesting question is *which deployment problem benefits most from a small fast end-to-end on-robot WM*. The likeliest candidates are tasks where (a) data is scarce and similar across users, (b) latency budgets are tight, and (c) a small task-shaped encoder can match the task's intrinsic dimensionality — i.e. things like the medication-fetcher above, not "make breakfast."

## Anchor exercise

> **Read [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) and [DINO-WM-on-Stretch experiment plan](dino-wm-on-stretch-experiment.md). State the one experiment most worth running.**

The anchor exercise is curated to make you take a real position. Both syntheses sketch experiments that could plausibly be run with current artifacts — RUM's open dataset for action-conditioning data, a single Stretch (loaned or borrowed), and a researcher with a few months. They differ on which world-model variant gets the trial.

The argument-for-LeWM (lower scale; end-to-end task-shaped; novel SIGReg validation):

- Smaller model fits on Stretch's onboard hardware budget.
- Closer to the [hello-world scope](lewm-hello-world-project-scope.md); lower setup cost.
- A real-robot LeWM result would be a first-of-its-kind validation of SIGReg outside the four toy benches.

The argument-for-DINO-WM (frozen encoder; less risky; better-validated on lightweight benches):

- Frozen DINOv2 is robustness-from-pretraining; it transfers off-the-shelf to Stretch's RGB camera.
- The collapse failure mode is impossible by construction (no encoder training).
- Fewer engineering surprises; you can finish phase A faster and iterate.

Pick a side and write a paragraph. The exercise's *point* is that the curriculum doesn't tell you which is right — the wiki has both sketched, both are reasonable, and the choice depends on what you're trying to learn from the experiment. (My personal lean: **DINO-WM-on-Stretch is the lower-risk first attempt; LeWM-on-Stretch is the more interesting second attempt.** But that's an opinion.)

[Module 14](robot-learning-curriculum.md)'s capstone is, in part, "actually run that experiment." Phase A is paper-and-sim only; phase B is the real Stretch.

## Recommended reading

In order:

1. **[Stanford HAI AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)** — for the 89.4 / 12.4 datum.
2. **[Stretch as the de-facto assistive-robotics platform](stretch-as-assistive-platform.md)** — why every deployment converges here.
3. **[Long-term in-home robot deployments](long-term-in-home-robot-deployments.md)** — what longitudinal records exist; what's missing.
4. **[Assistive robotics — R&D landscape](assistive-robotics-research-landscape.md)** — seven blocking problems, timeline, active researchers, JEPA-fit analysis.
5. **[Robot Utility Models paper](../sources/robot-utility-models-paper.md)** — the strongest published home-robotics-on-Stretch result.
6. **[Nanavati et al. 2024 PAR review](../sources/nanavati2024-physically-assistive-robots-review.md)** — the user-side state of the field.
7. **[Yang et al. 2025 — Sense of agency](../sources/yang2025-sense-of-agency.md)** — the autonomy-preference finding.
8. **[Levels of autonomy in assistive robotics](levels-of-autonomy-in-assistive-robotics.md)** — three orthogonal autonomy axes.
9. **[Underserved PAR domains](underserved-par-domains.md)** — dressing, bathing, medication, and the medication-fetcher target.
10. **[LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md)** + **[DINO-WM-on-Stretch experiment plan](dino-wm-on-stretch-experiment.md)** — concrete experiment plans for the anchor exercise.

## What you should now be able to do

- Recite the 89.4 / 12.4 gap and locate any new home-robotics result on the spectrum between them.
- Read a paper claiming "household manipulation" capability and quickly classify whether it's lab-controlled (RLBench-class) or scene-realistic (BEHAVIOR-1K-class), and weight the claim accordingly.
- Argue for or against using LeWM-class WMs on a particular deployment task by checking: data scarcity, latency budget, intrinsic task dimensionality, robustness requirements.
- Recognize when a "home robotics" claim is actually a tabletop-manipulation claim relabeled, and when it's the real thing.
- Defend a specific experiment (LeWM-on-Stretch vs DINO-WM-on-Stretch) given current wiki artifacts and what you're trying to learn.

## Hand-off to Module 14

[Module 14](robot-learning-curriculum.md) is the **capstone**:

- **Phase A (paper / sim — required):** reproduce LeWM PushT from scratch ([hello-world scope](lewm-hello-world-project-scope.md)); produce a written experiment-design memo for the smallest credible LeWM-on-Stretch or DINO-WM-on-Stretch experiment.
- **Phase B (hardware — when Stretch is available):** execute the phase-A memo on a real Stretch. Use [RUM](../entities/robot-utility-models.md)'s open dataset to bootstrap the action-conditioning data. Compare against a Diffusion Policy baseline.

Module 13's anchor exercise (pick the one experiment most worth running) feeds Module 14's phase-A memo directly. The choice you defend in Module 13 *is* the experiment you scope in Module 14.

## Related curriculum modules

- **[Module 6 — Imitation learning](curriculum-06-imitation-learning.md)** — RUM + OK-Robot are BC-line successes.
- **[Module 7 — BC lineage](curriculum-07-bc-lineage-pusht.md)** — the architectural lineage RUM and OK-Robot ride on.
- **[Module 9 — VLA](curriculum-09-vla.md)** — the alternative paradigm for generalist home policies.
- **[Module 12 — LeWM deep-dive](curriculum-12-lewm-deep-dive.md)** — LeWM-on-Stretch feasibility sits on top of this module's content.
- **[Module 14 — Capstone](robot-learning-curriculum.md)** — direct successor; the experiment-design memo and phase-B execution.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- **A LeWM-on-Stretch (or DINO-WM-on-Stretch) result.** No such result exists in the wiki; both are scoped but unrun. Module 14 phase B is where this becomes a real experiment.
- **A BEHAVIOR-1K result with WM-class techniques.** Currently no published WM result on this benchmark; would be the cleanest "did WMs move the gap?" datum.
- **Cross-paradigm comparison on a real Stretch deployment.** Direct head-to-head: RUM (BC) vs DINO-WM-MPC (frozen WM) vs LeWM-MPC (end-to-end WM) on the same task. Doesn't exist; would be informative.
- **Long-horizon WM evaluation.** Most WM papers evaluate at horizons 5–20. What does WM performance look like at horizons of *minutes* (a household task)? Wiki's [generative-video vs JEPA synthesis](generative-video-vs-jepa-world-models.md) flags this gap.

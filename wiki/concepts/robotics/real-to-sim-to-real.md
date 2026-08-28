---
title: Real-to-sim-to-real (R2S2R)
type: concept
created: 2026-08-26
updated: 2026-08-26
sources: 4
tags: [real-to-sim, sim-to-real, r2s2r, simulation, robot-policy-evaluation, world-model, gaussian-splatting, deformable]
---

**Real-to-sim-to-real (R2S2R)** — reconstruct a *specific real task* as an interactive simulation aligned with reality in both appearance and dynamics, use that world to train and evaluate policies at scale, then return to hardware; real outcomes feed back to improve the world. The name comes from [World Labs / SceniX](../../sources/world-labs-r2s2r.md), but the pattern is older and the wiki already held both halves separately.

## Why it is a distinct thing from sim-to-real

Classical [sim-to-real](../learning/sim-to-real-transfer.md) starts with a **hand-authored** simulator and asks how to close the gap to reality — domain randomization, domain adaptation, better rendering. R2S2R inverts the starting point: the real task comes first and the simulator is *constructed from it*, per task, from captures of the robot, sensors, environment, objects and demonstrations.

That changes what the "gap" even is. A hand-authored simulator is **inspectable** — you can read the wrong friction coefficient. A reconstructed one is fit to observations, so alignment becomes an empirical claim requiring its own validation protocol rather than a modeling assumption.

| | Classical sim-to-real | R2S2R |
|---|---|---|
| Simulator origin | Authored ahead of time, general-purpose | Reconstructed from captures of one real task |
| Gap closed by | Randomization / adaptation over a known model | Fitting appearance *and* dynamics to the real task |
| Validation | Policy transfers or doesn't | **Matched open-loop rollouts** in sim and real, compared directly |
| Reuse | One simulator, many tasks | One reconstructed world per task, reused across policies and embodiments |
| Failure mode | Modeling error you can read | Reconstruction error you cannot |

## The two halves

**Real-to-sim.** Capture the physical setup and rebuild it as an interactive world preserving "both what the robot perceives and the physical interactions that determine success or failure." World Labs claims a *generative* world-modeling system for this rather than photogrammetry plus a physics engine, combining representations per task because real measurements are dirty — "object shape, weight, and friction may be uncertain; cameras and robots can differ from their specifications; and cables, packaging, and tools deform in ways that simple models cannot fully capture" ([R2S2R](../../sources/world-labs-r2s2r.md)).

**Sim-to-real.** Systematically vary appearance, object configuration, clutter, physics, robot state, speed and camera viewpoint to manufacture the coverage hardware cannot produce. Two things simulation supplies that hardware cannot at any budget:

- **No resets.** Policies can "repeatedly and intentionally encounter difficult states and learn from both successes and failures without resetting a physical environment after every trial."
- **Counterfactual supervision.** Precise object states, contacts, visibility, forces, and **"outcomes under alternative actions"** — the last is unobtainable on real hardware by construction, since you only ever get one branch.

## Validation: matched open-loop execution

The alignment test worth remembering: run the **same action sequence** in sim and reality **open-loop**, and compare observations, object responses and outcomes. Open loop is the honest choice — a closed-loop policy corrects for dynamics error as it goes, which hides exactly the discrepancy being measured.

## The two things customers actually buy

From the [a16z conversation](../../sources/a16z-worldlabs-scenix-conversation.md), which is the only source that states the value proposition in operational terms:

**Reliability** — "you need data to provide **systematic coverage of all the state space** and the variations that robots might encounter." Simulation permits systematic randomization of "lighting, frictions, geometries, object types and all different kinds of physical parameters," and — crucially for a claim of coverage — lets you say *"exactly what distribution you have covered."*

**Efficiency, and this one is about speed, not cost:**

> "If you look at many of the teleoperation devices — imagining all the exoskeletons you are using — **you're actually collecting the data at a speed that is slower than a human actually doing the task.** But for many of our clients, human speed to them is not good enough. **They want faster than human speeds.** For the robot to move faster, it's not as simple as just driving the robot faster, **because the gravity doesn't change.** But in simulation, you can do systematic speed-up of the robot's behaviors to train the robot such that it considers all the dynamics changes of the environment."

> [!note] A teleoperation limit the wiki had not recorded
> Every other source here treats teleop's problem as **cost and scale** — operators, hours, hardware. This adds a *ceiling*: demonstrations are collected **slower than a human doing the task by hand**, so a policy trained on them inherits sub-human speed, and customers deploying against a labor baseline need super-human speed. You cannot simply replay the demonstrations faster, because gravity does not rescale with playback — the contact dynamics change. Simulation is the only place the speed-up can be done *with* the dynamics. That is an argument for simulation that is independent of data volume, coverage, or cost.

## The fidelity question is open, and its authors say so

Pressed for a formal statement of how aligned is aligned enough, Yunzhu Li declines and argues by analogy: quadrupeds and bipeds "can walk on snow, they can walk on bushes. But you don't need a simulator that can simulate all the bushes and snow very precisely. You need a simulation that **captures the essential structure of the problem** and does a whole different kind of randomizations inside the digital environment."

He then names the open problem outright: *"what is the level of fidelity we need to model the massive worlds… such that we'll be able to transfer the robotic systems trained in the simulated environment back into the real scenarios."* Worth holding against the [R2S2R results post](../../sources/world-labs-r2s2r.md), whose demos implicitly claim to have settled this for their task set.

## Simulation does not replace real data — per its own vendors

> [!warning] The blog post oversells relative to what its authors say out loud
> ["Zero real-world training data"](../../sources/world-labs-r2s2r.md) reads as a claim that reconstructed worlds substitute for real collection. In [conversation](../../sources/a16z-worldlabs-scenix-conversation.md), both principals say the opposite. Asked about [Sergey Levine](../../entities/sergey-levine.md)'s objection that simulation always deviates and real collection is essential, Yunzhu Li: **"They don't contradict with each other."** The stated design is a *shifting mixture* — "it doesn't necessarily have to be pure physics; it can be a combination between both physics and also learning," physics-weighted early "to make sure we have the right consistency and right structure," moving "towards more learning-based modeling" as real data accumulates through deployment and customer collaboration.
>
> So R2S2R is a **data flywheel with a physics prior**, not a replacement for real data. That is a more defensible claim than the blog post makes, and it is the one to record.

**The counterfactual argument** is the strongest defense available for learned simulation, and notably it is orthogonal to fidelity — [Fei-Fei Li](../../entities/fei-fei-li.md): *"there's a very important role simulation plays that real-world data doesn't play, which is counterfactual reasoning — you play out events that haven't happened or cannot happen… and while you play it out, you learn how to act in it."* Even an imperfect simulator lets you explore branches that never occurred; whether those branches are *informative* is the real question, and no source here answers it. Her precedent: **Waymo "use billions of hours of simulation" and is "more simulation-heavy than just real-world-data heavy"** — with her own caveat that "cars are the simplest kind of robots."

## The evaluation claim, and the standard it sets

R2S2R's more consequential use is not training but **screening**. The stated bar is deliberately ordinal:

> "A useful simulation need not match real-world success rates exactly. It must support the same decisions as reality: identify where policies succeed and fail, **rank** which policies are better, and predict whether improvements during training will carry over to hardware." ([R2S2R](../../sources/world-labs-r2s2r.md))

> [!note] Four independent arrivals at ranking-not-magnitude
> This is the same trade the wiki recorded from three unrelated directions before R2S2R existed. [RoboArena](../../sources/roboarena-paper.md) abandons absolute rates for pairwise preference and gets Pearson **≈0.95** against an oracle ranking versus **≈0.60** for centralized success-rate evaluation. The [Veo world-simulator harness](../../sources/veo-robotics-policy-evaluation-paper.md) reports **0.88** correlation with absolute rates running low. [WorldArena](../../sources/worldarena-paper.md) reports **r = 0.986** for [Ctrl-World](../../entities/ctrl-world.md) with absolute rates *inflated* by "partial overfitting to successful trajectories." A vendor with every incentive to claim fidelity instead pre-emptively disclaims it and defends ordinal validity — which is the strongest available evidence that **ordinal is what simulated evaluation actually delivers**, and that asking it for a deployment success rate is asking the wrong question.

**The industry criterion, stated as a wall-clock question.** Yunzhu Li's definition of evaluation is not a success rate but a discrimination time:

> "The key criterion people use in industry is **how long in wall-clock time does it take for you to distinguish between a checkpoint that is 90% from a checkpoint that is 92%.**"

That 2-point discrimination is exactly the **±2 pp band** the [Clopper-Pearson bar](robot-policy-evaluation.md#the-sample-size-problem) prices at ≈1,030 rollouts. A practitioner independently named the wiki's own number as the operational bar — without naming the statistics, and while selling the way around it.

**The sample-size asymmetry is structural, not incidental.** World Labs evaluates each checkpoint on **2,000 simulated trials** (1,000 ID + 1,000 OOD) against **100 real trials** (50 ID + 50 OOD). The simulated side clears the [~1,030-rollout Clopper-Pearson bar](robot-policy-evaluation.md#the-sample-size-problem); the real side is ~±10 pp per cell. Any sim-vs-real correlation is therefore bounded by the precision of its *real* half — which is the general case, since the whole motivation is that real rollouts are expensive. **A method that makes simulated evaluation cheap does not make the ground truth it is validated against any cheaper.**

## What it is trying to fix

- **[RoboLab](../../sources/nvidia-robolab-evaluation-blog.md)'s failure mode #1.** Visual domain overlap, whose standard fix is real2sim via Gaussian splatting at **>1 hour per scene** — "pricing out large-scale testing." R2S2R is a bid to industrialize that pipeline.
- **The iteration-rate gap.** "Robot development iterates orders of magnitude more slowly than language-model development because policy evaluation remains heavily tied to physical hardware."
- **Coverage, not volume.** Internet video "falls short of systematically covering the environments, objects, appearances, physical properties, robot states, robot embodiments, and failure conditions" required.

## The unresolved tension

> [!warning] The train-and-judge problem is not solved, only defended
> [Sim-to-real transfer](../learning/sim-to-real-transfer.md#the-learned-simulator-failure-mode-teaching-to-a-flawed-test) records the [HAI brief](../../sources/hai-world-model-spatial-intelligence-brief.md)'s warning: using one learned model to both train and judge means "the score would reflect an error in the model, not readiness for a real road." **R2S2R does exactly this** — the same reconstructed world trains the policy and evaluates it. The defenses offered (matched open-loop validation, checking sim ranking against real ranking) are the right defenses in kind, but they are asserted without numbers by the party selling the world.
>
> The general principle survives: a reconstructed world is only as trustworthy as the *independent* real-world check on it, and that check is exactly the expensive thing R2S2R exists to avoid. The economics push toward validating less as confidence grows, which is the direction that fails silently.

> [!warning] Partial contradiction with WorldArena
> [WorldArena](../../sources/worldarena-paper.md) measured learned world models as **data engines** and found them marginal — only 2 of 6 beat real data, on the easier task only. R2S2R claims policies trained on **zero real data** transfer directly across diverse robots and contact-rich tasks. The plausible reconciliation is that WorldArena tested *generative-video* models producing pixels, while R2S2R reconstructs a world carrying explicit geometry, collision meshes and physics — the [renderer-vs-simulator line](../world-models/world-model-functional-taxonomy.md) itself. If that reconciliation holds, it is direct evidence for the taxonomy's linchpin claim; the wiki should not assume it holds without a paper.

## Precedent this is not the first of

Simulation-first training is established where embodiment is simple: the R2S2R post's own framing notes that L3/L4 self-driving is "powered by models trained using both real-world driving and simulation data," and that aircraft, rockets, drones and quadruped locomotion are developed and tested in simulation. The open question is whether it extends to **contact-rich manipulation of deformables**, which is where the wiki's [sim-to-real gap](../learning/sim-to-real-transfer.md#quantified-gap-2025) numbers are worst (RLBench 89.4% vs BEHAVIOR-1K 12.4%).

## Related concepts

- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — the classical direction and its reality gap.
- [Robot policy evaluation](robot-policy-evaluation.md) — the statistical standard R2S2R's protocol sits against.
- [World-model simulators](../world-models/world-model-simulators.md) — learned models as the environment.
- [World-model functional taxonomy](../world-models/world-model-functional-taxonomy.md) — the linchpin argument R2S2R exists to demonstrate.
- [World-model evaluation](../world-models/world-model-evaluation.md) — how you would trust a learned world at all.

## Mentioned in

- [Building Worlds That Train Robots (R2S2R)](../../sources/world-labs-r2s2r.md) — the naming source.
- [World Labs Acquires SceniX](../../sources/world-labs-scenix-acquisition.md)
- [How to Evaluate General-Purpose Robot Policies for Real-World Deployment](../../sources/nvidia-robolab-evaluation-blog.md) — the >1 hr/scene real2sim cost.
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../../sources/a16z-worldlabs-scenix-conversation.md) — the commercial articulation, the teleop-speed ceiling, and the admission that simulation does not replace real data.
- [WorldArena paper](../../sources/worldarena-paper.md)

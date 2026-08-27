---
title: "Building Worlds That Train Robots (R2S2R)"
type: source
url: https://www.worldlabs.ai/blog/real-to-sim-to-real
author: World Labs
published: 2026-07-28
ingested: 2026-08-26
venue: World Labs blog
format: results blog post
tags: [world-labs, scenix, real-to-sim-to-real, sim-to-real, robot-policy-evaluation, manipulation, deformable, world-model, simulator]
---

# Building Worlds That Train Robots

Subtitle: *"Real-to-sim-to-real (R2S2R) as a scalable engine for training and evaluating robot policies."*

## Summary

First technical results from the [SceniX](../entities/scenix.md) team after its [acquisition](world-labs-scenix-acquisition.md) by [World Labs](../entities/world-labs.md). Presents an **R2S2R engine**: reconstruct a real robot task as an interactive, generatively-modelled simulation aligned with reality in *both appearance and dynamics*, then use that world for two things — **training policies with zero real-world data**, and **predicting how policies will rank on hardware**. The claimed firsts are that policies trained entirely in simulation transfer directly across diverse robots and contact-rich tasks (deformable cables, articulated boxes, clutter), and that simulated evaluation **preserves relative policy ranking** and localizes failure regions on hardware. Framed explicitly as the evidence for the [functional taxonomy essay](world-labs-functional-taxonomy.md)'s claim that the simulator is the linchpin.

> [!warning] Vendor blog, no paper, no numbers
> Every quantitative claim below is a **protocol** count or a qualitative assertion. The post reports **no success rates, no correlation coefficients, and no baselines** — the sim-vs-real ranking result is presented as a chart and prose, not a table. No preprint, no code, no benchmark. Treat as a capability announcement, not a measurement. This matters more than usual because the wiki holds [directly comparable measured results](../concepts/robotics/robot-policy-evaluation.md) that *do* report correlations.

## Key claims

### The framing: experience, not architecture, is the bottleneck

- **"While we have seen rapid advances in robot learning methods such as vision-language-action models ([VLAs](../concepts/learning/vla-models.md)) and world-action models ([WAMs](../concepts/world-models/world-action-model.md)), the key bottleneck is not architecture alone, but experience and evaluation at scale."**
- Internet video is insufficient in a specific way: it "falls short of systematically covering the environments, objects, appearances, physical properties, robot states, robot embodiments, and failure conditions" needed. The complaint is about **systematic coverage**, not volume.
- The AV analogy is used as precedent *and* as a floor: "some of the most successful L3 or L4-level self-driving cars running on the road today are powered by models trained using both real-world driving and simulation data" — and driving "has a much simpler physical embodiment and a less complex task environment compared to general robotics."
- Explicitly ties back to the taxonomy: **"In our functional taxonomy of world models… we argued that the simulator is the linchpin because it turns a world into a place where agents can act, learn, and be evaluated. The work we share here puts that argument to the test."**

### Real-to-Sim: reconstructing tasks as aligned worlds

- Input is a **physical task**: capture "the robot, sensors, surroundings, objects, and task demonstrations," reconstruct as an interactive world "that preserves both what the robot perceives and the physical interactions that determine success or failure."
- Claims a **"novel, generative world modeling system"** producing high-fidelity appearance, accurate geometry, *and* realistic physics/dynamics together — asserted to exceed "what a traditional simulator can do."
- **Combines representations per task rather than committing to one.** The stated reason is measurement uncertainty in the real world: "Object shape, weight, and friction may be uncertain; cameras and robots can differ from their specifications; and cables, packaging, and tools deform in ways that simple models cannot fully capture."
- **Validation protocol: matched open-loop execution.** The same action sequence is run in sim and reality open-loop, comparing observations, object responses, and outcomes. Open-loop is the honest choice here — a closed-loop policy can mask dynamics error by correcting for it.
- Demonstrated task/robot pairs (all video, no metrics):

| Task | Robot | Interaction class |
|---|---|---|
| Bimanual box packing | [ALOHA](../entities/aloha.md) | Articulated + rigid |
| Cable manipulation (slide, route, plug) | [YAM](../entities/yam.md) | Deformable, sustained contact |
| Elastic cable insertion | [ALOHA](../entities/aloha.md) | Deformable under tolerance |
| Power-cord routing around a refrigerator | RB-Y1 | Deformable, bimanual, mobile-scale |
| Cube handover | [ALOHA](../entities/aloha.md) | Precision, arm-to-arm |
| Test-tube transfer | Flexiv | Tight geometric tolerance |
| Marker / pencil singulation from clutter | xArm | Thin objects, dense clutter |

- The stated significance is deliberately not any single video: **"a repeatable system that produces aligned worlds across interactions that have traditionally been difficult to simulate."**

### Sim-to-Real: training

- **"The policies shown here were trained entirely in simulation, with zero real-world training data, and transferred directly to diverse real robot platforms."**
- Systematic variation axes: "object configurations, robot states, viewpoints, appearance, physical properties, speed, and difficulty" — plus lighting perturbation shown as a robustness case.
- Two advantages claimed over hardware data that are about *supervision*, not volume:
  - Policies can "repeatedly and intentionally encounter difficult states and learn from both successes and failures **without resetting a physical environment after every trial**."
  - Simulation "provides supervision that is difficult to obtain on hardware, including precise object states, contacts, visibility, forces, and **outcomes under alternative actions**." (The last is counterfactual supervision — unobtainable on hardware by construction.)
- **Duration claim, repeated per task: "Operated autonomously for one hour without intervention."** Applied to power-cord manipulation (RB-Y1), cable manipulation (YAM), test-tube transfer (Flexiv), marker singulation (xArm), pencil singulation (xArm).
- **Reusability as the business claim:** "R2S2R is both policy- and embodiment-agnostic… A task reconstructed once can support new models and hardware over time, turning each world into **reusable infrastructure rather than a one-off simulation**."

### Sim-to-Real: evaluation — the load-bearing result

- The stated problem: **"Robot development iterates orders of magnitude more slowly than language-model development because policy evaluation remains heavily tied to physical hardware."**
- **The standard proposed is ordinal, not absolute:** *"A useful simulation need not match real-world success rates exactly. It must support the same decisions as reality: identify where policies succeed and fail, rank which policies are better, and predict whether improvements during training will carry over to hardware."*
- Two alignment results on an ALOHA bimanual cube-handover task, all **closed-loop** rollouts in both worlds:
  - **Near-boundary behavior matches.** "The policy normally grasps near the center of the cube. Near its generalization boundary, it grasps close to the edge and nearly fails, yet completes the task in both simulation and reality." Matched failures likewise. Claimed significance: the sim "reproduces the conditions that push a policy toward success or failure," not merely the final success label.
  - **Ranking is preserved.** "Across policy architectures, training configurations, and both ID and OOD settings, policies that perform better in simulation also perform better on hardware. Simulation preserves their relative ranking, tracks improvements and plateaus across checkpoints, and reveals similar spatial regions of success and failure."
- **The one hard protocol number in the post:** each checkpoint evaluated on **2,000 simulated trials (1,000 ID + 1,000 OOD)** and **100 real-world trials (50 ID + 50 OOD)**. ID = cube positions inside the post-training distribution; OOD = held-out positions outside it.
- The operational pitch: "screen checkpoints, catch regressions, guide policy and data iteration, and decide which models warrant costly hardware evaluation… a **high-throughput evaluation layer** for robot development."

### The closing loop

"Real-world outcomes improve the world model, the data, and the policy." Evaluation "actively searches for where they fail; and those failures guide what experience to generate next" — find the weakness, generate the experience, improve the policy, all in sim before returning to hardware.

## How this lands against what the wiki already measured

> [!note] Independent arrival at the wiki's ranking-not-magnitude conclusion
> R2S2R's evaluation standard — *don't match success rates, preserve rankings and failure regions* — is the same trade the wiki had already recorded from three unrelated directions: [RoboArena](roboarena-paper.md) (pairwise preference, r ≈ 0.95 vs ≈ 0.60 for centralized success-rate eval, at the cost of ever producing a number), the [Veo world-simulator evaluation](veo-robotics-policy-evaluation-paper.md) (Pearson 0.88, absolute rates run low), and [WorldArena](worldarena-paper.md) (ranking r = 0.986 for [Ctrl-World](../entities/ctrl-world.md), absolute rates inflated by "partial overfitting to successful trajectories"). A vendor with every incentive to claim its simulator matches reality instead pre-emptively **disclaims absolute fidelity and defends ordinal validity.** That convergence is worth more than the post's own evidence.

Three further contact points:

- **It industrializes the cost that [RoboLab](nvidia-robolab-evaluation-blog.md) named as a blocker.** RoboLab's first failure mode is visual domain overlap, whose standard fix is real2sim via Gaussian splatting at **>1 hour per scene**, "pricing out large-scale testing." R2S2R is a bid to make exactly that pipeline cheap and repeatable. If it works, it attacks RoboLab's problem #1 at the root.
- **The trial counts sit on both sides of the sample-size bar.** 2,000 simulated trials per checkpoint clears the [~1,030-rollout Clopper-Pearson bar](../concepts/robotics/robot-policy-evaluation.md#the-sample-size-problem) comfortably. The **100 real-world trials do not** — at n=100 split 50/50 the real-side bands are roughly ±10 pp per cell, so the *real* half of every sim-vs-real correlation in this post is measured at a precision that cannot resolve small gaps. The post's ordinal framing is not just principled; at n=50 per cell it is forced.
- **It is the direct counter-case to the learned-simulator failure mode the wiki flagged.** [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md#the-learned-simulator-failure-mode-teaching-to-a-flawed-test) records the HAI brief's warning about using one learned model to both train and judge — "the score would reflect an error in the model, not readiness for a real road." **R2S2R does exactly this**: the same aligned world trains the policy and evaluates it. The post's implicit defense is the matched open-loop validation and the sim-vs-real ranking check, which is the right defense in kind — but it is offered without numbers, and by the party selling the world.

> [!warning] Contradiction with the wiki's WAM-as-planner evidence — partial
> [WorldArena](worldarena-paper.md) measured learned world models as **data engines** and found them marginal: only 2 of 6 models beat real data, on the easier task only. R2S2R claims policies trained on **zero real data** transfer directly. These are not strictly incompatible — WorldArena tested *generative-video* world models generating trajectories, while R2S2R reconstructs a specific task into a physics-bearing interactive world with collision geometry, which is a different artifact — but the gap between "marginal data engine" and "sole source of training experience" is large enough that it should not be waved through. **The distinguishing variable is whether the learned world carries explicit geometry and physics or only pixels**, which is precisely the renderer-vs-simulator line the [taxonomy](world-labs-functional-taxonomy.md) draws. R2S2R is the taxonomy's own argument used as an explanation for its results.

## Entities mentioned

- [World Labs](../entities/world-labs.md) / [SceniX](../entities/scenix.md) / [Fei-Fei Li](../entities/fei-fei-li.md) / [Yunzhu Li](../entities/yunzhu-li.md)
- [ALOHA](../entities/aloha.md), [YAM](../entities/yam.md) — robots with existing pages.
- **RB-Y1** (Rainbow Robotics), **Flexiv**, **xArm** (UFACTORY) — no pages; named as demo platforms only.
- Martin Casado / a16z — companion conversation, not ingested.

## Concepts touched

- [Real-to-sim-to-real (R2S2R)](../concepts/robotics/real-to-sim-to-real.md) — the concept page this source creates.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)
- [World-model simulators](../concepts/world-models/world-model-simulators.md)
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md)
- [VLA models](../concepts/learning/vla-models.md) / [world-action model](../concepts/world-models/world-action-model.md)

## Open questions

- **What is the "novel generative world modeling system"?** No architecture, no training data description, no parameter count. Whether it is [Marble](../entities/marble.md) extended, SceniX's pre-existing stack, or a fusion is unstated.
- **"Combines different representations and modeling techniques according to what matters for each task"** — how much of that selection is manual? A per-task engineering step would undercut the "repeatable engine" claim, and the post does not say.
- **No success rates anywhere.** The wiki cannot place R2S2R next to [WorldArena](worldarena-paper.md)'s r = 0.986 or [Veo](veo-robotics-policy-evaluation-paper.md)'s 0.88 without a correlation coefficient.
- **Which policies were ranked?** "Across policy architectures" — unnamed. Whether these were [π0](../entities/pi-zero.md)-class VLAs or task-specific diffusion policies changes what the ranking result means entirely.
- **Zero-real-data training is claimed but the worlds are built from real captures.** The real data moved from policy training into world construction; the post never quantifies how much capture a task needs. That number is the actual cost of the method.
- **One hour without intervention** is a duration, not a success rate. Cycles completed, failures recovered, and what "without failure" means for a repeated singulation task are all unstated.
- **No safety constraint checked** — same gap as every other success claim in this wiki ([PACS](pacs-paper.md)).

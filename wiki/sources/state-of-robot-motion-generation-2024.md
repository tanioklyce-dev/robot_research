---
title: The State of Robot Motion Generation (Bekris et al., 2024)
type: source
url: https://arxiv.org/abs/2410.12172
author: Kostas E. Bekris, Joe Doerr, Patrick Meng, Sumanth Tangirala (Rutgers University CS)
published: 2024-12-16 (arXiv 2410.12172v2; v1 2024-10)
venue: arXiv review paper (Springer-style formatting; likely an ISRR 2024 invited review — not confirmed in the PDF)
ingested: 2026-07-04
local_path: raw/TheStateOfMotionGEneration_2410.12172v2.pdf
format: pdf (16 pp., 100 refs)
tags: [motion-generation, motion-planning, tamp, trajectory-optimization, sampling-based-planning, mpc, imitation-learning, rl, survey, rutgers]
---

## Summary

A 50-year cross-community review of robot motion generation that deliberately crosses survey boundaries usually kept separate. Organizing question: *"Will the emerging set of data-driven methods for generating robot motion supersede the traditional techniques as access to robot motion data increases?"* All methods are classified along one top-level divide — those operating over an **explicit model** (analytical expressions or simulators of world geometry/dynamics) vs those learning an **implicit model** (representations stored in ML parameters). Explicit-model motion generation is mature and deployed (autonomous vehicles, industrial arms); implicit/data-driven methods excel exactly where explicit models fail (dexterous manipulation, unstructured locomotion) but only near their demonstration distribution. The verdict (§4): **neither side supersedes the other — integrative approaches are needed** for robust, safe, cost-effective deployment. This is the wiki's first structured coverage of the classical motion-planning stack.

## Key claims

### Branch 1 — explicit models (§2)
1. **[Motion planning](../concepts/robotics/motion-planning.md) (§2.1)** — search-based (Dijkstra/A*; optimal with admissible heuristics; curse of dimensionality), **sampling-based** (PRM multi-query roadmaps; RRT single-query trees needing no steering function; PRM*/RRT* asymptotically optimal; OMPL implementations), **optimization-based** (CHOMP, TrajOpt, KOMO, factor graphs/STEAP, Graph of Convex Sets — fast, high-quality, but local-minima-prone), and ML-for-planning (learned sampling/collision checks; Motion Planning Networks).
2. **[Task and motion planning](../concepts/robotics/task-and-motion-planning.md) (§2.2)** — long-horizon multi-step tasks; motion-constrained operators + lifted logical variables + plan skeletons; categorized sequencing-first / satisfying-first / interleaved. Critically relies on engineered preconditions/effects; struggles under partial observability.
3. **Belief-space planning (§2.3)** — (PO)MDPs over belief distributions; exact solutions intractable; approximations: point-based (SARSOP), tree search (DESPOT), policy search, heuristics.
4. **Control & feedback-based planning (§2.4)** — PID (robust but myopic); potential/navigation functions; operational-space + null-space hierarchical control; LQR, feedback linearization, sequential composition, **LQR-Trees** (sums-of-squares-verified regions of attraction + SBMPs); **MPC/NMPC and replanning** ("applicable across robotic systems for bridging the model gap" but tuning-heavy) — see [optimal control](../concepts/robotics/optimal-control.md).

### Branch 2 — implicit models (§3)
1. **Learning from demonstrations (§3.1)** — BC (compounding distributional shift to OOD states), DAgger-style corrections, inverse RL (dense-reward extraction; high-dim scaling is the challenge), **diffusion policies** (capture multi-modal demo distributions that MSE-trained MLPs average away; [Diffusion Policy](../entities/diffusion-policy.md) over LSTM-GMM cited; inference speed flagged as the active challenge — the exact gap [VQ-BeT](../entities/vq-bet.md) targets).
2. **RL (§3.2)** — four core RL-for-robotics challenges: sample inefficiency, instability, reward engineering, long horizons (an update of [Kober et al. 2013](kober-rl-robotics-survey-2013.md)'s four curses). Variants mapped to each: sim + domain randomization, off-policy (TD3/SAC/HER), offline (IQL/CQL), model-based (MOPO), hierarchical.
3. **Cross-task learning (§3.3)** — transfer, multi-task (AdaShare), lifelong (replay mixing, modular composition).
4. **Large models (§3.4)** — LLMs for task specification/reward code (Eureka), VLMs (SayCan affordances; Manipulate-Anything demo generation), **VLAs/robot foundation models** ([OpenVLA](../entities/openvla.md) on [Open X-Embodiment](../entities/open-x-embodiment.md); in-distribution strong, fine-tunable).

### Verdict & integrative directions (§4)
- **Explicit side:** industrial-arm collision-free planning "reliably addressed today at high speeds"; fails where model/state-estimation reliability is low (complex contacts, clutter, uneven terrain, high-speed unstructured). [TAMP](../concepts/robotics/task-and-motion-planning.md) requires engineers to encode concepts + expensive combinatorial reasoning.
- **Implicit side:** diffusion-based LfD wins exactly where explicit models struggle — *but only when the execution setup resembles the demonstration setup*. RL's sample inefficiency remains a bottleneck for accuracy across wide initial-condition sets.
- **On the foundation-model bet (hedged):** "While this direction should be pursued, it is not clear that it is possible to collect internet-scale demonstration data that will allow learning robust enough policies" for novel, unstructured, human environments — and predicting when learned solutions succeed is a significant safety concern.

> [!note] Direct counterpoint within the wiki
> The hedge above is the explicit-model community's answer to the scaling bets the wiki tracks on the learning side — [EgoScale](egoscale-paper.md)'s VLA scaling law, [GR00T N1](groot-n1-paper.md)'s data pyramid, [π0.7](pi07-paper.md)'s emergent capabilities. Both positions are live; the disagreement is the field's central open question.

- **Recommendations:** (1) explicit-model planners in sim as *demonstrators* for data-driven policies; (2) wrap learned controllers in verification-inspired safety architectures; (3) explicit methods for controller composition on long horizons (adaptive task planning, skill discovery, failure explanation); (4) maintain an internal learned world model ("cognitive physical engine") for explainability — cites SayPlan and ReKep as existing hybrids.
- **Infrastructure gap:** no common interfaces/benchmarks span both methodological families.

## Entities mentioned

- [Diffusion Policy](../entities/diffusion-policy.md), [OpenVLA](../entities/openvla.md), [Open X-Embodiment](../entities/open-x-embodiment.md) — implicit-side anchors with wiki pages.
- Named classical methods without wiki pages: PRM (Kavraki), RRT/RRT* (LaValle; Karaman & Frazzoli), OMPL, CHOMP, TrajOpt, KOMO, GCS (Tedrake group), SARSOP, DESPOT, LQR-Trees, D* Lite.
- Named learned systems: DAgger, TossingBot, Eureka (NVIDIA GEAR — see [GEAR publications](nvidia-gear-publications.md)), SayCan, SayPlan, ReKep.
- Authors: Kostas Bekris (Rutgers) et al. — no entity pages; prominent cited researchers (Tedrake, Toussaint, Khatib, Kaelbling, Lozano-Pérez, Levine…) likewise.

## Concepts touched

- **[Motion planning](../concepts/robotics/motion-planning.md)** — new concept page from this ingest.
- **[Task and motion planning](../concepts/robotics/task-and-motion-planning.md)** — new concept page from this ingest.
- [Optimal control](../concepts/robotics/optimal-control.md) — §2.4 is the OC-as-motion-generation family.
- [Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md) — named here in one clause of §2.1; see the caveat below.
- [Imitation learning](../concepts/learning/imitation-learning.md), [VLA models](../concepts/learning/vla-models.md), [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [World model](../concepts/world-models/world-model.md) ("cognitive physical engine" recommendation).

> [!warning] Its one-clause summary of optimization-based planning is wrong about one of the methods it names (added 2026-08-16)
> §2.1 characterizes the optimization-based family as *"fast, high-quality when they work; local minima on non-convex problems"* and lists **Graph of Convex Sets** alongside CHOMP, TrajOpt and KOMO. Fair for the other three; **not** for GCS, whose whole point is that the relaxation is tight enough to recover the *global* optimum from a single convex program — with a per-query certificate of the gap ([Marcucci, Petersen, von Wrangel & Tedrake 2022 / Science Robotics 2023](gcs-motion-planning-paper.md), ingested here 2026-08-16, and published a year before this survey).
>
> Not a serious flaw in a 16-page 50-year review, but it is the kind of compression that a wiki built on the survey would otherwise inherit permanently. The correct qualifier on GCS is **restricted problem class** (kinematic, convex-decomposable free space) rather than **local minima**.

## Open questions

1. The framing question itself — supersession vs integration (paper answers: integration).
2. Can internet-scale demonstration data yield robust policies for novel human environments? (The wiki's scaling-law sources bet yes; this paper hedges no.)
3. Verification/safety certification for implicit-model policies — how to predict when a learned solution will succeed.
4. Diffusion-policy inference speed (answered in part by [VQ-BeT](vq-bet-paper.md)'s 5×/25× results, which this survey does not cite).
5. Missing cross-family benchmarks and interfaces.

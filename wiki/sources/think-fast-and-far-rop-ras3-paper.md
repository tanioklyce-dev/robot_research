---
title: "Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling — ROP-RAS3 (Liang et al., 2026)"
type: source
url: https://arxiv.org/abs/2606.04355
local_path: raw/2606.04355.pdf
sha256: 61fbc1fb95fe95a8fd5080461df9e0a718eb65053fb3da4f699d1633e42c267d
author: "Yuanchu Liang, Edward Kim, J. Arden Knoll, Wil Thomason, Zachary Kingston, Lydia E. Kavraki, Hanna Kurniawati"
affiliations: "Australian National University (RDL Lab); Rice University (Kavraki Lab); Purdue"
published: 2026-06-03
venue: "arXiv preprint (v1), SAGE journal formatting (IJRR-style); extends the authors' ISRR 2024 paper"
format: paper (23 pp; 15 pp body + references + appendix)
arxiv: 2606.04355
code: https://github.com/RDLLab/ROPRAS3
tags: [POMDP, planning-under-uncertainty, motion-planning, sampling-based-planning, VAMP, macro-actions, reference-based-POMDP, belief-space, long-horizon, stretch-3, franka-panda, classical-planning]
ingested: 2026-09-12
---

# Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling (ROP-RAS3)

## Summary

**A classical planner that solves 1,500-step, 35-dimensional POMDPs online by never enumerating actions.** Two advances are combined. First, the *reference-based POMDP* (Kim, Karunanayake & Kurniawati 2023), reformulated here over stochastic policies: penalise KL-divergence from a reference policy π̄ and the Bellman backup has a closed form — V(b) = (1/η) log ∫ π̄(a|b) exp(ηQ(b,a)) da, with π*(a|b) ∝ π̄(a|b) exp(ηQ(b,a)) — so the **maximisation over actions becomes an expectation** that Monte Carlo can estimate, no bandit, no UCB, and the convergence rate depends on the number of actions *sampled*, C_A, rather than the size of the action space. Second, the reference policy is generated on the fly by **VAMP** (Thomason, Kingston & Kavraki 2024), a SIMD-vectorised sampling-based motion planner that returns collision-free paths in microseconds: sample a state from the belief, sample an *informative* target (a goal, a landmark, an observation zone), plan a path, convert it to a macro-action. Tens of thousands of such macro-actions per second give the tree diverse, geometry-aware long actions that a learned macro-action method (MAGIC) needs hours to train.

On seven simulated problems — 2D/3D navigation with localisation only at landmarks, a four-drone tag with a teleporting target (15-D), and three 7-DoF [Franka](../entities/franka-panda.md) manipulation tasks up to a 35-D shelf-clearing problem with a 1,500-step planning horizon — ROP-RAS3 wins every scenario, often by multiples: **Maze2D 90% where POMCP, MAGIC and RMAG score 0%**; **Shelf-Move 70% vs 10%** with 100 simulations and under 10 s of planning. A physical [Stretch 3](../entities/stretch.md) uses it to detour behind a moving pedestrian where the reference policy alone drives into them.

> [!note] What "optimal" means here
> The solution is optimal for the *reference-based* objective, not the original POMDP; a poor reference policy caps performance (the ε-exploration ablation shows graceful but real degradation toward a uniform reference). The reference policies are built from **hand-designed sampling heuristics per problem**, which the authors call *"fundamental to the success."* Evaluation is 30 runs per scenario with 1 s of planning per step; learned baselines run on two problems only; the physical demonstration is *"a few trials."* A strong, well-controlled planning result with the usual planning-paper caveat that the heuristics are where the domain knowledge went.

## Key claims

### Theory (Sec. 3, 4.4, App. A.1)

- Reference-based POMDP over stochastic policies, tuple ⟨S, A, O, Z, T, R, γ, η, π̄⟩; Theorem 2 gives the analytical backup; *"enumerative maximization in (1) is replaced with expectation."* Continuous state, action and observation spaces handled by double progressive widening with uniform re-sampling from existing children (no bandit needed).
- Theorem 3: the sparse-sampling idealisation converges at **O(C_A (C_A C_S)^D exp(−min{C_A, C_S} t²_max))** — C_A sampled actions and C_S particles, versus |A| in Lim et al.'s rate. The proof treats the V-estimate as a second self-normalised importance-sampling estimator whose weights are the observation weights re-weighted by the fully-observable reference policy's support.
- Iterating with the solution as the next reference converges to the true POMDP optimum (Kim & Kurniawati 2025) but is out of scope.

### Algorithm (Sec. 4)

- VAMP: forward kinematics and collision checks vectorised over configurations; robot-specific code generated from a URDF; *"probabilistically-complete, global, collision-free trajectories for high-DoF systems at kilohertz rates."*
- Macro-action sampler: source state ~ belief, target ~ heuristic J(·|b). **UNIFORM** heuristic: goal with p = 0.5, other informative states uniformly. **DYNAMIC**: goal with p = 1 − H(b) (normalised belief entropy), else information states weighted by inverse distance. Multi-drone: nearest drone toward a sampled target, others spread.
- Depth-first tree growth, a new action edge each time a new particle reaches a node — which is why the DYNAMIC heuristic helps ROP-RAS3 and hurts R-POMCP, which expands all actions at once.

### Results (Tab. 2–5, 30 runs, 1 s planning for navigation)

| Problem | S / A / horizon | ROP-RAS3 | Best baseline |
|---|---|---|---|
| Light-Dark | R² / 4 / 8 | 96.7% | MAGIC / RMAG 88% |
| Maze2D | R² / 4 / H_min 100 | **90%** (dynamic) | B-VAMP 50%; POMCP, MAGIC, RMAG, R-POMCP **0%** |
| Random3D (4 densities) | R³ / 6 / 40 | 47–67% | B-VAMP 0–43%; R-POMCP 7–13% |
| Multi-Drone Tag | R¹⁵ / 24 / 20 | **90%** | R-POMCP 66.7% |
| Sphere-Search | R¹³ / R⁷ / 50 | **100%** | R-POMCP 76.7% |
| Ray-Detect | R³¹ / R⁷ / 80 (plan 500) | **80%** | R-POMCP 26.7% |
| Shelf-Move | R³⁵ / R⁷ / 300 (plan 1,500) | **70%** (dynamic; 100 sims; 8.9 s) | R-POMCP / B-VAMP 10% |

- Robust to reference-policy failure: in Random3D the RRT-Connect reference fails on up to 23% of queries at the highest clutter and success holds at 47–57%, *"as long as there is sufficient diversity of macro-actions."*
- Ray-Detect: the only method that *"consistently realizes that the most robust way to reach the cylinder is to use the ray to observe obstacles on the path and swing around."* Shelf-Move: removes two obstacles to non-target locations, and re-arranges if it blocks the target slot by mistake — *"Other methods… their successful runs were often lucky runs."*
- Ablations: ε-greedy sampling toward uniform degrades non-linearly (Maze2D drops sharply from ε = 0.6 to 1) but still beats R-POMCP at ε = 1 (13% vs 0%); tree depth should be *"roughly the number of steps needed to solve the problem under deterministic settings."*
- Implementation: Python (pomdp_py) with VAMP in C++; 30–50 simulations suffice in complex scenarios; particle reinvigoration needed; observation widening replaced by binning.

### Physical Stretch 3 (Sec. 5.5, App. A.2.3)

16-D state (13 robot + 3 pedestrian-as-sphere), 45 open-loop twist primitives (three linear speeds × angular velocities in 0.1 rad/s steps, 0.7 s each), Euler-integrated transitions with added noise, IMU for belief updates, horizon 75, planning horizon 25; +800 goal, −800 collision, −20 within 0.3 m. ROP-RAS3 *"is the only method that demonstrates a consistent smart and robust strategy of taking an efficient detour to go behind the moving pedestrian"*; B-VAMP steers straight into the pedestrian; R-POMCP takes a long detour into the tables. Trial count unstated.

## Why it matters in this wiki

- **The classical pole.** The wiki's coverage of acting under uncertainty is almost entirely learned policies; [belief states](../concepts/world-models/belief-states-and-mixed-states.md) is filed under world models. This is the planning literature's answer — explicit beliefs, a generative model, a tree — with a convergence theorem, on the same Stretch 3 the learned methods use. It is a useful reference point for what *"long-horizon"* means outside VLA papers: 1,500 planning steps, not ten subtasks.
- **Hardware-accelerated motion planning as an enabler.** VAMP's microsecond plans are what make sampling macro-actions online feasible at all; the [motion-planning](../concepts/robotics/motion-planning.md) page should carry that number beside cuRobo's GPU parallelism.
- **A structural echo.** π* ∝ π̄ exp(ηQ) is the same KL-regularised policy-improvement form that appears in advantage-weighted and CFGRL-style extraction on the [real-world RL](../concepts/learning/real-world-robot-rl.md) page — one is solved by tree search over a belief, the other by fine-tuning a network on rollouts.
- **[Task and motion planning](../concepts/robotics/task-and-motion-planning.md)** — Shelf-Move is TAMP under partial observability, solved without a symbolic layer.

## Entities mentioned

- [Stretch](../entities/stretch.md) — Stretch 3 pedestrian-dodging demonstration.
- [Franka Panda](../entities/franka-panda.md) — the 7-DoF arm in the three manipulation simulations.
- Lydia Kavraki, Hanna Kurniawati, Zachary Kingston, Wil Thomason — no entity pages; VAMP and cuRobo — no entity pages.

## Concepts touched

- [Motion planning](../concepts/robotics/motion-planning.md) — VAMP as the fast primitive; macro-actions from paths.
- [Belief states](../concepts/world-models/belief-states-and-mixed-states.md) — explicit particle beliefs, the classical form.
- [Optimal control](../concepts/robotics/optimal-control.md) — KL-regularised (linearly-solvable) control lineage: Todorov 2006, Azar et al. 2012.
- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md) — Shelf-Move.

## Open questions

- **How much is the heuristic?** The paper says sampling heuristics are fundamental and shows degradation toward uniform; it does not test a *learned* target sampler.
- **Trial counts on hardware.** "A few trials."
- **Compute on the robot.** Planning ran on a workstation in Python; on-robot budgets are not discussed.
- **Reference-based vs true optimum.** How far apart they are on these problems is not measured; the iterative fix exists in a separate paper.
- **Learned baselines on manipulation.** MAGIC and RMAG were not run on the 7-DoF tasks because they "do not naturally extend" — the comparison there is planner-vs-planner only.

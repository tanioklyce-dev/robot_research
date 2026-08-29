---
title: Reinforcement Learning in Robotics — A Survey (Kober, Bagnell & Peters, IJRR 2013)
type: source
url: https://journals.sagepub.com/doi/10.1177/0278364913495721
author: Jens Kober (Bielefeld / Honda Research Institute Europe), J. Andrew Bagnell (CMU Robotics Institute), Jan Peters (MPI Intelligent Systems Tübingen / TU Darmstadt)
published: 2013 (IJRR 32(11):1238–1274)
ingested: 2026-07-04
local_path: raw/RL_Survey_Kober_IJRR_2013.pdf
sha256: afe949ac5ee4c624537bf97cef312353cc12460436affc7b2cb5fa9878739bd4
format: pdf (author-typeset, 73 pp.)
tags: [reinforcement-learning, robotics, survey, policy-search, imitation-learning, model-based-rl, reward-shaping, historical]
---

## Summary

The canonical pre-deep-learning survey of RL applied to real robots. Thesis: naive application of RL to robots is "likely to be doomed to failure" because robotics imposes **four compounding curses** — dimensionality, real-world samples, under-modeling/model uncertainty, and goal specification. Every notable real-robot RL success circa 2013 tamed this complexity through three levers: **effective representations, approximate models ("mental rehearsal"), and prior knowledge (especially demonstrations)** — and by favoring **policy search over value-function methods** (and often model-based over model-free), the opposite of mainstream ML-community RL at the time. Grounded in the authors' own ball-in-a-cup case study on a Barrett WAM. Sits chronologically and intellectually between [Sutton & Barto](sutton-barto-rl-textbook.md) (the general theory) and the wiki's modern demonstration-dominated robot-learning line.

## Key claims

### Framing (§1)
- RL and robotics relate "like physics and mathematics": robotics supplies inspiration, validation, and impact; RL supplies a framework for behaviors too hard to engineer by hand.
- RL sits atop a two-axis hierarchy of ML problems (reward-structure × interactive/sequential complexity, after Langford & Zadrozny 2005), subsuming supervised learning, contextual bandits, structured prediction, and imitation learning. Imitation's compounding-error problem (Ross et al. 2011) noted; "Baseline Distribution RL" (expert-provided initial-state distribution) is dramatically easier.
- RL cast as **"adaptive [optimal control](../concepts/robotics/optimal-control.md)"**: optimal control assumes a perfect model; RL works from measured data; a key robotics approach is classical optimal control (LQR, DDP) applied to *learned* models (§1.2).
- Circa-2013 robotics reality (§1.3): 10–30 dimensional continuous state/action spaces, partial observability, expensive rollouts — and **most demonstrated successes were model-based, using policy search rather than value functions**.

### The four curses (§3)
1. **Dimensionality** — 10ⁿ states; robotics copes with hierarchical decomposition and operational-space reductions at the cost of dynamic capability.
2. **Real-world samples** — hardware cost, wear, manual resets, safe exploration, dynamics drift (learning "may never fully converge"; needs tracking), fixed control rates and delays violating the Markov assumption. Sample efficiency dominates compute.
3. **Under-modeling / model uncertainty** — sim-trained policies rarely transferred for dynamic/unstable tasks (small model errors accumulate; Atkeson 1994); transfer works better for **self-stabilizing** tasks (the ball-paddling elastic string made the real system self-stabilizing while sim predicted near-uncontrollability).
4. **Goal specification** — binary rewards almost never suffice; **reward shaping** is a substantial manual contribution; RL is "notorious for exploiting the reward function in ways not anticipated by the designer" (early statement of reward hacking). **Inverse RL** (Abbeel & Ng 2004; Ratliff et al. 2006; Ziebart et al. 2008) presented as the promising alternative.

### Why policy search dominated robotics (§2.2–2.3, consolidated)
- Formal taxonomy: optimizing the primal of the average-reward problem = policy search; optimizing the Lagrangian dual (multipliers = value function) = value-function methods.
- Value-function methods need **global** state-space coverage and their largest local error bounds policy quality; Bellman backups + function approximation can diverge — "considerably more dangerous" on hardware.
- Policies often need far fewer parameters than value functions (LQR: linear vs quadratic in state dim) and admit expert structure, demonstrations, constraints.
- Policy search makes only **local, controlled changes to the state distribution** — the safe, sample-efficient regime the curses demand; knowing a good policy's state distribution turns RL from provably intractable to polynomial (Kakade & Langford 2002).
- Policy-search families catalogued: gradients (finite-difference; REINFORCE; natural gradients), EM-style (reward-weighted regression, **PoWER**, CrKR), path integrals (**PI²**), Relative Entropy Policy Search.

### Tractability levers (§4–6)
- **Representation (§4):** discretization, value-function approximation (incl. the Brainstormers' MLP value functions that won RoboCup — with Riedmiller's "clamping" trick against divergence), and **pre-structured policies**: dynamical-system motor primitives (Ijspeert/Schaal), splines, locally linear controllers (helicopter; Tedrake biped; LittleDog).
- **Prior knowledge (§5):** demonstrations are the strongest lever — **the most dramatic benefit is removing the need for global exploration** (the Fosbury Flop as the caveat: local optimization around a demo finds only local optima). Modes: motion capture (correspondence problem), teleoperation, kinesthetic teach-in, hand-crafted initial policies. Also task structuring (hierarchical RL, progressive tasks) and directed exploration.
- **Models / "mental rehearsal" (§6):** core issue is **simulation bias** — policies exploit model errors, "analogous to overfitting"; mitigated by artificial noise injection (Jakobi 1995; Atkeson 1998 — the ancestor of domain randomization), distributions over models (GP dynamics; **PILCO** cart-pole in <20 s of interaction), and PEGASUS-style common random numbers. Model-exploiting successes: iterative learning control (surgical knot-tying at superhuman speed, van den Berg 2010), locally linear LQR/DDP (aerobatic helicopters).

### Ball-in-a-cup case study (§7)
- Barrett WAM; 20 state dims, 7 action dims; shaped exponential reward at the moment the ball crosses the cup rim downward (earlier distance-only rewards were exploited — hitting the cup from below).
- Policy = dynamical-system motor primitives, **217 parameters** (31/DoF × 7); initialized by **kinesthetic teach-in** (imitation gets the shape, misses by centimeters); improved with **PoWER** (EM-style, no learning rate, importance sampling over ~10 best episodes).
- **First success after 42–45 episodes; reliable by 70–80; converged by ~100** — with manual ball resets each episode. Sim was used only for algorithm tuning; sim-trained policies missed on the real robot and vice versa. Contrast: Nemec et al. 2010 solved it with SARSA + discretization needing 220–300 sim + 40–90 real episodes.

### Recommendations (§8)
- Open questions: automatic representation choice; generating rewards from data; how much prior knowledge is needed; **tighter integration with perception** (2013 work "abstracts away perceptual information"); handling model errors.
- Practical: exploit datasets and transfer across skills/robots — "making such data sets with many skills publicly available would be a great service" (anticipates [Open X-Embodiment](../entities/open-x-embodiment.md)); standardized benchmarks.
- Lessons for RL: robot RL in practice sits **closer to classical optimal control than to ML-textbook RL**; exploit domain structure; local optimality + controlled state distributions explain policy search's success; shaped, physically motivated rewards over sparse binary ones.

## What aged well / poorly (wiki assessment)

> [!note] Assessment, not paper content.

**Held up:** the four curses remain the canonical diagnosis; "demonstrations remove global exploration" is arguably the survey's most prophetic claim — modern robot learning ([Diffusion Policy](../entities/diffusion-policy.md), [VQ-BeT](../entities/vq-bet.md), [GR00T](../entities/nvidia-groot.md)-class VLAs) is demonstration-dominated, with RL as fine-tuning around demonstration-anchored distributions (exactly the §5.1/§7 loop; [π*0.6](pistar06-paper.md)'s RECAP is the modern instance). The public-dataset call anticipated OXE. "Exploiting the reward function" became reward hacking. "Tighter integration with perception" named the gap end-to-end visuomotor learning and VLAs filled. Noise injection foreshadowed domain randomization.

**Overturned:** "sim-trained policies rarely transfer" — massively parallel GPU [sim-to-real](../concepts/learning/sim-to-real-transfer.md) + domain randomization made model-free sim-trained RL the *dominant* paradigm for locomotion. The skepticism toward neural value functions predates DQN (2013–15) and the actor-critic renaissance (PPO/SAC) — though PPO/TRPO's trust-region logic directly descends from the survey's "local optimality and controlled state distributions" lesson via Kakade & Langford. Hand-designed 217-parameter policies gave way to generic deep networks; 10–30 dims being "large" reads quaintly against pixel-input control.

## Entities mentioned

- Authors: Jens Kober, J. Andrew Bagnell, Jan Peters (no entity pages; file if they recur).
- [Boston Dynamics](../entities/boston-dynamics.md) — LittleDog (jumping, Kolter & Ng 2009).
- Platforms without entity pages: Barrett WAM, Sony Aibo, Sarcos DB, Stanford/CMU autonomous helicopters, Brainstormers Tribots, Crusher UGV, OBELIX, Zebra Zero.
- People cited who have wiki pages via other lineages: none directly, but the Schaal/Atkeson motor-primitive line and the Abbeel/Ng apprenticeship line are the ancestors of much of the wiki's [imitation-learning](../concepts/learning/imitation-learning.md) coverage.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — §5.1 is the clearest early statement of why demonstrations are the master key.
- [Optimal control](../concepts/robotics/optimal-control.md) — "RL = adaptive optimal control"; the bridge the wiki also draws via [Sussmann & Willems 1997](sussmann-willems-1997-300-years-optimal-control.md) and [Sutton & Barto](sutton-barto-rl-textbook.md).
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — simulation bias, noise injection, self-stabilizing-task transfer.
- Model-based RL / mental rehearsal — ancestor of the wiki's [world model](../concepts/world-models/world-model.md) line ([Dreamer](../entities/dreamer.md), [TD-MPC](../entities/td-mpc.md)).
- Reward shaping / inverse RL — precursor to RLHF-era reward learning.
- [Curriculum Module 8 — RL vocabulary](../syntheses/curriculum/curriculum-08-rl-vocabulary.md) — this survey is the historical robotics companion to Module 8's vocabulary.

## Open questions

- Jan Peters / Stefan Schaal motor-primitive lineage (DMPs) has no concept page; file if DMPs recur (they're resurfacing in modern skill-learning work).
- The [Atari RL lineage synthesis](../syntheses/rl/atari-rl-lineage.md) covers the value-function renaissance this survey didn't foresee; a "robot RL lineage" synthesis (Kober 2013 → deep-RL locomotion → RECAP-class VLA fine-tuning) would complete the pair.

---
title: "Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., MIT Press 2018 / 2020 reprint)"
type: source
url: http://incompleteideas.net/book/the-book.html
local_path: raw/RLbook2020.pdf
draft_path: raw/SuttonBartoIPRLBook2ndEd.pdf
isbn: 9780262039246
license: CC BY-NC-ND 2.0 (electronic) / hardcover via MIT Press
author: Richard S. Sutton, Andrew G. Barto
affiliation: U Massachusetts Amherst (Barto); U Alberta / DeepMind (Sutton); A Bradford Book, The MIT Press
published: 1st ed. 1998; 2nd ed. published 2018; 2020 reprint
ingested: 2026-05-14 (initial against 2014–2015 in-progress draft); 2026-05-14 (updated against 2018 final 2nd edition)
tags: [reinforcement-learning, textbook, sutton-barto, foundational, mdp, value-function, bellman, dynamic-programming, monte-carlo, td-learning, q-learning, sarsa, eligibility-traces, actor-critic, policy-gradient, reinforce, mcts, mbrl, dqn, alphago, dedicated]
---

> [!note] Ingest depth + version
> **Two PDFs on file**, both now ingested:
> - **`raw/RLbook2020.pdf`** (548 pages, PDF metadata `CreationDate D:20220426`; ©2018, 2020) — the **published 2018 final 2nd edition**, ISBN 9780262039246. **This is the canonical reference and the `local_path` target.** License: CC BY-NC-ND 2.0 (electronic).
> - **`raw/SuttonBartoIPRLBook2ndEd.pdf`** (352 pages, PDF metadata `CreationDate D:20150412`) — the **2014–2015 in-progress draft** of the 2nd edition, retained as a historical reference for the field's drafting period. `draft_path` in frontmatter.
>
> Ingest covers both at the **section-summary** level: front matter, Ch 1 (RL problem), Ch 2 (bandits), Ch 3 (MDPs), Ch 4 (DP), Ch 5 (MC), Ch 6 (TD), Ch 7 (n-step bootstrapping), Ch 8 (planning + MCTS), Part II (function approximation — Ch 9–12 in 2018 final), **Ch 13 (Policy Gradient Methods — substantial new chapter in 2018 final)**, and Part III "Looking Deeper" (Ch 14–17 in 2018 final, including DQN/Atari + AlphaGo case studies). Not a verbatim reproduction; key equations transcribed, derivation outlines summarized.

## Summary

**"Reinforcement Learning: An Introduction"** by Richard S. Sutton and Andrew G. Barto is the **canonical textbook for the field of reinforcement learning** — sometimes called "the RL bible." The 1st edition (1998) established the field's vocabulary; the **2nd edition (MIT Press 2018, with a 2020 reprint)** is a 548-page substantial expansion that incorporates two decades of progress, including the function-approximation chapters (Ch 9–12), the full Policy Gradient Methods chapter (Ch 13) covering REINFORCE / Actor–Critic / Policy Gradient Theorem, and applications case studies (Ch 16) including **DQN on Atari** (Mnih et al. 2015) and **AlphaGo / AlphaGo Zero** (Silver et al. 2016, 2017). Sutton & Barto won the **2024 Turing Award** for the work this book consolidates.

The book defines a **computational study of goal-directed learning from interaction**, distinct from both supervised learning (no labels, only scalar rewards) and unsupervised learning (there *is* a target — the cumulative reward). Sutton & Barto identify four sub-elements of an RL system (§1.3):

1. **Policy `π(a | s)`** — mapping from states to actions. What you're learning.
2. **Reward signal** — the scalar number the environment hands back. Defines the goal.
3. **Value function `v(s)` or `q(s, a)`** — long-term reward expected from a state (or state-action pair). The thing most algorithms estimate.
4. **(Optional) model of the environment** — predicts next state / reward given (state, action). Model-based vs model-free is the central axis the book organizes around.

The book runs from **tabular bandits** (Ch 2) to **tabular MDP solution methods** (Ch 3–8, covering DP, MC, TD, eligibility traces, Dyna, MCTS) to **function approximation** (Ch 9–11, the bridge to deep RL) to **frontiers** (Ch 12–15, psychology, neuroscience, applications, prospects). The unifying narrative: every method is a point in the space of "**how much do you bootstrap from existing estimates vs. how much do you sample from real returns?**" and "**do you have a model or not?**"

## Why it matters to this wiki

- **The canonical reference for [Curriculum Module 8 — Reinforcement learning vocabulary](../syntheses/curriculum/curriculum-08-rl-vocabulary.md).** Module 8 already names this textbook as "the standard reference" in its Recommended-reading list — this ingest fills in the primary-source link.
- **Foundation for every MBRL / world-model paper in the wiki.** [DreamerV3](dreamer-v3-paper.md), [TD-MPC2](td-mpc2-paper.md), and the JEPA-line world models ([LeWM](leworldmodel-paper.md), [DINO-WM](dino-wm-paper.md), [DINO-world](dino-world-paper.md), [JEPA-WMs](jepa-wms-paper.md), [PLDM](pldm-paper.md)) all use Sutton-Barto vocabulary verbatim — value functions, policies, planning, on-policy / off-policy / offline, TD bootstrapping, actor-critic. The wiki tracks ~10 papers that assume this vocabulary; this is their primary source.
- **Foundation for the RLHF / DPO / GRPO line that underlies VLA fine-tuning.** [Wolfe's SFT survey](wolfe-sft-blog.md) ends with RLHF; every wiki-tracked VLA ([π0](pi-zero-paper.md), [Helix](helix-blog.md), [GR00T](../entities/nvidia-groot.md)) uses some form of policy-gradient or preference-tuning RL at the end. PPO and SAC — the workhorses — derive from the policy-gradient chapter (Ch 11 here, Ch 13 in the 2018 final). Trace the lineage backwards and you land on this textbook.
- **The "RL = approximate optimal control over an unknown model" framing** is the explicit bridge to [Sussmann & Willems 1997 — 300 Years of Optimal Control](sussmann-willems-1997-300-years-optimal-control.md). Bellman dynamic programming (Ch 4) is the discrete-time / stochastic extension of the [Pontryagin Maximum Principle](sussmann-willems-1997-300-years-optimal-control.md); when you sample instead of taking expectations against a known model, you get RL. The two books together — Sutton-Barto + Sussmann-Willems — are the wiki's primary-source foundation for the entire control-and-decision-making thread.
- **The fly-brain / [biomechanical-simulation](../concepts/bio/biomechanical-simulation.md) thread** uses RL-trained controllers ([flybody](../entities/flybody.md), flygym, [NeuroMechFly](../entities/neuromechfly.md)); the *Whole-organism agentic AI* synthesis page describes them in Sutton-Barto language.

## Structure (2018 final 2nd edition)

**Front matter:**
- Preface to the Second Edition (pp. xiii–xvi) — *"The twenty years since the publication of the first edition of this book have seen tremendous progress in artificial intelligence, propelled in large part by advances in machine learning, including advances in reinforcement learning."* Notes the project began in 2012; the new edition adds new topics and expands coverage of topics they now understand better; sets off the more mathematical parts in shaded boxes the non-mathematical reader may skip.
- Preface to the First Edition (pp. xvii–xviii) — historical motivation: Sutton & Barto started at UMass in 1979 under A. Harry Klopf's *heterostatic theory*; the seminal observation was "the simplest idea — a learning system that *wants* something — had received surprisingly little computational attention."
- Summary of Notation (p. xix) — the **canonical RL notation** (`S_t`, `A_t`, `R_t`, `γ`, `π`, `v_π`, `q_π`, `v_*`, `q_*`, `δ_t`, `α`, `β`, `λ`, `z_t`) that every subsequent RL paper uses. The 2018 edition refines notation slightly from the 1st edition — eligibility traces now denoted `z_t` (vector) rather than `e_t`; the change is called out in the new preface.

**Chapter 1 — Introduction** (pp. 1–22)
- §1.1 RL as a problem class — closed-loop, no labels, delayed reward.
- §1.2 Examples (Phil's breakfast; checkers; gazelle calf walking; mobile robot).
- §1.3 Elements — **policy / reward / value function / model**. The four-subelement decomposition the rest of the book is organized around.
- §1.5 Extended example: Tic-Tac-Toe. The minimal worked example.
- §1.7 Early History of Reinforcement Learning — traces three threads (trial-and-error psychology; optimal control / DP; temporal-difference) and their 1980s convergence.

**Part I — Tabular Solution Methods (Chapters 2–8)**

- **Ch 2 — Multi-armed Bandits** (pp. 25–44). `k`-armed bandit. Action-value methods. ε-greedy (with the 10-armed testbed), optimistic initial values, UCB, gradient bandits, associative search (contextual bandits). Sets up exploration-exploitation; **does not** yet have state.
- **Ch 3 — Finite MDPs** (pp. 47–70). The agent-environment loop (Fig 3.1). Returns `G_t = R_{t+1} + γ R_{t+2} + …`. Episodic vs continuing tasks. Policies + value functions `v_π(s) = E_π[G_t | S_t = s]` and `q_π(s, a)`. **Bellman equations** + backup diagrams. Optimal value functions `v_*`, `q_*`, optimal Bellman equations.
- **Ch 4 — Dynamic Programming** (pp. 73–89). Policy evaluation (the iterative Bellman update). Policy improvement. Policy iteration. Value iteration. Asynchronous DP. **Generalized Policy Iteration (GPI)** — the framework that unifies policy iteration, value iteration, MC, and TD.
- **Ch 5 — Monte Carlo Methods** (pp. 91–116). MC prediction (sample average of returns). MC control with exploring starts. ε-soft policies. Off-policy prediction via importance sampling — the off-policy thread that becomes central in Ch 7 + Ch 11.
- **Ch 6 — Temporal-Difference Learning** (pp. 119–140). **The book's pivotal chapter.** Sutton & Barto's framing: *"If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning."* TD(0): `V(S_t) ← V(S_t) + α [R_{t+1} + γ V(S_{t+1}) − V(S_t)]`. **Bootstrapping** (update an estimate using another estimate). **SARSA** (on-policy TD control) and **Q-learning** (off-policy TD control). Expected Sarsa, Double Learning, Maximization Bias. The TD-vs-MC-vs-DP triangle.
- **Ch 7 — n-step Bootstrapping** (pp. 141–158). Restructured chapter title vs the draft. `n`-step TD prediction → `n`-step SARSA → `n`-step off-policy learning → per-decision methods with control variates → tree-backup → **A unifying algorithm: n-step Q(σ)**. (The book's interpolating family that subsumes Q-learning, Expected SARSA, and tree-backup.)
- **Ch 8 — Planning and Learning with Tabular Methods** (pp. 159–190). Models as samples or distributions. **Dyna-Q** (interleave real experience + planning from a learned model — the simplest MBRL). Prioritized sweeping. Expected vs. sample updates. Trajectory sampling. **Real-time Dynamic Programming (RTDP)**. **Planning at Decision Time**. Heuristic search. **Rollout algorithms**. **Monte Carlo Tree Search (§8.11)** — the AlphaGo / AlphaZero lineage primary reference. Summary of Part I + a dimensions-of-RL recap.

**Part II — Approximate Solution Methods (Chapters 9–13)**

- **Ch 9 — On-policy Prediction with Approximation** (pp. 197–242). Function approximation: replace tabular `V(s)` / `Q(s, a)` with `V_w(s)` / `Q_w(s, a)`. Stochastic-gradient + semi-gradient methods. Linear methods + tile coding. **Artificial neural networks (§9.7)** — convolutional ANNs, deep RL function approximation primer. **Memory-based** (§9.9) + **kernel-based** (§9.10) function approximation. **Interest and Emphasis** (§9.11) — the on-policy weighting that motivates emphatic-TD in Ch 11.
- **Ch 10 — On-policy Control with Approximation** (pp. 243–256). **Episodic semi-gradient control** + semi-gradient n-step SARSA. **Average-reward setting** (§10.3) — alternative to discounted formulation for continuing tasks. **Deprecating the Discounted Setting** (§10.4) — Sutton's pointed argument that discounting causes more trouble than it solves for control with function approximation. Differential semi-gradient n-step SARSA.
- **Ch 11 — Off-policy Methods with Approximation** (pp. 257–292) — substantial new chapter expanded over the draft. Semi-gradient methods, examples of off-policy divergence. **The Deadly Triad** (§11.3) — **function approximation + bootstrapping + off-policy training** can cause divergence. The conceptual diagnosis of why deep-RL training is fragile. Linear value-function geometry. Gradient descent in the Bellman error. **The Bellman error is not learnable** (§11.6) — a Sutton-style negative result that motivates the rest of the chapter. **Gradient-TD Methods** (§11.7) + **Emphatic-TD Methods** (§11.8). Variance reduction.
- **Ch 12 — Eligibility Traces** (pp. 303–342) — moved here from the draft's Ch 7. Substantially expanded. The λ-return + offline λ-return algorithm + TD(λ) + n-step truncated λ-return. **True online TD(λ)** (van Seijen & Sutton 2014). Eligibility traces for SARSA + Watkins's Q(λ) + Tree-Backup(λ) — all generalized to off-policy with control variates. Closing equivalence proofs.
- **Ch 13 — Policy Gradient Methods** (pp. 321–338) — **major new chapter in the 2018 final.** *(See "Ch 13 detail" below.)*

**Part III — Looking Deeper (Chapters 14–17)** *(retitled from "Frontiers" in the draft)*

- **Ch 14 — Psychology** (pp. 341–375). Expanded substantially: classical + instrumental conditioning, blocking + higher-order conditioning, the **Rescorla–Wagner model** + **the TD model** of classical conditioning (the experimental-psychology cousin of TD-learning), delayed reinforcement, cognitive maps, habitual vs goal-directed behavior.
- **Ch 15 — Neuroscience** (pp. 377–420). Expanded: neuroscience basics, **dopamine reward-prediction-error hypothesis** (the Schultz/Dayan/Montague identification, citations to Schultz 1998 and Dayan & Montague experimental work), addiction. **The link the wiki touches in [Whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md).**
- **Ch 16 — Applications and Case Studies** (pp. 421–458) — **major expansion vs the draft.** *(See "Ch 16 detail" below.)*
- **Ch 17 — Frontiers** (pp. 459–478). General Value Functions and auxiliary tasks. **Temporal Abstraction via Options** (Sutton, Precup, Singh 1999). **Observations and State** — POMDPs and predictive state representations. **Designing Reward Signals** (§17.4) — the "specifying a reward signal is brittle for real-world tasks" recognition that became central to robot-learning practice in the late 2010s. **RL and the Future of AI**.

## Ch 13 detail — Policy Gradient Methods (pp. 321–338)

The chapter the wiki cares about most — the lineage of REINFORCE → A2C / A3C → TRPO → PPO → SAC → GRPO, which underlies every RLHF-tuned LLM and every fine-tuning stage of the wiki's tracked VLAs.

**Setup (§13.1).** Methods so far in the book are *action-value methods* — they learn `Q(s, a)` and act greedily / ε-greedy. This chapter introduces methods that *directly parameterize a policy* `π(a | s, θ)` and learn `θ` by gradient ascent on a performance objective `J(θ)`:

```
θ_{t+1} = θ_t + α · ∇̂J(θ_t)         (Eq. 13.1 — stochastic gradient ascent on policy parameters)
```

The chapter's central new equations:

**Soft-max policy (Eq. 13.2)** — the canonical discrete-action parameterization:

```
π(a | s, θ) = exp(h(s, a, θ)) / Σ_b exp(h(s, b, θ))
```

**The Policy Gradient Theorem (Eq. 13.5, episodic case)** — the chapter's theoretical centerpiece, proved in a shaded box on p. 325 by repeated unrolling of the value-function recursion:

```
∇J(θ) ∝ Σ_s μ(s) Σ_a q_π(s, a) ∇π(a | s, θ)
```

where `μ(s)` is the on-policy state distribution and `q_π(s, a)` is the action-value function. The remarkable thing: **the gradient of performance with respect to policy parameters does not involve the derivative of the state distribution**. This is what makes the family tractable.

**REINFORCE (Eq. 13.8, §13.3)** — the simplest policy-gradient algorithm. Substitute a Monte-Carlo return `G_t` for `q_π(s, a)`, and use the log-derivative trick `∇log π = ∇π / π`:

```
θ_{t+1} = θ_t + α · G_t · ∇log π(A_t | S_t, θ_t)
```

Sample-and-shout: high variance, but unbiased. The basic recipe behind every modern policy-gradient method.

**REINFORCE with Baseline (Eq. 13.11, §13.4)** — subtract a *state-dependent* baseline `b(s)` (any function that doesn't depend on action) to reduce variance without introducing bias:

```
θ_{t+1} = θ_t + α · (G_t − b(S_t)) · ∇log π(A_t | S_t, θ_t)
```

The natural choice is `b(s) = v̂(s, w)` — a learned state-value function as the baseline. This is the conceptual gateway to actor-critic.

**Actor-Critic Methods (§13.5).** Replace the Monte-Carlo return `G_t` with a *bootstrapped* TD-style estimate `G_{t:t+1} = R_{t+1} + γ v̂(S_{t+1}, w)`. Now the state-value function plays a *critic* role (evaluating the action via the one-step return), while the policy is the *actor*. One-step actor-critic update:

```
θ_{t+1} = θ_t + α^θ · δ_t · ∇log π(A_t | S_t, θ_t)
w_{t+1} = w_t   + α^w · δ_t · ∇v̂(S_t, w_t)

where δ_t = R_{t+1} + γ v̂(S_{t+1}, w) − v̂(S_t, w)   (TD error)
```

This is the conceptual ancestor of **A2C / A3C / TRPO / PPO / SAC** — the family that dominates modern deep-RL practice and the RLHF / VLA fine-tuning pipeline. **PPO** (Schulman et al. 2017) adds a clipped surrogate objective + multiple epochs over the same on-policy batch; **SAC** adds an entropy bonus + soft Q-functions; **GRPO** (DeepSeek 2024) drops the value critic in favor of group-relative advantages — but they all live in the Ch 13 framework.

**Continuing problems + continuous actions (§13.6–13.7).** Reformulates policy gradient for the average-reward continuing case. For continuous action spaces: parameterize `π(a | s, θ)` as a Gaussian with mean `μ(s, θ_μ)` and (possibly state-dependent) standard deviation `σ(s, θ_σ)`. This is the recipe most robot-control papers use.

## Ch 16 detail — Applications and Case Studies (pp. 421–458)

The applications chapter expanded substantially in the 2018 final. Of the 8 case studies, three are directly relevant to the wiki's threads:

- **§16.1 — TD-Gammon** (Tesauro 1992, expanded). The proof-of-concept that put RL on the map — TD(λ) with a one-hidden-layer ANN on backgammon, self-play, eligibility traces, learning rate `0.1`. TD-Gammon 0.0 → 1.0 → 3.0 progression. Beat the best previous backgammon programs and reached world-class human level. The original deep-RL avant la lettre.

- **§16.5 — Human-level Video Game Play** — **DQN (Mnih et al. 2015, Nature)**. The watershed deep-RL paper: Q-learning + deep convolutional ANN + experience replay + target network, applied to 49 Atari 2600 games using identical hyperparameters per game (only the random initialization differs). Achieved at-or-above human level on a large fraction of the 49 games. The paper that started the post-2013 deep-RL renaissance. *Sutton & Barto cite this as the canonical demonstration that the framework scales.*

- **§16.6 — Mastering the Game of Go** — **AlphaGo (§16.6.1)** and **AlphaGo Zero (§16.6.2)**. AlphaGo (Silver et al. 2016) combined a deep policy network (trained by supervised learning on human games + policy gradient) + a deep value network + MCTS rollouts. Beat 18-time world champion Lee Sedol 4–1 in March 2016. AlphaGo Zero (Silver et al. 2017) removed the human-data initialization — trained purely from self-play + MCTS — and reached superhuman level in 3 days, beating the original AlphaGo 100–0. **The cleanest demonstration in the book that the Ch 8 MCTS material + the Ch 13 policy-gradient material + deep function approximation compose into something the field had not previously believed possible.**

Other case studies: Samuel's Checkers (§16.2, the historical 1959 system); Watson's Daily-Double Wagering (§16.3); Optimizing Memory Control (§16.4, learned DRAM controllers); Personalized Web Services (§16.7); Thermal Soaring (§16.8, RL-controlled glider drones).

## Key equations and concepts (the field's vocabulary)

| Concept | Notation / equation | Section (2018 final) |
|---|---|---|
| State, action, reward | `S_t ∈ S`, `A_t ∈ A(S_t)`, `R_t ∈ R ⊂ ℝ` | §3.1 |
| Policy | `π(a | s) = P(A_t = a | S_t = s)` | §3.5 |
| Return | `G_t = R_{t+1} + γ R_{t+2} + γ² R_{t+3} + …` | §3.3 |
| State-value function | `v_π(s) = E_π[G_t | S_t = s]` | §3.5 |
| Action-value function | `q_π(s, a) = E_π[G_t | S_t = s, A_t = a]` | §3.5 |
| Bellman equation (state-value) | `v_π(s) = Σ_a π(a|s) Σ_{s',r} p(s', r | s, a) [r + γ v_π(s')]` | §3.5 |
| Bellman optimality | `v_*(s) = max_a Σ_{s',r} p(s', r | s, a) [r + γ v_*(s')]` | §3.6 |
| TD error | `δ_t = R_{t+1} + γ V(S_{t+1}) − V(S_t)` | Ch 6 |
| TD(0) update | `V(S_t) ← V(S_t) + α δ_t` | Ch 6 |
| Q-learning | `Q(S_t, A_t) ← Q + α [R_{t+1} + γ max_a Q(S_{t+1}, a) − Q]` | §6.5 |
| SARSA | `Q(S_t, A_t) ← Q + α [R_{t+1} + γ Q(S_{t+1}, A_{t+1}) − Q]` | §6.4 |
| Expected SARSA | `Q(S_t, A_t) ← Q + α [R_{t+1} + γ Σ_a π(a|S_{t+1}) Q(S_{t+1}, a) − Q]` | §6.6 |
| Discount factor | `γ ∈ [0, 1)` | §3.3 |
| Eligibility trace (vector) | `z_t ← γλ z_{t-1} + ∇v̂(S_t, w_t)` | Eq 12.5 |
| TD(λ) | interpolates between TD(0) (λ=0) and MC (λ=1) | Ch 12 |
| **Policy gradient theorem** | `∇J(θ) ∝ Σ_s μ(s) Σ_a q_π(s, a) ∇π(a | s, θ)` | **Eq 13.5** |
| **REINFORCE update** | `θ_{t+1} = θ_t + α G_t ∇log π(A_t | S_t, θ_t)` | **Eq 13.8** |
| **REINFORCE with baseline** | `θ_{t+1} = θ_t + α (G_t − b(S_t)) ∇log π(A_t | S_t, θ_t)` | **Eq 13.11** |
| **One-step actor-critic** | `θ ← θ + α^θ δ_t ∇log π;  w ← w + α^w δ_t ∇v̂` | **§13.5** |
| Soft-max policy | `π(a|s,θ) = exp(h(s,a,θ)) / Σ_b exp(h(s,b,θ))` | Eq 13.2 |
| **Deadly Triad** | function approximation + bootstrapping + off-policy training → divergence risk | **§11.3** |

## Position in the optimal-control / RL lineage

```
1696   Bernoulli — brachystochrone (calculus of variations)
1956   Pontryagin et al. — Maximum Principle (deterministic OC)
1957   Bellman — Dynamic Programming, value function, principle of optimality
1959   Howard — policy iteration
1960   Klopf — heterostatic theory (the seed Sutton & Barto worked on)
1979   Sutton & Barto begin work at UMass
1988   Sutton — TD(λ) paper (the original TD-learning paper)
1989   Watkins — Q-learning thesis
1992   Tesauro — TD-Gammon (deep RL avant la lettre)
1998   Sutton & Barto 1st edition — the canonical textbook
2013   Mnih et al. — DQN on Atari (deep-RL renaissance; in Ch 16.5)
2015   Mnih et al. — Nature paper on Atari DQN
       In-progress 2nd-ed draft circulating (raw/SuttonBartoIPRLBook2ndEd.pdf)
2016   Silver et al. — AlphaGo beats Lee Sedol (Ch 16.6.1)
2017   Schulman et al. — PPO
       Silver et al. — AlphaGo Zero (Ch 16.6.2)
2018   Sutton & Barto 2nd edition (published; raw/RLbook2020.pdf, 2020 reprint)
2019   Levine — UC Berkeley CS285 (canonical deep-RL course)
2023+  DreamerV3 / TD-MPC2 / world-model + planning era
2024   Sutton & Barto — Turing Award
```

The wiki's RL-adjacent content (Module 8, Dreamer, TD-MPC, every JEPA-WM, every VLA's RLHF stage) sits in the post-2013 deep-RL branch of this tree, but all of it inherits the vocabulary fixed in this textbook.

## Entities mentioned

- **Richard S. Sutton** — U Massachusetts, then U Alberta, then DeepMind. Originator of TD-learning (1988), co-author of this book. Awarded the 2024 Turing Award (jointly with Barto). Not yet a wiki entity.
- **Andrew G. Barto** — U Massachusetts Amherst; Sutton's PhD advisor. Co-author. 2024 Turing Award. Not yet a wiki entity.
- **A. Harry Klopf** — the heterostatic-theory-of-adaptive-systems framing that started Sutton & Barto's work in 1979. Dedicated to in the book's frontispiece.
- **Christopher Watkins** — Q-learning (PhD thesis, Cambridge, 1989). Not yet a wiki entity.
- **Gerald Tesauro** — TD-Gammon (1992) (§14.1). The first large-scale "RL works" demonstration. Not yet a wiki entity.
- **Arthur Samuel** — checkers player (1959, 1967) (§14.2). The earliest RL-like learning system.
- **Demis Hassabis / DeepMind / Mnih et al.** — implicit but not central in the 2014 draft. The 2018 final cites DQN (Mnih et al. 2013/2015) substantially.
- **Wolfram Schultz, Peter Dayan, P. Read Montague** — the dopamine = TD-error identification (1997). Ch 13.

(None of these have wiki entity pages yet. Sutton + Barto are the most overdue stubs — they keep appearing in the wiki's lineage diagrams as "Sutton & Barto 1998" without a target.)

## Concepts touched (the entire RL vocabulary)
- [Optimal control](../concepts/robotics/optimal-control.md)

- **Reinforcement learning** — the field. **Not yet a concept page**; this source is the natural anchor. The most overdue concept-page creation in the wiki.
- **MDP / Markov Decision Process** — `(S, A, P, R, γ)`. Foundational.
- **Bellman equation / Bellman optimality equation** — the recursive structure of value functions.
- **Dynamic programming** — value iteration, policy iteration, generalized policy iteration. The "I have a model" branch.
- **Monte Carlo methods** — sample-based estimation of returns. The "no model, wait for episode end" branch.
- **Temporal-difference learning** — bootstrap-based estimation. The "no model, but update every step" branch. **The book's central novel idea.**
- **Eligibility traces** — credit assignment over time via decaying weights. Bridges MC and TD.
- **Q-learning, SARSA** — the two canonical TD-control algorithms.
- **Dyna / model-based RL** — interleaved real experience + simulated planning. The substrate of MBRL.
- **Monte Carlo Tree Search (MCTS)** — the AlphaGo / AlphaZero substrate. Ch 8.8.
- **Actor-critic methods** — policy + value learned together. The ancestor of PPO, A3C, SAC. Ch 11.
- **Function approximation** — replacing tabular `V`, `Q` with `V_θ`, `Q_θ`. The bridge to deep RL. Ch 9.
- **On-policy vs off-policy** — does the data come from the policy you're improving, or some other (behavior) policy?
- **Exploration vs exploitation** — ε-greedy, UCB, optimism, Boltzmann. Ch 2.
- **Importance sampling** — the off-policy correction. Ch 5.6, used throughout Part II.
- **POMDP (partially-observable MDP)** — state not directly observed. Mentioned in Ch 15.2 (frontiers).
- **Options framework / temporal abstraction** — Sutton/Precup/Singh 1999, mentioned in Ch 15.3 as frontier.

## Curriculum hookup

This is the **primary-source canonical textbook** for [Curriculum Module 8 — Reinforcement learning vocabulary](../syntheses/curriculum/curriculum-08-rl-vocabulary.md). Module 8's existing Recommended-reading list already names "Sutton & Barto" at position 5 (low priority because Module 8 is vocabulary-only); this ingest now lets that line link to a wiki source page rather than a bare author/title.

The book is also referenced implicitly by:
- **[Module 10 — World models, broad](../syntheses/curriculum/curriculum-10-world-models.md)** — MBRL framing.
- **[Module 11 — JEPA in depth](../syntheses/curriculum/curriculum-11-jepa-deep.md)** — when a JEPA-WM paper says "we train an off-policy goal-conditioned value function," that's Sutton-Barto language.
- **[Module 13 — Home robotics deployment reality](../syntheses/curriculum/curriculum-13-home-robotics-deployment.md)** — when discussing why pure-RL approaches struggle on real robots (sample inefficiency, reward specification, compounding error).

For readers who want a depth pass: the Module-8-recommended path is **Wikipedia → OpenAI Spinning Up → DreamerV3 paper → TD-MPC2 paper → Sutton & Barto** (with this textbook as the late, deep stop). Few wiki readers will read all 550 pages of the 2018 final; the natural target chapters for our wiki's threads are **Ch 1, 3, 4, 6, 8, 9, 11** (foundations + the MBRL / function-approximation / policy-gradient bridges).

## Why pure RL is hard for robots (recap from the wiki's existing position)

The textbook does not address this directly (it pre-dates the "RL is sample-inefficient for robots" consensus of 2018+), but the framework explains why:

- **Sample inefficiency.** A Bellman-style update is fast in a tabular MDP and easy in a simulator (DreamerV3 burns 10⁸+ steps in MuJoCo); on a real robot, ~10⁴ steps/hour is the budget — six orders of magnitude. **Sim-to-real** ([wiki/concepts/sim-to-real-transfer.md](../concepts/learning/sim-to-real-transfer.md)) is the standard workaround.
- **Reward specification.** Sutton & Barto's framework *assumes* a reward signal arrives from the environment. For real-world tasks (folding laundry, pouring coffee, helping with breakfast), specifying a dense scalar reward is brittle — the field has largely punted to **demonstrations (BC) + RL fine-tuning** instead, which is what every wiki-tracked VLA / IL line does.
- **Compounding error in long-horizon tasks.** The book's TD-learning derivation makes the bias-variance trade-off explicit (Ch 6.2): MC is unbiased but high-variance; TD is low-variance but biased through bootstrapping. For long-horizon real-robot tasks, both options break — which is why **learned world models** (the [Module 10–12](../syntheses/curriculum/curriculum-10-world-models.md) thread) exist.

## Open questions / TBD

- **A wiki `concepts/reinforcement-learning.md` hub page.** The most overdue concept-page creation in the wiki. Would unify Module 8 + DreamerV3 + TD-MPC2 + every VLA's RLHF stage + the implicit MBRL framing in the JEPA-WM literature. This source is the natural anchor.
- **A wiki `concepts/policy-gradient.md` page.** With Ch 13 now ingested, the Policy Gradient Theorem + REINFORCE + Actor-Critic vocabulary is ready to be hubbed. Would unify the SFT→RLHF pipeline (see [Wolfe SFT survey](wolfe-sft-blog.md), [HF TRL SFT Trainer](huggingface-trl-sft-trainer.md)) with the modern PPO / SAC / GRPO line. Defer until at least one PPO/RLHF primary-source paper is ingested.
- **The Deadly Triad as a standalone concept page.** Function approximation + bootstrapping + off-policy is the cleanest theoretical explanation of why deep-RL training is fragile (Ch 11.3). Increasingly cited in modern RL papers; would help readers of any DQN / off-policy paper in the wiki.
- **Entity stubs for Sutton + Barto.** They keep appearing in the wiki's lineage diagrams. A one-line stub each would let future ingests attach cleanly.
- **The "RL = optimal control under uncertainty" framing as a bridge synthesis.** Sussmann-Willems-1997 + Sutton-Barto together support a natural `syntheses/optimal-control-and-rl.md` page; would unify Module 8 + Module 10 + the optimal-control thread. Defer until at least one more bridging source surfaces.
- **TD-Gammon entity stub.** Mentioned in Ch 14.1 as the canonical "RL works at scale" demo (Tesauro 1992). Predates DQN by ~20 years; would be a useful "deep RL prehistory" pointer.
- **Bellman, Howard, Watkins** — primary-source ingests for the foundational RL math papers (Bellman 1957 *Dynamic Programming*; Howard 1960 *Dynamic Programming and Markov Processes*; Watkins 1989 PhD thesis on Q-learning) — candidate future ingests if the wiki picks up a "math foundations of RL" thread.
- **OpenAI Spinning Up** as a separate pedagogical-companion source — would pair with this textbook the way [karpathy/nanoGPT](karpathy-nanogpt.md) pairs with [Attention Is All You Need](attention-is-all-you-need.md): the canonical clean code companion to the canonical clean theory. Logged as candidate ingest.

---
title: "Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., 2014–2015 in-progress draft)"
type: source
url: http://incompleteideas.net/book/the-book.html
local_path: raw/SuttonBartoIPRLBook2ndEd.pdf
author: Richard S. Sutton, Andrew G. Barto
affiliation: U Massachusetts Amherst (Barto); U Alberta / DeepMind (Sutton); A Bradford Book, The MIT Press
published: 2014–2015 (in-progress draft of 2nd edition on file); 1st ed. 1998; final 2nd ed. printed 2018
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
tags: [reinforcement-learning, textbook, sutton-barto, foundational, mdp, value-function, bellman, dynamic-programming, monte-carlo, td-learning, q-learning, sarsa, eligibility-traces, actor-critic, mcts, mbrl, dedicated]
---

> [!note] Ingest depth + version
> The PDF on file (`raw/SuttonBartoIPRLBook2ndEd.pdf`, 352 pages, PDF metadata `CreationDate D:20150412`) is the **2014–2015 in-progress draft** of the 2nd edition (not the final 2018 print version). Content is mostly stable across versions; the **published 2018 2nd edition** is ~550 pages with reorganized Part III chapters (psychology, neuroscience, case studies, prospects), an expanded **policy-gradient chapter** (Ch 13 in the 2018 version, only a brief Ch 11 here), and chapters on **off-policy approximation methods** (Ch 10 here, expanded in 2018) and **deep RL applications**. Ingest below covers: front matter, Ch 1 (RL problem), Ch 3 (MDPs), Ch 4 (DP) → Ch 8 (planning + MCTS), Part II (function approximation), Part III (frontiers) at the **section-summary** level — not a verbatim reproduction. A future re-ingest against the 2018 final PDF should update the policy-gradient coverage and any added chapters.

## Summary

**"Reinforcement Learning: An Introduction"** by Richard S. Sutton and Andrew G. Barto is the **canonical textbook for the field of reinforcement learning** — sometimes called "the RL bible." The 1st edition (1998) established the field's vocabulary; the 2nd edition (2014–2015 in-progress draft; final print 2018) updates and substantially expands the coverage to include the post-2010 deep-RL renaissance, function approximation, and policy-gradient methods.

The book defines a **computational study of goal-directed learning from interaction**, distinct from both supervised learning (no labels, only scalar rewards) and unsupervised learning (there *is* a target — the cumulative reward). Sutton & Barto identify four sub-elements of an RL system (§1.3):

1. **Policy `π(a | s)`** — mapping from states to actions. What you're learning.
2. **Reward signal** — the scalar number the environment hands back. Defines the goal.
3. **Value function `v(s)` or `q(s, a)`** — long-term reward expected from a state (or state-action pair). The thing most algorithms estimate.
4. **(Optional) model of the environment** — predicts next state / reward given (state, action). Model-based vs model-free is the central axis the book organizes around.

The book runs from **tabular bandits** (Ch 2) to **tabular MDP solution methods** (Ch 3–8, covering DP, MC, TD, eligibility traces, Dyna, MCTS) to **function approximation** (Ch 9–11, the bridge to deep RL) to **frontiers** (Ch 12–15, psychology, neuroscience, applications, prospects). The unifying narrative: every method is a point in the space of "**how much do you bootstrap from existing estimates vs. how much do you sample from real returns?**" and "**do you have a model or not?**"

## Why it matters to this wiki

- **The canonical reference for [Curriculum Module 8 — Reinforcement learning vocabulary](../syntheses/curriculum-08-rl-vocabulary.md).** Module 8 already names this textbook as "the standard reference" in its Recommended-reading list — this ingest fills in the primary-source link.
- **Foundation for every MBRL / world-model paper in the wiki.** [DreamerV3](dreamer-v3-paper.md), [TD-MPC2](td-mpc2-paper.md), and the JEPA-line world models ([LeWM](leworldmodel-paper.md), [DINO-WM](dino-wm-paper.md), [DINO-world](dino-world-paper.md), [JEPA-WMs](jepa-wms-paper.md), [PLDM](pldm-paper.md)) all use Sutton-Barto vocabulary verbatim — value functions, policies, planning, on-policy / off-policy / offline, TD bootstrapping, actor-critic. The wiki tracks ~10 papers that assume this vocabulary; this is their primary source.
- **Foundation for the RLHF / DPO / GRPO line that underlies VLA fine-tuning.** [Wolfe's SFT survey](wolfe-sft-blog.md) ends with RLHF; every wiki-tracked VLA ([π0](pi-zero-paper.md), [Helix](helix-blog.md), [GR00T](../entities/nvidia-groot.md)) uses some form of policy-gradient or preference-tuning RL at the end. PPO and SAC — the workhorses — derive from the policy-gradient chapter (Ch 11 here, Ch 13 in the 2018 final). Trace the lineage backwards and you land on this textbook.
- **The "RL = approximate optimal control over an unknown model" framing** is the explicit bridge to [Sussmann & Willems 1997 — 300 Years of Optimal Control](sussmann-willems-1997-300-years-optimal-control.md). Bellman dynamic programming (Ch 4) is the discrete-time / stochastic extension of the [Pontryagin Maximum Principle](sussmann-willems-1997-300-years-optimal-control.md); when you sample instead of taking expectations against a known model, you get RL. The two books together — Sutton-Barto + Sussmann-Willems — are the wiki's primary-source foundation for the entire control-and-decision-making thread.
- **The fly-brain / [biomechanical-simulation](../concepts/biomechanical-simulation.md) thread** uses RL-trained controllers ([flybody](../entities/flybody.md), [flygym](../entities/flygym.md), [NeuroMechFly](../entities/neuromechfly.md)); the *Whole-organism agentic AI* synthesis page describes them in Sutton-Barto language.

## Structure (current draft)

**Front matter:**
- Preface (pp. viii–xi) — historical motivation: Sutton & Barto started at UMass in 1979 under A. Harry Klopf's *heterostatic theory*; the seminal observation was "the simplest idea — a learning system that *wants* something — had received surprisingly little computational attention."
- Series Forward (xii); Summary of Notation (xiii) — the **canonical RL notation** (`S_t`, `A_t`, `R_t`, `γ`, `π`, `v_π`, `q_π`, `v_*`, `q_*`, `δ_t`, `α`, `β`, `λ`, `E_t(s)`) that every subsequent RL paper uses.

**Chapter 1 — The Reinforcement Learning Problem** (pp. 1–25)
- §1.1 The problem class — closed-loop, no labels, delayed reward.
- §1.2 Examples (Phil's breakfast; checkers; gazelle calf walking; mobile robot).
- §1.3 Elements — policy / reward / value function / model. **The four-subelement decomposition the rest of the book is organized around.**
- §1.5 Extended example: Tic-Tac-Toe. The minimal worked example.
- §1.7 History of RL — long historical chapter; traces three threads (trial-and-error psychology; optimal control / DP; temporal-difference) and their 1980s convergence.

**Part I — Tabular Solution Methods (Chapters 2–8)**

- **Ch 2 — Multi-arm Bandits** (pp. 31–47). `n`-armed bandit. Action-value methods. ε-greedy, optimistic initial values, UCB, gradient bandits. Sets up exploration-exploitation; **does not** yet have state.
- **Ch 3 — Finite MDPs** (pp. 53–80). The agent-environment loop (Fig 3.1). Returns `G_t = R_{t+1} + γ R_{t+2} + …`. Episodic vs continuing tasks. The Markov property (§3.5). Value functions `v_π(s) = E_π[G_t | S_t = s]` and `q_π(s, a)`. **Bellman equations** (Eq 3.14 + Fig 3.4 backup diagrams). Optimal value functions `v_*`, `q_*`, optimal Bellman equations.
- **Ch 4 — Dynamic Programming** (pp. 89–107). Policy evaluation (Eq 4.5, the iterative Bellman update). Policy improvement (4.7–4.9). Policy iteration. Value iteration. Asynchronous DP. **Generalized Policy Iteration (GPI)** (Fig 4.7) — the framework that unifies policy iteration, value iteration, MC, and TD.
- **Ch 5 — Monte Carlo Methods** (pp. 113–138). MC prediction (sample average of returns). MC control with exploring starts. ε-soft policies. Off-policy prediction via importance sampling — the off-policy thread that becomes central in Ch 7–10.
- **Ch 6 — Temporal-Difference Learning** (pp. 143–161). The book's pivotal chapter. Sutton & Barto's framing: *"If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning."* TD(0): `V(S_t) ← V(S_t) + α [R_{t+1} + γ V(S_{t+1}) − V(S_t)]` (Eq 6.2). **Bootstrapping** (update an estimate using another estimate). **SARSA** (on-policy TD control) and **Q-learning** (off-policy TD control). The TD-vs-MC-vs-DP triangle.
- **Ch 7 — Eligibility Traces** (pp. 167–190). `n`-step TD prediction. **TD(λ)** — forward and backward views. SARSA(λ), Watkins's Q(λ). The "unifying" chapter that bridges MC (λ=1) and TD(0) (λ=0).
- **Ch 8 — Planning and Learning with Tabular Methods** (pp. 195–220). Models as samples or distributions. **Dyna-Q** (interleave real experience + planning from a learned model — the simplest MBRL). Prioritized sweeping. Trajectory sampling. **Monte Carlo Tree Search (§8.8)** — the AlphaGo / AlphaZero lineage primary reference.

**Part II — Approximate Solution Methods (Chapters 9–11)**

- **Ch 9 — On-policy approximation of action values** (pp. 225–249). Function approximation: replace tabular `V(s)` / `Q(s, a)` with `V_w(s)` / `Q_w(s, a)`. Gradient-descent TD. Linear methods + tile-coding. Where the deep-RL line picks up.
- **Ch 10 — Off-policy approximation** (p. 255 — in this draft, chapter is largely a placeholder; substantially expanded in the 2018 final).
- **Ch 11 — Policy approximation** (pp. 257–263). **Actor-critic methods** (§11.1) — the policy-gradient line that becomes PPO / A3C / SAC / TRPO in the 2010s. Eligibility traces for actor-critic. R-learning + average-reward setting. (In the 2018 final, this becomes a full Ch 13 with policy-gradient theorems and modern algorithms.)

**Part III — Frontiers (Chapters 12–15)**

- **Ch 12 — Psychology** (p. 269). Connections to operant conditioning, Thorndike's law of effect, Pavlovian conditioning, secondary reinforcement. The historical link between RL and behaviorist psychology.
- **Ch 13 — Neuroscience** (p. 271). Dopamine = reward prediction error (the Schultz/Dayan/Montague identification of TD-error with phasic dopamine signals). The link the wiki touches in [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md).
- **Ch 14 — Applications and Case Studies** (pp. 273–301). TD-Gammon (Tesauro 1992 — the proof-of-concept that started modern RL). Samuel's checkers player. The Acrobot. Elevator dispatching. Dynamic channel allocation. Job-shop scheduling. The **canonical "RL works in the real world"** case studies, all pre-deep-RL.
- **Ch 15 — Prospects** (pp. 303–309). The unified view; state estimation; temporal abstraction (options framework — Sutton, Precup, Singh 1999); predictive representations of state. Open frontiers as of ~2015.

## Key equations and concepts (the field's vocabulary)

| Concept | Notation / equation | Section |
|---|---|---|
| State, action, reward | `S_t ∈ S`, `A_t ∈ A(S_t)`, `R_t ∈ R ⊂ ℝ` | §3.1 |
| Policy | `π(a | s) = P(A_t = a | S_t = s)` | §3.1 |
| Return | `G_t = R_{t+1} + γ R_{t+2} + γ² R_{t+3} + …` | §3.3 |
| State-value function | `v_π(s) = E_π[G_t | S_t = s]` | §3.7 |
| Action-value function | `q_π(s, a) = E_π[G_t | S_t = s, A_t = a]` | §3.7 |
| Bellman equation (state-value) | `v_π(s) = Σ_a π(a|s) Σ_{s',r} p(s', r | s, a) [r + γ v_π(s')]` | §3.7 |
| Bellman optimality | `v_*(s) = max_a Σ_{s',r} p(s', r | s, a) [r + γ v_*(s')]` | §3.8 |
| TD(0) update | `V(S_t) ← V(S_t) + α [R_{t+1} + γ V(S_{t+1}) − V(S_t)]` | Eq 6.2 |
| TD error | `δ_t = R_{t+1} + γ V(S_{t+1}) − V(S_t)` | Ch 6 |
| Q-learning | `Q(S_t, A_t) ← Q + α [R_{t+1} + γ max_a Q(S_{t+1}, a) − Q]` | Eq 6.8 |
| SARSA | `Q(S_t, A_t) ← Q + α [R_{t+1} + γ Q(S_{t+1}, A_{t+1}) − Q]` | Eq 6.7 |
| Discount factor | `γ ∈ [0, 1)` | §3.3 |
| Eligibility trace | `E_t(s)` accumulates "credit" for state `s` to apply later updates | Ch 7 |
| TD(λ) | interpolates between TD(0) (λ=0) and MC (λ=1) | Ch 7 |

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
2013   Mnih et al. — DQN on Atari (deep-RL renaissance)
2015   This draft — 2nd edition in progress
2017   Schulman et al. — PPO
2018   Sutton & Barto 2nd edition (published)
2019   Levine — UC Berkeley CS285 (canonical deep-RL course)
2023+  DreamerV3 / TD-MPC2 / world-model + planning era
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

This is the **primary-source canonical textbook** for [Curriculum Module 8 — Reinforcement learning vocabulary](../syntheses/curriculum-08-rl-vocabulary.md). Module 8's existing Recommended-reading list already names "Sutton & Barto" at position 5 (low priority because Module 8 is vocabulary-only); this ingest now lets that line link to a wiki source page rather than a bare author/title.

The book is also referenced implicitly by:
- **[Module 10 — World models, broad](../syntheses/curriculum-10-world-models.md)** — MBRL framing.
- **[Module 11 — JEPA in depth](../syntheses/curriculum-11-jepa-deep.md)** — when a JEPA-WM paper says "we train an off-policy goal-conditioned value function," that's Sutton-Barto language.
- **[Module 13 — Home robotics deployment reality](../syntheses/curriculum-13-home-robotics-deployment.md)** — when discussing why pure-RL approaches struggle on real robots (sample inefficiency, reward specification, compounding error).

For readers who want a depth pass: the Module-8-recommended path is **Wikipedia → OpenAI Spinning Up → DreamerV3 paper → TD-MPC2 paper → Sutton & Barto** (with this textbook as the late, deep stop). Few wiki readers will read all 550 pages of the 2018 final; the natural target chapters for our wiki's threads are **Ch 1, 3, 4, 6, 8, 9, 11** (foundations + the MBRL / function-approximation / policy-gradient bridges).

## Why pure RL is hard for robots (recap from the wiki's existing position)

The textbook does not address this directly (it pre-dates the "RL is sample-inefficient for robots" consensus of 2018+), but the framework explains why:

- **Sample inefficiency.** A Bellman-style update is fast in a tabular MDP and easy in a simulator (DreamerV3 burns 10⁸+ steps in MuJoCo); on a real robot, ~10⁴ steps/hour is the budget — six orders of magnitude. **Sim-to-real** ([wiki/concepts/sim-to-real-transfer.md](../concepts/sim-to-real-transfer.md)) is the standard workaround.
- **Reward specification.** Sutton & Barto's framework *assumes* a reward signal arrives from the environment. For real-world tasks (folding laundry, pouring coffee, helping with breakfast), specifying a dense scalar reward is brittle — the field has largely punted to **demonstrations (BC) + RL fine-tuning** instead, which is what every wiki-tracked VLA / IL line does.
- **Compounding error in long-horizon tasks.** The book's TD-learning derivation makes the bias-variance trade-off explicit (Ch 6.2): MC is unbiased but high-variance; TD is low-variance but biased through bootstrapping. For long-horizon real-robot tasks, both options break — which is why **learned world models** (the [Module 10–12](../syntheses/curriculum-10-world-models.md) thread) exist.

## Open questions / TBD

- **Re-ingest against the 2018 published 2nd edition.** The draft on file is 2015; the 2018 final adds substantial policy-gradient depth (Ch 13 in 2018 = "Policy Gradient Methods"), reorganizes Part III, adds chapters on deep RL applications, and incorporates corrections. Re-ingest worth doing if the wiki's RL coverage deepens.
- **A wiki `concepts/reinforcement-learning.md` hub page.** The most overdue concept-page creation in the wiki. Would unify Module 8 + DreamerV3 + TD-MPC2 + every VLA's RLHF stage + the implicit MBRL framing in the JEPA-WM literature. This source is the natural anchor.
- **Entity stubs for Sutton + Barto.** They keep appearing in the wiki's lineage diagrams. A one-line stub each would let future ingests attach cleanly.
- **The "RL = optimal control under uncertainty" framing as a bridge synthesis.** Sussmann-Willems-1997 + Sutton-Barto together support a natural `syntheses/optimal-control-and-rl.md` page; would unify Module 8 + Module 10 + the optimal-control thread. Defer until at least one more bridging source surfaces.
- **TD-Gammon entity stub.** Mentioned in Ch 14.1 as the canonical "RL works at scale" demo (Tesauro 1992). Predates DQN by ~20 years; would be a useful "deep RL prehistory" pointer.
- **Bellman, Howard, Watkins** — primary-source ingests for the foundational RL math papers (Bellman 1957 *Dynamic Programming*; Howard 1960 *Dynamic Programming and Markov Processes*; Watkins 1989 PhD thesis on Q-learning) — candidate future ingests if the wiki picks up a "math foundations of RL" thread.
- **OpenAI Spinning Up** as a separate pedagogical-companion source — would pair with this textbook the way [karpathy/nanoGPT](karpathy-nanogpt.md) pairs with [Attention Is All You Need](attention-is-all-you-need.md): the canonical clean code companion to the canonical clean theory. Logged as candidate ingest.

---
title: Learning to play Table Tennis using Multi-agent RL (USC project)
type: source
url: null
author: Basu, Coimbatore Selvakumar, Fu, Chunduru Balaji, Ramesh, Voona, Wu (USC)
published: null
ingested: 2026-07-17
local_path: raw/RL_TableTennis.pdf
sha256: 5efcbdf8d9972adf2b7ba0c2307fb396641daf14db87601aa39f24853b8be555
venue: University of Southern California — semester course project report
license: null
format: PDF (9 pages, IEEE-conference template)
tags: [reinforcement-learning, multi-agent-rl, self-play, unity-ml-agents, ppo, sac, curriculum-learning, table-tennis, simulation]
---

# Learning to play Table Tennis using Multi-agent Reinforcement Learning

## Summary

A seven-author USC **course-project report** that trains table-tennis-playing agents inside a custom **[Unity ML-Agents](../entities/unity-ml-agents.md)** environment, framing ping-pong as a two-player **[Markov Game](../concepts/learning/multi-agent-rl.md)** and attacking it with self-play RL. The team builds both a **dual-agent** (competitive self-play, ranked by ELO) and a **single-agent** (return-a-served-ball) setup, and sweeps hyperparameters across **[PPO](../syntheses/curriculum/curriculum-08-rl-vocabulary.md)**, **[SAC](../entities/sac.md)**, and Unity's **MA-POCA** multi-agent trainer, plus **curriculum learning** on the reward and bat size. The headline result: an **SAC** self-play agent reaches an ELO of **2352** after 8M steps (vs. an initial 1200), and single-agent SAC learns to reliably return served balls even under randomized velocity and spin. It is a modest, unrefereed student project — useful to the wiki as a concrete, end-to-end **self-play MARL in a game engine** worked example, not as a research result.

> [!note] Confidence / provenance
> This is a **semester course-project report**, not a peer-reviewed paper — no venue, no publication date, incomplete/duplicated citation keys in the PDF (e.g. AlphaGo cited as `[?]`), and self-reported ELO/reward numbers with no baseline comparison against prior table-tennis-robot work. Treat the numbers as illustrative of what Unity ML-Agents self-play can produce, not as benchmarks.

## Key claims

- **Problem framing (§IV.A).** Table tennis modeled as a **Markov Game** — an N-agent extension of an MDP `<S, N, {Aᵢ}, {Rᵢ}, {Oᵢ}, ρ, λ, Z>` with per-agent local observations and rewards; the not-strictly-zero-sum nature (a foul is not exactly the opponent's gain) motivates trying **mixed** cooperative/competitive methods, not only pure competition. (p. 4)
- **Environment (§III).** Built in **Unity 3D 2020.3.20** + the **Unity ML-Agents Toolkit**, trained via PyTorch, logged in TensorBoard. Observations = positions + velocities of bat A, bat B, and the ball; actions = bat translation along X/Y and rotation about X (Z-axis motion left as future work). (pp. 2–3)
- **Reward design (§III.B.3).** Fouls (ball into net, ball out of bounds, double-bounce on one side) reward the *opponent*; bookkeeping tracks `Last Hit Agent`, `Last Collided With`, and `Next Agent Turn`. Single-agent variant instead rewards hitting the ball / clearing the net / landing on the opponent's table, penalizing misses and double-hits. (pp. 3, 6–7)
- **Algorithms surveyed (§IV.B).** PPO (on-policy, clipped surrogate), SAC (off-policy, max-entropy), DQN (value-based + experience replay + target network), **MA-POCA** (Unity's centralized-critic multi-agent trainer with posthumous credit assignment, self-play-compatible), and DDPG — though only PPO / SAC / MA-POCA were actually trained; DQN/DDPG are listed as future Unity-conversion work. (pp. 4–5, 8)
- **Self-play + ELO (§V.A).** Dual-agent training uses Unity self-play with ELO as the fitness signal (initial ELO 1200). Best model: **SAC**, batch 128, LR 3e-4, 1-bounce, 2 layers → **ELO 2352 @ 8M steps** and still rising. PPO plateaued near the initial ELO (~1170–1208 across the sweep) and "could not guide the agents to play the game well." (pp. 5–6)
- **Single-agent results (§V.F.2).** SAC reaches near-max cumulative reward: **~1.0** fixed-velocity serve, **0.8** randomized-velocity (6M steps), **0.9** randomized-spin (8M steps) — i.e. the agent learns to read spin and return it. (p. 8)
- **Curriculum learning (§IV.B.6, §V.D).** Two curricula, both keyed on `current_steps / max_steps`: (1) **reward reduction** — start with high reward for merely hitting the ball, decay it while raising the reward for scoring, to shift the agent from "make contact" to "play legal, scoring shots"; (2) **bat-size shrink** — start with an oversized bat, shrink toward normal size to force larger range of motion. Reward-reduction curriculum gave more stable, higher final ELO than flat training. (pp. 5, 6–7)
- **Limitations (§VI).** 2-D (X/Y) motion only; compute-limited hyperparameter search; no DQN/DDPG self-play (blocked on Unity model-conversion); future work = add Z-axis, doubles play, external-framework (Gym) models.

## Entities mentioned

- [Unity ML-Agents](../entities/unity-ml-agents.md) — the game-engine RL framework the whole project runs on.
- [SAC](../entities/sac.md) — best-performing algorithm here (self-play ELO 2352).
- [Gymnasium](../entities/gymnasium.md) — named as the "external framework" the team wanted to plug in but couldn't (Unity model-conversion gap).

## Concepts touched

- [Multi-agent reinforcement learning](../concepts/learning/multi-agent-rl.md) — the primary concept: MARL, Markov Games, self-play, CTDE, MA-POCA, independent learning.
- [Reinforcement-learning vocabulary (curriculum Module 8)](../syntheses/curriculum/curriculum-08-rl-vocabulary.md) — PPO / SAC / DQN / DDPG / actor-critic, all used here.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the paper's Related Work surveys the robot-table-tennis lineage (Anderson 1988 → Gao 2020 model-free RL → Büchler pneumatic muscles) that sits on the real-hardware side of this sim-only project.

## Open questions

- How well would the self-play policies transfer out of the (physically simplified, 2-D) Unity environment toward the real robot-table-tennis systems the Related Work cites? The paper does not attempt sim-to-real.
- MA-POCA barely moved ELO (~1212–1270) here — is that a tuning artifact or a genuine mismatch between posthumous-credit-assignment and a fixed-size 2-player game?

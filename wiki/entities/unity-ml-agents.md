---
title: Unity ML-Agents Toolkit
type: entity
subtype: simulator-framework
created: 2026-07-17
updated: 2026-07-17
sources: 1
tags: [simulator, game-engine, reinforcement-learning, multi-agent-rl, self-play, ppo, sac, unity]
---

# Unity ML-Agents Toolkit

**Unity ML-Agents** — an open-source toolkit from Unity Technologies that turns a **Unity game-engine scene into an RL training environment**: game objects become agents, C# scripts expose observations/actions/rewards, and a Python (`mlagents-learn` + PyTorch) side trains policies that can then be embedded back into the Unity scene as inference models ([Juliani et al. 2020, "Unity: A general platform for intelligent agents"](../sources/usc-table-tennis-marl.md)).

## Why it matters in this wiki

It sits in the **game-engine simulator** slice of the [agentic-robotics simulator landscape](../syntheses/simulators/simulators-for-agentic-robotics-2026.md) — the same "environment authoring + built-in trainers" role that Gym/Gymnasium plays for Python-first work, but scene-first and 3D-native. Its distinguishing feature for the wiki is **batteries-included multi-agent + self-play**: PPO and SAC ship as trainers, **MA-POCA** provides a centralized-critic multi-agent trainer, and a built-in **self-play + ELO** loop lets you train competitive agents without wiring your own tournament harness. That makes it the low-friction entry point for [multi-agent RL](../concepts/learning/multi-agent-rl.md) experiments, as in the wiki's [USC table-tennis project](../sources/usc-table-tennis-marl.md).

## Key facts

- **Built-in trainers:** PPO (on-policy), SAC (off-policy), and **MA-POCA** (MultiAgent POsthumous Credit Assignment) — a centralized "coach" critic that can hand team or individual rewards and tolerates agents being added/removed mid-episode; combinable with self-play.
- **Self-play:** first-class, with **ELO** as the fitness/tracking signal for competitive training.
- **Curriculum learning:** supported via progress-keyed (`current_steps / max_steps`) lesson schedules over reward or environment parameters.
- **Stack:** Unity (C# scene + `Agent` classes: `CollectObservations`, `OnActionReceived`, `Heuristic`) ↔ Python `mlagents-learn` (config-file-driven) + PyTorch; TensorBoard logging.
- **Gap noted in practice:** converting **external-framework** (e.g. [Gymnasium](gymnasium.md)) models or custom algorithms (DQN, DDPG) back into Unity-embeddable models is not turnkey — a friction point flagged by the [USC table-tennis project](../sources/usc-table-tennis-marl.md).

## Related

- [Multi-agent reinforcement learning](../concepts/learning/multi-agent-rl.md) — the concept its self-play / MA-POCA machinery serves.
- [SAC](sac.md) — one of its two built-in deep-RL trainers.
- [Gymnasium](gymnasium.md) — the Python-first counterpart; ML-Agents is the game-engine-first alternative.
- [Simulators for agentic robotics — 2026 landscape](../syntheses/simulators/simulators-for-agentic-robotics-2026.md) — where game-engine sims sit.

## Mentioned in

- [Learning to play Table Tennis using Multi-agent RL (USC project)](../sources/usc-table-tennis-marl.md) — full worked example: Unity 3D + ML-Agents self-play (PPO / SAC / MA-POCA) + curriculum.

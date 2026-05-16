---
title: Gymnasium
type: entity
subtype: api-standard
created: 2026-05-07
updated: 2026-05-10
sources: 3
tags: [farama, gymnasium, gym, rl, api-standard]
---

Standard API for **single-agent reinforcement learning environments**, with reference environments. Maintained by the [Farama Foundation](farama-foundation.md) as the successor to OpenAI's `gym` ([Farama Foundation Projects Page](../sources/farama-projects-page.md)).

## Relationship to OpenAI gym
- Forked from OpenAI `gym` after OpenAI deprecated active maintenance.
- API is gym-compatible at the level of `Env` semantics but with fixes (e.g. `step()` returning `(obs, reward, terminated, truncated, info)` — five-tuple — vs. gym's four-tuple).
- The legacy `gym` package still ships on PyPI but is unmaintained. Robotics codebases that pin `gym==0.21.0` (e.g. via the [LeWM](../syntheses/world-models/leworldmodel-howto.md) dep tree) inherit known PEP 440 metadata bugs and SWIG-build issues — see that howto for the workarounds.

## Why it matters here
- **The de-facto interface for RL envs.** Anything that calls itself a Gym/Gymnasium environment exposes `reset()` / `step()` / `action_space` / `observation_space` and slots into the same training/eval scaffolding.
- Downstream implementations include [Gymnasium-Robotics](gymnasium-robotics.md) (in-Farama), [MuJoCo Playground](mujoco-playground.md) (DeepMind, MJX-backed), and bindings via Shimmy for envs like DM Control.
- `gymnasium[all]` is a common transitive dep — it pulls box2d-py, ALE, MuJoCo, etc., and is what triggers the SWIG requirement noted in [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) gotcha #2.

## Related
- [Farama Foundation](farama-foundation.md) — maintainer.
- [PettingZoo](pettingzoo.md) — multi-agent counterpart from the same org.
- [Gymnasium-Robotics](gymnasium-robotics.md) — robotics envs implementing this API.

## Mentioned in
- [Farama Foundation Projects Page](../sources/farama-projects-page.md)
- [Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md)

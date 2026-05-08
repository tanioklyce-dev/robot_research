---
title: Gymnasium
type: entity
subtype: api-standard
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [farama, gymnasium, gym, rl, api-standard]
---

Standard API for **single-agent reinforcement learning environments**, with reference environments. Maintained by the [[farama-foundation|Farama Foundation]] as the successor to OpenAI's `gym` ([[farama-projects-page|Farama Foundation Projects Page]]).

## Relationship to OpenAI gym
- Forked from OpenAI `gym` after OpenAI deprecated active maintenance.
- API is gym-compatible at the level of `Env` semantics but with fixes (e.g. `step()` returning `(obs, reward, terminated, truncated, info)` — five-tuple — vs. gym's four-tuple).
- The legacy `gym` package still ships on PyPI but is unmaintained. Robotics codebases that pin `gym==0.21.0` (e.g. via the [[leworldmodel-howto|LeWM]] dep tree) inherit known PEP 440 metadata bugs and SWIG-build issues — see that howto for the workarounds.

## Why it matters here
- **The de-facto interface for RL envs.** Anything that calls itself a Gym/Gymnasium environment exposes `reset()` / `step()` / `action_space` / `observation_space` and slots into the same training/eval scaffolding.
- Downstream implementations include [[gymnasium-robotics|Gymnasium-Robotics]] (in-Farama), [[mujoco-playground|MuJoCo Playground]] (DeepMind, MJX-backed), and bindings via Shimmy for envs like DM Control.
- `gymnasium[all]` is a common transitive dep — it pulls box2d-py, ALE, MuJoCo, etc., and is what triggers the SWIG requirement noted in [[leworldmodel-howto|LeWM howto]] gotcha #2.

## Related
- [[farama-foundation|Farama Foundation]] — maintainer.
- [[pettingzoo|PettingZoo]] — multi-agent counterpart from the same org.
- [[gymnasium-robotics|Gymnasium-Robotics]] — robotics envs implementing this API.

## Mentioned in
- [[farama-projects-page|Farama Foundation Projects Page]]
- [[gymnasium-robotics-docs|Gymnasium-Robotics Documentation]]
- [[leworldmodel-howto|LeWorldModel — train and run howto]]

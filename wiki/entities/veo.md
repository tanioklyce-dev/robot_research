---
title: Veo
type: entity
subtype: model
created: 2026-08-03
updated: 2026-08-08
sources: 2
tags: [veo, video-model, world-model, generative-simulation, policy-evaluation, google-deepmind]
---

**Veo** — [Google DeepMind](google-deepmind.md)'s frontier **video foundation model**. In this wiki it appears in its robotics specialization, **Veo (Robotics)**, used as a **generative world simulator for evaluating robot policies** ([paper](../sources/veo-robotics-policy-evaluation-paper.md)).

## The robotics adaptation
Beyond base Veo, the system adds **robot action conditioning**, **multi-view consistency**, and integrated **generative image editing + multi-view completion** to synthesize realistic variations of real scenes. Multi-view consistency is exactly the limitation [RoboART](roboart.md) flagged ten months earlier.

## Validation
Against **1600+ real-world evaluations**, 8 [Gemini Robotics](gemini-robotics.md) checkpoints, 5 tasks, 80 scene-instruction combinations, 8-second closed-loop rollouts scored by humans:

| Metric | Value |
|---|---|
| Pearson (predicted vs real success) | **0.88** |
| MMRV (ranking consistency) | **0.03** |

> [!warning] Ranks, does not measure
> "The absolute values of predicted success rates are **lower** than their real counterparts." Veo(Robotics) is a validated *relative* instrument — like [RoboArena](roboarena.md)'s pairwise preference, it gives ordering rather than deployable magnitude.

## Why it matters in this wiki
It makes safety evaluation possible where hardware testing is **infeasible rather than merely costly** — probing whether a policy leaves broken glass on the floor should not require broken glass on a floor. It is the wiki's third robot-policy-evaluation paradigm, after real rollouts and pairwise preference.

Known failure modes: contact-rich interaction with small objects (objects can spontaneously appear mid-grasp), 8-second horizon limit, human scoring still required.

## Related
- [World model simulators](../concepts/world-models/world-model-simulators.md) — a video WM as evaluation harness rather than policy or data generator.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [Semantic safety](../concepts/safety/semantic-safety.md).
- [RoboArena](roboarena.md) — the other rank-not-magnitude paradigm.
- [Gemini Robotics](gemini-robotics.md) — the policies evaluated.

## Mentioned in
- [Evaluating Gemini Robotics Policies in a Veo World Simulator](../sources/veo-robotics-policy-evaluation-paper.md) — primary source.

## Veo 3.1 in third-party benchmarking

[WorldArena](worldarena.md) evaluates **Veo 3.1** among 14 embodied world models: **3rd on EWMScore (58.87)**, with the field's best interaction quality (0.7872), best instruction following (0.9328), and best perspectivity (0.8276) — yet weak trajectory accuracy (0.1231) and "limited improvements in embodied-specific metrics." It is the clearest single instance of the perception–functionality gap: near-perfect at looking and sounding right, mediocre at the dynamics ([WorldArena paper](../sources/worldarena-paper.md)).

> [!note] Two learned evaluators, opposite biases
> Veo-as-evaluator predicts **low** absolute success rates (ranking r = 0.88 against 1,600+ real evaluations). WorldArena finds its learned evaluators predict **high** — "partial overfitting to successful trajectories." Both preserve ranking better than level; the sign disagreement is unexplained. See [world-model evaluation](../concepts/world-models/world-model-evaluation.md) and [Ctrl-World](ctrl-world.md).

## Mentioned in (additional)

- [WorldArena paper](../sources/worldarena-paper.md)

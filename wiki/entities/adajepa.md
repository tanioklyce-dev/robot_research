---
title: AdaJEPA
type: entity
subtype: model
created: 2026-08-26
updated: 2026-08-26
sources: 2
tags: [adajepa, jepa, world-model, test-time-adaptation, mpc, distribution-shift, planning, lecun]
---

**AdaJEPA** — a latent [world model](../concepts/world-models/world-model.md) that **adapts at test time inside the MPC loop**. Plan; execute the first action chunk; use the observed next-state transition as a self-supervised signal; take **one gradient step**; replan. The adaptation loss is the *same next-embedding prediction loss used in pretraining* — no demonstrations, no reward, no new objective. Wang, Bounou, [LeCun](yann-lecun.md), Mengye Ren (NYU), June 2026 ([paper](../sources/adajepa-paper.md)).

## Why it matters here

It is the wiki's first **online** answer to learned-world-model fragility. Everything else here is offline — better regularization ([SIGReg](leworldmodel.md), [SMWM](smwm.md)), better data ([R2S2R](../concepts/robotics/real-to-sim-to-real.md) randomization), better measurement ([stable-worldmodel](../sources/stable-worldmodel-paper.md), [WorldArena](worldarena.md)). AdaJEPA repairs the model *during the episode*.

And it targets the wiki's sharpest counter-result directly: [stable-worldmodel](../sources/stable-worldmodel-paper.md) measured [LeWM](leworldmodel.md) collapsing **50.8% → 6–26%** on Push-T under color/size/shape shift. AdaJEPA tests those exact shift families (shapes T→L/Z/+/I/smallT/square; visual blur/noise/darkening/red-agent/red-block/red-anchor) and reports substantial recovery — *"nearly doubles the planning success rate"* on unseen shapes.

## Findings

- **In-distribution it is safe**: >20% gain where the frozen model is suboptimal, **no harm** where it is already near-optimal.
- **Success keeps rising over MPC steps** while the frozen model **saturates early** — adaptation lets a planner recover from initially wrong predictions instead of committing to them.
- **Visual shifts split by kind.** Gains under blur, noise, lighting; **modest under red-block / red-anchor**, and the reason is precise: the model uses color to distinguish the fixed anchor from the manipulated object, so the *identity* signal itself is destroyed — adaptation cannot repair what is no longer present. That needs augmentation or invariance regularization instead.
- **Dynamics shifts:** the frozen baseline is already strong, attributed to **in-context** adaptation over the 3-frame history. AdaJEPA still adds gains.
- **Layout shifts:** adapting **earlier predictor layers** beats the default last-layer update; adapted trajectories run closer to the shortest path.
- **Model-agnostic** across world-model variants.

## Mechanism

Replay buffer with recency-focused sampling and hard-N retention; **stop-gradient as the default anti-collapse stabilizer during online adaptation** (notable — single-sample online updates are exactly where a JEPA could collapse); updates restricted to a small subset of encoder/predictor parameters. Frameskip 5, history 3. Both GD and CEM planners.

> [!warning] It inherits the train-and-judge problem in a new form
> A world model fitted to the current episode cannot also be a neutral evaluator of that episode. AdaJEPA's own results are measured in the real environment so this is not a flaw in the paper — but an adaptive world model used as an [evaluation harness](../concepts/robotics/robot-policy-evaluation.md) would construct precisely the circularity [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md#the-learned-simulator-failure-mode-teaching-to-a-flawed-test) warns about.

## Open questions

- **Results are curves, not tables** — "over 20% gain," "nearly doubles"; few extractable point estimates, no intervals.
- **No compute or latency accounting.** A gradient step per replanning step is not free, and latent world models' appeal is partly speed.
- **No reported failure mode** — adapting on one recent transition could chase noise; no case where it hurts is shown.
- **Not run against the stable-worldmodel benchmark**, despite testing the same shifts on the same environment — so the fraction of that collapse recovered is unknown.
- PushT and PointMaze only; no real robot.

## Related

- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — the concept.
- [LeWorldModel](leworldmodel.md) / [DINO-WM](dino-wm.md) — the frozen tradition it departs from.
- [Identifiability](../concepts/world-models/identifiability.md) — the robustness gap.
- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — same signal, opposite use.
- [Temporal Straightening](../sources/temporal-straightening-paper.md) — sibling from the same NYU group (Wang, Bounou, LeCun, Ren); fixes the latent *geometry* where AdaJEPA fixes the model *online*.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — AdaJEPA tests both GD and CEM planners.

## Mentioned in

- [AdaJEPA paper](../sources/adajepa-paper.md)

---
title: Decision Transformer
type: entity
subtype: architecture
created: 2026-08-30
updated: 2026-08-30
sources: 0
tags: [decision-transformer, offline-rl, sequence-modeling, returns-to-go, conditional-imitation, credit-assignment, berkeley]
---

**Decision Transformer (DT)** — Chen, Lu et al. (Berkeley / FAIR / Google Brain, NeurIPS 2021; [paper](../sources/decision-transformer-paper.md)). Recasts reinforcement learning as **next-token prediction**: condition on the return you want, and let a causally-masked GPT emit the actions that achieve it. No value function, no policy gradient, no bootstrapping.

```
τ = ( R̂₁, s₁, a₁,  R̂₂, s₂, a₂,  … )        R̂_t = Σ_{t'≥t} r_{t'}   (return-to-go)
```

`K` timesteps → **`3K` tokens**, one learned linear embedding per modality, plus a **per-timestep** embedding distinct from the standard positional embedding (one timestep is three tokens). At rollout: pick a target return, act, **decrement the target by the reward received**, repeat.

**The source of the interleaved observation-action token format** that most robot policies in this wiki inherit.

## The two findings worth carrying

**It is largely conditional imitation, and the authors show it.** Their own §5.1 invents **Percentile Behaviour Cloning** (%BC — plain BC on the top `X%` of timesteps by return) and finds DT "competitive with the performance of the best %BC." DT's real advantage is that it *finds* the right percentile automatically from the return conditioning, where choosing it manually would require evaluating rollouts. But **DT does not learn a policy better than its data** — it imitates the good parts on request. Publishing that ablation is to their credit and it is routinely dropped downstream.

**Where it genuinely beats TD learning: long-horizon credit assignment.** On **Key-to-Door**, trained only on *random walks* with the whole episode as context, DT produces near-optimal paths while CQL "cannot effectively propagate Q-values over the long horizons involved." Self-attention assigns credit in one hop where TD must chain estimates through every intervening step — the same `O(1)` path-length argument [Attention Is All You Need](../sources/attention-is-all-you-need.md) makes for language, applied to reward.

## Mentioned in

- [Decision Transformer paper](../sources/decision-transformer-paper.md)
- [EchoWorld paper](../sources/echoworld-paper.md) — beats DT 7.44 → 7.05 by replacing the interleaving with **pairwise 6-DOF pose differences in the attention keys and values** rather than an index added to tokens.

## Open questions / TBD

- **Does return conditioning survive real robots?** Every result is simulated, and a return-to-go target needs a scalar reward specifiable in advance, which most manipulation tasks lack.
- **Stitching** — the known weakness of return-conditioned BC — is untested here.
- **[EchoWorld](echoworld.md)'s pose-conditioned attention vs DT interleaving on a standard robot benchmark.** Both codebases are open; nobody has run it.

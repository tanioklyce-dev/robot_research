---
title: "Decision Transformer: Reinforcement Learning via Sequence Modeling (Chen, Lu, Rajeswaran et al., NeurIPS 2021)"
type: source
url: https://arxiv.org/abs/2106.01345
local_path: raw/2106.01345v2.pdf
sha256: 6ff675a7b8286ca7bf8e01e4b90a41bf5c90f4c3c007e17fdb4d24e26fd05e28
author: "Lili Chen*, Kevin Lu*, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas†, Igor Mordatch†"
affiliation: UC Berkeley; Facebook AI Research; Google Brain
venue: "NeurIPS 2021; arXiv 2106.01345"
published: 2021-06-02
ingested: 2026-08-30
tags: [decision-transformer, offline-rl, sequence-modeling, returns-to-go, credit-assignment, conditional-imitation, berkeley, abbeel, neurips-2021, foundational]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2106.01345v2.pdf`, 21 pages). §1–6 read in full including the ablations, which are the most interesting part; per-environment hyperparameter appendices skimmed. Ingested because [EchoWorld](echoworld-paper.md) beats it as a baseline and the wiki knew it only as the thing being beaten.

## Summary

**Decision Transformer** — Chen, Lu, Rajeswaran, Lee, Grover, Laskin, Abbeel, Srinivas & Mordatch (Berkeley / FAIR / Google Brain; NeurIPS 2021). **The paper that recast reinforcement learning as next-token prediction**, and thereby supplied the sequence format most robot policies in this wiki still use.

The idea in one line: **condition on the return you want, and let an autoregressive model produce the actions that achieve it.** No value function, no policy gradient, no bootstrapping.

The trajectory representation is the whole contribution:

```
τ = ( R̂₁, s₁, a₁,  R̂₂, s₂, a₂,  …,  R̂_T, s_T, a_T )
```

where `R̂_t = Σ_{t'≥t} r_{t'}` is the **return-to-go** — the sum of *future* rewards, not the reward received. The paper is explicit about why: "we would like the model to generate actions based on future desired returns, rather than past rewards."

At test time you specify a target return and the start state, generate an action, execute it, **decrement the target return by the reward actually received**, and repeat.

## Architecture

Feed the last `K` timesteps — **`3K` tokens**, one per modality per step. A **learned linear layer per modality** projects raw inputs to the embedding dimension, followed by layer norm; visual states go through a convolutional encoder instead. Then a GPT with a causal self-attention mask predicts actions autoregressively.

> [!note] One detail everyone reimplements and half get wrong
> "An embedding for each **timestep** is learned and added to each token — note this is different than the standard positional embedding used by transformers, as **one timestep corresponds to three tokens**."
>
> The positional signal has to be *per timestep*, not per token position, or the model cannot tell a return from a state from an action at the same instant. This is the small structural fact that makes the interleaved format work, and it is the piece [EchoWorld](echoworld-paper.md) replaces with something richer — pairwise 6-DOF pose differences injected into the attention keys and values rather than an index added to the tokens.

## Results

Competitive with or better than **CQL** (the model-free offline-RL state of the art at the time), REM, and QR-DQN on Atari, OpenAI Gym / D4RL, and Key-to-Door — without any of the machinery those methods depend on.

## The ablation that deflates the framing — and the authors run it themselves

§5.1 asks: *"Does Decision Transformer perform behavior cloning on a subset of the data?"*

They invent **Percentile Behavior Cloning (%BC)** — run plain behaviour cloning on only the top `X%` of timesteps by episode return, sweeping `X ∈ {10, 25, 40, 100}%`. Result, on D4RL:

| Dataset | Env | **DT** | 10%BC | 25%BC | 40%BC | 100%BC | CQL |
|---|---|---|---|---|---|---|---|
| Medium | HalfCheetah | 42.6 | 42.9 | 43.0 | 43.1 | 43.1 | 44.4 |
| Medium | Hopper | **67.6** | 65.9 | 65.2 | 65.3 | 63.9 | 58.0 |
| Medium | Walker | 74.0 | 78.8 | **80.9** | 78.8 | 77.3 | 79.2 |
| Medium | Reacher | 51.2 | 51.0 | 48.9 | 58.2 | **58.4** | 26.0 |
| Medium-Replay | HalfCheetah | 36.6 | 40.8 | 40.9 | 41.1 | 4.3 | **46.2** |

Their own reading: *"On most environments, Decision Transformer is competitive with the performance of the best %BC, indicating it can hone in on a particular subset after training on the entire data distribution."*

> [!warning] "RL via sequence modeling" is largely return-conditioned imitation, and the paper says so
> In the data-rich D4RL regime, **DT is roughly as good as behaviour cloning on the right subset of the data** — and the only way to *find* the right subset is to evaluate rollouts, so %BC "is not a realistic approach." That is DT's genuine advantage: it selects the subset automatically, from the return conditioning, without needing to know which percentile is best.
>
> But it is a weaker claim than the title implies. **DT does not learn a policy better than its data; it learns to imitate the good parts of its data on request.** Anything requiring genuine improvement over the behaviour distribution — trajectory stitching, extrapolating beyond the best observed return — is outside what these results demonstrate.
>
> Worth carrying into every [VLA](../concepts/learning/vla-models.md) claim in this wiki: the architecture is inherited from DT, the training is behaviour cloning, and the honest description of what such a model does is *conditional imitation*. Publishing the ablation that shows this is to the authors' credit, and it is routinely dropped downstream.

### Where it genuinely beats TD learning: Key-to-Door

Pick up a key in phase one, open a door in phase three, with irrelevant actions in between. Credit must propagate across the whole episode, skipping the middle. Trained **only on random-walk trajectories**, with the **entire episode as context** rather than a fixed window:

- DT and %BC (trained only on successful episodes) produce **near-optimal paths despite training on random walks**.
- **CQL "cannot effectively propagate Q-values over the long horizons involved and gets poor performance."**

This is the real argument for the reframing: **self-attention does credit assignment directly**, in one hop, where TD bootstrapping has to chain value estimates through every intervening step. It is the same `O(1)` path-length argument [Attention Is All You Need](attention-is-all-you-need.md) makes for language, applied to reward.

They also show that when DT is made to predict return tokens too, it "continuously updates reward probability based on events during the episode" and **attends to the critical events** — picking up the key, reaching the door.

## Entities mentioned

- **Pieter Abbeel** (Berkeley), Igor Mordatch (Google Brain), Aravind Srinivas, Aravind Rajeswaran (FAIR). No wiki pages.
- **GPT** — the architecture used directly.
- **CQL**, REM, QR-DQN — the offline-RL baselines. D4RL, Atari.

## Concepts touched

- **[Imitation learning](../concepts/learning/imitation-learning.md)** — what §5.1 shows this largely is.
- **[VLA models](../concepts/learning/vla-models.md)** — the interleaved `(observation, action)` token format descends from here.
- **[Real-world robot RL](../concepts/learning/real-world-robot-rl.md)** — the offline-RL alternative this sidesteps.
- **[Attention](../glossary.md#attention)** — credit assignment as a path-length argument.

## Open questions / TBD

- **Does return conditioning survive contact with real robots?** Every result here is simulated. A return-to-go target requires a scalar reward the operator can specify in advance, which most manipulation tasks do not have.
- **Stitching.** The known theoretical weakness of return-conditioned BC — it cannot compose sub-trajectories from different episodes into a better one — is not tested here, and later work (e.g. Q-learning-augmented variants) exists and is un-ingested.
- **[EchoWorld](echoworld-paper.md) beats DT by replacing the interleaving with pose-conditioned attention** (7.44 → 7.05) on probe guidance. Nobody has run that comparison on a standard robot benchmark, and both codebases are open.

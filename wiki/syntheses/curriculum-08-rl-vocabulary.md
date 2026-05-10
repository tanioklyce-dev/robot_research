---
title: Curriculum Module 8 — Reinforcement learning vocabulary
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-8, reinforcement-learning, mdp, policy-gradient, ppo, dqn, mbrl, mfrl, dreamer, td-mpc]
prereqs: [curriculum-01]
status: draft
---

> [!note] Curriculum context
> This is **Module 8** of the [Robot-learning curriculum](robot-learning-curriculum.md). It only requires [Module 1](robot-learning-curriculum.md) (NN basics) and is otherwise self-contained — RL is *not* the focus of this curriculum, so this module is deliberately **light**: read for vocabulary, not implementation.
>
> The downstream modules that need this vocabulary are [Module 10](curriculum-10-world-models.md) (the Dreamer-line and TD-MPC-line of WMs), [Module 11](curriculum-11-jepa-deep.md) (referenced as alternatives), and [Module 12](curriculum-12-lewm-deep-dive.md) (the LeWM paper compares against Dreamer and TD-MPC as baselines, which would be illegible without RL terminology).
>
> If you already know RL, **skim this module in 10 minutes** to make sure your vocabulary matches the curriculum's. If you don't, **spend 1–2 hours** internalizing the definitions below — that's enough to read the rest of the curriculum.
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there.

## What this module is

Just enough RL to read the LeWM-baseline column headers and the Dreamer / TD-MPC paragraphs in [Module 10](curriculum-10-world-models.md). Specifically:

- **Markov Decision Process ([MDP](../glossary.md#mdp))** — the formalism.
- **Return, value, policy** — the three core objects.
- **On-policy vs off-policy** — what training data the algorithm needs.
- **Policy gradient (REINFORCE → [PPO](../glossary.md#ppo))** — the canonical "directly improve the policy" lineage.
- **Q-learning ([DQN](../glossary.md#dqn))** — the canonical "learn the value, derive the policy" lineage.
- **Model-free vs model-based ([MFRL](../glossary.md#mfrl) vs [MBRL](../glossary.md#mbrl))** — the question of whether you learn dynamics.
- **[Dreamer](../entities/dreamer.md)-class "latent imagination"** — the specific MBRL technique that's a baseline in [LeWM](../entities/leworldmodel.md).

By the end you should be able to:

1. Read "DreamerV3 trains an actor-critic in imagination on top of a recurrent latent dynamics model" without confusion.
2. Read "TD-MPC2 uses local trajectory optimization in the latent space of a learned implicit world model with TD-bootstrapped value" and parse each phrase.
3. Distinguish a *policy gradient* update from a *value-function bootstrap* update without re-reading.
4. Tell whether a paper is on-policy or off-policy and reason about what that constrains.

## The MDP — the formalism

A **Markov Decision Process** is a tuple `(S, A, P, R, γ)`:

- `S` — set of states (or observations, for partially-observable variants).
- `A` — set of actions.
- `P(s' | s, a)` — transition probability.
- `R(s, a)` — reward function.
- `γ ∈ [0, 1]` — discount factor.

The **agent** observes `s_t`, picks action `a_t`, receives reward `r_t = R(s_t, a_t)`, and the world transitions to `s_{t+1} ~ P(· | s_t, a_t)`. Repeat.

**Markov property.** `P(s_{t+1} | s_t, a_t)` depends *only* on the current state and action, not on the history. This is a modeling assumption — most real environments aren't strictly Markov, but you can usually engineer state representations that approximately satisfy it.

## Three core objects: return, value, policy

### Return

The discounted sum of rewards from time `t` onward:

```
G_t = r_t + γ · r_{t+1} + γ² · r_{t+2} + ⋯ = Σ_{k=0}^∞ γ^k · r_{t+k}
```

The discount factor `γ < 1` ensures convergence and prioritizes near-term reward. Typical values: `γ = 0.99` for long-horizon control; `γ = 0.95` for shorter-horizon.

### Value function

The expected return from state `s` under policy `π`:

```
V^π(s)  =  𝔼_π [ G_t | s_t = s ]
Q^π(s, a) = 𝔼_π [ G_t | s_t = s, a_t = a ]      // state-action value
```

`V` is "how good is this state, assuming we follow `π`?" `Q` is "how good is taking action `a` in state `s`, then following `π`?"

The relationship: `V^π(s) = 𝔼_{a ~ π(·|s)}[Q^π(s, a)]`.

### Policy

A function `π(a | s)` that maps states to a probability distribution over actions. Can be deterministic (`a = π(s)`) or stochastic. Modern deep-RL policies are typically Gaussian (continuous) or categorical (discrete).

The goal of RL: **find a policy that maximizes expected return**.

## On-policy vs off-policy

A central distinction that determines which algorithm you can use.

- **On-policy.** The policy being trained is the same policy being used to collect data. Each round of training requires fresh rollouts from the current policy. Typically more stable to train but sample-inefficient.
- **Off-policy.** Training reuses data collected by other policies (older versions of itself, a behavior policy, demonstrations). Sample-efficient but trickier to train (importance weighting, distribution-shift effects).

Examples:
- **[PPO](../glossary.md#ppo)** — on-policy.
- **[DQN](../glossary.md#dqn)** — off-policy (it has a replay buffer).
- **[SAC](../glossary.md#sac)** — off-policy.
- **Behavior cloning** ([Module 6](curriculum-06-imitation-learning.md)) — off-policy, sort of: the "policy that collected the data" is the human expert, not the agent.

Most modern robotics RL is **off-policy** (you can't afford fresh rollouts from each new policy on real hardware) or **offline** (no environment interaction at all during training; learn from a fixed dataset of past interactions).

## Policy gradient — direct policy improvement

The "REINFORCE → PPO" lineage. You parameterize the policy `π_θ`, and you optimize `θ` directly to maximize expected return. The gradient is:

```
∇_θ J(θ)  =  𝔼_τ ~ π_θ [ Σ_t  ∇_θ log π_θ(a_t | s_t) · G_t ]      // REINFORCE
```

Three observations:

1. The gradient updates each action's log-probability *proportional to its observed return*. Actions that led to higher returns get their probabilities pushed up.
2. The expectation is taken over trajectories sampled from the *current* policy. That makes this on-policy.
3. The gradient is high-variance — the return `G_t` averages over the long stochastic future. Variance reduction (baselines, advantage functions, GAE) is most of what real implementations do.

### REINFORCE → A2C → PPO sketch

- **REINFORCE** (Williams 1992): the basic policy gradient above.
- **Advantage Actor-Critic (A2C)**: subtract a learned value baseline `V(s_t)` to reduce variance. The "advantage" `A(s_t, a_t) = G_t − V(s_t)` is what's now multiplied with the log-prob.
- **[PPO](../glossary.md#ppo)** (Schulman et al. 2017): clip the policy update so it doesn't move too far from the previous policy in any one step. The dominant on-policy actor-critic algorithm in 2025–2026.

You don't need to know PPO in detail for this curriculum; you need to recognize the name and know it's "actor-critic, on-policy, clipped, the modern default."

## Q-learning — value-based

The DQN lineage. You learn `Q(s, a)` and derive the policy as `π(s) = argmax_a Q(s, a)`. The Bellman recursion gives the training target:

```
Q*(s, a)  ←  r(s, a) + γ · 𝔼_{s'} [ max_{a'} Q*(s', a') ]
```

At training time, you sample `(s, a, r, s')` transitions and minimize:

```
L  =  ( Q_θ(s, a)  −  [r + γ · max_{a'} Q_target(s', a')] )²
```

Two notes:
- This is **off-policy** — you can use any `(s, a, r, s')` transitions, regardless of whose policy collected them.
- The `Q_target` (a target network) is a slowly-updated copy of `Q_θ`. Stabilizes training.

**[DQN](../glossary.md#dqn)** (Mnih et al. 2015, the original Atari result) is the canonical instance for discrete actions. **DDPG / TD3 / [SAC](../glossary.md#sac)** extend this to continuous actions by replacing the `max_{a'}` with a learned actor network.

You'll see "DQN" in the curriculum as a vocabulary reference, not a paper anyone here implements.

## MFRL vs MBRL — the model question

The axis that maps directly onto [Module 10](curriculum-10-world-models.md)'s world-model taxonomy.

- **Model-Free RL ([MFRL](../glossary.md#mfrl)).** Learn the policy and/or value function directly from interaction. No explicit model of the environment dynamics.
  - Examples: [PPO](../glossary.md#ppo), [SAC](../glossary.md#sac), [DQN](../glossary.md#dqn).
  - Pros: simple; the dominant industrial choice for large-scale RL.
  - Cons: sample-inefficient — needs many environment interactions.

- **Model-Based RL ([MBRL](../glossary.md#mbrl)).** Learn an explicit dynamics model `f(s, a) → s'` (a [world model](../concepts/world-model.md)). Use the model to either *plan* (MPC, [Module 10](curriculum-10-world-models.md)) or *generate synthetic interactions for policy training* (the Dreamer recipe).
  - Examples: [Dreamer / DreamerV3](../entities/dreamer.md), [TD-MPC / TD-MPC2](../entities/td-mpc.md).
  - Pros: sample-efficient — once you have a model, "imagined" rollouts are free.
  - Cons: dynamics models accumulate error; the MBRL agent's policy is only as good as the model.

[Module 10](curriculum-10-world-models.md) decomposes MBRL further into the four-family taxonomy. Module 8's job is just to make "MBRL" a parseable phrase.

## Dreamer-class latent imagination

The specific MBRL technique that's the [LeWM](../entities/leworldmodel.md) baseline you'll see in [Module 12](curriculum-12-lewm-deep-dive.md). Roughly:

```
1. Train a world model from interaction data:
     z_t = encoder(o_t)
     z_{t+1} = transition(z_t, a_t)
     ô_t = decoder(z_t)            // for Dreamer; TD-MPC skips this
     r_t = reward_head(z_t)         // critical for MBRL — must predict reward

2. Train an actor-critic policy IN THE WORLD MODEL:
     - Sample a starting state z_0 from the data.
     - Roll out (z_t, a_t, r_t, z_{t+1}) using the world model + the current actor.
     - Compute returns; update the actor and critic.
     - The world model is the environment.

3. Use the actor on the real environment to collect more data; loop.
```

This is **"latent imagination"** — the policy is trained on synthetic rollouts produced by the world model. The wins:

- Sample-efficient: imagined rollouts are free.
- The world model's reward head provides *learned* return signals, extending effective horizons (the "value bootstrap" trick from [Module 10](curriculum-10-world-models.md)).

The losses:

- The world model has to be good enough that imagined rollouts approximate reality.
- The reward head has to predict reward well — which requires reward labels at training time.

[Dreamer / DreamerV3](../entities/dreamer.md) decodes to pixels (and reward); [TD-MPC2](../entities/td-mpc.md) skips the pixel decoder but keeps the value bootstrap. Both are MBRL. Both are LeWM baseline columns. Knowing this is enough to read [Module 10](curriculum-10-world-models.md)'s "where LeWM lives" section and Module 12's results table.

## What this curriculum is *not* doing

Things this module deliberately doesn't cover:

- **Mathematical RL theory** (Bellman optimality proofs, contraction mappings, regret bounds).
- **Implementation details** (reward normalization, entropy bonuses, KL divergences in PPO, target-network update rates in DQN).
- **Modern MFRL deep-dive** (PPO/SAC variants, distributional RL, soft Q-learning, …).
- **Offline RL** as a paradigm (CQL, IQL, RvS, …) — though [Module 10](curriculum-10-world-models.md)'s reference to GCIQL / GCIVL as LeWM baselines is implicitly here.

If you want depth on any of these, the standard reference is **Sutton & Barto's *Reinforcement Learning: An Introduction*** (the textbook). For deep RL specifically, the **OpenAI Spinning Up** lecture series is the canonical free entry point.

## Anchor exercise

> **Read a DreamerV3 figure caption out loud, and have it parse.**

The deliberate "you can read it now" exercise. The [DreamerV3 paper](../sources/dreamer-v3-paper.md) figure captions reference: "actor-critic", "imagined rollouts", "RSSM" (Recurrent State Space Model), "two-hot reward representation", "symlog squashing", "world model latent". After this module:

- Actor-critic — yes, Module 8 §5 and §6.
- Imagined rollouts — yes, §6.
- RSSM — recurrent latent dynamics; you can read this as "Dreamer's specific transition architecture" without re-deriving.
- Two-hot reward / symlog squashing — these are stability tricks from the paper; you can skim past them on first read.
- World model latent — the `z_t` in §6's pseudocode.

Pick any DreamerV3 paper figure, read the caption, and check whether each phrase makes sense. If yes, you're ready for [Modules 10–12](curriculum-10-world-models.md).

## Recommended reading

In order of effort:

1. **Wikipedia entries on MDP, value function, policy gradient.** Your first stop if anything in §1–4 above is unfamiliar.
2. **OpenAI Spinning Up** (free, online) — for "I understand it from words; I'd like to see code."
3. **[DreamerV3 paper](../sources/dreamer-v3-paper.md)** — read the abstract + intro. Pick out the RL terms and check yourself against this module.
4. **[TD-MPC2 paper](../sources/td-mpc2-paper.md)** — read the abstract. Same drill.
5. **Sutton & Barto** — only if you want depth and have a few weekends.

## What you should now be able to do

- Read a sentence like "Dreamer trains an actor-critic in imagination on top of a recurrent latent dynamics model with two-hot reward prediction" and parse each phrase.
- Identify whether an arbitrary RL paper is on-policy / off-policy / offline, MFRL / MBRL, value-based / policy-gradient.
- Skip RL implementation details when reading a robotics paper without losing the methodological takeaway.
- Tell when an RL paper's contribution is at the *RL algorithm* level (PPO variant, new exploration scheme) vs the *world-model* level (Dreamer is mostly the latter despite being filed in the RL literature).

## Hand-off

Module 8 is the supporting vocabulary, not part of the main reading chain. Use it as needed when:

- Reading [Module 10](curriculum-10-world-models.md)'s Dreamer / TD-MPC family description.
- Reading [Module 11](curriculum-11-jepa-deep.md)'s comparison of frozen-feature vs end-to-end JEPAs to MBRL alternatives.
- Reading [Module 12](curriculum-12-lewm-deep-dive.md)'s LeWM results table where Dreamer and TD-MPC are baseline columns.

## Related curriculum modules

- **[Module 1 — NN basics](robot-learning-curriculum.md)** — sole prerequisite.
- **[Module 6 — Imitation learning](curriculum-06-imitation-learning.md)** — the IL/RL/WM trichotomy.
- **[Module 10 — World models, broad](curriculum-10-world-models.md)** — where MBRL fits as Family 4 (reward-conditioned MBRL).
- **[Module 12 — LeWM deep-dive](curriculum-12-lewm-deep-dive.md)** — the LeWM baseline columns (Dreamer, TD-MPC) need this vocabulary.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- **Sutton & Barto reference** — could be linked from a "deep on RL" pointer page if the curriculum picks up readers who want to go further than vocabulary.
- **OpenAI Spinning Up entity page** — worth filing if more curriculum modules end up linking to it.
- **A worked PPO + Dreamer notebook** — would make the abstract math concrete; not in scope for "vocabulary only" but a good extension if a reader wants depth.

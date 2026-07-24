---
title: π*0.6 + RECAP
type: entity
subtype: model
created: 2026-05-25
updated: 2026-05-25
sources: 4
tags: [pi-star-zero-6, pistar06, recap, pi-zero-6, pi-zero, vla, flow-matching, advantage-conditioning, offline-rl, distributional-value-function, classifier-free-guidance, dagger, real-world-rl, physical-intelligence]
---

**π*0.6** — [Physical Intelligence](physical-intelligence.md)'s **RL-adapted variant of π0.6**, paired with **RECAP** ("RL with Experience and Corrections via Advantage-conditioned Policies") — a recipe for VLAs to **improve through real-world deployment** ([paper](../sources/pistar06-paper.md)). Sibling to [π0.7](pi07.md). The wiki's first ingest of an RL-from-deployment recipe for an expressive flow-matching VLA.

## Headline result

On the hardest tasks, RECAP **more than doubles task throughput** and **roughly halves failure rate** vs the IL-only baseline. Enough to run π*0.6 **continuously for 13 hours making espresso drinks**, **2+ hours folding novel laundry in a new home uninterrupted**, and **box assembly at factory packaging reliability**. The wiki's first published evidence of **multi-hour autonomous VLA deployment** with RL-in-the-loop self-improvement.

## The RECAP recipe

Three iterated steps:

1. **Data collection** — deploy current VLA on task; label each episode with sparse task-outcome reward; optionally collect human interventions (human-gated DAgger).
2. **Value function training** — train a **multi-task distributional value function** `V^πref` on all data so far. **201 discrete value bins**, cross-entropy on Monte Carlo returns. Same architecture as the VLA policy but with a smaller VLM backbone.
3. **Advantage-conditioned policy training** — train a new VLA conditioned on a **binarized advantage indicator** `I = δ(A^πref(o,a,ℓ) > ε_ℓ)` from the value function. Train both with and without the indicator (classifier-free-guidance style); at inference, condition on "improved" to extract the better policy.

Iterate as many times as needed.

## Why advantage conditioning (not PPO or AWR)

- **PPO / REINFORCE** are hard to apply to flow-matching VLAs — flow models don't readily provide tractable log-likelihoods, blocking the standard policy-gradient recipe.
- **AWR** (advantage-weighted regression) discards or down-weights significant portions of data — wasteful.
- **Advantage conditioning** trains on ALL data with supervised learning, plus an extra "is this action good?" conditioning input. Direct lineage: **[CFGRL](https://arxiv.org/abs/2502.02484)** (classifier-free guidance RL) + "condition the policy on a function of trajectory."

Bayes-rule derivation (paper §IV-B): `π̂(a|o,ℓ) ∝ π^ref(a|o,ℓ) · (π^ref(a|I,o,ℓ) / π^ref(a|o,ℓ))^β`. For β=1, `π̂ = π^ref(a|I,o,ℓ)` — i.e., **just train the policy to model both with and without the improvement indicator, then condition on "improved" at inference**.

## Architecture

- **Built on π0.6** ("improvement on π0.5 with larger backbone + diverse conditioning").
- Adds **advantage-indicator conditioning** to the VLA prefix.
- Same **[Knowledge Insulation (KI)](../concepts/learning/knowledge-insulation.md)** training recipe as [π0.7](pi07.md) — VLM trained via next-token prediction with [FAST](fast-action-tokenization.md) tokens; flow-matching action expert with **stop-gradient** (no gradient flow back to VLM).
- Value function: same architecture as policy, smaller VLM backbone.

## Data composition

Iterated mixture across pre-training and post-training phases:
- **Tens of thousands of hours of demonstrations** (pre-training).
- **Autonomous rollouts** from prior model deployments (post-training).
- **Expert teleoperated interventions** (human-gated DAgger).
- **Sparse outcome rewards** (succeeded / failed) — robust to ambiguous and stochastic real-world reward signals.

## Demonstrated tasks

- **Espresso drinks** with a professional espresso machine — **13-hour continuous operation**.
- **Box assembly** for real factory packaging.
- **Folding diverse laundry** — novel items in a new home; **2+ hours uninterrupted**.

## Why it matters in this wiki

1. **First VLA-scale real-world RL recipe that works on flow-matching action heads.** RECAP sidesteps the policy-gradient problem on flow models via advantage conditioning. This is the technical unlock for VLA self-improvement.
2. **Quantifies the IL → RL-from-deployment gain**: **2× throughput, ½ failure rate** on the hardest tasks. The strongest case yet for **integrating RL into VLA training pipelines** rather than treating IL as the end state.
3. **Multi-hour autonomous deployment numbers are rare** in the published literature. 13 hours of espresso-making is one of the strongest data points to date.
4. **Sibling to [π0.7](pi07.md) in PI's late-2025 push**: π0.7 = "more diverse data + diversified prompts," π*0.6 = "iterate on deployment experience." Two papers, same lab, complementary directions.

## Related

- [π0](pi-zero.md) — grandfather.
- [π0.7](pi07.md) — sibling release.
- [Physical Intelligence](physical-intelligence.md) — lab.
- [VLA models](../concepts/learning/vla-models.md) — broader concept.
- [Imitation learning](../concepts/learning/imitation-learning.md) — pre-training is offline-RL-flavored IL.
- [Diffusion Policy](diffusion-policy.md) — sibling continuous-action approach; lacks RECAP-style RL fine-tuning.

## Code & blog

- Project page: https://pi.website/blog/pistar06
- Paper: [π*0.6 source page](../sources/pistar06-paper.md) (local PDF at `raw/pistar06.pdf`).

## Mentioned in

- [π*0.6 paper](../sources/pistar06-paper.md) — primary source.
- [π0.7 paper](../sources/pi07-paper.md) — sibling release.
- [π0 entity](pi-zero.md) — listed as successor.
- [Physical Intelligence entity](physical-intelligence.md) — entry in the model line.

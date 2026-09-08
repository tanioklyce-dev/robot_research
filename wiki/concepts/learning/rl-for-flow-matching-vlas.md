---
title: RL for flow-matching VLAs — reweight the sampler, not the gradient
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [rl, vla, flow-matching, awr, recap, advantage-conditioning, cfg, policy-extraction, offline-rl, off-policy, exploration]
---

**How do you improve a policy whose action head is a flow-matching sampler?** Policy-gradient RL needs the probability of the action taken — REINFORCE and TRPO need `log π(a|s)`, PPO needs the ratio `π_new/π_old`. A [flow-matching](flow-matching.md) head learns a velocity field that transports Gaussian noise to an action chunk; it can *sample* from its distribution but cannot *evaluate* it. So the estimators that dominate LLM post-training do not apply directly, and the workarounds (PPO on an approximated problem, per-denoising-step MDPs) change the problem being solved ([Larchenko](../../sources/larchenko-lehome-part1-rl-for-vlas.md) [28:02–31:07]; [π*0.6](../../sources/pistar06-paper.md) §IV-B).

## The move: change the target distribution, keep the sampler

Both working recipes in the wiki avoid likelihoods entirely. They **define a better distribution in terms of the data's implied policy μ and the advantage**, then train the flow head to sample from it exactly as behaviour cloning would.

| Method | Target distribution | How the flow head learns it | Extra machinery |
|---|---|---|---|
| **AWR** (Peng et al. 2019; closed form of max E[A] s.t. KL(π‖μ) ≤ ε) | `π ∝ μ · exp(A/β)` | weight each sample's BC loss — or, Larchenko's variant, **sample it** — by `exp(clip(A)/β)` | none; one weight in the BC pipeline |
| **RECAP** advantage conditioning (Physical Intelligence, [π*0.6](../../entities/pistar06.md); lineage CFGRL) | `π ∝ μ · P(A > ε)^β`; for β = 1, the conditional `μ(a \| A > ε, s)` | train one network **with and without** an advantage-indicator token; roll out with it on | an advantage estimate per sample; unlocks **classifier-free guidance** at inference |
| **Both together** (Larchenko) | AWR lifts the unconditional base; RECAP's conditional pass lifts further | as above, simultaneously | CFG scale 7–9 in practice, plus best-of-N |

Two properties follow. (1) **Off-policy by construction**: data from old checkpoints, humans, and DAgger corrections all count as samples of μ, so nothing is discarded on a schedule — the opposite of PPO's collect-update-discard cycle. (2) **On-manifold**: neither method pushes probability *away* from bad actions; both move it *toward* good ones while still training on the bad ones at lower weight. In a 360-dimensional action chunk whose valid set is a thin manifold, "push down" can send mass anywhere; "pull toward" cannot leave the data ([Larchenko](../../sources/larchenko-lehome-part1-rl-for-vlas.md) [44:36–46:47]).

## Where the advantage comes from

- **π*0.6**: a separate **distributional value model** (201 bins, Monte-Carlo returns, smaller VLM backbone), advantage binarised against a per-task threshold.
- **Larchenko**: **the policy is its own value function** — auxiliary heads on the VLA predict success probability and completion from images, and a *success delta* after the action chunk that is *"something between a Q and an advantage."* Advantages for training are computed from returns in the stored rollouts, not from model predictions; old rollouts are down-weighted because their stored value predictions go stale.

Which is better is unmeasured. The combined design sees exactly what the policy sees and saves a network; the separate design can be retrained without touching the policy.

## The ceiling

**Neither method explores.** Reweighting a distribution cannot put mass where μ has none. Larchenko reports *"literally zero exploration … the model never learned new behavior"* on LeHome; π*0.6 gets its new behaviour from **human corrections** during deployment, which is the same admission in a different form. Improvement is a sharpening of what the demonstrations already contained. For a home robot that means the demonstration set, not the RL, decides what the policy can ever do.

## Practical recipe, as run on one H200 + one workstation GPU

1. BC on organiser demonstrations (π0.5, PaliGemma + flow expert + FAST branch).
2. Asynchronous loop through the Hugging Face Hub: trainer pulls rollouts, computes advantages from returns, trains AWR + RECAP, pushes a checkpoint every 30–60 min; rollout workers pull the latest checkpoint, roll out under domain randomisation, tag hard states, push datasets.
3. Curriculum on success rate (target 40–50 %), success replay under heavy visual randomisation, semi-success replay from near-misses.
4. Inference: advantage token on, CFG 7–9, best-of-N 2–3, replan every ~5 of 30 steps.

## Related concepts

- [Flow matching](flow-matching.md) — the head, and the page that previously said no wiki source had done this.
- [Real-world robot RL](real-world-robot-rl.md) — the HIL-SERL lineage; this is its low-budget, sim-first, human-optional cousin.
- [Reward post-training of diffusion models](reward-post-training-diffusion.md) — the image-generation analogue of the same problem.
- [Imitation learning](imitation-learning.md) — μ; DAgger as one more sample source.
- [VLA models](vla-models.md).

## Key references

- [π*0.6: a VLA that learns from experience](../../sources/pistar06-paper.md) — RECAP, the derivation, the separate value model, real-world deployment results.
- [Larchenko, LeHome Part 1](../../sources/larchenko-lehome-part1-rl-for-vlas.md) — AWR + RECAP combined on a flow-matching VLA; the manifold argument; the zero-exploration report.
- Un-ingested: AWR (Peng, Kumar, Zhang, Levine 2019, arXiv 1910.00177); AWAC (Nair et al. 2020); CFGRL; Larchenko's tech report (arXiv 2606.27163).

## Current state

Two instances, one at company scale with human corrections and one at single-GPU scale in simulation, agreeing on the method and on its limit. No head-to-head against a PPO-on-flow variant, no ablation of combined-vs-separate value estimation, and no measurement of how much of the gain is RL over BC. The exploration ceiling is the open problem.

## Mentioned in

- [π*0.6 paper](../../sources/pistar06-paper.md)
- [Larchenko — LeHome deep dive, Part 1](../../sources/larchenko-lehome-part1-rl-for-vlas.md)

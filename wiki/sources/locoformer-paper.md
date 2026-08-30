---
title: "LocoFormer: Generalist Locomotion via Long-context Adaptation"
type: source
url: https://arxiv.org/abs/2509.23745
local_path: raw/2509.23745v1.pdf
sha256: 248ba53b1feb2ede28fa1b50deee0c75d4e8e76e548097a2d37e042f418b07ca
author: Min Liu, Deepak Pathak, Ananye Agarwal (Skild AI)
published: 2025-09-28
ingested: 2026-08-29
venue: CoRL 2025 (9th Conference on Robot Learning, Seoul)
format: PDF (15 pp., arXiv:2509.23745v1)
project_page: https://generalist-locomotion.github.io
tags: [locoformer, skild-ai, locomotion, cross-embodiment, in-context-learning, transformer-xl, rl, domain-randomization, sim-to-real, procedural-generation, corl-2025]
---

# LocoFormer: Generalist Locomotion via Long-context Adaptation

## Summary

**A single locomotion policy that controls robots it has never seen — including robots that do not exist.** LocoFormer is trained purely with RL on **procedurally generated** bipeds, quadrupeds and their wheeled variants, using *no parameters from any real robot*, and transfers zero-shot to ten commercial platforms including [Unitree G1](../entities/unitree-g1.md)/H1/A1/Go2-W, Fourier GR1, LimX TRON1, [Boston Dynamics Spot](../entities/spot.md) and ETH ANYmal C.

The paper's thesis is that cross-embodiment generality comes from **two choices acting together**: massive-scale RL over an aggressively randomized procedural robot distribution, and a **context window extended by orders of magnitude — far enough to span trial boundaries.** Prior locomotion controllers adapt over "a few hundred milliseconds" and are, in the authors' word, *myopic*; LocoFormer carries up to ~18 seconds and, crucially, **remembers across falls**.

The consequence is the paper's most striking result: **the robot learns from failure within a deployment, not within training.** Given a body so unstable it fails on the first attempt, LocoFormer retains the failed trajectory in its cache and **walks stably by the third trial** — with frozen weights.

This is the source that **substantiates [Skild AI](../entities/skild-ai.md)'s "omni-bodied" claim**, which its manipulation model [S1](skild-s1-blog.md) notably does not. Unlike S1 this is a peer-reviewed CoRL 2025 paper with baselines, ablations and stated limitations.

## Key claims

### Method

- **Multi-trial episodes.** An episode is *k* trials (k ~ Uniform(1..K)); memory persists across trials and the objective maximizes expected discounted return **over the whole episode**, not the trial. This is what makes cross-failure learning trainable at all.
- **Adaptation budget.** Training samples an adaptation time budget *u* ~ Uniform(0, U); the policy may take arbitrarily many trials within it before a final scored trial. Deployment at *u*=0 is the zero-shot setting.
- **Transformer-XL backbone.** Fixed-length segments with cached keys/values from the previous segment under stop-gradient, so effective context grows as **O(N·L)** in layers × segment length. Concretely: **6 layers × segment 128 → up to 896 timesteps ≈ 18 s at 50 Hz.** Attention is masked at *episode* boundaries but deliberately **not** at *trial* boundaries.
- **Unified joint space.** A superset of joints subsuming most contemporary legged robots; the policy emits target joint positions in that space and each robot extracts its own. No morphology descriptor, no kinematics input, no system identification.
- **Procedural task space.** Bipeds, quadrupeds and wheeled variants generated from common design principles, randomizing joints and joint ordering plus mass, centre of mass, inertia, control gains and joint limits — *"without actually incorporating any exact robot parameters available on the market."*
- **PPO at scale**, two-phase: short trials and small *U* first to force adaptive behavior, then longer trials for deployment realism.

### Results

Ten unseen robots, **1,000 randomized environments each**, rough terrain, intensified domain randomization. Metric is average displacement toward a sampled goal, normalized to [0,1].

| Method | Average |
|---|---|
| **LocoFormer (zero-shot)** | **0.96 ± 0.19** |
| **LocoFormer (few-shot)** | **0.98 ± 0.13** |
| Conditioning baseline | 0.78 ± 0.37 |
| GRU baseline | 0.37 ± 0.41 |
| **Per-robot expert policy** | **0.99 ± 0.07** |

**A generalist that never saw these robots lands within 0.03 of per-robot experts.** The GRU baseline at 0.37 is the load-bearing ablation: same data, same task distribution, recurrent memory instead of long attention — and it collapses. Architecture, not just scale, is doing the work.

- **TRON1** (a biped *without ankle joints*) is the hardest zero-shot case at 0.87; **5 seconds of adaptation yields ~10%**, to 0.96.
- **Out-of-distribution stress** (2× domain-randomization ranges): **15.4% more robots achieve R > 6**, and the **25th-percentile reward improves by 3.6** — gains concentrated in the tail, which is where locomotion failures live.
- **Representations become embodiment-specific online.** Across 4,096 zero-shot rollouts of four humanoid variants, second-layer activations start nearly identical and **separate into distinct clusters by ~5 seconds** — the policy is building a body model from experience, with no morphology ever supplied.

### Emergent adaptation — all from the same frozen model

| | Perturbation | Behavior |
|---|---|---|
| A | Knee locked mid-walk (quadruped → 3 legs) | Tips forward, then shifts weight back and **walks on three legs after 2–3 s**. Three-legged robots are outside the training design space |
| B | Biped, no ankle motor, single point of support | **Fails trial 1**, retains the failure in cache, **walks stably by trial 3** — then robust to pushes and added weight |
| C | Wheels locked in software mid-roll | Detects the dynamics change and **switches to a walking gait**; also absorbs added mass |
| D | Stilts attached | Adapts step timing and foot placement to the extended limb |
| E | One or two legs locked (wheeled quadruped) | Redistributes load, preserves balance |
| F | **Lower legs cut off** (−4 DoF) | Steps in place, then after **7–8 s** discovers large-amplitude thigh swings and **walks on its knees** |

> [!note] Why (B) is the important one
> A, C, D, E and F are within-trial adaptation — impressive, but a sufficiently reactive policy could in principle do them. **B is different in kind**: the information that makes trial 3 succeed *is the memory of trial 1 failing*. The weights never change. That is in-context reinforcement learning on real hardware, and it is the clearest demonstration in this wiki that "learning" and "training" can come apart at deployment.

### Stated limitations (the authors')

- **Training is highly resource-intensive** compared to a specialist policy — expected given the far wider task distribution and context, but real.
- **The procedural task space is hand-crafted** and "might be hard to design in general." The authors suggest automated task generation from LLMs or web-scale sources as future work.

## Significance for this wiki

- **It supplies the cross-embodiment evidence [S1](skild-s1-blog.md) lacks.** [Skild AI](../entities/skild-ai.md) markets an "omni-bodied brain for any robot"; S1 names no embodiment at all. LocoFormer is where that claim actually lives — for **locomotion**, not manipulation. The distinction should survive any summary of Skild.
- **Two different things are being called in-context learning.** S1 conditions on a **demonstration of the task**; LocoFormer conditions on **its own accumulated experience of the body**. One is few-shot imitation at inference, the other is online system identification. Both avoid weight updates; they are not the same mechanism. See [in-context robot learning](../concepts/learning/in-context-robot-learning.md).
- **Evidence grade is much higher than the rest of the Skild material** — peer-reviewed CoRL 2025, with baselines, an ablation that fails informatively (GRU 0.37), per-robot expert upper bounds, and limitations the authors state themselves. The [S1 blog](skild-s1-blog.md) has none of that.
- **It partly closes a known gap.** The [awesome-physical-ai gap analysis](awesome-physical-ai-github.md) flagged the locomotion corpus (RMA / legged_gym / H2O line) as missing from this wiki. With **[RMA](rma-paper.md)** (Kumar, Fu, Pathak & Malik, RSS 2021 — ingested 2026-08-29), the wiki now holds both ends of that arc: the paper that established fast proprioceptive adaptation and the paper that calls it *myopic*. See the comparison table on [RMA](rma-paper.md#why-this-matters-in-this-wiki).

## Entities mentioned

- [Skild AI](../entities/skild-ai.md) — all three authors; LocoFormer is the company's locomotion line.
- [Deepak Pathak](../entities/deepak-pathak.md) — co-author; Skild co-founder and CEO.
- [Unitree G1](../entities/unitree-g1.md) — evaluated zero-shot (0.98); H1, A1 and Go2-W also in the test set.
- [Boston Dynamics Spot](../entities/spot.md) — evaluated zero-shot (1.00).
- [Unitree A1](../entities/unitree-a1.md) — evaluated zero-shot (0.92); the platform [RMA](rma-paper.md) was built on.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the experience-conditioned mode, as distinct from S1's demonstration-conditioned mode.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — transfer from *procedurally generated robots that do not exist* to ten commercial platforms, with no system identification.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — adaptation across trials on hardware without weight updates.
- [Soft-prompt cross-embodiment](../concepts/learning/soft-prompt-cross-embodiment.md) — an alternative route to one policy across bodies.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — LocoFormer's whole mechanism, with zero gradient steps.

## Open questions

- **No real-robot success-rate table.** Table 1 is simulation. The hardware results are the qualitative Fig. 5 demonstrations — compelling, but not quantified, and with no rollout counts ([success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) applies).
- **How much of the gain is context length vs. procedural diversity?** The GRU ablation confounds architecture with memory horizon; a long-context GRU or a short-context transformer would separate them.
- **Does the recipe transfer to manipulation?** The authors say they *"believe that this simple, yet general recipe can be used to train foundation models for other robotic skills."* [S1](skild-s1-blog.md) is presumably that attempt — but S1 conditions on demonstrations, not on its own experience, so the recipe appears to have changed in the move.
- ~~RMA is uningested~~ — **ingested 2026-08-29** ([RMA](rma-paper.md)). The remaining gap in the arc is the **vision** follow-up (Agarwal, Kumar, Malik & Pathak, CoRL 2022), cited in LocoFormer's related work.
- **Inference cost on-robot.** The paper notes quadratic segment cost and mentions inference acceleration; the deployed compute budget is not given.

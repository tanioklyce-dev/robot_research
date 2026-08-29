---
title: "HIL-SERL — Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning (Luo et al. 2024)"
type: source
url: https://arxiv.org/abs/2410.21845
author: Jianlan Luo, Charles Xu, Jeffrey Wu, Sergey Levine
published: 2024-10
ingested: 2026-07-05
local_path: raw/RL_with_HumanInTheLoop_2410.21845v3.pdf
sha256: 547a4d5d9440a3f70a773798813db1c8a612f006a6994398bbee2a566daab526
venue: arXiv 2410.21845 (v3)
format: pdf
tags: [reinforcement-learning, real-world-rl, manipulation, human-in-the-loop, dexterous-manipulation, imitation-learning, uc-berkeley, dual-arm, contact-rich]
---

**HIL-SERL** (Human-In-the-Loop Sample-Efficient Robotic reinforcement Learning) is a vision-based real-world RL system from [Sergey Levine](../entities/sergey-levine.md)'s UC Berkeley lab that trains **near-perfect (100% success) manipulation policies in 1–2.5 hours of real-world training** by combining a small set of demonstrations, on-policy human corrections, a sparse classifier reward, and the sample-efficient off-policy RL algorithm [RLPD](../concepts/learning/real-world-robot-rl.md). Project + code: [hil-serl.github.io](https://hil-serl.github.io/).

## Summary

The paper's thesis is that with the right *system-level* design choices — not a new algorithm — reinforcement learning can be trained **directly in the real world** to solve a wide range of dexterous, contact-rich, and dynamic manipulation tasks at superhuman reliability and speed, within practical wall-clock times. The core loop: a human supervises training via a SpaceMouse and takes over ("intervenes") when the policy is about to fail or gets stuck; these corrections are folded back into an off-policy RL update ([RLPD](../concepts/learning/real-world-robot-rl.md)) rather than into supervised imitation. Across seven diverse tasks, HIL-SERL reaches **100% success on nearly all of them**, averaging **+101% success rate and 1.8× faster cycle time vs. an HG-DAgger imitation-learning baseline trained on the same human data**. It is, to the authors' knowledge, the first RL system to learn **dual-arm image-based coordination** in the real world, plus previously-infeasible skills like whipping a Jenga block out of a tower and assembling a timing belt.

## Key claims

- **Headline result (§4.3, Table 1a).** 100% success within 1–2.5 hr real-world training on nearly all of 7 tasks (100 eval trials each). HG-DAgger baseline averages **49.7%**. Average improvement **+101% success, 1.8× faster cycle time** (9.6 s → 5.4 s). Gap widens most on the hardest tasks: RAM insertion (29%→100%), Timing belt (2%→100%, "+4900%"), Jenga whipping (8%→100%).
- **Method = system integration, not a new algorithm (§3).** Builds on **[RLPD](../entities/rlpd.md)** ([Ball et al. 2023](rlpd-paper.md)) — an off-policy actor-critic that samples training batches **50/50 from a demo buffer and an on-policy RL buffer**. Predecessor is **[SERL](../entities/serl.md)** ([Luo et al. 2024](serl-paper.md)); HIL-SERL's novelty over SERL is the **online human-correction loop** (SERL used demos only).
- **Human-in-the-loop corrections (§3.4).** Human intervenes via SpaceMouse at any timestep; intervention actions go to **both** the demo and RL buffers, while the policy's own surrounding transitions go **only** to the RL buffer. Interventions are frequent early, then taper toward **0% intervention rate** as the policy converges — the intervention-rate curve is the paper's convergence signal. Similar in spirit to HG-DAgger, but the data trains an RL objective, not supervised BC.
- **Sparse classifier reward (§3.3).** No reward shaping. A **binary success classifier** (trained offline on ~200 positive + ~1000 negative teleop frames, ~5 min of data, >95% eval accuracy) provides the only reward signal.
- **Pretrained vision backbone.** **ResNet-10 pretrained on ImageNet**, shared across wrist + side cameras; embeddings concatenated with proprioception into an MLP. Images cropped and resized to **128×128**. Only 20–30 demos initialize the demo buffer.
- **Egocentric relative-frame trick (§3.3).** Proprioception and actions are expressed relative to the end-effector's episode-start frame, and the EE start pose is randomized each episode. This yields spatial generalization *and* robustness to mid-episode object motion — the RAM policy still inserts when the motherboard is physically moved during insertion.
- **Separate discrete grasp critic.** Gripper control is a **separate DQN** over discrete actions (open/close/stay; 3²=9 for dual-arm) rather than folded into the continuous Gaussian policy — discrete grasping is hard to approximate with a continuous distribution.
- **Beats every baseline (§4.5, Table 1b).** On RAM insertion / dashboard / object flipping, HIL-SERL averages **100%** vs. Diffusion Policy 34%, HG-DAgger 39%, BC 31%, IBRL 57%, Residual RL 32%, DAPG 33%, and **RL-from-scratch 0%**. Feeding SERL 10× more demos (200 vs. 20) without online corrections still fails complex tasks (0% on dashboard) — **online corrections are the crucial ingredient**.
- **Diffusion Policy underperforms on reactive tasks (§4.5).** [Diffusion Policy](../entities/diffusion-policy.md) trained on 200 demos gets only 27% (RAM) / 28% (dashboard) / 56% (flip). The authors argue DP's strength — expressive multi-modal action distributions that "memorize" motions — doesn't help on tasks needing continuous **closed-loop visual servoing** to correct errors.
- **Zero-shot robustness (§4.4).** Learned policies handle adversarial perturbations never scripted in training: forcing grippers open mid-task (policy re-grasps), moving the target during insertion, deforming/repositioning the timing belt, poor grasps (release + regrasp). Emerges purely from autonomous RL exploration.
- **Why RL hits 100% — the "funnel" analysis (§5.1).** State-visitation heatmaps show the policy forming a **funnel** from randomized starts to the target, concentrating mass on high-reward regions. "Critical states" (high Q-value *variance* under action perturbation, Eq. 4) coincide with high Q-values — the policy learns precisely where action choice matters. HG-DAgger's funnel is diffuse by comparison. RL's self-correction via policy sampling is credited as the source of reliability that interactive imitation lacks.
- **Reactive vs. predictive behaviors (§5.2).** The *same* method yields **closed-loop reactive** policies (visual servoing for insertion/assembly) and **open-loop predictive** policies (Jenga whip, pan flip via feedforward end-effector wrenches ≈ commanded accelerations) depending on task demands.
- **Cycle-time speedup is a discounting effect.** With discount γ<1, RL optimizes discounted return and is thus incentivized to finish faster — mechanistically why HIL-SERL beats human-teleop cycle times, which imitation cannot.
- **Hardware/compute.** Single- and dual-arm impedance-controlled setups (impedance controller with reference limiting for contact-rich tasks; feedforward wrenches for dynamic tasks); onboard computation on a **single NVIDIA RTX 4090**. Control loop 10 Hz. Distributed actor/learner/replay architecture.

> [!note] Robot arm not named in the extracted text
> The specific manipulator model is shown in figures/supplementary but does not appear in the extractable body text. HIL-SERL's predecessor [SERL](serl-paper.md) designed its impedance controller around [Franka Panda](../entities/franka-panda.md), and the follow-on [AutoSERL](autoserl-paper.md) runs HIL-SERL-style insertion on a Franka, so Franka is the likely platform — but this ingest does not assert it from the HIL-SERL source text.

## Entities mentioned

- [Sergey Levine](../entities/sergey-levine.md) — senior author.
- [Jianlan Luo](../entities/jianlan-luo.md) — lead author; also lead of [SERL](../entities/serl.md).
- [RLPD](../entities/rlpd.md) — the off-policy base algorithm.
- [SERL](../entities/serl.md) — the demo-only predecessor system.
- [Diffusion Policy](../entities/diffusion-policy.md) — baseline that underperforms on reactive/contact-rich tasks here.
- [Franka Panda](../entities/franka-panda.md) — likely (unconfirmed in text) manipulator.

## Concepts touched

- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — this paper is the anchor; RLPD, SERL, HG-DAgger, sparse classifier rewards.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the baseline family HIL-SERL outperforms; HG-DAgger / BC / DAgger contrast.

## Open questions

- **Generalization across object instances / scenes.** Robustness is shown to perturbations of the *trained* object; cross-instance and cross-scene generalization is not evaluated. Each policy is task-specific.
- **Reward-classifier failure modes.** A binary classifier reward can be gamed or mislabel edge cases; the paper notes collecting extra false-pos/false-neg data but doesn't quantify residual reward hacking.
- **Human-labor accounting.** "1–2.5 hr training" requires a skilled operator continuously supervising with a SpaceMouse. Total human cost vs. a demo-only pipeline isn't tabulated.
- **Value-function pretraining (§5, mentioned).** The authors note a pretrained value function could cut training time further but leave it as future work — a hook toward foundation-model-style RL warm-starts.
- **Relation to VLA-scale RL.** How this real-world HIL loop composes with large pretrained [VLA models](../concepts/learning/vla-models.md) is the natural next question; cf. [π*0.6 / RECAP](pistar06-paper.md), the wiki's VLA-scale RL-from-deployment recipe, which cites the same human-gated-correction lineage.

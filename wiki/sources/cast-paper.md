---
title: CAST — Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models (Glossop, Chen, Bhorkar, Shah, Levine; 2025)
type: source
url: https://arxiv.org/abs/2508.13446
fetch_url: https://arxiv.org/pdf/2508.13446v2
author: Catherine Glossop, William Chen, Arjun Bhorkar, Dhruv Shah, Sergey Levine
published: 2025-08-19
ingested: 2026-09-11
venue: arXiv v2 (2026-06-08); 12 pp.
local_path: raw/2508.13446v2.pdf
sha256: 0d0e4c0832583f22abaf4b482966332c880daa4bb810727d616fa9cbd9dcaf52
format: pdf
tags: [cast, counterfactual, language-following, posterior-collapse, vla, paligemma, synthetic-labels, gemini, navigation, manipulation, bridge, steerability, berkeley, rail, mutual-information]
---

## Summary

A data-augmentation method for the failure every language-conditioned policy has: **the instruction is ignored because the observation already predicts the action.** If a robot only ever approaches a door when a door is visible, the label adds nothing and the policy learns to drop it — *posterior collapse*, borrowed from VAEs. CAST breaks the correlation by attaching **several different instructions with several different action endings to the same observation**: a VLM (Gemini 2.5 Pro) proposes counterfactual instructions at decision points ("turn right into the kitchen" where the robot went straight), each paired with an **atomic command** ("turn right"); a small **atomic policy**, trained on heuristically segmented real data, turns the command into an 8-step action chunk that branches off the original trajectory. Trained on GNM data augmented this way, a 3B PaliGemma VLA (**CounterfactualVLA**) follows complex navigation instructions **27 points** better than the identical VLA trained on hindsight labels alone and 19 points better than the best prior method, over 645 real trials; on Bridge manipulation with distractors it **doubles** success. The paper's conceptual contribution is an argument that this maximizes a lower bound on I(action; language | observation).

## Key claims

### The argument (§IV-A)

- Language is attended to only when it carries information about the action beyond the observation: I(a; ℓ | o). With the chain ℓ → a → ℓ_a (instruction determines action, action determines its atomic command), the data-processing inequality gives **I(a; ℓ | o) ≥ H(ℓ_a | o) − H(ℓ_a | ℓ, o)**. So: many different atomic commands per observation (high H(ℓ_a | o)), each uniquely implied by its instruction (low H(ℓ_a | ℓ, o)). CAST "approximates just this"; the authors call the relationship heuristic.

### The pipeline (§IV-B, §V)

- **Atomic decomposition** of navigation trajectories by yaw-change thresholds into {turn right, turn left, adjust right, adjust left, go forward, stop}; labels are functions of the actions alone, so the atomic policy (EfficientNet-b2 + T5 + action-chunk diffusion) follows them reliably and inherits collision avoidance from real data.
- **Hindsight labels** for unlabeled GNM data: Gemini 2.5 Pro describes objects and relations from a subsampled frame sequence, proposes instructions, then a second pass filters against the atomic sequence. 65K trajectories → 320K labels → **filtered to 16K trajectories, 65K labels, 86K counterfactual chunks.**
- **Counterfactuals** are generated at atomic-segment boundaries; no counterfactual *observations* are produced — action chunking lets the policy "be perturbed from states covered in the existing data toward states aligned with the counterfactual task."
- **VLA:** PaliGemma 3B (Gemma 2B + SigLIP 400M) with 128 added action tokens for binned Cartesian deltas; 40K steps, v4-16 TPU, batch 384; 4 Hz via a PD controller.
- **Manipulation:** all 60K Bridge trajectories, subtask decompositions from Steerable Policies as atomic commands, 500K counterfactual instruction-action pairs; same backbone with 512 action tokens; 8×H200, 60K steps.

### Results

- **Label quality (11 judges, 440 labels):** hindsight **60.5% correct**, counterfactual **69.4%**; the dominant error is *grounding* (the VLM hallucinates the motion-to-scene relation; counterfactual endings that would collide). "Although these labels are noisy… they still provide sufficient language-action diversity."
- **Navigation (27 tasks × 3 environments × 5 trials = 645 trials, 21 h):** CounterfactualVLA **+27 points** over the standard VLA trained on hindsight labels only, **+19** over the best prior method. CoNVOI (VLM + LiDAR planner) matches on object and referential tasks and fails on *continuous* ones ("move along the wall"); π_a + planning (VLM picks atomic commands at test time, same atomic policy) "performs poorly on all tasks."
- **Manipulation (120 trials, 6 tasks with distractors):** without distractors the two VLAs tie; with them the standard VLA "oscillates between modes" and CounterfactualVLA is **2×** better.
- **Robustness (Table I):** morning 63% / night 63% — lighting does nothing; a person walking in front drops it to **37–43%**, attributed to 4 Hz inference and the absence of counterfactual observations.
- **Architecture ablation (Fig. 6):** ResNet + FiLM with a frozen CLIP encoder (the [LeLaN](lelan-paper.md) architecture) handles object-navigation and atomic commands but fails complex instructions — "a high-capacity model is needed to make full use of" diverse language.

## Reading it against the wiki

- **Posterior collapse is the named mechanism behind a pattern the wiki has recorded from the outside** — [π0.5](pi-zero-5-paper.md) buying scene generalization but not instruction generalization; the OmniVLA edge model matching the 7B on pose and image goals and losing only on language. CAST's diagnosis is that the *data* makes language redundant, and the fix is data-side.
- **The counterfactual actions are synthetic, from an atomic policy.** This is the third variant of the RAIL line's move — [LeLaN](lelan-paper.md) synthesizes actions from NoMaD, [MBRA](mbra-paper.md) from a forward model, CAST from an atomic-command policy — and the first whose labels are audited: **~60–70% correct**, and it still works. That number is the honest prior for every VLM-labeled robot dataset in the wiki.
- **The manipulation result needs its distractors.** Without them the augmentation is worthless, because the task is inferable from the image. Any language-following benchmark without distractors is measuring observation-following.

## Entities mentioned

- [Dhruv Shah](../entities/dhruv-shah.md), [Sergey Levine](../entities/sergey-levine.md); Catherine Glossop, William Chen, Arjun Bhorkar.
- PaliGemma (backbone), Gemini 2.5 Pro (labeler), Bridge / WidowX (manipulation), CoNVOI and NaVILA-style hierarchies (baselines) — no pages.

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [VLA models](../concepts/learning/vla-models.md), [imitation learning](../concepts/learning/imitation-learning.md), [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md).

## Open questions

- Absolute success rates per task are in Table II of the PDF (not transcribed); the headline deltas are what the text reports.
- Whether counterfactual *observations* (generated video) would fix the dynamic-obstacle failure, as the authors suggest, or introduce the drift they fear.

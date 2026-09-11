---
title: NoMaD — Goal Masked Diffusion Policies for Navigation and Exploration (Sridhar, Shah, Glossop, Levine; ICRA 2024)
type: source
url: https://arxiv.org/abs/2310.07896
fetch_url: https://arxiv.org/pdf/2310.07896v1
author: Ajay Sridhar, Dhruv Shah, Catherine Glossop, Sergey Levine
published: 2023-10-11
ingested: 2026-09-11
venue: ICRA 2024 (arXiv v1)
local_path: raw/2310.07896v1.pdf
sha256: 05fe73918a7e454c6a006b7cba9aaec6bfc46ce96f65e28eb7a0967263a48af9
format: pdf (8 pp.)
tags: [nomad, navigation, visual-navigation, diffusion-policy, goal-masking, exploration, multimodal-actions, topological-memory, jetson-orin, berkeley, rail, shah, levine]
---

## Summary

One policy for both **goal-directed navigation** and **goal-agnostic exploration**, and — the paper's own claim — "the first successful instantiation of a goal-conditioned action diffusion model… deployed on a physical robot." NoMaD keeps [ViNT](vint-paper.md)'s EfficientNet-B0 + Transformer encoder and adds two things: a binary **goal mask** applied in attention (sampled with p = 0.5 during training, set by the user at test time) so the same context vector can be goal-conditioned or not, and a **[Diffusion Policy](../entities/diffusion-policy.md)** head (1-D conditional U-Net, 10 denoising steps) that models the multimodal distribution over 8-step action chunks — bimodal at a junction, snapped to one mode when a goal image is given. With 19M parameters it beats ViNT's 335M subgoal-diffusion system on exploration by **25 points with 8× fewer collisions**, matches it on navigation, and runs on a Jetson Orin.

## Key claims

### Method (§IV)

- Goal masking: m = 1 blocks attention to the goal token (exploration), m = 0 attends to it (goal-reaching); Bernoulli(0.5) during training gives equal samples of each.
- Diffusion: conditional (not joint) action distribution p(a_t | c_t) so the visual encoder trains end-to-end and inference is real-time; square-cosine schedule, K = 10 steps, 15-layer 1-D conditional U-Net as the noise predictor; auxiliary temporal-distance loss weighted 10⁻⁴.
- Trained on **GNM + SACSoN (>100 h)**, 30 epochs, batch 256, 96 × 96 images, 4-layer 4-head 256-D Transformer; **19M parameters**.
- Deployed with a topological graph and frontier-based exploration, as in ViKiNG.

### Results (six indoor/outdoor environments; success and collisions per run)

| Method | Params | Exploration success | Collisions | Navigation success |
|---|---:|---:|---:|---:|
| Masked ViNT (point estimates) | 15M | 50% | 1.0 | 30% |
| VIB (RECON) | 6M | 30% | 4.0 | 15% |
| Autoregressive (discretized) | 19M | 90% | 2.0 | 60% |
| Random Subgoals (ViNT-R) | 30M | 70% | 2.7 | 90% |
| Subgoal Diffusion (ViNT system) | 335M | 77% | 1.7 | 90% |
| **NoMaD** | **19M** | **98%** | **0.2** | **90%** |

- **Unified vs dedicated (Table II):** NoMaD matches a plain Diffusion Policy on undirected exploration (98% vs 98%) and the ViNT checkpoint on goal-reaching (92% vs 92%) at comparable size — "training for these two behaviors involves learning shared representations."
- **Encoder ablation (Table III):** late-fusion CNN 52% / 3.2 collisions; early-fusion CNN 68% / 1.5; ViT with attention masking 32% / 2.5 ("optimization challenges in training end-to-end with diffusion"); ViNT encoder + attention masking **98% / 0.2**.
- Autoregressive discretized actions "can (in principle) express multimodal distributions, [but] the predictions are largely unimodal, equivalent to the policy learning the average action distribution," and the deployed policy is "jerky and slow to respond."

### Limitations

Goal images only ("not the most natural modalities for users"); frontier exploration is a fixed high-level strategy. Both are what [OmniVLA](omnivla-paper.md) and MBRA later address. The paper says six environments in the text and five in Table I's caption.

## Reading it against the wiki

- **Action diffusion beats image diffusion for the same job, at 1/15 the size.** ViNT generated subgoal *pictures* and was rescued by the policy's tolerance of bad ones; NoMaD generates *actions* directly and needs no rescue. This is the navigation-scale version of the wiki's repeated finding that pixels are the wrong target ([mimic-video](mimic-video-paper.md), the Unitree WMA-0 → WLA-1.0 retreat on the [world-action model](../concepts/world-models/world-action-model.md) page).
- **Why diffusion, stated cleanly:** exploration is inherently multimodal (left or right at a junction, never the average), and the autoregressive baseline collapses to the mean. This is the same argument [Diffusion Policy](../entities/diffusion-policy.md) made for manipulation, confirmed on a robot with a competing discretized-token baseline in the same table.
- **Goal masking is task dropout.** Randomly hiding the conditioning during training to get one model that works with and without it is the pattern OmniVLA generalizes to *modality* dropout, and that the KI recipe uses for action representations.

## Entities mentioned

- [Dhruv Shah](../entities/dhruv-shah.md), [Sergey Levine](../entities/sergey-levine.md); Ajay Sridhar, Catherine Glossop.
- [Diffusion Policy](../entities/diffusion-policy.md) — the head; ViNT — the encoder; LoCoBot (deployment platform).

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [imitation learning](../concepts/learning/imitation-learning.md), [world-action model](../concepts/world-models/world-action-model.md) (the pixels-vs-actions target question).

## Open questions

- Per-environment numbers are not given; 98% on ~6 environments is a small denominator.
- Whether goal masking costs anything at scale — OmniVLA's modality dropout suggests not, but on a different backbone.

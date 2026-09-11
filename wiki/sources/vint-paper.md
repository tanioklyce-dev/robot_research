---
title: ViNT — A Foundation Model for Visual Navigation (Shah, Sridhar, Dashora, Stachowicz, Black, Hirose, Levine; CoRL 2023)
type: source
url: https://arxiv.org/abs/2306.14846
fetch_url: https://arxiv.org/pdf/2306.14846v2
author: Dhruv Shah, Ajay Sridhar, Nitish Dashora, Kyle Stachowicz, Kevin Black, Noriaki Hirose, Sergey Levine
published: 2023-06-26
ingested: 2026-09-11
venue: CoRL 2023, oral (arXiv v2, 2023-10-24)
local_path: raw/2306.14846v2.pdf
sha256: 175369795be4c276d74c76aa39c4c977b742d994bb717fcdf582052dc311d37d
format: pdf (25 pp. incl. appendix)
tags: [vint, navigation, visual-navigation, foundation-model, transformer, cross-embodiment, image-goal, subgoal-diffusion, physical-search, topological-memory, prompt-tuning, fine-tuning, carla, unitree-go1, berkeley, rail]
---

## Summary

The GNM idea rebuilt as a **"foundation model"** — defined here as a model that (i) deploys zero-shot on new sensors, bodies and environments and (ii) adapts to new tasks with little data. ViNT is a **31M-parameter** decoder-only Transformer over EfficientNet-B0 tokens (P = 5 past frames plus a **goal-fusion token**), trained on **>100 h from 8 robot platforms** with GNM's normalized-waypoint action space, run at 4 Hz through a PD controller. Three things make it more than a bigger GNM. First, a **318M image-to-image diffusion model** proposes candidate subgoal images which ViNT grounds and an A*-like **physical search** scores, giving exploration and **kilometer-scale** guided navigation (1.27 km on GPS, 1.04 km on satellite imagery, no interventions). Second, the goal-fusion design — chosen because late fusion fails and early fusion cannot be adapted — lets the goal encoder be **swapped for a "soft prompt"** from another modality (GPS waypoints, turn-by-turn routing) with under an hour of data. Third, **emergent behaviors**: with random, unreachable subgoals ViNT still reaches goals 80% of the time, prefers paved roads and hallway centers despite weavy training data, and avoids dynamic pedestrians. It drives a **Unitree Go1** zero-shot (45 m max displacement vs GNM's 8 m), the wiki's first appearance of that quadruped.

## Key claims

### Architecture (§3, Appendix A)

- Tokens: current + P = 5 past 85 × 64 images each through EfficientNet-B0 → 512-D; a separate **goal-fusion encoder** takes the current and goal images channel-stacked (6 × 85 × 64). Decoder-only Transformer, 4 layers × 4 heads, d_FF = 2048; heads predict temporal distance d and H = 5 normalized waypoints. 31M params; trained from scratch, 8×V100, 30 h.
- **Why goal fusion (Table 5):** late fusion (independent goal encoder) "often ignor[es] the goal entirely" — "effective features for image-based goal-reaching tasks are often *relative*"; early fusion (goal stacked onto every frame) performs best but cannot be adapted to new goal modalities; FiLM as in RT-1 was unstable. Goal fusion nearly matches early fusion and keeps a swappable goal token.
- Maximum subgoal distance 20 steps; distance-loss weight λ = 0.01.

### Exploration and long-horizon navigation (§4)

- Subgoal diffusion: 318M-param U-Net, 128 × 128, trained on future frames 5–20 steps ahead from ViNT's data, DDIM 200 steps, classifier-free guidance; TPU v4-8, 30 h. Samples "are often of low quality with many artifacts" — ViNT's robustness to bad subgoals is what makes the system work.
- Physical search: cost f(s) = graph distance to parent + predicted distance + heuristic h; h = 0 for coverage, Euclidean for position/GPS goals, a learned satellite-image heuristic outdoors.
- **Table 1 — coverage exploration success:** ViNT **0.94 indoor / 1.00 outdoor**; ViNT-R (random subgoals) 0.81 / —; end-to-end BC 0.72 / 0.44; end-to-end GCG — / 0.61; RECON (VIB) 0.19 / 0.23.
- **Table 2 — guided navigation vs ViKiNG:** indoor position goals 0.60 → **0.90** success (56 → 91 m); outdoor GPS 0.64 → **0.95**, SPL 0.42 → 0.84, 720 → **1,270 m**; satellite-guided 0.77 → **1.00**, SPL 0.68 → 0.94, 780 → 1,040 m.

### Zero-shot cross-embodiment (Table 3, max displacement without intervention, m)

| Robot | single-robot model | GNM | **ViNT** |
|---|---:|---:|---:|
| LoCoBot | 40 | 60 | **120** |
| **Unitree Go1** (not in training data) | 12 | 8 | **45** |
| Vizbot | 40 | 20 | **110** |
| Jackal | 184 | 427 | **438** |

"Positive transfer for in-domain robots (Vizbot)… an emergent phenomenon not present in smaller models."

### Fine-tuning and adaptation (Table 3 right, CARLA)

- Full fine-tune, image goals, <5 h data: **ViNT 0.82** success / 0.82 in-lane vs GNM 0.49 / 0.66, ImageNet 0.22, SimCLR 0.21, VC-1 0.19, scratch 0.45. "General pre-trained visual representations… are not sufficient to extract navigational affordances."
- Adaptation via a new goal token: GPS positions **0.89** vs GNM 0.45; routing commands **0.72** vs GNM 0.49. 40% zero-shot → 80% with <1 h of fine-tuning data, beating a single-domain model trained on 5× the data.

### Limitations (§7)

Transformer inference cost on power-constrained platforms; assumes structural similarity — cannot control a quadcopter's altitude or ingest LiDAR.

## Reading it against the wiki

- **The soft-prompt trick predates X-VLA by two years.** ViNT's "learn a small network mapping a new goal modality into the goal-token space, keep the rest frozen" is the same move [X-VLA](../entities/x-vla.md) makes with per-embodiment [soft prompts](../concepts/learning/soft-prompt-cross-embodiment.md) — here applied to *task modality* rather than embodiment, and citing Lester et al.'s prompt tuning directly.
- **Generic visual pretraining loses to task-relevant robot data**, again: ImageNet / SimCLR / VC-1 backbones all underperform a 31M navigation model on CARLA. The same ordering GNM found, at higher stakes.
- **The subgoal-image diffusion model is the part NoMaD deletes.** 318M parameters to generate images that are often invalid, rescued by ViNT's default collision-free behavior — [NoMaD](nomad-paper.md) replaces it with a 19M action-diffusion policy and gains 25% on exploration. A concrete instance of the wiki's recurring finding that pixel generation is rarely the useful world-model target ([world-action model](../concepts/world-models/world-action-model.md)).
- **Max displacement without intervention** as a metric (Table 3) is a coverage-style number worth remembering for [policy evaluation](../concepts/robotics/robot-policy-evaluation.md): it measures how far a policy can be trusted, not whether it hit one goal.

## Entities mentioned

- [Dhruv Shah](../entities/dhruv-shah.md), [Noriaki Hirose](../entities/noriaki-hirose.md), [Sergey Levine](../entities/sergey-levine.md); Sridhar, Dashora, Stachowicz, Kevin Black (later of [π0](../entities/pi-zero.md)).
- [Unitree Go1](../entities/unitree-go1.md) — first wiki appearance; LoCoBot, Vizbot, Jackal, DJI Tello.
- [X-VLA](../entities/x-vla.md) — the later soft-prompt parallel.

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [soft prompts for cross-embodiment](../concepts/learning/soft-prompt-cross-embodiment.md), [world-action model](../concepts/world-models/world-action-model.md), [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).

## Open questions

- Table 3 mixes two tables under one number in the PDF (displacement; CARLA) — the wiki separates them above.
- The eight-platform, >100 h mixture is only itemized in Appendix C (not transcribed here); GNM's 6-robot / 60–70 h is the documented core.

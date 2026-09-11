---
title: Learning to Drive Anywhere with Model-Based Reannotation (MBRA / LogoNav)
type: source
url: https://arxiv.org/abs/2505.05592
fetch_url: https://arxiv.org/pdf/2505.05592v3
author: Noriaki Hirose, Lydia Ignatova, Kyle Stachowicz, Catherine Glossop, Sergey Levine, Dhruv Shah
published: 2025-05-08
ingested: 2026-09-11
venue: IEEE Robotics and Automation Letters 2025 (arXiv v3, 2025-11-21)
local_path: raw/2505.05592v3.pdf
sha256: 4b01fd37ca6154b11050ec3e7ae6cbd5d66530e21e05df1b78e346c9fabb50dc
format: pdf (9 pp., 8 figures, 6 tables)
tags: [mbra, logonav, navigation, visual-navigation, frodobots, crowdsourcing, passive-data, action-relabeling, model-based-learning, inverse-dynamics, youtube-video, cross-embodiment, berkeley, rail, levine, shah, hirose, earth-rovers, unitree-go1]
---

## Summary

Berkeley RAIL's answer to a specific question: **what do you do with 2,000 hours of crowdsourced robot data whose action labels are garbage?** [FrodoBots-2K](../entities/frodobots.md) — gamer-teleoperated sidewalk rovers in 10+ cities — is 25× larger than any public visual-navigation dataset (Table I), but its actions are corrupted by cheap GPS/IMU, wheel slip, vibration, inconsistent operators, and internet delay, so policies trained on them fail. **Model-Based ReAnnotation (MBRA)** trains a short-horizon relabeler that *never imitates the actions*: it emits an 8-step velocity chunk, rolls it through a differentiable unicycle model plus a monocular-depth collision count, and is trained to land on a state ~7 s ahead without collisions. That relabeler then rewrites every action in the dataset — and can also **generate** actions for 100 hours of action-free YouTube walking tours — and the clean labels are distilled into **LogoNav**, a GPS-waypoint-conditioned long-horizon policy. LogoNav reaches goals **300+ m away** through pedestrians on the Earth Rover, transfers unchanged to a wheeled VizBot and a Unitree Go1 quadruped, and the relabeler alone is evaluated in **six countries on three continents** — "the first global evaluation for visual navigation." The paper is the strongest evidence in this wiki that **the value of crowdsourced robot data is its observations, not its actions**, and that a model-based objective, unlike an inverse-dynamics model, keeps improving as noisy data is added.

## Key claims

### The problem, in the authors' words (§IV-A)

- FrodoBots-2K: 2,000 h, 10+ cities; after EKF smoothing (bidirectional, fusing raw commands, wheel speeds, GPS, compass) and dropping long pauses, **~700 h** remain — "still an order of magnitude larger than any currently available visual navigation dataset," but "the signal remains too noisy for direct training."
- Five named noise sources: robot inconsistencies and the operator's corrections for them, low-cost GPS/IMU, wheel slip in turns, vibration in turns, and **system delay**.
- Curated navigation datasets (RECON, GO Stanford, SCAND, HuRoN, TartanDrive, …) sum to "dozens of hours" — Table I lists the largest at 75 h.

### The method (§III–IV)

- **Relabeler π^s(O_c; O_g)** → 8 actions at 3 Hz (linear + angular velocity). Objective J_mbl = Σ (s_ref − ŝ_i)², where ŝ_i = [pose, collision count, action difference] comes from a **frozen differentiable forward model f**: unicycle integration for pose, a Depth360 monocular depth estimate of O_c for collisions. Target s_ref = [goal pose, 0, 0]. **Only the distant target is supervised**, "not to be sensitive for low-quality states in the dataset." Goals are sampled up to N_g = 20 steps (~7 s) ahead.
- **Delay-aware.** The network takes the delay length L and the previous L actions as inputs (receding-horizon-control style); LogoNav instead executes the L-th predicted step at inference, as UMI and ViNT do.
- **Architecture:** EfficientNet-B0 encoders for (current+goal) and for history, Transformer + MLP head. LogoNav swaps the goal-image encoder for an MLP over the relative 2-D goal pose p_g, sampled up to N_g = 100 steps (~33 s, ~50 m) ahead — "at least 10 times further" than the relabeler's ~3 m.
- **Training data:** relabeled FrodoBots-2K co-trained with the GNM mixture (RECON, GO Stanford, CoryHall, TartanDrive, HuRoN, Seattle, SCAND) at GNM's weights; π^s frozen while π^l trains.
- **Why not an inverse-dynamics model?** VPT-style IDMs and multi-step goal-conditioned policies (GCP) must be trained on other datasets (distribution shift) or on the noisy labels; MBRA "generates synthetic actions that are optimized to reach future states… while satisfying basic navigational objectives via a forward model, rather than greedily maximizing the probability of the action given a pair of adjacent states."

### Results

**Table II — LogoNav, GPS goals, 7 outdoor sites × 3 trials (n = 21).** GS = goal success, COV = fraction of goal distance covered before failure.

| Policy | FrodoBots-2K | Relabeler | GS | COV |
|---|---|---|---:|---:|
| NoMaD | no (GNM only) | — | 0.333 | 0.471 |
| NoMaD | yes | EKF-filtered | 0.286 | 0.429 |
| BC | yes | raw actions | 0.286 | 0.567 |
| BC | yes | EKF-filtered | 0.286 | 0.624 |
| BC | yes | visual SLAM (DPVO) | 0.286 | 0.486 |
| BC | yes | VPT inverse model | 0.095 | 0.314 |
| BC | yes | GCP | 0.619 | 0.757 |
| **LogoNav** | yes | **MBRA** | **0.857** | **0.924** |

- **Table III — cross-embodiment, 10 trials each, ≤100 m:** Go1 quadruped GS 0.30 → **0.80** (GCP → MBRA), COV 0.68 → 0.85; VizBot indoor GS 0.20 → **0.60**, COV 0.63 → 0.82. Same policy, no adaptation; action conversion inside each robot stack.
- **Table IV — action-free YouTube (100 h, 32 countries), goal-image policy, 8 routes of 10–31 m:** GNM only 0.500 / 0.680; + video labeled by visual SLAM **0.125** / 0.313; + video labeled by MBRA **0.875** / 0.909. SLAM "often fails on videos with fisheye lenses, dense crowds, or few features."
- **Table VI — the data-scaling ablation (short-horizon, 8 routes):** GCP on raw FrodoBots actions collapses to **0.000** GS; with EKF-filtered data GCP peaks at **1%** of the dataset (0.750) and *falls* at 10/40/70/100% (0.375–0.500). MBRA is 0.875 with GNM alone and reaches **1.000 / 1.000 at 40%, 70% and 100%**.
- **Table V — six countries (USA, Mexico, China, Mauritius, Costa Rica, Brazil), 24 topological graphs:** GCP 0.500 → 0.736 (GNM → +1% FrodoBots); MBRA 0.833 → **0.899 GS / 0.983 SC** (GNM → +full FrodoBots).
- Fig. 7: ~20 min, ~300 m, subgoals every ~80 m, no collisions, human-occupied spaces.

### Stated limitations (§VI)

The forward model can produce "unreasonable actions because of inaccuracies in the robot model"; the approach "does require some strong conditions on the model itself that could prove difficult to translate to more complex tasks like **manipulation**"; human preferences (staying off grass, crowd norms) are inherited from the data, not enforced. Applicability to other navigation tasks is claimed via OmniVLA (arXiv 2509.19480).

## Reading it against the wiki

> [!note] Crowdsourced actions: the number is zero
> The [crowdsourcing](../concepts/learning/crowdsourced-robot-training-data.md) page asked how much of a crowdsourced action stream survives relabeling. Table VI answers for FrodoBots-2K: a policy imitating the raw actions scores **0.000**, and even after Kalman smoothing, adding more than 1% of the data makes an imitation-based relabeler *worse*. Every useful bit came from the images. This is the robot-teleop counterpart to what the human-video crowdsourcers (Go-Big, Index, [DreamDojo](dreamdojo-paper.md)) assume from the start — that the actions have to be inferred — with the difference that here the actions *existed* and still had to be thrown away.

- **Model-based versus inverse-dynamics labeling.** The wiki's video-to-action thread — VPT-style IDMs, [DreamDojo](dreamdojo-paper.md)'s continuous latent actions, [UniT](../concepts/learning/latent-action-tokens.md)'s cross-reconstruction — labels video by predicting actions from adjacent frames. MBRA's claim is that this is the wrong objective under heavy noise, and its Table VI is the cleanest ablation of that claim: the IDM route peaks early and degrades, the forward-model route scales monotonically. The cost is stated honestly: you need a differentiable robot model and a collision proxy, which navigation has (unicycle + monocular depth) and manipulation mostly does not.
- **Coverage rate** is a partial-credit metric worth keeping — it separates "never left the start" from "failed at 90%," which binary success hides; see [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).
- **Sample sizes are small** — 21, 10, 8, and 24 trials per cell. By the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline the 0.857-vs-0.619 headline is a real gap (≈5 of 21 trials), the 1.000s in Table VI are 8-trial cells, and the six-country result is the strongest because n = 24 and the sites are independent. Read the *ordering* of the ablation, which is consistent across four tables, rather than any one number.
- **Delay is treated as a first-class input**, not noise — the same ~500 ms link the [Earth Rover Challenge](earth-rover-challenge-frodobots-2k.md) runs on. Feeding L and the last L actions to the relabeler is a small, transferable idea for any policy trained on remotely teleoperated data.

## Entities mentioned

- [FrodoBots](../entities/frodobots.md) — FrodoBots-2K and the Earth Rover Zero (data collection and main evaluation platform).
- [Dhruv Shah](../entities/dhruv-shah.md), [Noriaki Hirose](../entities/noriaki-hirose.md), [Sergey Levine](../entities/sergey-levine.md); Kyle Stachowicz, Catherine Glossop, Lydia Ignatova (Berkeley RAIL).
- Unitree Go1 (no page; see [Unitree](../entities/unitree.md)); VizBot; [Open X-Embodiment](../entities/open-x-embodiment.md) and [DROID](../entities/droid.md) cited as the manipulation-side "internet data doesn't transfer" precedents.

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md) — new concept page; GNM → ViNT → NoMaD → LogoNav lineage.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md), [imitation learning](../concepts/learning/imitation-learning.md), [latent action tokens](../concepts/learning/latent-action-tokens.md) (the IDM-labeling alternative), [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).

## Open questions

- Does relabeling preserve operator *intent* (the paper says image sequences "still reflect the teleoperator's semantic intent") or replace it with the forward model's preferences? No metric separates the two.
- How much of the 700 filtered hours actually mattered — the ablation is on fractions of the filtered set, and 40% already saturates the 8-route test.
- What the manipulation analogue of "unicycle + depth-based collision" would be; the authors say none is obvious.
- The Berkeley-FrodoBots-7K release ([challenge site](earth-rover-challenge-frodobots-2k.md)) is described as the full ~7,000 h "reannotated with MBRA" — the paper only uses 2,000 → 700 h; the 7K relabeling is undocumented.

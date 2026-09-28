---
title: Robostral Navigate (Mistral AI, arXiv 2607.20785)
type: source
url: https://arxiv.org/abs/2607.20785
fetch_url: https://arxiv.org/pdf/2607.20785v3
author: Mistral AI (14 core contributors incl. Arjun Majumdar, Guillaume Lample, Khyathi Raghavi Chandu; 276 authors listed)
published: 2026-07-22
ingested: 2026-09-28
venue: arXiv (cs.RO) technical report; v3 2026-07-31
format: pdf, 12 pages
local_path: raw/robostral-navigate_2607.20785v3.pdf
sha256: b8cc86d333f57d2904d0f3a003b68e14c4d571ab951593aeaca69419d0b825e0
related_raw: "raw/2026-07-08-mistral-robostral-navigate-blog.md (launch blog, mistral.ai/news/robostral-navigate)"
tags: [mistral, robostral, navigation, vision-language-navigation, vln-ce, r2r-ce, rxr-ce, habitat, pointing, monocular-rgb, cross-embodiment, sim-only-training, prefix-caching, tree-attention-mask, online-rl, cispo, diffusion-policy, hierarchical-policy, closed-weights]
---

## Summary

**Robostral Navigate** is [Mistral AI](../entities/mistral-ai.md)'s first robotics model. It is an **8B vision-language model for instruction-following navigation** that sees only a **single monocular RGB stream** and outputs its next waypoint **by pointing**: the pixel coordinates (u, v) of the farthest visible point on the path, plus the heading change on arrival. When the target is out of view, it falls back to a metric displacement (Δx, Δy, Δθ). It is trained entirely in simulation on **2.4M trajectories across 350k scenes**. The SFT recipe packs a whole episode into one sequence behind a **prefix-tree attention mask**, which cuts training tokens **22×** ("months to days"). It is then post-trained with online RL (**CISPO**) on 35k hard tasks. The paper reports state of the art on **R2R-CE val-unseen (77.4% SR, 74.2% SPL)** and **RxR-CE (75.1% SR, 68.7% SPL)**, beating every monocular method and, on R2R-CE, every depth or multi-camera method. The real-robot story is a three-level hierarchy: VLM at **0.5 Hz** → 121M diffusion transformer outputting 1-second chunks → embodiment-specific tracker at **100 Hz**. The same weights run on a [Galaxea R1](../entities/galaxea-r1.md) and a [Hiwonder](../entities/hiwonder.md) JetAuto. **No weights, code or data are released**; the blog ends in "talk with our team."

> [!warning] What the benchmark numbers actually measure
> §4: *"For these evaluations, we use a pathfinder from Habitat … for navigation between the waypoints predicted by Robostral Navigate."* So the headline R2R-CE/RxR-CE numbers score the **VLM's waypoint choices with Habitat's map-based oracle planner doing the moving**, not the diffusion policy and tracker described in §2. Most of the Table 1 baselines (NaVid, Uni-NaVid, NaVILA, StreamVLN) emit **low-level discrete actions** (0.25 m forward / 15° turn) and have to avoid obstacles themselves. That is the harder setting, and why the older VLN-CE literature split "waypoint" and "low-level" tracks ([Krantz et al. 2021](https://arxiv.org/abs/2110.02207), which the paper cites). The "single RGB camera, no pre-built maps" framing is true of the deployed system but **not of the benchmarked one**. The gain over monocular baselines (+10.5 on R2R-CE) is not like-for-like. It mixes a better high-level policy with an easier low-level setting, and the paper has no ablation separating the two.

## Key claims

### Architecture (§2)

- **Base model.** "A dense 8B-parameter VLM designed for spatial grounding tasks such as pointing, counting, and object localization." It is unnamed in the paper. The blog adds that it is "built entirely in-house and does not rely on existing open-source VLMs." Frames go through a vision encoder, and the visual tokens are appended to the instruction. The full frame history is kept.
- **Pointing with displacement fallback (§2.2).** With the target visible, the output is all five of **(u, v, Δx, Δy, Δθ)**, so the metric terms act as a co-training signal. With it out of view (≈**10%** of training data), the output is just (Δx, Δy, Δθ). There is also a **STOP** token. The waypoint is the *farthest visible* point on the ground-truth path.
- **Pointing → actions (§2.3).** A **~121M DiT** takes the waypoint, robot height and radius, the frame the VLM saw, and the current frame (to compensate for VLM latency). It outputs **30 (dx, dy, dθ) deltas for the next second**. An embodiment-specific motion controller then turns that into motor commands.
> [!note] Internal inconsistency on the diffusion policy's rate
> §2.1 and Fig. 1 say the diffusion policy outputs a trajectory "at 10 Hz", but §2.3 says one chunk is "a sequence of 30 delta coordinates … for the next second," which is 30 Hz sampling. Either it's a 30-step chunk replanned at 10 Hz, or one of the two figures is wrong. The paper doesn't say which.
- **Cross-embodiment by randomization (§2.4).** Sim data randomizes robot height (0.4–1.8 m), radius (0.15–0.45 m), camera height (70–100% of robot height) and camera pitch (0–25°). The two robots shown, the wheeled bimanual [Galaxea R1](../entities/galaxea-r1.md) and the small Jetson-based Hiwonder JetAuto, share the VLM and DiT weights; only the low-level controller differs. The abstract and blog also claim **legged and aerial** robots, but the paper shows only these two wheeled platforms and gives **no real-world success numbers** for either.

### Training (§3)

- **Data (§3.1).** A sim pipeline with farthest-point-sampled start/goal pairs, some multi-floor, across "offices, residential buildings, commercial spaces, and outdoors." It cites Habitat and **HM3D**, but 350k scenes is ~350× HM3D's 1,000, so **the scene source is undisclosed**. So is whether the MP3D scenes behind R2R-CE/RxR-CE val-unseen are excluded. The **instruction source** (templated, LLM-generated or human) is also not described.
- **Prefix-tree SFT (§3.2).** Training per time step costs O(T²) tokens per episode. Packing `I | O₀ | a₀ | … | Oₙ | aₙ` into one sequence makes it O(T). A **tree attention mask** hides earlier ground-truth actions, because they leak future actions under the farthest-visible-waypoint labeling. The paper claims it gives a "provably identical training signal" to per-step samples and **22× fewer tokens**, mattering most on RxR's long episodes. It is credited as inspired by **Molmo2**'s shared-context masking ([Molmo](../entities/molmo.md)). The implication is that at inference the model conditions on past *observations* only, not its own past actions.
- **Online RL with CISPO (§3.3).** This is CISPO, the clipped importance-sampling policy optimization from MiniMax-M1, with group-relative advantages. The reward is **−max(2, geodesic distance to goal)**, so it stops improving within 2 m (success is 3 m), which pushes the policy to emit STOP. It uses **35k hard tasks** (episodes the SFT policy fails on). A simulator, vLLM rollouts and trainer run as an async loop, and batches are **scene-contiguous**, which "empirically outperforms random shuffling."

### Results (§4, Table 1: val-unseen)

| | R2R-CE SR | R2R-CE SPL | RxR-CE SR | RxR-CE SPL |
|---|---|---|---|---|
| **Robostral Navigate** (mono) | **77.4** | **74.2** | 75.1 | **68.7** |
| Qwen-RobotNav-4B (mono) | 66.9 | 60.5 | 71.3 | 61.5 |
| Qwen-RobotNav-8B (mono) | 65.7 | 59.6 | 73.4 | 63.5 |
| Qwen-RobotNav-8B (depth / multi-cam) | 72.1 | 66.6 | **76.5** | 65.7 |
| OmniNav (depth / multi-cam) | 69.5 | 66.1 | 73.6 | 62.0 |
| StreamVLN (mono) | 56.9 | 51.9 | 52.9 | 46.0 |
| [GA-VLN](ga-vln-paper.md) (not in table; mono + depth-projected BEV) | 61.0 | — | — | — |

- **RL contribution:** R2R-CE unseen 73.40 → 77.43 (+4.03) and seen 75.96 → 79.43; RxR-CE 71.2 → 75.1 (+3.9).
- On RxR-CE it **trails** the depth-assisted Qwen-RobotNav-8B on SR (75.1 vs 76.5) and leads on SPL and NE. "New state of the art" on RxR-CE therefore holds for monocular methods and for SPL, not for SR overall.

> [!warning] Checkpoint chosen on the reported split
> §4: "Peak validation performance during the run reached 80.46% on seen and **77.43% on unseen**." The unseen number reported is *exactly* the peak of the run, so the checkpoint appears to have been selected on val-unseen, the split being reported. No R2R-CE **test** (leaderboard) number is given, and there are no seeds or intervals. The baselines' numbers are copied from their papers. Treat gaps under ~3 points as noise, per the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline. The 10.5-point lead over monocular methods survives that; the 5.3-point lead over depth methods is borderline.

> [!warning] Contradiction: blog vs paper numbers
> The Mistral launch blog (page metadata 2026-07-08, two weeks before arXiv v1) says **76.6%** unseen, "+9.7" over the best monocular method, "+4.5" over the best depth or multi-camera method, and "+3.2%" from RL. All three arXiv versions (v1 07-22, v2 07-24, v3 07-31) say **77.4%, +10.5, +5.3, +4.03**. A diff of v1–v3 shows the revisions changed **only the contributor list**. The higher paper number is likely a later checkpoint from the same run, consistent with the "peak validation" note above. Cite the paper, and note that the blog's figures are the earlier ones. The blog also adds: "We are not seeing any plateauing."

## Entities mentioned

- [Mistral AI](../entities/mistral-ai.md) — publisher; first robotics / embodied model (new entity).
- [Galaxea R1](../entities/galaxea-r1.md), [Hiwonder](../entities/hiwonder.md) (JetAuto) — the two deployment platforms.
- [Habitat](../entities/habitat.md) — simulator, VLN-CE benchmarks, and the evaluation-time pathfinder.
- [Molmo](../entities/molmo.md) — Molmo2's attention masking inspired the prefix-tree recipe.
- [Qwen](../entities/qwen.md) — Qwen-RobotNav and Qwen-VLA are the strongest Table 1 baselines.
- Also cited but without wiki pages: NaVid, Uni-NaVid, NaVILA, StreamVLN, InternVLA-N1, NavFoM, ABot-N0, OmniNav; MiniMax-M1 (CISPO).

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md) — the MLLM-VLN lineage. Its image-space pointing is the VLM-scale version of GNM's *normalized waypoints* trick for cross-embodiment.
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) — a pointing-specialized VLM repurposed as a policy; "once the model understands where things are, it learns how to move."
- [Cross-embodiment transfer](../concepts/learning/cross-embodiment.md) — image-space actions plus randomized body and camera geometry.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — a slow VLM, a fast diffusion head and a 100 Hz tracker in series; the frame-latency compensation is the fast-slow pattern.
- [Diffusion Policy](../entities/diffusion-policy.md) — the 121M DiT action head.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — sim-only training; real-world transfer shown by video only.

## Open questions

- **How much of the lead is the waypoint + oracle-planner setting?** One run with the paper's own DiT + tracker inside Habitat (instead of the pathfinder) would separate the policy's quality from the evaluation protocol.
- **Where do 350k scenes come from**, and are the MP3D val-unseen scenes excluded from training? Without this, "unseen" is unverifiable.
- **Which 8B base?** "In-house, dense, grounding-specialized" suggests a Pixtral / Ministral-family VLM, but the paper never names it. Weights: none; product access through sales.
- **Legged and aerial robots**: the abstract claims them and the paper shows neither. Real-world success rates on the two ground robots aren't given either.
- **Does prefix-tree packing transfer to manipulation VLAs?** Their episodes are long, observation-dominated, and have the same O(T²) redundancy. It is a general trick for any history-conditioned policy, not a navigation one.

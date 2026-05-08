---
title: Why JEPA research skips the simulator stack
type: synthesis
created: 2026-05-07
updated: 2026-05-07
tags: [jepa, world-model, simulators, v-jepa, leworldmodel, jepa-wms, dino-wm, vla-jepa, droid, sim-to-real, evaluation]
---

# Why JEPA research skips the simulator stack

> [!warning] Major revision 2026-05-07
> The first draft of this synthesis claimed JEPA research **structurally skips** heavy agentic-robotics simulators. After ingesting five additional JEPA / JEPA-adjacent papers, that generalization is too strong. The same FAIR group that produced [[v-jepa-2|V-JEPA 2]] (no sim) released [[jepa-wms|JEPA-WMs]] (Dec 2025) which trains and evaluates on [[robocasa|RoboCasa]] + Metaworld + DROID + real Franka. The pattern was real for first-generation JEPA-for-robotics work but is **fragmenting** as of 2026-Q1, not solidifying. This rewrite reflects that.

## The original observation, narrowed

When this wiki contained only [[v-jepa-2-paper|V-JEPA 2]] and [[leworldmodel-paper|LeWorldModel]], a clean pattern was visible:

| Paper | Pretraining | Action-conditioning | Evaluation |
|---|---|---|---|
| [[v-jepa-2-paper\|V-JEPA 2]] (FAIR + Mila, Jun 2025) | 1M+ hr **internet video** | 62 hr **real Droid teleop** | **Zero-shot real Franka**, two new labs |
| [[leworldmodel-paper\|LeWorldModel]] (Mila + NYU + Samsung SAIL + Brown, Mar 2026) | None — end-to-end from pixels | Action-conditioned at training | **PushT, cube, two-rooms, reacher** — _not real-robot data_ |

Across both papers, [[nvidia-isaac-lab|Isaac Lab]], [[mujoco-playground|MuJoCo Playground]], [[maniskill|ManiSkill]], [[robocasa|RoboCasa]], and [[genesis|Genesis]] were absent. That is still true _for those two papers_. The observation that prompted this synthesis is not wrong — it just doesn't generalize.

## What broke the generalization

**[[jepa-wms-paper|Terver, Yang, Ponce, Bardes, LeCun — "What drives success in physical planning with JEPA-WMs?"]]** (arxiv 2512.24497, Dec 30 2025 / revised Jan 8 2026, code at `facebookresearch/jepa-wms`).

This is the load-bearing source. Same FAIR group as V-JEPA 2 (Bardes and LeCun are senior on both). The repo README enumerates the actual environments:

- **42 Metaworld tasks** (100 episodes each)
- **Push-T**, **PointMaze**, **Wall**
- **[[robocasa|RoboCasa]] kitchen manipulation**
- **DROID** dataset (raw stereo HD, 8.7 TB; or non-stereo HD, 5.6 TB)
- **Franka** robot trajectories
- Optional video pretraining: Kinetics-400, Kinetics-710, SSv2, HowTo100M

Within ~6 months of the V-JEPA 2 release, the same lab published a JEPA paper using a heavy household-manipulation sim ([[robocasa|RoboCasa]]) alongside real-robot data. The "watch for the first JEPA paper that explicitly trains in heavy sim" caveat from the original draft was already wrong by the time it was filed.

## The full picture across seven JEPA / JEPA-adjacent papers

| Paper | Pretraining substrate | Sim weight class | Sim platforms | Real robot |
|---|---|---|---|---|
| [[v-jepa-2-paper\|V-JEPA 2]] (Jun 2025) | Internet video | **None** | — | Real Franka, zero-shot |
| [[v-jepa-2-1-paper\|V-JEPA 2.1]] (Mar 2026) | Internet video | **None** | — | Real-robot grasp + nav |
| [[leworldmodel-paper\|LeWorldModel]] (Mar 2026) | End-to-end pixels | **Lightweight** | PushT, cube, two-rooms, reacher | None |
| [[dino-wm-paper\|DINO-WM]] (Nov 2024) | Frozen DINOv2 features | **Lightweight** | PushT, Wall, PointMaze, Rope, Granular, Reacher (likely MuJoCo 2.1) | None |
| [[dino-world-paper\|DINO-world]] (Jul 2025) | Frozen DINOv2 features | **Light video sim** | "driving and indoor scenes to simulated environments" (generic) | None |
| [[vla-jepa-paper\|VLA-JEPA]] (Feb 2026) | JEPA-as-auxiliary | **Mid-weight** | LIBERO, LIBERO-Plus, **SimplerEnv** | Yes, unspecified |
| [[jepa-wms-paper\|JEPA-WMs]] (Dec 2025) | Frozen DINOv2 + co-trained predictor | **Heavy** | **[[robocasa\|RoboCasa]]**, Metaworld, Push-T, Wall, PointMaze | DROID + Franka |

Read across the rows, the JEPA literature fragments across **four sim weight classes**: no sim, lightweight benches, mid-weight (LIBERO / SimplerEnv), heavy (RoboCasa). The "JEPA skips sim" framing collapsed all four into one. They are different design choices for different research questions.

## Why each weight class makes sense for its paper

- **No sim (V-JEPA 2 / V-JEPA 2.1):** thesis is "internet-scale video gives you a good encoder; transfer to real robot is the test." Sim doesn't contribute to that thesis and would muddy the headline. Eval is real Franka because that's what proves the claim.
- **Lightweight (LeWM, DINO-WM, DINO-world):** these are training-method papers. LeWM proves an anti-collapse regularizer with 15M params on a single GPU; DINO-WM proves zero-shot planning works on frozen DINOv2 features. Heavy sim would be overkill — classic 2D/3D benches are the cheapest correct testbed.
- **Mid-weight (VLA-JEPA):** an auxiliary objective inside a VLA needs to be evaluated where VLAs already get evaluated. LIBERO + SimplerEnv is the right benchmark suite for that comparison.
- **Heavy (JEPA-WMs):** "what drives success in physical planning" is a benchmarking question that needs realistic environments. RoboCasa kitchen manipulation is the right choice; Metaworld + Push-T + PointMaze cover the lightweight comparisons; DROID + real Franka close the loop.

So sim choice tracks paper question, not a JEPA-vs-sim ideology.

## What the JEPA papers *say* about sim choice

**Almost nothing explicit.** I searched the V-JEPA 2 paper, the V-JEPA 2.1 abstract, the LeWM paper, the DINO-WM project page, the DINO-world abstract, the VLA-JEPA abstract, and the JEPA-WMs abstract for: simulator, simulation, Isaac, MuJoCo, Habitat, RoboCasa, ManiSkill, Genesis, sim-to-real, synthetic. The hits are sparse:

- V-JEPA 2 frames its data choice positively: _"self-supervised learning enables us to make use of internet-scale video — depicting sequences of states without direct observations of the actions."_ This is the only direct statement of rationale across all sources.
- JEPA-WMs abstract describes its setup as _"experiments using both simulated environments and real-world robotic data"_ — generic, no defense of why this combination.
- No paper or Meta blog argues that sim is the wrong tool for JEPA training.

**Implication:** the "JEPA skips sim" pattern in V-JEPA 2 / LeWM is not an ideological stance — it's an artifact of paper-specific tradeoffs. Once the question becomes "what drives planning success" (Terver et al.), heavy sim is back on the table.

## The four "whys" from the original draft, reassessed

The first draft hypothesized four reasons JEPA research avoids sim. With more sources, those should be labeled as the **wiki author's inference**, not citations:

| Hypothesis | Status after revision |
|---|---|
| (a) Observation-scale data thesis: internet video > sim | **Supported by primary text.** V-JEPA 2 says this directly. |
| (b) Latent-space sim-to-real bypass | **Inferred, not stated.** Plausible reading of behavior. No JEPA paper argues this. |
| (c) DROID replacing sim's data-multiplier role | **Implicit.** V-JEPA 2 emphasizes "62 hr" as a feature but never frames it as substituting for sim. |
| (d) Real-robot zero-shot as test of truth | **Behavior-supported, not stated.** V-JEPA 2 + V-JEPA 2.1 both headline real-Franka. But [[jepa-wms-paper\|Terver et al.]] also evaluates on real Franka **and** RoboCasa, so sim and real are complementary in the same paper, not opposed. |

Hypothesis (a) is the only one with direct primary-source backing. The others are reasonable readings of paper behavior but are author inference, not paper rationale.

## Two corrections to flag

1. **The `stable-worldmodel` env zoo is broader than the [[leworldmodel-howto|LeWM howto]] exposed.** The canonical repo (`rbalestr-lab/stable-worldmodel`) ships DM Control Suite (12 envs), Atari (ALE 100+), Push-T, Two-Room, OGBench cube + scene, Craftax, **and Gymnasium-Robotics Fetch (reach/push/slide/pick-and-place) under `swm/FetchReach-v3` etc.** It does not yet integrate Isaac Lab / MuJoCo Playground / ManiSkill / RoboCasa / Habitat. So the LeWM infrastructure is "many lightweight benches plus Fetch," not strictly "four 2D/3D toys." The howto page understates this and should be updated when the env zoo is verified end-to-end.

2. **DINO-WM and JEPA-WMs share a research lineage.** Basile Terver is on [[dino-world-paper|DINO-world]] (Jul 2025) and lead-authors [[jepa-wms-paper|JEPA-WMs]] (Dec 2025). DINO-world's "DINOv2 features → world model" approach evolves into JEPA-WMs' RoboCasa + DROID + Franka full-stack evaluation in five months. The DINO-world → JEPA-WMs path is one continuous research line at FAIR moving from generic-video to robot-specific.

## Updated implications for tool builders and researchers

- **Sim-stack vendors:** JEPA is back as a customer, but selectively. RoboCasa is in (via JEPA-WMs); Isaac Lab and MuJoCo Playground specifically are still not. If sim weight class tracks paper question, expect future "physical planning" JEPA papers to keep using heavy sim while "self-supervised representation" JEPA papers continue without.
- **Choosing a world-model paradigm:** the JEPA value proposition is no longer "skip the sim-stack tax" categorically — it's "predict in latent space, choose your sim weight class to fit your evaluation question."
- **Watching the field:** the next milestone to track is the first JEPA paper that **explicitly trains inside Isaac Lab or MuJoCo Playground** (the two heaviest, OpenUSD-native stacks). RoboCasa happened in Dec 2025; those two would close the gap.
- **Bread-crumb signal:** when a research-line lead author shows up across consecutive papers (Terver: DINO-world → JEPA-WMs), expect the next paper from that line to extend the trajectory — likely toward fuller integration with the sim stack of choice.

## What the wiki still cannot adjudicate

> [!note] Sample size is now seven
> Up from two. Still not exhaustive — JEPA work in adjacent labs (e.g. industrial vendors using JEPA internally) and post-March-2026 papers are not in this wiki. The pattern of fragmentation may consolidate or fragment further.

> [!note] Affiliations and code links are partial
> Several abstracts (JEPA-WMs, V-JEPA 2.1, VLA-JEPA, DINO-world) do not list affiliations on the abstract page — author overlap and code namespaces let me infer FAIR / Mila / USTC, but full institutional lists need the paper bodies.

> [!note] DINO-world's specific simulators are not enumerated in the abstract
> The abstract describes "driving and indoor scenes to simulated environments" generically. The paper body may name specific suites; I have not extracted them.

> [!note] Affiliations of DINO-WM, V-JEPA 2.1, JEPA-WMs lab list need paper-body verification
> Author overlap strongly implies FAIR + NYU + Mila but is not directly stated on the arxiv abstract pages I fetched.

## Sources used in this synthesis

- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[leworldmodel-howto|LeWorldModel — train and run howto]]
- [[dino-wm-paper|DINO-WM Paper]]
- [[dino-world-paper|DINO-world Paper]]
- [[vla-jepa-paper|VLA-JEPA Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
- [[v-jepa-2|V-JEPA 2 entity]] / [[jepa-wms|JEPA-WMs entity]] / [[dino-wm|DINO-WM entity]] / [[dino-world|DINO-world entity]] / [[vla-jepa|VLA-JEPA entity]]
- [[jepa|JEPA concept page]]
- [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]] — companion synthesis on the paradigm split.
- [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths to generalist policies]] — companion synthesis showing where the rest of the field sits.

## Related

- [[jepa|Joint-Embedding Predictive Architecture]] — the architecture family.
- [[world-model-simulators|World-model simulators]] — broader paradigm context.
- [[openusd-support-across-simulators|OpenUSD support across simulators]] — companion catalog.

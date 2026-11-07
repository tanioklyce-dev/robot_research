---
title: "RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies"
type: source
url: https://arxiv.org/abs/2607.04434
local_path: raw/robodojo_2607.04434v3.pdf
sha256: e07c215f30169dde6a792c34b046b1f54818d09331763988732dcf9ead89a9d4
author: "Tianxing Chen, Yue Chen, Zixuan Li, Junyuan Tang, Kailun Su, Haoran Lu, Weijie Wan, et al. (~43 authors); corresponding: Mingyu Ding, Wenbo Ding, Ping Luo, Masayoshi Tomizuka"
published: 2026-07-05
venue: "arXiv preprint (cs.RO), v3 2026-07-08; MMLab@HKU, UC Berkeley, Tsinghua, PKU, Stanford, MIT and others"
format: "46-page PDF (v3)"
tags: [robodojo, benchmark, evaluation, sim-and-real, isaac-sim, isaac-lab, bimanual, arx-x5, piper, xpolicylab, leaderboard, vla, world-action-model, pi0.5, molmoact2, gr00t, x-vla, human-baseline, reproducibility, hidden-test-set]
ingested: 2026-11-07
---

# RoboDojo (Chen et al., 2026)

## Summary

The primary paper behind [RoboDojo](../entities/robodojo.md), from the team that built [RoboTwin](../entities/robotwin.md). It has four parts:
- **42 Isaac Sim tasks**, all on a dual **ARX X5**, grouped into five capability dimensions: Generalization 12, Memory 6, Precision 8, Long-Horizon 8 and Open 8.
- **18 real-world tasks**, 6 each on ARX X5, [Piper](../entities/agilex-piper.md) and Piper X.
- A standardized real-robot rig, **RoboDojo-RealEval**, with remote cloud access.
- **XPolicyLab**, a shared policy interface with 30 integrated policies.

The headline is how badly current policies do. On the frozen 2026-07-03 simulation leaderboard the **best of 30 policies averages 8.80% success** (Hy-Embodied-0.5-VLA), against **76.03% for expert human teleoperators**. [π0.5](../entities/pi-zero-5.md) scores 6.91%, [GR00T N1.7](../entities/nvidia-groot.md) 1.31%, [MolmoAct2](../entities/molmoact2.md) 0.38% and [OpenVLA-OFT](../entities/openvla-oft.md) 0.02%. **Open** tasks, which recombine trained skills toward unseen goals, are near zero for everyone (best 1.67%). In the real world π0.5 leads with **12.8%** over 180 trials, and human teleop scores **100%**.

The paper says explicitly that the sim and real suites are **not paired**: *"The real-world benchmark is not intended to measure direct sim-to-real transfer on matched tasks."* On the policies evaluated in both, it reports only that rankings are *"partially but not completely"* aligned.

## Key claims

### Simulation benchmark (§3.1)
- **Platform.** Dual ARX X5 with the arm bases 0.6 m apart, built on Isaac Sim / Isaac Lab via MagicSim's manager architecture. Tasks are YAML-specified.
- **Assets.** Rigid, articulated and deformable, with rigid assets partly reconstructed using Meshy AI.
- **Data collection.** Automated trajectory synthesis composes annotated skills (grasp, place, handover, insert, open, close, stack, push_up) on **cuRobo v2**. Tasks too hard to synthesize use VR teleop.
- **Task dimensions:**
  - **Generalization (12):** unseen backgrounds, lighting, objects and **up to 25 clutter objects** (RoboTwin 2.0 had at most 10). Training demonstrations are collected *without* domain randomization. A train-only "DLC" set of 100 randomized pick-and-place trajectories adds visual diversity without leaking task solutions.
  - **Memory (6):** non-Markovian tasks, e.g. remember the category of an object that disappears on a conveyor, or reproduce an ordering another arm demonstrated. Inspired by RMBench.
  - **Precision (8):** insertion, screws, keys, xylophone, and similar.
  - **Long-Horizon (8):** for example, sorting objects that needs bimanual handover.
  - **Open (8):** goals not in training whose component skills are. **Not represented in the training data at all.**
- **Training data.** 35 directories, 3,500 trajectories (100 per task), 1,859,602 frames, **20.66 h** at 25 Hz. Head RGB-D plus two wrist RGB-D cameras at 640×480.
- **Evaluation.**
  - 50 episodes per task, 2,100 in total. Generalization tasks split them 25 standard / 25 random.
  - Both success and a partial-progress **score** are reported.
  - The overall figure is the **mean over the five dimensions**, not over tasks, so larger dimensions don't dominate.
  - The horizon is 1.2× the 90th-percentile demonstration length (1.5× for short synthesized tasks).
- **Seeds.** Most policies have 3 training seeds × 50 trials per task, i.e. 150 trials per task.

### Real-world benchmark (§3.2, §4.2, App. E, G)
- **Embodiments.** Three collaborative bimanual platforms, with **no one-to-one task pairing with simulation**.
- **Data.** Homogeneous leader–follower teleop (the leader arm matches the follower), 100 demonstrations per task from 4 operators: 1,800 trajectories, 17.91 h at 25 Hz.
- **The RealEval rig:**
  - A 1.5 × 1.5 m frame with a 1.2 m table, 3D-printed fixtures, and fixed robot and camera poses (Orbbec Gemini 335L head, 305 wrist ×2).
  - 24-hour LED lighting.
  - A touchscreen web UI.
  - **Layout replay**: an overlay of the target layout image on the live stream, used to restore initial conditions.
- **Protocol.** 10 trials per task. Each trial is scored **double-blind by three evaluators**, partial sub-steps included, and the scores are averaged. Videos are released, and there is an appeal mechanism. End-effector policies go through the Pink IK solver.
- **Cost.** π0.5 on all 18 tasks took **202 min (3.4 h) for 180 trials**, about 11.2 min per task.

### Integrity and governance (§3.3, App. A.2)
- **Who runs it.** The leaderboard is run by **AI MMLab Club, a non-profit**, with academic co-governance and *"no commercial company… involved in the official evaluation process."*
- **Requirements for the verified leaderboard:**
  - Official remote evaluation, so scores are not self-reported.
  - **3 seeds** in simulation (training seeds, or evaluation seeds on one checkpoint).
  - All three real embodiments.
  - **Hidden verification layouts**: a significant gap from the public layouts invalidates a submission.
  - Release of the checkpoint, code and config through XPolicyLab.
  - Release of the videos.
- **Closed-source track.** Results that are not released go on a separate, unverified track.

### Simulation leaderboard (Table 1, frozen 2026-07-03; score / success, average of the 5 dimensions)

| Policy | Avg | Note |
|---|---|---|
| Hy-Embodied-0.5-VLA | 13.07 / **8.80%** | best Long-Horizon (14.92%) and Memory (12.11%) |
| Spatial Forcing (π0.5 base) | 12.38 / 8.04% | best Generalization (9.33%) |
| π0.5 | 11.41 / 6.91% | best Open (**1.67%**) |
| X-VLA | 10.13 / 6.52% | best Precision (12.00%) |
| X-WAM (Wan2.2-5B) | 7.69 / 3.83% | best world-action model |
| GR00T N1.7 | 2.85 / 1.31% | |
| MolmoAct2 | 1.02 / 0.38% | |
| OpenVLA-OFT | 0.21 / 0.02% | last |
| **Human expert (VR teleop)** | 80.42 / **76.03%** | Precision is the human's weakest (64%) |

- **Policy families tested.** 30 policies in all, including π0, SmolVLA, ACT, RDT-1B, H-RDT, GO-1, InternVLA-A1, LingBot-VLA, GalaxeaVLA G0, StarVLA-α, Xiaomi-Robotics-0, and the WAMs: Fast-WAM, AHA-WAM, GigaWorld-Policy.
- **Fine-tuning recipes differ widely by policy** (App. K). LingBot-VLA trained 15K steps, LDA-1B 300K, π0.5 60K at batch 256, GR00T N1.7 100K at batch 640, MolmoAct2 100K at batch 128. Each followed its own default rather than a matched compute budget.

### Findings (§6.1, simulation)
1. **There is a large gap to balanced generalist manipulation**, and strengths are fragmented: each dimension has a different leader.
2. **Scene randomization collapses everyone.** Standard → random score drops by **64.6–100%** for every policy except OpenVLA-OFT, whose scores are near zero in both. Hy-Embodied falls 21.98 → 1.57 (−92.9%). Spatial Forcing keeps the most (−67.2% vs π0.5's −72.2%), credited to 3D spatial-representation alignment.
3. **Long-horizon: stages without completion.** Score exceeds success, so policies finish sub-stages but not whole tasks. Skill composition is not reliable.
4. **Precision fails through open-loop behaviour.** In `insert_key`, policies *"continue executing the subsequent insertion motion"* after a failed handover. Action jitter appears in both end-effector and joint-space policies.
5. **Memory.** Explicit memory (EventVLA's KEM) helps less than strong pretraining with history (Hy-Embodied). The WAM X-WAM gets a higher partial-progress score but lower success. The paper's reading is that video prediction encodes continuity but does not *retrieve* sparse evidence once it has gone from view.
6. **Open-semantic manipulation is essentially unsolved** (≤ 1.67%).

### Real-world leaderboard (Table 2; 1 seed per embodiment, 10 trials per task)
- **π0.5 leads at 22.9 / 12.8%.** Then InternVLA-A1 12.0 / 7.2%, GalaxeaVLA 9.0 / 4.4%, Xiaomi-Robotics-0, X-VLA 7.6 / 3.3%, GR00T N1.7 5.9 / 1.7%, π0, StarVLA-α, Spirit v1.5, and DM0 at 0.0 / 0.0%.
- **Piper X is the hardest embodiment.** π0.5 gets 3.3% there; most policies get 0%.
- **Human teleop: 100% on every task.**
- **Sim and real rankings are "only partially aligned."** InternVLA-A1 and GalaxeaVLA rank higher in the real world than in sim. DM0 produces erratic motion that needs safety intervention.

### Efficiency and stability (§6.3–6.4)
- **Heterogeneous parallelism.** Different tasks, assets and object counts run in one simulator process, with strict physics replication disabled.
- **Throughput.** On 8× RTX 4090, 10 environments per GPU, 640×480:
  - **77.4 interactions/s** heterogeneous vs 40.0 homogeneous (1.94×).
  - **64.0/s with π0.5 inference** served from an A800 (1.63×).
  - RoboTwin 2.0 manages 44.6/s at 320×240.
- **Sim stability across GPUs.** Three RTX 4090s, layout 0 only, 3 policies × 3 seeds. The largest standard deviation is **1.1 pp** in success and **≤ 0.5 pp** overall.
- **Real stability.** Three repeated rounds. The overall standard deviation is **≤ 1.3 pp**, but individual tasks reach **23.1 pp** (π0.5 `store_in_safe`).

### Future extensions
Dexterous hands, humanoid whole-body, tactile and mobile manipulation, each on multiple embodiments.

## Entities mentioned
- [RoboDojo](../entities/robodojo.md) · [RoboTwin](../entities/robotwin.md) · [AgileX Piper](../entities/agilex-piper.md)
- **Policies:** [π0.5](../entities/pi-zero-5.md) · [π0](../entities/pi-zero.md) · [X-VLA](../entities/x-vla.md) · [GR00T](../entities/nvidia-groot.md) · [MolmoAct2](../entities/molmoact2.md) · [OpenVLA-OFT](../entities/openvla-oft.md) · [SmolVLA](../entities/smolvla.md) · [ACT](../entities/act.md) · [RDT](../entities/rdt.md) · [AGIBOT](../entities/agibot.md) (GO-1)
- **Benchmarks compared:** [LIBERO](../entities/libero.md) · [RoboCasa](../entities/robocasa.md) · [SimplerEnv](../entities/simplerenv.md) · [BEHAVIOR](../entities/behavior-benchmark.md) · [RoboLab](../entities/nvidia-robolab.md) · [RoboArena](../entities/roboarena.md)
- [Isaac Sim](../entities/nvidia-isaac-sim.md) · [Isaac Lab](../entities/nvidia-isaac-lab.md) · [cuRobo](../entities/curobo.md)
- No pages: Hy-Embodied-0.5-VLA (Tencent), Spatial Forcing, X-WAM, Fast-WAM, AHA-WAM, GigaWorld-Policy, Xiaomi-Robotics-0, InternVLA-A1, GalaxeaVLA G0, LingBot-VLA, StarVLA-α, EventVLA, DM0, ARX X5, Piper X, XPolicyLab, MagicSim, RMBench

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): hidden-layout verification, a human-teleop ceiling, double-blind real scoring, and a measured stability spread.
- [VLA models](../concepts/learning/vla-models.md): how the 2026 VLA cohort does on a hard, broad suite.
- [World-action model](../concepts/world-models/world-action-model.md): four Wan2.2-based WAMs, all mid-table or below.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): unpaired sim and real suites, so no transfer claim is made.

## Open questions
- **Is it the policies or the data?** 100 demonstrations per task across 34 tasks (~20 h) is small for multi-task fine-tuning of 3–5B models, and recipes vary widely. Low absolute numbers may partly reflect under-training on a new embodiment. No data-scaling curve is given.
- **Is the human baseline a ceiling or a floor?** The experts have 1,000+ h (sim) and 1,500+ h (real) of teleop and *built the datasets*. 100% real-world success is the upper bound of the demonstrators themselves, not of the task.
- **How wide are the real-world error bars?** 10 trials per task, one training seed. The overall spread across rounds is small (≤ 1.3 pp), but a binomial interval on 10 trials is about ±30 pp per task, so per-task real rankings are mostly noise.
- **How stable is the sim leaderboard really?** The stability test varies GPUs only on layout 0. The training-seed spread is reported per policy in the leaderboard, but the cross-layout spread is not.
- **MolmoAct2 at 0.38%** contrasts sharply with its strong LIBERO numbers on its own page. A cross-benchmark memorization signal, or a fine-tuning problem with ARX X5 joint actions? The paper doesn't diagnose individual policies.
- **Leaderboard drift.** The website leaderboard has moved since 2026-07-03, and the 2026-09 `get_obs` and RGB-channel fixes reportedly left results *"essentially unchanged"* ([branch READMEs](robodojo-isaaclabarena-branch.md)).

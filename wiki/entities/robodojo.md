---
title: RoboDojo
type: entity
subtype: benchmark
created: 2026-11-07
updated: 2026-11-07
sources: 5
tags: [robodojo, benchmark, evaluation, isaac-sim, isaac-lab-arena, sim-and-real, bimanual, arx-x5, piper, xpolicylab, robotwin, mit]
---

# RoboDojo

**RoboDojo** is a unified **sim-and-real benchmark** for generalist manipulation policies, from the team led by Tianxing Chen that also maintains [RoboTwin](robotwin.md). It was released 2026-07-06 under the MIT license ([paper, arXiv 2607.04434](../sources/robodojo-paper.md); [branch READMEs](../sources/robodojo-isaaclabarena-branch.md)). The leaderboard is run by the non-profit AI MMLab Club, with academic co-governance and no commercial participation.

## Design (per the main-branch README)
- **Coverage.** **42 simulation tasks**, all on a dual ARX X5 in Isaac Sim. **18 real-world tasks**, 6 each on ARX X5, [Piper](agilex-piper.md) and Piper X. Only the ARX X5 appears in both.
- **Five capability dimensions.** Generalization, Memory, Precision, Long-Horizon and Open. The README calls them *"designed to probe different skills rather than simple object or layout reskins"* and the tasks *"intentionally hard."*
- **Simulation.** Heterogeneous parallel simulation runs different tasks and scenes concurrently. Rigid, articulated and deformable assets share one configuration-driven scene.
- **Eval only.** Policies plug in through **[XPolicyLab](xpolicylab.md)** (arXiv 2608.09892), *"40+ policies behind one interface"* for sim and real alike (the paper, frozen 2026-07-03, integrates 30). There is also a RoboDojo-RealEval protocol and a live leaderboard.
- **Shared maintenance with RoboTwin.** The September 2026 RGB channel-ordering fix was made *"together with RoboTwin"* to keep the two consistent.

## What the paper measured (frozen 2026-07-03)

From the [paper](../sources/robodojo-paper.md):

- **Training data.** Sim: 100 demonstrations per task, 3,500 trajectories, 20.66 h. Open tasks get no training data at all. Real: 1,800 leader–follower teleop trajectories, 17.91 h.
- **Simulation.** 30 policies, mostly 3 seeds × 50 trials per task, averaged over the five dimensions.
  - **Best average:** Hy-Embodied-0.5-VLA 8.80%, then Spatial Forcing 8.04%, [π0.5](pi-zero-5.md) 6.91% and [X-VLA](x-vla.md) 6.52%.
  - **Further down:** [GR00T N1.7](nvidia-groot.md) 1.31%, [MolmoAct2](molmoact2.md) 0.38%, [OpenVLA-OFT](openvla-oft.md) 0.02%.
  - **Human VR teleop:** 76.03%.
  - **Open tasks:** ≤ 1.67% for every policy.
  - **Randomized scenes** cut scores by 64.6–100% for every policy except one near-zero outlier.
- **Real world.** 10 policies, 1 seed, 10 trials per task, double-blind 3-rater scoring. π0.5 leads at **12.8%**, human teleop scores 100%, and Piper X is the hardest embodiment.
- **Sim vs real.** The paper says the two suites are **unpaired by design**: it is *"not intended to measure direct sim-to-real transfer."* Rankings are *"only partially aligned"*; InternVLA-A1 and GalaxeaVLA do better in the real world than in sim.
- **Stability.**
  - Sim: ≤ 1.1 pp across GPUs, measured on layout 0 only.
  - Real: overall ≤ 1.3 pp across three rounds, but a single task reaches 23 pp.
- **Integrity.** Hidden verification layouts, mandatory release of the checkpoint and code for the verified board, released videos, and an appeal process.

## The board as of 2026-09-10

The leaderboard has moved a long way since the paper was frozen ([GPT-6 Astra on RoboDojo](../sources/gpt-6-astra-robodojo-paper.md), Table 1; average SR):
- **The new top of the board.** **DM0.5 19.34%**, GalaxeaVLA G0.5 14.88%, Xiaomi-Robotics-1 13.93%, OpenWAM-α 11.92% and Meituan-Robotics-0 9.53%. Hy-Embodied-0.5-VLA's 8.80% is now 7th, and π0.5 (6.91%) is 9th.
- **An LLM entry.** **[GPT-6 Astra](gpt-6-astra.md), with no robot policy and no fine-tuning, scores 22.48%**, above every public policy. It leads on Open (31.0% vs ≤ 2.1%) and Generalization, and trails on Precision, Long-Horizon and Memory. GPT-5.5 scores 0.88% on the same interface.
- **Real board.** OpenWAM-α now leads at **24.40%**, ahead of π0.5's 12.80%. Astra's real-robot campaign was **stopped for safety** after it damaged hardware.
- **Comparability.** The LLM entries received a wiki-derived task recipe, including the process-score ladder, that the policies never saw. They were run on one seed.

## The submission path (XPolicyLab, 2026-11)
- **77 policies** are now integrated, up from 30 in the paper. A PR to XPolicyLab with a checkpoint download script is the only route onto the official board ([XPolicyLab GitHub](../sources/xpolicylab-github.md)).
- **Two newer kinds of entrant:**
  - ten-plus world-action models;
  - **[GPT-6 Astra](gpt-6-astra.md)**, eval-only, calling one `move_eef` tool through RoboDojo's non-learned IK and path planner. It now ranks first ([GPT-6 Astra on RoboDojo](../sources/gpt-6-astra-robodojo-paper.md)).
- **Reading the scores.** Every RoboDojo number is measured *through* an XPolicyLab adapter, so adapter fidelity is part of what a score means.

## Isaac Lab-Arena port (2026-10-30)
- RoboDojo is the second suite from this team ported to [Isaac Lab-Arena](isaac-lab-arena.md), after RoboTwin 2.0. The port lives on the `RoboDojo-IsaacLabArena` branch.
- **Scope.** **54 tasks** (42 + 12 `_random` variants), **2,100 episodes**, on the dual ARX X5, with a [π0.5](pi-zero-5.md) adapter.
- **Pins.** A pinned 38.4 GiB asset snapshot and pinned Arena and Isaac Lab commits, on Isaac Sim 5.1.
- **Checks and multi-env.** CPU contract tests, and heterogeneous multi-environment batches with per-slot termination.
- **No results yet.** No success rates and no native-vs-Arena parity numbers have been published, only the tooling to compute them ([branch READMEs](../sources/robodojo-isaaclabarena-branch.md)).

## Why it matters for this wiki
- It is a direct check on Arena's pitch. A third-party benchmark was ported in, and it took a pinned, older Arena commit plus an offline-assets patch to do it.
- **It has a sim track and a real track, but it deliberately does not answer the sim-to-real correlation question** that [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) keeps asking. The tasks are unpaired, and only the ARX X5 is shared. What it offers instead is the partial rank agreement across the 10 policies run in both.
- **It is the hardest public scoreboard the wiki has for the 2026 VLA cohort.** Even with the September entries, the best policy is under 20%, against 76% for human teleop. That sets the level for any claim of "generalist" manipulation. (When the paper was frozen in July, every policy was in single digits; see [the board as of 2026-09-10](#the-board-as-of-2026-09-10).) They also contrast sharply with the same models' LIBERO-class numbers elsewhere in the wiki.
- The Piper embodiment ties it to the low-cost arms the wiki tracks.

## Related
- [RoboTwin](robotwin.md), the sibling benchmark from the same team.
- [XPolicyLab](xpolicylab.md), the policy adapters and server every submission goes through.
- [Isaac Lab-Arena](isaac-lab-arena.md) · [Isaac Sim](nvidia-isaac-sim.md)
- [ToyBlocks](toyblocks.md), the opposite design choice: one narrow, editable world rather than a broad fixed suite.

## Mentioned in
- [RoboDojo — RoboDojo-IsaacLabArena branch (GitHub READMEs)](../sources/robodojo-isaaclabarena-branch.md)
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md): listed as "coming soon" in Arena's ecosystem, 2026-09-14.
- [RoboDojo paper (Chen et al., 2026)](../sources/robodojo-paper.md) — the primary: task design, both leaderboards, governance, efficiency and stability.
- [XPolicyLab GitHub](../sources/xpolicylab-github.md) — the policy-side harness: 77 adapters, websocket serving, the RGB codec rule, and the PR-plus-checkpoint route onto the leaderboard.
- [GPT-6 Astra on RoboDojo](../sources/gpt-6-astra-robodojo-paper.md) — the 2026-09-10 board (DM0.5 19.34%, OpenWAM-α 24.40% real), and an LLM-as-policy entry at 22.48% that ranks first; real-robot campaign stopped for safety.

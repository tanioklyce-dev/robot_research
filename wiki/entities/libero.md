---
title: LIBERO
type: entity
subtype: benchmark
created: 2026-05-08
updated: 2026-08-27
sources: 32
tags: [libero, manipulation-benchmark, lifelong-learning, robosuite, mujoco, code-as-policy]
---

**LIBERO — "Lifelong Robot Learning Benchmark."** Procedural manipulation benchmark designed to test **lifelong / continual policy learning** across diverse manipulation tasks. Suite of task families ("Spatial," "Object," "Goal," and "100" — long-tail) commonly used as a [VLA](../concepts/learning/vla-models.md) evaluation harness in 2024–2026. Built on robosuite + MuJoCo.

## Evaluation protocol (confirmed 2026-07-27)

**50 evaluation episodes per task** — stated by [LIBERO-PRO](../sources/libero-pro-paper.md) as *"consistent with the original LIBERO protocol."* Each suite holds **10 tasks**, so:

- **500 episodes per suite**
- **2,000 for a four-suite average** (Spatial / Object / Goal / Long)

The benchmark totals **130 tasks across 4 suites** (the LIBERO paper's own count — Spatial/Object/Goal/Long at 10 each, plus LIBERO-90). Training data is **50 expert demonstrations per task** — note this is the *same number* as the evaluation episode count, and the two are easy to confuse in secondary write-ups.

This closes a standing gap: the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) had computed against 500/2,000 as **assumptions**, and they are now **confirmed**.

## Position in this wiki
Primary reference is [VLA-JEPA](../sources/vla-jepa-paper.md) (Sun et al., Feb 2026), which evaluates on **LIBERO + LIBERO-Plus + SimplerEnv + real-world manipulation**. LIBERO has effectively become the de-facto VLA-eval bench — alongside [RoboCasa](robocasa.md) for household manipulation and [Metaworld](metaworld.md) for multi-task RL.

## Why it matters
- **Standard VLA-eval suite.** Most VLA papers in 2024–2026 report LIBERO numbers; comparability across papers is the value.
- **Continual / lifelong framing.** The design tests whether policies can absorb new tasks without catastrophic forgetting — a different question than single-task or pure multi-task evaluation.

## Related
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — why the numbers below are a tier and not a ranking.
- [LIBERO-PRO](../sources/libero-pro-paper.md) — the memorization critique; the more serious of the two problems.
- [RoboArena](roboarena.md) — the real-world, pairwise-preference alternative that routes around both.
- [VLA-JEPA](vla-jepa.md) — primary JEPA-line consumer in this wiki.
- [MuJoCo](mujoco.md) — physics backend.
- [RoboCasa](robocasa.md) / [Metaworld](metaworld.md) — adjacent manipulation benchmarks.
- LIBERO-Plus — extended variant referenced by VLA-JEPA; could become its own entity if cross-cited.
- SimplerEnv — companion mid-weight sim used alongside LIBERO in VLA-JEPA.

## Reported numbers in this wiki

> [!warning] Two independent problems with every number below — read them in order
>
> **1. The benchmark may be measuring memorization.** [LIBERO-PRO](../sources/libero-pro-paper.md) (Zhou et al.) reports that models scoring **>90% on standard LIBERO collapse to 0.0%** when objects, initial states, instructions, or environments are perturbed — because *"evaluation tasks are identical to the training tasks, differing only by marginal perturbations in initial object states."* Models **keep grasping when the target object is replaced** and produce **unchanged outputs under corrupted instructions**. Tested on OpenVLA, π0, π0.5 (π0.5 most robust at 0.38, still severe). **The 2026-class models at the top of this table were not tested** — that is the open question.
>
> **2. The top of the table is a statistical tie.** Four of its members — CogVLA, VLA-Adapter, MemoryVLA, FLOWER — are only characterized on the [tie-cluster holding page](libero-tie-models.md).
>
> **2a.** Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md): at the confirmed protocol (**50 episodes/task → 500/suite, 2,000 for a four-suite average**), separating two policies at ~97% requires a gap of **>1.8 pp** (or >1.0 pp on the average). **MolmoAct2 97.2, MolmoAct2-Think 98.1, [X-VLA](x-vla.md) 98.1, [TurboVLA](turbovla.md) 97.7, CogVLA 97.4, VLA-Adapter 97.3, [VLA-JEPA](vla-jepa.md) 97.2, OpenVLA-OFT 97.1, GR00T N1.7 97.0, and π0.5 96.9 are not distinguishable from one another** (all pairwise p > 0.1 except Think-vs-base at p=0.06). Same for the VLA-0 94.7 / π0.5-KI 94.3 / π0 94.2 cluster. **The tied cluster is now ten models wide and spans 1.2 pp.**
>
> What *does* separate: MolmoAct2 vs VLA-0 (2.5 pp) and anything vs MolmoAct 86.8 (10.4 pp). Phrases below asserting a **rank** inside the 94–98 band are not supported by the sample sizes; the tier membership is.
>
> **A tie among numbers that may not measure generalization is the second-order problem.** Problem 1 is the one to act on.

- **[MolmoAct2](molmoact2.md) / MolmoAct2-Think ([MolmoAct2 paper](../sources/molmoact2-paper.md), Table 8)** — MolmoAct2 Spatial **97.8** / Object **100.0** / Goal **97.8** / Long **93.2** / avg **97.2**; **MolmoAct2-Think** Spatial **98.8** / Object **99.8** / Goal **98.5** / Long **95.4** / avg **98.1** — the **numerically highest** LIBERO average in the wiki but **statistically tied with** OpenVLA-OFT (97.1), GR00T N1.7 (97.0), π0.5 (96.9) (see the callout above), and +10.6 over the predecessor MolmoAct-7B-D (86.6). The Think variant's largest gain (+2.2) is on the hardest suite (Long), where the base leaves the most headroom. Baseline table also reports GR00T N1.7 97.0, π0.5 96.9, NORA-1.5 94.5, π0 94.2.
- **[TurboVLA](turbovla.md) ([TurboVLA paper](../sources/turbovla-paper.md), Table 1)** — Spatial **99.2** / Object **99.8** / Goal **97.4** / Long **94.2** / avg **97.7**, at **0.2 B params, 0.9 GB VRAM, 31.2 ms** on an RTX 4090 and **no embodied pretraining**. Numerically second-highest in the wiki, statistically tied with everything above 96.9. The table is also the wiki's most complete **efficiency-annotated** LIBERO comparison — 16 models with params / VRAM / latency all re-measured by the authors on one 4090. Adds otherwise-unseen entries: CogVLA 97.4, VLA-Adapter 97.3, [VLA-JEPA](vla-jepa.md) 97.2, MM-ACT 96.3, DDVLA 96.4, [UniVLA](univla.md) 95.2, [Evo-1](evo-1.md) 94.8, DreamVLA 92.6, and **[Diffusion Policy](diffusion-policy.md) 72.4 / [SmolVLA](smolvla.md) 88.8** as the low anchors.
- **[GR00T](nvidia-groot.md) 1.7 (LeRobot-trained, NVIDIA-reported)** — Spatial **95%**, Object **100%**, Goal **98%**, Long **93%**, avg **96.5%**; vs GR00T 1.5 avg 87% ([NVIDIA HF blog, 2026-07-07](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)). Per-suite fine-tuned checkpoints released (`nvidia/gr00t17-lerobot-libero_*-640`). Vendor self-comparison — no third-party baselines in the post.
- **[X-VLA](x-vla.md) ([X-VLA paper](../sources/xvla-paper.md), Tab. 2 + 13)** — Spatial **98.2** / Object **98.6** / Goal **97.8** / Long **97.6** / avg **98.1** at **0.9 B params**, joining the top of the tied cluster from below on model size rather than above. Two things here are more informative than the average. **Long is 97.6** — the suite where everyone else leaves headroom (MolmoAct2-Think 95.4, OpenVLA-OFT 94.5, π0 85.2) and where X-VLA's margin is 2.2–12.4 pp, comfortably past the [audit](../syntheses/platforms/vla-success-rate-audit.md) threshold. And under **LoRA at 9 M tunable params** it still scores 95.4/96.6/96.0/84.2 — within ~1 pp of fully-finetuned π0 at 300× fewer tuned parameters. Baselines it reports: OpenVLA-OFT 97.1, MemoryVLA 96.7, DD-VLA 96.3, FLOWER 95.7, UniVLA 95.4, π0 94.1, GR00T-N1 93.9, SmolVLA 88.8, OpenVLA 76.5.
- **[OpenVLA-OFT](openvla-oft.md) ([OFT paper](../sources/openvla-oft-paper.md), Table I)** — Spatial **97.6** / Object **98.4** / Goal **97.9** / Long **94.5** / avg **97.1** — claimed **SOTA**, lifting base OpenVLA from 76.5 *on the same weights* via parallel decoding + action chunking + continuous L1 head, at **26× throughput**. **The 76.5 → 97.1 recipe effect (+20.6 pp) is the robust result here** and easily clears the [audit](../syntheses/platforms/vla-success-rate-audit.md) bar; its *position* relative to MolmoAct2/GR00T/π0.5 does not.
- **π0.5-KI ([Knowledge Insulation](../concepts/learning/knowledge-insulation.md) paper, "from generalist")** — Spatial **98.0**, Object **97.8**, Goal **95.6**, Long(10) **85.8**, LIBERO-**90 96.0** — claims **SOTA on LIBERO-90 and LIBERO-Spatial** ([KI paper](../sources/knowledge-insulation-paper.md), Table 1); this is the primary source for the "π0.5-KI 94.3" figure the VLA-0 table relays. Also reports OpenVLA-OFT (97.6/98.4/97.9/94.5), π0 (96.8/98.8/95.8/85.2), π0-FAST (96.4/96.8/88.6/60.2).
- **[VLA-0](vla-0.md) (NVIDIA, no action pretraining)** — Spatial **97.0**, Object **97.8**, Goal **96.2**, Long **87.6**, avg **94.7** — **best rank (1.0) among no-pretraining models** and rank 2.8 overall, above π0 (94.2), [π0.5-KI](../concepts/learning/knowledge-insulation.md) (94.3), GR00T-N1 (93.9), [MolmoAct](molmoact.md) (86.8), [π0-FAST](fast-action-tokenization.md) (86.0), OpenVLA (76.5); only [OpenVLA-OFT](openvla-oft.md)-pretrained (97.1) is higher. A rare **cross-method LIBERO table with consistent baselines** ([VLA-0 paper](../sources/vla-0-paper.md), Table I).

## Mentioned in

> [!note] Curated list — **32** source pages link here; the ones below are those that shaped this page.
- [LIBERO-PRO paper](../sources/libero-pro-paper.md) — perturbation-based critique; confirms the 50-episodes-per-task protocol.
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md) — LIBERO as the robotics entry in a policy-facing survey of world-model benchmarks.
- [What Makes Video World Model Latents Action-Relevant](../sources/action-relevant-latents-paper.md) — uses a **task-OOD split** (104 train / **26 tasks held out entirely**) for frozen-feature action probing. A stricter protocol than the standard suites, and a template worth reusing: the held-out tasks never touch world-model training.
- [WorldArena 2.0 paper](../sources/worldarena-2-paper.md) — LIBERO used as one of three platforms (with [RoboTwin 2.0](robotwin.md) and a real ALOHA) for **cross-platform world-model evaluation**; functional rankings correlate between the two simulators and collapse against the real robot.
- [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — LIBERO kitchen scenes repurposed as a direct-LLM-control benchmark; 0-5.5% end-to-end.
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md)
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **natively integrated** as one of two simulation benchmarks (alongside [Metaworld](metaworld.md)). Confirms the four task families: SPATIAL, OBJECT, GOAL, plus continuing-task LIBERO-90 and long-horizon LIBERO-LONG.
- [NVIDIA Isaac Teleop and GR00T 1.7 in LeRobot (HF blog)](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) — GR00T 1.7 vs 1.5 LIBERO table; describes LIBERO as "130 language-annotated tabletop manipulation tasks."
- [VLA-0 paper](../sources/vla-0-paper.md) — primary simulation benchmark; the wiki's most complete cross-method LIBERO comparison (11 models, with/without action pretraining).
- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — MolmoAct2 97.2 / MolmoAct2-Think 98.1, **tied with [X-VLA](x-vla.md) 98.1 at the numerical top and [statistically inseparable](../syntheses/platforms/vla-success-rate-audit.md) from the other eight models in the cluster.**
- [Knowledge Insulation paper](../sources/knowledge-insulation-paper.md) — LIBERO-90 + LIBERO-Spatial SOTA claim; π0.5-KI vs π0 / π0-FAST / OpenVLA-OFT (Table 1).
- [OpenVLA-OFT paper](../sources/openvla-oft-paper.md) — the 97.1% SOTA + 26× throughput result; the primary source for OFT's LIBERO numbers.
- [X-VLA paper](../sources/xvla-paper.md) — 98.1 avg at 0.9 B; 97.6 on Long, the one suite where the tie breaks.
- [FAST paper](../sources/fast-paper.md) — evaluates π0-FAST across the four LIBERO suites.
- [CaP-X paper](../sources/cap-x-paper.md) — integrates **130 LIBERO-PRO tasks** into CaP-Gym; the first code-as-policy comparison against VLAs on the perturbation suites.
- [ASPIRE paper](../sources/aspire-paper.md) — LIBERO-Pro and LIBERO-90 → LIBERO-Pro Long zero-shot transfer; independently reproduces the VLA collapse.
- [TurboVLA paper](../sources/turbovla-paper.md) — 97.7 avg from a **0.2 B LLM-free policy**; the wiki's most complete efficiency-annotated LIBERO table. Its no-language ablation (avg → 70.8, **Goal 97.4 → 11.6**) is the clearest measurement of how much of LIBERO is solvable from visual priors alone: on Object, almost all of it (99.4 without any instruction).

## LIBERO-PRO with a non-VLA comparison point (added 2026-08-03)

The [LIBERO-PRO](../sources/libero-pro-paper.md) collapse finding was previously a statement about VLAs with nothing to contrast against. Two code-as-policy papers now run the same perturbation suites, and the contrast is the informative part.

**[CaP-X](../sources/cap-x-paper.md)** (30 LIBERO-PRO tasks), success under position (Pos) and instruction (Task) perturbation:

| Method | object Pos/Task | goal Pos/Task | spatial Pos/Task |
|---|---|---|---|
| [OpenVLA](openvla.md) | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 |
| [π0](pi-zero.md) | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 |
| π0.5 | 0.17 / 0.01 | **0.38** / 0.00 | **0.20** / 0.01 |
| **CaP-Agent0** (training-free) | **0.22 / 0.18** | 0.26 / **0.17** | 0.12 / **0.14** |

**[ASPIRE](../sources/aspire-paper.md)** (10 tasks × 50 held-out seeds per suite/perturbation) then adds **+77 / +41.5 / +42.5 points** over the strongest baseline on object / goal / spatial.

> [!note] What the contrast isolates
> **VLAs are asymmetric; the coding agent is not.** π0.5 retains some position robustness but goes to ~0.00 under paraphrase, because it is trained on a fixed instruction distribution. A [code-as-policy](../concepts/agents/code-as-policy.md) agent reads the instruction with a general language model, so paraphrase costs it nothing — its Pos and Task columns are roughly equal.
>
> This does **not** mean code-as-policy is better at manipulation. On *position* perturbation π0.5 still beats CaP-Agent0 on two of three suites, and on standard (unperturbed) LIBERO the VLAs post 94–98% while nothing in the code-as-policy line comes close. The claim it supports is narrower and more useful: **the LIBERO-PRO collapse is specifically a language-generalization failure, not a general brittleness of learned policies** — and it is fixable by changing where language is interpreted.

ASPIRE also independently reproduces the LIBERO-PRO result (OpenVLA and π0 at 0), which was previously single-sourced.

## As an LLM-control benchmark (not just a VLA benchmark)

Anthropic's [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) adapts LIBERO kitchen scenes to a different question: not *how well does a trained policy do*, but *how well does a general LLM do driving a [Franka Panda](franka-panda.md) directly*. End-to-end pick-and-place success across eleven frontier models spans **0 to 5.5%** — against the 94–98% that trained VLAs post on LIBERO. Decomposed by subgoal, reaching and grasping improve markedly across model generations while **placing** stays the bottleneck. LIBERO-40 (40 tasks x 5 seeds, 200 trials) is also the substrate for the [MolmoAct](molmoact.md)-supervision experiments.

That gap — **~5% for a general LLM vs ~97% for a purpose-trained VLA on the same benchmark** — is the clearest single quantification in this wiki of what action-pretraining buys.

## Reach beyond robotics

LIBERO is now cited **in policy documents** as the robotics anchor of the world-model evaluation landscape — the [HAI world-model brief](../sources/hai-world-model-spatial-intelligence-brief.md) lists it alongside VBench / VideoPhy / PhyGenBench / WorldScore / WorldModelBench / WorldArena as the benchmark that "tests how well robots complete simulated manipulation tasks," then concludes that none of them gives policymakers an adequate basis for safety-critical deployment. Given [LIBERO-PRO](../sources/libero-pro-paper.md)'s >90% → **0.0%** result, that conclusion is if anything understated. See [world-model evaluation](../concepts/world-models/world-model-evaluation.md).

## Open questions / TBD
- Original LIBERO paper (Liu et al., NeurIPS 2023) still not ingested directly — would let us cite design rationale (why the four task families, what "lifelong" means concretely). **The protocol question it was wanted for is now answered** via [LIBERO-PRO](../sources/libero-pro-paper.md); what remains is rationale, not numbers.
- Authors per the LeRobot ICLR 2026 citation: **Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone** (NeurIPS 2023, 36:44776–44791).

---
title: LIBERO
type: entity
subtype: benchmark
created: 2026-05-08
updated: 2026-07-17
sources: 6
tags: [libero, manipulation-benchmark, lifelong-learning, robosuite, mujoco]
---

**LIBERO — "Lifelong Robot Learning Benchmark."** Procedural manipulation benchmark designed to test **lifelong / continual policy learning** across diverse manipulation tasks. Suite of task families ("Spatial," "Object," "Goal," and "100" — long-tail) commonly used as a [VLA](../concepts/learning/vla-models.md) evaluation harness in 2024–2026. Built on robosuite + MuJoCo.

## Position in this wiki
Primary reference is [VLA-JEPA](../sources/vla-jepa-paper.md) (Sun et al., Feb 2026), which evaluates on **LIBERO + LIBERO-Plus + SimplerEnv + real-world manipulation**. LIBERO has effectively become the de-facto VLA-eval bench — alongside [RoboCasa](robocasa.md) for household manipulation and [Metaworld](metaworld.md) for multi-task RL.

## Why it matters
- **Standard VLA-eval suite.** Most VLA papers in 2024–2026 report LIBERO numbers; comparability across papers is the value.
- **Continual / lifelong framing.** The design tests whether policies can absorb new tasks without catastrophic forgetting — a different question than single-task or pure multi-task evaluation.

## Related
- [VLA-JEPA](vla-jepa.md) — primary JEPA-line consumer in this wiki.
- [MuJoCo](mujoco.md) — physics backend.
- [RoboCasa](robocasa.md) / [Metaworld](metaworld.md) — adjacent manipulation benchmarks.
- LIBERO-Plus — extended variant referenced by VLA-JEPA; could become its own entity if cross-cited.
- SimplerEnv — companion mid-weight sim used alongside LIBERO in VLA-JEPA.

## Reported numbers in this wiki

- **[GR00T](nvidia-groot.md) 1.7 (LeRobot-trained, NVIDIA-reported)** — Spatial **95%**, Object **100%**, Goal **98%**, Long **93%**, avg **96.5%**; vs GR00T 1.5 avg 87% ([NVIDIA HF blog, 2026-07-07](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)). Per-suite fine-tuned checkpoints released (`nvidia/gr00t17-lerobot-libero_*-640`). Vendor self-comparison — no third-party baselines in the post.
- **[OpenVLA-OFT](openvla-oft.md) ([OFT paper](../sources/openvla-oft-paper.md), Table I)** — Spatial **97.6** / Object **98.4** / Goal **97.9** / Long **94.5** / avg **97.1** — new **SOTA**, lifting base OpenVLA from 76.5 *on the same weights* via parallel decoding + action chunking + continuous L1 head, at **26× throughput**. The top LIBERO score in the wiki.
- **π0.5-KI ([Knowledge Insulation](../concepts/learning/knowledge-insulation.md) paper, "from generalist")** — Spatial **98.0**, Object **97.8**, Goal **95.6**, Long(10) **85.8**, LIBERO-**90 96.0** — claims **SOTA on LIBERO-90 and LIBERO-Spatial** ([KI paper](../sources/knowledge-insulation-paper.md), Table 1); this is the primary source for the "π0.5-KI 94.3" figure the VLA-0 table relays. Also reports OpenVLA-OFT (97.6/98.4/97.9/94.5), π0 (96.8/98.8/95.8/85.2), π0-FAST (96.4/96.8/88.6/60.2).
- **[VLA-0](vla-0.md) (NVIDIA, no action pretraining)** — Spatial **97.0**, Object **97.8**, Goal **96.2**, Long **87.6**, avg **94.7** — **best rank (1.0) among no-pretraining models** and rank 2.8 overall, above π0 (94.2), [π0.5-KI](../concepts/learning/knowledge-insulation.md) (94.3), GR00T-N1 (93.9), [MolmoAct](molmoact.md) (86.8), [π0-FAST](fast-action-tokenization.md) (86.0), OpenVLA (76.5); only [OpenVLA-OFT](openvla-oft.md)-pretrained (97.1) is higher. A rare **cross-method LIBERO table with consistent baselines** ([VLA-0 paper](../sources/vla-0-paper.md), Table I).

## Mentioned in
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md)
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **natively integrated** as one of two simulation benchmarks (alongside [Metaworld](metaworld.md)). Confirms the four task families: SPATIAL, OBJECT, GOAL, plus continuing-task LIBERO-90 and long-horizon LIBERO-LONG.
- [NVIDIA Isaac Teleop and GR00T 1.7 in LeRobot (HF blog)](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) — GR00T 1.7 vs 1.5 LIBERO table; describes LIBERO as "130 language-annotated tabletop manipulation tasks."
- [VLA-0 paper](../sources/vla-0-paper.md) — primary simulation benchmark; the wiki's most complete cross-method LIBERO comparison (11 models, with/without action pretraining).
- [Knowledge Insulation paper](../sources/knowledge-insulation-paper.md) — LIBERO-90 + LIBERO-Spatial SOTA claim; π0.5-KI vs π0 / π0-FAST / OpenVLA-OFT (Table 1).
- [OpenVLA-OFT paper](../sources/openvla-oft-paper.md) — the 97.1% SOTA + 26× throughput result; the primary source for OFT's LIBERO numbers.

## Open questions / TBD
- Original LIBERO paper (Liu et al., NeurIPS 2023) not yet ingested as a source — would let us cite design rationale (why the four task families, what "lifelong" means concretely).
- Authors per the LeRobot ICLR 2026 citation: **Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone** (NeurIPS 2023, 36:44776–44791).

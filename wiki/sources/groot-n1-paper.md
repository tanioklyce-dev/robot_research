---
title: GR00T N1 — An Open Foundation Model for Generalist Humanoid Robots (paper)
type: source
url: https://arxiv.org/abs/2503.14734
author: NVIDIA (corporate); research leads Jim Fan & Yuke Zhu; ~50 contributors incl. Scott Reed, Ruijie Zheng, Guanzhi Wang, Johan Bjorck, Joel Jang, Zhenjia Xu, Soroush Nasiriany, Zhenyu Jiang, Seonghyeon Ye, Ajay Mandlekar, Jan Kautz, Dieter Fox
published: 2025-03 (arXiv 2503.14734v2, 2025-03-27; no peer-review venue)
ingested: 2026-07-04
local_path: raw/GR00T_N1_2503.14734v2.pdf
sha256: 76e38cf679637b816b16edf7170340883dd09175bf334aeeaed49392777731b9
format: pdf (36 pp.)
tags: [groot, vla, nvidia, gear, humanoid, flow-matching, data-pyramid, neural-trajectories, fourier-gr1, foundation-model]
---

## Summary

The primary paper behind [NVIDIA GR00T](../entities/nvidia-groot.md) N1 — an open [VLA](../concepts/learning/vla-models.md) foundation model for humanoid robots with a Kahneman-inspired dual-system architecture: a pre-trained VLM (System 2, ~10 Hz) interprets vision + language, and a Diffusion Transformer trained with action [flow matching](../concepts/learning/flow-matching.md) (System 1, 120 Hz) generates closed-loop motor actions; both are trained jointly end-to-end. Its answer to robot learning's "data islands" problem is the **data pyramid**: web data and human video at the base, synthetic data (physics-sim trajectories + video-model-generated "neural trajectories") in the middle, real teleoperation at the peak — unified by annotating action-less video with VQ-VAE latent actions (LAPA-style) and IDM pseudo-actions. GR00T-N1-2B outperforms BC-Transformer and [Diffusion Policy](../entities/diffusion-policy.md) across three simulation benchmarks and achieves **76.8% average success on real [Fourier GR-1](../entities/fourier-gr-1.md) tabletop tasks vs 46.4% for Diffusion Policy**, with strong data efficiency (10%-data GR00T is within 3.8 points of full-data DP). Checkpoint, training data, and sim benchmarks are released openly.

## Key claims

### Architecture (§2.1)
- **System 2** = NVIDIA **[Eagle](../entities/eagle-vlm.md)-2 VLM** (finetuned from a SmolLM2 LLM + SigLIP-2 image encoder), 10 Hz on an L40 GPU. **System 1** = Diffusion Transformer (DiT, adaLN timestep conditioning) trained with **action flow matching**, 120 Hz action generation.
- **GR00T-N1-2B: 2.2B total parameters (1.34B in the VLM)**; sampling a 16-action chunk takes **63.9 ms** on an L40 in bf16.
- Images at 224×224 + pixel shuffle → 64 tokens/frame; vision-language features taken from a **middle LLM layer (layer 12)** rather than the final layer — faster *and* higher policy success.
- DiT alternates cross-attention (to VLM tokens) with self-attention (over noised action + state embeddings). **Embodiment-specific MLP state/action encoders + decoder** handle variable dimensions across embodiments. Explicit contrast with [π0](../entities/pi-zero.md)'s mixture-of-experts bridging: simple cross-attention decouples VLM and action-module architecture choices (§5).
- Action chunk H=16; flow-matching loss with Beta(1.5, 1) timestep prior (following π0); only **K=4 Euler denoising steps** at inference across all embodiments.
- Auxiliary **object-detection loss** (App. F): predict the normalized 2D center of the target object (auto-annotated with OWL-v2); total loss = flow matching + detection.

### Data pyramid (§2.2, §3; Table 7)
- **Full pre-training corpus: 592.9M frames = 8,375.7 hours** — real robot 3,288.8 h (AgiBot-Alpha 1,979.4 h; [DROID](../entities/droid.md) 428.3 h; RT-1 338.4 h; Language Table 195.7 h; Bridge-v2 111.1 h; more via [Open X-Embodiment](../entities/open-x-embodiment.md)), human video 2,517.0 h (Ego4D 2,144.7 h; HoloAssist 169.6 h; Ego-Exo4D 123 h; EPIC-KITCHENS 31.7 h; others), simulation 1,742.6 h, neural-generated 827.3 h.
- **Real teleop peak:** in-house GR-1 pre-training set = **88.4 h (6.4M frames, 20 Hz)** via VIVE Ultimate Tracker + Xsens Metagloves (also Apple Vision Pro, Leap Motion), IK-retargeted.
- **Neural trajectories:** WAN2.1-I2V-14B fine-tuned via [LoRA](../concepts/learning/low-rank-adaptation.md) on the 88 h of teleop (3,000 language-annotated samples), generating **827 h ≈ 300k trajectories — a ~10× multiplication of the real data** — with counterfactual prompts; a multimodal LLM does prompt generation, filtering-as-judge, and re-captioning. Cost: ~**105k L40 GPU-hours** (3,600 L40s, ~1.5 days).
- **Simulation:** [DexMimicGen](../entities/mimicgen.md) multiplies a few dozen human demos into **780k trajectories ≈ 6,500 h (nine person-months of demonstration) in 11 hours**; pre-training sim set = 540k demos under the [RoboCasa](../entities/robocasa.md) framework (GR-1 embodiment, mink-based whole-body IK).
- **Action-less video unification:** VQ-VAE **latent actions** (continuous pre-quantized embedding as flow-matching target, treated as a distinct "LAPA" embodiment) + trained **inverse dynamics model (IDM)** pseudo-actions.
- **Training compute (§2.3):** H100 cluster (NVIDIA OSMO + Ray, up to 1024 GPUs); **~50k H100 GPU-hours** for pretraining; batch 16,384 × 200k steps; vision encoder unfrozen, LLM frozen. Single-A6000 finetuning is feasible (adapters + DiT only).

### Results (§4)
- **Simulation, 100 demos/task (Table 2):** average success GR00T-N1-2B **45.0%** vs Diffusion Policy 33.4% vs BC-Transformer 26.4%. Per-benchmark: RoboCasa 32.1 / 25.6 / 26.3; DexMimicGen suite 66.5 / 56.1 / 53.9; GR-1 Tabletop **50.0 / 32.7 / 16.1**.
- **Demo scaling (Table 4):** GR00T vs DP at 30/100/300 demos — RoboCasa 17.4/32.1/49.6 vs 14.7/25.6/43.2; DexMG 29.6/58.5/74.2 vs 23.7/46.9/68.4; GR-1 43.2/50.0/49.3 vs 21.3/32.7/40.4.
- **Real Fourier GR-1 (Tables 3, 5):** full-data average **76.8% vs DP 46.4%** (+30.4); 10%-data: **42.6% vs 10.2%** — 10%-data GR00T is only 3.8 points below full-data DP. Category breakdown (full data): Pick-and-Place 82.0% (seen 92.0 / unseen 72.0), Articulated 70.9%, Industrial 70.0%, Multi-Agent Coordination 82.5%.
- **Pre-trained checkpoint, no post-training (§4.4):** bimanual handover 76.6%; novel object → unseen container 73.3%.
- **Neural-trajectory ablations (Fig. 9):** co-training with neural trajectories gains +4.2/+8.8/+6.8 points at 30/100/300 demos (RoboCasa) and +5.8 points across 8 real GR-1 tasks (10%-data regime). **LAPA latent actions win in the lowest-data regime (30 demos); IDM pseudo-actions win at 100–300** as IDM alignment improves with data.
- **Catastrophic forgetting observed (§4.5):** the pretrained checkpoint spontaneously performs an unseen left-to-right handover for an out-of-reach pick; the post-trained checkpoint *loses* this ability because post-training data was right-hand-only.

### Systems contributions (App. E)
- Extends the [LeRobot](../entities/lerobot.md) dataset format with `modality.json`, fine-grained state/action field semantics, multiple annotation types, and explicit rotation representations; standardized cross-embodiment action space (6D rotation EEF state, axis-angle EEF actions, min-max normalization).

## Entities mentioned

- [NVIDIA GR00T](../entities/nvidia-groot.md) — this is its primary source. [NVIDIA GEAR](../entities/nvidia-gear.md) ([Jim Fan](../entities/jim-fan.md), [Yuke Zhu](../entities/yuke-zhu.md), [Joel Jang](../entities/joel-jang.md)).
- [Fourier GR-1](../entities/fourier-gr-1.md) — primary real-robot platform (also the DreamDojo eval platform).
- [Franka Panda](../entities/franka-panda.md) — RoboCasa benchmark embodiment; bimanual Panda variants in DexMimicGen.
- [RoboCasa](../entities/robocasa.md), [MimicGen](../entities/mimicgen.md) (DexMimicGen), [Open X-Embodiment](../entities/open-x-embodiment.md), [DROID](../entities/droid.md), [AgiBot](../entities/agibot.md) (AgiBot-Alpha dataset), [LeRobot](../entities/lerobot.md) (dataset format), [Hugging Face](../entities/hugging-face.md).
- [π0](../entities/pi-zero.md) — architectural contrast; [Diffusion Policy](../entities/diffusion-policy.md) + BC-Transformer (RoboMimic) — baselines; [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — cited alongside WAN2.1 for neural-trajectory generation; [Octo](../entities/octo.md), [OpenVLA](../entities/openvla.md)-line VLAs — related work.
- 1X (acknowledged for humanoid hardware support).
- [SigLIP 2](../entities/siglip-2.md) — the vision half of the Eagle-2 VLM (SmolLM2 + SigLIP-2).

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — GR00T N1 is the wiki's canonical open dual-system VLA; System 1/System 2 pattern per [Curriculum Module 9](../syntheses/curriculum/curriculum-09-vla.md).
- [Flow matching](../concepts/learning/flow-matching.md) — action head; K=4 Euler steps at inference.
- [Imitation learning](../concepts/learning/imitation-learning.md) — pre-train + post-train BC at foundation scale.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — the data pyramid is the qualitative precursor to [EgoScale](egoscale-paper.md)'s quantitative scaling law.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — DexMimicGen sim data + neural trajectories as the middle of the pyramid.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — neural trajectories are video-models-as-data-generators, the same pattern DreamGen/[DreamDojo](dreamdojo-paper.md) later scale up.

## Open questions

- Restricted to **short-horizon tabletop manipulation**; long-horizon loco-manipulation named as future work requiring hardware + architecture + data advances.
- Video-generated synthetic data still struggles to produce diverse counterfactuals **while adhering to physics** (authors' own caveat).
- Post-training can destroy pre-trained skills (handover regression) — the pretraining-retention question is raised but not resolved.
- How the N1 recipe evolved into N1.5/N1.6/N1.7 (Cosmos-Reason2 backbone, EgoScale corpus) — the wiki tracks the later versions via [EgoScale](egoscale-paper.md) and [Top 10 Physical AI Models 2026](top-10-physical-ai-models-2026.md), but no N1.5/N1.6 primary paper is on file.

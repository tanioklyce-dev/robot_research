---
title: NVIDIA Isaac Teleop and GR00T 1.7 Open VLA Model Available in LeRobot (HF blog)
type: source
url: https://huggingface.co/blog/nvidia/nvidia-isaac-teleop-and-gr00t17-in-lerobot
author: Lior Ben Horin, Kartik S, Johnny Nuñez Cano, Edith Llontop, Leung, Andrew C Wrenn, Shane Reetz (NVIDIA)
published: 2026-07-07
ingested: 2026-07-07
format: vendor blog post (Hugging Face)
tags: [groot, gr00t-n1.7, lerobot, isaac-teleop, vla, nvidia, libero, so-101, fine-tuning, teleoperation]
---

## Summary

NVIDIA-authored Hugging Face blog announcing two things: (1) **[GR00T](../entities/nvidia-groot.md) 1.7 is natively integrated into [LeRobot](../entities/lerobot.md)** (`--policy.type=groot`, base model `nvidia/GR00T-N1.7-3B`) — "the latest open, commercially viable VLA foundation model for general-purpose humanoid robots," with **GR00T N1.5 explicitly no longer supported**; and (2) **[Isaac Teleop](../entities/nvidia-isaac-teleop.md)**, a new teleoperation framework (pip package `isaacteleop`, ~1.3.131, with CloudXR + retargeters) for collecting demonstrations on real or sim robots via **SO-101 leader arm or VR/XR headset**, in LeRobot-compatible formats. The post walks the full loop on an [SO-101](../entities/so-arm101.md): install (uv-based) → XR-controller teleop → record 50 episodes → fine-tune (20k steps, batch 64, relative actions excluding gripper, bf16) → `lerobot-rollout` deployment with optional RTC (real-time-chunking) inference. Headline numbers: **LeRobot GR00T 1.7 averages 96.5% on LIBERO vs 87% for GR00T 1.5**, with per-suite fine-tuned checkpoints published.

## Key claims

- **GR00T 1.7 in LeRobot** — "integrates natively into LeRobot, requiring no infrastructure changes"; LeRobot and the open-source [Isaac-GR00T](isaac-gr00t-github.md) path use **identical `nvidia/GR00T-N1.7` weights**, so benchmarked performance carries across development and deployment stacks.
- **N1.5 deprecated** — GR00T 1.7 "offers improved performance over GR00T N1.5, which is no longer supported."
- **Post-training requires LeRobot Dataset v3.0** format (the [GR00T line previously consumed "a flavor of" LeRobot v2](isaac-gr00t-github.md) — this is a version-bump signal for the whole ecosystem).
- **LIBERO results** (130-task tabletop suite, [LIBERO](../entities/libero.md), NeurIPS 2023), LeRobot-trained:

  | Suite | GR00T 1.5 | GR00T 1.7 |
  |---|---|---|
  | LIBERO-Spatial | 82% | **95%** |
  | LIBERO-Object | 99% | **100%** |
  | LIBERO-Goal | — | **98%** |
  | LIBERO-Long | 82% | **93%** |
  | **Average** | **87%** | **96.5%** |

  Fine-tuned checkpoints released per suite: `nvidia/gr00t17-lerobot-libero_{spatial,object,goal,10}-640`.
- **Isaac Teleop** — two collection modes: SO-101 **leader arm** or **VR headset** (`--teleop.type=xr_controller`); ships as `isaacteleop[cloudxr,retargeters-lite]`; targets "high-quality demonstrations, real and sim, in formats compatible with downstream training pipelines."
- **Recommended fine-tune recipe** (SO-101, from the training command): `chunk_size=16`, `n_action_steps=16`, **`use_relative_actions=true` excluding the gripper**, bf16, batch 64, 20k steps, seed 42, image transforms on, `embodiment_tag=new_embodiment`; multi-GPU via `accelerate launch`. Tested on an **RTX 6000 Pro**; an [NVIDIA Brev](../entities/nvidia-brev.md) LaunchPad is offered for GPU instances.
- **Deployment** via the new-style `lerobot-rollout` CLI with an **RTC (real-time chunking) inference block** (`--inference.type=rtc`, execution horizon 10 — disabled in the example) and `n_action_steps=8` at rollout vs 16 at training.
- **[DGX Spark](../entities/dgx-spark.md) support** — CUDA 13 users pin `torch==2.11.0+cu130` / `torchvision==0.26.0+cu13` from the cu130 wheel index (ARM64/GB10 path).

> [!note] Vendor benchmark caveat
> The LIBERO table is NVIDIA-reported, on NVIDIA-trained LeRobot checkpoints, comparing only against its own previous version — no π0/SmolVLA/third-party baselines in the post. Useful as a version-over-version delta and for the released checkpoints; not an independent leaderboard.

## Why it matters in this wiki

- **The GR00T ↔ LeRobot convergence is now official product surface.** The wiki has tracked GR00T consuming LeRobot data formats ([GR00T N1 paper](groot-n1-paper.md) extended `LeRobotDataset`; [Isaac-GR00T repo](isaac-gr00t-github.md) consumes LeRobot v2) and community GR00T-on-LeRobot use (the [Seeed hackathon champions](seeed-embodied-ai-hackathon-2025-recap.md) ran N1.5 on SO-ARM101/XLeRobot). This post makes it first-party: NVIDIA publishing GR00T as a LeRobot `policy.type` with a supported SO-101 recipe.
- **N1.7 graduates from Early Access** — the [GR00T entity](../entities/nvidia-groot.md)'s version table had N1.7 as "EA / current"; this is the general-availability signal plus the **first published N1.7 benchmark numbers** (the N1.6/N1.7 pages had claimed improvements without numbers).
- **First-party affordable-arm targeting**: the reference robot is the **$100-class [SO-101](../entities/so-arm101.md)**, not a humanoid — NVIDIA meeting the LeRobot hobbyist tier where it lives, consistent with the hackathon-signal trajectory.
- **Isaac Teleop enters a crowded teleop field** the wiki tracks (leader arms in the LeRobot workflow, [ALOHA](../entities/aloha.md)-style rigs, [UMI](umi-paper.md) handheld grippers) with an XR/VR-first, sim+real story tied to CloudXR.

## Entities mentioned

- [NVIDIA GR00T](../entities/nvidia-groot.md) — N1.7 GA in LeRobot; N1.5 deprecated; LIBERO numbers.
- [NVIDIA Isaac Teleop](../entities/nvidia-isaac-teleop.md) — new entity; XR/leader-arm teleop framework.
- [LeRobot](../entities/lerobot.md) — `groot` policy type, Dataset v3.0, `lerobot-rollout` + RTC.
- [LIBERO](../entities/libero.md) — benchmark; per-suite checkpoints released.
- [SO-ARM101](../entities/so-arm101.md) — reference platform for the whole walkthrough.
- [DGX Spark](../entities/dgx-spark.md) — CUDA-13 torch pin path.
- [NVIDIA Brev](../entities/nvidia-brev.md) — LaunchPad for training instances.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — open VLA fine-tune/deploy loop on hobbyist hardware.
- [Imitation learning](../concepts/learning/imitation-learning.md) — teleop demonstration collection feeding VLA post-training.

## Open questions / TBD

- **What changed N1.7 EA → this release?** The post gives no architecture delta vs the [Isaac-GR00T repo](isaac-gr00t-github.md)'s N1.7 EA description (Cosmos-Reason2-2B backbone, EgoScale pretrain) — presumably the same weights, now GA'd through LeRobot. Watch for a GR00T 1.7 research page.
- **LeRobot Dataset v3.0** — the wiki has no page on what changed v2 → v3; worth capturing when LeRobot documents it.
- **RTC (real-time chunking) inference** — new LeRobot inference mode surfaced here (disabled in the example); relates to the async-inference stack in the [LeRobot ICLR paper](lerobot-iclr-2026-paper.md). Not yet documented in the wiki.
- **Isaac Teleop scope** — retargeters, CloudXR dependency, supported headsets, and whether it works against Isaac Sim embodiments beyond SO-101 are not detailed in the post; the Isaac Teleop docs would deepen the [entity](../entities/nvidia-isaac-teleop.md).
- LIBERO-Goal has no GR00T 1.5 number in the table (marked —) — unclear if untested or unreported.

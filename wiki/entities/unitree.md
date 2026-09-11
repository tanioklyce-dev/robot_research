---
title: Unitree Robotics
type: entity
subtype: company
created: 2026-09-11
updated: 2026-09-11
sources: 3
tags: [unitree, china, humanoid, quadruped, hardware, foundation-model, unifolm]
---

**Unitree Robotics** (Hangzhou Yushu Technology Co., Ltd., Hangzhou) — the Chinese legged-robot maker whose low price points set the floor for academic humanoid and quadruped research, and since 2025 also a publisher of robot foundation models.

## Hardware (the platforms the wiki tracks)

- [Unitree A1](unitree-a1.md) — 12 kg quadruped; the workhorse of learned-locomotion research (RMA and its lineage).
- [Unitree Go1](unitree-go1.md) — 2021 quadruped ($2.7k Air / $3.5k Pro / Edu); the cross-embodiment test body of the Berkeley navigation line (ViNT, MBRA, OmniVLA).
- [Unitree Go2](unitree-go2.md) — current quadruped tier (~$1.6k Air to ~$17k EDU); the robot in Anthropic's Project Fetch.
- [Unitree H1](unitree-h1.md) — full-size research humanoid (~$90k).
- [Unitree Z1](unitree-z1.md) — 6-DoF force-controlled arm (2022); the single/dual-arm platform in [WMA-0](../sources/unifolm-wma-0-project-page.md)'s demos and datasets.
- [Unitree G1](unitree-g1.md) — ~$16k base / ~$30–45k EDU Plus; the default humanoid for whole-body-control papers (SONIC, ASAP, BumbleBee, LocoFormer) and for GR00T's `UNITREE_G1_SONIC` embodiment.

The pattern across those pages: Unitree hardware appears in this wiki far more often as *someone else's* research platform than as the subject of Unitree's own work.

## Models — the UnifoLM line

[UnifoLM](unifolm.md): WMA-0 video world model (Sep 2025) → VLA-Base (Jan 2026) → **UnifoLM-WLA-1.0** (Sep 2026), a 6B humanoid policy whose released pieces so far are two 4.4B embodied-reasoning VLMs on Qwen3-VL-4B and a 32-task G1 dataset ([project page](../sources/unifolm-wla-1-project-page.md)). Weights are **CC BY-NC-SA 4.0** — research-only.

The strategic read: Unitree is moving from selling the body to shipping the brain for it — the same vertical move as [Figure](figure.md) with Helix and [AGIBOT](agibot.md) with Genie, but from the cheapest hardware base of the three, and with the model gated non-commercially.

## Data

Unitree publishes its own G1 / Z1 teleop datasets on Hugging Face (LeRobot format, CC BY-NC-SA) and co-authored [HIW-500](hiw-500.md) with [BitRobot](bitrobot.md) — 500+ h of G1 whole-body teleop in real homes, **CC BY 4.0** ([page](../sources/bitrobot-hiw-500-dataset-page.md)).

## Mentioned in

- [UnifoLM-WLA-1.0 project page](../sources/unifolm-wla-1-project-page.md) — first source about Unitree's own models.

> [!note] Curated list
> Unitree hardware is cited across ~20 source pages via the per-robot entity pages above; those are listed there, not here.
- [UnifoLM-WMA-0 project page](../sources/unifolm-wma-0-project-page.md) — the 2025 world-model release.
- [HIW-500 dataset page](../sources/bitrobot-hiw-500-dataset-page.md) — co-author of the dataset.

---
title: "Grievous (alexkoven/Grievous) — cheap, human-like, fully-autonomous testbed"
type: source
url: https://github.com/alexkoven/Grievous
author: Alex Koven
published: 2026 (active development; ingested at early-stage repo state)
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
tags: [grievous, mobile-aloha, xlerobot, lerobot, raspberry-pi-5, downstream, testbed, low-cost, wip]
---

## Summary

**Grievous** — an early-stage, in-development project to build a "cheap, human-like, fully-autonomous testbed" by **Alex Koven**. The repo README is one-paragraph short: design is based on **[Mobile ALOHA](../entities/aloha.md) + [XLeRobot](../entities/xlerobot.md)**, software is built on top of **[LeRobot](../entities/lerobot.md)**. The two-process runtime architecture is **RPi5 host (`grievous_host` module) + remote PC**. This is the first downstream-of-Mobile-ALOHA project ingested in this wiki, landing the same day as the Mobile ALOHA paper ingest itself.

## Key claims

- **Design lineage**: "based on Mobile ALOHA and XLeRobot." Both already filed in the wiki as [aloha.md](../entities/aloha.md) and [xlerobot.md](../entities/xlerobot.md).
- **Software lineage**: "built on top of LeRobot." Confirmed by the module path `lerobot.robots.grievous.grievous_host` — Grievous registers itself as a LeRobot-managed robot.
- **Compute split**: **RPi5 on robot + remote PC for inference**. Same control-vs-AI split documented across [Stretch 4 (NUC + Jetson Orin NX)](../entities/stretch.md), [XLeRobot (Pi 4/5 relay + PC inference)](../entities/xlerobot.md), and [PX4 (Pixhawk FMU + Jetson companion)](../entities/px4-autopilot.md).

### Install + run recipe (verbatim from README)

```bash
# Environment
conda create -y -n grievous python=3.10
conda activate grievous
conda install ffmpeg -c conda-forge

# Code
git clone git@github.com:alexkoven/Grievous.git
cd ./Grievous
pip install -e .

# Run — on the RPi5
python -m lerobot.robots.grievous.grievous_host

# Run — on the remote PC
./test_record.sh
```

## What's NOT yet on the repo

- No paper, blog, or design doc — the README is the only documentation.
- No specs (DOF, sensors, payload, cost) — the "based on Mobile ALOHA + XLeRobot" framing is the only design pointer.
- No published policies or trained checkpoints.
- No demo video beyond the `media/short_demo_920.gif` referenced in the README.
- License not stated in the README excerpt.

## Entities mentioned

- [Grievous](../entities/grievous.md) — the testbed project (new entity).
- [Mobile ALOHA](../entities/aloha.md) — design ancestor.
- [XLeRobot](../entities/xlerobot.md) — design ancestor.
- [LeRobot](../entities/lerobot.md) — software substrate.

## Concepts touched

- Compute split: CPU/Pi on robot + GPU/PC for inference; same pattern as [Jetson Thor / DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md), [Stretch 4](../entities/stretch.md), [PX4 + companion computer](../entities/px4-autopilot.md), [XLeRobot](../entities/xlerobot.md).

## Open questions

- **Hardware BOM** — not published. Mobile ALOHA used ViperX 300 arms (~$5–6k each); XLeRobot uses SO-ARM101 (~$200 each). Whether Grievous uses SO-ARM101, ViperX, or another SKU determines budget tier and policy-transfer story.
- **Mobile base** — Mobile ALOHA used AgileX Tracer ($7k); XLeRobot uses an IKEA RÅSKOG cart on omni wheels. Which (if either) Grievous picks isn't documented.
- **"Human-like"** — README says "human-like." Mobile ALOHA is functionally bimanual + mobile, not anthropomorphic. Whether Grievous adds a humanoid form factor (head, torso, articulated waist) or stays platform-shaped is unclear.
- **License** — not in the README excerpt; check before any downstream use.
- **Author affiliation** — Alex Koven is the GitHub handle; lab / institution not in the README.
- **Maturity** — repo is explicitly WIP ("We will update this repo as we go"). Worth re-ingesting if it reaches a published milestone (paper, demo video, or hardware BOM release).

## Why this matters

Grievous is the **first downstream-of-Mobile-ALOHA project** ingested here and the **first concrete attempt to lower the Mobile-ALOHA hardware cost into the [XLeRobot](../entities/xlerobot.md) / [LeRobot](../entities/lerobot.md) tier** ($660 cart-based dual-arm at the lower bound vs $32k Mobile ALOHA at the upper). If this works, it's the path to bringing bimanual + mobile manipulation under $5k. If it stalls, it's a data point on what makes the Mobile-ALOHA hardware envelope hard to cost-reduce.

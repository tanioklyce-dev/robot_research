---
title: Grievous
type: entity
subtype: product
created: 2026-05-25
updated: 2026-07-04
sources: 3
tags: [grievous, mobile-aloha, xlerobot, lerobot, raspberry-pi-5, downstream, testbed, wip]
---

**Grievous** — early-stage open-source project by **Alex Koven** to build a "cheap, human-like, fully-autonomous testbed." Design is **based on [Mobile ALOHA](aloha.md) + [XLeRobot](xlerobot.md)**; software is built on top of **[LeRobot](lerobot.md)** (registered as `lerobot.robots.grievous.grievous_host`). Runtime architecture: **RPi5 on the robot + remote PC for inference**. Repo: https://github.com/alexkoven/Grievous ([source page](../sources/grievous-github.md)).

## What's known

- Conda Python 3.10 + ffmpeg + `pip install -e .` install path.
- Two-process runtime: `python -m lerobot.robots.grievous.grievous_host` on the Pi; `./test_record.sh` on the remote PC.
- Demo gif in `media/short_demo_920.gif` (referenced but not described in the README).
- Explicit WIP: *"We will update this repo as we go."*

## What's NOT yet known

- Hardware BOM (arms, base, sensors, cost).
- License.
- Author affiliation beyond the GitHub handle.
- Any paper, blog, or design doc.
- Whether "human-like" means humanoid form factor or just bimanual mobile.

See [Grievous source page](../sources/grievous-github.md) for the full open-questions list.

## Why it matters in this wiki

The **first downstream-of-Mobile-ALOHA project ingested here** and the first concrete attempt at **lowering Mobile ALOHA's $32k hardware envelope into the [XLeRobot](xlerobot.md)/[LeRobot](lerobot.md) ($660–$5k) tier**. If it works, it's the path to bringing bimanual + mobile manipulation under $5k. If it stalls, it's a data point on what makes the Mobile-ALOHA hardware envelope hard to cost-reduce.

## Related
- [Mobile ALOHA](aloha.md) — design ancestor.
- [XLeRobot](xlerobot.md) — design ancestor; same low-cost lineage.
- [LeRobot](lerobot.md) — software substrate.

## Mentioned in
- [Grievous GitHub source page](../sources/grievous-github.md)
- [SmolVLA Paper](../sources/smolvla-paper.md) — Grievous named among the sub-$1k hardware lines that can run SmolVLA.
- [Mobile ALOHA project page](../sources/mobile-aloha-project-page.md) — flags Grievous as a downstream-of-Mobile-ALOHA project to re-check.

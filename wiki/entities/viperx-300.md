---
title: Trossen ViperX 300
type: entity
subtype: product
created: 2026-05-25
updated: 2026-05-25
sources: 3
tags: [viperx-300, trossen, robot-arm, 6dof, aloha, mobile-aloha, hardware]
---

**Trossen Robotics ViperX 300** — 6-DOF benchtop robot arm; vendor [trossenrobotics.com/viperx-300-robot-arm](https://www.trossenrobotics.com/viperx-300-robot-arm.aspx). The **canonical bimanual-teleop SKU** for academic robotics — used as both leader and follower arms in [ALOHA](aloha.md) and [Mobile ALOHA](aloha.md) (4 arms per Mobile ALOHA setup: 2 leaders + 2 followers).

## What we know (from [Mobile ALOHA source](../sources/mobile-aloha-paper.md))

- **6 DOF.**
- **Repeatability:** 1 mm.
- **Accuracy:** 5–8 mm.
- **Per-arm payload:** 750 g (extended); two arms can combine for 1.5 kg.
- **Pull force:** 100 N at 100 cm vertical.
- Used in **leader-follower kinematic puppeteering**: operator-side leader arm broadcasts joint positions, follower arm tracks.
- 4× ViperX 300 + a $7k AgileX Tracer base + 3× webcams + a laptop = the $32k Mobile ALOHA system.

## Why it matters in this wiki

- **The wiki's first Trossen-class arm entry.** Prior arm coverage centered on the [SO-ARM101](so-arm101.md) (Hugging Face / The Robot Studio hobbyist SKU), [xArm 7](xarm-7.md) (UFactory mid-tier), and [Franka Panda](franka-panda.md) (research-grade industrial). The ViperX 300 sits in a fourth slot: research-grade benchtop bimanual.
- **Hardware substrate for the entire ALOHA / ACT / Mobile ALOHA literature** — if a paper says "ALOHA-style bimanual teleop," it usually means a ViperX 300 leader-follower pair.

## Open questions

- **Current pricing** — Mobile ALOHA's $32k breakdown doesn't itemize per-arm cost; the wiki should chase the vendor price (~$5–6k/arm anecdotally) on a future ingest.
- **Versions and variants** — Trossen ships multiple ViperX SKUs (250, 300, 300 6-DOF, 300S); the Mobile ALOHA cite is "ViperX 300 6DOF." Worth confirming the SKU lineage on a vendor-page ingest.
- **Comparable Trossen-class alternatives** — WidowX, PincherX. None ingested.

## Related
- [ALOHA / Mobile ALOHA](aloha.md) — primary user.
- [SO-ARM101](so-arm101.md) — cheaper hobbyist alternative tracked in the wiki.
- [xArm 7](xarm-7.md), [Franka Panda](franka-panda.md) — other research-grade arm SKUs.

## Mentioned in
- [Mobile ALOHA Paper](../sources/mobile-aloha-paper.md)

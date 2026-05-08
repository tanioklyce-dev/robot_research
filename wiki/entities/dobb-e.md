---
title: Dobb·E
type: entity
subtype: method
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [dobb-e, behavior-cloning, hpr-encoder, stretch, nyu, shafiullah, predecessor]
status: stub
---

**Dobb·E** — *"On Bringing Robots Home"* (Shafiullah et al., arxiv 2306.16650, 2023). NYU work led by Mahi Shafiullah; precursor to [[robot-utility-models|Robot Utility Models]] from the same group. Establishes the **HPR (Home Pretrained Representation) encoder**, the **Stick-v1 hand-held data-collection tool**, and the **Homes of New York dataset** — three pieces of infrastructure that RUM later directly reuses.

## What RUM inherits from Dobb·E
1. **HPR encoder** — pretrained ResNet34 vision encoder. RUM initializes its policies from this checkpoint rather than ImageNet, gaining the "robot-relevant" inductive prior. ([[robot-utility-models-paper|RUM paper]] §2.3.)
2. **Stick-v1 data-collection tool** — hand-held device with a stick-mounted gripper for collecting in-home demonstrations. RUM's [[robot-utility-models-paper|Stick-v2]] is the iPhone-Pro-based successor, retaining the "portable, no-calibration" design philosophy.
3. **Homes of New York dataset** — Dobb·E's in-home demonstrations corpus. RUM seeds its **door-opening dataset** from this pre-existing corpus, augmenting it with new Stick-v2 demonstrations.

## Why it matters in this wiki
Dobb·E is the **load-bearing predecessor** to the RUM project. Without it, RUM doesn't have a vision-encoder pretrained checkpoint, doesn't have a battle-tested data-collection workflow, and doesn't have a head-start corpus for door-opening data. The "engineering shape" of "low-cost robot + learned-from-data zero-shot policy" that RUM popularized was already largely built in Dobb·E.

## Related
- [[robot-utility-models|Robot Utility Models]] — direct successor.
- [[stretch|Stretch]] — primary deployment platform (Dobb·E used Stretch first).
- [[lerrel-pinto|Lerrel Pinto]] — co-senior on Dobb·E and RUM.
- [[hello-robot|Hello Robot]] — supplied the Stretch hardware.

## Mentioned in
- [[robot-utility-models-paper|Robot Utility Models Paper]] — references Dobb·E for HPR encoder, Homes of New York dataset, and Stick-v1.
- [[robot-utility-models-website|Robot Utility Models Project Page]]

## Open questions / TBD
- **Primary source not yet ingested.** Dobb·E paper (arxiv 2306.16650) deserves its own source page; this entity is built from RUM-paper references rather than direct read.
- HPR encoder training details — what exactly is "Home Pretrained Representation" vs an ImageNet-pretrained ResNet34? Worth documenting once the Dobb·E paper is ingested.
- The full Homes of New York dataset is presumably released; would be useful infrastructure to flag.

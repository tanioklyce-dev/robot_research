---
title: Dobb·E
type: entity
subtype: method
created: 2026-05-08
updated: 2026-07-04
sources: 4
tags: [dobb-e, behavior-cloning, hpr-encoder, stretch, nyu, shafiullah, predecessor]
---

**Dobb·E** — *"On Bringing Robots Home"* ([Shafiullah et al. 2023](../sources/dobb-e-paper.md), arxiv 2311.16098). NYU work led by [Mahi Shafiullah](mahi-shafiullah.md); precursor to [Robot Utility Models](robot-utility-models.md) from the same group. Establishes the **HPR (Home Pretrained Representation) encoder**, the **Stick-v1 hand-held data-collection tool**, and the **Homes of New York dataset** — three pieces of infrastructure that RUM later directly reuses. Headline result: **81% success rate on 109 tasks across 10 homes** with 5 minutes of demonstration + 15 minutes of adaptation per task ([paper](../sources/dobb-e-paper.md)).

## What RUM inherits from Dobb·E
1. **HPR encoder** — pretrained ResNet34 vision encoder. RUM initializes its policies from this checkpoint rather than ImageNet, gaining the "robot-relevant" inductive prior. ([RUM paper](../sources/robot-utility-models-paper.md) §2.3.)
2. **Stick-v1 data-collection tool** — hand-held device with a stick-mounted gripper for collecting in-home demonstrations. RUM's [Stick-v2](../sources/robot-utility-models-paper.md) is the iPhone-Pro-based successor, retaining the "portable, no-calibration" design philosophy.
3. **Homes of New York dataset** — Dobb·E's in-home demonstrations corpus. RUM seeds its **door-opening dataset** from this pre-existing corpus, augmenting it with new Stick-v2 demonstrations.

## Why it matters in this wiki
Dobb·E is the **load-bearing predecessor** to the RUM project. Without it, RUM doesn't have a vision-encoder pretrained checkpoint, doesn't have a battle-tested data-collection workflow, and doesn't have a head-start corpus for door-opening data. The "engineering shape" of "low-cost robot + learned-from-data zero-shot policy" that RUM popularized was already largely built in Dobb·E.

## Related
- [Robot Utility Models](robot-utility-models.md) — direct successor.
- [Stretch](stretch.md) — primary deployment platform (Dobb·E used Stretch first).
- [Lerrel Pinto](lerrel-pinto.md) — co-senior on Dobb·E and RUM.
- [Hello Robot](hello-robot.md) — supplied the Stretch hardware.

## Mentioned in
- [Dobb·E Paper](../sources/dobb-e-paper.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md) — references Dobb·E for HPR encoder, Homes of New York dataset, and Stick-v1.
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [VQ-BeT Paper](../sources/vq-bet-paper.md) — cites the Dobb·E → RUM → VQ-BeT NYU continuity; uses the HPR encoder + Stick.
- [Stretch 4 launch](../sources/hello-robot-stretch-4-launch.md) — Dobb·E named among Stretch-3-trained policies whose Stretch 4 transfer is an open question.

## Open questions / TBD
- [Dobb·E Paper](../sources/dobb-e-paper.md) now filed (2026-05-16) at the abstract level. Confirmed: 13 hours / 22 NY homes / CC-BY-4.0 / 81% success on 109 tasks. **arxiv ID corrected to 2311.16098** (the earlier 2306.16650 reference may be an even-earlier preprint or a typo).
- HPR encoder architecture (the "ResNet34" claim) is from the RUM paper, not yet verified against the Dobb·E paper body — paper-body §3 has the training procedure.
- "5-min demo + 15-min adaptation" mechanics: full fine-tune vs frozen-encoder + small head? Paper body needed.

---
title: Dobb·E — On Bringing Robots Home (paper)
type: source
url: https://arxiv.org/abs/2311.16098
author: Nur Muhammad Mahi Shafiullah, Anant Rai, Haritheja Etukuru, Yiqian Liu, Ishan Misra, Soumith Chintala, Lerrel Pinto
published: 2023-11
ingested: 2026-05-16
tags: [dobb-e, home-robotics, imitation-learning, hpr-encoder, stick, nyu, hello-stretch]
---

## Summary
The primary [Dobb·E](../entities/dobb-e.md) paper from NYU's Pinto group — *"On Bringing Robots Home,"* a system bringing affordable robotic manipulation into actual homes. Three integrated contributions: **(1) the Stick** — a cheap iPhone-mounted demonstration tool, **(2) Homes of New York** — a 13-hour, 22-home dataset, and **(3) HPR (Home Pretrained Representations)** — a vision encoder pretrained on that data that enables rapid task adaptation. Headline result: **81% success rate across 109 tasks in 10 homes over 30 days**, with only **5 minutes of demonstrations and 15 minutes of adapting** per new task. The direct precursor to [Robot Utility Models](../entities/robot-utility-models.md) (RUM) from the same group — RUM later reuses HPR as the encoder backbone and Stick-v2 as the data-collection iteration.

## Key claims

### Abstract (verbatim, partial)
"Throughout history, we have successfully integrated various machines into our homes...we initiate a large-scale effort towards this goal by introducing Dobb-E, an affordable yet versatile general-purpose system for learning robotic manipulation within household settings...we test our system in 10 homes, with a total of 109 tasks in different environments, and finally achieve a success rate of 81%."

### Three contributions

1. **The Stick (v1)** — "demonstration collection tool we built out of cheap parts and iPhones." A handheld grabber with an iPhone mount that lets users teleoperate-by-demonstration without a robot present. Predecessor to RUM's Stick-v2.
2. **Homes of New York dataset** — "13 hours of data in 22 homes of New York City." First in-home demonstration corpus of this scale.
3. **Home Pretrained Representations (HPR)** — vision encoder pretrained on the Homes-of-New-York data, providing a robot-relevant inductive prior superior to ImageNet pretraining for downstream policy learning.

### Headline experimental results
| Metric | Value |
|---|---|
| Homes tested | **10** |
| Tasks attempted | **109** |
| Test duration | 30 days |
| Per-task demonstration time | 5 minutes |
| Per-task adaptation time | 15 minutes |
| Overall success rate | **81%** |

### Documented real-world failure modes
- "Effects of strong shadows" — vision-encoder degradation under uneven lighting.
- "Variable demonstration quality by non-expert users" — Stick-collected demos vary in quality more than lab teleop.

### Release
- Open-source software stack, models, data, and hardware designs.
- License: **CC-BY-4.0**.

## Entities mentioned
- [Dobb·E](../entities/dobb-e.md)
- [Robot Utility Models](../entities/robot-utility-models.md) — successor system at NYU.
- [Mahi Shafiullah](../entities/mahi-shafiullah.md), [Lerrel Pinto](../entities/lerrel-pinto.md) — first / senior authors.
- [Stretch](../entities/stretch.md) — the deployment platform (per the wiki entity; not in the abstract excerpt).
- Other co-authors: Anant Rai, Haritheja Etukuru, Yiqian Liu, Ishan Misra, Soumith Chintala.

## Concepts touched
- [Imitation learning](../concepts/learning/imitation-learning.md) — Dobb·E is canonical few-demonstration IL.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — in-home manipulation context.

## Open questions
- HPR encoder architecture and training procedure not in the abstract — the entity page calls it a ResNet34, but that hasn't been verified against the paper body. Worth pulling for the [imitation learning](../concepts/learning/imitation-learning.md) concept page.
- "5-min demo + 15-min adaptation" — what exactly happens during the 15-min adaptation step? Fine-tune the full encoder? A small policy head on top of frozen HPR? The abstract is silent.
- The wiki entity page cites arxiv 2306.16650 (earlier preprint) for Dobb·E; this source uses **2311.16098** (the verified-fetch version). Worth aligning the entity page.
- 81% success rate is reported overall — distribution across the 109 tasks (which task classes work, which don't) is in the paper body.

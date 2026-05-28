---
title: Hugging Face
type: entity
subtype: organization
created: 2026-05-10
updated: 2026-05-15
sources: 11
tags: [hugging-face, foundation-models, open-source, lerobot, robotics, ml-platform]
---

**Hugging Face** — Brooklyn / Paris-based open-source AI company. Foundational ML platform (Transformers library, Datasets, Hub) for the modern open-weights ecosystem. In this wiki, Hugging Face is most directly relevant as the **maintainer of [LeRobot](lerobot.md)**, the open-source imitation-learning framework that has become the de-facto software stack for low-cost mobile manipulators (SO-ARM100/101, LeKiwi, XLeRobot, Bambot, Koch v1.1).

> [!note] Stub-level entity
> Hugging Face appears across many sources in this wiki (model checkpoints for V-JEPA 2, LeWM, DINO-WM, etc., all live on the HF Hub), but their broader company / ecosystem hasn't been ingested in depth. This entity exists primarily as a citation target for LeRobot-related sources.

## Why it matters in this wiki

- **LeRobot** is the dominant open-source IL framework in the wiki's "affordable mobile manipulator" cluster.
- The **HF Hub** is the de-facto distribution channel for model checkpoints across the wiki's JEPA, VLA, and IL coverage (e.g., V-JEPA 2 checkpoints, LeWM checkpoints, DINOv2 backbones).
- Hugging Face's role in the LeRobot ecosystem is purely software / framework maintenance; design and distribution of compatible hardware happens via independent partners ([SIGRobotics-UIUC](sigrobotics-uiuc.md) for LeKiwi, [The Robot Studio](the-robot-studio.md) for SO-ARM, [Seeed Studio](seeed-studio.md) as a distributor).

## Robotics-adjacent people

- [Remi Cadene](remi-cadene.md) — LeRobot lead.
- Thomas Wolf — co-founder of HF; co-organizer of the [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md).
- Marine Caous (`maringetxway`) — hackathon curator; maintains the `all-winners` dataset.

## Related

- [LeRobot](lerobot.md) — primary HF-maintained project relevant here
- [Meta FAIR](meta-fair.md) — origin lab for many models that ship via HF Hub
- [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md) — HF-organized community event

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **17 HF authors** (Cadene, Aliberts, Capuano, Aractingi, Zouitine, Kooijmans, Choghari, Russi, Pascal, Palma, Shukor, Moss, Soare, Aubakirova, Lhoest, Gallouédec, Wolf); ICLR 2026 conference paper; canonical academic reference for the [LeRobot](lerobot.md) framework.
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md)
- (Plus indirect references across many model-checkpoint-bearing sources)

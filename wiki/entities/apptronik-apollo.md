---
title: Apptronik Apollo
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-11-17
sources: 9
tags: [apollo, apptronik, humanoid, bipedal, nvidia-partnership, ut-austin]
status: stub
---

**Apptronik Apollo** — humanoid from Apptronik (Austin, TX; UT Austin spinout). Announced August 2023; commercial deployments at Mercedes-Benz and other industrial pilots in 2024–2025. **NVIDIA collaboration**: Apollo is one of the platforms targeted by [GR00T](nvidia-groot.md) and the broader Physical AI stack.

## Specs (Apollo, 2023–2024 generation)
- ~1.73 m tall, ~73 kg.
- ~25 kg payload (high relative to other humanoids).
- Battery-swap design for ~24-hour effective uptime.
- Cameras + force sensors; designed for industrial workcells.

## Mercedes-Benz kitting pilot with Gemini Robotics 2.5 (2026-11)
The first quantified Apollo deployment result in the wiki comes from Google DeepMind, not Apptronik ([GR 2.5 blog](../sources/gemini-robotics-2-5-blog.md)). On "active automotive production lines" in **Kecskemét, Hungary** and **Sindelfingen, Germany**, **Apollo 2** performed automotive kitting: picking metal brackets from supply bins into sequencing containers in line order. Gemini Robotics ER tracked the workflow and [Gemini Robotics 2.5](gemini-robotics.md) controlled the arms and hands. Reported success: **96%**, described as a proof-of-concept.

Apptronik CEO Jeff Cardenas: the models improved "dramatically in just a few weeks of post-training" and carried over to production "with very little drop-off." So the figure is for a task-specific post-trained model. Pick count, duration, cycle time and intervention rate are not given.

In DeepMind's lab evaluation the same robot, with the 22-DoF [SharpaWave](sharpa-wave.md) hand, is the five-finger platform for GR 2.5's dexterity charts (for example packing pastries with tongs at 100% and untying a ribbon bow at 70%).

## Position vs other humanoids
- **Industrial / logistics focus.** Like Figure's BMW partnership, Apollo's first deployments are warehouse + automotive manufacturing.
- **NVIDIA-aligned AI stack.** GR00T was demonstrated on Apollo at GTC 2024 / 2025. Closer to NVIDIA's open-stack position than Tesla / Figure's vertical integration. The one deployment with a published number, though, runs Google's models ([GR 2.5 blog](../sources/gemini-robotics-2-5-blog.md)).
- **Higher payload** than most humanoids in this size class — design choice for industrial use.

## Related
- Apptronik — manufacturer (UT Austin spinout).
- [NVIDIA GR00T](nvidia-groot.md) — VLA targeted at Apollo.
- [NVIDIA](nvidia.md) — strategic partner.
- [Atlas](atlas.md) / [Figure](figure.md) — industrial-humanoid competitors.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — landscape.

## Mentioned in
- [Gemini Robotics: Bringing AI into the Physical World](../sources/gemini-robotics-report-2025.md) — the earliest Gemini Robotics result on Apollo (March 2025): fine-tuned to pack a lunch bag with five-fingered hands, shown in one figure with no success rate.
- [Gemini Robotics 1.5 tech report](../sources/gemini-robotics-1-5-report.md) — Apollo is one of GR 1.5's three training/eval embodiments (ALOHA / Franka / Apollo).
- [DeepMind Gemini Robotics model page](../sources/deepmind-gemini-robotics-model-page.md) — Apptronik named as a Gemini Robotics 2 partner; per press coverage the whole-body demonstration platform is **Apollo 2**, a version this page does not yet cover.
- [Gemini Robotics 2 blog](../sources/gemini-robotics-2-blog.md) — **Apollo 2** is the whole-body demonstration platform, benchmarked with both **[SharpaWave](sharpa-wave.md)** (5-finger, 22-DoF) and **Inspire** hands.
- [Gemini Robotics 2: Safety Evaluations](../sources/gemini-robotics-2-safety-report.md) — real-world safe-stopping evaluated on Apollo 2 in a garage: 99% human detection, 96% safe-pose transition.
- [Gemini 4 Argon for Robotics](../sources/gemini-4-argon-robotics-blog.md) — Apollo 2 in simulation only: Argon turns a paper sketch into a mujoco_warp scene and a 76-DoF whole-body throw that knocks down 6/6 boxes.
- [AI Search news roundup (2026-11-01)](../sources/ai-search-news-2026-11-01.md) — Apollo appears in a Genie 4 + Gemini 4 Argon checkers demo; DeepMind's blog names it, and the footage is generated.
- [Gemini Robotics 2.5 blog](../sources/gemini-robotics-2-5-blog.md) — the Mercedes-Benz kitting pilot (96%, two plants) and Apollo 2 + SharpaWave as the five-finger evaluation platform.

## Open questions / TBD
- **No primary source ingested.** Apptronik's product pages + GR00T-on-Apollo announcements would anchor specs and partnership details.
- Specific GR00T deployment numbers on Apollo — not public.
- Mercedes-Benz pilot results — one figure now public (96% kitting success, via DeepMind); volume, duration, interventions and which hand was used are not.

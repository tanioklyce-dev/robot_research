---
title: HIW-500 — Humanoids In-the-Wild Dataset (BitRobot, Unitree, Hugging Face)
type: source
url: https://bitrobot-foundation.github.io/humanoids-in-the-wild-500-hours/
author: BitRobot, Unitree, Hugging Face
published: 2026-06
ingested: 2026-09-11
format: web (dataset page + two HF dataset cards + LeRobot meta/info.json)
local_path: raw/2026-06-bitrobot-hiw-500-dataset-page.md
sha256: cb1197ef29fa15bf0c7bc88858eff052e05208e1ea0e1bd5103c6260dba8fdba
license: CC BY 4.0
tags: [hiw-500, bitrobot, unitree, unitree-g1, dataset, humanoid, whole-body, teleoperation, in-the-wild, household, mobile-manipulation, lerobot, open-data, cc-by]
---

## Summary

**HIW-500** is a **500+ hour, 23,743-episode** dataset of **whole-body teleoperation of a [Unitree G1](../entities/unitree-g1.md)** doing household tasks in **12 real homes in Southeast Asia**, published June 2026 by [BitRobot](../entities/bitrobot.md) with Unitree and Hugging Face under **CC BY 4.0** — the most permissive license on any humanoid dataset in this wiki. Eleven tasks (setting the table, restocking the fridge, sweeping, laundry, hanging keys, assembling a children's table …), 161 subtask labels, 148K+ subtask annotations, ~10 TB raw. Two formats: raw ROS bag / MCAP, and **LeRobot v3.0**. It is one of the named ingredients of Unitree's [UnifoLM-WLA-1.0](unifolm-wla-1-project-page.md) training mix. The site pitch: "built for learning from real homes, not lab-only scenes," with layout, object state, lighting, clutter and operator style varying per episode.

## Key claims

### Scale and composition (page chart data + LeRobot `info.json`)

| Task | Episodes | Hours | Avg episode |
|---|---:|---:|---:|
| Building children table | 760 | 110.0 | 8 m 41 s |
| Hang hanger | 1,481 | 68.8 | 2 m 47 s |
| Clean up the room | 1,454 | 62.9 | 2 m 36 s |
| Setting the table | 5,526 | 46.6 | 30 s |
| Restocking fridge | 1,879 | 42.6 | 82 s |
| Kitchen organization | 1,586 | 42.2 | 96 s |
| Hang keys on a hook | 2,381 | 30.3 | 46 s |
| Move pillow to sofa | 1,995 | 24.8 | 45 s |
| Sweep floor | 1,877 | 20.6 | 40 s |
| Picking trash | 1,805 | 19.3 | 39 s |
| Clothes washing | 2,423 | 17.2 | 26 s |

- Chart totals: **23,167 episodes / 485.3 h** across the 11 tasks; LeRobot `info.json`: **23,743 episodes, 40,839,947 frames at 30 fps, 11 tasks**.

> [!note] Three hour-counts that do not agree
> The headline is "500+ hours"; the per-task chart (labeled "hours in selected cleaned dataset") sums to **485 h**; and the LeRobot release's frame count works out to **378 h** (40.84 M frames ÷ 30 fps). The raw ROS-bag release is presumably the 500+ h figure; the LeRobot conversion appears to be a subset, or the chart hours include streams the frame count does not. Quote **~380 h in LeRobot format** for anything trained from the LeRobot repo, and "500+ h raw" otherwise.

- **Subtask annotation is navigation-heavy.** The top labels by count are *move to table* (51,257), *move to bed* (24,374), *dump trash* (19,650), *move to trash can* (16,143), *pick trash* (14,412), *move to sink*, *move to fridge*, *move to countertop* — six of the top eight are locomotion. This is a **mobile-manipulation** corpus; the manipulation is short grasp/place primitives between walks.
- The long-horizon outlier is **Building children table** — 760 episodes averaging 8.7 min, 110 h, 23% of all hours — which is also the BitRobot **2026 Humanoid IKEA Assembly Challenge** task, published separately as a raw challenge dataset.

### Hardware and modalities

- **Robot:** Unitree G1 with **Dex1-1 two-finger grippers**; **head stereo camera** (HBVCAM-4M2214HD, per the challenge card) and **wrist RealSense D405** (RGB + stereo IR), all **480p @ 30 fps**. LeRobot video keys: `observation.images.head` at **1280×480** (side-by-side stereo), `left_wrist` / `right_wrist` at 640×480, AV1-encoded.
- **State:** `observation.state` = **29 joint positions** (legs, waist, arms, wrists, named per Unitree SDK); `observation.state.wbc` = 23-D; IMU and odometry in the raw bags; camera intrinsics/extrinsics in metadata.
- **Action (23-D) is the whole-body-controller command, not joint targets:** `pivot_vx, vy, vyaw, roll, pitch, yaw, height` (7 base/torso commands) + left and right **end-effector 6-DoF pose** + `left/right trigger, squeeze` (gripper). The teleoperator drives a WBC; the dataset records what the WBC was told. See [whole-body control](../concepts/robotics/whole-body-control.md).
- **Language:** `language_persistent` (episode-level instruction) and `language_events` (timed subtask labels) — the 148K annotations live in the events stream.

### Provenance and terms

- HF repos created **2026-06-09**; raw repo last modified 2026-06-29, LeRobot repo 2026-07-17. Roadmap: V1 = 500+ h (June 2026); V2 = "more tasks and environments," undated.
- **CC BY 4.0** for the public release; the page also sells **commercial licensing for "additional humanoid data"** and custom collection — HIW-500 is a sample of a larger in-house corpus.
- Citation lists **BitRobot, Unitree and Hugging Face** as authors; no individual names, no paper, no collection protocol (operator count, teleop rig, consent, home selection) is published.

## Entities mentioned

- [BitRobot](../entities/bitrobot.md) — publisher (new entity); [Unitree](../entities/unitree.md), [Unitree G1](../entities/unitree-g1.md); [Hugging Face](../entities/hugging-face.md) / [LeRobot](../entities/lerobot.md) (v3.0 format).
- [HIW-500](../entities/hiw-500.md) — the dataset's own entity page.
- [UnifoLM](../entities/unifolm.md) — consumer of the data.

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — the action space *is* the WBC interface.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — BitRobot's network model as a third sourcing pattern; and the same silence on consent.
- [Imitation learning](../concepts/learning/imitation-learning.md), [VLA models](../concepts/learning/vla-models.md).

## Open questions

- **Which 500 hours?** Reconcile raw vs LeRobot hour counts before quoting scale.
- **Who teleoperated, with what rig, how many operators?** "Operating style varies per episode" is a claim about the operator pool, and the pool is undescribed.
- **Consent and privacy** for footage inside 12 occupied homes — nothing stated, as with Figure's Go-Big and Index.
- **Does the WBC-level action space transfer?** A policy trained on `pivot_*` + EE poses assumes Unitree's WBC underneath; it is not a joint-space dataset and cannot be retargeted without one.
- **Is this the "lower-body stream" of UnifoLM-WLA-1.0?** The base/torso commands here are the obvious content of WLA's lower-body RVQ tokens; unconfirmed.

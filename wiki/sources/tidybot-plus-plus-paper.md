---
title: "TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning (Dec 2024)"
type: source
url: https://arxiv.org/abs/2412.10447
fetch_url: https://arxiv.org/pdf/2412.10447v1
local_path: raw/tidybot-plus-plus-2412.10447v1.pdf
sha256: a1a349a410c8e7ea90fbce9509bf546ba3b6321f2f00dae69498faa4e8598e81
author: Jimmy Wu, William Chong, Robert Holmberg, Aaditya Prasad, Yihuai Gao, Oussama Khatib, Shuran Song, Szymon Rusinkiewicz, Jeannette Bohg
published: 2024-12-11
ingested: 2026-11-08
tags: [tidybot-plus-plus, mobile-manipulation, holonomic, open-source, imitation-learning, household, diffusion-policy, primary-source]
---

# TidyBot++

## Summary

[TidyBot++](../entities/tidybot-plus-plus.md) is an open-source holonomic mobile base using powered casters, costing **$5–6k** before an arm, with a phone teleoperation interface for collecting imitation-learning data. Princeton and Stanford researchers trained diffusion policies on six household tasks in a real apartment. Its main research finding is that holonomic motion makes tasks much easier to learn.

## Key claims

- **Hardware.** Powered-caster base, 34 kg, 54 × 50 cm footprint, payload rated at 60 kg in the paper's table. The reference build adds a Kinova Gen3 7-DoF arm (12 kg with mount and power supply), which is not included in the base price, and a mini PC.
- **Imitation-learning results (10 rollouts each, real apartment).** Open fridge 10/10, wipe countertop 9/10, load dishwasher 7/10, take out trash 10/10, load laundry 7/10, water plant 6/10. Policies used 50 demonstrations, or 100 for the fridge task, and each set took one to two hours to collect.
- **Holonomic versus differential drive.** Same conditions (50 demonstrations, 500 epochs): holonomic 9/10, differential drive **4/10**.
- **Openness.** Documentation and code at [tidybot2.github.io](http://tidybot2.github.io).

## Entities mentioned

- [TidyBot++](../entities/tidybot-plus-plus.md)
- [Jeannette Bohg](../entities/jeannette-bohg.md)
- [Kinova](../entities/kinova.md)
- [Diffusion Policy](../entities/diffusion-policy.md)

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- Each task was evaluated in one environment. How well do these policies transfer to a second home?

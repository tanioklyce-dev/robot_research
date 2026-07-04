---
title: Standard Bots
type: entity
subtype: company
created: 2026-07-04
updated: 2026-07-04
sources: 1
tags: [standard-bots, industrial-robot-arm, manufacturing, learn-from-demonstration, commercial, ro1]
---

**Standard Bots** — US industrial robot-arm maker (Glen Cove, NY; CEO Evan Beard; ~$63M raised) building 6-axis arms for manufacturing automation, with a **self-serve learn-from-demonstration AI platform** ([AI page](../sources/standardbots-ai-page.md)). The commercial / industrial face of imitation learning in this wiki.

## Products
- **Spark** (7 kg / 900 mm / $29,500), **Core / RO1** (18 kg / 1,300 mm / $37,000), **Thor** (30 kg / 2,000 mm / $49,500), **Bolt** (mobile droid, 14 kg / 900 mm, beta).

## AI offering
*"First self-serve AI platform for industrial robots — train by demonstration."* Teleoperation capture (gamepad / anti-gravity / jogging) → onboard-vision recording → **cloud model training** → autonomous, self-correcting execution; claimed **~1 demo, 0 code**. No disclosed model architecture or benchmarks. Customers: NASA, Amazon, Lockheed Martin, Verizon.

## Why it matters in this wiki
- **Industrial LfD counterpoint** to the research-VLA line. Where [GR00T](nvidia-groot.md) / [π0](pi-zero.md) chase cross-embodiment foundation models, Standard Bots productizes single-vendor, per-customer skill learning as a no-code service — the same teleop→train→deploy loop as [LeRobot](lerobot.md) wrapped for factory buyers.
- A data point on how [imitation learning](../concepts/learning/imitation-learning.md) reaches industrial users in 2026.

## Related
- [Imitation learning](../concepts/learning/imitation-learning.md) — the underlying paradigm.
- [Standard Bots RO1 industrial arm](https://standardbots.com) — flagship product.
- [LeRobot](lerobot.md) — the open-source analogue of the teleop→train→deploy loop.

## Mentioned in
- [Standard Bots — AI page](../sources/standardbots-ai-page.md) — primary source.

## Open questions
- Whether there's a foundation model behind the platform or per-skill behavior cloning.
- Any NVIDIA/other partnership; the compute stack behind "cloud training."

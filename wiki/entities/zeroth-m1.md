---
title: Zeroth M1
type: entity
subtype: robot
created: 2026-08-17
updated: 2026-08-17
sources: 1
tags: [zeroth, m1, home-robot, companion-robot, assistive-robotics, fall-detection, biped, wheeled, consumer-robotics]
---

**Zeroth M1** — a **$2,499**, ~494 mm tall consumer home robot from [Zeroth Robotics](zeroth-robotics.md), marketed for companionship, elder safety monitoring, child interaction and pet monitoring. Hybrid **bipedal + wheeled** locomotion, 20 DoF, sold as a pre-order.

## Specifications

All figures from the [product page](../sources/zeroth-m1-product-page.md) — vendor-published, none independently verified.

| Item | Value |
|---|---|
| Price | **$2,499** |
| Height | **494 mm** (~19.4 in); footprint 195 × 125 mm |
| Dual-arm span | 20.08 in (~510 mm) |
| Weight | body **6.17 lb** (~2.8 kg); mobility base 3.08 lb; dock 6.17 lb |
| DoF | **20** (no breakdown published) |
| Speed | **bipedal 0.05 m/s**, **wheeled 0.6 m/s**, autonomous following |
| Obstacle clearance | 40 mm bipedal / 20 mm wheeled |
| Endurance | ~2 h; 80% charge in 1 h |
| Sensors | LDS LIDAR, iTOF depth, vision camera, IMU, 3-mic array (16 ft) |
| Interaction | voice + app, multi-language |

## The two speeds are the design

**0.05 m/s walking is ~3 m per minute** — roughly 1/25 of adult pace. **0.6 m/s on wheels** is ordinary indoor-robot speed. The biped mode is therefore best read as a **demonstration and expressive capability**, with the wheeled base doing the actual transport. That distinction is not cosmetic for the advertised safety features: crossing a 10 m room takes **~17 s wheeled and over 3 minutes walking**.

At **2.8 kg and 494 mm with no published payload or reach**, the M1 is not a physically assistive robot in the sense this wiki uses the term — see [assistive robotics](../concepts/robotics/assistive-robotics.md), where the mobile-manipulation tier is [Stretch](stretch.md)-class. Nothing on the product page describes lifting, carrying, fetching or manipulating an object. Its advertised value is **sensing, conversation and alerting**.

## Advertised capabilities

"Gentle fall detection, mobile safety checks, daily assistance, alerts, scam prevention, interactive learning for kids, pet behavior monitoring and remote interaction." Also positioned for developers via "an open multi-language programming platform, VR integration and reinforcement learning tools."

> [!warning] No evidence accompanies any of these claims
> The page publishes **no accuracy figure, no evaluation, no trial, and no deployment result** for fall detection or any other safety feature. It also publishes **no compute specification** — the robot's processor, and whether inference runs on-device or in the cloud, are absent from every Zeroth page. CES-launch coverage says it **runs Google Gemini**; if accurate, the safety features depend on a network round-trip, which is a materially different product from an on-device monitor. See [open questions](../sources/zeroth-m1-product-page.md).
>
> There is likewise **no privacy or data-handling statement** for a device with an always-on camera, LIDAR and a 16-foot microphone array in a home — the standing gap the [long-term in-home deployments](../syntheses/assistive/long-term-in-home-robot-deployments.md) literature treats as decisive for household acceptance.

## Where it sits in this wiki

- **Price tier:** an order of magnitude below [Stretch](stretch.md) (**$29,950** for Stretch 4; ~$20k for the S3) and [Kinova Jaco](kinova-jaco.md) (~$35k) — the entrants this wiki treats as the in-home benchmarks.
- **Capability tier:** the **social / monitoring** band, not the mobile-manipulation band. Closest in kind to the companion and social-assistive robots catalogued under [assistive robotics](../concepts/robotics/assistive-robotics.md), not to [OK-Robot](ok-robot.md) or [Robot Utility Models](robot-utility-models.md).
- **Evidence tier:** the weakest in the wiki's home-robot set — one vendor page, zero independent measurements.

## Related

- [Zeroth Robotics](zeroth-robotics.md) — maker; also W1 ($7,999 outdoor/security) and Jupiter ($89,999 humanoid).
- [Stretch](stretch.md) — the research-grade in-home mobile manipulator.
- [Aging in place](../concepts/robotics/aging-in-place.md) — the demand-side ADL/IADL taxonomy this product gestures at.
- [Levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md).

## Mentioned in

- [Zeroth M1 — product page](../sources/zeroth-m1-product-page.md)

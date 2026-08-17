---
title: Zeroth M1 — product page
type: source
url: https://www.zeroth0.com/products/m1
author: Zeroth Robotics
published: undated (page assets stamped 2025-12-22; Shopify theme "[dev] sainstore | M1 landing page | 20260804")
ingested: 2026-08-17
venue: Zeroth Robotics online store (Shopify)
tags: [zeroth, m1, home-robot, assistive-robotics, consumer-robotics, fall-detection, companion-robot, ces-2026, preorder]
---

## Summary

Vendor product page for the **Zeroth M1**, a **$2,499**, ~494 mm tall home robot marketed as "embodied intelligence" for domestic companionship, elder safety and child interaction. It is a **hybrid biped/wheeled** design — walking at 0.05 m/s, rolling at 0.6 m/s — with 20 DoF, LIDAR + iTOF + camera + IMU + 3-mic array, and ~2 hours of endurance.

The page is worth having because of **what it prices**, not what it proves. The wiki's in-home assistive cluster is anchored on research platforms an order of magnitude more expensive ([Stretch](../entities/stretch.md) at $29,950, [Kinova Jaco](../entities/kinova-jaco.md) at ~$35k), and its strongest household results — [OK-Robot](../entities/ok-robot.md), [Robot Utility Models](../entities/robot-utility-models.md) — are lab systems. A consumer device claiming **fall detection and daily assistance at $2,499** is a datapoint about where the price floor is being tested, even though the page substantiates almost none of the capability it advertises.

> [!warning] This is marketing copy, not a spec sheet, and the storefront is visibly unfinished
> Read the claims below as *advertised*, not verified. Concrete signals from the page itself:
> - The HTML `meta description` reads **"This is a product description for W1."** — a placeholder for the sibling product.
> - The product's `name` in the page's own structured data is literally **`"M1 - 2499"`**, and `description` / `category` are empty strings.
> - Schema.org `availability` is **`InStock`** while the call-to-action reads **"Reserve Now"** — a pre-order presented as stock.
> - The live theme is named **`[dev] sainstore | M1 landing page | 20260804`** — a development theme serving production.
> - "Watch the full **videoo**" appears twice.
> - On the sibling [Jupiter](https://www.zeroth0.com/products/jupiter) page, the listed sale price is **$89,999** while the reserve button says **"Only $131,999."**
> - Every "About Us" navigation target — Our Identity, Our Journey, Our Innovation, Press — **returns HTTP 404**.

## Key claims

### Positioning

- "M1 is an embodied intelligence. It sees. It listens. It remembers. And it acts." Framed around "human–technology symbiosis," "interaction, companionship, and protection."
- Marketed as **"one of the world's first embodied intelligence robots designed specifically for home environments"** (from the site's product-carousel copy). *This wiki does not support that as a first-ness claim* — see [domestic-robot precursors](../concepts/robotics/assistive-robotics.md) and the [long-term in-home deployments](../syntheses/assistive/long-term-in-home-robot-deployments.md) record.
- Three advertised scenarios: **Home**, **Nature**, **Lab**.

### Advertised capabilities

| Scenario | Claims |
|---|---|
| Home | "gentle fall detection, mobile safety checks, daily assistance, alerts, **scam prevention**, interactive learning for kids, pet behavior monitoring and remote interaction" |
| Nature | "independent outdoor mobility, nature-based interactive learning for children, real-time pet behavior tracking with remote reassurance" |
| Lab | "20 degrees of freedom, an **open multi-language programming platform**, **VR integration** and **reinforcement learning tools**" for builders and developers |

Feature headings, given without elaboration: *Proactive, Human-like Interaction · A Living Intelligence That Grows with You · Deeper Connection, True Companionship · Guardian Mode, Reimagined · Precision in Motion · An Open Platform for Exploration.*

### Specifications (as published)

| Item | Value |
|---|---|
| **Price** | **$2,499.00** USD ("Reserve Now") |
| Dimensions | 195 mm (L) × 125 mm (W) × **494 mm (H)** |
| Dual-arm span | 20.08 in (~510 mm) |
| Weight | Robot body **6.17 lb** (~2.8 kg); mobility base 3.08 lb; charging dock 6.17 lb |
| DoF | **20** |
| Mobility | **Bipedal 0.05 m/s**; **wheeled 0.6 m/s**; "supports autonomous following" |
| Obstacle handling | Bipedal 1.58 in (~40 mm); wheeled 0.79 in (~20 mm) |
| Endurance | **~2 hours** |
| Charging | 80% in 1 hour |
| Sensing | **LDS LIDAR** (whole-home mapping), **iTOF** depth (small household obstacles), **vision camera** (recognition & avoidance), **IMU** (posture/motion), **3-mic circular array** (16 ft pickup) |
| Interaction | Voice / app; multi-language; "natural, continuous conversational interaction" |
| Materials | Stainless steel, aluminium alloy, ABS, rubber, silicone, glass |

### Product line context (sibling pages)

| Product | Price | Positioning |
|---|---|---|
| **M1** | $2,499 | "The Companion — At Home" |
| **W1** | $7,999 | "The Explorer — In the Wild": 578×520×680 mm, **28 kg**, high payload, 24/7 security patrol, portable power, expressive face (1 DoF eyebrows, 1 DoF eye sockets) |
| **Jupiter** | $89,999 (button: $131,999) | "The Wanderer — Among Stars": human-scale humanoid, teleoperation + autonomous, "training, simulation, and front-of-house service" |
| Humanoid | — | "Coming Soon" |

## What the page does *not* say

These absences were checked by string search against the page source, and each one is load-bearing for a home robot that claims fall detection:

- **No compute specification of any kind** — no SoC, no processor, no on-board vs cloud split. (Secondary reporting says the M1 runs **Google Gemini**; the vendor page never mentions Gemini, cloud, or connectivity.)
- **No privacy or data-handling statement** on a product with an always-on camera, LIDAR and 16-foot microphone array in a home.
- **No Wi-Fi / connectivity spec**, no app platform requirements.
- **No payload, no arm DoF breakdown, no reach, no lift capacity** — despite "daily assistance."
- **No ship date, no deposit terms, no refund policy, no warranty.**
- **No accuracy or evaluation figure** behind fall detection, scam prevention, or pet behaviour monitoring.

> [!note] The two mobility numbers are the most informative specs on the page
> **0.05 m/s bipedal** is roughly 1/25 of adult walking pace — about 5 cm per second, or 3 m/min. **0.6 m/s wheeled** is a normal indoor robot speed. Read together, the biped is a demonstration mode and the wheels are the transport. A robot that reaches a fallen person at 0.6 m/s crosses a 10 m room in ~17 s; at 0.05 m/s it takes over three minutes. For the "gentle fall detection" claim, which mode is used matters more than the DoF count.

## Entities mentioned

- [Zeroth Robotics](../entities/zeroth-robotics.md)
- [Zeroth M1](../entities/zeroth-m1.md)

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md)
- [Aging in place](../concepts/robotics/aging-in-place.md)

## Open questions

- **What actually runs the perception and dialogue?** Secondary CES coverage says Gemini, which would imply a cloud dependency for the "Guardian Mode" safety features. Unverified against any Zeroth primary. **This is the single fact that decides whether the device is an assistive robot or a networked camera with legs.**
- **Is the $2,499 price real?** CES coverage cited "starting near $2,899"; the page says $2,499; the Jupiter page contradicts itself by $42,000. Price claims on this storefront are not yet reliable.
- **What is the "open multi-language programming platform"?** No SDK, repo, docs link, or licence is given anywhere on the site. The developer positioning is currently an assertion.
- **What does 20 DoF cover?** No breakdown. The sibling W1 page itemises DoF down to eyebrows, so the omission on M1 is a choice.
- **Has anyone independent handled one?** All coverage found is CES-launch and press-release derived. No teardown, no review, no measured result.

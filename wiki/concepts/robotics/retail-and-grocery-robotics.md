---
title: Retail and grocery robotics
type: concept
created: 2026-11-08
updated: 2026-11-08
sources: 9
tags: [retail, grocery, mobile-manipulation, teleoperation, reliability, shelf-stocking]
---

**Retail and grocery robotics** covers robots that scan, stock, pick or deliver goods for stores and shoppers. Scanning and delivery are deployed at scale. Physically picking items from live shelves remains early.

## Key references

- [TRI grocery field tests](../../sources/tri-grocery-mobile-manipulation-paper.md) — the real-store reference.
- [From Pixels to Shelf](../../sources/pixels-to-shelf-paper.md) — low-cost stocking on Stretch 3.
- [Groceryshop 2026](../../sources/robot-report-groceryshop-2026.md) — where the deployed market stands.
- [RoboBenchMart](../../sources/robobenchmart-paper.md) and [MarketGen](../../sources/marketgen-paper.md) — the two open simulated benchmarks.
- [Starship press releases](../../sources/starship-grocery-press-releases.md) — the largest delivery volume, by the company's own figures.

## Current state

- **Scanning.** Simbe says it has rolled out 3,000 Tally robots, which capture shelf data and do not handle goods ([The Robot Report](../../sources/robot-report-groceryshop-2026.md)).
- **Stocking.** Stretch 3 exceeded 98% per object and 87% per task in a mock supermarket, limited to cans and small boxes ([Peron et al.](../../sources/pixels-to-shelf-paper.md)).
- **Autonomous shopping.** TRI's best result was 35.7% of runs and 28.9% of listed items, at night, excluding produce, refrigerated goods, glass and items over 4.5 kg ([TRI](../../sources/tri-grocery-mobile-manipulation-paper.md)).
- **Teleoperated order picking.** [Blue Collar Robotics](../../entities/blue-collar-robotics.md) reports about 120 items an hour with one remote person per robot ([Utah Business](../../sources/utah-business-blue-collar-robotics.md)), and planned paid trials for Q4 2026 ([company](../../sources/blue-collar-robotics-site.md)).
- **Delivery to the door.** [Starship](../../entities/starship-technologies.md) reports over 10 million deliveries across all goods and is moving over 1,200 robots from campuses to grocery. In Finland, S Group says robots handle as much as 20% of its online grocery orders ([Starship](../../sources/starship-grocery-press-releases.md)). These are company figures.
- **Simulated benchmarks.** In [RoboBenchMart](../../sources/robobenchmart-paper.md), the best fine-tuned policy reached 63% on picking in familiar scenes, fell to 38% in new ones and 10% with new items, and scored zero on multi-step tasks. In [MarketGen](../../sources/marketgen-paper.md), modular LLM agents stayed below 15% with partial credit.
- **Vendor deployment claims.** [Galbot](../../entities/galbot.md) claims retail and warehouse sites at scale in China ([product page](../../sources/galbot-g1-product-page.md)), not independently confirmed here.

## A recurring design pattern

TRI paired a parallel-jaw gripper with suction because tight shelves favour it. Blue Collar uses suction alone, and Galbot offers it as a swappable tool. Shelves seem to pull designs away from hands.

> [!note] Comparing these numbers
> The 98% and 35.7% figures measure different things. One is per object in a lab; the other is a complete multi-item run in a real store. TRI shows why the gap is expected: at 99% per action, a chain of 103 actions falls below 35.7%.

> [!note] The benchmarks don't yet measure what the field disagrees about
> RoboBenchMart supports only parallel-jaw grippers, even though [suction keeps appearing](#a-recurring-design-pattern) on real grocery robots. Neither benchmark's main task has been run on a real robot, so simulated scores can't yet be compared with TRI's in-store result.

## Related concepts

- [Behavior trees](behavior-trees.md) · [Runtime failure detection](runtime-failure-detection.md) · [Assistive robotics](assistive-robotics.md)

## Mentioned in

- [TRI grocery field tests](../../sources/tri-grocery-mobile-manipulation-paper.md)
- [From Pixels to Shelf](../../sources/pixels-to-shelf-paper.md)
- [The Robot Report on Groceryshop 2026](../../sources/robot-report-groceryshop-2026.md)
- [Blue Collar Robotics — company site](../../sources/blue-collar-robotics-site.md)
- [Utah Business on Blue Collar Robotics](../../sources/utah-business-blue-collar-robotics.md)
- [Galbot G1 — product page](../../sources/galbot-g1-product-page.md)

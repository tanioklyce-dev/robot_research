---
title: "This $3,555 Humanoid Robot Learns New Chores in 30 Minutes, Startup Says (CNET)"
type: source
url: https://www.cnet.com/tech/computing/flourish-3555-humanoid-robot-learns-chores-in-30-minutes-startup-says/
local_path: raw/2026-09-29-cnet-flourish-1.md
sha256: b37279e147c42166f31642252906d6974c0257acc0874844b8b94158cf158a4b
author: Ajay Kumar (CNET)
published: 2026-09-29
ingested: 2026-10-07
venue: CNET (consumer tech press)
format: "launch-day article (~1,100 words) with emailed CEO quotes and price comparisons"
tags: [flourish, flourish-1, home-robot, consumer-robotics, pricing, 1x-neo, weave-isaac, teleoperation, safety, secondary]
---

# This $3,555 Humanoid Robot Learns New Chores in 30 Minutes, Startup Says

## Summary

Consumer-press launch piece on [Flourish 1](../entities/flourish-1.md). It is useful for three things the other coverage lacks: the CEO's claims about **manufacturing status and margins**, his statement that **no remote human operator runs the robot in normal use**, and a **price comparison** against [1X NEO](../entities/1x-neo.md) and Weave Isaac 1. The reviewer calls $3,555 *"optimistic on the company's part, especially given… a limited production run of just 50 units."*

## Key claims
- CEO Antoine Marcel, by email: *"It's a product launch, not a paid beta… the main dependency is supply chain rather than fundamental R&D. The robots are already in the manufacturing and assembly process. Some components, particularly the batteries, have production lead times of around two months."*
- Generalization claim: *"If you teach Flourish 1 something like, 'put the shoes into the shoe cabinet,' you're teaching it the task, not a fixed sequence of coordinates… the shoes don't need to be in exactly the same place every day."*
- **No teleoperators:** *"in normal operation, there's no human operator remotely controlling the robot."* CNET contrasts this with 1X and Weave, which *"employ teleoperators for tasks their robots can't complete."*
- Teaching: use the phone as **a proxy object** (e.g. slide it across the table to show wiping). An hour later the robot is ready to run or schedule the task.
- Tasks include **loading a dishwasher**. The [company site](flourish-robots-website.md) does not list this task and says "no water".
- Safety, from the CEO: *"The robot is designed to stop its motion when it detects a person or animal entering its working area."* He says the wheeled base and limited arm payload and power *"reduce the amount of energy involved when the robot is operating around people."*
- Body: 3'7", 44 lb, 35" reach, 12 h runtime, and *"what appears to be a telescoping torso."*
- Privacy: customers *"can opt out of sharing data to train models"* in the app.
- Price context given by CNET: **1X NEO ~$20,000 or $499/month**; **Weave Isaac 1 $7,999 or $449/month**, shipping in California in fall 2026. Flourish says it is **not selling at a loss**. Cost argument: *"Some humanoid platforms add legs that can represent tens of thousands of dollars in hardware, or build arms designed to carry 10 kg."*
- The first 50 units are built by Flourish itself. Going further needs *"industrializing the product and expanding manufacturing capacity."*

## Contradictions with other sources

> [!warning] Contradiction — "not a paid beta"
> The [Terms of Sale](flourish-robots-website.md) call Flourish 1 *"an experimental product… not a finished consumer appliance"*, sold as-is with no warranty and no returns. Both describe the same 50 units.

> [!warning] Contradiction — opting out of training data
> CNET says you can opt out of sharing training data. The [Privacy Policy](flourish-robots-website.md) §5 says *"teaching a task requires a recording session, so declining means that task cannot be taught,"* and approved recordings train fleet models. The opt-out exists, but its price is not being able to teach the robot.

> [!note] Dishwasher loading vs. "no water"
> The task appears in CNET and the [press release](flourish-1-launch-press-release.md) but not on the site's task tabs. A dishwasher is dry while you load it, so this is not strictly inconsistent. No source reports a success rate for it ([Clubic](clubic-flourish-1.md) says so explicitly).

## Entities mentioned
- [Flourish Robots](../entities/flourish-robots.md) · [Flourish 1](../entities/flourish-1.md) · [1X NEO](../entities/1x-neo.md) · Weave Isaac 1 (no entity page)

## Concepts touched
- [Levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md): an autonomy-only claim (no remote operator), against 1X's Expert Mode.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md): stop-on-intrusion and low energy are design claims, with no certification stated.

## Open questions
- "Stop when a person or animal enters the working area" detected by what? A wrist camera and a floor-level lidar see different volumes. A cat on a counter is in neither.

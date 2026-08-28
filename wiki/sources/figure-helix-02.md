---
title: Introducing Helix 02 — Full-Body Autonomy (Figure AI)
type: source
url: https://www.figure.ai/news/helix-02
author: Figure AI
affiliation: Figure AI
published: 2026-01-27
ingested: 2026-08-28
tags: [figure, helix, helix-02, vla, whole-body-control, loco-manipulation, system-0, tactile-sensing, sim-to-real, rl, vendor-source]
---

> [!warning] Vendor announcement, no evaluation
> Helix 02 has no paper, no benchmark, no baseline, no success rate, and no failure analysis. Every result is a video Figure describes as autonomous. The architecture description is unusually specific for a Figure post; the *results* are not measured at all.

## Summary

**Helix 02** — [Figure AI](../entities/figure.md)'s second-generation VLA, announced 2026-01-27, extending [Helix](helix-blog.md)'s upper-body control to the **entire robot**. The architectural news is a third tier below the existing System 1 / System 2 split: **System 0**, a 10M-parameter learned whole-body controller running at **1 kHz**, trained on **1,000+ hours of retargeted human motion** plus sim-to-real RL, which Figure says **replaces 109,504 lines of hand-engineered C++**. S1 is rewired from "images + joint state → upper body" to **"all sensors in, all actuators out"** — head cameras, palm cameras, fingertip tactile and full-body proprioception → every joint including legs. The headline demonstration is a **4-minute, 61-action continuous dishwasher task** across a full-sized kitchen with no resets and no human intervention, which Figure claims is "the longest horizon, most complex task completed autonomously by a humanoid robot to date."

## The three-tier stack

| | Role | Rate | Size |
|---|---|---|---|
| **S2** | Scene understanding, language, goal latents | slow (7–9 Hz in Helix 1) | 7B (Helix 1 figure) |
| **S1** | Visuomotor policy → full-body joint targets | 200 Hz | 80M (Helix 1 figure) |
| **S0** | Balance, contact, whole-body coordination → actuator commands | **1 kHz** | **10M** |

Figure gives sizes only for S0 in this post; S1/S2 parameter counts carry over from the [original Helix post](helix-blog.md) and may be stale.

## Key claims

### System 0 — the new layer

- *"A foundation model for human-like whole-body control: a learned prior over how people move while maintaining balance and stability."*
- **Training data**: over **1,000 hours of joint-level retargeted human motion data**.
- **Architecture**: **10M-parameter** network; inputs full-body joint state + base motion; outputs joint-level actuator commands at **1 kHz**.
- **Training**: entirely in simulation across **more than 200,000 parallel environments** with extensive domain randomisation; direct transfer to real robots, generalising "across the fleet."
- Explicitly *not* per-behaviour reward engineering: rather than "separate reward functions for walking, turning, crouching, or reaching," S0 learns to **track human motion directly**, and coordination/posture/balance fall out of that.
- **"Replaces 109,504 lines of hand-engineered C++ with a single neural prior."**

### System 1 — all sensors in, all joints out

- **Inputs**: head cameras, **palm cameras**, **fingertip tactile sensors**, full-body proprioception.
- **Outputs**: complete joint-level control of legs, torso, head, arms, wrists and individual fingers.
- Still a transformer conditioned on S2 latents, but now emitting full-body targets that S0 tracks.
- *"The palm cameras and tactile sensors are new hardware capabilities from Figure 03. This is the first time we've demonstrated neural network policies that depend on these modalities."* — the explicit statement that **Helix 02 requires Figure 03 hardware**.

### System 2

- Unchanged in role; expanded in **scope** of instruction. Helix 1: *"Pick up the ketchup."* Helix 02: *"Walk to the dishwasher and open it," "Carry the bowls to the counter," "Go back to the top rack and pick up the cups."* S2 does not plan footsteps.

### Results (videos, described)

The dishwasher task — walk to dishwasher, unload, cross the room, stack in cabinets, load, start it:

- **4 minutes**, **61 loco-manipulation actions**, correct ordering, "implicit error recovery," task state maintained across minutes.
- **Locomotion under manipulation constraints** — walks while holding delicate objects.
- **Whole body as a tool** — closes a drawer with its **hip**, lifts the dishwasher door with its **foot** when hands are full.
- **Bimanual coordination** — objects transferred between hands, stacked, placed.
- **Motor range spanning four orders of magnitude** from millimetre finger motion to room-scale locomotion, from one network.

Four dexterity tasks enabled specifically by tactile + palm cameras: unscrewing a bottle cap (tactile-regulated grip and torque); **extracting a single pill** from an organiser when occluded from the head camera; **dispensing exactly 5 ml from a syringe** against variable resistance; **singulating small metal parts from clutter** (real BotQ parts).

## Assessment

> [!note] The 109,504-line claim is the most interesting number here
> It is a precise, falsifiable-shaped statement about what learned whole-body control displaced: an entire hand-written controller stack. Whether the C++ was *equivalent* in scope is unknowable from outside — but the direction matches what the rest of the wiki shows independently ([SONIC](sonic-paper.md), [BumbleBee](bumblebee-experts-to-generalist-wbc.md), [MotionBricks](motionbricks-paper.md)): motion-tracking RL on retargeted human mocap is displacing model-based WBC on humanoids. Figure's S0 is architecturally unremarkable against that literature — 10M params, 1 kHz, mocap retargeting, massive-parallel sim, domain randomisation is the standard recipe. What is different is that it sits under a production VLA on a robot being built at one per hour.

> [!warning] "Longest horizon, most complex task to date" is unfalsifiable as stated
> No competing system is named, no metric defines "complex," and no success rate is given for the 4-minute task — one successful video is compatible with a 5% success rate. The wiki's comparable claims all come with numbers: [Gemini Robotics 2](gemini-robotics-2-blog.md) publishes per-height pick success (76.3% / 68.4% / 45.7%). Figure publishes none.

> [!warning] Still no external results, three announcements running
> Helix (Feb 2025), Helix 02 (Jan 2026), Index (Aug 2026) — see [Figure](../entities/figure.md). Zero externally checkable numbers across all three.

## Entities mentioned

- [Helix](../entities/helix.md) · [Figure 03](../entities/figure-03.md) · [Figure](../entities/figure.md) · [BotQ](../entities/botq.md)

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — S0 is a WBC motion-tracking policy in the SONIC/BumbleBee family.
- [VLA models](../concepts/learning/vla-models.md) — the S2/S1 hierarchy, now three-tier.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — 200k parallel envs + domain randomisation, zero-shot.
- [Imitation learning](../concepts/learning/imitation-learning.md) — human motion retargeting as the S0 training signal.

## Open questions

- **What is the success rate of the dishwasher task?** Unstated, and it is the only number that would make the claim meaningful.
- **Where does the 1,000 hours of human motion come from?** AMASS? Internal capture? [Index](../entities/figure-index.md) had not launched. Retargeting method unstated.
- **What is the S2 model in Helix 02?** The 7B VLM is a Helix-1 figure; nothing says it carried over.
- **Onboard or off?** Helix 1 claimed onboard inference on "embedded low-power GPUs." A 1 kHz S0 + 200 Hz S1 + a 7B S2 is a demanding budget against the [~460 W whole-robot draw](figure-f03-battery.md) implied by the battery. Never addressed.

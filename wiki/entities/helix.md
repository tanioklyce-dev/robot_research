---
title: Helix (Figure AI)
type: entity
subtype: model
created: 2026-08-28
updated: 2026-08-28
sources: 4
tags: [helix, figure, vla, humanoid, system-0, whole-body-control, loco-manipulation, hierarchical-policy, vendor-source]
---

**Helix** — [Figure AI](figure.md)'s proprietary vision-language-action model for humanoid control. Two generations: **Helix** (2025-02-20), a two-tier System 2 / System 1 architecture controlling the **upper body**; **Helix 02** (2026-01-27), which adds a third tier, **System 0**, and extends control to the **entire robot** — walking, manipulating and balancing under one network, from pixels to actuator commands.

> [!warning] No paper, no benchmark, no baseline — across both generations
> Every Helix claim in this wiki comes from Figure blog posts. There is no published evaluation, no success rate, no comparison against any other system, and no external replication. Architectural detail is specific; *results* are videos.

## The three-tier stack (Helix 02)

| Tier | Role | Rate | Size |
|---|---|---|---|
| **S2** | Scene understanding, language, goal latents | 7–9 Hz | 7B VLM (Helix-1 figure) |
| **S1** | Visuomotor policy → joint targets | 200 Hz | 80M transformer (Helix-1 figure) |
| **S0** | Balance, contact, whole-body coordination → actuator commands | **1 kHz** | **10M** |

Only S0's size and rate are stated for Helix 02; S1/S2 numbers carry over from the [original Helix post](../sources/helix-blog.md) and may be stale.

## Helix 1 (Feb 2025)

From the [Helix blog](../sources/helix-blog.md):

- Two-tier S2 (7B VLM @ 7–9 Hz) / S1 (80M visuomotor transformer @ 200 Hz), **end-to-end gradients between the tiers**.
- Figure-claimed firsts: high-rate continuous control of the **entire humanoid upper body**; simultaneous operation on **two robots** on a shared long-horizon task; generalisation to "thousands" of unseen household objects from language; **onboard** inference on "embedded low-power GPUs"; one unified weight set, no task-specific fine-tuning.
- Trained on **~500 hours** of teleoperated demonstration — marketed as **"<5% of typical VLA datasets."**

> [!warning] Figure has since abandoned the small-data framing
> [Index](figure-index.md) (Aug 2026) claims ingest of ~43,200 h of human video per day — Helix's entire training set every ~17 minutes — and argues the opposite thesis. Figure has never retracted the earlier framing; it stopped using it. See [Figure](figure.md).

## Helix 02 (Jan 2026) — System 0 and full-body control

From [Introducing Helix 02](../sources/figure-helix-02.md):

### System 0 — learned whole-body control

- *"A foundation model for human-like whole-body control: a learned prior over how people move while maintaining balance and stability."*
- **1,000+ hours of joint-level retargeted human motion data.**
- **10M parameters**, in: full-body joint state + base motion; out: joint-level actuator commands at **1 kHz**.
- Trained **entirely in simulation across 200,000+ parallel environments** with extensive domain randomisation; transfers directly to hardware and generalises "across the fleet."
- No per-behaviour reward engineering — walking, turning, crouching and reaching all fall out of motion tracking.
- **Replaces 109,504 lines of hand-engineered C++.**

### System 1 — "all sensors in, all actuators out"

- **In**: head cameras, **palm cameras**, **fingertip tactile**, full-body proprioception. **Out**: legs, torso, head, arms, wrists, individual fingers.
- Requires [Figure 03](figure-03.md) hardware: *"the first time we've demonstrated neural network policies that depend on these modalities."*

### System 2

- Same role, wider instruction scope: from *"Pick up the ketchup"* to *"Walk to the dishwasher and open it."* S2 does not plan footsteps.

### Demonstrated

- **4-minute, 61-action continuous dishwasher task** across a full-sized kitchen — no resets, no intervention. Closes a drawer with its **hip**, lifts the dishwasher door with its **foot** when hands are full. Motor range spanning **four orders of magnitude** from one network.
- Four tactile/palm-camera dexterity tasks: unscrewing a bottle cap, extracting a single **pill** from an organiser, dispensing **exactly 5 ml** from a syringe, singulating small metal parts from clutter.

### Perception-conditioned S0 (April 2026)

From [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md): S0 was body-blind — stairs and ramps "required hand-tuned mode switches and operator intervention." It is now conditioned on head-camera RGB lifted to 3D through Figure's stereo model, trained end-to-end with RL across thousands of randomised terrains, transferring **zero-shot** to real stairs with no fine-tuning or calibration.

### In production

[F.03 at BMW](../sources/figure-03-at-bmw.md) (June 2026): Helix 02 drives the **sequencing** use case at BMW Spartanburg — manipulating thin-walled parts while stepping and repositioning, and pulling a caster-wheeled cart.

## Assessment

> [!note] S0 is conventional; its position is not
> 10M params, 1 kHz, mocap retargeting, 200k parallel envs, domain randomisation — that is the standard motion-tracking WBC recipe the wiki already documents in [SONIC](../sources/sonic-paper.md), [BumbleBee](../sources/bumblebee-experts-to-generalist-wbc.md) and [MotionBricks](../sources/motionbricks-paper.md). What is unusual is that it sits **under a production VLA, on a robot being built at one per hour**, with OTA delivery to a 350+ unit fleet. Figure's advantage is not the algorithm; it is the loop from fleet to data to deployment.

> [!warning] "Longest horizon, most complex task by a humanoid to date" is unfalsifiable as stated
> No competitor named, no metric for "complex," and **no success rate** — one successful video is compatible with a 5% success rate. Contrast [Gemini Robotics 2](../sources/gemini-robotics-2-blog.md), which publishes per-height pick success (76.3% / 68.4% / 45.7%).

## Related

- [Figure 03](figure-03.md) — the hardware Helix 02 requires.
- [Figure](figure.md) — the company.
- [Index](figure-index.md) — the human-video corpus intended as Helix pretraining data.
- [VLA models](../concepts/learning/vla-models.md) — the paradigm.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — what S0 is.
- [NVIDIA GR00T](nvidia-groot.md) — the open counterpart with published benchmarks.

## Mentioned in

- [Helix (Figure AI blog)](../sources/helix-blog.md) — Helix 1.
- [Introducing Helix 02](../sources/figure-helix-02.md) — S0, full-body control.
- [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md) — perception-conditioned S0.
- [F.03 Arrives at BMW](../sources/figure-03-at-bmw.md) — Helix 02 in a factory.

## Open questions

- **Success rates. Any success rate at all.**
- **Where did the 1,000 hours of human motion come from?** AMASS? Internal capture? Retargeting method unstated. [Index](figure-index.md) had not launched.
- **What is S2 in Helix 02?** The 7B VLM figure is from Helix 1.
- **Onboard or off, and on what?** A 1 kHz S0 + 200 Hz S1 + a 7B S2 against Figure 03's [~460 W whole-robot budget](../sources/figure-f03-battery.md) is a real constraint Figure never addresses.

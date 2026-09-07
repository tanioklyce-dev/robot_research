---
title: Tactile sensing
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [tactile-sensing, gelsight, vision-based-tactile, slip-detection, force-torque, visuo-tactile, contact-rich, multimodal-fusion]
---

# Tactile sensing

## Definition

**Tactile sensing** measures contact directly at the interface — location, normal and shear force distribution, and incipient slip — as opposed to inferring it from a single wrench at the wrist or from vision that is occluded exactly when contact happens.

The distinction that matters is **distribution versus resultant**. A wrist-mounted force/torque sensor reports one six-component wrench: the *sum* of everything happening at the fingertips. A tactile array reports *where* on the surface the load is, which is the difference between "3 N of normal force" and "3 N concentrated on one corner of a glass panel." ([Zhang et al.](../../sources/safe-learning-contact-rich-survey.md), §3.3.5)

## Sensor families

- **Vision-based tactile** — a camera behind a deformable gel membrane, reading contact geometry from the gel's deformation. The **GelSight** family dominates robot learning use. High spatial resolution; bulky; a full image pipeline per fingertip. Task-adapted geometries (hemispherical, finger-shaped) extend it beyond the original flat pad.
- **Tactile arrays / skins** — flexible, low-cost, arrayable taxel grids. Lower resolution, far easier to distribute over a hand or a link.
- **Proprioceptive contact estimation** — not a sensor: an observer that estimates contact state from joint torques and motion. The fallback when no tactile hardware exists.

## What touch buys that a wrist sensor cannot

The safety argument is that **unsafe contact patterns are visible before they become unsafe forces**:

> Tactile skins and fingertip arrays reveal pressure distributions, shear and incipient slip at the exact points of interaction, making it possible to detect unsafe contact patterns — such as concentrated loads on corners or sliding on fragile surfaces — **before they escalate into damage or failure**.

Four uses the survey documents:

1. **Encoding what a safe contact configuration looks like.** In furniture assembly, tactile ensembles across fingers characterize how surfaces, edges and fasteners behave during *successful* insertion; the policy is trained to reproduce those signatures and avoid the ones associated with **jamming or over-tightening**.
2. **Gentle manipulation as an emergent property.** Policies rewarded for acquiring task-relevant information while keeping **per-taxel pressures and impact magnitudes low** steer themselves toward soft sliding contacts rather than hard impacts. Safety here is not an external constraint — it is a consequence of how touch is encoded in the observation and reward.
3. **Driving variable impedance online.** Where no base F/T sensing exists — aerial and lightweight manipulators sliding along uneven terrain — tactile plus proprioception is the whole signal: **stiffen when contact is well supported, soften or back off when the taxels report high local pressure or impending slip.** Contact-loss recovery and passivity-aware safety on unknown 3D curved surfaces work the same way. See [impedance control](impedance-control.md).
4. **Confirming what vision planned.** In hierarchical visuo-tactile controllers, vision anticipates geometric constraints and decides *where and when* contact should occur; **tactile confirms whether the contact is distributed and stable the way the planner expected**; proprioception enforces kinodynamic limits. The stated payoff is that tying safety decisions to tactile patterns rather than coarse force thresholds gives more nuanced protection for delicate objects and human collaborators.

## Scale

Tactile is where the newest work is and the thinnest data is. The largest dataset the survey names is **"Touch in the Wild"** (Zhu, Huang & Li, 2025) — a portable visuo-tactile gripper yielding **over 2.6 million vision–touch pairs across 43 manipulation tasks**, used to pretrain a visuo-tactile encoder.

For calibration: that is roughly the scale of a *single* mid-sized vision dataset, for a modality with no web-scrapable equivalent whatsoever. It is the concrete instance of the [contact-data argument](contact-rich-manipulation.md#the-data-problem-which-is-structural) — force and touch have to be collected, one contact at a time, on hardware.

> [!note] Five papers
> In the survey's modality table, **tactile appears in five reviewed works**, against ~60 for force/torque and ~30 for vision. Every claim on this page rests on a small literature. The direction is clearly up — portable collection rigs, pretrained visuo-tactile encoders, multi-DoF grippers enabling cable disentangling and thin-card flipping — but the wiki should treat "tactile sensing improves safety" as a well-motivated hypothesis with a handful of demonstrations, not an established result.

## Related concepts

- [Contact-rich manipulation](contact-rich-manipulation.md) — the task class, and why vision degrades exactly at contact.
- [Impedance and admittance control](impedance-control.md) — what tactile feedback is usually wired into.
- [Dexterous tool manipulation](dexterous-tool-manipulation.md) — the in-hand regime where touch is least substitutable.
- [Six-DOF grasp generation](six-dof-grasp-generation.md) — the open-loop counterpart: predict a grasp from geometry, without ever feeling it.
- [Safe reinforcement learning](../learning/safe-reinforcement-learning.md) — tactile as an observation and a reward channel.
- [VLA models](../learning/vla-models.md) — generalist policies, which almost universally lack a touch input.

## Current state

Vision-based tactile is the research default and GelSight the reference design; low-cost arrays are the deployment-plausible option. The pattern the literature is converging on is **not** tactile-only control but **fusion** — vision for where and when, tactile for whether the contact is what was expected, proprioception for limits. The gap is data: one 2.6M-pair dataset is the largest thing anyone can point to, no web source exists, and no benchmark scores tactile-conditioned safety.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — §3.3.5, the source for this page.

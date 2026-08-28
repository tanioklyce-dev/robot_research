---
title: Actuator fidelity in sim-to-real
type: concept
created: 2026-08-27
updated: 2026-08-27
sources: 1
tags: [sim-to-real, actuator-model, domain-randomization, backlash, bam, dynamixel, locomotion, rl, system-identification]
---

**Actuator fidelity** is the branch of [sim-to-real transfer](sim-to-real-transfer.md) that treats the **motor**, rather than the scene, as the dominant source of the reality gap: instead of an idealised PD controller that produces exactly the commanded torque, the simulator models the physical drivetrain — voltage control law, back-EMF, friction, gear play, command latency, and a battery that sags.

## Why it is a separate thing from domain randomization

Most of the wiki's [domain-randomization](sim-to-real-transfer.md) coverage randomizes what the policy *sees*: textures, lighting, backgrounds, object poses, mass and friction coefficients. That is the right attack when the gap is perceptual or when a manipulator's contact model is uncertain.

It is the wrong attack when the gap is in the **actuator's own dynamics**, because randomizing an idealised model more widely still never produces the *shape* of the real behaviour. A servo that cannot reach its commanded torque at low battery, or that has 2° of dead zone before the output moves, is not a noisy ideal servo — it is a different system. Randomizing around the wrong model widens the distribution without moving it onto reality, and the usual symptom is a gait that is beautiful in sim and immediately falls over.

The distinction sharpens with scale. Large, geared, well-instrumented research actuators approximate ideal PD closely enough that the residual gap is elsewhere. Cheap hobby servos on a light robot do not:

> "At this scale — tiny servos driving a ~800 g biped — **actuator fidelity is most of the sim2real gap**, which is why the actuator is modeled down to its voltage control law instead of an ideal PD." — [Microduck RL](../../sources/pollen-robotics-microduck.md)

Corollary worth stating plainly: **the cheaper the robot, the more of the sim-to-real budget belongs in the actuator model.** This inverts the usual assumption that low-cost platforms should get the cheap version of the sim-to-real treatment.

## The four things a fidelity-first actuator model adds

Taken from the [Microduck](../../entities/microduck.md) implementation, which is the wiki's first fully-published example:

1. **A physical control law instead of a torque source.** The **BAM M6** model ([Rhoban](../../entities/rhoban.md)) of the [Dynamixel](../../entities/dynamixel.md) XL330 simulates the **voltage** control law and **back-EMF**, so the achievable torque falls off with speed the way a real DC motor's does, and with **Coulomb / Stribeck / load-dependent friction** so stiction near zero velocity is present rather than smoothed away.
2. **Randomization over the actuator's own failure axes**, not the scene's: **battery voltage**, **voltage sag under load**, **command delay**, and **friction magnitude**. Note that two of these are *power-system* properties — the policy is being trained to survive a draining battery, which is a real deployment condition no scene randomization reaches.
3. **Backlash as geometry, not noise.** Microduck models **±1° of gear play (2° total)** as an **unactuated hinge in series with each servo joint** — real kinematic freedom in the physics model, not additive noise on the command. The consequence is that the leg can move while the servo does not, and the policy has to learn to cope.
4. **Sensing the model correctly.** The subtle part, and the part that is easy to get wrong: **the real encoder sits on the output side of the play**, so the simulated observations and the firmware's PD emulation must read *through* the backlash hinge (`qpos[servo] + qpos[backlash]`), not at the servo. A backlash model observed at the wrong side of the joint teaches the policy a proprioceptive signal the real robot never produces — worse than no backlash model at all.

Microduck's implementation keeps observation and action dimensions unchanged across the backlash variants, so the same ONNX export path and runtime serve both. That is the engineering property that makes a fidelity twin cheap to maintain: **the fidelity lives in the physics model, not in the interface.**

## Relationship to system identification

Fidelity-first modelling is system identification with the target moved. Classical sysID fits parameters of an assumed model to real trajectories; the actuator-fidelity move is to first choose a model *structure* rich enough to contain the real behaviour (voltage law + friction + play), and only then randomize over its parameters. Getting the structure wrong is not recoverable by better fitting or wider randomization.

This is also why the approach travels well: the [BAM](../../entities/rhoban.md) model is a model of *a class of hobby servo*, published independently of any one robot, and reusable by anyone driving XL330s.

## Related concepts

- [Sim-to-real transfer](sim-to-real-transfer.md) — the parent problem; this page is the actuator-side branch.
- [Real-world robot RL](real-world-robot-rl.md) — the alternative to closing the gap: train on the robot and pay the reset cost.
- [Real-to-sim-to-real](../robotics/real-to-sim-to-real.md) — the scene-side inversion (rebuild the world from the task); this is the actuator-side one (rebuild the motor from the datasheet and the bench).

## Current state

Thinly sourced in this wiki — one worked example. But it is a *complete* one: [`pollen-robotics/microduck_rl`](https://github.com/pollen-robotics/microduck_rl) publishes the actuator classes, the backlash generator, the randomization toggles and the reward-design notes under Apache-2.0, attached to a $399 robot anyone can buy. If the claim generalises — that actuator fidelity dominates the gap below some mass/cost threshold — it reframes how the wiki's low-cost-platform cluster ([SO-ARM101](../../entities/so-arm101.md), [LeKiwi](../../entities/lekiwi.md), [XLeRobot](../../entities/xlerobot.md), all FeeTech- or Dynamixel-class) should approach simulation. **Open question: does anyone in the LeRobot ecosystem model their servos at this level?** Nothing ingested so far suggests they do.

## Mentioned in

- [Microduck — Pollen Robotics launch](../../sources/pollen-robotics-microduck.md) — BAM M6 on XL330, voltage/sag/delay/friction randomization, backlash-as-hinge with output-side encoder reads.

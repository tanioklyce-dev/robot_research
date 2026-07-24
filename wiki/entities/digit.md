---
title: Digit
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-07-15
sources: 2
tags: [digit, agility-robotics, humanoid, bipedal, logistics, gxo, amazon, functional-safety, nvidia-halos]
---

**Digit** — bipedal humanoid from Agility Robotics (Oregon State spinout). First commercial humanoid in **fully-active commercial deployment** at scale: **GXO Logistics** (2024), **Amazon** warehouse trials (2024). Targets warehouse package handling specifically, not general-purpose tasks.

## Specs (Digit V4, 2024)
- ~1.75 m tall, ~65 kg.
- Bipedal with backward-bending knees (ostrich-like leg geometry — distinct from anthropomorphic humanoids).
- 16 DOF; two-arm + grasping.
- Battery + autonomous charging; designed for 24/7 warehouse operation.

## Position vs other humanoids
- **Furthest along in commercial deployment.** GXO and Amazon trials are real production environments, not pilots — distinguishes Digit from research-tier or industrial-pilot-only humanoids.
- **Narrow task focus.** Package totes / shelf-stocking / sortation — explicitly *not* general-purpose. Different design philosophy than Atlas / Figure / Optimus, which target generalist behavior.
- **Non-anthropomorphic legs.** Reverse-knee geometry trades human-form-factor compatibility for energetic efficiency in walking — a deliberate engineering choice.

## Functional safety — inaugural NVIDIA Halos partner
Digit is the **inaugural humanoid partner** for **[NVIDIA Halos](nvidia-halos.md)** ([Halos for Robotics](../sources/nvidia-halos-robotics.md)): it ships with **Halos OS** and demonstrates the **Inside-Out** safety mode — onboard **IGX [Thor](jetson-thor.md) + Halos Core** managing the robot's immediate safety envelope. Notable that the wiki's furthest-deployed-at-scale humanoid is also the first to adopt a certified functional-safety stack — consistent with its warehouse-production focus.

## Related
- Agility Robotics — manufacturer (Oregon, US).
- [NVIDIA Halos](nvidia-halos.md) — functional-safety stack; Digit is its flagship Inside-Out humanoid.
- [Atlas](atlas.md) / [Figure](figure.md) — generalist-humanoid competitors.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — landscape; Digit is the "deployed-at-scale" data point.

## Mentioned in
- [NVIDIA Halos for Robotics](../sources/nvidia-halos-robotics.md) — Digit as inaugural humanoid Halos partner (Inside-Out safety).

## Open questions / TBD
- **No primary source ingested.** Agility's product page + GXO + Amazon press releases would anchor specs and deployment claims.
- Digit's internal software stack — proprietary; minimal academic literature.
- Whether Digit's narrow-task model holds up vs generalist-humanoid pressure from Figure / Atlas / Optimus.

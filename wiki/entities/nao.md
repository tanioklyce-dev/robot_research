---
title: NAO
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-08
sources: 0
tags: [nao, softbank, aldebaran, humanoid, education, social-robot]
status: stub
---

**NAO** — small bipedal educational humanoid from **SoftBank Robotics / Aldebaran** (originally Aldebaran Robotics, France). Introduced 2008. **The canonical educational humanoid** — most CS / robotics curricula that teach humanoid programming use NAO.

## Specs (NAO V6, current generation)
- ~58 cm tall, ~5.4 kg.
- 25 DOF (configuration varies slightly by version).
- Cameras (eye-mounted), microphones, sonars, IMU, force sensors in feet.
- Onboard Intel Atom CPU (~1.6 GHz).
- Programmable in Python, C++, ROS, Choregraphe (visual scripting).

## Why it matters in this wiki
- **Educational humanoid reference point.** Equivalent role to [TurtleBot](turtlebot.md) but for humanoid hardware. Generations of CS students have learned humanoid programming on NAO.
- **RoboCup standard platform** — Standard Platform League uses NAO.
- **Doesn't appear in JEPA / VLA literature.** Like TurtleBot, NAO occupies a clear pedagogical niche but is largely absent from the agentic-robotics research line in this wiki. The educational tier hasn't yet absorbed the JEPA / VLA wave.

## Position vs other humanoids
- **Far smaller than research humanoids.** ~58 cm vs ~1.5–1.8 m for [Atlas](atlas.md) / [H1](unitree-h1.md) / [Figure](figure.md). Tabletop-scale, not human-scale.
- **Less capable than [Unitree G1](unitree-g1.md)** (also smaller-class, but G1 is ~$16k vs NAO's ~$8–15k — comparable price, different capabilities).
- **Long product lifetime** — NAO has been continuously available since 2008 with incremental version updates; few robots have that longevity.

## Related
- Aldebaran / SoftBank Robotics — manufacturer.
- Pepper — larger SoftBank social-robot sibling (no entity page yet).
- [TurtleBot](turtlebot.md) — educational mobile-robot reference (analogous role for non-humanoids).
- [Humanoid platforms survey](../syntheses/humanoid-platforms-survey.md) — landscape.

## Mentioned in
- *(no source pages directly cite NAO; entity built from general knowledge)*

## Open questions / TBD
- **No primary source ingested.** SoftBank's NAO product page would anchor specs.
- Whether NAO has been used in any JEPA / VLA research paper — likely not, but a literature check would close this question.
- NAO's place in 2026 — does it remain the standard, or does Robotis OP3 / Unitree G1 take over?

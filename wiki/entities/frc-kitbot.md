---
title: FRC KitBot
type: entity
created: 2026-05-08
updated: 2026-05-08
sources: 2
tags: [frc, kitbot, chassis, educational-robotics, andymark]
---

# FRC KitBot

A beginner-friendly robot platform included in the [FIRST Robotics Competition](first-robotics-competition.md) Kickoff Kit, designed to get rookie and resource-limited teams competition-ready with minimal fabrication.

## Platform

- **Chassis**: [AndyMark](andymark.md) AM14U6 drivetrain — a multi-season FRC staple; configurable for tank or West Coast drive ([FRC KitBot 2026](../sources/frc-kitbot-2026.md)).
- **2026 configuration**: "Square" variant with side plates cut 3in shorter than stock.
- **Drivetrain**: 6-wheel tank drive (typical AM14U6 setup); belt or chain driven.
- **Materials**: Primarily aluminum extrusion and plate.

## Resources (2026 season)

| Resource | Format |
|----------|--------|
| Build instructions | PDF (6 languages: EN, ZH, HE, PT, ES, TR) |
| CAD models | Onshape (browser) + STEP download |
| Robot code | Java (WPILib) + explanatory guide |
| Enhancement guide | PDF — brainstorming iteration ideas |
| Bumper guide | Linked from Game Manual §8.4 |

Source: [FRC KitBot 2026 page](../sources/frc-kitbot-2026.md).

## Design philosophy

The KitBot is intentionally minimal — it provides a drivable, inspectable robot out of the box, but is designed to be iterated upon. The enhancement guide encourages teams to add game-specific mechanisms (intakes, shooters, climbers) incrementally rather than designing a full custom robot from scratch ([FRC KitBot 2026](../sources/frc-kitbot-2026.md)).

This mirrors the broader FRC ethos of rapid prototyping and iterative design within a compressed build season (~6 weeks from Kickoff to first competition).

## Comparison to other FRC drivetrains

| Drivetrain | Vendor | Type | Approx. cost | Notes |
|-----------|--------|------|-------------|-------|
| **AM14U6 (KitBot)** | [AndyMark](andymark.md) | Tank / WCD | KOP (included) | Default starting point |
| REV MAXSwerve | REV Robotics | Swerve | ~$1,600/set | Higher performance ceiling |
| WCP SwerveX / Swerve X2 | WestCoast Products | Swerve | ~$1,400–1,800/set | Competition-tier swerve |
| Thrifty Swerve | Thrifty Bot | Swerve | ~$1,000/set | Budget swerve option |

Most competitive teams at Worlds run swerve drivetrains, but KitBot-based robots can be effective at Regional/District level, especially with strong game-specific mechanisms.

## Mentioned in
- [FRC 2026 Game Manual](../sources/frc-2026-game-manual.md) (bumper guide reference, §8.4)
- [FRC KitBot 2026](../sources/frc-kitbot-2026.md)

---
title: FRC 2026 Game Manual — REBUILT
type: source
url: https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf
local_path: raw/FRC2026GameManual.pdf
sha256: 5c67300fc412a1eed8ca9dc37fb6644aee05795a2befed1f69736643cbf95139
author: FIRST
published: 2026-01-10
ingested: 2026-05-08
tags: [frc, competition, robotics, game-design, educational-robotics]
---

# FRC 2026 Game Manual — REBUILT presented by Haas

## Summary

The official 166-page rule book for the 2026 [FIRST Robotics Competition](../entities/first-robotics-competition.md) season game **REBUILT**, presented by the Gene Haas Foundation. The game challenges two three-robot alliances to score foam-ball FUEL into HUBs, navigate obstacle structures (BUMPS and TRENCHES), and climb a three-rung TOWER — all within a 2-minute-40-second match. A distinctive alternating-HUB mechanic ties autonomous performance to teleop strategy, making AUTO results consequential throughout the match. The manual also specifies comprehensive robot construction constraints (weight, size, motors, power, pneumatics, software), the [AprilTag](../concepts/robotics/apriltags.md)-instrumented field, and the [roboRIO](../entities/roborio.md)-based control system. Version TU22 (Team Update 22).

## Key claims

### Game overview
- Game name: **REBUILT** presented by Haas; season theme **FIRST AGE** presented by Qualcomm (archaeology-inspired).
- Two alliances of 3 FRC teams each compete in 2:40 matches (§4, p.15).
- Three scoring actions: score FUEL in HUB, cross obstacles, climb TOWER.
- ~3,700 teams from 30+ countries; ~90,000 high-school students projected for 2026 (§1.3, p.5).
- 56 Regionals, 125 District Competitions, 15 District Championships, plus FIRST Championship in April 2026.

### Field layout (§5)
- **FIELD**: ~317.7in × 651.2in (~8.07m × 16.54m) carpeted area (Shaw Neyland II carpet). (§5.2, p.17)
- **HUB** (×2): 47in × 47in rectangular prism; hexagonal 41.7in opening at 72in height; FUEL exits distribute balls into NEUTRAL ZONE; DMX light bars indicate active/inactive status. (§5.4, p.22)
- **BUMP** (×4): 73in wide, 44.4in deep, 6.5in tall HDPE ramps at 15° on each side of HUBs. (§5.5, p.25)
- **TRENCH** (×4): 65.65in wide, 47in deep, 40.25in tall structures robots drive underneath; 22.25in clearance under the arm. (§5.6, p.25)
- **DEPOT** (×2): 42in × 27in staging areas along ALLIANCE WALL with 3in × 1in steel barriers. (§5.7, p.26)
- **TOWER** (×2): 49.25in wide, 45in deep, 78.25in tall climbing structure with 3 rungs (LOW 27in, MID 45in, HIGH 63in from floor), 18in apart center-to-center, 1.66in OD pipe. (§5.8, p.27)
- **OUTPOST** (×2): FUEL delivery point; CHUTE (15° slope, holds ~25 FUEL) + CORRAL (floor-level collection area). (§5.9.2, p.31)
- **NEUTRAL ZONE**: 283in × 317.7in central area between the two ALLIANCE ZONES. (§5.3, p.21)
- **AprilTags**: 32 unique markers from the 36h11 family (IDs 1–32), 8.125in square, on 10.5in polycarbonate panels. Located on HUBs (16 tags), TOWERs (4), OUTPOSTs (4), TRENCHEs (8). (§5.11, p.33)

### Match structure (§6.4)
- **AUTO** (0:20–0:00): 20 seconds, robots operate autonomously. Score FUEL, optionally climb TOWER LEVEL 1. (§6.4, p.44)
- **TELEOP** (2:20–0:00): Driver-controlled. Split into:
  - **TRANSITION SHIFT** (2:20–2:10): 10s, both HUBs active.
  - **SHIFT 1** (2:10–1:45): 25s — alliance that scored MORE in AUTO has HUB deactivated first.
  - **SHIFT 2** (1:45–1:20): 25s — HUBs swap active/inactive.
  - **SHIFT 3** (1:20–0:55): 25s — swap again.
  - **SHIFT 4** (0:55–0:30): 25s — swap again.
  - **END GAME** (0:30–0:00): 30s — both HUBs active; TOWER climbing window.
- HUB alternation mechanic: AUTO winner's HUB goes inactive in SHIFT 1, then alternates. If tied, FMS randomly selects. FMS Game Data relays which alliance scored more. (§6.4.1, p.44–45)

### Scoring (§6.5)
- **FUEL** in active HUB: 1pt (AUTO or TELEOP). Inactive HUB: 0pt. (§6.5.3, p.47)
- **TOWER** — AUTO: LEVEL 1 = 15pts (max 2 robots). TELEOP: LEVEL 1 = 10pts, LEVEL 2 = 20pts, LEVEL 3 = 30pts. Each robot earns only one TELEOP TOWER level. (§6.5.3, p.47)
- **TOWER scoring criteria**: LEVEL 1 = off carpet/TOWER BASE; LEVEL 2 = bumpers fully above LOW RUNG; LEVEL 3 = bumpers fully above MID RUNG. Must contact RUNG/UPRIGHT. (§6.5.2, p.46)
- **Ranking Points**: Win = 3 RP, Tie = 1 RP. Plus 3 BONUS RPs:
  - **ENERGIZED RP**: ≥100 FUEL scored in active HUB (Regional/District). (§6.5.3, p.48)
  - **SUPERCHARGED RP**: ≥360 FUEL scored in active HUB.
  - **TRAVERSAL RP**: ≥50 TOWER points total.
  - Thresholds increase at District Championships (ENERGIZED→240) and FIRST Championship (ENERGIZED→360, SUPERCHARGED→500). (Table 6-5, p.48)
- Scoring assessment continues 3 seconds after timer hits 0:00 (both AUTO and TELEOP) to account for FUEL processing time. (§6.5, p.45)

### SCORING ELEMENTS (§5.10)
- **FUEL**: 5.91in (15.0cm) diameter high-density foam balls, 0.448–0.500lb (~203–227g). Custom-made, purchasable from [AndyMark](../entities/andymark.md) (am-5801). (§5.10.1, p.32)
- 504 FUEL per match: 24 per DEPOT (×2), 24 per OUTPOST CHUTE (×2), up to 8 preloaded per ROBOT (48 max), remainder (~360–408) in NEUTRAL ZONE. (§6.3.4, p.43)
- At District/FIRST Championship, count may increase to 600. (§6.3.4, p.43)
- Robots may CONTROL any number of FUEL simultaneously (no possession limit). (§5.10, p.32)

### Robot construction rules (§8)
- **R103**: Weight ≤115.0lb (52.16kg), excluding bumpers, battery, and Anderson connector. (p.78)
- **R104**: Starting config perimeter ≤110.0in, height ≤30.0in. (p.79)
- **R105/R106**: Horizontal extension ≤12in beyond perimeter, in only one direction at a time. (p.79–80)
- **R107**: Vertical extension: total height ≤30.0in (no extension above starting height). (p.81)
- **R408**: Weight with bumpers ≤135.0lb. (p.90)
- **BUMPERS**: Required around entire perimeter (≤1.25in gaps); 2.25in minimum foam padding depth, 4.5in tall; must be in BUMPER ZONE (2.5–5.75in from floor); team number displayed in 3+ locations. (§8.4, p.85–92)
- **R301**: No individual non-KOP item >$600 FMV. (p.82)
- **R302**: MAJOR MECHANISMS must be built after Kickoff (Jan 10, 2026). (p.84)
- **R303**: Pre-Kickoff designs/software only allowed if publicly available. (p.84)

### Motors & actuators (§8.5)
- Comprehensive allowlist of permitted motors (Table 8-1, p.92): CIM, Falcon 500, NEO, NEO 550, Kraken X60/X44, REV Vortex, and many others.
- Max 8 motor slots on certain motors (CIM-class); unlimited on small motors (RS-550 class and below).
- Servo motors allowed (≤10W continuous at 6V for hobby servos; COTS smart servos up to $75 FMV).

### Power distribution (§8.6)
- Single 12V nominal battery (Pb-acid or LiFePO4 approved types).
- Main breaker: 120A.
- PDH or PDP required; wire gauge tables specified per circuit (10–18 AWG depending on breaker size).

### Control system (§8.7)
- **[roboRIO](../entities/roborio.md)** (roboRIO 1 or roboRIO 2) is the mandatory robot controller. (R710, p.104)
- **Radio**: must use the FRC Radio provided at events (pre-configured at Radio Kiosks).
- **FMS** (Field Management System): Ethernet connection from DRIVER STATION shelf to OPERATOR CONSOLE; manages wireless, E-stop, A-stop, scoring.
- Approved programming languages: Java, C++, LabVIEW (via WPILib). Python supported via RobotPy.
- **OPERATOR CONSOLE**: team-supplied laptop/controller setup; 120VAC outlet provided; E-stop and A-stop buttons on shelf.
- CAN bus and PWM for motor controllers; I2C, SPI, UART, MXP for sensors.

### Pneumatics (§8.8)
- Max 120 PSI stored pressure; working pressure regulated to ≤60 PSI (high side) or ≤30 PSI (low side).
- PCM or PH for solenoid control.
- Compressor must be controlled by PCM/PH auto-fill.

### Inspection (§9)
- Robots must pass initial inspection before competing.
- Interchangeable mechanisms allowed (I103) but all configurations must comply.
- Re-inspection required after significant modifications.

### Drive team (§6.2)
- Up to 5 people: 1 DRIVE COACH (any team member), 1 TECHNICIAN (any member), up to 3 DRIVERS/HUMAN PLAYERS (must be STUDENTS — not yet completed high school as of Sep 1 prior to Kickoff). (Table 6-1, p.40)
- HUMAN PLAYERS manage FUEL through the OUTPOST (CHUTE and CORRAL).

### Strategy notes
- **HUB alternation** is the central strategic mechanic: winning AUTO means your HUB is deactivated first, but you know which shifts are yours. Teams can collect FUEL during inactive shifts for burst scoring during active shifts. (§6.4.1)
- **FUEL volume** is enormous (504+ balls) with no possession limit — intake speed and throughput matter more than precise manipulation.
- **TOWER climbing** provides high point value (up to 30pts per robot = 90pts for 3 robots climbing LEVEL 3) but requires END GAME timing and mechanical complexity.
- **Ranking Point thresholds** incentivize consistent high scoring: 360 FUEL for SUPERCHARGED RP means ~2.25 FUEL/second across all active periods for the alliance.
- **AprilTags** on every major field element enable vision-based autonomous navigation and targeting.

### FMS & software infrastructure
- FMS Game Data is broadcast to all OPERATOR CONSOLEs at TELEOP start, informing which alliance scored more in AUTO. Teams can use this to adapt TELEOP strategy programmatically. (§6.4.1, p.45)
- Audio cues for match milestones: "Cavalry Charge" (match start), buzzers (period ends), "Steam Whistle" (END GAME), etc. (Table 5-4, p.36)
- Team signs display real-time SHIFT indicator, FUEL RP progress, TOWER points, and timer during qualification matches. (§5.9.1, p.29–30)
- Open ports defined by FMS whitepaper; robot code cannot be deployed while connected to FMS. (§5.12, p.36)

## Entities mentioned
- [FIRST Robotics Competition](../entities/first-robotics-competition.md)
- [FRC KitBot](../entities/frc-kitbot.md) (referenced in bumper guide, §8.4)
- [AndyMark](../entities/andymark.md) (field elements, chassis, FUEL am-5801, field variants)
- [roboRIO](../entities/roborio.md) (mandatory controller, R710)
- [AprilTags](../concepts/robotics/apriltags.md) (36h11 vision fiducials, 32 on field)

## Concepts touched
- [AprilTags](../concepts/robotics/apriltags.md) — 32 fiducial markers enabling autonomous vision
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — FRC teams increasingly use simulation for autonomous development
- [Imitation learning](../concepts/learning/imitation-learning.md) — FRC autonomous modes are typically hand-coded, but ML approaches emerging

## Open questions
- What simulation tools do FRC teams use for autonomous development and AI training?
- How do teams implement vision-based autonomous targeting using the AprilTag layout?
- What is the actual distribution of FUEL scoring rates at competition (empirical data on ENERGIZED/SUPERCHARGED RP achievement)?
- How does the HUB alternation mechanic change optimal alliance composition strategy vs. prior years?
- What FRC-specific physics simulators exist for testing robot designs against REBUILT field elements?

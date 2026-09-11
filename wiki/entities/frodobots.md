---
title: FrodoBots (FrodoBots Lab / Earth Rovers)
type: entity
subtype: company
created: 2026-09-11
updated: 2026-09-11
sources: 3
tags: [frodobots, earth-rovers, sidewalk-robot, navigation, teleoperation, crowdsourcing, gamification, depin, dataset-publisher, bitrobot, real-world-evaluation]
---

**FrodoBots** — a 2022 weekend project by brothers Michael and Sam Cho that became the first working instance of **crowdsourcing robot data through a game**: players remotely drive **Earth Rovers**, $199–299 four-wheel sidewalk robots with cameras, GPS, IMU and 4G, in a global scavenger hunt ("ET Fugi" / "Drive to Earn"); the drives become open datasets; and the same fleet then hosts the **Earth Rover Challenge**, an AI-versus-human navigation competition at IROS 2024, ICRA 2025 and IROS 2026 ([challenge site + dataset card](../sources/earth-rover-challenge-frodobots-2k.md)). In February 2025 it merged its network ambitions into [BitRobot](bitrobot.md) with Protocol Labs' Juan Benet ([whitepaper](../sources/bitrobot-network-whitepaper.md)); the datasets now live under the BitRobot Hugging Face org and Earth Rovers is BitRobot's Subnet 01.

## What it has produced

- **FrodoBots-2K** — ~2,000 h / 1 TB / 10+ cities / 9,000+ sessions of teleoperated driving with front and rear video, 10 Hz control inputs, GPS, IMU and two-way audio; **CC BY-SA 4.0**, May 2024.
- **Berkeley-FrodoBots-7K** — the ~7,000 h full set, action labels **reannotated by Berkeley's MBRA** model-based expert; gated, CC BY-SA, Sep 2024.
- **Earth Rover Challenge** — same rovers, same missions across 14 sites; four tracks in 2026 (urban GPS, indoor image-goal, off-road, a ~5 h marathon); co-organized with Dhruv Shah, Wenhao Yu and Tingnan Zhang (DeepMind), Ted Xiao, David Hsu and others. **Top AI vs top human: 15.4 vs 42.0 (2024), 23.78 vs 30.0 (2025).**
- **Earth Rovers SDK** — Python remote-access SDK (off-board compute; ~20 Hz stream, ~500 ms latency; four discrete actions); the platform [SIGRobotics-UIUC](sigrobotics-uiuc.md) builds on.
- Research using the data: MBRA / LogoNav and OmniVLA (Berkeley, Levine and Shah), HPT (MIT), and navigation-scaling papers from Tampere, UCLA and PKU, per the BitRobot site.

## Why it matters in this wiki

- **The earliest crowdsourced-robot-data loop that produced cited research**, predating Figure's Go-Big and Index by two years — but with a lesson the [crowdsourcing](../concepts/learning/crowdsourced-robot-training-data.md) page did not yet have: the human *actions* were degraded by latency and game objectives, so the best downstream work **relabeled them** rather than learning from them.
- **Evaluation as the product.** A standing multi-city fleet scoring AI as a fraction of the best human run is the concrete form of the [BitRobot whitepaper](../sources/bitrobot-network-whitepaper.md)'s "evaluation fleets" idea — and a rare human-normalized real-world benchmark for the [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) page.
- Its three stated theses — robotic gaming as a genre, toy-priced robots, **DePIN tokenomics** — are the BitRobot design in miniature.

## Open questions

- What players are paid; the token itself (the site says "token-incentivized," nothing more).
- Whether the Octo Arms manipulation game ever launched beyond invite-only.
- Cross-edition comparability of the challenge numbers.

## Mentioned in

- [Earth Rover Challenge site + FrodoBots-2K card](../sources/earth-rover-challenge-frodobots-2k.md) — primary.
- [BitRobot Network whitepaper](../sources/bitrobot-network-whitepaper.md) — the origin story and the network it became.
- [SIGRobotics-UIUC projects page](../sources/sigrobotics-uiuc-projects-page.md) — as a sponsor and SDK target.

---
title: Earth Rover Challenge (IROS 2026 site) + FrodoBots-2K dataset card
type: source
url: https://earth-rover-challenge.github.io/
author: Earth Rover Challenge organizers; FrodoBots Lab (dataset card)
published: 2026
ingested: 2026-09-11
format: web (competition site + HF dataset card + company site + SDK README)
local_path: raw/2026-09-11-earth-rover-challenge-and-frodobots-2k.md
sha256: 6fe1f79e74d1c5c6ed74862b0ef30592477ccd44d11a1d53a429c16a197b10e7
license: FrodoBots-2K CC BY-SA 4.0
tags: [frodobots, earth-rovers, earth-rover-challenge, bitrobot, navigation, sidewalk-robot, teleoperation, crowdsourcing, gamification, depin, dataset, real-world-evaluation, ai-vs-human, iros, mbra]
---

## Summary

Two documents that together describe [FrodoBots](../entities/frodobots.md)' loop: **gamers teleoperate $199–299 sidewalk robots** ("Earth Rovers") in a scavenger-hunt game, the drives become an open navigation dataset (**FrodoBots-2K**, ~2,000 h across 10+ cities, CC BY-SA 4.0, May 2024), and the same fleet is then used to **evaluate autonomous policies against the best human players** in the **Earth Rover Challenge** — IROS 2024 (Abu Dhabi), ICRA 2025 (Atlanta), and IROS 2026 (Pittsburgh, 27 Sep–1 Oct, 14 sites, four tracks). The headline the site leads with is the **AI-versus-human gap**: top AI scored 15.4 against a human 42.0 in 2024 (37% of the human ceiling) and 23.78 against 30.0 in 2025 (57%). This is the crowdsourced-data model in its earliest and most-cited form — the one the [BitRobot whitepaper](bitrobot-network-whitepaper.md) later generalized into a protocol — and the only wiki source where **the same fleet is both the data source and the evaluation instrument.**

## Key claims

### FrodoBots-2K (dataset card, May 2024)

- **~2,000 h, 1 TB, 10+ cities, 9,000+ driving sessions** of human-teleoperated Earth Rovers, from the "Drive to Earn" game. Seven streams per drive: gamer control inputs at **10 Hz** plus four wheel RPMs; GPS at 1 Hz; 9-DoF IMU (accelerometer 100 Hz, gyro and magnetometer 1 Hz); front camera **1024×576 @ ~20 fps**; rear camera 540×360; microphone and speaker audio at 16 kHz. As of 12 May 2024, ~1,300 h were downloadable with ~700 h still being cleaned.
- **Three theses** stated on the card: robotic gaming can be a genre; toy-priced robots collect data as well as expensive ones; **"DePIN can scale this project"** via tokenomics. The site's own phrasing: "Embodied AI will be solved by gamers" and "much like how Tesla builds its Autopilot feature by learning from drivers' actions."
- The card's walkthrough video is described as including "a discussion on **latency issues** surrounding the data collection" — the human actions were issued over a ~500 ms remote link.
- **Berkeley-FrodoBots-7K** (challenge site): the ~7,000 h full set, **reannotated with MBRA** "for higher-fidelity action labels"; gated on HF, CC BY-SA, created 2024-09-20.

### The Earth Rover Challenge (site, 2026 edition)

- **Format.** "A globally distributed competition pitting autonomous policies against expert human teleoperators. Same rovers, same missions, across 10+ cities." 14 sites, 35 outdoor rovers + 5 indoor/off-road; free to enter; all compute **off-board** through the Remote Access SDK ("stream front camera in, control commands out; GPS + map exposed"). Teams get **up to 20 h/week of pre-event real-world testing** at remote sites.
- **Platform: Earth Rover Mini+** — 4WD turn-in-place chassis, front + rear cameras, GPS, IMU, 4G LTE; **~20 Hz stream at ~500 ms latency**; discrete action space **forward / backward / left / right**. SDK README: 1.4 kg, 250×190×195 mm, 4 km/h, 12 km range, 18° max slope.
- **Four tracks:** urban GPS-waypoint navigation; indoor image-goal (no GPS); off-road image-goal; and a new **marathon** — urban → indoor → off-road with one policy, leg 1 = 32 checkpoints, ~5 h of driving.
- **Scoring:** reach the checkpoint within **15 m** GPS tolerance; each mission carries a difficulty rating 1–10; aggregate difficulty wins, cumulative time breaks ties.
- **Results so far:** IROS 2024 — top AI **15.4 vs human 42.0** (Seoul National University; top human `masterchi_`). ICRA 2025 — **23.78 vs 30.0** (National University of Singapore). Presented as "the gap is closing fast."
- **Co-organizers:** Chen Feng (NYU), Xuesu Xiao (GMU), Michael Cho and Santiago Pravisani (FrodoBots), David Hsu (NUS), **Dhruv Shah** (Princeton), Joanne Truong (Rhoda AI), **Ted Xiao** (Project Prometheus), Naoki Yokoyama (Georgia Tech), **Wenhao Yu and Tingnan Zhang (Google DeepMind)**, Dinesh Manocha (UMD).

### Downstream research the data enabled (abstracts, not ingested)

- **MBRA / LogoNav** (Hirose, Ignatova, Stachowicz, Glossop, Levine, Shah; [arXiv 2505.05592](https://arxiv.org/abs/2505.05592)): a learned short-horizon model-based expert **relabels or generates actions** for passive data — "large volumes of crowd-sourced teleoperation data and unlabeled YouTube videos… despite their potential for lower quality or missing action labels" — then distills into a long-horizon policy that navigates >300 m in unseen environments, evaluated on a fleet in six cities on three continents.
- **An Earth Rover dataset recorded at the ICRA@40 party** (Zhang, Lin, Visser, Amsterdam; arXiv 2407.05735): a small Rotterdam recording with the challenge robot; vSLAM on FrodoBots-2K.

## Reading it against the wiki

> [!note] The crowdsourcing page's failure modes, with a different one on top
> The [crowdsourcing](../concepts/learning/crowdsourced-robot-training-data.md) page's worries are fraud and embedding-blind dedup. FrodoBots' data has a prior problem: **the human action labels are themselves degraded** — issued at 10 Hz over a ~500 ms link, in a game whose objective (points, scavenger targets) is not "drive well." That is why the most important paper built on it, MBRA, exists: it throws the raw human actions away and *relabels* them with a model-based expert. The dataset's value turned out to be its **observations and diversity**, not its actions — which is the same conclusion the [human-video](../concepts/learning/crowdsourced-robot-training-data.md) crowdsourcers reach from the other side.

- **Evaluation is the durable contribution.** Whatever one thinks of the data, a **standing, calibrated, multi-city fleet** that scores AI as a fraction of the best human run — with pre-event access — is exactly what the [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) page says the field lacks, and it is the concrete instance of the "evaluation fleets" idea in the [BitRobot whitepaper](bitrobot-network-whitepaper.md). The per-edition "fraction of the human ceiling" number is a rare **size-invariant, human-normalized** real-world benchmark.
- **The two numbers are not comparable across editions** — different cities, missions, difficulty ratings, and human fields — so "37% → 57%" is a trend claim on n = 2 with a changing denominator. Read as direction, not magnitude.
- **The action space explains the ceiling.** Four discrete commands at ~2 Hz effective (20 Hz stream, 500 ms latency) make this a low-bandwidth navigation problem where a patient human excels; it says little about manipulation, which is where FrodoBots' "Octo Arms" and BitRobot's TeleArms subnets are trying to extend the same loop.

## Entities mentioned

- [FrodoBots](../entities/frodobots.md) — the subject; [BitRobot](../entities/bitrobot.md) — the successor network and current HF host of the datasets.
- [Google DeepMind](../entities/google-deepmind.md) — co-organizers; [Sergey Levine](../entities/sergey-levine.md) — MBRA senior author.
- [SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md) — maintains an Earth Rover Mini SDK; FrodoBots sponsor.

## Concepts touched

- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md), [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).
- Navigation policies (GNM / ViNT / NoMaD lineage) — **no concept page yet**.

## Open questions

- Per-edition mission lists and difficulty ratings, to make the 2024→2025 comparison meaningful.
- Token economics of "Drive to Earn" — what a gamer actually earned per hour; the site says only "well-designed tokenomics."
- Whether MBRA's relabeling recovers the *intent* of human drives or replaces it — the paper is worth ingesting for that alone.

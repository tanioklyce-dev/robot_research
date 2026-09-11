---
title: BitRobot (BitRobot Network / Foundation)
type: entity
subtype: company
created: 2026-09-11
updated: 2026-09-11
sources: 5
tags: [bitrobot, crowdsourcing, robot-data, network, blockchain, depin, subnets, humanoid, earth-rovers, frodobots, protocol-labs, dataset-publisher, evaluation]
---

**BitRobot** — a **blockchain-coordinated network of robotics "subnets"** that pays contributors (teleoperators, robot owners, compute providers, researchers) in token emissions for validator-scored **Verifiable Robotic Work**, and licenses the resulting datasets and models ([whitepaper](../sources/bitrobot-network-whitepaper.md), March 2025). It grew out of **[FrodoBots](frodobots.md) Lab** (2022, brothers Michael and Sam Cho), whose ET Fugi sidewalk-robot game crowdsourced navigation data across 40+ cities and whose Earth Rovers challenge placed at IROS 2024; Protocol Labs' **Juan Benet** and Jonathan Victor joined in February 2025 to turn it into the network. The **BitRobot Foundation** is the stewarding entity — infrastructure, grants, hackathons, and the commercial licensing arm; it is the sponsor that appears on the [SIGRobotics-UIUC](sigrobotics-uiuc.md) page and the publisher of [HIW-500](hiw-500.md). Self-description: "the world's open robotics lab."

## How it works (whitepaper)

- **Subnets** define a unit of work (miles driven, teleop hours, scenarios generated, models evaluated), a validation rule, and a reward split among Owners, Validators and Contributors. Public subnets receive emissions and their outputs default to open-source **non-commercial**; private subnets pay to use the framework and keep their IP.
- **Robots are NFTs** ("Embodied Node Tokens") that post collateral; penalties and fee sinks (registration, rental cut, licensing) are the economic checks.
- **Emissions** are steered each epoch by a **Senate** and an AI agent ("Gandalf AI") whose votes are weighted by participant delegation — a measurement → evaluation → reward loop.
- Two loops: rent network resources to third parties (e.g. **a fleet of sidewalk robots to evaluate a lab's model**), or produce an output and license it commercially. HIW-500's CC BY public release plus paid access to the larger corpus is the second loop in practice.

## What it has produced

- **[FrodoBots](frodobots.md) navigation data** — FrodoBots-2K (~2,000 h, CC BY-SA) and the MBRA-relabeled Berkeley-FrodoBots-7K; cited by Berkeley RAIL (MBRA, OmniVLA), MIT (HPT) and others. The **Earth Rover Challenge** (IROS 2024 / ICRA 2025 / IROS 2026) is the evaluation-fleet loop actually running: top AI at 37% then 57% of the best human run ([site](../sources/earth-rover-challenge-frodobots-2k.md)).
- **[HIW-500](hiw-500.md)** ([page](../sources/bitrobot-hiw-500-dataset-page.md)) — 500+ h of [Unitree G1](unitree-g1.md) whole-body teleop in 12 real homes, CC BY 4.0, with Unitree and Hugging Face; the **2026 Humanoid IKEA Assembly Challenge** task sits inside it.
- Active subnets (site, 2026): ET Fugi rovers (SN/01), SeeSaw phone-video collection (SN/02, "4 million tasks"), TeleArms and Axis teleop-in-sim (SN/03, SN/04); a **$5M Grand Challenges fund** (Sep 2025) for origami, IKEA assembly, urban navigation.

## Where it sits in the wiki

- A **third sourcing model** on the [crowdsourced robot data](../concepts/learning/crowdsourced-robot-training-data.md) page — neither Figure's landlord (Go-Big) nor its marketplace (Index), but a protocol that pays for validator-scored work. It is the crowdsourcing page's adversarial-data problem written into a mechanism: the measurement is what gets rewarded, validators are the filter, collateral is the deterrent, and cryptographic verification is deferred ([whitepaper](../sources/bitrobot-network-whitepaper.md) §6).
- The wiki's fullest instance of [mechanism design](../concepts/economics/mechanism-design.md) applied to robot data, and the first proposal of an AI agent as a governance voter.
- The evaluation-fleet idea is the one the wiki most wants to exist; its only running instance is the [Earth Rover Challenge](frodobots.md) for sidewalk navigation.

## Open questions

- The fungible token, emission amounts, and what teleoperators are actually paid — unstated everywhere.
- The whitepaper's non-commercial default versus HIW-500's CC BY 4.0.
- Consent terms for footage inside homes and on sidewalks.
- Validator incentives and measurement Goodharting — no audit published.

## Mentioned in

- [BitRobot Network whitepaper](../sources/bitrobot-network-whitepaper.md) — primary.
- [HIW-500 dataset page](../sources/bitrobot-hiw-500-dataset-page.md)
- [UnifoLM-WLA-1.0 project page](../sources/unifolm-wla-1-project-page.md) — HIW-500 as training data.
- [SIGRobotics-UIUC projects page](../sources/sigrobotics-uiuc-projects-page.md) — as a sponsor.
- [Earth Rover Challenge site + FrodoBots-2K card](../sources/earth-rover-challenge-frodobots-2k.md) — the Earth Rovers subnet's data and the running evaluation loop.

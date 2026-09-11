---
title: BitRobot Network Whitepaper (Cho, Victor, Benet — March 2025)
type: source
url: https://bitrobot.ai/whitepaper
author: Michael Cho, Jonathan Victor, Juan Benet
published: 2025-03-10
ingested: 2026-09-11
format: web (HTML whitepaper; companion site pages captured alongside)
local_path: raw/2025-03-10-bitrobot-network-whitepaper.md
sha256: 515013870448c8029d08284a0092c5e1245e5674e26c4ad086edc7b18546bae3
tags: [bitrobot, whitepaper, crowdsourcing, robot-data, data-markets, mechanism-design, incentives, blockchain, depin, subnets, verifiable-robotic-work, frodobots, protocol-labs, evaluation, governance]
---

## Summary

The design document for the [BitRobot](../entities/bitrobot.md) Network, written by FrodoBots founder Michael Cho with Protocol Labs' Juan Benet and Jonathan Victor. Its diagnosis is that Embodied AI is bottlenecked less by algorithms than by **three kinds of data** (synthetic, human video, teleoperation) each with a named gap, and by **two resource problems**: nobody outside a few corporate labs has fleets of robots to evaluate models on, and access to data, compute and evaluation is concentrating. Its proposal is a **blockchain-coordinated network of subnets**, each defining a unit of **Verifiable Robotic Work (VRW)**, with robots registered as NFTs (**ENTs**) posting collateral, validators scoring contributions, and token **emissions** allocated per monthly epoch by a **Senate** plus an AI agent (**"Gandalf AI"**) weighted by participant delegation. Outputs of emission-funded subnets default to open-source **non-commercial**; the Foundation licenses them commercially and recycles fees. It is the mechanism behind the [HIW-500](../entities/hiw-500.md) dataset and the [Earth Rovers](../entities/sigrobotics-uiuc.md) ecosystem, and the most explicit **incentive design for robot data** in this wiki.

## Key claims

### Problem statement (§2–3) — consistent with the wiki's own reading

- **Three data types, three gaps.** Synthetic data: the **sim-to-real gap**, especially for in-the-wild navigation and deformables. Human video: the **embodiment gap** — the Messi analogy: hours of footage of a player "lacks information about his specific body, data processing, and sensory inputs." Teleoperation: what it calls the **"unconscious-to-conscious gap"** — human action-in-response-to-events data exists nowhere at web scale and "requires costly coordination and investment of both physical hardware and human man-hours."
- **Evaluation is the larger bottleneck.** "The only way to evaluate a new model is to observe how the model fares in real world settings… as the model improves, the rate of failure is only observable with large-scale fleets of robots." This is the fleet-scale version of the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) argument (±2 pp needs ≈1,030 rollouts): statistical power for real-world eval is a *hardware* problem.
- **Resource asymmetry** (Fig. 1): a handful of labs hold data flywheels, eval platforms and compute; academia and startups cannot iterate at the same pace — "a worrying trend of significant concentration of scientific progress."

### The mechanism (§4)

- **Verifiable Robotic Work (VRW)** — a per-subnet, validator-scored measure of useful work: distance driven and difficulty scores for sidewalk robots, scenario counts and quality scores for simulated folding, teleop hours, robot online-hours, model creation and evaluation. "Verifiable" at launch means *public inputs, public outputs, public transformations* — **not** cryptographic proofs, which §6 defers until zero-knowledge costs fall.
- **Embodied Node Token (ENT)** — an NFT that is a robot's digital twin and payment conduit; **requires collateral**, which funds penalties for abuse.
- **Subnets** with three roles — Owners (define VRW, output type, validation, reward split), Validators (score contributors; may be the owners), Contributors (researchers, teleoperators, manufacturers). Public subnets are emission-eligible; private ones consume the framework without emissions and keep their IP.
- **Governance** — a **Senate** of "nominated representatives of the broader cryptocurrency and Embodied AI research communities" votes each epoch on which subnets receive emissions and with what weights; **Gandalf AI**, a to-be-open-sourced agent, submits rival weight proposals "as a counter balance"; participants **delegate** voting power to either. The stated end state: responsibilities "transition directly between BitRobot Network participants and Gandalf AI."
- **IP regime (§4.4)** — outputs of emission-funded public subnets are "by default open-sourced for **non-commercial** use"; private-subnet outputs are not. (The live page repeats this paragraph under §4.5 Governance — a rendering fault.)

### The economy (§5)

- **Measurement → Evaluation → Reward loop.** Each Senator and Gandalf AI assigns weights to measurements (e.g. "Qualified Miles" for Subnet 1, or "number of rented humanoid robots"), evaluates subnets against them, and the delegation-weighted, normalized sum sets that epoch's emissions per subnet. The formula is an image; from its variable list, emissions to subnet *k* in epoch *l* scale with N_l · Σ_j D_j · Σ_i E_ij · M_ik, normalized across subnets.
- **Fees and sinks:** subnet registration (anti-spam), ENT registration, a resource-allocation cut on third-party rentals, **licensing fees** for commercial use of Foundation-stewarded data, penalties, collateral.
- **Two loops.** (1) Emissions buy resources that third parties rent — "an AI lab hires a fleet of sidewalk robots to evaluate their latest model." (2) Emissions buy resources that create an output (dataset, model) which is then **commercially licensed**, fees recycled. HIW-500's "CC BY public release + commercial licensing for more data" is loop 2 verbatim.

### What the companion pages add (site, not whitepaper; captured in the raw file)

- **Lineage:** FrodoBots Lab (2022, brothers Michael and Sam Cho, "gamify robotics data collection") → ET Fugi sidewalk-robot game (Jul 2023, 40+ cities) → 2k-hour dataset used by Berkeley RAIL (May 2024) → Earth Rovers challenge, first at IROS 2024 → Protocol Labs' Benet and Victor join (Feb 2025) → whitepaper (Mar 2025).
- **Traction claimed:** a $5M Grand Challenges fund (Sep 2025); SN/02 SeeSaw phone-video subnet at "4 million tasks" (Jul 2026); research citations of FrodoBots data including MBRA and OmniVLA (Berkeley, Levine/Shah), HPT (MIT), and navigation-scaling work from Tampere, UCLA, PKU. A CoRL 2025 keynote titled "Making the Case for Crypto to the World's Top Robotics Minds."
- The FAQ heading "Why is BitRobot built as a blockchain network?" confirms the substrate the whitepaper only implies.

## Reading it against the wiki

> [!note] It is the adversarial-data problem, formalized — and it moves the problem rather than solving it
> The [crowdsourcing](../concepts/learning/crowdsourced-robot-training-data.md) page's first failure mode is that a contributor paid per accepted unit optimizes *acceptance*, and the filter's criteria become the fraud's specification. VRW is that filter written into a protocol: the **measurement** ("Qualified Miles," scenario counts, teleop hours) is the thing rewarded, validators are the filter, collateral and penalties are the deterrent. Three things the whitepaper does not address: **validators are themselves reward-seeking** and may be the subnet owners; **Goodhart on the measurement** — miles and hours are cheap to inflate and say nothing about novelty or contact-rich content, which is exactly the variation the crowdsourcing page says embedding-based dedup cannot see; and **cryptographic verification is explicitly deferred.** Figure's Index answers the same problem with centralized human analysts auditing at the user level; BitRobot decentralizes the auditors and pays them too.

- **As [mechanism design](../concepts/economics/mechanism-design.md):** the closest thing in the wiki to a full incentive-compatible design for a robot-data market — collateral, penalties, fee sinks, and a delegation-weighted evaluation loop. It is also the first place a robotics document proposes an **AI agent as a governance voter** with its own delegated weight.
- **Against the [industry map](../syntheses/society/robot-ai-industry-map.md):** its "resource asymmetry" figure is the whitepaper's own version of the map's structural-safety argument, and its bet is that a network can out-aggregate any single lab. The evidence so far is navigation data (FrodoBots) and one humanoid dataset (HIW-500); the humanoid-fleet-for-hire and model-evaluation subnets it describes are not yet visible on the site.
- **The IP tension.** §4.4 says emission-funded outputs default *non-commercial*; HIW-500 shipped **CC BY 4.0**. Either HIW-500 was a Foundation/private-subnet output, or the default was relaxed — the whitepaper predates the dataset by fifteen months and the site says "updated as necessary."
- **The strongest idea is the evaluation one**, not the data one. Fleets for statistically meaningful real-world eval are something no dataset marketplace offers and no lab outside the top few has; "an AI lab hires a fleet of sidewalk robots to evaluate their latest model" is the use case the wiki's [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) page would most want to exist.

## Entities mentioned

- [BitRobot](../entities/bitrobot.md) — the subject; [FrodoBots](../entities/frodobots.md) — the origin (Earth Rovers, FrodoBots-2K); Protocol Labs (no page).
- [HIW-500](../entities/hiw-500.md) — a produced output; [Figure](../entities/figure.md) (Index) as the centralized comparison.
- Cited work the wiki holds: [Open X-Embodiment](../entities/open-x-embodiment.md), [π0](../entities/pi-zero.md), [Genesis](../entities/genesis.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [World Labs](../entities/world-labs.md), GAIA-1.

## Concepts touched

- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md), [mechanism design](../concepts/economics/mechanism-design.md), [collectivist AI / AI-as-market](../concepts/economics/collectivist-ai.md).
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md), [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [cross-embodiment](../concepts/learning/soft-prompt-cross-embodiment.md).

## Open questions

- What the fungible network token is, how emissions are denominated, and what has actually been paid to HIW-500's teleoperators — the whitepaper is silent on numbers.
- Whether any subnet has run the evaluation-fleet loop (loop 1) for a third-party lab.
- Validator collusion and measurement Goodharting: is there a published incident or audit?
- Consent for footage from occupied homes (HIW-500) and public sidewalks (ET Fugi) — not in the whitepaper.

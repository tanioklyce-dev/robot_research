---
title: Stanford HAI — AI Index Report 2026
type: source
url: https://aiindex.stanford.edu/report/
pdf_url: https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
doi: https://doi.org/10.48550/arXiv.2606.15708
local_path: raw/ai_index_report_2026.pdf
local_path_revised: raw/ai_index_report_2026_rev_2026-06-29.pdf
author: Stanford Institute for Human-Centered AI (HAI); Co-chairs Yolanda Gil, Raymond Perrault
published: 2026-04
revised: 2026-06-29
ingested: 2026-05-09
rechecked: 2026-08-29
tags: [ai-index, stanford, benchmark, robotics, economy, responsible-ai, vla, humanoid]
---

## Summary

The ninth edition of the Stanford HAI AI Index Report (2026). Comprehensive annual measurement of the global AI field across R&D, technical performance, economy, responsible AI, science, medicine, education, policy, and public opinion. Central framing: AI is scaling faster than the governance and evaluation systems built around it. The gap between capability and the infrastructure to manage it — evaluation frameworks, regulation, workforce adaptation — is the defining tension of 2025–26. For this wiki, the most important sections are §2.7 (Robotics and Autonomous Motion) and the §1.1/§2.1 performance overview showing industry concentration and model convergence.

## Key claims

### AI capability and performance
- Industry produced >90% of notable AI models in 2025 (91.2%); only 2 from academia vs. 93 from industry ([§1.1](../sources/stanford-hai-ai-index-2026.md)). Top orgs 2025: OpenAI (20), Google (14), Alibaba (11), Anthropic (7).
- **Model performance converging at the frontier**: top four providers (Anthropic 1,503; xAI 1,495; Google 1,494; OpenAI 1,481) now clustered within 25 Elo points on the Arena Leaderboard (as of March 2026).
- **US–China gap effectively closed**: as of March 2026, top US model (Claude Opus 4.6, 1,503) leads top Chinese model (Dola-Seed-2.0-Preview, 1,464) by just 2.7%; gap has fluctuated between near parity and low single digits since early 2025.
- **Open vs closed**: top closed model leads open model (GLM-5, 1,454) by 3.4%; six of the top ten Arena models are now closed.
- SWE-bench Verified rose from ~60% to near 100% in a single year. GPQA Diamond, MMMU, AIME all at or above human baseline by 2025.
- **Jagged frontier**: Gemini Deep Think scored 35 points (gold) at the 2025 IMO; same-era models read analog clocks correctly only 50.6% of the time (ClockBench).
- **Benchmark reliability concerns**: 2–42% invalid question rates across nine widely-used benchmarks (MMLU Math 2%; GSM8K 42%). Reporting from frontier labs on bias and environmental impact is declining.

### Robotics (§2.7) — most relevant to this wiki
- **RLBench**: EquAct reaches **89.4% success** on the 18-task controlled-simulation subset (as of Jan 2026). Progress from ~48% in 2022. Benchmark tests short-horizon tasks in a controlled simulation environment.
- **[BEHAVIOR-1K](../entities/behavior-benchmark.md)** (real household environments): 2025 Challenge top team (Robot Learning Collective) Q-score 26%; **full task success rate only 12.4%**. "Reliably executing household tasks in realistic environments is still beyond current capabilities."
- **ResponsibleRobotBench**: 23 multi-stage tasks with electrical, fire/chemical, and human hazards. GPT-4o best at safe success rate (SSR) of 0.64; even top model fails >⅓ of tasks safely.
- **Humanoid landscape (2025–26)**: rapid growth in hardware availability and investment, not widespread deployment. Figure 02 spent 11 months at BMW plant: 1,250+ runtime hours, 90,000+ parts loaded across 30,000+ vehicles. Unitree: R1 from $4,900, G1 from $13,500. AgiBot: ~100 teleoperated humanoids running up to 17 hr/day, ~10,000 units manufactured. 1X NEO waitlist open for $20,000 US deliveries in 2026.
- **Humanoid landscape table (§2.7) — corrected in the June revision.** The April edition's vendor table listed **Toyota Research Institute** as *Japan / teleoperated systems / retail, logistics / "focus on teleoperated manipulation."* The 2026-06-29 revision replaces that row with *United States / various / research / "**diffusion policy and large behavior models**."* The original row was wrong on country, product, sector, and research program — it read as a conflation with the Japanese teleop vendors listed adjacent to it (SoftBank Robotics, Telexistence). This wiki's [TRI](../entities/tri.md) page, built from primaries ([Diffusion Policy](diffusion-policy-paper.md), [UMI](umi-paper.md), [TRI LBM](tri-lbm-paper.md)), never carried the error; the corrected AI Index row now agrees with it.
- **Physical AI and VLAs**: Physical Intelligence's π0 (2024) and π0.6 (2025) demonstrate cross-platform generalization (e.g. laundry folding without task-specific retraining). NVIDIA GR00T and Gemini Robotics take a similar direction. Data is the biggest constraint: every robot training example requires a physical robot or high-fidelity sim. World Foundation Models (Cosmos) address this by generating synthetic physics data. "VLA technology remains at the research stage, and the gap between what these models can do in a controlled setting and what they can handle in the real world is still wide."
- **Autonomous vehicles**: Waymo operating ~2,500 fully autonomous robotaxis; ~450,000 weekly trips across 5 US cities. Baidu Apollo Go: ~11 million fully driverless rides in 2025, 175% YoY increase.

### Economy and investment (§4)
- US private AI investment: **$285.9 billion in 2025**, more than 23× China's $12.4B (private figures; China's total spending with government guidance funds is likely substantially higher).
- US: 1,953 newly funded AI companies in 2025, >10× the next closest country.
- Number of AI researchers/developers moving to the US dropped **89% since 2017**, including 80% decline in the last year alone.
- Gen AI population adoption: **53%** within 3 years — faster than PC or internet adoption. US ranks 24th globally at 28.3%; Singapore at 61%, **UAE at 64%** (April edition's prose said 54%; corrected in the June revision — see [Edition history](#edition-history)). Figure 4.3.10's country diffusion numbers are **Microsoft telemetry**, not survey estimates — the April prose mislabelled them.
- Estimated consumer value of gen AI tools to US consumers: **$172 billion annually** by early 2026; median value per user tripled between 2025 and 2026.
- Organizational adoption: 88%.

### Responsible AI (§3)
- Documented AI incidents rose to **362 in 2025**, up from 233 in 2024.
- Responsible AI benchmark reporting from frontier labs remains "spotty."
- Recent research found that improving one responsible AI dimension (e.g. safety) can degrade another (e.g. accuracy).

### Infrastructure and compute (§1.2–1.4)
- Global AI compute capacity: **17.1 million H100-equivalents** (3.3× per year since 2022). NVIDIA accounts for >60% of total.
- US: 5,427 data centers, >10× any other country. TSMC fabricates nearly every leading AI chip.
- AI data center power capacity rose to **29.6 GW** (comparable to New York state at peak demand).
- Grok 4 estimated training emissions: **72,816 tons CO₂ equivalent**. Annual GPT-4o inference water use may exceed drinking-water needs of 1.2 million people.

## Entities mentioned

- [Stanford HAI](../entities/stanford-hai.md) — publisher; also author of the 2026 [world-model policy brief](hai-world-model-spatial-intelligence-brief.md).
- [Anthropic](../entities/anthropic.md) — Arena 1,503 (top closed model); 7 notable models in 2025.
- [NVIDIA](../entities/nvidia.md) — >60% of global AI compute; GR00T VLA mentioned.
- [Google DeepMind](../entities/google-deepmind.md) — 14 notable models; Veo 3 video generation; Gemini Robotics VLA.
- [Meta FAIR](../entities/meta-fair.md) — Arena 1,335 (flattened since early 2025).
- [Figure](../entities/figure.md) — Figure 02 at BMW: 1,250+ runtime hours, 90k+ parts, 30k vehicles.
- [1X NEO](../entities/1x-neo.md) — $20,000 household humanoid; waitlist open for 2026 US deliveries; backed by OpenAI.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — listed in Physical AI / VLA highlight.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — cited as example of World Foundation Model generating synthetic robot training data.
- [Physical Intelligence](../entities/physical-intelligence.md) — π0 (2024) and π0.6 (2025) VLAs demonstrating cross-platform generalization without task-specific retraining.
- [Toyota Research Institute](../entities/tri.md) — miscategorised in the April humanoid table; corrected to US / research / diffusion policy + LBMs in the June revision.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — π0/π0.6, GR00T, Gemini Robotics; VLA assessed as still research-stage; data bottleneck framing.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — 89.4% RLBench (sim) vs 12.4% BEHAVIOR-1K full task success (real household); canonical gap number.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — BEHAVIOR-1K 12.4% household task success; humanoid landscape for home use.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — AI incidents 362 (up from 233); responsible AI not keeping pace with capability; safety–accuracy tradeoff.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — World Foundation Models (Cosmos) as synthetic data source for robot training.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — AI agents on OSWorld 12% → 66.3%; still fail ~1 in 3 on structured benchmarks.

## Edition history

The URL `hai.stanford.edu/assets/files/ai_index_report_2026.pdf` serves a **revised** PDF as of **2026-06-29** (InDesign 21.4 export; 37.9 MB) replacing the **2026-04-28** export (21.3; 24.9 MB) that was ingested on 2026-05-09. Both are kept in `raw/`; the original is not overwritten. Page count is identical (425) and the size jump is image re-export, not content.

A full page-by-page text diff of the two exports found **four** substantive changes — everything else is kerning/typesetting noise:

| # | Location | April edition | June revision |
|---|---|---|---|
| 1 | §2.7 humanoid vendor table | Toyota Research Institute — Japan / teleoperated systems / retail, logistics | **United States / various / research / diffusion policy and large behavior models** |
| 2 | Exec. summary + §4.3 prose | UAE gen-AI adoption **54%** | **64%** (the April *chart* already read 64.00% — prose and figure disagreed) |
| 3 | §4.3, Figure 4.3.10 | "survey-based estimates of AI usage across countries" | "**Microsoft's telemetry data** of AI usage across countries" |
| 4 | How to Cite (p. 5) | no DOI | adds `https://doi.org/10.48550/arXiv.2606.15708` |

> [!note] What this changes for the wiki
> Nothing in the robotics numbers this wiki leans on. **RLBench 89.4%, [BEHAVIOR-1K](../entities/behavior-benchmark.md) 12.4%, ResponsibleRobotBench 0.64, the Figure 02 BMW hours, Unitree/AgiBot/1X figures, Waymo and Apollo Go ride counts are byte-identical across the two exports** — the canonical 89.4/12.4 gap figure cited in the [syntheses](../index.md) is unaffected. The corrections land on (1) a vendor table row and (2) the diffusion statistics.

> [!warning] Methodology correction worth carrying
> Change #3 is the one with teeth. Country-level "AI adoption" in Figure 4.3.10 is **Microsoft product telemetry**, not a population survey. Telemetry measures accounts touching Microsoft AI surfaces, so it is sensitive to Microsoft's market share per country and is not interchangeable with survey-based adoption rates. Cite these numbers as *Microsoft-telemetry diffusion*, not *population adoption*.

> [!note] Confirmation, not correction, for [TRI](../entities/tri.md)
> Change #1 is a case where the wiki's independently-built entity page was right and a heavily-cited secondary aggregator was wrong for two months. The AI Index is a *tertiary* source on individual vendors — it aggregates. Where this wiki holds primaries (TRI, Physical Intelligence, 1X, Figure), prefer them over the AI Index's landscape tables.

## Open questions
- The report covers physical AI at a high level; deeper numbers (π0/π0.6 success rates, Gemini Robotics eval specifics) require primary sources from Physical Intelligence and Google.
- Responsible AI benchmark numbers are aggregate; specific frontier labs' disclosure practices would need primary-source system cards to fill in.
- BEHAVIOR-1K challenge data: top team 12.4% full success — does this hold for assistive tasks specifically, or are some household task categories harder than others?

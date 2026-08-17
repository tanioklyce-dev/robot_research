---
title: Wiki Backlog — deferred lint items & knowledge gaps
type: meta
created: 2026-07-04
updated: 2026-08-16
tags: [backlog, lint, todo, knowledge-gaps]
---

# Wiki Backlog

Deferred maintenance items and knowledge gaps surfaced during lint passes but not yet actioned. Pick these up in a future session. Newest section first. When an item is done, strike it and note the commit/date, or delete it.

## [2026-08-16b] Literature-search correction — three "nobody has done it" claims were wrong

*Prompted by a direct challenge to the claim that the runtime thread's remaining gaps were "buildable, not readable." A targeted search falsified three of four in one pass. **Lesson: in a fast-moving area, "no ingested source does X" and "nobody does X" are different claims, and the wiki must write the first.***

- [ ] **Ingest queue, VLA-era runtime monitoring** — the claim "no monitor runs on a generalist policy" is false. **SAFE** (Gu, Ju, Sun, Gilitschenski, **Nishimura**, **Itkina**, Shkurti; **NeurIPS 2025**, arXiv 2506.09937) monitors **OpenVLA, π₀, π₀-FAST** from VLA internal features with conformal calibration and generalizes to unseen tasks — and shares two authors with [FAIL-Detect](sources/fail-detect-paper.md). Then **VLA-FAIL** (2606.21386), **Hide-and-Seek in Trajectories** (2605.30834, critiques SAFE's labelling), **VLAConf** (2605.29605), **ActProbe** (2606.08508, STAC-like signal without the sampling cost). **SAFE first.**
- [ ] **Ingest Latent Safety Filters** (2502.00935, Nakamura & Bajcsy) + **Uncertainty-aware** (2505.00779) + **partial-observability** follow-up (2510.06492) — HJ reachability in a world model's latent space; the answer to "every safety layer assumes perception it does not do." Same lab as [FOREWARN](sources/forewarn-paper.md), which makes the pairing natural.
- [ ] **Ingest Rewind-IL** (2604.16683) — closes **detection → recovery** with conformal-calibrated chunk-consistency detection plus VLM-selected rewind checkpoints, on real hardware. Falsifies "detection is not recovery" as a field-level claim and answers the "cross the two monitor designs" item.
- [ ] **Read Agia's dissertation, *Deployment-Time Reliability of Learned Robot Policies*** (Stanford, 2026-03, 182 pp) — [Sentinel](sources/sentinel-paper.md)'s first author, with a different three-way cut: monitoring / **policy interpretability via influence functions** / long-horizon coordination. **The wiki has zero coverage of tracing a runtime failure back to the training data that caused it.**
- [ ] **Check the cross-layer survey** (2606.05660) against [the synthesis](syntheses/platforms/prevention-detection-intervention.md) — it organizes safety by planning-time / policy-time / execution-time and argues risks *accumulate* across layers. Different cut, same instinct; the synthesis should cite it rather than imply novelty.
- [ ] **The one surviving claim**: that a safety filter's braking is indistinguishable to a progress monitor from a stalled policy. Not falsified by search, but **low confidence** — the neighbours (over-conservative filters under partial observability; monitors firing on benign situations) are well documented separately. Still the cheapest thing to build.

## [2026-08-16] GCS + the constraint-envelope safety layer — open threads

*The "did GCS reach deployment?" question is closed ([Dexai Robotics](entities/dexai-robotics.md), production, PRM displaced). These are the threads it opened.*

- [ ] **The deployment evidence is two years stale.** Both sources are from early 2024 ([seminar](sources/tedrake-gcs-foundation-models-talk.md) 2024-04-07, [ARM](sources/arm-institute-gcs-dexai-project.md) 2024-02-26). Unknown: whether Dexai still runs GCS, whether any second adopter exists, what became of the five ARM modules (`IrisBuilder`, `WarmGcsPlanner` are the interesting two). **Highest-value single check** — one datapoint decides whether GCS is a niche win or a spreading one.
- [ ] **Every extension in the seminar is described from slides, and none is ingested.** Named work, presumably published by now: geodesic-convexity GCS (planning on manifolds), analytical-IK regions for task-space constraints, visibility-graph **minimum clique cover** region generation, and the **SDP/spectrahedron** contact formulation. Also still uningested from the earlier session: **Marcucci's shortest-paths-in-GCS framework paper**, which both the planner paper and this wiki treat as a black box.
- [ ] **The composition nobody has documented**: a learned generalist policy pruning a planner's graph (Tedrake's own answer to "the graph gets too big for dexterous hands"). If a real instance exists anywhere, it belongs in this wiki — it is the concrete form of the planning-and-learning argument the whole seminar makes.
- [x] ~~**Marcucci's shortest-paths-in-GCS framework paper.**~~ — **done 2026-08-16**: [ingested](sources/shortest-paths-in-graphs-of-convex-sets-paper.md). It reframes GCS as an optimization technique whose target application is **hybrid/PWA control**, not motion planning.
- [ ] **Hybrid MPC via GCS, today.** The framework paper's 7.1 s on a 30-step PWA problem is a planning result. Closing the loop needs warm starts (Marcucci & Tedrake 2021, uningested) or heuristic search over the graph (`GCS*`, implicit graphs, uningested). Where has this line got to, and does anyone run it at control rates?
- [ ] **Appendix A is an unopened door**: TSP-with-neighborhoods, MST-with-neighborhoods and friends in high dimensions via the same perspective/set-based relaxation. Offered, never evaluated. If it works, GCS's reach is far wider than robotics.
- [ ] **No ingested source on IRIS** — the region-generation half of every GCS pipeline is still covered only secondhand (IRIS, IRIS-NP, C-IRIS, and the visibility-graph clique-cover successors).
- [x] ~~**The CBF upgrade to the constrained-QP safety layer**~~ — **done 2026-08-16**: [OSCBF ingested](sources/oscbf-paper.md). It supplies the forward-invariance guarantee the deployed envelope lacks, plus **task consistency** (filter the task output, not the control input) and 168 constraints at ~3 kHz. Two caveats carried onto the pages: the relaxed QP *"enforces (but does not guarantee) safety"* once many constraints conflict, and obstacles are supplied rather than perceived.
- [x] ~~**Nobody has run a learned policy through a CBF filter.**~~ — **closed 2026-08-16, and the claim was wrong in the direction that matters**: it was true of *this corpus*, not of the field. [PACS](sources/pacs-paper.md) (ICRA 2026) measured it. The answer: a reactive CBF filter costs a diffusion policy **almost all of its task success** (0.04 avg on robomimic vs 0.70 unfiltered), because it pushes the policy off the demonstration manifold; a **path-consistent** filter costs ~nothing (0.72). Filed on [safety filters for learned policies](concepts/robotics/safety-filters.md). Lesson for future "nobody has done X" notes: scope them to the corpus explicitly, then go check the field.
- [ ] **Static-obstacle path consistency.** [PACS](sources/pacs-paper.md) handles *dynamic* hazards and defers *"(semi-)static obstacles via constraint-aware online replanning"*; [OSCBF](sources/oscbf-paper.md) handles hundreds of static collision pairs and never faces distribution shift. **Nothing covers both**, and a home robot needs both.
- [x] ~~**The runtime-monitoring cluster PACS cites is entirely uningested**~~ — **two of three done 2026-08-16**: [Sentinel](sources/sentinel-paper.md) (CoRL 2024) and [FAIL-Detect](sources/fail-detect-paper.md) (RSS 2025, TRI), anchoring the new [runtime failure detection](concepts/robotics/runtime-failure-detection.md) page. Still uningested: **Römer et al., NeurIPS 2025 — failure *prediction* at runtime**, which is the one thing both ingested papers explicitly do not do (they detect as failures occur, not before).
- [x] ~~**Römer et al., NeurIPS 2025 — failure prediction at runtime**~~ — **done 2026-08-16**: [FIPER](sources/fiper-paper.md) ingested; the cluster is complete. Contributes **TWA** (a metric that rewards early prediction) and the Success-OOD-vs-Fail-ID protocol.
- [ ] **Build the composition — and instrument the interfaces first.** The synthesis names a hazard nobody has hit: **a safety filter braking for a human is indistinguishable, to a progress monitor, from a stalled policy**, and a steered policy looks like a policy in trouble to both monitors. Any real stack needs filters and steerers to *announce* their interventions. **This is a design proposal worth writing, not an ingest** — and cheap, because it is an interface, not an algorithm.
- [ ] **Nobody has crossed the two runtime-monitoring designs.** [Sentinel](sources/sentinel-paper.md) contributes *what to measure* (a failure taxonomy + the action-chunk-overlap signal); [FAIL-Detect](sources/fail-detect-paper.md) contributes *how to threshold* (a time-varying conformal band) and a cheaper score. **STAC as a score inside FAIL-Detect's stage-2 band** is the obvious experiment and neither paper runs it.
- [x] ~~**Neither monitor has been run on a generalist policy.**~~ — **wrong, corrected 2026-08-16**: true of the ingested monitors, false of the field (SAFE, NeurIPS 2025). See the correction section above. All experiments are single-task diffusion/flow policies. [LBMs](concepts/learning/large-behavior-models.md) and [VLAs](concepts/learning/vla-models.md) are untested, and STAC in particular needs cheap batch sampling that a large autoregressive VLA does not offer. TRI has both halves in the building.
- [x] ~~**Detection is not recovery — the gap is now named on three pages.**~~ — **wrong at field level, corrected 2026-08-16**: Rewind-IL (2604.16683) does detection + rewind-to-checkpoint recovery on real hardware. The gap remains real for the *ingested* sources and for filter-inclusive loops. Safety filters stop the arm; monitors raise a flag; nothing says what happens next (handoff, retry, replan, safe park). Same shape as the [empty execution rail](syntheses/agents/guardrails-for-robot-agents.md) on the agent side, and the `interrupt()` design-proposal item below is the cheapest concrete move on it.
- [ ] **Should "safe success" be retrofitted to the wiki's benchmark coverage?** Every success rate here was measured without a safety constraint being checked. PACS shows a policy family at **0.79 task success / 0.00 safe success**. Worth a note on the pages that report success rates near humans, and a standing question at ingest: *was anything being enforced while this number was collected?*
- [ ] **Perception is the shared blocker for both safety layers.** Keep-out boxes and sphere decompositions are authored offline on both coasts. Real-time perception → constraint geometry is the piece that would make either usable in an unstructured home.
- [ ] **Auto-caption attribution debt.** The seminar page deliberately declines to assert surnames for the students whose results it describes. If the follow-on papers get ingested, the credit lines can be repaired from the author lists.

## [2026-08-13h] Niantic Spatial + LingBot-Map — a whole tradition was missing

*Two ingests that exposed a structural gap rather than filling a named one.*

### The gap

- [x] **The wiki covered world models extensively and had no page for SLAM, visual relocalization, Gaussian splatting, or NeRF** — despite the [XLeRobot plan](syntheses/projects/xlerobot-nav-manip-teleop-bringup.md)'s entire navigation leg being [RTAB-Map](entities/rtab-map.md) + [Nav2](entities/nav2.md). Opened [visual relocalization and mapping](concepts/robotics/visual-relocalization-and-mapping.md). **World models ask *what happens if I act*; this tradition asks *where am I and what shape is this place*.**
- [ ] **Still uncovered inside it, named honestly on that page**: **NeRF**, **Gaussian splatting as a method** (not a Niantic product feature), **ORB-SLAM / visual-inertial odometry**, **factor graphs as a formalism**, **Frank Dellaert**'s lineage. And [GTSAM](entities/gtsam.md) + [RTAB-Map](entities/rtab-map.md) remain **stubs with no primary source ingested for either** — a real hole given both are load-bearing for the active project plan.

### Follow-ups

- [ ] **LingBot-Map paper** (arXiv 2604.14141) — every quantitative claim lives there; the README publishes no accuracy table. KITTI and Oxford Spires numbers unread.
- [ ] **What hardware gives LingBot-Map ~20 FPS?** Unstated, and it decides whether it is deployable on a robot or only in a datacentre. Same omission the [control-rate ladder](syntheses/platforms/control-rate-ladder.md) keeps finding.
- [ ] **Can LingBot-Map relocalize against a prior map?** Not described — and that is exactly what RTAB-Map's localization-only mode gives the XLeRobot plan. Until answered, **RTAB-Map stays the right choice** because it is the only option with a measured deployment on comparable hardware.
- [ ] **Primary sources for LingBot-VLA and LingBot-World** — the two [Robbyant](entities/robbyant.md) layers known only secondhand. LingBot-World placed **5th of 10 on WorldRoamBench and collapsed on physics (47.32)**, which makes its primary worth reading.
- [ ] **What is the Large Geospatial Model, technically?** [Niantic](entities/niantic-spatial.md) names it as the foundation of everything and never describes it.
- [ ] **Ingest "On the Limits of Pseudo Ground Truth in Visual Camera Re-Localisation"** (Brachmann et al., ICCV 2021) — **a fourth independent instance of the wiki's measurement thread**, and the earliest: LIBERO-PRO says the *tasks* are wrong, VP² says the *metrics* are wrong, the audit says the *sample sizes* are wrong, this says **the labels are wrong**. Four subfields, ~5 years, no cross-citation.
- [ ] **monodepth2** (Godard et al., ICCV 2019) — the ancestor of a great deal of cheap-robot depth perception, no page here.
- [ ] **Niantic's accessibility strand** (NaviNote, *Don't Look Now*) — CHI/UIST work on spatial annotation for blind and low-vision navigation, adjacent to the wiki's [assistive robotics](concepts/robotics/assistive-robotics.md) coverage and entirely uningested.

## [2026-08-13g] LangChain + UME ingested; the lint's gap check was itself defective

### The lint defect, fixed

- [x] **LangChain appeared in 12 pages and was never flagged** — above any sane threshold. Cause: the §6 "frequently mentioned, no page" check was a **hand-written candidate list**, so it found exactly what it was told to look for and everything off the list was invisible. **Now automated** as check #10 in [`scripts/lint_wiki.py`](../scripts/lint_wiki.py).
- Check #10 is **deliberately high-precision, low-recall**: it keeps only terms that *look* like proper nouns (internal capitals, a hyphen, or multi-word), skips anything whose slug is a substring of an existing page, and filters licence strings and dates. **It would have caught LangChain.** It will **not** catch ordinary-looking single words — Drake, Zenoh, Moondream — which stay a human-pass problem. Precision over recall on purpose: a noisy check gets ignored, which is how gaps persist in the first place.

### Real leads it surfaced immediately

- [ ] **OpenAI — 48 pages, no entity page.** The most-cited organization in the wiki without one.
- [ ] **PyTorch — 47 pages, no page.** The substrate under every model here.
- [ ] **SIGReg — 47 pages**, from the [LeJEPA](sources/lejepa-paper.md) line; a named method with no page.
- Triaged as noise: `VLAs`/`VLMs` (plurals of concepts), `Joint-Embedding Predictive` (fragment of JEPA's expansion), `SO-100`/`SO-101` (covered by [SO-ARM101](entities/so-arm101.md)), `GR00T N1` (covered by [GR00T](entities/nvidia-groot.md)).

### UME — the position-only gap now has a researched answer

- [x] **[UME](entities/ume.md)** ingested ([project page](sources/ume-project-page.md)) — **$1,900** torque-feedback exoskeleton, records joint torques, contact-rich policies from **26–157 demos each**.
- [x] ~~**Ingest the paper (arXiv 2606.14218)**~~ — **done 2026-08-13**: [UME paper](sources/ume-paper.md). Answers below.
- [x] ~~**Do UME's learned policies consume torque as an input?**~~ — **yes**, explicitly: the No-torque baseline is *"the same dataset without including the torque modality to compute the proprioception embedding."* Torque is an observation channel, not just better demonstrations.
- [x] ~~**Does force feedback buy data efficiency or operator comfort?**~~ — **both, measured separately.** Policy side: torque ablation drops box flipping **0.85 → 0.00** and box pushing **0.90 → 0.50**. Operator side: **3.3× demonstrations per minute**, at 71% of unaided human speed.
- [ ] **The comparison that would settle the paradigm trade is missing: UME vs UMI on *collection throughput*.** UME's 3.3× is measured against torque-disabled UME, not against UMI — and UME weighs **12 kg** against UMI's handheld gripper. Better data versus easier data at scale is unresolved, and it is the question a builder actually faces.
- [ ] **Does torque help long-horizon mobile tasks at all?** Fridge retrieval 0.95 vs 0.90 at n=20 is indistinguishable (p=1.00). Either the task is not force-mediated enough, or the effect is real and n=20 cannot see it. A larger n settles it.
- [ ] **No cross-embodiment *policy* transfer tested** — universal *teleoperation* is shown, policy transfer is not. And **real-Franka results are simulation-only** pending hardware delivery.
- [ ] **Nothing bridges $1,900 to the $660 tier.** [OpenFT](entities/openft-sensor.md) is the only cheaper route and is unmaintained, unbenchmarked, and unlicensed.
- [ ] **Is WowRobo's OpenArm 1.0 the same lineage as [Sensori](entities/sensori-robotics.md)'s OpenArm+?** Two unrelated platforms sourcing "OpenArm" hints at a standard consolidating above the SO-ARM101 tier.

## [2026-08-13f] LangGraph ingested — one gap closed, two opened

- [x] **LangGraph** ingested ([source](sources/langgraph.md)); entity upgraded from secondhand and **a wrong inference of mine corrected**. DimOS uses the **ReAct tool-calling loop only** — no checkpointing, no interrupts, no custom graph, no memory across a crash.
- [ ] **`interrupt()` as the missing execution rail.** The [guardrails synthesis](syntheses/agents/guardrails-for-robot-agents.md) says the rail ships empty; LangGraph's human-in-the-loop interrupt is a ready-made mechanism, present in DimOS's dependency tree and unused. **This is a design proposal worth writing, not an ingest** — and it is cheap, because the framework is already there.
- [ ] **Does *any* robot stack use durable execution?** DimOS does not. If none does, the finding strengthens from "DimOS hasn't bothered" to "the category hasn't needed it," which is a claim about maturity rather than about one team.
- [ ] **LangChain itself is uncovered** — the substrate under LangGraph, and the source of `create_agent`.

## [2026-08-13e] Lint punch list — WORKED

*All mechanical items closed; the one judgment item resolved by decision. Reproducible from now on: **`python3 scripts/lint_wiki.py`** (add `--fix-source-counts` to re-derive counts).*

### Done

- [x] **§3 stale claims** — [LIBERO](entities/libero.md)'s "wiki's highest LIBERO averages" now reads as a tie with [X-VLA](entities/x-vla.md) at 98.1 and points at the [audit](syntheses/platforms/vla-success-rate-audit.md); [deployability landscape](syntheses/platforms/vla-deployability-landscape.md) retitled to **five axes** with the fifth explained; [TurboVLA](entities/turbovla.md)'s "four axes" reference updated.
- [x] **§4** — `welchlabs-lecun-1b-bet-against-llms-part2` added to the index; `ingested: 2026-07-27` added to `libero-pro-paper` and `roboarena-paper`. **Index coverage and schema are now 100%.**
- [x] **§5** — 11 stale `_stub_` markers cleared (`genie-3`, `pi-zero-6`, `rt-2`, `agilex-piper`, `openvla`, `open-x-embodiment`, `bagel`, `octo`, `smolvlm`, `gemma3`, …).
- [x] **§6 top three ingested** — **[Drake](entities/drake.md)** (+ [source page](sources/drake-documentation.md)), **[RDT-1B](entities/rdt.md)**, **[Zenoh](entities/zenoh.md)**, all wired into the pages that were citing them bare.
- [x] **§2 decided: `sources:` is now DERIVED**, regenerated by the script from inbound source-page links. 169 pages corrected.
- [x] **§1 partially** — 9 unambiguous missing back-links repaired (a source page named for an entity that failed to link it: `voyager`, `saycan`, `dinov3`, `inner-monologue`, `language-to-rewards`, `ok-robot`, `rosetta`, `tri`, `smwm`).

### The decision, recorded

**`sources:` now means "distinct source pages that markdown-link to this page."** That makes it derivable and undriftable — but it is a **link-hygiene measure and a lower bound on real provenance**: a source discussing an entity in prose without linking it does not count. So **`sources: 0` means "no ingested source links here," not "undocumented."** The fix is the back-link, never the number.

### Still open — the one item that needs judgment, not automation

- [ ] **~306 one-way citations remain.** An entity/concept cites a source; that source's `## Entities mentioned` omits it. **This is a lead list, not a defect list** — the right question per pair is *"does this source actually discuss this entity?"*, and for many the answer is no (the entity cites the source for a passing claim). Auto-adding all 306 would turn source pages into link dumps. Work them opportunistically: when an ingest touches a source page, repair its back-links then.
- [ ] Seven entity pages now read **`sources: 0`** — including **[Tesla Optimus](entities/tesla-optimus.md)**. Not a counting bug: nothing ingested links to them, so their coverage is entirely secondhand from other entity pages. That is a **provenance finding worth acting on** — either cite a real source or mark them as uncited.
- [x] ~~**§6 remainder**~~ — **closed 2026-08-13**: [Zenoh](entities/zenoh.md) properly ingested ([source](sources/zenoh-io.md)), plus [RTAB-Map](entities/rtab-map.md), [GTSAM](entities/gtsam.md), [CuRobo](entities/curobo.md), [LangGraph](entities/langgraph.md), [DP3](entities/dp3.md), and the [LIBERO tie cluster](entities/libero-tie-models.md) holding page. **Moondream remains** — the only §6 item left, and the thinnest.
- [x] ~~**Moondream**~~ — **done 2026-08-13**: [source](sources/moondream-ai.md) + [entity](entities/moondream.md). **§6 is now fully closed.** Brought in the wiki's only small-VLM edge-latency ladder (Thor 246 ms, AGX Orin 514 ms) and a second independent instance of VLM **pointing** beside [Molmo](entities/molmo.md).
- [ ] **Reproduce Moondream's Qwen comparison.** Its headline "47× faster than GPT-5.4 Mini" compares local inference to a network API; the honest row is **Qwen 3.5 4B + vLLM at 73 ms vs 59 ms — a 21% edge**. Vendor-measured, never independently replicated, and the ladder is a **Photon** result on Apache-2.0 weights. Running Moondream 3.1 under vLLM/llama.cpp on the same hardware is the missing control.
- [ ] **Nothing below AGX Orin is published** on that ladder, and this wiki's low-cost platforms run **Orin NX 16 GB / Orin Nano 8 GB**. Same shape as the standing "measure an LLM-free VLA on a Jetson" item — the cheap tier is unmeasured by everyone.
- [ ] **Primary ingests wanted for the new stubs.** [RTAB-Map](entities/rtab-map.md) and [GTSAM](entities/gtsam.md) are at `sources: 0` — documented only from other pages' methods sections, and both are now load-bearing for the [XLeRobot bring-up plan](syntheses/projects/xlerobot-nav-manip-teleop-bringup.md). Highest value in the [tie cluster](entities/libero-tie-models.md): **MemoryVLA** (held the 7 B Simpler-WidowX SOTA that a 0.9 B model beat by 23.9 pts) and **FLOWER** (holds CALVIN 4.53, the one benchmark X-VLA lost).

---

## [2026-08-13d] FULL WIKI LINT — punch list

*Automated pass over **940 pages** (385 sources / 389 entities / 81 concepts / 79 syntheses). Nothing auto-fixed, per the lint workflow. Ordered by value.*

### Clean — no action needed

**Broken internal links: 0** · **Orphan pages: 0** · **Duplicate titles: 0** · **Date sanity: 0** (no `updated` before `created`, no future dates) · **Obsidian wikilinks: 0 real** (3 hits are `overview.md`/`log.md` *documenting* the banned syntax) · **Schema conformance: 2 issues in 940 pages.** The structural discipline is holding.

### 1. The systemic one — citations are one-directional

- [ ] **325 pairs where an entity/concept cites a source page and that source page does not cite it back**, spread over **172 entity/concept pages and 149 source pages**. The schema calls for both directions: source pages carry `## Entities mentioned`, entity pages carry `## Mentioned in`. In practice the entity→source direction is maintained and the source→entity direction rots, because ingests add entity links to new sources but rarely revisit *old* sources when a new entity page is created.
- Worst source pages (thinnest `Entities mentioned` relative to who cites them): `libero-pro-paper` (13), `computational-life-self-replicating-programs-paper` (10), `cap-x-paper` (8), `waddle-labs-introducing-waddle` (8), `anthropic-how-claude-performs-on-robotics-tasks` (7), `aspire-paper` (7), `leworldmodel-paper` (7).
- Worst entity/concept pages: `optimal-control` (8), `energy-based-models` (7), `ai-red-teaming` (7), `physical-intelligence` (7), `pi-zero-5` (7).
- **This subsumes the `sources:` count item below** — see §2.

### 2. `sources:` counts — 322/470 exact, and the errors are a *symptom*

- [ ] **129 understated, 19 overstated**, 322 exact. Understatement is benign drift (a new source cites an old page; the count isn't bumped). Worst: `vla-models` 81→101, `google-deepmind` 16→32, `control-abstraction-levels` 4→19, `imitation-learning` 65→78, `llm-agent-architecture` 43→55.
- [ ] **The 19 overstatements are the interesting ones, and they are not counting errors.** `voyager` claims 3 with **0** inbound source links — but its body *does* cite 4 source pages; none link back. Same shape for `inner-monologue`, `language-to-rewards`, `saycan`, `smwm`. **The counts are roughly right; the back-links are missing.** Fixing §1 fixes most of this.
- Decide before fixing: is `sources:` worth maintaining by hand at all, or should it be **derived** from inbound source links at lint time? A derived count cannot drift.

### 3. Stale claims (specific, verified)

- [ ] **`entities/libero.md:71`** — MolmoAct2 called *"the wiki's highest LIBERO averages."* **[X-VLA](entities/x-vla.md) now ties it at 98.1**, and the [audit](syntheses/platforms/vla-success-rate-audit.md) holds that any ranking inside the tie is unsupportable. This is exactly the phrasing the audit corrected once before.
- [ ] **`syntheses/platforms/vla-deployability-landscape.md`** — the page *title* still says "the four axes" while [index.md](index.md) records that TurboVLA exposed a **fifth**. `entities/turbovla.md` repeats "the four axes" too. Retitle or add the fifth explicitly.
- [x] ~~"four action-head families" is stale~~ — **not a defect**: [llm-free-vla](concepts/learning/llm-free-vla.md) explicitly positions itself as orthogonal, and the other "four families" hits are the *world-model* taxonomy, a different thing. Closing the 2026-08-04 backlog item.

### 4. Index and schema

- [ ] **1 page missing from `index.md`**: `sources/welchlabs-lecun-1b-bet-against-llms-part2.md`. (939/940 coverage.)
- [ ] **2 source pages missing `ingested:`** — `libero-pro-paper.md`, `roboarena-paper.md`.

### 5. Stub markers that outlived their pages

- [ ] **10 pages marked `_stub_` in the index but >45 lines**: `genie-3` (70), `pi-zero-6` (70), `rt-2` (63), `agilex-piper` (56), `openvla` (56), `open-x-embodiment` (52), `bagel` (50), `octo` (49), `smolvlm` (47), `gemma3` (46). `rt-2` and `agilex-piper` were both substantially expanded since being marked. (15 stubs are correctly marked at <25 lines.)

### 6. Knowledge gaps — frequently mentioned, no page

Ranked by how many non-index pages mention them:

- [ ] **Drake (16 pages)** — the biggest single gap. It is the simulator/planner under [TRI](entities/tri.md)'s entire [LBM](concepts/learning/large-behavior-models.md) line, appears in [UMI](entities/umi.md), [Russ Tedrake](entities/russ-tedrake.md), [DimOS](entities/dimos.md) manipulation, [xArm 7](entities/xarm-7.md), and the simulator syntheses. The wiki has the people and the products but not the tool.
- [ ] **RDT / RDT-1B (12)** — a 1 B bimanual diffusion VLA, a baseline in [RoboTwin 2.0](entities/robotwin.md), [RoboMIND](entities/robomind.md), and [X-VLA](entities/x-vla.md). Cited constantly, never described.
- [ ] **Zenoh (12)** — [DimOS](entities/dimos.md)'s reliable transport and a live [ROS 2](entities/ros2.md) alternative in the ros2-mcp-server work.
- [ ] **LangGraph (9)** — the agent framework under DimOS's `McpClient`.
- [ ] **The RoboTwin baseline cluster** — DP3 (4), BAKU (5), MemoryVLA (4), CogVLA (4), VLA-Adapter (5), FLOWER (3). Several sit *inside* the LIBERO tie the wiki reasons about; describing them is cheap and would make that table interpretable.
- [ ] **Navigation/planning stack**: RTAB-Map (4), CuRobo (3), GTSAM (4) — all three are now load-bearing for the [XLeRobot bring-up plan](syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) and the [5-DoF experiment](syntheses/projects/five-dof-arms-in-robotwin.md).
- [ ] **Moondream (4)** — DimOS's local VLM option.

### Suggested order

1. **§3 stale claims** — two edits, both are wrong-as-written today.
2. **§4** — three trivial fixes.
3. **§6 Drake, RDT, Zenoh** — the three that would most improve reasoning about existing pages.
4. **§1/§2** — decide *derived vs hand-maintained* counts first; the answer determines whether §1 is a one-off repair or a recurring chore.
5. **§5** — cosmetic.

## [2026-08-13c] XLeRobot bring-up — plan filed, decisions pending

*Scoped after the RoboTwin experiment was deferred as off-path. Plan: [XLeRobot — navigate, pick-and-place, teleoperate](syntheses/projects/xlerobot-nav-manip-teleop-bringup.md). It executes [fleet-ladder](syntheses/projects/fleet-agentic-framework.md) steps 0–1 for the single robot.*

### Phase 0 — unblocked (D435i owned, 2026-08-13)

The camera decision is settled: the **D435i is in hand**, and it is the unit the [camera options analysis](syntheses/projects/xlerobot-camera-options-low-light.md) recommends. What remains is a fit task on the [existing bracket](syntheses/projects/xlerobot-d435i-bracket.md) (`hardware/xlerobot-d435i-bracket/`, `.stl` + parametric `.scad`), whose two open parameters can now be resolved because the hardware exists:

- [ ] **Caliper `cam_m3_z`** — M3 hole height above the camera's bottom edge. Not in Intel's D400 datasheet; the current **17 mm is an estimate**. This is the one that will bite if wrong.
- [ ] **Measure the robot-side bolt pattern** on the XLeRobot "last mounting link" — currently a **placeholder** in the `.scad`.
- [ ] Re-export → print (64×42×16 mm, ~14.7 cm³) → test-fit → mount → **calibrate camera extrinsics**. Half a day including the print.

### Highest-value milestone

- [ ] **~50 demos of one top-down task → ACT on the Spark → runs on-robot.** Ladder step 0. 2–3 h of teleoperation at realistic rates. First point where the robot does something learned, and it validates the whole data flywheel.

### Known blocker with a known fix

- [ ] **One serial port, one owner.** A ROS 2 `JointState` publisher and LeRobot cannot both hold the FeeTech arm bus. Interim: time-slice (nav owns the base, LeRobot takes the arm only during a pick). General fix: **[Rosetta](entities/rosetta.md) owning the bus and serving both** — which makes the Rosetta arm-bus contract load-bearing for this project, not optional.

### Carried into the plan from today's research

- [ ] **Top-down grasps only** (radial for lateral). Derived in the [5-DoF analysis](syntheses/projects/five-dof-arms-in-robotwin.md); the one place today's cross-embodiment thread pays off practically. Teleoperate a candidate grasp by hand *before* recording 50 demos of it.
- [ ] **ACT onboard, SmolVLA off-board.** Measured on Orin Nano: ACT 36 ms / 27.8 Hz vs SmolVLA 713.8 ms / 1.4 Hz. The bottleneck is the iterative action expert, not the VLM — so it is not fixable by shrinking the language model.

## [2026-08-13b] RoboTwin 2.0 / RoboMIND / openFT — follow-ups

*Three backlog items closed. What they opened:*

### The action-space question is now the wiki's sharpest open thread

- [ ] **Nobody has run RoboTwin 2.0's data generator against a 5-DoF arm.** The grasp-adaptation benefit *grows as DoF falls* (Franka 7 → −0.1; Piper 6 → **+22.7**), and 5-DoF is the tier [SO-ARM101](entities/so-arm101.md) / [XLeRobot](entities/xlerobot.md) / [Sourccey](entities/sourccey.md) actually occupy. **Plan written 2026-08-13: [Can RoboTwin 2.0 generate data for a 5-DoF arm?](syntheses/projects/five-dof-arms-in-robotwin.md)** — ~1 week, RoboTwin is MIT and the SO-101 URDF is Apache, both verified present. Carries a falsifiable kinematic prediction (5-DoF is dexterous top-down, constrained laterally — the *opposite* of Piper's documented preference, so RoboTwin's candidate augmentation is likely pointed the wrong way), a virtual-6-DoF-twin control isolating DoF from reach, and a hard prerequisite: **WSL cannot run it** (rendering ❌ per RoboTwin's own support matrix), so this needs native Linux or a rented RTX-class GPU.
  - **DEFERRED 2026-08-13** after scoping against the owner's actual goal (XLeRobot navigating / picking / teleoperable). It is **not on that critical path**: zero overlap with navigation or teleoperation, and for pick-and-place the direct route is better — **[SmolVLA](entities/smolvla.md) is trained and validated on SO-100/SO-101, the same 5-DoF arm**, at 78.3% real-world multi-task. The 5-DoF gap is a gap in the *cross-embodiment / synthetic-data* line, **not** in the LeRobot single-platform line. Revisit when **demonstration collection is demonstrably the bottleneck**.
  - [ ] Note the split if it is ever revived: **embodiment bring-up ≈ 3–4 days** (useful on its own if you want synthetic XLeRobot data), **control arm + analysis ≈ 3 days** (pure research). Doing the bring-up for practical reasons makes the experiment a cheap add-on.
  - [ ] **Compute is unresolved and a [DGX Spark](entities/dgx-spark.md) does not fix it.** GB10 is ARM64 (SAPIEN wheels are x86_64-first), Spark runs the CUDA 13 stack against RoboTwin's recommended 12.1, and RoboTwin documents stalls on datacenter-class GPUs (issue #83 / SAPIEN #219) — so **prefer RTX-class**. If a Spark is the only option, budget a spike day proving SAPIEN + CuRobo run on ARM64 first.
- [ ] **What action space makes dexterous-hand data usable in a cross-embodiment VLA?** [RoboMIND](entities/robomind.md)'s 15,187 [Tien Kung](entities/tien-kung.md) trajectories are 14% of the dataset and structurally excluded by `xyz + Rot6D + binary gripper`. Candidate answers exist in the wiki ([latent action tokens](concepts/learning/latent-action-tokens.md), [UniT](entities/unit.md)'s shared codebook) and none has been tested on this data.

### Unused resources sitting in ingested sources

- [ ] **RoboMIND's 5k annotated failure trajectories** — the only failure corpus in the wiki, and no downstream use is recorded anywhere. Every other failure-driven result here ([π*0.6](entities/pistar06.md), [ASPIRE](entities/aspire.md), [RoboTwin 2.0](entities/robotwin.md)'s VLM localizer) *generates* failure signal at training time instead.
- [ ] **RoboMIND's Isaac Sim digital twin** (30,035 trajectories replicating the real tasks and assets) — set up for exactly the controlled real-vs-sim comparison the wiki keeps wanting, and unused. RoboTwin 2.0 built its own twins from scratch rather than reusing these.
- [ ] **No ablation isolates which of RoboTwin's five randomization axes carries the gain.** The texture library alone cost 20,000 Stable Diffusion generations filtered to 11,000; knowing whether texture matters would be worth having before anyone rebuilds it.

### openFT — a weekend project with an outsized payoff if it works

- [ ] **Does the 4-cluster Hall arrangement reject servo magnetic field?** The first question for any wrist mount, unaddressed in the repo, and the one that decides whether the design is viable at all.
- [ ] **No specs published** — range, resolution, noise floor, bandwidth, hysteresis, temperature drift, cost. Nothing can be compared to a commercial part without at least range and noise floor.
- [ ] **What does calibration actually cost?** "A load cell or reference sensor" is the difference between a $60 project and a $2,000 one.
- [ ] It has **no LICENSE file** despite the README saying open-source. Worth an upstream issue.

### Carried forward from this morning

- [ ] The 5-DoF field trial ([Sourccey](entities/sourccey.md) ships September), prompt retrieval, Soft-Fold release, the Sep–Nov Sourccey re-check, and the standing finding that **four agentic-robotics stacks publish zero success rates between them**.

## [2026-08-13] Sourccey + X-VLA and DimOS ingests — follow-ups

*Two ingests, 44 pages. Drift they introduced was fixed the same day (LIBERO tie six→ten propagated to the audit page, index, and deployability landscape; RoboTwin randomized-scene item closed; across-stacks stack counts corrected). What remains is below.*

### Highest value: nobody measures anything in agentic robotics

- [ ] **Four stacks, zero published success rates.** [stretch_ai](entities/stretch-ai.md), [ROSOrin](entities/rosorin.md)/[OpenClaw](entities/openclaw.md), [Waddle](entities/waddle-labs.md), and now [DimOS](entities/dimos.md) at 3,874★ — none reports a rollout count, a latency, or a success rate. The [across-stacks synthesis](syntheses/agents/llm-agent-architecture-across-stacks.md) claims the pattern beats VLAs on shippability; that claim rests on the **absence of measurement on both sides**. A rollout-backed comparison of any two of these is the highest-value experiment currently available, and DimOS makes it cheap: `dimos --replay` and `--simulation` run the full agent stack with no hardware.
- [ ] Related and concrete: **does `@skill` discovery scale past ~10 skills** before tool selection becomes the bottleneck? DimOS ships ten. Nobody has hit the wall yet.

### X-VLA follow-ups

- [ ] **The 5-DOF question.** X-VLA aligns all embodiments to absolute SE(3) EEF pose and pretrains only on ≥6-DOF arms. [Sourccey](entities/sourccey.md) ships it on **5-DOF + gripper** arms. Soft prompts are the mechanism that *should* absorb this and nothing published tests it — an uncontrolled field trial begins in September. Watch for it.
- [ ] **Prompt retrieval for zero-shot embodiment transfer** — proposed in the paper's §5.3, never run. Pretrain on enough platforms that a new robot is served by its nearest existing prompt. The cleanest follow-on experiment the paper names.
- [ ] **No independent replication of soft prompts.** But X-VLA is upstream in [LeRobot](entities/lerobot.md) as the `xvla` policy, which lowers the bar considerably.
- [ ] **Soft-Fold dataset** (1,200 bimanual cloth-folding episodes) — release promised, not confirmed. Would be the wiki's reference dexterous-manipulation dataset if it lands.
- [ ] **Is the ℓ1-error proxy transferable?** R² = −0.925 between held-out action error and adaptation success was measured on X-VLA's own targets. If it generalizes it is the cheapest instrument the field has for scaling studies, which are rare precisely because rollouts are expensive.

### Ingests newly exposed

- [x] ~~**RoboMind**~~ — **done 2026-08-13**: [paper](sources/robomind-paper.md) + [entity](entities/robomind.md). Surfaced the dexterous-hand exclusion and the n=10 floor case.
- [x] ~~**Primary RoboTwin 2.0 paper**~~ — **done 2026-08-13**: [paper](sources/robotwin2-paper.md). Confirmed the 5,000-rollout protocol, corrected the ICML venue claim, and supplied the Piper 2.4%→25.1% DoF result.
- [x] ~~**`openFT-sensor`**~~ — **done 2026-08-13**: [source](sources/openft-sensor-github.md) + [entity](entities/openft-sensor.md). Complete hardware package, zero specs, no license, unmaintained.
- [ ] **UniVLA primary**, **TAMP**, **LTL** — carried forward unchanged from 2026-08-04.

### Re-check dated items (Sep–Nov 2026)

- [ ] **[Sourccey](entities/sourccey.md) price, runtime, and open-source completeness.** All three unknown; all three resolve on the published roadmap. Specifically: do STLs, a BOM, wiring, and a **URDF** land? Does the advertised "Electrical" repo appear? What is the runtime on 120 Wh?
- [ ] **Which X-VLA checkpoint ships on Sourccey, and are the weights open?** "4 micromodels" implies four task finetunes from an unnamed base.

### Smaller open questions

- [ ] What action-space convention does `dimos dataprep` write into its LeRobot v3.0 export, and is it compatible with SO-101/DROID-trained policies? This is the whole question for anyone hoping to train on DimOS-collected data.
- [ ] Why is Jetson Orin Nano **experimental** in DimOS — VRAM, ARM wheels, or thermals? Bears directly on [onboard compute for XLeRobot](syntheses/platforms/jetson-onboard-compute-xlerobot.md).
- [ ] What is `gpt-5.6-luna`? Named as DimOS's default planner in two places, uncovered here.
- [ ] Does [Vulcan](entities/vulcan-robotics.md) intend `dimos-vulcan` as a [Sourccey](entities/sourccey.md) navigation layer? The fit is legible; the fork is one star and untouched since July.

## [2026-08-04] Action-representation session — next steps and gaps

*Four ingests in one day ([TurboVLA](sources/turbovla-paper.md), [RT-H](sources/rt-h-paper.md), and a six-source batch: [behavior trees](sources/behavior-trees-book.md), [RT-1](sources/rt-1-paper.md), [RT-2](sources/rt-2-paper.md) + [blog](sources/rt-2-deepmind-blog.md), [PDDL generalized planning](sources/generalized-planning-pddl-llm-paper.md), [UniT](sources/unit-paper.md)), plus one synthesis: [action representation languages](syntheses/agents/action-representation-languages.md). ~40 pages added. Recommended order below.*

### 1. Lint pass — do this first, it is the cheapest and the debt compounds silently

Three standing claims moved today and pages elsewhere may still quote the old versions:

- [ ] **The [LIBERO](entities/libero.md) top tier went from six models to nine** (TurboVLA 97.7, CogVLA 97.4, VLA-Adapter 97.3 joined; cluster now spans 1.2 pp). Grep for "top of the wiki's LIBERO table," "highest LIBERO," and any phrasing implying a *ranking* inside the tie. The [audit](syntheses/platforms/vla-success-rate-audit.md) already caught that exact phrase in three places once before.
- [ ] **The [VLA taxonomy](concepts/learning/vla-models.md) gained an orthogonal axis** ([LLM-free / V+L→A](concepts/learning/llm-free-vla.md)). Pages describing "four action-head families" as the complete picture are now incomplete — the families describe how actions *leave* an LLM, not whether one is present.
- [ ] **The [deployability landscape](syntheses/platforms/vla-deployability-landscape.md) gained a fifth axis** (compute class required to hit a latency figure). Anything citing "the four axes" needs a look.
- [ ] **Stub markers**: [RT-2](entities/rt-2.md) was promoted stub → primary the same day it was created; check `_stub_` markers in [index.md](index.md) for others now filled ([Evo-1](entities/evo-1.md), [UniVLA](entities/univla.md), [PaLI-X](entities/pali-x.md) remain genuine stubs).
- [ ] **Source counts** — several concept/entity pages had `sources:` bumped by hand today; verify against actual inbound links.

### 2. Measure an LLM-free VLA on a Jetson — the highest-value missing row in the wiki

- [ ] **Step 0, a real blocker: verify TurboVLA checkpoints actually exist.** The [paper](sources/turbovla-paper.md) announces `github.com/H-EmbodVis/TurboVLA`; repo contents were **not verified at ingest**. If weights are unreleased, the fallback is [Evo-1](entities/evo-1.md) (0.8 B / 1.7 GB) — still informative, since its 137.2 ms on a 4090 is the wiki's case study in **small ≠ fast**.
- [ ] **The measurement.** [TurboVLA](entities/turbovla.md)'s **0.9 GB inference footprint is the first in this wiki that fits an 8 GB [Orin Nano](entities/jetson-orin-nano.md) with headroom** — [GR00T](entities/nvidia-groot.md)'s 16 GB floor eliminates the board outright. Every edge number on the [control-rate ladder](syntheses/platforms/control-rate-ladder.md) comes from a pre-2026 architecture; **no LLM-free policy has ever been measured at the edge.**
- [ ] **Protocol** — match [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md) exactly so numbers are comparable: end-to-end camera→action, FP16, batch 1, reported beside its ACT 27.8 Hz / Diffusion 1.8 Hz / SmolVLA 1.4 Hz on the same board class. Record power draw, which that source also lacks for most rows.
- [ ] **Both outcomes are results.** Band B on an Orin → a new fact about what runs on a battery. Band C → the 4090 figure does not survive edge memory bandwidth, which is the honest prior and directly qualifies the [deployability landscape](syntheses/platforms/vla-deployability-landscape.md)'s fifth axis.

### 3. Build the BT-over-VLA — the architecture nobody has built

- [ ] The [action-representation synthesis](syntheses/agents/action-representation-languages.md) concludes that **[behavior trees](concepts/robotics/behavior-trees.md) make the *composition* readable while staying agnostic about the *action*** — the only place readability and portability co-occur. The implied architecture is a **BT with a latent-token or LLM-free policy at an Action leaf**: portable structure, auditable guards, opaque-but-transferable policy underneath.
- [ ] **No ingested source does this.** It is also the concrete form of the [guardrails](syntheses/agents/guardrails-for-robot-agents.md) finding that **the execution rail ships empty** — BTs are a 20-year-old, formally-analyzed candidate for exactly that layer (safety-by-construction via sequence guards; stochastic BTs reduce to Markov chains yielding success probability and expected completion time).
- [x] ~~Prerequisite ingest: **BehaviorTree.CPP and the Nav2 BT navigator**~~ — **done 2026-08-04**: [engine](sources/behaviortree-cpp-docs.md) + [production instance](sources/nav2-behavior-trees-docs.md). The scaffolding is complete — ports give the typed boundary, Nav2 gives cause-selected recovery / bounded retries / preemption / runtime plugin swap, and **no Nav2 leaf is a learned policy**. Only the substitution remains.

### 4. Ingests, in descending value

- [ ] **Task-and-motion planning (TAMP)** — newly exposed and *not* closed. TAMP bridges symbolic specifications to continuous motion, which is exactly [PDDL](concepts/agents/symbolic-task-planning.md)'s "says nothing about motion" limitation and the gap the whole action-representation thread keeps hitting. [Kaelbling](entities/leslie-kaelbling.md) is already an entity and a founder of the line.
- [ ] **UniVLA primary** (RSS 2025) — the last secondhand model in the action-representation thread; [UniT](sources/unit-paper.md)'s taxonomy files it as the vision-only design that *"entangles low-level appearance confounders."*
- [ ] **Universal action tokenization / action priors** (arXiv 2606.26095) — secondhand only; would round out [latent action tokens](concepts/learning/latent-action-tokens.md).
- [ ] **LTL / temporal-logic task specification** — still uncovered; the formal-verification neighbour of PDDL.
- [ ] **RT-1's baselines**: **Gato** and **BC-Z** have no pages. **QT-Opt** supplied the Kuka data behind the wiki's earliest cross-embodiment result (22 → 39%) and is likewise unfiled.

### Open questions carried forward (unresolved, from the four ingests)

- [ ] **Run [LIBERO-PRO](sources/libero-pro-paper.md) on [TurboVLA](entities/turbovla.md).** Named in three places as the decisive test. TurboVLA is the wiki's **most exposed** model to the memorization critique — 0.2 B, no embodied pretraining, no web-scale language priors, trained on LIBERO alone. Counter-hypothesis is equally live: [Grounding DINO](entities/grounding-dino.md) pretraining may transfer under object swaps *better* than an LLM latent. Ai2's [harness](sources/vla-evaluation-harness-github.md) runs it at ~18 min/H100.
- [ ] **Does RT-H's extraction grammar port across morphologies?** [RT-H](entities/rt-h.md)'s lexicon is generated mechanically from *one robot's* 9 action dimensions. The design move the synthesis proposes is **specify the grammar, induce the lexicon** — re-run the same extraction on a different embodiment and test whether the induced lexicons are mutually interpretable. **Untested by anyone.**
- [ ] **Why was the language route to cross-embodiment abandoned?** [RT-H](sources/rt-h-paper.md)'s own Future Work proposes bridging [OXE](entities/open-x-embodiment.md) embodiments and human video *with language motions* (2024). The field went to [latent tokens](concepts/learning/latent-action-tokens.md) instead. **Tried and failed, or never attempted?** Unrecorded, and the most interesting unknown in the thread. [UniT](sources/unit-paper.md) does not cite RT-H — the two traditions answer the same question without talking to each other.
- [ ] **Nobody has compared a readable and a latent action interface on the same robot and tasks.** The cleanest experiment the synthesis names.
- [ ] **The names result has an untested confound.** RT-H-OneHot, TurboVLA task-ID, and PDDL No-Names all consume **text-pretrained models**, so the three-way convergence measures what such models need, not what is intrinsically necessary. A policy trained from scratch on robot data alone might not care.
- [ ] **Add a CNL condition to TurboVLA's instruction-encoding ablation** — the one-training-run experiment (four consumer GPUs). Free-form English 97.7 / **a controlled vocabulary** / task-ID 95.4. Parity → readability is free; near the floor → the grammar discarded the compositional semantics.
- [ ] **[UniT](entities/unit.md)'s visual anchoring assumes visible consequences** — force-dominant, occluded, and in-hand manipulation untested; transfer evidence is pick-and-place-shaped (EgoDex `basic_pick_place`, `pour`).
- [x] ~~**[RoboTwin 2.0](entities/robotwin.md) randomized-scene setting is unrun.**~~ — **closed 2026-08-13** by the [X-VLA paper](sources/xvla-paper.md), which reports both settings across all 50 tasks: **domain randomization costs every model 20–31 points** (X-VLA 70.0→39.0, π0 46.4→16.4, RDT 34.5→13.7), the ranking survives, and per-task numbers show total collapses hiding in the average (`Place Object Basket` 50.0 → **0.0**). The headroom argument holds — leaders sit at 39% on hard, where 3 pp gaps separate. Still open: the LIBERO-PRO-shaped question of *why* specific tasks collapse.
- [ ] **RT-2's blog/paper discrepancy is recorded but not generalized.** The [blog](sources/rt-2-deepmind-blog.md) headlines 3× generalization where the paper reports ~2×. The wiki cites vendor blogs often; **a systematic pass checking blog claims against their papers** would be cheap and high-yield — this instance was found only because both were ingested together.
- [ ] **[RT-1](sources/rt-1-paper.md) / [RT-2](sources/rt-2-paper.md) have no per-cell N.** 3,000 and 6,000 trials across 200+ instructions; aggregate gaps hold, per-task and per-category orderings do not. Do not repeat PaLI-X-vs-PaLM-E-on-math as a ranking.
- [ ] **The [behavior-trees book](sources/behavior-trees-book.md) was read structurally.** The formal proofs (Ch. 6), planning algorithms (Ch. 7), and stochastic reliability calculus (Ch. 9) were summarized from their framing, not verified line by line. Fine for current use; needs a deeper read before any claim leans on the math.

## [2026-08-03] DeepMind robot-safety cluster — follow-ups
- [x] ~~**Ingest SciFi-Benchmark**~~ — **done 2026-08-03**: [paper](sources/scifi-benchmark-paper.md) (arXiv 2503.10706, Sermanet/Majumdar/Sindhwani — confirming shared authorship; [Sindhwani](entities/vikas-sindhwani.md) is now on all five safety-program papers). Confirmed as the provenance of ASIMOV-Dilemmas-Scifi (9,056/53,384 corpus numbers match). Headline: constitutions lift alignment 79.4%→95.8% and resist adversarial prompting 23.3%→92.3%; sci-fi constitutions top-perform on ASIMOV's real-world data. **All three works named on the [safety page](sources/deepmind-gemini-robotics-safety-page.md) are now ingested.**
- [ ] **What is the delta between ASIMOV v1 and ASIMOV-2.0?** The wiki now has v1 ([paper](sources/asimov-benchmark-paper.md)) and knows 2.0 only as a name in the [GR 1.5 report](sources/gemini-robotics-1-5-report.md), paired with Auto-Red-Teaming. No ingested source documents the change.
- [ ] **Does the semantic-safety layer have an enforcement mechanism anywhere?** The [concept page](concepts/safety/semantic-safety.md) concludes it is "measured, sometimes predicted, and not yet enforced" — matching the [guardrails thread](syntheses/agents/guardrails-for-robot-agents.md)'s finding that the execution rail ships empty. **Worth a synthesis** joining the two: safety-from-the-model-side and safety-from-the-runtime-side reach the same gap from opposite directions.
- [ ] **Bridge the formal and empirical safety wings — or record that nobody has.** [Safely Learning Dynamical Systems](sources/safely-learning-dynamical-systems-paper.md) covers linear/polynomial systems with known uncertainty sets; nothing the wiki tracks (diffusion policies, VLAs, code-writing agents) qualifies. Same author ([Sindhwani](entities/vikas-sindhwani.md)) on both sides, no paper connecting them. The most interesting open problem in this cluster.
- [ ] **Does the Veo simulator offer a cheap route to LIBERO-PRO-style perturbation testing at scale?** The [audit backlog](#) has long wanted a 2026-class model run through perturbation suites. A generative simulator can synthesize perturbations cheaply — but whether simulator-measured robustness transfers is untested.
- [ ] **RoboART is validated only on diffusion policies.** Whether embedding-space anomaly detection predicts degradation for **VLAs** — which is what the wiki mostly tracks — is untested.
- [ ] **Springer version-of-record not diffed.** The [Safely Learning](sources/safely-learning-dynamical-systems-paper.md) ingest used the arXiv preprint (2305.12284v2, 2024-06) because the FoCM page is cookie-gated; the journal version (2026-04) is the citable one and may differ.

## [2026-08-03] Gemini Robotics 2 — the wiki is a generation behind
- [x] ~~**Ingest the Gemini Robotics 2 blog post**~~ — **done 2026-08-03**: [blog](sources/gemini-robotics-2-blog.md). Supplies the benchmark tables the model page lacked; the [entity](entities/gemini-robotics.md)'s "generation behind" warning is retired. — `deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/`. The [model page](sources/deepmind-gemini-robotics-model-page.md) revealed a **"2" generation (GR 2 / ER 2 / On-Device 2, released 2026-07-30)** but carries **no numbers at all**. The blog is the substantive primary announcement and the ingest that would actually update [Gemini Robotics](entities/gemini-robotics.md), whose every quantitative claim is still 1.5-era.
- [x] ~~**Ingest the *Gemini Robotics 2: Safety Technical Report*.**~~ — **done 2026-08-03**: [report](sources/gemini-robotics-2-safety-report.md). Introduces **ASIMOV-Agentic**; extends [semantic safety](concepts/safety/semantic-safety.md) from judgment to orchestration and confirms the "measured, not enforced" conclusion in the vendor's own words. Would extend the wiki's safety thread, which currently ends at **ASIMOV-2.0** in the [1.5 report](sources/gemini-robotics-1-5-report.md), and is the likeliest home for the benchmark numbers the model page omits.
- [ ] **Gemini Robotics On-Device 2 deployment envelope** — **partially closed 2026-08-03**: the [official model card](sources/gemini-robotics-on-device-2-model-card.md) was found and ingested. It supplies lineage (GR 1.5 tech + on-device Gemma), **v1→v2 results (SO101 53.3% vs 6.7%; Dexmate 75.6% vs 33.3%)**, and the high-DoF limitation — but **still no params, memory, hardware, or control rate**, so the [control-rate ladder](syntheses/platforms/control-rate-ladder.md) entry remains impossible. A third-party tutorial claims ~0.25 s closed-loop (~4 Hz) — unofficial. Watch for a technical report or dev-blog with the envelope.
- [ ] **ASIMOV-Agentic is on Hugging Face** (`google/asimov_agentic`, CC-BY-4.0) but the dataset itself is not ingested — only the report describing it. Per-model numbers live in figures, not tables, so exact scores were not extractable at this depth.
- [ ] **Privacy and fairness are explicitly out of scope** in the GR 2 safety report. A human-proximity detector with demographic performance variance is an unexamined risk the report names and defers.
- [ ] **"Attention jailbreaking"** is named as untested — the 100% safety-tool-calling result is acknowledged as possibly fragile at long context. Watch for the follow-up.
- [ ] **Was 1.6 a full family release or ER-only?** Now sandwiched between two documented generations; the wiki knows ER 1.6 only as Boston Dynamics' AIVI-Learning engine.
- [x] ~~**[Apptronik Apollo](entities/apptronik-apollo.md) has no Apollo 2**~~ — **added 2026-08-03**: Apollo 2 is the GR 2 whole-body platform, benchmarked with both [SharpaWave](entities/sharpa-wave.md) (5-finger, 22-DoF) and Inspire hands, and the real-world safe-stopping testbed (99% detection / 96% safe-pose). — per press coverage that is the GR 2 whole-body demonstration platform.
- [x] ~~**Did GR 2 actually lift 1.5's dexterity ceiling?**~~ — **answered 2026-08-03: partly.** Gripper tasks 74–90% (precise insertion 89.6%), but **four of five multi-finger tasks sit at 32–44%**. Sharpest evidence: **unscrew bulb 92% vs screw bulb 36%** — same object and hand, 2.5x gap, removal vs threaded insertion. No trial counts published, so the 44/40/36/32 cluster is not internally separable. 1.5's stated weakness was "dexterity ≈ prior generation"; GR 2 leads with dexterity claims while at least one press headline framed it as still struggling. No primary evidence either way — resolve from the tech report, don't infer.

## [2026-07-28] MolmoAct2 version-check — follow-ups
- [ ] **Watch for a v3 / camera-ready of arXiv 2605.02881.** v2 (2026-05-08) is latest as of 2026-07-28, but the **arXiv abstract has already been rewritten** with `MolmoER` / `MolmoThink` / `OpenFAST` — which usually signals a camera-ready in progress. If a v3 lands with those names in the body, the wiki should **rename** rather than alias, and the [naming table](sources/molmoact2-paper.md) becomes the migration record.
- [x] ~~**Ingest the `allenai/molmoact2` GitHub repo.**~~ — **done 2026-08-03**: [repo](sources/molmoact2-github-repo.md) + [SO-100/101 model card](sources/molmoact2-so100-101-model-card.md). **Partially met the stated goal:** the README does *not* document per-layer KV conditioning or OpenFAST (it mentions "depth-token reasoning" only), so grounding those mechanisms still needs a **source-level** read, not a docs read. **What it did deliver:** the full checkpoint family, memory footprints (SO-100/101 5B at ~16 GB bf16; DROID ~88 GB fp32), the fact that **MolmoAct2 ships as a [LeRobot](entities/lerobot.md) application** (v3.0 datasets, LeRobot submodule, LeRobot training workflows), FastAPI client/server deployment, [ManiSkill](entities/maniskill.md) sim eval, and **no Jetson support of any kind**. Consequences filed on the [control-rate ladder](syntheses/platforms/control-rate-ladder.md) and [XLeRobot compute page](syntheses/platforms/jetson-onboard-compute-xlerobot.md).
- [ ] **Source-level read of `allenai/molmoact2`** for the mechanisms the README skips — [per-layer KV conditioning](concepts/learning/per-layer-kv-conditioning.md) and the [OpenFAST tokenizer](entities/fast-action-tokenization.md). The docs ingest above did not reach them.
- [ ] **Version-check the wiki's other load-bearing papers.** This check cost minutes and returned a naming divergence + missing repo IDs. Candidates: the JEPA line ([LeWorldModel](entities/leworldmodel.md), [LeJEPA](sources/lejepa-paper.md)), [π0](sources/pi-zero-paper.md)/[FAST](sources/fast-paper.md), [OpenVLA-OFT](sources/openvla-oft-paper.md) — all arXiv preprints the wiki cites heavily and none re-checked since ingest.

## [2026-07-27] Five-source batch — follow-ups
- [x] ~~**Re-audit the wiki's real-robot success-rate claims against the ~1,030-rollout bar.**~~ — **done 2026-07-27**: [Success-rate audit](syntheses/platforms/vla-success-rate-audit.md). Top of the LIBERO table is one statistical tie (needs >1.8 pp to separate at ~97%; cluster spans 1.6 pp); every structural conclusion survives; MolmoAct2-Think's +0.9 shown unestablished. **Residual work:** (a) **record N at ingest going forward** — the audit was expensive because trial counts were missing from the pages quoting the rates; (b) **two unknown-N comparisons still need their rollout counts** — SmolVLA 78.3 vs π0 61.7, and Cosmos3-Nano vs π0.5 on RoboLab-120; (c) ~~confirm the LIBERO protocol~~ — **done 2026-07-27** via [LIBERO-PRO](sources/libero-pro-paper.md): **50 episodes/task → 500/suite, 2,000 per four-suite average**. Section A is now grounded, not provisional.
- [x] ~~**rliable / robomimic / RoboArena still unfiled**~~ — **RoboArena ingested 2026-07-27** ([paper](sources/roboarena-paper.md) + [entity](entities/roboarena.md)); the evaluation-methodology story now has both poles. **Still open: rliable / robomimic** — the *statistical-reporting* tooling (bootstrap CIs, stratified metrics) that would let the wiki report intervals instead of point estimates, which is the concrete fix the [audit](syntheses/platforms/vla-success-rate-audit.md) implies.
- [ ] **Run a 2026-class model through LIBERO-PRO** — **status upgraded 2026-08-03: no longer blocked on tooling.** Ai2's [vla-evaluation-harness](sources/vla-evaluation-harness-github.md) (ingested) supports LIBERO-Pro *and* MolmoAct2 / GR00T N1.7 / π0.5 in one system, with reproduction reports verifying four LeRobot checkpoints at 96–100% of published standard-LIBERO scores. **The perturbation run itself remains unpublished.** Lead: arXiv 2606.27663 (June 2026) appears to report expanded LIBERO-PRO numbers incl. GR00T-N1.6 — verify before quoting (its numbers differ from LIBERO-PRO's own protocol). Also confirmed: the wiki's recorded LIBERO-PRO numbers match the current arXiv v2 (2026-05-25).
- [ ] **RoboArena residuals** — what the "oracle" ranking is (the r≈0.95-vs-0.60 headline rests entirely on it); whether the live leaderboard still runs the paper's Bradley-Terry variant and how many comparisons back [Cosmos 3](entities/nvidia-cosmos.md)'s reported #1; inter-rater agreement given that evaluators set their own preference criteria; what the [0–100] progress score is used for if the ranking uses the binary preference.
- [ ] **LIBERO-PRO per-model × per-perturbation table** not captured at ingest depth (Figure 7). Also unresolved: whether "0.0%" is the union of all perturbations or one axis, and whether anyone has *adopted* LIBERO-PRO — a benchmark critique only bites if people report the harder number.
- [ ] **Cosmos3-Edge-Policy-DROID has no published benchmark score.** The wiki has the 16B Nano at 39.7% vs π0.5's 28.1% on RoboLab-120; the 4B Edge policy's number is unpublished, so the 16B→4B quality drop is unpriced. Watch for it — it decides whether the 15 Hz edge rate is worth having.
- [ ] **Is Cosmos 3 Edge's 15 Hz end-to-end?** Camera→action (like the [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md) numbers it sits beside on the [control-rate ladder](syntheses/platforms/control-rate-ladder.md)) or model-forward only? Also unstated: power draw at that rate, T2000/T3000 numbers, and the **Edge license** (Nano/Super are OpenMDW-1.1).
- [ ] **microGPT line count** — 243 per Karpathy's announcement, ~200 per one reading of his blog post. Resolvable in one minute by reading the [gist](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) directly; not done during ingest.
- [ ] **Who is Mitchell A. Carroll / what is arcnem.ai?** No affiliation on the [deck](sources/arcnem-strange-loops-ai-agents.md), no other source from either in the wiki. If the strange-loop thread continues, verify before leaning on it.
- [ ] **Hofstadter primaries un-ingested** — *GEB* and *I Am a Strange Loop*. Both wiki sources invoking him are secondary. Also unsourced here: **Hofstadter's own skepticism about LLMs**, which is directly relevant to sources borrowing his metaphor to argue LLMs are strange loops.
- [ ] **Model collapse / synthetic-data recursion has no page** — the [strange-loops concept](concepts/agents/strange-loops-and-self-reference.md) names the robotics instance (DreamGen/DreamDojo neural trajectories, MimicGen, 827 h in GR00T N1's data pyramid) and asks whether it is a productive or compounding-error loop. The wiki has no source that answers it.
- [ ] **GNW / IIT / predictive processing** are named once each (via Masood) and nowhere else. Only worth pages if consciousness/cog-sci sources keep arriving.
- [ ] **NPE (Neural Posterior Estimation) is a one-mention technique** — first simulation-based-inference sighting in the wiki. If it recurs in evaluation work, it deserves a concept page.

## [2026-07-27] Anthropic Frontier Red Team robotics arc — follow-ups
*(Three sources ingested this day: [Project Fetch](sources/anthropic-project-fetch-robot-dog.md), [Phase Two](sources/anthropic-project-fetch-phase-two.md), [How Claude Performs on Robotics Tasks](sources/anthropic-how-claude-performs-on-robotics-tasks.md).)*

- [x] ~~**Ingest *How Claude Performs on Robotics Tasks***~~ — **done 2026-07-27**, and it turned up a third page ([Phase Two](sources/anthropic-project-fetch-phase-two.md)) that was also ingested. The arc is complete.
- [x] ~~**Confirm the Project Fetch robot**~~ — **resolved 2026-07-27**: the eval names it, *"a real Unitree Go2 (the quadruped robot of Project Fetch)"*. Caveat retired on [Unitree Go2](entities/unitree-go2.md).
- [x] ~~**Uplift measurement is a one-source concept**~~ — partially: [AI uplift studies](concepts/safety/ai-uplift.md) now has 3 sources including the autonomy re-run. **Still open:** no *non-Anthropic* uplift study. The biological-risk originals are referenced but un-ingested; METR-style developer-productivity RCTs would be the obvious outside anchor and would test whether the control-arm-habituation problem generalizes.
- [ ] **Frontier Red Team people pages** — five bylined authors across the arc, none filed: **Michael Ilie** and **C. Daniel Freeman** (both on two of three papers — the connective authors), **Kevin K. Troy**, **Shmuel Berman**, **Jia Deng**. If Deng is the Princeton/ImageNet Jia Deng that's worth confirming and noting, but the sources don't say.
- [ ] **Is `github.com/safety-research/embody` actually released?** The eval gives the URL as "once released." An ingest of the harness would ground the four-level taxonomy in runnable code and is the single highest-value follow-up here — it would make [control abstraction levels](concepts/robotics/control-abstraction-levels.md) reproducible rather than descriptive.
- [x] ~~**Put the 83 Hz figure on one axis with the wiki's edge-latency numbers.**~~ — **done 2026-07-27**: [The control-rate ladder](syntheses/platforms/control-rate-ladder.md). ~30 rows, four bands, REQ/MEAS/CAP tagging. Main result: the 83 Hz figure names a band *nothing in the wiki deploys into*, so the tracking comparison is LLM (0.2–0.4 Hz) vs the **VLA planner tier** (1.4–27.8 Hz). **Residual gaps recorded on the page** — (a) no 2026-class VLA has an on-Jetson number ([MolmoAct2](entities/molmoact2.md) is H100-only; **the highest-value missing measurement in this area**), (b) no published chunk-adjusted *effective control rates*, so inference-Hz vs control-Hz stays qualitative, (c) **no ingested source measures a small local LLM in a control loop** — the 1 Hz agent figures are status heartbeats, (d) power is an unmodelled third axis.
- [ ] **Why does VLA supervision hurt in-distribution?** The eval establishes that every tested model scores below [MolmoAct](entities/molmoact.md)-alone on tasks it already handles, and that better models hurt less — but not what the overrides get *wrong*. This is the crux for the whole [LLM-agent robot](concepts/agents/llm-agent-architecture.md) thread. Watch for a follow-up that decomposes it.
- [ ] **Unitree Robotics company entity** — the wiki has [G1](entities/unitree-g1.md), [H1](entities/unitree-h1.md), and [Go2](entities/unitree-go2.md) but **no parent-company page**, and all three link to bare-text "Unitree Robotics". Not filed because no ingested source carries citable company facts (founding, Wang Xingxing, Hangzhou, funding, IPO).
- [ ] **Claude 4 System Card p. 114** — the prior "Claude trains a quadruped locomotion policy in sim, not yet autonomously capable" evaluation is cited by Project Fetch but un-ingested. Would be the wiki's first system-card ingest and the actual baseline the whole arc is measured against.
- [ ] **Quadruped tier is still the thinnest-sourced platform group.** [Go2](entities/unitree-go2.md) is now well-instrumented *as an evaluation target* but has **no primary technical source** (no datasheet, no SDK docs), same for [Spot](entities/spot.md), and **no ingested research paper uses a quadruped** — while quadruped locomotion RL is a major subfield. Flagged on the [robot platforms comparison](syntheses/platforms/robot-platforms-comparison.md).
- [ ] **No wiki page for any model named in the eval** — Claude Opus 4.5/4.6/4.7, Claude Mythos Preview, GPT-5.1/5.4, Gemini 3.1 Pro Preview, Kimi K2.6, Qwen 3.6+. Recorded as the source states them. Probably fine (the wiki isn't an LLM tracker), but the *Mythos Preview* profile is genuinely anomalous — only model where reasoning budget mattered, best novel-task supervisor, worst in-distribution supervisor — and would be worth a page if it recurs.

## [2026-07-18] VLA-cluster session — wrap-up notes (where things stand)
Session arc: ingested 3 raw drops (VLA-0, YOLOv11n child-detection, USC table-tennis MARL) → filed the VLA-baseline cluster VLA-0 pointed at (OpenVLA-OFT, FAST/π0-FAST, MolmoAct, Molmo + concepts: Knowledge Insulation, multi-agent-rl, SAHI) → then paid down the "primary un-ingested" debt by ingesting **4 VLA primaries**: VLA-0 (2510.13054), Knowledge Insulation (2505.23705), OpenVLA-OFT (2502.19645), FAST (2501.09747). The VLA action-representation design space is now anchored on those four ingested primaries.
- [x] ~~**Remaining un-ingested VLA primaries:** MolmoAct + Molmo~~ — **both done**: Molmo ingested 2026-07-24 ([molmo-pixmo-paper](sources/molmo-pixmo-paper.md)), OLMo/OLMoE entities filed same day; **MolmoAct primary ingested 2026-08-03** ([molmoact-paper](sources/molmoact-paper.md)) — v1 is Franka-only; editable-trace steerability is its distinctive contribution. The Allen-Institute lineage is now fully primary-grounded end to end (OLMo → Molmo → MolmoAct → MolmoAct2).
- [x] ~~**Author page — Moo Jin Kim**~~ — **filed 2026-07-27**: [Moo Jin Kim](entities/moo-jin-kim.md), now also a [RoboArena](entities/roboarena.md) co-author. **Percy Liang** still has no page.

## [2026-07-17] VLA-0 ingest — lint follow-ups
- [x] ~~**OpenVLA-OFT entity**~~ — filed 2026-07-17; **primary ingested 2026-07-18** ([openvla-oft-paper](sources/openvla-oft-paper.md), arXiv 2502.19645): parallel decoding + action chunking + continuous L1 head; 76.5→97.1 LIBERO at 26× throughput. Entity now primary-grounded + de-stubbed.
- [x] ~~**π0-FAST / π0.5-KI entities**~~ — filed 2026-07-17; **both primaries ingested**: [FAST paper](sources/fast-paper.md) (2501.09747, 2026-07-18; acronym corrected to *Frequency-space Action Sequence Tokenization*) + [Knowledge Insulation paper](sources/knowledge-insulation-paper.md) (2505.23705, 2026-07-17). Both concept/entity pages now primary-grounded.
- [x] ~~**MolmoAct entity**~~ — **filed 2026-07-17**: [MolmoAct entity](entities/molmoact.md) (grounded in VLA-0's LIBERO row; **primary 2508.07917 still un-ingested** → see wrap-up above).
- [x] ~~**Molmo entity**~~ — **filed 2026-07-17**: [Molmo entity](entities/molmo.md) (Ai2 fully-open VLM; pointing capability; [MolmoAct](entities/molmoact.md) backbone). **Primary arXiv 2409.17146 + OLMo/OLMoE LLMs still un-ingested** → see wrap-up above.
- [ ] **`## Mentioned in` section missing** on 6 stub entities: [octo](entities/octo.md), [paligemma](entities/paligemma.md), [smolvlm](entities/smolvlm.md), [gemma3](entities/gemma3.md), [bagel](entities/bagel.md), [open-x-embodiment](entities/open-x-embodiment.md). (openvla fixed 2026-07-18 during FAST ingest.) Cosmetic; normalize on a stub-cleanup pass.
- [ ] **13 pre-existing index/frontmatter source-count mismatches** (2026-07-17 lint): mostly off-by-one — `lerobot` 19/20, `nvidia-cosmos` 15/16, `google-deepmind` 8/9, `jetson-orin-nano` 11/12, `nvidia-halos` 3/4, `nvidia-brev` 2/3, `ros2` 4/5, `robot-safety-standards` 2/3, `ai-red-teaming` 4/5, `large-behavior-models` 4/5, `world-model` 29/30; plus two larger needing ground-truth recount before syncing: **`latent-space` 18/22**, **`whole-body-control` 3/5**. (The 4 self-introduced this session were fixed in-commit.)

## [2026-07-16] NVIDIA batch (Jetson skills / DeepStream / RoboLab / Halos blog) — follow-ups
- [ ] **TensorRT entity** — referenced as bare text from [DeepStream](entities/nvidia-deepstream.md), JetPack, and several Jetson pages; no entity page. File if it keeps recurring.
- [ ] **NVIDIA SRL (Seattle Robotics Lab) entity** — [RoboLab](entities/nvidia-robolab.md) is filed but its parent lab (Dieter Fox / Birchfield / Ramos / Tremblay group) isn't; would anchor DROID + a lot of NVIDIA robot-eval work. The `/labs/srl/` attribution is inferred from the URL path — confirm the lab's official name before filing.
- [x] ~~**RoboArena** — no page.~~ **Filed 2026-07-27**: [entity](entities/roboarena.md) + [paper](sources/roboarena-paper.md).
- [ ] **DeepStream vs Isaac ROS** perception-boundary synthesis — if both keep recurring (video-analytics/IVA vs robot-perception/VSLAM).
- [ ] **Halos deploy-skill name reconciliation** — `hoisa-deploy-profile` (Trust Center) vs `warehouse-deploy` / `halos-deploy` (blog); confirm on next Halos update.

## [2026-07-16] Agile / Techman / EngineAI ingest — follow-ups
- [ ] **NavBot store** — deliberately not filed as a source (user call, thin page). If it recurs, a source page could anchor the **[NavBot-D1 quadruped ($4,999)](https://navbot.com/collections/complete-robots)**, EN01 wheel-legged kit, OpenDuck Mini RL kit — open-source-robotics-store tier alongside Elephant/Hiwonder. Reviewed 2026-07-16.
- [ ] **Universal Robots entity** — referenced from the new [cobots concept](concepts/robotics/collaborative-robots.md) as the market leader (~50% share) but has no entity page. File if cobots recur.
- [ ] **EngineAI SA01 / SE01 / PM01** — company + [T800](entities/engineai-t800.md) filed; the cheaper/earlier models (incl. the world-first-front-flip **PM01**, <$15k) are only mentioned in prose. Break out if referenced.
- [ ] **Agile Robots "Thor Series"** — Agile Robots markets a product line called "Thor" (its own naming). Confirm it's unrelated to [NVIDIA Jetson Thor](entities/jetson-thor.md) (assumed collision).
- [ ] **Autonomy of URKL combat robots** — unresolved whether T800 fighters run learned policies, scripted move-sets, or teleop. Watch for a technical source that settles it (decides whether combat leagues are a real autonomy benchmark).

## [2026-07-04] Fleet-framework build pieces (from the fleet synthesis)
Surfaced by [Fleet agentic control framework](syntheses/projects/fleet-agentic-framework.md) — genuine wiki gaps that are also the project's DIY work:
- [x] ~~**ROS 2 ↔ MCP server**~~ — **built + published + ingested 2026-07-04**: [design doc](syntheses/projects/ros2-mcp-server-design.md), the [`ros2-mcp-server`](https://github.com/tanioklyce-dev/ros2-mcp-server) repo (MIT), and the round-trip [source page](sources/ros2-mcp-server-github.md) + [entity](entities/ros2-mcp-server.md). Remaining (in the *repo*, not the wiki): wire the `ros_bridge` ROS 2 calls + SSE transport; re-ingest to deepen the source page as the repo matures.
- [ ] **A2A for multi-robot robotics** — the wiki names the [A2A protocol](concepts/agents/llm-agent-architecture.md) but has **no robotics instance**; watch for the first real one.
- [ ] **HIL-SERL** has no dedicated concept/source page (only referenced via LeRobot); would anchor the "minimal-human continual-improvement" flywheel.
- [~] ~~**Cross-embodiment policy transfer at hobby scale** — SO-ARM101 ↔ HX-12H~~ — **being designed out** (2026-07-04): the fleet owner is swapping the ROSOrin Pro's HX-12H for an [SO-ARM101](entities/so-arm101.md), homogenizing all three robots to one arm → one shared policy, no transfer problem. See the [fleet framework arm-swap decision](syntheses/projects/fleet-agentic-framework.md). (The measurement question only matters if someone keeps a mixed-arm fleet.)

## [2026-07-04] New gaps from the SONIC / Gemini-1.5 / YAM batch
- [ ] **Vision-language navigation (VLN)** — flagged by the [Awesome-Embodied-Robotics list](sources/awesome-embodied-robotics-agent.md) as a genuine wiki gap (ALFRED / R2R / VLN-CE); no concept or source yet.
- [ ] **Household simulators** beyond the [Habitat](entities/habitat.md) stub — AI2-THOR, iGibson (same list).
- [x] ~~**BEHAVIOR / BEHAVIOR-1K + OmniGibson**~~ — **fully ingested 2026-07-04**: [BEHAVIOR-1K paper](sources/behavior-1k-paper.md) + [BEHAVIOR entity](entities/behavior-benchmark.md) + [OmniGibson entity](entities/omnigibson.md) + dedicated [OmniGibson codebase ingest](sources/omnigibson-github.md) (Isaac Sim 4.1.0, 14-robot roster, install). Residual: **iGibson** predecessor lineage + **AI2-THOR / Habitat** peer sims still un-ingested; exact OmniGibson VRAM/disk minimums (inherited from Isaac Sim 4.1.0) unconfirmed.
- [ ] **Nemotron entity** (carried) — now also referenced from the SONIC-adjacent NVIDIA stack.

## [2026-07-04] Agents / edge-inference ingest — follow-ups
- [x] ~~**Duplicate raw PDF decision**~~ — resolved 2026-07-04: the re-dropped `xlerobot_cutting_the_cord_2603.09051v1.pdf` was byte-identical to the tracked `raw/2603.09051v1.pdf`; deleted the duplicate (paper already fully ingested as [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md)). If the descriptive filename is preferred, `git mv` the tracked file + update its `local_path` — not done (cosmetic).
- [ ] **Gemma 4 primary source** — [entity](entities/gemma4.md) built from the NVIDIA edge blog only; Google's Gemma 4 model card/report not ingested (variant params confirmed via the blog). Deepen when filed.
- [ ] **Nemotron entity** — `nvidia/nemotron-3-super-120b-a12b` (120B-MoE / 12B-active) is now referenced by [NemoClaw](entities/nemoclaw.md) + [Hermes quickstart](sources/nvidia-nemoclaw-hermes-quickstart.md) but has no entity page; file if it recurs.

## [2026-07-04] Concept-subdir count audit (NEW — found during DreamGen/FLARE/Eagle ingest)
- [ ] **Re-lint concept catalog counts for pages in subdirectories.** The [2026-07-04] lint's mismatch checker used regex `(?:entities|concepts)/([a-z0-9-]+\.md)` which does **not** match `concepts/<subdir>/<page>.md` (world-models/, learning/, robotics/, …), so all subdirectory concept counts went unverified. Use a corrected regex like `(?:entities|concepts)(?:/[a-z0-9-]+)+\.md`. **10 known stale index counts** (index vs frontmatter, found 2026-07-04; verify ground truth before syncing — frontmatter itself may be over/undercounted, per the entity lesson last session): `scaling-laws-vla` 2/4, `energy-based-models` 4/5, `latent-space` 10/14, `siamese-network` 5/8, `llm-agent-architecture` 8/18, `ai-safety-alignment` 3/6, `assistive-robotics` 16/22, `agentic-uavs` 4/5, `biomechanical-simulation` 5/7, `connectome` 3/4. (jepa/world-model/world-model-simulators already fixed; nvidia-gear + joel-jang were this-session-introduced and fixed immediately.)

## [2026-07-04] Lint pass (post GR00T-version-line ingest)

Clean at time of writing: 0 broken links (7,175 checked), 0 orphan pages, all `sources/` pages linked from index, all catalog counts synced to frontmatter (6 mismatches fixed this session — apptronik-apollo, tonypi, dobb-e, grievous, ollama, pi-zero-6).

### Knowledge gaps — NVIDIA GR00T line (highest value first)
- [x] ~~**DreamGen entity**~~ — filed 2026-07-04: [DreamGen entity](entities/dreamgen.md) + [DreamGen paper](sources/dreamgen-paper.md).
- [x] ~~**FLARE concept note**~~ — filed 2026-07-04: [FLARE concept](concepts/world-models/flare.md) + [FLARE paper](sources/flare-paper.md).
- [x] ~~**Eagle VLM entity**~~ — filed 2026-07-04: [Eagle entity](entities/eagle-vlm.md) + [Eagle-1](sources/eagle-paper.md) + [Eagle 2.5](sources/eagle-2-5-paper.md) papers.
- [ ] **Eagle 2** — the exact GR00T N1 production backbone has no standalone paper on file (only Eagle-1 research study + Eagle 2.5). Low priority.
- [ ] **DreamZero** — the middle Dream\* entry (DreamGen → **DreamZero** → DreamDojo) still has no source page.
- [x] ~~**YAM arms**, **Galaxea R1 Pro**, **GEAR-SONIC controller**~~ — all filed 2026-07-04: [YAM](entities/yam.md), [Galaxea R1](entities/galaxea-r1.md), [GEAR-SONIC](entities/gear-sonic.md) ([SONIC paper](sources/sonic-paper.md)).

### Deferred stub-marker cleanups (cosmetic, not counted as lint failures)
- [ ] [Dobb·E](entities/dobb-e.md) is still marked `_stub_` in [index.md](index.md) despite having a full entity page + an ingested paper ([dobb-e-paper](sources/dobb-e-paper.md)) + 4 citing sources. The `_stub_` marker is stale — drop it on next pass.
- [ ] Re-audit `_stub_` markers globally against actual page depth — several may be stale now that counts are synced (candidates: [pi-zero-6](entities/pi-zero-6.md), [ollama](entities/ollama.md)). Not urgent.

### Pre-existing gaps carried forward (not from this session)
- [ ] **`concepts/reinforcement-learning.md` hub page** — the most-overdue concept page; natural RL-side companion to [optimal-control](concepts/robotics/optimal-control.md). Both primary anchors ([Sutton & Barto](sources/sutton-barto-rl-textbook.md), [Kober 2013](sources/kober-rl-robotics-survey-2013.md)) are now filed.
- [ ] **`syntheses/rl/robot-rl-lineage.md`** — Kober 2013 → deep-RL locomotion → RECAP-class VLA fine-tuning; the robotics companion to the existing [atari-rl-lineage](syntheses/rl/atari-rl-lineage.md).
- [ ] **Nicklas Hansen entity** — would anchor the TD-MPC1 → TD-MPC2 lineage ([TD-MPC](sources/td-mpc-paper.md) now filed).
- [ ] **VQ-BeT parameter count** — unpublished in the paper; only layer dims are citable.

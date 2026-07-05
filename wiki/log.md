# Log

Append-only chronological record of wiki events. Each entry begins with `## [YYYY-MM-DD] <action> | <subject>` for grep-ability.

## [2026-05-25] lint | LINT audit + flow-matching concept page + 8 entity stubs + 2 stale-claim fixes

User invoked `/LINT`. Audit found 0 broken links and 0 orphans across 414 files (excluding wiki/notes/); 2 hub-only-inbound pages; 12+ under-covered entities/concepts; 3 stale TODOs. User asked me to act on items 1–4 of the punch list.

- **Item 2 (cleanup)**: edited [vla-jepa-paper.md](sources/vla-jepa-paper.md) and [smolvla-paper.md](sources/smolvla-paper.md) to remove the stale "LIBERO entity not yet filed / SimplerEnv has no entity" claims; both entities exist. SmolVLA's open-questions section now links the new flow-matching concept page.

- **Item 1 (flow matching concept)**: filed [flow-matching.md](concepts/learning/flow-matching.md). Captures mechanics (Beta-sampled τ, straight-line interpolant, vector-field regression target, ~10 ODE steps at inference), the **VLA action-head taxonomy** (autoregressive tokens / DDPM / flow matching, with the three families framed as instances of a Fenchel-Young loss per Blondel & Roulet ch. 18), and the architectural variation across flow-matching VLAs (π0 = full bidirectional SA; π0.7 / π*0.6 = KI + stop-gradient; SmolVLA = interleaved CA + causal SA). Closes 50 mentions × 16 files of dangling "flow matching" references.

- **Item 3 (7 entity stubs)**: filed thin entity pages for the most-under-covered things:
  - [OpenVLA](entities/openvla.md) — 49 mentions across 23 files. The reference 7 B open-VLA baseline (Kim et al. 2024, Llama-2 backbone + autoregressive action tokens).
  - [Octo](entities/octo.md) — 17 mentions across 10 files. Transformer-from-scratch generalist policy on OXE (Octo Model Team 2024).
  - [PaliGemma](entities/paligemma.md) — 19 mentions across 10 files. Google's 3 B VLM (SigLIP + Gemma 2B); backbone of π0.
  - [Gemma3](entities/gemma3.md) — 20 mentions across 8 files. Google's 2025 VLM family (1B/4B/12B/27B with built-in 400M vision encoder); backbone of π0.7.
  - [SmolVLM-2](entities/smolvlm.md) — 13 mentions across 7 files. Hugging Face's compact 0.4 B VLM (SigLIP + SmolLM2); backbone of SmolVLA.
  - [Open X-Embodiment (OXE)](entities/open-x-embodiment.md) — 15 mentions across 9 files. The 22-embodiment umbrella corpus that [DROID](entities/droid.md) is a single-embodiment subset of.
  - [BAGEL](entities/bagel.md) — 12 mentions across 6 files. 14 B mixture-of-transformers image-gen + editing model; the substrate of π0.7's subgoal-image world model.

- **Item 4 (π0.6 stub anchoring)**: filed [pi-zero-6.md](entities/pi-zero-6.md) as the anchor for the **π0.5 / π0.6 / π0.6-MEM** intermediate generations (combined ~84 mentions across 14+ files). None has a publicly released primary paper the wiki has ingested; documented entirely via downstream references in π0.7 and π*0.6.

- **Cross-link updates** for the 9 new entity / concept pages:
  - [Physical Intelligence](entities/physical-intelligence.md) — π-series lineage table now links the intermediate generations through pi-zero-6.md.
  - [VLA models concept](concepts/learning/vla-models.md) — action-head taxonomy table now links new entities (OpenVLA, Octo, PaliGemma, Gemma3, SmolVLM-2, BAGEL, flow-matching concept).
  - [DROID](entities/droid.md) — explicit "constituent of OXE" note added.
  - [index.md](index.md) — new entries under Datasets (OXE), new "VLM backbones" subsection (PaliGemma + Gemma3 + SmolVLM-2), new "Generative models for image / world" subsection (BAGEL), VLA-list extended with OpenVLA + Octo + pi-zero-6, Learning concepts list now includes flow-matching.

### Lint results not addressed (lower priority)

- Knowledge Insulation (KI) / FAST tokens concept page — 16 mentions; held for a third paper to use it.
- CFGRL / AWR / human-gated DAgger concept pages — held until used outside the RECAP-related ingest cluster.
- MEM (memory encoder) entity — held; mentioned only via π0.6-MEM / π0.7.
- SO-100 entity — 29 mentions but distinct from SO-ARM101 (which has an entity); filing it should wait for a dedicated primary source.
- Vincent Roulet, Alex Koven, Francesco Capuano person entities — low priority.

### Cross-source insight

The lint surfaced a concrete **structural recommendation** for the wiki's VLA design-pattern coverage: now that flow matching is filed as its own concept and OpenVLA + Octo + π0 + π0.7 + π*0.6 + SmolVLA + EgoScale all have entities, the [VLA action-head taxonomy table](concepts/learning/vla-models.md#action-head-design-across-vlas) is the densest single artifact tying late-2025 VLA design space together. A future synthesis page on "VLA architectural design space, mid-2026" would consolidate this into a comparison study.

## [2026-05-25] ingest | The Elements of Differentiable Programming (Blondel & Roulet, Google DeepMind)

User dropped `raw/2403.14606v3.pdf` — Blondel & Roulet's **485-page reference textbook** on differentiable programming, draft v3 (June 24, 2025), free on arXiv. The wiki's most comprehensive single mathematical-foundation reference to date.

- **Created**: [Blondel & Roulet source page](sources/blondel-roulet-differentiable-programming.md) — captures the 5-part / 18-chapter structure (Fundamentals → Differentiable programs → Differentiating through programs → Smoothing programs → Optimizing differentiable programs) plus a chapter-to-wiki-content mapping table tying each major section to the wiki's existing threads (transformers ch. 4.8 → every VLA; autodiff ch. 8 → every learned model; REINFORCE ch. 12.3 → [RECAP](entities/pistar06.md); reparametrization ch. 12.4 → flow matching in [π0](entities/pi-zero.md) / [π0.7](entities/pi07.md) / [SmolVLA](entities/smolvla.md); softmax + sparsemax ch. 13.5 → attention + action heads; Fenchel-Young losses ch. 18 → unifying VLA action-head taxonomy). Filed in the textbook-precedent style (cf. [Welch Labs Vol I](sources/welchlabs-illustrated-guide-to-ai.md), [Sutton & Barto](sources/sutton-barto-rl-textbook.md)) — section-summary depth, not deep ingest.

- **Created**: [Mathieu Blondel entity](entities/mathieu-blondel.md) — Google DeepMind research scientist; **Fenchel-Young loss + sparsemax** lineage + **JAX ecosystem** contributions (JAXopt, optax). The author who unifies softmax / cross-entropy / sparsemax / hinge loss into one Fenchel-Young construction — which is directly the framework the wiki's VLA action-head taxonomy (autoregressive tokens vs DDPM vs flow matching) sits inside.

- **Updated**: [Robot-learning curriculum hub](syntheses/curriculum/robot-learning-curriculum.md) — new "Rigorous mathematical companion" callout pointing at the Blondel & Roulet book as the **lookup reference** when a curriculum module hand-waves through a derivation. Specifically called out for Module 1 (backprop = ch. 8 autodiff), Module 3 (transformers = ch. 4.8), Module 5 (generative models + reparametrization = chs. 12.4 + 13), Module 8 (RL gradient estimators = ch. 12.3).

- **Updated**: [index.md](index.md) — new chronological source entry; Mathieu Blondel added to People.

### Cross-source insight

The book formalizes a framing the wiki has been implicitly using across many ingests: **every action-distribution choice in VLAs (autoregressive tokens, DDPM, flow matching, sparsemax) is an instance of a Fenchel-Young loss with a different convex-conjugate regularizer.** This unifies the [vla-models taxonomy](concepts/learning/vla-models.md) under one mathematical structure. Worth a future synthesis page once a couple more wiki ingests reinforce the connection.

## [2026-05-25] ingest | π0.7 + π*0.6 — completes the π-series spine (π0 → π0.7 + π*0.6)

User dropped `raw/pi07.pdf` and `raw/pistar06.pdf` mid-session and asked to ingest both. Both are direct successors to π0 from [Physical Intelligence](entities/physical-intelligence.md) and were referenced as gaps in this morning's π0 entity ingest. The two papers represent Physical Intelligence's late-2025 push along two complementary axes — π0.7 = "scale data + diversify the prompt" and π*0.6 = "iterate on deployment experience via RL."

### π0.7 (https://pi.website/pi07)

- **Created**: [π0.7 source page](sources/pi07-paper.md) — 5 B-param VLA = Gemma3 4B VLM + 860 M flow-matching action expert + MEM video-history encoder; **Knowledge Insulation (KI) training** with FAST tokens + stop-gradient to VLM. Captures the **diversified prompt** structure (subtask instructions, **subgoal images from a separate BAGEL 14B world model**, episode metadata = speed/quality/mistake, control mode), each component randomly dropped during training. Documents the data mixture (demonstrations + autonomous rollouts incl. failures + open-source robot datasets + egocentric human video + non-robot web data) and the demonstrated emergent capabilities (espresso machine, laundry folding, trash bag, box folding, vegetable peeling out-of-the-box; zero-shot cross-embodiment; compositional generalization like sweet-potato-into-air-fryer).
- **Created**: [π0.7 entity](entities/pi07.md) — first credible "emergent capabilities" VLA; the architectural contribution is the diversified-prompt recipe, not a new module.

### π*0.6 + RECAP (https://pi.website/blog/pistar06)

- **Created**: [π*0.6 source page](sources/pistar06-paper.md) — π0.6 + RECAP ("RL with Experience and Corrections via Advantage-conditioned Policies"). Three-step iterated recipe: data collection (autonomous rollouts + human-gated-DAgger interventions + sparse outcome rewards) → multi-task **distributional value function** training (201 bins, MC return target, same architecture as policy but smaller VLM backbone) → **advantage-conditioned** policy training via CFGRL-style classifier-free guidance. Sidesteps the policy-gradient problem on flow-matching VLAs by training the policy with and without an improvement indicator, then conditioning on "improved" at inference. Demonstrated tasks: 13-hr espresso machine, 2+ hr novel-laundry-folding in a new home, factory-grade box assembly. Headline: 2× throughput, ½ failure rate on hardest tasks.
- **Created**: [π*0.6 entity](entities/pistar06.md) — the wiki's first VLA-scale real-world RL recipe that works on expressive flow-matching action heads.

### Cross-source updates

- [Physical Intelligence entity](entities/physical-intelligence.md) — full rewrite of the model-line table to capture **π0 → π0.5 → π0.6 → π0.6-MEM → π0.7 + π*0.6 (RL branch)** lineage. Three primary sources (π0, π0.7, π*0.6) are ingested; three intermediates (π0.5, π0.6, π0.6-MEM) remain not-separately-ingested. Sources count 3 → 5.
- [π0 entity](entities/pi-zero.md) — Related section + "default π-series reference" now point at π0.7 and π*0.6 successors.
- [VLA models concept](concepts/learning/vla-models.md) — full π0.7 + π*0.6 entries added to the notable-VLAs list; action-head taxonomy table expanded to show **π0 (full bidirectional SA) / π0.7 (KI + stop-gradient) / π*0.6 (advantage conditioning) / SmolVLA (interleaved CA + causal SA)** as four distinct architectural variants within the flow-matching family.
- [index.md](index.md) — new chronological source entries for both papers; π0.7 + π*0.6 added to the VLA-list; Physical Intelligence source count bumped.

### Cross-source insight

The four π-papers ingested today (π0 full HTML + π0.7 + π*0.6 + SmolVLA) reveal **a tightly converged architectural recipe** for late-2025 VLAs: **frozen-or-stop-gradient pretrained VLM backbone + flow-matching action expert + action chunks of length n ≈ 50**. The remaining design variation is concentrated in three dimensions:

1. **Backbone**: PaliGemma 3 B (π0) → Gemma3 4B+MEM (π0.7) → SmolVLM-2 (SmolVLA, ~0.4 B).
2. **Action-expert attention**: full bidirectional SA (π0) → KI + stop-gradient (π0.7, π*0.6) → interleaved CA + causal SA (SmolVLA).
3. **Training signal**: pure IL on demonstrations (π0) → IL + diverse-data + diversified-prompt (π0.7) → offline RL + advantage conditioning (π*0.6) → IL on community datasets + async inference (SmolVLA).

**No one design wins everywhere.** SmolVLA beats π0 on real-world SO-100 at ~7× fewer params; π0.7 claims emergent capabilities π0 doesn't show; π*0.6 doubles throughput on the same hardware via RL. The 2025 VLA design space is now exploring all four dimensions of the variation simultaneously.

### Lingering wiki gaps

- **π0.5 / π0.6 / π0.6-MEM** intermediate papers — referenced extensively across π0.7 + π*0.6 but no primary sources.
- **Flow matching** concept page — now load-bearing across π0, π0.7, π*0.6, SmolVLA, EgoScale, and the LeRobot tutorial.
- **Knowledge Insulation (KI) + FAST tokens** — referenced training recipe used by both π0.7 and π*0.6; deserves its own concept page if a third paper uses it.
- **BAGEL 14B world model** — referenced as π0.7's subgoal-image generator; not in the wiki.
- **MEM memory system + Gemma3** — referenced architectural components; not separately filed.

## [2026-05-25] ingest | π0 full-HTML deepening + SmolVLA paper — closes the two largest VLA gaps

User asked to ingest `https://arxiv.org/html/2410.24164v1` and a new raw file. The raw file turned out to be `raw/2506.01844v1.pdf` = the **SmolVLA paper** (Shukor et al., HF/Sorbonne/valeo.ai/ENS, June 2025) — the other VLA entity gap flagged in this morning's LeRobot tutorial ingest. Both ingests landed at once, filling the two largest VLA gaps the wiki had been carrying.

### π0 — full HTML deepening (arxiv 2410.24164)

Existing `pi-zero-paper.md` was abstract-only since 2026-05-10. Full HTML ingested today.

- **Deepened**: [π0 source page](sources/pi-zero-paper.md) — full architectural detail (PaliGemma 3 B VLM + flow-matching action expert with full bidirectional attention; 3.3 B total params), training data (10,000 hr in-house teleop across 7 robot configs / 68 tasks + OXE + DROID + Bridge), the demonstrated task list (laundry folding, table bussing, microwave dish loading, egg-carton stacking, box assembly, grocery bagging), baselines (beats OpenVLA + Octo), and the VLM-as-planner + π0-as-controller stack.
- **Created**: [π0 entity](entities/pi-zero.md) — split off from [Physical Intelligence](entities/physical-intelligence.md) since π0 is now sufficient as a standalone entity (5 sources). Includes a head-to-head architectural comparison table vs SmolVLA.
- **Updated**: [Physical Intelligence entity](entities/physical-intelligence.md) — points at the new π0 entity; sources count 2 → 3.

### SmolVLA — new ingest (arxiv 2506.01844)

- **Created**: [SmolVLA source page](sources/smolvla-paper.md). Captures the three contributions (lightweight architecture, community-data pretraining, async inference), the architectural details (SmolVLM-2 backbone + interleaved CA + causal SA action expert at hidden=0.75×VLM + layer N=L/2 feature read + 64 visual tokens/frame), training data (481 community HF datasets / 22.9 K episodes / 10.6 M frames), the VLM-cleaned-task-annotation + camera-view-normalization tricks, the async-inference RobotClient/PolicyServer architecture with threshold-`g` + observation similarity filter, the analytical derivation of the queue-non-empty condition, the LIBERO + Meta-World + real-world SO-100 + real-world SO-101 result tables, and the implementation envelope (200 K steps × batch 256, ~30 K GPU hours total, can train on a single GPU).
- **Created**: [SmolVLA entity](entities/smolvla.md). The canonical affordable-VLA reference; **beats π0-3.5 B by +16.6 pts on real-world SO-100 multi-task** despite ~7× fewer params.

### Cross-source updates

- [VLA models concept](concepts/learning/vla-models.md) — π0 entry deepened with the full training-data + task list; SmolVLA entry expanded with all the architectural + result detail; action-head taxonomy table updated to show **autoregressive (OpenVLA) vs DDPM (Diffusion Policy) vs flow matching (π0, SmolVLA, EgoScale)** as the three families.
- [Diffusion Policy entity](entities/diffusion-policy.md) — new section explicitly framing DDPM-vs-flow-matching as the wiki's central continuous-action-head contrast; mentioned-in extended.
- [LeRobot entity](entities/lerobot.md) — π0 and SmolVLA called out as the two LeRobot-distributed reference VLA checkpoints; mentioned-in extended.
- [LeRobot tutorial source page](sources/lerobot-robot-learning-tutorial.md) — the two "π0 entity / SmolVLA entity" open questions are now resolved and stricken; SmolVLA author overlap with the tutorial authors noted.
- [index.md](index.md) — π0 + SmolVLA source entries expanded; new VLA-list entries for both; Physical Intelligence source-count bumped.

### Cross-source insight worth flagging

The two ingests **establish a clean architectural taxonomy across 2024–2025 VLAs**:

- **Action head**: autoregressive tokens (OpenVLA) → DDPM (Diffusion Policy) → flow matching (π0, SmolVLA, EgoScale). The flow-matching family is winning the 2025 design contest.
- **Attention pattern within action expert**: full bidirectional SA (π0) → interleaved CA + causal SA (SmolVLA) — SmolVLA's empirical win at smaller scale suggests the SmolVLA pattern may become the new default.
- **Data**: corporate teleop at scale (π0: 10,000 hr in-house) vs community datasets (SmolVLA: 22.9 K episodes from 481 HF datasets) vs egocentric human video (EgoScale: 20,854 hr). All three approaches are now backed by published artifacts.
- **The empirical surprise**: SmolVLA-0.45 B > π0-3.5 B on real-world SO-100 multi-task. **Smaller model + community data + better attention pattern + careful inference engineering beats raw param-count + corporate-data.** Same direction as the [Mobile ALOHA co-training pattern](sources/mobile-aloha-paper.md), [RUM data diversity finding](entities/robot-utility-models.md), and [EgoScale's human-video scaling law](sources/egoscale-paper.md).

### Lingering wiki gap surfaced

**Flow matching** as a concept is now load-bearing across π0, SmolVLA, EgoScale, and the LeRobot tutorial — but no dedicated `concepts/learning/flow-matching.md` page exists. Worth filing on a future pass.

## [2026-05-25] ingest | Mobile ALOHA project page + Grievous (downstream) + LeRobot tutorial (HF Space)

User asked to ingest three URLs in one batch: the [Mobile ALOHA project page](sources/mobile-aloha-project-page.md), the [alexkoven/Grievous repo](sources/grievous-github.md), and the [LeRobot "Robot Learning: A Tutorial" HF Space](sources/lerobot-robot-learning-tutorial.md). All three turned out to be tightly intertwined with the morning's [Mobile ALOHA paper](sources/mobile-aloha-paper.md) ingest and the wiki's existing heavy [LeRobot](entities/lerobot.md) / [XLeRobot](entities/xlerobot.md) coverage.

- **3 new source pages**:
  - [Mobile ALOHA project page (mobile-aloha.github.io)](sources/mobile-aloha-project-page.md) — companion to the paper; surfaces the tutorial Google Doc, the dataset Drive folder, author homepages (Fu, Zhao, Finn), and **the [ACT++](entities/act-plus-plus.md) codebase name** (`MarkFzp/act-plus-plus`) that the paper itself only cites as "ACT [104]".
  - [Grievous (alexkoven/Grievous)](sources/grievous-github.md) — early-stage WIP testbed "based on Mobile ALOHA + XLeRobot, built on LeRobot." RPi5-on-robot + remote-PC inference. Direct downstream of Mobile ALOHA + XLeRobot + LeRobot — all three of which are already heavily covered.
  - [Robot Learning: A Tutorial (LeRobot)](sources/lerobot-robot-learning-tutorial.md) — Hugging Face LeRobot team-authored tutorial (Capuano, Pascal, Zouitine, Wolf, Aractingi); arXiv 2510.12403 + interactive HF Space (410 likes). Chapter arc Classical Robotics → RL → IL → Generalist VLAs with runnable `lerobot` code examples for ACT, Diffusion Policy, async inference, π₀, and SmolVLA. **First HF-Space ingest in the wiki.**

- **2 new entities**:
  - [Grievous](entities/grievous.md) — the testbed project.
  - [ACT++](entities/act-plus-plus.md) — the mobile-extended ACT codebase; bundles the 16-dim action vector + co-training + action-chunk delay-shift introduced by Mobile ALOHA.

- **Updated**:
  - [ALOHA / Mobile ALOHA entity](entities/aloha.md) — added Hardware Code + ML Code (ACT++) repo URLs; new Downstream Projects section listing Grievous; Mentioned-in extended.
  - [ACT entity](entities/act.md) — new "Codebase evolution" section (original ACT → ACT++ → LeRobot's re-implementation); sources count 1 → 3.
  - [XLeRobot entity](entities/xlerobot.md) — new Downstream Projects section listing Grievous.
  - [LeRobot entity](entities/lerobot.md) — new "Official pedagogical reference" section pointing at the Capuano-et-al. tutorial; new "Downstream / hardware-ecosystem projects" listing Grievous; sources count 6 → 8.
  - [Imitation learning concept](concepts/learning/imitation-learning.md) — LeRobot tutorial called out as the canonical IL onboarding text; ACT++ codebase added to Frameworks-and-stacks bullet.
  - [Robot-learning curriculum synthesis](syntheses/curriculum/robot-learning-curriculum.md) — new callout pointing at the LeRobot tutorial as the parallel official version; explains the bottom-up (wiki) vs mid-stack-first (LeRobot) split.
  - [Mobile ALOHA paper source](sources/mobile-aloha-paper.md) — cross-link to the project page; ACT++ surfaced as the codebase name.
  - [index.md](index.md) — 3 new chronological sources; Grievous + ACT++ added to entity lists; Mobile ALOHA + ACT source counts bumped.

- **Cross-source insight worth flagging**: the three ingests **trace a single emerging cost-reduction arc** — Mobile ALOHA ($32k bimanual mobile, 2024) → XLeRobot ($660 bimanual stationary on a cart, Aug 2025) → Grievous (in-progress synthesis of both, 2026). The LeRobot tutorial is the pedagogical glue that makes this arc traversable in a single weekend by a new practitioner. All four artifacts (Mobile ALOHA, XLeRobot, Grievous, LeRobot tutorial) share the same software substrate ([LeRobot](entities/lerobot.md)) and the same default IL method ([ACT](entities/act.md)). The wiki now has the full lineage filed.

- **Open questions** (logged on the source pages): π₀ and SmolVLA still don't have their own entities despite being referenced across [DreamDojo](sources/dreamdojo-paper.md), [scaling-laws-vla.md](concepts/learning/scaling-laws-vla.md), [Physical Intelligence entity](entities/physical-intelligence.md), and now this tutorial; worth filing as a follow-up pass. Grievous's hardware BOM, license, and form-factor ("human-like") are also unresolved.

## [2026-05-25] ingest | Mobile ALOHA — fills a long-standing ALOHA / ACT gap

User dropped `raw/mobile-aloha.pdf` and asked to ingest. The paper is Fu, Zhao, Finn (Stanford, Jan 2024) — bimanual mobile manipulation via whole-body teleoperation + a co-training-with-static-data IL recipe. **The ingest closes an explicit wiki gap**: both [chelsea-finn.md](entities/chelsea-finn.md) and the [robot-platforms-comparison synthesis](syntheses/platforms/robot-platforms-comparison.md) had previously flagged "ALOHA / ACT — not yet ingested."

- **Created**: [Mobile ALOHA source page](sources/mobile-aloha-paper.md). Captures the $32k hardware envelope (4× ViperX 300 + AgileX Tracer base + RTX 3070 Ti laptop + 1.26 kWh battery; 12 hr runtime; whole-body teleop via waist-tether-to-base + wheel-backdrive), the seven evaluated tasks with success-rate table (avg +34% absolute from co-training, up to +90% on Rinse Pan / Call Elevator / Push Chairs), method compatibility across ACT / Diffusion Policy / VINN, the data-efficiency + mixture-robustness + co-train-vs-pre-train ablations, and the mobile-platform-specific **action-chunk delay-shift trick** (execute first k−d arm actions + last k−d base actions to compensate for the base's velocity-control delay).

- **Created 5 new entities**:
  - [ALOHA / Mobile ALOHA](entities/aloha.md) — platform line covering both original (2023) + Mobile (2024).
  - [ACT (Action Chunking Transformer)](entities/act.md) — IL method introduced with ALOHA; operationalized action chunking as a first-class IL primitive.
  - [Tony Z. Zhao](entities/tony-zhao.md) — original ALOHA + ACT first author; Mobile ALOHA co-lead.
  - [Zipeng Fu](entities/zipeng-fu.md) — Mobile ALOHA co-lead; Stanford Graduate Fellowship.
  - [Trossen ViperX 300](entities/viperx-300.md) — the 6-DOF benchtop arm SKU underneath ALOHA / Mobile ALOHA; wiki's first Trossen-class arm entry.

- **Updated**:
  - [Chelsea Finn entity](entities/chelsea-finn.md) — Mobile ALOHA added as her third paper in the wiki; the "ALOHA / ACT not yet ingested" note now relaxed (still flagged for the original 2023 paper, which is covered here only transitively).
  - [Imitation learning concept](concepts/learning/imitation-learning.md) — new bullet on action-chunked BC crediting ACT as the originator (vs Diffusion Policy as popularizer); new bullet on **co-training across heterogeneous datasets** as a method-agnostic IL primitive; Mobile ALOHA's mobile-platform delay-shift trick called out.
  - [Diffusion Policy entity](entities/diffusion-policy.md) — Mobile ALOHA evaluation added (Diffusion Policy underperforms ACT in the very-low-demo regime — 50 demos is below DP's typical floor of ≥250).
  - [Robot platforms comparison synthesis](syntheses/platforms/robot-platforms-comparison.md) — Mobile ALOHA added to the at-a-glance table and the research-tier list; "Research-tier mobile manipulation = Stretch" framing updated to "Stretch (single-arm) or Mobile ALOHA (bimanual)"; "ALOHA / ViperX bimanual setup — no entity page" gap closed.
  - [index.md](index.md) — new chronological source entry; Mobile ALOHA + ViperX 300 added under mobile manipulators; ACT added under BC methods; Tony Zhao + Zipeng Fu added under People; Chelsea Finn source count incremented.

- **Cross-source insight**: Mobile ALOHA is the **smallest-scale clean evidence** for the "data diversity > data quantity" pattern that runs across the wiki at multiple scales — [Robot Utility Models](entities/robot-utility-models.md) at NYC-homes scale, [EgoScale](sources/egoscale-paper.md) at 20k-hour egocentric scale, and now Mobile ALOHA at 825-static-demos + 20–50-in-domain scale. Same shape (mix small-targeted + larger-out-of-domain), same direction (positive transfer), wildly different orders of magnitude.

## [2026-05-25] ingest | JEPA-WMs GitHub (reproducibility recipe)

User asked to ingest `https://github.com/facebookresearch/jepa-wms`. README pulled via curl from raw.githubusercontent.com (no auth required for public repos; bypasses WebFetch). Distinct ingest from this morning's TMLR-paper deepening: the paper is the *what* and *why*, the GitHub repo is the *how-to-actually-clone-and-run-it*.

- **Created**: [JEPA-WMs GitHub source page](sources/jepa-wms-github.md). Captures the 12 downloadable checkpoints (5 JEPA-WMs + 5 DINO-WM + 2 V-JEPA-2-AC variants + 4 VM2M decoder heads), TorchHub + HF loading patterns, conda+uv install recipe, the 5 `JEPAWM_*` env vars, the 6 shipped HF datasets vs the gsutil-only DROID download (5.6–8.7 TB), the paper-config → environment mapping, the `Basile-Terver/robosuite` and `Basile-Terver/robocasa` forks, the MuJoCo 2.1 PointMaze quirk, and — most importantly — the **CC-BY-NC 4.0 license** which constrains downstream Stretch / ROSOrin Pro projects to non-commercial use.

- **The single most operationally useful fact in the repo**: it ships **both** V-JEPA-2-AC variants. `vjepa2_ac_droid` is the **rollout-loss-bug-fixed** retraining that produced the paper Table 2 numbers (formerly only described in §C); `vjepa2_ac_oss` is the original [V-JEPA 2 GitHub](sources/vjepa2-github.md) checkpoint. This closes the loop on the [V-JEPA 2 entity callout](entities/v-jepa-2.md) about the bug-fix — the fixed weights are now downloadable rather than requiring user retraining.

- **Updated**: [JEPA-WMs entity](entities/jepa-wms.md) — sources 4 → 5; Code section now lists the GitHub source page + checkpoint count + CC-BY-NC license caveat; Mentioned-in extended.

- **Updated**: [V-JEPA 2 entity](entities/v-jepa-2.md) — callout extended to point to the downloadable `vjepa2_ac_droid` (fixed) and `vjepa2_ac_oss` (original) checkpoint pair.

- **Updated**: [index.md](index.md) — new chronological-sources entry; positioned next to the paper.

- **Open questions** (logged on the source page): dataset license inheritance for the re-hosted Push-T / PointMaze / Wall sets (originally from `apple/ml-dino-wm`); divergence between the Basile-Terver forks of robosuite/robocasa vs upstream; bit-exact reproducibility of Table 2 numbers (README ships config filenames but doesn't claim it); SLURM-free distributed-training path for non-HPC users.

## [2026-05-25] ingest | Stretch 4 datasheet (Rev 5) + JEPA-WMs TMLR-version deepening

User dropped two PDFs in `raw/` and asked to ingest. Both turned out to be deepenings of existing wiki entries, not new topics.

### Stretch 4 datasheet — `raw/HelloRobot-DataSheet-Stretch-4-Rev5_AsLaunched.pdf`

The official 2-page Hello Robot spec sheet that the [Stretch 4 launch source page](sources/hello-robot-stretch-4-launch.md) explicitly flagged as **404 at first-ingest time** (2026-05-17). It has now surfaced and is the canonical Stretch 4 spec reference.

- **Created**: [Stretch 4 Datasheet source page](sources/hello-robot-stretch-4-datasheet.md). Captures exact sensor model numbers (**Hesai J128** LiDAR; **Luxonis OAK-FFC AR0234** wide-FOV; **Luxonis OAK-FFC IMX378** high-res; **OAK-D SR** wrist depth with 4 TOPs), specific compute (**Intel NUC 15 Core Ultra 5 225H** + 32 GiB + 1 TB; **Jetson Orin NX** with 16 GB + 128 GB + WiFi 5.2), the safety architecture (motor-current force limiting + 100 Hz watchdog + IMU tilt avoidance + dedicated head Runstop + **6× Pixart cliff curtains**), **24 V Feetech RS485 tool bus**, environmental envelope (10–30 °C / IP20 / 10–90 % RH), 12-month warranty, **not-yet-FCC-Class-A** caveat, plus absolute dynamic-speed numbers (lift 50 cm/s; arm 70 cm/s; base 60 cm/s; 20 mm step clearance).
- **Updated**: [Stretch entity](entities/stretch.md) — merged spec table now cites both launch page and datasheet, with per-row source attribution. Added contradiction-callout for the **9 DOF (datasheet) vs 8 + gripper (launch)** countings of the same hardware. Footprint corrected from 45 cm → 43 cm.
- **Updated**: [Hello Robot entity](entities/hello-robot.md) — sensor + compute SKUs now reflect datasheet detail; sources count 8 → 9.
- **Updated**: [Stretch 4 launch source page](sources/hello-robot-stretch-4-launch.md) — closed the "datasheet missing" TBD; provenance callout points to the new datasheet source page.
- **Updated**: [index.md](index.md) — datasheet added to Sources (chronological).

### JEPA-WMs TMLR-version full-paper deepening — `raw/7271_What_Drives_Success_in_Ph.pdf`

55-page TMLR-published (05/2026) version of Terver et al. The wiki had ingested only the arxiv-abstract + GitHub-README level on 2026-05-07; the full paper has now landed.

- **Updated**: [JEPA-WMs source page](sources/jepa-wms-paper.md) — full content rewrite. Confirms authors / affiliations (Meta FAIR + Inria + ENS/PSL + NYU). Adds the **recommended recipe per task type** (Table 1), the **head-to-head results table** (Table 2 — Ours beats DINO-WM on every env; beats V-JEPA-2-AC on every env where both ran), and all **8 design-axis findings** (encoder type, predictor architecture, multi-step rollout, proprioception, context length, planner, model + data scaling).
- **Updated**: [JEPA-WMs entity](entities/jepa-wms.md) — full rewrite. Recipe table + results table + design-axis findings now anchor the entity.
- **Updated**: [JEPA concept page](concepts/world-models/jepa.md) — new **"Design-axis lessons for JEPA-WM-style robot planning"** section consolidating the seven findings as load-bearing recommendations for anyone building this class.
- **Updated**: [DINO-WM entity](entities/dino-wm.md) — added the head-to-head loss row (DINO-WM beaten on every env by JEPA-WMs).
- **Updated**: [V-JEPA 2 entity](entities/v-jepa-2.md) — added callout that FAIR's own JEPA-WMs recipe beats V-JEPA-2-AC on Rc-R + DROID, with the structural-reason explanation (DINO's fine object segmentation > V-JEPA's coarser segmentation for control).
- **Created**: [Jean Ponce entity](entities/jean-ponce.md) — recurring senior author on FAIR JEPA-line papers (VICReg 2022; JEPA-WMs 2026); ENS/PSL + NYU.
- **Updated**: [index.md](index.md) — JEPA-WMs entry now reflects the TMLR publication + recipe + head-to-head numbers.

### Cross-source insight (worth flagging)

The wiki now has two parallel deepenings landing on the same day, both compute-split-flavored: **Stretch 4 (control on NUC 15 + AI on Jetson Orin NX)** and **JEPA-WMs (planning loop = encoder forward + predictor unroll + CEM)**. The Stretch 4 datasheet locks in a per-platform shape for the [Jetson Thor / DGX Spark train-vs-deploy](syntheses/platforms/jetson-thor-vs-dgx-spark.md) pattern that's been recurring across the wiki. The JEPA-WMs recipe gives the **first published reasoning about what to run on that AI accelerator** for image-goal planning — DINOv3-L encoder + AdaLN+RoPE predictor (depth 12) + 2-step rollout + CEM-L₂. A future synthesis could connect the two.

## [2026-05-17] query+howto | "Configure Orin Nano to boot NVMe when SD has no boot partition"

User running Jetson Orin Nano on L4T 36.5.0 from SD asked how to configure UEFI auto-fallback to NVMe. Reduces to: (a) make both media bootable; (b) put SD first in `BootOrder`; (c) trust UEFI's built-in skip-on-missing-bootloader behavior.

- **Updated**: [Jetson Orin Nano flash howto](syntheses/projects/jetson-orin-nano-flash-howto.md) — new section **"SD-primary with NVMe fallback (UEFI auto-fallback)"** with: prerequisite QSPI-bootloader check, two paths to install OS on NVMe from a running SD system (`nvme_install.sh` and manual rsync + partitioning), `efibootmgr -o` boot-order configuration, verification procedure, and configuration-specific caveats (multi-boot-media version match, ESP requirements, `extlinux.conf` UUID rewrites, QSPI-NVRAM persistence). Tags + intro updated to reflect broader scope; previously the page covered only "replace SD with NVMe."
- **Mechanism documented**: UEFI's `BootOrder` variable + automatic-fallthrough-when-entry's-bootloader-is-missing behavior. This is the user-friendly version of dual-boot fallback on Jetson without resorting to GRUB or manual chain-loading.

## [2026-05-17] ingest | PX4 Autopilot documentation

User pointed at `docs.px4.io/main/en/` — the canonical doc site for PX4, the dominant open-source autopilot for drones. Big gap in the wiki: existed UAV-AI research coverage ([Agentic UAVs concept](concepts/robotics/agentic-uavs.md), the [UAVs Survey](sources/uavs-agentic-ai-survey.md), [MIT drone adaptive control](sources/mit-drone-adaptive-control.md)) but no entity for the autopilot substrate underneath.

- **Created 1 source**: [PX4 Autopilot Documentation (docs.px4.io/main)](sources/px4-docs-main.md). Top-of-tree summary of the ~250-page docs site. Covers project facts (BSD 3-Clause, Dronecode Foundation, v1.16 stable / v1.17 alpha), vehicle types, [Pixhawk](entities/pixhawk.md) FMUv3–v6X-RT hardware, software architecture (NuttX RTOS + uORB pub-sub + EKF2 + control allocation), communication (MAVLink + ROS 2 / uXRCE-DDS + DroneCAN), GCS + SDKs (QGroundControl + MAVSDK), simulation (Gazebo + SIH + AirSim + HITL), and — most relevant to this wiki — the **Neural Networks subsystem** (TFLM + RAPTOR Adaptive RL NN Module + MC NN Control Module).

- **Created 4 entities**:
  - [PX4 Autopilot](entities/px4-autopilot.md) — the project; primary entity.
  - [Pixhawk](entities/pixhawk.md) — open-hardware flight-controller standard underneath PX4.
  - [Dronecode Foundation](entities/dronecode-foundation.md) — Linux Foundation Collaborative Project; steward of PX4 + MAVLink + Pixhawk + QGroundControl + MAVSDK. Same governance shape as [Farama Foundation](entities/farama-foundation.md).
  - [MAVLink](entities/mavlink.md) — telemetry / command protocol; spoken across PX4 + ArduPilot + ground-station tooling.

- **Updated**:
  - [Agentic UAVs concept](concepts/robotics/agentic-uavs.md) — new "Open-source autopilot substrate" section linking PX4 + Pixhawk + Dronecode + MAVLink + the RAPTOR module as the production realization of the concept's Control layer; sources 2→3.
  - [index.md](index.md) — PX4 under Software stacks; Pixhawk added under Controllers / edge AI compute; Dronecode under Companies; MAVLink under Formats / standards; PX4 docs added to chronological Sources.

- **Cross-source insight**: PX4's compute-split model — **deterministic real-time control on a [Pixhawk](entities/pixhawk.md) flight controller; AI / perception / planning on a [Jetson](entities/jetson-thor.md) companion computer** — is structurally identical to the wiki's recurring "CPU for control, GPU for AI" pattern. Same shape as [Jetson Thor / DGX Spark train-vs-deploy](syntheses/platforms/jetson-thor-vs-dgx-spark.md) and [Stretch 4](entities/stretch.md)'s NUC + optional Jetson Orin NX split. Three independent product lines (UAV, edge-AI cluster, mobile manipulator) converging on the same compute-split architecture in 2026.

- **Open questions** (logged on the source page): RAPTOR algorithm specifics, TFLM-on-FMUv6X-RT empirical performance, MC NN Control vs classical-allocator comparisons, whether anyone has shipped a VLA + PX4 integration, Auterion Skynode entity, PX4 + Newton physics-engine sim option.

## [2026-05-17] query+synthesis | "Summary of renting NVIDIA GPUs"

Spun off from the wiki-query-agent deployment plan after surfacing that [DGX Spark](entities/dgx-spark.md) is rentable from third-party providers — Brev didn't have it. That gap motivated a broader survey.

- **Created**: [NVIDIA GPU rental landscape](syntheses/platforms/nvidia-gpu-rental-landscape.md). Grouped catalog of providers across four tiers — NVIDIA-native (Brev, DGX Cloud, Launchables), AI-focused clouds (RunPod, Lambda Labs, CoreWeave, Vast.ai, Modal, Paperspace, Together AI, FluidStack / Crusoe / Spheron), hyperscalers (AWS / GCP / Azure / Oracle), DGX Spark-specific (Enverge, Server Room, Primcast), peer-to-peer (Vast.ai, NVIDIA forum P2P).
- **Pricing data** (per GPU-hr, mid-2026): H100 $1.25 (spot floor) – $6.98 across 15+ providers; B200 ~$2.12–$8; B300 $2.45–$6.80; A100 ~$0.80–$3; DGX Spark $0.48 (Enverge).
- **Decision guide** for picking a provider by use case (NVIDIA devtools / multi-GPU NVLink / production SLA / hobbyist / sporadic inference / DGX Spark specifically / already-on-hyperscaler).
- **Cross-source insight**: GPU rental pricing has compressed sharply in 2026 vs the 2023–2024 H100 supply crunch — H100 spot at $1.25/hr is a meaningful change vs $4–$8 during peak demand. Blackwell B200/B300 supply has caught up enough that they're now in similar price bands as H200.
- **Updated**: [NVIDIA Brev entity](entities/nvidia-brev.md) (cross-link to the rental landscape); [wiki-query agent deployment plan](syntheses/projects/wiki-query-agent-on-dgx-spark.md) (cross-link to the rental landscape from its Brev callout); [index.md](index.md) (new Platforms synthesis entry).

## [2026-05-17] query+synthesis | "How to make this wiki queryable online as an agent?"

User asked how to serve the wiki online as an agent. Conversation walked through:
- Three hosting paths (Anthropic API + file_search; static-site + RAG; MCP server).
- Trust dynamics of BYOK API-key UIs and who-pays-the-fees.
- Local open-source LLM options across consumer + server hardware tiers.
- Thor vs Spark for the inference workload specifically.

**User's decision: [DGX Spark](entities/dgx-spark.md) as the inference server**, justified by the other workloads the box handles (training, fine-tuning, Isaac Sim — RT-core-dependent things Thor can't do). Wiki query is the marginal use case, not the justifying one.

- **Created**: [Wiki-query agent on DGX Spark — deployment plan](syntheses/projects/wiki-query-agent-on-dgx-spark.md). Captures the three-option comparison, the Spark-over-Thor rationale, Qwen 2.5 72B Q8 as the default model recommendation (matches the wiki's existing Qwen precedent via [stretch_ai](entities/stretch-ai.md) + [ROSOrin](entities/rosorin.md)), vLLM as the serving stack, architecture sketch with Cloudflare/Tailscale exposure, cost ballpark, and open questions (retrieval strategy, conversation memory, tool use, update cadence, evaluation).

- **Cross-source insight**: The wiki's "Qwen + Ollama" local-LLM pattern (already in production for stretch_ai's LLM agent and the ROSOrin offline curriculum) generalizes cleanly to the wiki-self-hosting case. Qwen 2.5 72B at Q8 is the same family scaled up to fit Spark's 128 GB unified memory.

- **Updated**: [index.md](index.md) — new Projects-syntheses entry.

## [2026-05-17] ingest | Stretch 4 launch (Hello Robot purchase + product page)

User pointed at `hello-robot.com/purchase/` for **Stretch 4 details**. Hello Robot launched **Stretch 4 on 2026-05-12** — a generational jump from Stretch 3, not a point release.

- **Created**: [Stretch 4 launch source](sources/hello-robot-stretch-4-launch.md). Combines the purchase page (canonical pricing + accessories) with the product page (spec table) and the forum launch announcement (the most substantive published technical writeup). The official datasheet PDF returned 404 at ingest time.

- **Headline changes vs Stretch 3**:
  - **Mobile base: differential-drive → 3-wheel omnidirectional holonomic** (8" wheels for carpet/rug/threshold).
  - **~2× faster** across arm, lift, and base. **+10% reach** (horizontal + vertical).
  - **8 redundant DOF + gripper** (was 7).
  - **New 3DOF ambidextrous cobot-style wrist**; no external cabling; integrated Luxonis OAK-SR wrist depth.
  - **Sensor suite rebuilt**: dual hemispherical 3D LiDAR (>2M depth readings/sec), global-shutter fisheye RGB with 10 Hz RGB-D point cloud, 12 MP central RGB, OAK-SR at wrist.
  - **Power**: 512 Wh LiFePO4, 10× cycle life vs Stretch 3, 8 hr light-CPU runtime, self-charging dock.
  - **Compute split**: Intel Ultra 5 NUC (32 GB / 1 TB) as primary; **Jetson Orin NX is now a $2,495 optional accessory** (was bundled in Stretch 3).
  - **ROS 2 Jazzy** (was Humble); 100 Hz Stretch Body; MuJoCo-based self-collision avoidance; IMU overtilt detection.
  - **Pricing**: $20k → **$29,950** base; +$2,495 Jetson; +$1,495 dock / parallel gripper / spare battery. Fully-loaded research config approaches $40k.
  - **Certification**: still laboratory and research use only.

- **Updated**:
  - [Stretch entity](entities/stretch.md) — rewritten to make Stretch 4 the current generation; new spec table; generations table; Stretch 3 specs preserved as historical; sources 13→14.
  - [Hello Robot entity](entities/hello-robot.md) — current-product line updated to Stretch 4; ROS 2 Jazzy noted; sources 7→8.
  - [overview.md](overview.md) — Stretch row in the newcomer robots table updated to current price + Stretch 4 generation.
  - [Household robot decision — Stretch vs G1 synthesis](syntheses/platforms/household-robot-decision-stretch-vs-g1.md) — top-of-page callout noting Stretch 4 supersedes Stretch 3 in the analysis; recommendation unchanged but pricing gap to G1 widens.
  - [index.md](index.md) — new Sources entry.

- **Cross-source insight**: Hello Robot's Stretch 4 follows the same compute-split pattern the wiki articulates in the [Jetson Thor / DGX Spark synthesis](syntheses/platforms/jetson-thor-vs-dgx-spark.md) at a different scale — **deterministic control on CPU, AI inference on GPU/Jetson**. Stretch 3 mixed both onto one NUC; Stretch 4 separates them, with the Jetson now buyer-specified rather than always-included. Cheaper for control-only buyers; more expensive for AI-heavy workflows.

- **Open questions** (logged on the source page): policy transfer from Stretch 3 to Stretch 4 (the [Robot Utility Models](entities/robot-utility-models.md) / [OK-Robot](entities/ok-robot.md) / [Dobb·E](entities/dobb-e.md) results are all S2/S3 — Stretch 4's holonomic base + new wrist DOF make non-trivial action-space transfer); stretch_ai compatibility; what "Enterprise" tier means; home/clinical certification roadmap; gripper finger-force / max-base-speed specs (datasheet PDF needed).

## [2026-05-17] lint + ingest | Lint pass + JetPack 7 / Jetson Thor whitepaper-stand-in

User asked for a lint pass and approved all three suggested follow-ups: source-count drift fixes, overview.md formatting + Quick-stats refresh, and ingesting the dangling JetPack 7 whitepaper reference.

- **Lint findings** (382-page scan): 1 broken link (the JetPack 7 reference), 0 orphan pages, 4 source-count drifts (|diff|≥2), 1 stale claim (overview Quick-stats date), 4 minor overview.md formatting issues, 3 known knowledge gaps.

- **Ingest**: Created [JetPack 7.0 for Jetson Thor software-stack reference](sources/nvidia-jetpack-7-thor-whitepaper.md) as a stand-in for the never-published "whitepaper" the [Jetson Thor launch newsroom](sources/nvidia-jetson-thor-launch-newsroom.md) referenced. Combines two NVIDIA primary materials: the **2025-08-25 forum release announcement** (Jetson Linux 38.2 / kernel 6.8 / Ubuntu 24.04 / CUDA 13 / cuDNN 9.12 / TensorRT 10.13 / MIG / preemptible real-time kernel / SBSA / Holoscan Sensor Bridge / CSI-over-Ethernet) and the **2025-10-15 technical blog** on Thor's 7× post-launch generative-AI throughput improvement (NVFP4 + EAGLE-3 speculative decoding; Llama 3.3 70B 12.64 → 41.5 → 88.62 tok/s).

- **Factual correction caught during ingest**: [jetpack.md](entities/jetpack.md) previously claimed JetPack 7 paired with **Jetson Linux R37.x**. The actual pairing is **R38.2** (kernel 6.8, Ubuntu 24.04). Fixed on jetpack.md + jetson-thor.md + jetson-linux.md.

- **Lint cleanups applied**:
  - Source-count drift bumped on 4 pages: [vla-models](concepts/learning/vla-models.md) 20→22, [assistive-robotics](concepts/robotics/assistive-robotics.md) 20→22, [kona](entities/kona.md) 2→4, [nvidia-groot](entities/nvidia-groot.md) 13→15.
  - [overview.md](overview.md): fixed broken table row (TurtleBot 4 missing leading `|`), heading typo ("Where to else start" → "Where else to start"), grammar ("You're want" → "You want"), and refreshed Quick-stats (date 2026-05-15→2026-05-17; totals 334→383).

- **Updated entity pages** post-ingest:
  - [jetson-thor.md](entities/jetson-thor.md): software-stack section expanded with full JetPack 7 contents; new quantization-format list; new post-launch generative-AI throughput table; tags + sources 4→5; open-questions refreshed (added per-MIG-instance perf, JetPack 7.1 timeline).
  - [jetpack.md](entities/jetpack.md): JetPack 7 section rewritten with verbatim component versions, MIG / real-time kernel / SBSA / CoE callouts, and AI-serving-framework list; sources 6→7.
  - [jetson-linux.md](entities/jetson-linux.md): new "R38 line — Jetson Thor track" section with R36 vs R38 comparison table; sources 7→8.

- **Index + log**: new Sources entry under chronological Jetson cluster.

- **Result**: 0 broken links remain; all originally drifted source-counts now match; overview.md formatting clean; the wiki's JetPack 7 / Thor software story is now accurate (was R37, now correctly R38.2).

## [2026-05-17] query+synthesis | "List open-source robot AI research projects"

User asked for a grouped catalog of every open-source project tracked in this wiki, dropping the "community" qualifier (so big-lab open releases stay in — Meta FAIR's JEPAs, NVIDIA GR00T, DeepMind's MuJoCo, etc.). Filed as a synthesis page so the work compounds.

- **Created**: [Open-source robot AI research projects — landscape](syntheses/platforms/open-source-robot-ai-projects.md). Filed under `platforms/` as the loosest fit; explicitly notes scope (closed products excluded) and gaps (OpenVLA, RLHF-line open implementations, Voyager).
- **Categories**: LeRobot ecosystem; JEPA / world-model open code; open VLAs; BC baselines; Karpathy's pedagogical repos; whole-organism fly; open simulators + physics engines; Farama Foundation RL stack; open vision foundation models; OpenUSD; open generative models; open robot platforms; educational kits with open code; orgs that maintain the above.
- **Updated**: [index.md](index.md) — new entry under Platforms syntheses.

## [2026-05-17] ingest | Logical Intelligence Kona product page (primary source)

Follow-up to the morning's Aleph EBM video ingest. User pointed at `logicalintelligence.com/kona-ebms-energy-based-models` — the [Kona](entities/kona.md) product page, dated **2026-05-14**. **First primary-source coverage of Kona** in the wiki (everything prior was secondary).

- The page is short and marketing-light on architecture: no training procedure, no parameter count, no benchmark numbers. Its value is **verbatim positioning copy** ("Certainty, Not Probability." / "It does not predict likely outcomes. It enforces constraints." / "Replaces trust with proof") and the **live Sudoku demo** at `sudoku.logicalintelligence.com`.
- Methodologically interesting demo detail: **code execution is disabled for both Kona and LLMs** to prevent LLMs from brute-forcing Sudoku via a code interpreter. Without that control the comparison would be meaningless.
- "Kona evaluates the entire puzzle at once" + "all possible states of a system" language is consistent with **non-autoregressive whole-state evaluation** — corroborates the earlier framing from the Bodnia interview summary.

- **Created 1 source**: [Kona EBMs page](sources/2026-05-14-logical-intelligence-kona-ebms-page.md). Explicitly flagged as marketing-light; paired with the video source page for the substance.

- **Updated**:
  - [Kona](entities/kona.md): new "Logical Intelligence's own positioning" section with the verbatim quotes; new "Public demo" section linking to the Sudoku page; sources 1→2.
  - [Logical Intelligence](entities/logical-intelligence.md): sources 1→2; Mentioned-in updated.
  - [Aleph](entities/aleph.md): sources 1→2 (page name-checks Aleph as the orchestrator that "delivers verified reasoning today").
  - [Energy-based models](concepts/learning/energy-based-models.md): sources 4→5; added vendor-authored positioning to Key references.
  - [index.md](index.md): new source line at the top of chronological 2026-05 cluster.

- **Open questions still open from the morning's ingest** — this page doesn't close any of them. Architecture, training, inference procedure, and benchmark numbers all remain undocumented in this wiki. Need a real Kona tech report.

## [2026-05-17] ingest | "Aleph and Energy-Based Models: The AI That Refuses to Bullshit" (YouTube)

User dropped a YouTube URL (NYmXYF8A3Q4). Video page itself was gated (no transcript), but search + WebFetch surfaced the subject: an editorial commentary on **[Logical Intelligence](entities/logical-intelligence.md)**'s January 2026 launch and the May 2026 [Aleph](entities/aleph.md) PutnamBench result. Built the ingest from primary materials (Logical Intelligence blog, BusinessWire press release, an Eve Bodnia interview summary) and cited those as the substantive sources; the video itself enters as the entry-point.

- **Headline data points**:
  - **Aleph (GPT-5.2) hits 99.4% / 668-of-672 on [PutnamBench](concepts/learning/putnambench.md)** with Lean proofs (May 2026), beating ByteDance and Apple. Three-stage Plan → Prove → Refine agentic pipeline; Lean kernel as the deterministic verifier.
  - **[Kona](entities/kona.md)** = non-autoregressive **energy-based reasoning model**; 16M–200M parameters; reasons in abstract vector space, not language. Q1 2026 pilots in energy / advanced manufacturing / semiconductor.
  - **Leadership**: [Eve Bodnia](entities/eve-bodnia.md) CEO; [Yann LeCun](entities/yann-lecun.md) Founding Chair of Tech Research Board; Fields Medalist [Michael Freedman](entities/michael-freedman.md) Chief of Math; [Vlad Isenbaev](entities/vlad-isenbaev.md) Chief of AI; [Patrick Hillmann](entities/patrick-hillmann.md) CSO.

- **Notable disambiguation**: LeCun is **also** Founding Chair at Logical Intelligence — separate from his reported Executive Chairman role at [AMI Labs](entities/ami-labs.md). The wiki previously treated AMI Labs as LeCun's sole post-Meta affiliation. Updated [yann-lecun.md](entities/yann-lecun.md) note + Related sections to reflect both. Whether the two companies collaborate, are parallel, or one is a subsidiary is not addressed by any source.

- **Created 1 source**: [Aleph EBM video](sources/2026-05-aleph-ebm-refuses-bullshit-video.md). Transparent about ingest depth — the video page itself is gated; substantive technical claims are cited to Logical Intelligence blog + BusinessWire + Bodnia interview summary, not "the video says X."

- **Created 7 entities**: [Logical Intelligence](entities/logical-intelligence.md), [Aleph](entities/aleph.md), [Kona](entities/kona.md), [Eve Bodnia](entities/eve-bodnia.md), [Michael Freedman](entities/michael-freedman.md), [Vlad Isenbaev](entities/vlad-isenbaev.md) _stub_, [Patrick Hillmann](entities/patrick-hillmann.md) _stub_.

- **Created 4 concept pages**:
  - **[Energy-based models (EBMs)](concepts/learning/energy-based-models.md)** — long-overdue. The [IBC source page](sources/ibc-paper.md) explicitly flagged this gap in May 2025; [LeCun's 2022 AMI paper page](sources/lecun2022-path-towards-ami.md) flagged it as "worth creating." Page connects the three EBM applications in the wiki: IBC (BC), JEPA (predictive representation learning), Kona (reasoning) — same LeCun-line architectural commitment, three different problems.
  - **[Formal verification](concepts/learning/formal-verification.md)** — the "translate / propose / verify" pipeline; deterministic checker as the structural cure for hallucination.
  - **[Lean theorem prover](concepts/learning/lean-theorem-prover.md)** — stub focused on Aleph's use; Mathlib + tactic + term mode + kernel-determinism.
  - **[PutnamBench](concepts/learning/putnambench.md)** — the benchmark.

- **Updated**:
  - [Yann LeCun](entities/yann-lecun.md): added Logical Intelligence affiliation alongside AMI Labs in the org-change callout; new Related-section entries; Mentioned-in updated; tags + sources count 18→19.
  - [IBC source page](sources/ibc-paper.md): "Energy-based models (no entity page; could become one if more EBM-line work surfaces)" line replaced with a real concept-page link — that note has been load-bearing for a year.
  - [LeCun 2022 source page](sources/lecun2022-path-towards-ami.md): EBM-concept-page open question resolved; replaced with link to the new concept page.
  - [index.md](index.md): new source line (post-Welch Labs); new Companies entry (Logical Intelligence); new section "Reasoning / formal-verification models" under Entities for Aleph + Kona (they don't fit BC / VLA / WM); 4 new People entries; 4 new Concepts entries under Learning.

- **Cross-source insight**: The wiki now has **three distinct EBM applications** all downstream of LeCun's 2022 vision: IBC (imitation learning), JEPA (predictive representation learning), Kona (reasoning / constraint satisfaction). Same architectural commitment, three different problem domains, different training-side machinery at each. The new [EBM concept page](concepts/learning/energy-based-models.md) is the hub that connects them.

- **Caveats called out on the relevant pages**:
  - Cost/extrapolation claims about Kona are from a single founder interview summary; reproduced with attribution, not endorsement.
  - Reproducibility of Aleph + GPT-5.2 by third parties is unverified (the Lean proofs themselves are mechanically verifiable; the agent that produced them may require Logical Intelligence's hosted stack).
  - The video's own substance beyond the editorial framing is unverified — no transcript surfaced.

## [2026-05-16] query+ingest | Jetson Thor capabilities + DGX Spark comparison

User asked: can Jetson Thor run AI training programs, run Isaac Sim, and other apps that run on DGX Spark? Wiki had no Thor or DGX Spark entity page (Thor had been flagged in the Seeed hackathon ingest as parked-for-future). Did targeted web research and built out the cluster.

- **Headline answer**: Thor can run inference and edge fine-tuning brilliantly; **cannot run Isaac Sim or Isaac Lab even headless** (no RT cores — categorical Jetson-family limitation); cannot replace DGX Spark for clustered fine-tunes of large models. The correct mental model is **train on Spark, deploy on Thor**.

- Created 4 source pages:
  - [NVIDIA Jetson Thor product page](sources/nvidia-jetson-thor-product-page.md) — verbatim T5000 + T4000 specs.
  - [NVIDIA Blackwell-Powered Jetson Thor Now Available — Newsroom](sources/nvidia-jetson-thor-launch-newsroom.md) — 2025-08-25 launch, $3,499 dev kit, 12-partner adopter list, Jensen "ultimate supercomputer" quote.
  - [NVIDIA DGX Spark Hardware Overview](sources/nvidia-dgx-spark-hardware-overview.md) — GB10 SoC, 20-core ARM, 6144-CUDA-core Blackwell with 4th-gen RT cores, 128 GB LPDDR5X unified at 273 GB/s, ConnectX-7.
  - [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor — RS DesignSpark](sources/rs-designspark-isaac-sim-on-thor.md) — the authoritative "no RT cores → no Isaac Sim" reference, including headless-still-needs-RT.

- Created 2 entity pages:
  - [Jetson Thor](entities/jetson-thor.md) — 2560-core Blackwell, 14-core Neoverse-V3AE, 128 GB / 273 GB/s, 2070 FP4-sparse TFLOPS, 40–130 W; T4000 sibling; AGX Thor Dev Kit $3,499. Full table of "what Thor can / can't do."
  - [NVIDIA DGX Spark](entities/dgx-spark.md) — GB10 Grace Blackwell, 6144 CUDA + RT cores, 128 GB unified, ConnectX-7 pairing for 405B-param inference.

- Created 1 synthesis: [Jetson Thor vs DGX Spark — train on Spark, deploy on Thor](syntheses/platforms/jetson-thor-vs-dgx-spark.md) — TL;DR capability matrix, why-similar / why-not-substitutes, FP4-inversion footnote (Thor's headline FP4 is 2× Spark's because Thor is FP4-sparse-tensor-optimized for on-robot deploy), recommended decision tree.

- Updated:
  - [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md): new "Hardware requirements" callout naming RT cores as the gating capability; sources 7→8.
  - [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md): same RT-core inheritance note; train-on-RTX deploy-on-Jetson workflow; sources 7→8.
  - [NVIDIA](entities/nvidia.md): Thor + DGX Spark added to product surface; sources 26→29.
  - [NVIDIA GR00T](entities/nvidia-groot.md): Brev / Thor links wired through on the N1.5 hackathon-winner bullet.
  - [index.md](index.md): 4 new source entries, Jetson Thor + DGX Spark added to Controllers / edge AI compute, new synthesis under Platforms.

- **Cross-source insight**: Thor and DGX Spark have **identical** memory (128 GB LPDDR5X @ 273 GB/s), same GPU generation, similar AI throughput class, and similar sub-$5k price — but RT cores + form factor + ConnectX-7 turn them into **the two halves of one workflow**, not redundant SKUs. Thor's FP4-sparse-tensor throughput is actually ~2× Spark's, but this reflects Thor's edge-inference-quantized-model design point, not raw superiority.

- **Open data we couldn't pin down**: T5000/T4000 production-module pricing through distribution; real benchmark numbers for GR00T N1.5/N1.7 EA on Thor; JetPack 7.x release cadence; whether subsequent Jetson generations will ever add RT cores (NVIDIA hasn't signalled this).

## [2026-05-14] ingest | Karpathy's four pedagogical repos — micrograd, nanoGPT, nanochat, autoresearch
- Created [Andrej Karpathy](entities/andrej-karpathy.md) entity page — independent AI researcher/educator; formerly Tesla AI director + OpenAI founding member; in this wiki, the author of the four reference-implementation repos that anchor the curriculum's "now read the code" exit ramps.
- Created [karpathy/micrograd (2020)](sources/karpathy-micrograd.md) — scalar-valued autograd in ~100 lines + ~50-line NN library. The cleanest "I understand backprop" milestone available.
- Created [karpathy/nanoGPT (2022)](sources/karpathy-nanogpt.md) — minimal GPT training repo (~300-line `model.py` + ~300-line `train.py`); reproduces GPT-2 124M on 8XA100 in ~4 days. **Deprecated November 2025** per the repo README in favor of nanochat; flagged as such on the source page, with the recommendation to still use `nanoGPT/model.py` as the *architecture-reading* reference and nanochat for *training pipeline*.
- Created [karpathy/nanochat (2025)](sources/karpathy-nanochat.md) — full ChatGPT pipeline (tokenizer + pretrain + SFT + RL + chat UI) for ~$48 / 2 hours on 8XH100; single `--depth` complexity dial; "Time-to-GPT-2" speedrun leaderboard. Rows 5–6 of that leaderboard (2.02 → 1.80 → 1.65 hours) are the autoresearch-driven entries — the first public evidence of agent-driven leaderboard improvement.
- Created [karpathy/autoresearch (2026-03)](sources/karpathy-autoresearch.md) — Karpathy's March 2026 project: AI coding agent edits `train.py` (a simplified nanochat) overnight with a 5-min experiment budget per iteration, measuring val_bpb. ~12 experiments/hr / ~100 overnight. The "tool calls" are `edit / train / measure / keep-or-revert` — structurally identical to robotics LLM-agent patterns, but with a training pipeline as the skill library.
- Updated [Curriculum Module 1 — Neural networks and training](syntheses/curriculum/curriculum-01-neural-networks.md) — converted the bare `https://github.com/karpathy/micrograd` external link in §"Recommended reading" to a wiki source-page link.
- Updated [Curriculum Module 3 — Sequence models, attention, transformers](syntheses/curriculum/curriculum-03-attention-and-transformers.md) — converted the nanoGPT external link to the wiki source page; added a sentence flagging the November 2025 deprecation and pointing readers to [nanochat](sources/karpathy-nanochat.md) for the modern end-to-end training pipeline; also converted the Vaswani 2017 external link to the wiki source page now that it's ingested.
- Updated [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) — added a new "Non-robotics example: agent-driven ML research" section. Frames autoresearch as the same `LLM-emits-tool-calls-against-a-skill-library` control pattern as the robotics examples, but with `edit / train / measure / commit` as the tool primitives. Notes the Onchain AI Garage LeWM reproduction as an independent occurrence of the same pattern. Source count bumped 8→9.
- Updated [index.md](index.md) — added all four repos under Sources (chronological) at their respective dates; added Karpathy as a People entry.
- Cross-cutting frame: the four repos form a coherent 6-year pedagogical progression (autograd → architecture → training pipeline → agent-driven research on the training pipeline) that maps cleanly onto the curriculum modules (1 → 3 → 3 → LLM-agent concept). The most wiki-novel of the four is **autoresearch + the nanochat leaderboard rows 5–6** — the first public empirical evidence that an AI coding agent can produce measurable improvements on a frontier ML training pipeline, which is the same wiki-relevant phenomenon the recent [Onchain AI Garage LeWM reproduction](sources/onchain-ai-garage-lewm-reproduction.md) demonstrates from a different direction.

## [2026-05-14] ingest | Onchain AI Garage — LeWM reproduction video (2026-04-24, 27 min)
- Created [Onchain AI Garage — "I Reproduced LeCun's JEPA World Model That Doesn't Predict Tokens" (2026-04-24)](sources/onchain-ai-garage-lewm-reproduction.md) — first independent LeWM reproduction on record in the wiki. Trains LeWM on Two Room on an RTX 3060 (12 GB VRAM) in WSL2 using Claude Code as implementation assistant; 4 epochs / ~8 hours / **92% success rate vs paper's 97%**. First half doubles as a JEPA popular-explainer. Full transcript ingested (~26K chars, 1634 s).
- Updated [Curriculum Module 12 — LeWorldModel deep-dive](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — added a "Prior-art reproduction video" callout right after the Anchor exercise Part A (the reproduce-LeWM-PushT step).
- Updated [LeWorldModel — train and run howto](syntheses/world-models/leworldmodel-howto.md) — added an "Independent reproduction available" callout at the top; flagged that all four of the howto's documented gotchas (Python version, batch-128 OOM, WSL2 CUDA errors, throughput) were corroborated by the video.
- Updated [LeWM hello-world project scope](syntheses/projects/lewm-hello-world-project-scope.md) — added a "Prior-art reproduction" note: the Two Room reproduction is on the *weakest* of LeWM's environments, so a PushT consumer-GPU reproduction is still wiki-novel.
- Updated [index.md](index.md) — added the video under Sources (chronological), right after the Welch Labs explainer (now two video sources in the LeWM cluster).
- Cross-cutting frame: this video is the **first concrete empirical data point in the wiki that LeWM trains and produces paper-ballpark numbers on consumer hardware**. Everything before this was paper-derived. The pattern (plan in main session → handoff markdown → execute in WSL via Claude Code) is also a wiki-relevant generalizable template for any reproduction work.
- Open follow-up: the host's prediction-loss starting value (0.08) is much lower than the paper's (0.25) — could be Two Room being simpler, different normalization, or different default hyperparameters in `stable-worldmodel`. Worth pinning down if the wiki's own PushT reproduction is attempted.

## [2026-05-14] ingest | Two foundational arch papers — Transformer (Vaswani 2017) + Siamese (Bromley/LeCun 1993)
- Created [Attention Is All You Need (Vaswani et al., NeurIPS 2017)](sources/attention-is-all-you-need.md) — the Transformer paper. Architecture (encoder–decoder, `N=6`, `d_model=512`, `h=8`), scaled dot-product attention math, multi-head attention, sinusoidal positional encoding, complexity table (self-attention `O(1)` max path length vs RNN `O(n)`), training setup (Adam + warmup + inverse-sqrt LR), WMT 2014 results (28.4 BLEU EN-DE big, 41.8 BLEU EN-FR), Section 6.3 constituency parsing as the first transformer task-generalization signal. Positioned as the foundation under LLMs, ViTs, VLA action heads, JEPA predictors, BeT / VQ-BeT, Diffusion Policy backbones — i.e., everything past curriculum Module 3.
- Created [Bromley, Guyon, LeCun, Säckinger, Shah 1993 — Signature Verification using a "Siamese" TDNN](sources/bromley1993-siamese-signature-verification.md) — the original Siamese network paper, AT&T Bell Labs / NIPS 1993. Two weight-tied TDNN sub-networks + cosine head + `±1` targets for genuine:genuine vs genuine:forgery pairs; 80-byte credit-card-stripe template constraint. Architecturally continuous with the modern joint-embedding SSL family (Barlow Twins, VICReg, DINOv2/v3) and with JEPA (J/A = Siamese, P = predictor on top). LeCun is a co-author — the 1990s seed of his 2020s JEPA program.
- Created [Siamese network](concepts/world-models/siamese-network.md) concept page — defining property (weight-tied branches), variants (asymmetric / triplet / N-way), the rep-collapse failure mode that emerged when later SSL work tried to train Siamese networks *without* labels, current state (DINOv3 / V-JEPA / LeWM are all Siamese descendants). 5 sources at creation.
- Updated [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md) — added "the J/A in JEPA descend from the [Siamese network](concepts/world-models/siamese-network.md) family; JEPA's contribution is the P" framing at the top of "What 'Joint' means"; added Bromley 1993 to Mentioned in; sources 14→15.
- Updated [Yann LeCun](entities/yann-lecun.md) — added "Earlier work (AT&T Bell Labs era)" section featuring the 1993 Siamese paper; bumped sources 16→17.
- Updated [glossary.md](glossary.md) — new "Siamese network" entry between SGD and SIGReg; linked the existing Transformer entry to the new Vaswani 2017 source page.
- Updated [index.md](index.md) — added both papers under "Sources (foundational, out of chronological order)" (alongside Barlow 1961 / Barlow Twins / VICReg / LeCun 2022 / DINOv3); added Siamese network under Concepts; bumped LeCun source count.
- Cross-cutting frame: this ingest closes two of the wiki's largest "foundational reference" gaps. **Transformer** was the single most-referenced architecture in the curriculum (Module 3 + Modules 5–14) with no primary-source page. **Siamese network** was the architectural ancestor cited across the SSL / JEPA lineage with no primary source. Both are now anchored to their original papers.
- Notable historical observation: the same Yann LeCun who is the senior author on every modern JEPA paper this wiki tracks co-authored the original Siamese network paper as a young researcher at AT&T Bell Labs **33 years earlier**. The architecture is continuous (two weight-tied encoders + a head); only the loss has changed (cos = ±1 → contrastive → anti-collapse regularizer → predictor-in-latent-space). The Welch Labs explainer's "JEPA is LeCun continuing his 1990s Siamese-network research" framing is literally correct.

## [2026-05-10] ingest | LeRobot Worldwide Hackathon 2025 — All Winners HF Space
- Created [LeRobot Worldwide Hackathon 2025 — All Winners](sources/lerobot-worldwide-hackathon-2025-winners.md) — June 14–15, 2025; 916 team members; ~400 submissions; 30 ranked winners pulled from the `maringetxway/all-winners` HF dataset (filenames carry rank + team).
- Created [LeRobot Worldwide Hackathon 2025](entities/lerobot-worldwide-hackathon-2025.md) (event entity), [Hope Jr Arm](entities/hope-jr-arm.md) (stub — premium-tier prize hardware), [Remi Cadene](entities/remi-cadene.md) (LeRobot lead at HF).
- Updated [LeRobot](entities/lerobot.md) 3→4 sources; added ecosystem-scale snapshot (916 / 400 / 30 / 189 datasets / 12 models) and linked Cadene as the project lead.
- Updated [Hugging Face](entities/hugging-face.md) 3→4 sources; added robotics-adjacent people (Cadene, Wolf, Caous).
- Updated [LeKiwi](entities/lekiwi.md) 2→3, [SO-ARM101](entities/so-arm101.md) 3→4, [Seeed Studio](entities/seeed-studio.md) 1→2 — flagged hackathon usage. Key market signal: LeKiwi was prize hardware in 22 of 30 ranked positions (top-3 + 6th–24th).
- Added new index subsection "Events" with the hackathon entity. Added the source under chronological sources.
- Headline: this is the ecosystem-scale evidence for the LeRobot stack ingested in the prior commit — ~400 community-team submissions on a single weekend means the buy → assemble → teleop → train → deploy loop is being closed in practice, not just in research papers.

## [2026-05-10] ingest | LeRobot ecosystem — XLeRobot, LeKiwi (SIGRobotics-UIUC), Seeed tutorial
- Created [XLeRobot Documentation](sources/xlerobot-docs.md) — Vector Wang's $660 dual-arm household manipulator; 2× SO-ARM101 on LeKiwi-class base; built on LeRobot; v0.3.0 released 2025-08-30.
- Created [Seeed Studio LeRobot LeKiwi Wiki](sources/seeed-lekiwi-wiki.md) — end-to-end build/teleop/train tutorial; STS3215 motor / Raspberry Pi 5 / ACT-policy spec; Seeed distributes LeKiwi hardware.
- Created [LeKiwi GitHub (SIGRobotics-UIUC/LeKiwi)](sources/lekiwi-github.md) — 1,300+ stars; 3-wheel Kiwi-drive holonomic base; Apache 2.0; Dynamixel/Koch v1.1 alternative arm variant.
- Created entities: [LeRobot](entities/lerobot.md), [LeKiwi](entities/lekiwi.md), [XLeRobot](entities/xlerobot.md), [SO-ARM101](entities/so-arm101.md) (SO-ARM100 lineage), [Vector Wang](entities/vector-wang.md), [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md), [Seeed Studio](entities/seeed-studio.md), [The Robot Studio](entities/the-robot-studio.md), [Hugging Face](entities/hugging-face.md).
- Updated [Imitation learning](concepts/learning/imitation-learning.md) 17→20 sources; added "Frameworks and stacks" section comparing LeRobot vs. Stretch AI vs. research-code tiers.
- Updated [index.md](index.md) — new sources under "Sources (chronological)"; new entities in Robot platforms, Software stacks, Companies, People; ACT/LeRobot tier flagged as the dominant sub-$1k IL stack.
- Cross-cutting frame: the LeRobot stack is the **gluing-existing-pieces-together** answer to affordable mobile manipulation — SO-ARM101 (The Robot Studio) + LeKiwi (SIGRobotics-UIUC) + LeRobot (Hugging Face) composes into XLeRobot's $660 dual-arm rig. Distinct from the integrated-vendor approach of Hello Robot (Stretch) or Pollen Robotics (Reachy 2).
- Noted UIUC footprint: [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) (low-cost mobile manipulation, LeKiwi) and the [Driggs-Campbell lab](entities/katherine-driggs-campbell.md) (assistive navigation, DRAGON) are independent UIUC groups both relevant to accessible robotics.

## [2026-05-10] ingest | Four new PDFs (DRAGON, Huh accessibility, Schneiders domestic, PAR review published version)
- Created [DRAGON — Dialogue-Based Robot for Assistive Navigation (Liu et al. 2024)](sources/dragon-assistive-nav-2024.md) — IEEE RA-L 2024; UIUC/Driggs-Campbell; TurtleBot 2i + CLIP landmark grounding + dialogue + VQA for PwVI; N=5 user study.
- Created [Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](sources/huh2026-accessible-robot-comm.md) — CHI 2026 InterAI Workshop; cross-institutional (UC Berkeley × UT Austin × UW); observational (10 blind) + controlled (20 blind + 20 sighted) study; 6 design guidelines; mixed-initiative narration preferred by blind users; Cakmak among co-authors.
- Created [Domestic Robots and the Dream of Automation (Schneiders et al. 2021)](sources/schneiders2021-domestic-robots-automation.md) — CHI 2021; Aalborg University; 24 Danish households; task fragmentation finding; under-trust → co-located monitoring pattern; strict task division contradicts Forlizzi 2007 (flagged with warning callout).
- Updated [Physically Assistive Robots — Systematic Review (Nanavati et al. 2024)](sources/nanavati2024-physically-assistive-robots-review.md) — `raw/annurev-control-062823-024352.pdf` is the published Annual Review version of `raw/nanavati2024physically.pdf` (already ingested). Source page now references both files and incorporates §6 detail on interaction interfaces, levels of autonomy, and adaptation (resolves previously open question).
- Created entities: [Katherine Driggs-Campbell](entities/katherine-driggs-campbell.md), [Shuijing Liu](entities/shuijing-liu.md), [Mina Huh](entities/mina-huh.md), [Amy Pavel](entities/amy-pavel.md), [Roberto Martin-Martin](entities/roberto-martin-martin.md), [Huihan Liu](entities/huihan-liu.md), [Eike Schneiders](entities/eike-schneiders.md), [Tiago](entities/tiago.md).
- Updated entities: [Maya Cakmak](entities/maya-cakmak.md) 8→9 sources; [Yuke Zhu](entities/yuke-zhu.md) 1→2; [Amal Nanavati](entities/amal-nanavati.md) (added Huh 2026 cross-reference for §6.1.3 follow-up); [Franka Panda](entities/franka-panda.md) 9→10; [TurtleBot](entities/turtlebot.md) 1→2; [HCR Lab](entities/hcrlab.md) 8→9.
- Created new concept page [Accessible robot communication](concepts/robotics/accessible-robot-communication.md) — the output-interface side of HRI for non-visual users; 6 DGs from Huh et al. 2026; ties together DRAGON / Huh / Nanavati-review / Schneiders.
- Updated concept page [Assistive robotics](concepts/robotics/assistive-robotics.md) 13→16 sources; added "Communication and the output-interface gap" + "Domestic-robot precursors" sections.
- Updated [index.md](index.md) — added new sources/entities/concept; bumped source counts; added new highlights under "Assistive Robotics" block.
- Notable cross-citations: Huh et al. 2026 is positioned as direct response to Nanavati et al. 2024 §6.1.3 (output-interface gap); DRAGON 2024 documented as counter-example to "TurtleBot no longer in research" hypothesis on the TurtleBot page; Schneiders 2021 under-trust + co-location pattern flagged as conceptual precursor to the blind-user monitoring problem.

## [2026-05-09] ingest | Boston Dynamics blog: Tools for Your To Do List with Spot and Gemini Robotics
- Created [Tools for Your To Do List with Spot and Gemini Robotics](sources/bostondynamics-spot-gemini-robotics.md) — Boston Dynamics Spot-team engineers wired Gemini Robotics-ER 1.5 into Spot via a tool-call layer over the Spot SDK; 2025 hackathon demo (living-room cleanup); productized as AIVI-Learning with ER 1.6.
- Created [Boston Dynamics](entities/boston-dynamics.md) entity (parent company, Hyundai-owned) — first BD entity page; ties to Atlas/Spot/Stretch/Orbit/AIVI-Learning.
- Created [Spot](entities/spot.md) entity — commercial quadruped; Spot SDK as the integration surface; documented Gemini Robotics-ER and Meta object-retrieval integrations.
- Created [Gemini Robotics](entities/gemini-robotics.md) entity — Google DeepMind robot foundation models; full VLA + Gemini Robotics-ER (embodied-reasoning VLM that emits tool calls).
- Updated [Google DeepMind](entities/google-deepmind.md) — added Gemini Robotics section, Boston Dynamics partnership, source count 5→6.
- Updated [Meta FAIR](entities/meta-fair.md) — added cross-vendor Spot-for-object-retrieval reference, source count 6→7.
- Updated [Atlas](entities/atlas.md) — linked to new Boston Dynamics + Spot entity pages.
- Updated [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) — added Spot + Gemini Robotics-ER as a third concrete example; added note on "embodied reasoning" as vendor branding for the same architecture; source count 5→6.
- Updated [VLA models](concepts/learning/vla-models.md) — clarified Gemini Robotics two-variant structure (full VLA vs -ER VLM).
- Updated [index.md](index.md) — added new source/entities; removed Spot from "needs-page" backlog.

## [2026-05-09] synthesis | Five new assistive-robotics syntheses
- Filed [Levels of autonomy in assistive robotics](syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) — three orthogonal autonomy axes; HCR Lab finding cluster (HRI 2020 → Walker 2024 → Yang 2025 → Nanavati 2025); EUP-over-RUM stack as unbuilt integration target.
- Filed [Long-term in-home robot deployments](syntheses/assistive/long-term-in-home-robot-deployments.md) — depth-sorted table; reliability gradient (RLBench 89.4% → BEHAVIOR-1K 12.4%); only one home has ≥1 month deployment data.
- Filed [Stretch as the de-facto assistive-robotics platform](syntheses/assistive/stretch-as-assistive-platform.md) — six of seven in-home deployments use Stretch; eight features that compound; decision matrix for platform choice.
- Filed [DINO-WM on Stretch — concrete experiment plan](syntheses/projects/dino-wm-on-stretch-experiment.md) — sibling to LeWM-on-Stretch; lower-risk frozen-encoder variant; predictor-only training on RUM dataset; phase-by-phase plan.
- Filed [Underserved PAR domains — dressing, bathing, medication](syntheses/assistive/underserved-par-domains.md) — sub-capability decomposition; medication-fetcher ranked most tractable for independent researcher.
- Updated index.md Highlights and Syntheses sections.

## [2026-05-09] lint | Audit of recent Sonnet ingestion + counts/cascade fixes
- Audited HCR Lab ingest (6 papers, 2 entities, 2 concepts, 1 synthesis): coverage solid, citations rigorous, no contradictions found.
- Fixed: synthesis heading "Six blocking problems" → "Seven blocking problems" (had 7 problem sections).
- Synced index source counts: HCR Lab 2→8, Maya Cakmak 7→8, Anthropic 1→2, DINO-WM 5→6, V-JEPA 2 5→6.
- Cascaded `Mentioned in` updates: DINO-WM (added LeWM, LeWM-GitHub, JEPA-WMs, DINO-world, VLA-JEPA), V-JEPA 2 (added JEPA-WMs, VLA-JEPA, towardsai-lecun).
- Anthropic frontmatter sources 1→2.
- No broken markdown links across 196 wiki pages. No orphan pages.
- Remaining drift between frontmatter `sources:` and `Mentioned in` lists for ~40 pages — bookkeeping-only, not load-bearing for retrieval.

## [2026-05-09] edit | index.md Highlights restructure
- Added "Assistive Robotics" highlights block (after AI Safety and Alignment)
- Moved "General" to end of Highlights list
- Moved Log link to bottom of index.md

## [2026-05-09] ingest | Stanford HAI AI Index Report 2026
- Created [Stanford HAI — AI Index Report 2026](sources/stanford-hai-ai-index-2026.md)
- New entity: [Physical Intelligence](entities/physical-intelligence.md) — π0/π0.6 VLAs
- Updated [Figure](entities/figure.md): added BMW deployment data (11 months, 1,250+ hr, 90k+ parts, 30k vehicles); sources 0→1
- Updated [VLA models](concepts/learning/vla-models.md): added π0/π0.6 + Gemini Robotics; added research-stage assessment from AI Index; sources 8→9
- Updated [Sim-to-real transfer](concepts/learning/sim-to-real-transfer.md): added quantified gap table (89.4% RLBench vs 12.4% BEHAVIOR-1K); sources 8→9
- Updated [Assistive robotics](concepts/robotics/assistive-robotics.md): added BEHAVIOR-1K 12.4% household task success section; sources 4→5
- Updated [Assistive robotics synthesis](syntheses/assistive/assistive-robotics-research-landscape.md): updated reliability gap framing with BEHAVIOR-1K numbers

## [2026-05-09] query | Assistive robotics R&D landscape and JEPA applicability
- Filed [Assistive robotics — R&D landscape and JEPA applicability](syntheses/assistive/assistive-robotics-research-landscape.md)
- Synthesized from: assistive-robotics concept, ok-robot, robot-utility-models, stretch, jepa-task-capabilities, v-jepa-2, dino-wm, vla-jepa

## [2026-05-09] ingest | Learning Control-Oriented Dynamical Structure from Data (ICML 2023)
- Created [learning-control-oriented-dynamical-structure](sources/learning-control-oriented-dynamical-structure.md) (arXiv 2302.02529)
- New entity: [Navid Azizan](entities/navid-azizan.md) — connects to MIT drone adaptive control source
- Updated [MIT drone adaptive control](sources/mit-drone-adaptive-control.md): linked prior work + Azizan entity

## [2026-05-09] ingest | UAVs Meet Agentic AI survey + MIT drone adaptive control
- Created [UAVs Meet Agentic AI survey](sources/uavs-agentic-ai-survey.md) (arXiv 2506.08045)
- Created [MIT drone adaptive control](sources/mit-drone-adaptive-control.md) (MIT News, 2025-06-09)
- New concept: [Agentic UAVs](concepts/robotics/agentic-uavs.md) — 4-layer architecture, 8 domains, adaptive control thread

## [2026-05-09] ingest | mega-batch: OK-Robot, OVMM, Stretch assistive, TurtleBot 4, Elephant Robotics, Fauna, 1X NEO, Reachy 2, assistive-robotics cluster, K-Scale Labs
- New sources (13): ok-robot-project-page, ovmm-homerobot, ieee-spectrum-stretch-assistive, clearpath-turtlebot-4, elephant-robotics-myagv-compound, elephant-robotics-mybuddy-280, fauna-robotics-sprout, 1x-neo-product-page, pollen-robotics-reachy, itu-aiforgood-assistive-robots, virginia-tech-assistive-robotics-lab, relab-ethz-tenoexo, robot-report-kscale-labs-lessons
- New entities (8): ok-robot, elephant-robotics, myagv, mybuddy-280, fauna-robotics, pollen-robotics, reachy, k-scale-labs
- New concept: assistive-robotics
- Updated entities: 1x-neo (stub → primary specs), turtlebot (stub → TurtleBot 4 specs), stretch (+price, OVMM/OK-Robot/assistive use cases), hello-robot (+Aaron Edsinger, Charlie Kemp, assistive, OVMM), lerrel-pinto (+OK-Robot), mahi-shafiullah (+OK-Robot)
- Skipped (failed/403): Reachy Mini HuggingFace, RobotShop myAGV Pro, Understanding Deep Learning book

## [2026-05-09] ingest | batch: ALE + LeWM GitHub + V-JEPA 2 GitHub + 3 secondary articles
- Created [Arcade Learning Environment — Farama Project Page](sources/ale-farama.md)
- Created [LeWorldModel GitHub](sources/lewm-github.md)
- Created [V-JEPA 2 GitHub](sources/vjepa2-github.md)
- Created [Towards AI — LeCun / AMI Labs](sources/towardsai-lecun-ami-labs.md) (secondary, provisional)
- Created [MLWorks — LeWM Navigate the World](sources/medium-lewm-navigate-world.md) (secondary, paywalled)
- Created [Towards Deep Learning — World Model Learns Physics](sources/towardsdeeplearning-world-model-physics.md) (secondary, paywalled)
- New entity: [Arcade Learning Environment](entities/ale.md)
- New entity: [AMI Labs](entities/ami-labs.md) (provisional — single secondary source)
- Updated [Yann LeCun](entities/yann-lecun.md): noted reported departure from Meta + AMI Labs founding (hedged)
- Updated [V-JEPA 2](entities/v-jepa-2.md): added variant family table (ViT-L/H/g → ViT-B–G), 80M–2B param range, V-JEPA 2.1 training additions, dual license
- Updated [LeWorldModel](entities/leworldmodel.md): added architecture component list (ViT+AR Predictor+action encoder+SIGReg), baseline list (PLDM/LeJEPA/IVL/IQL/GCBC/DINO-WM), MIT license
- Updated [Farama Foundation](entities/farama-foundation.md): ALE now links to entity page

## [2026-05-09] ingest | New Video Series: What Developers Need to Know About OpenUSD
- Created [nvidia-openusd-developer-video-series](sources/nvidia-openusd-developer-video-series.md)
- Updated [OpenUSD](entities/openusd.md): added Hydra pipeline section; bumped to 5 sources

## [2026-05-09] query | "What does 'Joint' refer to in JEPA?"
- Updated [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md): added "What 'Joint' means" section explaining joint embedding, the shared-encoder design, and contrast with generative architectures.

## [2026-05-06] bootstrap | Wiki initialized
- Created three-layer structure: `raw/`, `wiki/`, `CLAUDE.md`.
- Configured for the robot research domain.
- Subfolders: `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`.
- Index and log seeded; no sources ingested yet.

## [2026-05-06] research | Robot simulators for agentic robot software development
- Web survey via 7 search queries on the 2026 simulator landscape (no sources dropped into `raw/` — all from web).
- **Source pages created** (10): [NVIDIA Newton Physics Engine Developer Page](sources/nvidia-newton-physics-engine-developer-page.md), [NVIDIA Newton Contact-Rich Manipulation Blog](sources/nvidia-newton-contact-rich-manipulation-blog.md), [MuJoCo Playground Paper](sources/mujoco-playground-paper.md), [Genesis Project Page](sources/genesis-project-page.md), [AGIBOT Genie Sim 3.0 Announcement](sources/agibot-genie-sim-3-announcement.md), [AGIBOT Genie Envisioner 2.0 Announcement](sources/agibot-genie-envisioner-2-announcement.md), [Genie Envisioner Paper](sources/genie-envisioner-paper.md), [RoboCasa365 Paper](sources/robocasa365-paper.md), [ManiSkill-HAB Paper](sources/maniskill-hab-paper.md), [Top 10 Physical AI Models 2026](sources/top-10-physical-ai-models-2026.md).
- **Entity pages created** (14): [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md), [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md), [Newton physics engine](entities/newton-physics-engine.md), [MuJoCo Playground](entities/mujoco-playground.md), [Genesis](entities/genesis.md), [AGIBOT Genie Sim 3.0](entities/agibot-genie-sim.md), [RoboCasa](entities/robocasa.md), [ManiSkill](entities/maniskill.md), [NVIDIA Cosmos](entities/nvidia-cosmos.md), [Genie Envisioner](entities/genie-envisioner.md), [AGIBOT](entities/agibot.md), [NVIDIA](entities/nvidia.md), plus stubs for [NVIDIA GR00T](entities/nvidia-groot.md) and [Google DeepMind](entities/google-deepmind.md).
- **Concept pages created** (3): [VLA models](concepts/learning/vla-models.md), [Sim-to-real transfer](concepts/learning/sim-to-real-transfer.md), [World-model simulators](concepts/world-models/world-model-simulators.md).
- **Synthesis page created** (1): [Simulators for agentic robotics — 2026 landscape](syntheses/simulators/simulators-for-agentic-robotics-2026.md).
- Five-category framing: (1) core GPU physics platforms, (2) embodied-AI / household-scale platforms, (3) world-model simulators, (4) classic / ROS-native, (5) industry usage signals.
- **Open question logged**: GR00T version inconsistency (N1.6 GA vs. N1.7 EA) flagged as a contradiction in the synthesis and on the GR00T stub.
- **Coverage gaps captured in index** under "Known gaps / TBD": Drake, Gazebo/Webots/CoppeliaSim/PyBullet, Pi (Physical Intelligence), Skild AI, LIBERO, RoboMimic, SAPIEN, Hillbot, Disney Research.

## [2026-05-07] lint | Wikilink convention migration
- Issue: my initial pages used bare `[[Display Title]]` wikilinks but kebab-case filenames, so Obsidian couldn't resolve them and created empty placeholder files at the vault root for [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md), [NVIDIA Newton Physics Engine Developer Page](sources/nvidia-newton-physics-engine-developer-page.md), and [World-model simulators](concepts/world-models/world-model-simulators.md).
- Resolution: deleted the 3 zero-byte orphans; rewrote all wikilinks across 28 pages to the explicit `[[slug|Display]]` form via `sed`.
- CLAUDE.md updated with the filename convention (kebab-case slugs) and the wikilink convention (always slug-pipe-display, never bare display).

## [2026-05-07] lint | Wiki health check pass
- Deleted second Obsidian orphan: `wiki/Genie Envisioner Paper.md` (empty 0-byte file).
- Reconciled NVIDIA mention drift: added `[NVIDIA](entities/nvidia.md)` to [AGIBOT Genie Sim 3.0 Announcement](sources/agibot-genie-sim-3-announcement.md)'s "Entities mentioned" list, since the source genuinely discusses NVIDIA's stack via Isaac Sim and GR00T.
- Bumped `sources` counts on 7 entity pages whose frontmatter under-counted actual inbound source-page wikilinks: [AGIBOT Genie Sim 3.0](entities/agibot-genie-sim.md) (1→3), [Genesis](entities/genesis.md) (1→2), [Genie Envisioner](entities/genie-envisioner.md) (2→3), [MuJoCo Playground](entities/mujoco-playground.md) (1→2), [Newton physics engine](entities/newton-physics-engine.md) (2→3), [NVIDIA Cosmos](entities/nvidia-cosmos.md) (2→3), [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) (2→3). Mirrored counts in `index.md`.
- No content contradictions found beyond the already-tracked GR00T N1.6/N1.7 EA version overlap.
- Deferred to user: whether to stub frequently-mentioned-but-unstubbed entities (Hillbot, SAPIEN, Disney Research).

## [2026-05-07] stubs | Filled three lint-flagged entity gaps
- Created stub pages for [Hillbot](entities/hillbot.md) (UCSD spinoff, ManiSkill maintainer), [SAPIEN](entities/sapien.md) (simulation framework underlying ManiSkill), and [Disney Research](entities/disney-research.md) (Newton co-developer).
- Converted bare text mentions to wikilinks across `entities/maniskill.md` (Hillbot + SAPIEN ×3), `entities/newton-physics-engine.md`, `entities/google-deepmind.md`, `entities/nvidia.md`, `syntheses/simulators-for-agentic-robotics-2026.md` (Hillbot + SAPIEN + Disney in the Newton table cell), and added entries to `Entities mentioned` sections in `sources/maniskill-hab-paper.md` (Hillbot, SAPIEN) and `sources/nvidia-newton-physics-engine-developer-page.md` (Disney Research).
- Removed the three corresponding rows from `index.md` "Known gaps / TBD"; added the new stubs to Companies / Simulators sections.
- Updated synthesis "Coverage gaps" to drop SAPIEN (now stubbed); Drake remains.

## [2026-05-07] ingest | Hello Robot ecosystem (4 sources)
- **Sources ingested**: [Hello Robot Stretch Documentation](sources/hello-robot-stretch-docs.md) (https://docs.hello-robot.com/0.3/), [Robot Utility Models Project Page](sources/robot-utility-models-website.md) (https://robotutilitymodels.com/), [Stretch AI LLM Agent Documentation](sources/stretch-ai-llm-agent-docs.md) (github.com/hello-robot/stretch_ai), and `raw/22486_RoboCasa365_A_Large_Scal.pdf` — re-ingested with deeper detail (the existing [RoboCasa365 Paper](sources/robocasa365-paper.md) page was rewritten).
- **PDF tooling**: poppler-utils binaries weren't on PATH; `pypdf` was available, used a short Python script to extract pages 1–3 of the PDF. Found ICLR 2026 conference paper, full author list (Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu), and richer numbers (612 hr human + 1615 hr synthetic via [MimicGen](entities/mimicgen.md); 500K+ trajectories; 60 distinct activities behind the 365 tasks).
- **New entity pages** (5): [Hello Robot](entities/hello-robot.md) (company), [Stretch](entities/stretch.md) (robot), [stretch_ai](entities/stretch-ai.md) (software stack), [Robot Utility Models](entities/robot-utility-models.md) (method), [MimicGen](entities/mimicgen.md) (tool, stub).
- **New concept pages** (2): [Imitation learning](concepts/learning/imitation-learning.md), [LLM-agent architecture](concepts/agents/llm-agent-architecture.md).
- **Updated existing pages**: [RoboCasa](entities/robocasa.md) (added ICLR 2026 / authors / NVIDIA / MimicGen), [NVIDIA](entities/nvidia.md) (sources 4→5; new "Research arm" bullet about Yuke Zhu's NVIDIA Research affiliation on RoboCasa365), [VLA models](concepts/learning/vla-models.md) (sources 4→6; new "Adjacent: utility models" section noting RUMs and stretch_ai's LLM agent are non-language-conditioned alternatives), [Sim-to-real transfer](concepts/learning/sim-to-real-transfer.md) (sources 2→3; RoboCasa365 added as benchmark), and the synthesis (new section 6 "Real-robot agentic stacks" highlighting stretch_ai and RUM as the consumer-side counterweight to sim-heavy paths).
- **Index reorganized**: added "Robot platforms", "Software stacks", and "Tools" subsections under Entities; renamed "VLA models" → "VLA models / generalist policies"; added 5 new TBD items (TRI LBM, Octo, Stretch Mujoco, xArm 7, RUM/Hello Robot people).
- **New cross-source insight**: Aaron Edsinger (Hello Robot co-founder) is a co-author on the RUM paper — concrete vendor / academic collaboration explicitly bridging the hardware vendor to the generalist-policy research agenda.

## [2026-05-07] ingest | JEPA papers (V-JEPA 2 + LeWorldModel)
- **Sources ingested** (2): [V-JEPA 2 Paper](sources/v-jepa-2-paper.md) (`raw/JEPA_2506.09985v1.pdf`, arXiv 2506.09985, June 2025) and [LeWorldModel Paper](sources/leworldmodel-paper.md) (`raw/LeWorldMode_2603.19312v2.pdf`, arXiv 2603.19312v2, March 2026). Both extracted via pypdf.
- **New entity pages** (4): [V-JEPA 2](entities/v-jepa-2.md), [LeWorldModel](entities/leworldmodel.md), [Meta FAIR](entities/meta-fair.md), [Mila](entities/mila.md) (stub).
- **New concept page** (1): [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md) — umbrella architecture for both papers.
- **Restructured concept**: [World-model simulators](concepts/world-models/world-model-simulators.md) now organized as two explicit paradigms — Paradigm A (generative-video: Cosmos, Genie Envisioner) and Paradigm B (JEPA / latent-prediction: V-JEPA 2, LeWorldModel). Sources 2→4.
- **Synthesis updates**: section 3 split into 3a (generative-video) and 3b (JEPA / latent-prediction); intro reads "Six categories" (was "Five"); sources list refreshed to include the four sources added since the last synthesis update (stretch-ai docs, RUM website, V-JEPA 2, LeWorldModel).
- **Cross-link**: [NVIDIA Cosmos](entities/nvidia-cosmos.md) now cross-references the JEPA line as the contrasting paradigm.
- **Cross-source insight**: Yann LeCun is senior author on both papers — JEPA is his program, executed across two distinct teams (Meta FAIR for V-JEPA 2; Mila + NYU + Samsung + Brown for LeWM). The two papers represent **different points in the same design space**: V-JEPA 2 is large-scale + frozen-encoder + post-training; LeWM is small + end-to-end + simple. Together they argue JEPA is robust across scale.
- **Quantitative contrast captured**: V-JEPA 2 trains on **1M+ hours** with **1B parameters**; LeWM uses **15M parameters** on a single GPU. 60-70× model-size delta and ~5 orders of magnitude data delta — yet both are JEPAs and both demonstrate the paradigm.
- **TBD added**: DINO-WM, Dreamer/DreamerV3, TD-MPC, PLDM (world-model baselines from LeWM), Droid dataset (V-JEPA 2-AC training), Habitat (Meta), and a low-priority people-pages note (LeCun, Edsinger, Shafiullah, Zhu, Assran).

## [2026-05-07] ingest | Hiwonder ROSOrin documentation
- **Source ingested**: [Hiwonder ROSOrin Documentation](sources/hiwonder-rosorin-docs.md) (https://docs.hiwonder.com/projects/ROSOrin/en/jetson-orin-nano-version/). User specifically asked to include the Gazebo section; pulled chapter 9 (Gazebo) and chapter 10 (Large AI Models incl. Embodied AI + offline) by curl + Python parsing of the Sphinx HTML. WebFetch's summarizer truncated the AI chapter mid-page on first attempts; raw curl + grep was needed for sections 10.3–10.5.
- **New entity pages** (4): [Hiwonder](entities/hiwonder.md) (stub), [ROSOrin](entities/rosorin.md) (full), [Ollama](entities/ollama.md) (stub), [Qwen](entities/qwen.md) (stub but cross-references stretch_ai).
- **No new concept pages** — content fits the existing [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) concept.
- **Updated existing**: [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) (sources 1→2; added ROSOrin as a second concrete example, noting the pattern is converging across research and educational tiers); [stretch_ai](entities/stretch-ai.md) (sources 2→3 from new ROSOrin-docs cross-reference); [stretch_ai LLM Agent Documentation](sources/stretch-ai-llm-agent-docs.md) (wikilinked Qwen instead of bare text; corrected vendor attribution from "Tencent" to Alibaba); synthesis section 6 (added ROSOrin as the educational-tier counterpart to stretch_ai); synthesis sources list refreshed.
- **Index reorganized**: added "LLMs" subsection under Entities; expanded Robot platforms (now Stretch + ROSOrin); added Hiwonder to Companies; added Ollama to Tools.
- **Concrete agentic-AI tooling captured**:
  - **Cloud LLMs** in ROSOrin chapter 10: GPT-4o, GPT-4o-mini, gpt-4o-transcribe, Whisper-1, OpenAI TTS (tts-1/tts-1-hd/gpt-4o-mini-tts), Qwen-plus-latest, StepFun multimodal (Chinese fallback path).
  - **Offline stack**: ollama serve + qwen3:1.7b + sherpa-onnx (CUDA) + matcha-icefall-zh-baker (Chinese TTS) + vits-ljs (English TTS).
  - **Embodied-AI control loop**: LLM emits `{action: [...], response: ...}` JSON, executor runs `eval(f'self.{a}')` per action — security-questionable but a clear standard recipe.
- **Cross-source convergence insight**: stretch_ai (research, Hello Robot) and ROSOrin (education, Hiwonder) independently default to small Qwen variants (2.5-3B and 3:1.7b) for their LLM-agent planners. The same JSON tool-call architectural pattern is shared across two unrelated stacks. The wiki now treats this as a confirmed pattern rather than a single data point.
- **TBD added**: Gazebo entity page (referenced by both Hello Robot and Hiwonder docs; previously was a passing mention), TurtleBot (canonical educational ROS robot), StepFun (Chinese multimodal AI), sherpa-onnx (offline ASR/TTS toolkit), WonderEcho Pro (Hiwonder voice module), Hiwonder's chapter 7 vision/CV curriculum (YOLOv11 + TensorRT — could be its own ingest).

## [2026-05-07] ingest | ROSOrin Pro / OpenClaw (manipulation-capable Hiwonder variant)
- **Sources ingested** (2): [Hiwonder ROSOrin Pro User Manual](sources/hiwonder-rosorin-pro-user-manual.md) (chapter 1) and [Hiwonder OpenClaw Practical Tutorial](sources/hiwonder-openclaw-tutorial.md) (chapter 13). The overview-page URL the user supplied was browsed for TOC structure but not filed as a separate source page (per scope choice — it was largely TOC).
- **New entity pages** (3): [ROSOrin Pro](entities/rosorin-pro.md) (the kit), [OpenClaw](entities/openclaw.md) (the LLM-agent framework — software, not hardware despite the "Claw" suffix), [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md) (stub for the HX-12H-servo manipulator hardware).
- **Updated existing**: [ROSOrin](entities/rosorin.md) (added Pro variant to Related), [Hiwonder](entities/hiwonder.md) (sources 1→3; documented the two-doc-domain split — `docs.hiwonder.com` for base, `wiki.hiwonder.com` for Pro), [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) (sources 2→3; added OpenClaw as third concrete example, generalized the convergence claim from "across tiers" to "across tiers and capabilities"), synthesis section 6 (extended ROSOrin bullet to cover the Pro variant + OpenClaw), synthesis sources list, index (added rosorin-pro, rosorin-pro-arm, openclaw under their respective sections; bumped Hiwonder source count and reorganized so Hiwonder appears earlier in Companies).
- **Hardware specs captured** (now reusable for future ingests): COIN-D6 LiDAR, Deptrum Aurora930 depth + RGB camera, MPU6050 IMU, HX-12H bus servos, STM32F407VET6 low-level MCU, 11.1 V 6000 mAh battery.
- **Concrete OpenClaw skill surface captured**: ROS 2 services `/start_pick`, `/place`, `/claw_track_and_grab/start`, `/claw_track_and_grab/set_color`, topics `~/arm_group_control`, `~/chassis_command`, `/controller/cmd_vel`. Action groups: `voice_pick`, `voice_give`, `init`, `camera_up`. Functions: `parse_twist()`, `pick()`, `place_function()`, `obj_track_proc()`. Vision: LAB-color thresholding + PID visual servoing + AprilTag (ID 0/1) + depth-based interactive grasping (Jetson Orin only).
- **Cross-source convergence insight strengthened**: The LLM-agent pattern is now demonstrated across **three independent stacks** — [stretch_ai](entities/stretch-ai.md) (Hello Robot, research, mobile + arm), [ROSOrin](entities/rosorin.md) (Hiwonder, education, mobile-only), and [OpenClaw](entities/openclaw.md) (Hiwonder, education, mobile + arm). Same JSON tool-call architecture, same skill-library dispatch model. The claim has shifted from "this might be a pattern" to "this is the pattern" for non-VLA agentic-robotics deployment in 2026.
- **Notable absences in OpenClaw curriculum**: no VLA models (no OpenVLA/GR00T/RT-X/Pi), no LeRobot, no ACT or Diffusion Policy, no imitation learning, no teleoperation, no demonstration collection. Confirms the bifurcation already noted in the synthesis: VLA work happens in research labs (NVIDIA, Pi, Meta-via-RUM); deployed agentic stacks use LLM-orchestrated skill libraries.
- **Open question logged**: doc references `openai/gpt-5.4` — unclear if real OpenAI release or doc placeholder. Worth checking on the next OpenAI-related ingest.
- **TBD additions**: HX-12H, COIN-D6, Deptrum Aurora930, MPU6050 — hardware-component pages added as a single TBD line in the index (deferred until they recur).

## [2026-05-07] synthesis | LLM-agent architecture across stacks
- Filed [LLM-agent architecture across stacks — a converged pattern](syntheses/agents/llm-agent-architecture-across-stacks.md).
- Three-way side-by-side comparison of [stretch_ai](entities/stretch-ai.md), [ROSOrin](entities/rosorin.md), and [OpenClaw](entities/openclaw.md). Goes beyond the umbrella [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) concept by drawing structural implications — Qwen as the de-facto local default, JSON-shaped tool calls as the provider-portability layer, the bifurcation between research VLA stacks and deployed LLM-agent stacks.
- Surfaced two implementation hazards: `eval`-on-LLM-output dispatch in both Hiwonder stacks, and under-documented closed-loop replanning across all three.
- Open questions filed: no Claude backend anywhere; cross-vendor portability of skill libraries; whether VLAs eventually displace primitives without changing the orchestrator pattern.

## [2026-05-07] synthesis | Generative-video vs JEPA world models
- Filed [Generative-video vs JEPA world models](syntheses/world-models/generative-video-vs-jepa-world-models.md).
- Deep comparison of paradigms A and B from [World-model simulators](concepts/world-models/world-model-simulators.md). Five-table treatment: what each predicts, cost/speed, data scale, demonstrated real-robot results, failure modes — plus when-to-use guidance and a cross-paradigm interaction note (GR00T using Cosmos backbone; V-JEPA 2 encoder feeding multimodal LLMs).
- Anchored on the 48× planning-speed gap (LeWM) and the V-JEPA 2-AC zero-shot Franka result as the strongest published cross-paradigm validation.
- Open questions filed: no published head-to-head; GE-Sim2 zero-shot transfer evidence missing; JEPA scaling-law shape between 15M and 1B params; whether action-conditioned generative video can match V-JEPA 2-AC's data-efficiency.

## [2026-05-07] lint | Post-synthesis health check
- Cross-checked wikilinks: all 34 unique slugs referenced from the two new syntheses resolve to existing files. No broken links anywhere in the wiki (the only "Referenced but no file" hit was the literal `slug` example inside CLAUDE.md docs).
- No new orphan pages created by these syntheses.
- No source-count drift to fix — syntheses do not appear in `Mentioned in` sections by convention.
- One normalization: synthesis #1 originally used escaped pipes (`\|`) inside markdown-table wikilinks for delimiter safety; rewrote to unescaped `|` to match the rest of the wiki (the existing simulators synthesis uses unescaped pipes inside tables and renders correctly in Obsidian).
- No content contradictions detected between the two new syntheses and existing pages.
- Standing open items unchanged: GR00T N1.6 GA vs N1.7 EA contradiction, Pi / Skild AI coverage gap, Drake / Gazebo entity pages.

## [2026-05-07] synthesis | Newton + OpenUSD substrate convergence
- Filed [Newton + OpenUSD — the substrate convergence](syntheses/simulators/newton-openusd-substrate-convergence.md).
- Argues the structural unusual-ness of a physics engine designed as a backend pluggable into both NVIDIA Isaac Lab and DeepMind's MuJoCo Playground, with OpenUSD as the shared scene format and Linux Foundation as the vendor-neutral governance layer. Implication: physics layer commoditizes, ML differentiation moves up the stack to environment APIs / learning frameworks / VLAs.
- Disney Research's role flagged as the puzzle piece — entertainment-grade physics keeping Newton's contact / soft-body models honest beyond industrial robotics.
- Open questions filed: real cross-stack adoption demo not yet ingested; throughput-parity comparisons absent; whether MuJoCo Playground defaults to Newton or keeps MJX as primary; Disney's specific contributions still opaque.

## [2026-05-07] synthesis | Sim-heavy vs real-data paths to generalist policies
- Filed [Sim-heavy vs real-data paths to generalist policies](syntheses/simulators/sim-heavy-vs-real-data-paths.md).
- Reframes the simulator survey's "sim-vs-real divide" as a three-path comparison: Path A (sim-heavy synthetic-data scaling — RoboCasa365, Genie Sim 3.0), Path B (real-data viewpoint-locked — RUM), Path C (observation pretraining + small interaction — V-JEPA 2-AC). Different data-substitution bets, different scaling axes.
- Empirical asymmetry surfaced: Path B and Path C have published zero-shot real-robot results in unseen environments (RUM 90% on 5 tasks; V-JEPA 2-AC zero-shot Franka in 2 labs); Path A's evidence in the wiki is mostly intra-sim. The wiki has not ingested deep VLA-deployment results that would close this gap.
- Concrete number captured: RoboCasa365's 2.6× synthetic-to-human ratio is the wiki's only data point on Path A's optimal sim/real mix.
- Open questions filed: Pi / Skild positioning on this map; synthetic-ratio plateau; missing direct head-to-head training the same architecture across all three paths.

## [2026-05-07] lint | Final health check after four syntheses
- Cross-checked wikilinks: all slugs referenced from the four new syntheses resolve. The only "Referenced but no file" hit remains the literal `slug` example inside CLAUDE.md docs.
- No orphan pages created across the four syntheses.
- No escaped pipes (`\|`) anywhere in `wiki/syntheses/`; convention is consistent.
- Added a "Deeper dives" cross-reference section at the bottom of the simulator survey pointing to the four follow-up syntheses, since each takes one section of the survey further. Bumped the survey's `updated` to 2026-05-07.
- Synthesis count: 1 (survey, updated) + 4 (new) = 5 on file.
- No content contradictions detected between the four new syntheses or between them and the simulator survey. The standing GR00T N1.6 GA / N1.7 EA inconsistency is referenced consistently across pages.
- Standing TBD items unchanged: Pi (Physical Intelligence), Skild AI, Drake internals, classic VLA benchmarks (LIBERO / RoboMimic). The four new syntheses surface these gaps from new angles but do not fill them.

## [2026-05-07] research | OpenUSD as a robotics scene/physics format
- User asked to research OpenUSD as a scene-description format for simulators, then asked to also explore SolidWorks-to-OpenUSD conversion. Web search (4 queries) + WebFetch (4 successful + 1 403) + 1 follow-up search.
- **Sources ingested** (4): [OpenUSD Rigid Body Physics Proposal](sources/openusd-rigid-body-physics-proposal.md) (openusd.org, 2020 v1.0), [Using OpenUSD for Modular and Scalable Robotic Simulation](sources/nvidia-openusd-for-robotic-simulation.md) (NVIDIA blog 2025-03-18 by Aaron Luk, Pomi Lee, Renato Gasoto), [URDF vs MJCF vs USD comparison](sources/source-robotics-urdf-mjcf-usd-comparison.md) (Source Robotics blog 2026-03-13), [Building CAD-to-USD Workflows with NVIDIA Omniverse](sources/nvidia-cad-to-usd-jt-workflows.md) (NVIDIA blog 2025-07-29 by Justine Lin).
- **New entity page** (1): [OpenUSD](entities/openusd.md) — covers the format, the UsdPhysics schema, MjcPhysics + newton-usd-schemas extensions, and CAD ingestion paths.
- **Updated existing**: [Google DeepMind](entities/google-deepmind.md) (sources 2→3; documented authorship of the `MjcPhysics` USD plugin and `mujoco-usd-converter`); [Newton physics engine](entities/newton-physics-engine.md) (sources 3→4; added the `newton-usd-schemas` repo and the schema-promotion-into-UsdPhysics design); [Newton + OpenUSD substrate convergence synthesis](syntheses/simulators/newton-openusd-substrate-convergence.md) (substantial enrichment — added the "OpenUSD as physics schema" section, the "DeepMind authors USD plugins" section, the "CAD ingestion — the upstream half" section, and updated the convergence table to include physics-schema and CAD-ingestion rows).
- **Key new claims captured**:
  - **UsdPhysics is robotics-aware in the standard**. `PhysicsArticulationRootAPI` distinguishes "floating articulations" (mobile/aerial robots) from "fixed articulations" (industrial arms bolted down) — robotics jargon explicitly recognized in the OpenUSD spec.
  - **DeepMind ships USD schema plugins**, not just consumes USD. `MjcPhysics` is a DeepMind-maintained USD plugin authoring MuJoCo-specific solver attributes onto USD prims.
  - **`newton-usd-schemas` is a "proving ground"** — physics parameters generalizable across two Newton solvers may be promoted upstream into `UsdPhysics`. v0.2.0 released **2026-05-07** (the same day as this ingest), 52 commits, 7 releases — actively maintained.
  - **`mujoco-usd-converter`** lives in the `newton-physics` GitHub org, hosting the cross-stack bridge in vendor-neutral governance.
  - **CAD-to-USD geometry preservation is good; kinematic-joint preservation is the open question**. None of the ingested CAD sources documents automated SolidWorks-mate-to-`PhysicsJoint` conversion.
  - **Isaac Sim 5.0 / Omniverse Kit SDK 107 → OpenUSD 24.05**.
- **Open questions logged**: ABB/FANUC/KUKA/Yaskawa GTC 2026 adoption needs a primary source; URDF/MJCF/SDFormat → OpenUSD conceptual mapping shipping status; engineering.com 403 redo.
- **Skipped sources** (deliberately): Okino SolidWorks-to-USD page (thin), newton-usd-schemas GitHub README (folded into the Newton entity page).

## [2026-05-07] lint | Post-OpenUSD-ingest health check
- All wikilinks resolve; no orphan pages; no escaped pipes in new content.
- **Source-count drift fixed** on six entity pages whose frontmatter under-counted inbound source-page references after the ingest: [NVIDIA](entities/nvidia.md) 5→8, [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) 2→4, [Newton physics engine](entities/newton-physics-engine.md) 3→4 (already in ingest commit), [NVIDIA Cosmos](entities/nvidia-cosmos.md) 4→5, [Google DeepMind](entities/google-deepmind.md) 2→3 (already in ingest commit), [Disney Research](entities/disney-research.md) 1→2. Mirrored counts in `index.md`.
- **Removed a stray `Mentioned in` entry**: I had added `openusd-rigid-body-physics-proposal` under [Newton](entities/newton-physics-engine.md)'s "Mentioned in" but that source page does not list Newton in its "Entities mentioned" — only OpenUSD and NVIDIA. Removed.
- **Added missing `Mentioned in` entries**: appended the four new sources to the relevant entity pages (NVIDIA, Isaac Sim, Cosmos, Disney Research, Newton, DeepMind) per the convention.
- DeepMind's `_stub_` marker dropped from index since the entity page now has 3 sources and substantive content (MjcPhysics + Newton + MuJoCo).

## [2026-05-07] synthesis | LeWorldModel — train and run howto
- Filed [LeWorldModel — train and run howto](syntheses/world-models/leworldmodel-howto.md) from `lucas-maes/le-wm` README + project page.
- Updated [LeWorldModel Paper](sources/leworldmodel-paper.md): added `code` and `project_page` frontmatter; resolved the "code/website URLs missing" open question; added a Code & artifacts section.
- Updated [LeWorldModel](entities/leworldmodel.md): added Code section + howto link; bumped sources 1 → 2.
- Updated [index.md](index.md): filed howto under Syntheses.

## [2026-05-07] update | LeWorldModel howto: install gotchas added
- Installed and verified `quentinll/lewm-pusht` end-to-end on RTX 5070 / WSL2 / Python 3.10.
- Updated [LeWorldModel — train and run howto](syntheses/world-models/leworldmodel-howto.md) with a Gotchas section covering four real snags: gym 0.21.0 PEP 440 metadata, box2d-py SWIG dep, datasets resolved to 1.1.1, and the README conversion script's missing `_target_` filter.
- Expanded the "use pretrained" section with the actual HF→`_object.ckpt` conversion script + the `strip_target` fix.

## [2026-05-07] ingest | Farama Foundation Projects Page
- Source: [Farama Foundation Projects Page](sources/farama-projects-page.md) (https://farama.org/projects).
- New entities (focused scope): [Farama Foundation](entities/farama-foundation.md), [Gymnasium](entities/gymnasium.md), [PettingZoo](entities/pettingzoo.md), [Gymnasium-Robotics](entities/gymnasium-robotics.md).
- Cross-referenced gym/gymnasium gotchas in [LeWM howto](syntheses/world-models/leworldmodel-howto.md) to the new Gymnasium entity.
- Deferred: Minari, Metaworld, Shimmy, MO-Gymnasium, MOMAland, MAgent2, MPE2, Minigrid, MiniWoB++, ViZDoom, ALE, HighwayEnv, Procgen2, Stable-Retro, Jumpy — listed in index "Known gaps" with the source page as the canonical reference.

## [2026-05-07] ingest | Gymnasium-Robotics Documentation
- Source: [Gymnasium-Robotics Documentation](sources/gymnasium-robotics-docs.md) (https://robotics.farama.org/).
- Expanded [Gymnasium-Robotics](entities/gymnasium-robotics.md) from stub to real entity: confirmed MuJoCo backend (new bindings, not legacy mujoco-py), enumerated all six env families (Fetch, Shadow Hand, Maze, Adroit, Franka Kitchen, MaMuJoCo), added install snippet.
- Bumped source counts: gymnasium-robotics 1→2, gymnasium 1→2, farama-foundation 1→2.
- Added six env families to "Known gaps" for on-demand promotion (Adroit + Franka Kitchen most likely to surface, given D4RL / RoboCasa365 evaluation traditions).

## [2026-05-07] lint | Source-count drift fixes + MuJoCo entity
- Fixed source counts: [LeWorldModel](entities/leworldmodel.md) 2→1 (synthesis pages don't count per schema); [PettingZoo](entities/pettingzoo.md) 1→2; [MuJoCo Playground](entities/mujoco-playground.md) 3→5; [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) 3→4. Index updated to match.
- New entity: [MuJoCo](entities/mujoco.md) — the physics engine itself (was a 110-mention gap). 7 source pages reference it; entity covers `mujoco` vs `mujoco-py` vs MJX vs MJCF, history (Roboti → DeepMind 2021), and ecosystem role.
- Qualified the speculative "single-process CPU MuJoCo" claim on [Gymnasium-Robotics](entities/gymnasium-robotics.md) with a `> [!note]` callout — the docs root didn't actually state CPU-only.
- No broken wikilinks, no orphans, no contradictions surfaced.

## [2026-05-07] synthesis | OpenUSD support across simulators
- Filed [OpenUSD support across simulators](syntheses/simulators/openusd-support-across-simulators.md) — reference catalog of which simulators consume USD natively (Isaac Sim/Lab, Genie Sim 3.0), via plugin (MuJoCo via MjcPhysics + mujoco-usd-converter), as substrate (Newton via newton-usd-schemas), or not at all (Genesis, ManiSkill/SAPIEN, Gymnasium-Robotics).
- Companion to [Newton + OpenUSD — the substrate convergence](syntheses/simulators/newton-openusd-substrate-convergence.md) (structural argument) and [OpenUSD entity](entities/openusd.md) (format reference). Compiles the per-simulator answer into a single grep-able page.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-07] synthesis | Why JEPA research skips the simulator stack
- Filed [Why JEPA research skips the simulator stack](syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) — synthesis observing that V-JEPA 2 and LeWorldModel both avoid heavy agentic-robotics simulators (Isaac Lab, MuJoCo Playground, ManiSkill, RoboCasa, Genesis).
- V-JEPA 2: internet video pretrain → real Droid teleop post-train → real Franka zero-shot eval (no sim anywhere). LeWM: trains/evals on PushT/cube/two-rooms/reacher (lightweight 2D/3D control benches, not real-robot sim).
- Four plausible reasons: (1) JEPA's data thesis is observation-scale, internet video beats sim; (2) latent-space prediction sidesteps pixel-level sim-to-real gap; (3) Droid removes sim's data-multiplier role; (4) test-of-truth is real-robot zero-shot.
- Caveats explicit: sample size of two; `stable-worldmodel` env zoo may extend further than ingested; future JEPA work may converge back into sim once it scales up.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-07] ingest | Five JEPA / JEPA-adjacent papers (probe of original synthesis)
- Triggered by: user query "find more information about JEPA and LeWorldModel and probe whether these methods use simulations." Research agent surfaced one paper that contradicts the original ["JEPA skips sim" synthesis](syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) and four more that broaden the picture.
- New sources:
  - [JEPA-WMs Paper](sources/jepa-wms-paper.md) (Terver, Yang, Ponce, Bardes, LeCun — FAIR, Dec 2025) — **first JEPA-for-robotics paper this wiki has ingested using heavy sim**: RoboCasa kitchen manipulation + 42 Metaworld tasks + Push-T + PointMaze + DROID + real Franka.
  - [V-JEPA 2.1 Paper](sources/v-jepa-2-1-paper.md) (Mur-Labadia et al. — FAIR + Mila, Mar 2026) — "dense features"; +20pt real-Franka grasping per secondary research; sustains the no-sim line.
  - [DINO-WM Paper](sources/dino-wm-paper.md) (Zhou, Pan, LeCun, Pinto — NYU + FAIR, Nov 2024) — DINOv2 patch features + zero-shot planning on PushT/Wall/PointMaze/Rope/Granular/Reacher.
  - [VLA-JEPA Paper](sources/vla-jepa-paper.md) (Sun et al., Feb 2026) — JEPA-as-auxiliary inside VLA on LIBERO + SimplerEnv + real.
  - [DINO-world Paper](sources/dino-world-paper.md) ("Back to the Features", Baldassarre et al. — FAIR, Jul 2025) — DINOv2 video world model; Basile Terver bridge author to JEPA-WMs.
- New entities: [JEPA-WMs](entities/jepa-wms.md), [DINO-WM](entities/dino-wm.md), [VLA-JEPA](entities/vla-jepa.md), [DINO-world](entities/dino-world.md).
- Updated entities: [Meta FAIR](entities/meta-fair.md) sources 1→5, expanded JEPA-program description to include both encoder-co-trained (V-JEPA family) and frozen-DINOv2 (DINO-WM/DINO-world/JEPA-WMs) lines; [V-JEPA 2](entities/v-jepa-2.md) sources 1→2 + V-JEPA 2.1 successor note; [RoboCasa](entities/robocasa.md) sources 1→2 with JEPA-WMs cross-reference; [MuJoCo](entities/mujoco.md) sources 6→7 (DINO-WM uses it).
- Updated concept: [JEPA](concepts/world-models/jepa.md) sources 2→7; added all 5 new instances; added "Simulator stance — fragmenting, not avoiding" section; cross-referenced revised synthesis.
- Index updated: 5 new sources under chronological list, 4 new world-model entities, JEPA concept source-count bump, JEPA-related expansion gaps section added.

## [2026-05-07] synthesis | Major revision — Why JEPA research skips the simulator stack
- Rewrote [the synthesis](syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) in response to JEPA-WMs ingest (which directly contradicts the original claim).
- New framing: JEPA literature **fragments across four sim weight classes** (none / lightweight / mid-weight / heavy), not "skips sim wholesale." Original V-JEPA 2 + LeWM observation is correct for those papers but does not generalize.
- Each sim weight class explained by paper-specific question (representation learning vs. training-method vs. VLA-eval vs. physical-planning benchmark).
- The four "why" hypotheses from the original draft re-labeled: only (a) "internet-scale video > sim" has direct primary-source backing; (b)/(c)/(d) are wiki-author inference, not paper rationale.
- Two corrections folded in: `stable-worldmodel` env zoo includes DM Control + Gymnasium-Robotics Fetch (broader than the LeWM howto exposed); DINO-world → JEPA-WMs share research lineage via Basile Terver bread-crumb.
- New "watch item": first JEPA paper to explicitly train inside Isaac Lab or MuJoCo Playground (RoboCasa happened in Dec 2025; those two haven't yet).

## [2026-05-07] entity | DROID dataset
- Created [DROID](entities/droid.md) entity page — Distributed Robot Interaction Dataset, 350 hr / 76k traj / 564 scenes / 86 tasks of Franka Panda teleop across 13 institutions; lead authors Khazatsky + Pertsch, senior Finn + Levine. Source: project page at https://droid-dataset.github.io/.
- Captured the OXE comparison (DROID +22% in-dist / +17% OOD vs Open-X Embodiment policies) and the BridgeV2/RH20T/RT-1 "order of magnitude more scenes" claim.
- Wikilinked DROID across [V-JEPA 2](sources/v-jepa-2-paper.md) and [JEPA-WMs](sources/jepa-wms-paper.md) sources so Mentioned-in flows correctly.
- Index updated: added Datasets subsection under Entities; removed DROID from Known gaps. Added Franka Panda + DROID-paper-itself to Known gaps as follow-ups.
- Open: DROID **paper itself** (arxiv 2403.12945) not yet a source page; license terms not surfaced; Dec 2024 / Apr 2025 update deltas not documented.

## [2026-05-07] entities | Batch 1 — Franka Panda + Metaworld + DINOv2 + PushT + 3 people + world-model concept
- Filed 8 pages in one batch in response to "recommend entities, then file batch 1":
  - [Franka Panda](entities/franka-panda.md) — 7-DOF research arm; default tabletop manipulator across DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM. (4 sources)
  - [Metaworld](entities/metaworld.md) — Yu/Quillen/Levine/Finn 2019 meta-RL benchmark; 50 manipulation tasks on simulated Sawyer; staple in JEPA-WMs (42 tasks) + MuJoCo Playground. (3 sources)
  - [DINOv2](entities/dinov2.md) — Meta FAIR self-supervised ViT (Oquab et al. 2023); 142M images, ViT-S/B/L/g; substrate for DINO-WM, DINO-world, JEPA-WMs. Apache 2.0. (3 sources)
  - [PushT](entities/pusht.md) — 2D T-block pushing benchmark; introduced by IBC (Florence et al. 2021), popularized by Diffusion Policy (Chi et al. 2023). Default lightweight bench across LeWM / DINO-WM / JEPA-WMs. (3 sources)
  - [Yann LeCun](entities/yann-lecun.md) — Meta VP, NYU, Turing Award 2018; senior on V-JEPA 2 / V-JEPA 2.1 / LeWM / DINO-WM / DINO-world / JEPA-WMs. (6 sources)
  - [Adrien Bardes](entities/adrien-bardes.md) — FAIR; co-senior on V-JEPA 2 / V-JEPA 2.1 / JEPA-WMs; the FAIR-side champion of the V-JEPA program. (3 sources)
  - [Basile Terver](entities/basile-terver.md) — bread-crumb author across DINO-world (Jul 2025) → JEPA-WMs (Dec 2025), the lineage signal called out in the JEPA-skips-sim synthesis. (2 sources)
  - [World model](concepts/world-models/world-model.md) — broad concept page, distinct from the narrower [World-model simulators](concepts/world-models/world-model-simulators.md) companion. Covers generative-video / JEPA / frozen-feature / model-based-RL design points. (11 sources)
- Sources for these pages were drawn from the existing wiki + a small primary-source pass on Metaworld (project page), DINOv2 (GitHub README), PushT (Diffusion Policy project page).
- Primary sources note: people pages (LeCun, Bardes, Terver) are written from the wiki's own author-overlap context plus widely-known facts; primary-source bio fetches deferred.
- Index updated: new Vision foundation models subsection (DINOv2); new People subsection (LeCun, Bardes, Terver); Franka Panda added under Robot platforms; Metaworld + PushT added under Simulators / frameworks; World-model concept added at top of Concepts.
- Known gaps cleaned: Franka Panda removed; Metaworld removed from Farama gap list; LeCun removed from People-low-priority list. Added new gaps surfaced by ingest: Sergey Levine, Chelsea Finn, Karl Pertsch, Alexander Khazatsky, Lerrel Pinto, Pulkit Agrawal as future people pages.
- Open: bidirectional source-to-entity cross-links (e.g. adding [Yann LeCun](entities/yann-lecun.md) under "Entities mentioned" in V-JEPA 2 + LeWM + DINO-WM + DINO-world + JEPA-WMs source pages) **not done in this pass** — would tighten the graph but isn't load-bearing for retrieval. Worth a future lint pass.

## [2026-05-08] lint | Comprehensive fix pass
Triggered by user "fix everything" request after lint report.

### Source-count drift fixes (10 entities)
All 10 cases were missing Mentioned-in entries, not inflated declared counts. Added:
- agibot-genie-sim: + maniskill-hab-paper
- genesis: + nvidia-newton-physics-engine-developer-page
- genie-envisioner: + agibot-genie-sim-3-announcement, v-jepa-2-paper
- mujoco-playground: + farama-projects-page, source-robotics-urdf-mjcf-usd-comparison
- newton-physics-engine: + mujoco-playground-paper
- nvidia-cosmos: + nvidia-newton-contact-rich-manipulation-blog, v-jepa-2-paper
- nvidia-isaac-lab: + dino-wm-paper, farama-projects-page, maniskill-hab-paper (and bumped declared 4→5)
- rosorin: + hiwonder-rosorin-pro-user-manual
- stretch-ai: + hiwonder-openclaw-tutorial, hiwonder-rosorin-docs
- nvidia-groot: bumped declared 2→3 (Mentioned-in already had 3)

### Bidirectional cross-links (batch 1 entities → 7 source pages)
Updated Entities-mentioned / Concepts-touched in v-jepa-2-paper, v-jepa-2-1-paper, dino-wm-paper, dino-world-paper, jepa-wms-paper, leworldmodel-paper, robot-utility-models-website, vla-jepa-paper to wikilink yann-lecun, adrien-bardes, basile-terver, franka-panda, metaworld, dinov2, pusht, world-model where applicable.

### Stub markers cleared (5 entities)
hiwonder, pettingzoo, rosorin-pro-arm, nvidia-groot, qwen — content substantive, _stub_ marker removed from index. Also removed `status: stub` from nvidia-groot frontmatter. Genuinely thin stubs left as-is: mila, disney-research, hillbot, sapien, ollama, mimicgen.

### Filed 11 new entities to close lint gaps
Sims/benchmarks: [LIBERO](entities/libero.md), [SimplerEnv](entities/simplerenv.md), [DM Control Suite](entities/dm-control.md), [PointMaze](entities/pointmaze.md), [Habitat](entities/habitat.md).
Software: [stable-worldmodel](entities/stable-worldmodel.md) — Python infrastructure under LeWorldModel; clarifies the LeWM-vs-stable-worldmodel boundary; documents the broader env zoo (DM Control + Gymnasium-Robotics Fetch + …) understated in the LeWM howto.
People: [Lerrel Pinto](entities/lerrel-pinto.md), [Sergey Levine](entities/sergey-levine.md), [Chelsea Finn](entities/chelsea-finn.md), [Yuke Zhu](entities/yuke-zhu.md), [Karl Pertsch](entities/karl-pertsch.md) — top cross-paper authors surfaced by lint.
Updated meta-fair entity to wikilink the new Habitat page.

### Deferred from this pass
PLDM, TD-MPC, Dreamer/DreamerV3 baseline stubs — kept in known-gaps; primary-source confirmation needed before filing.
DROID/Metaworld/DINOv2 papers as standalone source pages — entities are filed; primary-source ingest deferred to next pass.

### What lint still flags
- Source-count drift detector noise: my actual-count algorithm includes synthesis pages and entity pages in the Mentioned-in count, while the schema's `sources:` field counts source pages only. The 10 fixes above all addressed real missing entries; future drift checks should filter to source-page targets only.

## [2026-05-08] synthesis | JEPA task capabilities
- Filed [JEPA task capabilities](syntheses/world-models/jepa-task-capabilities.md) in response to user query "what tasks can a JEPA model perform?"
- Reference index, not analytical synthesis: maps 7 JEPA / JEPA-adjacent papers (V-JEPA 2, V-JEPA 2.1, LeWM, DINO-WM, DINO-world, VLA-JEPA, JEPA-WMs) to 7 task categories: real-robot manipulation, navigation, planning-as-cost-function, video understanding, dense vision, video prediction, probing/interpretability.
- Includes a per-task per-model matrix, structural notes (cost-function-not-policy framing, no pixel generation, sim weight class independence), and a "what JEPA doesn't yet do" gap list.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | LeWM on ROSOrin Pro — feasibility analysis
- Filed [LeWM on ROSOrin Pro — feasibility analysis](syntheses/projects/lewm-on-rosorin-pro-feasibility.md) in response to user query "can LeWM be adapted to ROSOrin Pro?"
- Combines [LeWM](entities/leworldmodel.md) entity + [howto](syntheses/world-models/leworldmodel-howto.md) + [stable-worldmodel](entities/stable-worldmodel.md) with [ROSOrin Pro](entities/rosorin-pro.md) hardware + [OpenClaw](entities/openclaw.md) orchestration into a deployment-feasibility analysis.
- Verdict: feasible but research-grade. Five blockers documented (action-space mismatch, no teleop pipeline, LeWM not yet validated on real robots, no Gazebo wrapper for stable-worldmodel, partial sensor integration). Five enabling factors documented (compute footprint, planner latency, no reward shaping, OpenClaw-as-orchestrator architectural fit, cheap-training iteration).
- Recommended path: tabletop pushing in Gazebo first, retrain LeWM with 8-D action space, deploy with image-goal MPC.
- Architectural precedent: [RUM](entities/robot-utility-models.md)-on-[Stretch](entities/stretch.md) is the closest "low-cost robot + learned-from-data policy" blueprint, even though it's BC not JEPA.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] ingest | Robot Utility Models full paper (arxiv 2409.05865)
- Source: [Robot Utility Models Paper](sources/robot-utility-models-paper.md) — full paper companion to the existing project-page source. PDF at `raw/robot_utility_models_2409.05865v1.pdf`.
- Extracted via pypdf (per memory note on broken pdftotext).
- New paper-body content vs project page:
  - **Architecture**: VQ-BeT + Diffusion Policy as top performers; ACT + MLP-BC as baselines. ResNet34 vision encoder initialized from Dobb·E HPR; transformer policy trunk; 500 epochs on 2× A100.
  - **Stick-v2 details**: iPhone Pro + $25 BOM, 60 Hz RGB+depth, 100 Hz 6D pose via ARKit, no SLAM, no calibration. Trained gripper-aperture predictor from RGB.
  - **2,950 robot rollouts** across NYC / Jersey City / Pittsburgh.
  - **Performance breakdown**: 74.4% from raw VQ-BeT policy + 15.6% from gpt-4o-2024-05-13 retry → 90% headline.
  - **Cross-embodiment**: Stretch → xArm 7 with ~10pt drop (tissue 80%→70%, bag 84%→76%).
  - **Three data-recipe lessons**: data > algorithm; diversity > quantity (25 demos × many envs > 200 × few); expert > non-expert (co-training can hurt).
- Updated entities: [Robot Utility Models](entities/robot-utility-models.md) (1→2 sources, expanded with new architecture + ablation detail), [Lerrel Pinto](entities/lerrel-pinto.md) (2→3), [Franka Panda](entities/franka-panda.md) (4→5), [Stretch](entities/stretch.md) (3→4), [Hello Robot](entities/hello-robot.md) (3→4).
- Updated concept: [Imitation learning](concepts/learning/imitation-learning.md) (2→3).
- Index: filed under Sources chronological; all source-count bumps reflected.
- The paper provides the empirical backing for the [LeWM-on-ROSOrin-Pro feasibility](syntheses/projects/lewm-on-rosorin-pro-feasibility.md) synthesis's "RUM-on-Stretch is the closest deployment-shape precedent" claim.

## [2026-05-08] entities | 5 follow-up pages from RUM-paper ingest
- Created entity pages for the gaps surfaced at the end of the RUM-paper ingest:
  - [xArm 7](entities/xarm-7.md) — UFactory 7-DOF arm; RUM cross-embodiment transfer target.
  - [Dobb·E](entities/dobb-e.md) — NYU predecessor to RUM (Shafiullah et al. 2023, arxiv 2306.16650). HPR encoder + Stick-v1 + Homes of New York dataset.
  - [VQ-BeT](entities/vq-bet.md) — Vector-Quantized Behavior Transformer (Lee et al. 2024); top performer in RUM ablation.
  - [Diffusion Policy](entities/diffusion-policy.md) — Chi et al. 2023 (arxiv 2303.04137); introduced/popularized PushT + UMI gripper.
  - [Mahi Shafiullah](entities/mahi-shafiullah.md) — NYU + Hello Robot; lead author on Dobb·E and RUM.
- All 5 marked as `_stub_` in the index — primary sources not yet ingested for any of them; they're anchored in existing wiki context (mostly RUM-paper references).
- Updated [RUM paper source](sources/robot-utility-models-paper.md) to wikilink the 5 new entities under "Entities mentioned." Updated [PushT](entities/pusht.md) to wikilink Diffusion Policy. Updated [Lerrel Pinto](entities/lerrel-pinto.md) to add Dobb·E + Shafiullah-as-advisee.
- Index: new "Behavior-cloning methods" subsection added under Entities. xArm 7 added under Robot platforms. Dobb·E added under VLA models / generalist policies (alongside RUM). Shafiullah added under People.
- Known gaps cleaned: xArm 7 removed; Mahi Shafiullah removed from People-low-priority list. New gaps surfaced: Cheng Chi, Seungjae Lee, plus standalone source pages for Dobb·E / VQ-BeT / Diffusion Policy / IBC.

## [2026-05-08] entity + synthesis | TurtleBot + robot-platforms comparison
- Created [TurtleBot](entities/turtlebot.md) entity (stub). Four generations (2010 Willow Garage, 2012 Yujin, 2017 Robotis, 2022 Clearpath/iRobot). The educational-tier reference point that [ROSOrin](entities/rosorin.md) / [ROSOrin Pro](entities/rosorin-pro.md) succeed in modern form.
- Created [Robot platforms — comparison](syntheses/platforms/robot-platforms-comparison.md) synthesis. At-a-glance table for the 6 robot entities currently filed (Franka Panda, xArm 7, Stretch, ROSOrin Pro, ROSOrin, TurtleBot) sorted by tier (research / educational) and type (tabletop / mobile-manipulator / mobile-no-arm). Cross-tier observations on data availability, software-stack maturity, and the educational-tier convergence on "Jetson + LLM agent + ROS 2."
- Flagged missing platforms in the wiki: humanoids (Atlas, Optimus, Unitree, AGIBOT humanoid line), iRobot Create 3, ALOHA/ViperX bimanual, UR5/UR10, xArm 6.
- Index updated: TurtleBot added under Robot platforms; robot-platforms-comparison filed under Syntheses; TurtleBot removed from Known gaps.

## [2026-05-08] entities + synthesis | Humanoid robots batch + iRobot Create 3
- Created 10 humanoid entity stubs covering closed-development tier ([Atlas](entities/atlas.md), [Tesla Optimus](entities/tesla-optimus.md), [Figure](entities/figure.md), [1X NEO](entities/1x-neo.md)), industrial-deployed ([Apptronik Apollo](entities/apptronik-apollo.md), [Digit](entities/digit.md)), affordable research ([Unitree H1](entities/unitree-h1.md), [Unitree G1](entities/unitree-g1.md)), and educational ([NAO](entities/nao.md), [TonyPi](entities/tonypi.md)).
- Created [iRobot Create 3](entities/irobot-create-3.md) entity — Roomba-i3-derived ROS 2 mobile-robot base; chassis under [TurtleBot 4](entities/turtlebot.md). Cross-linked from TurtleBot entity.
- Filed [Humanoid platforms survey](syntheses/platforms/humanoid-platforms-survey.md) synthesis — companion to [Robot platforms — comparison](syntheses/platforms/robot-platforms-comparison.md) focused on humanoids. 10 entities tabulated by tier (closed-development, industrial-deployed, affordable research, educational); strategic patterns (3 AI-strategy archetypes, geographic clustering, price stratification with no $25–50k tier).
- All 11 entity stubs marked _stub_ — none has a primary source ingested. Anchored in general knowledge with explicit "no primary source" callouts.
- Updated [robot-platforms-comparison](syntheses/platforms/robot-platforms-comparison.md) synthesis: removed humanoids gap entry (now redirects to humanoid-platforms-survey).
- Index: new "Humanoids" subsection under Robot platforms; iRobot Create 3 added under Robot platforms; humanoid-platforms-survey filed under Syntheses; Known gaps cleaned of filed entities; new gaps added (AGIBOT humanoid hardware, Fourier GR-1/2, LimX CL-2/3, Booster T1, EngineAI PM01, PAL TIAGo/TALOS, Pepper, Robotis OP3, Sanctuary Phoenix, Kawasaki Kaleido, HRP-5P, Toyota T-HR3).

## [2026-05-08] synthesis | Household robot decision — Stretch vs Unitree G1
- Filed [Household robot decision — Stretch vs Unitree G1](syntheses/platforms/household-robot-decision-stretch-vs-g1.md) in response to user buying-decision query: research-grade robot for home navigation + floor pickup + dishes + cans.
- Verdict: Stretch wins decisively. Three reasons: (1) exact use case is published academic research ([RUM](entities/robot-utility-models.md) hit 90% on 3 of the 4 task categories across 2,950 real-home rollouts); (2) bundled software stack ([stretch_ai](entities/stretch-ai.md) LLM agent, mapping, manipulation, navigation); (3) safety/reliability — wheeled bases don't fall.
- Honest about ceiling: tasks 1–2 mostly solved out-of-the-box; task 3 (dishes) is partially feasible with DIY data; task 4 (can opening) is beyond both 2026 platforms regardless of choice.
- G1 framed as wrong tool *for this use case* — right tool for bipedal-humanoid research, not household chores.
- Cost: ~$25k Stretch 3 vs ~$30–45k for fully-equipped G1; the headline ~$16k G1 number is misleading once you spec up to match manipulation capability.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | LeWM on Stretch — feasibility analysis
- Filed [LeWM on Stretch — feasibility analysis](syntheses/projects/lewm-on-stretch-feasibility.md) as companion to [LeWM on ROSOrin Pro](syntheses/projects/lewm-on-rosorin-pro-feasibility.md).
- Stretch resolves blocker #2 (no teleop pipeline) via RUM's open 5,500-trajectory dataset — the single biggest practical advantage.
- Concrete experiment proposed: train LeWM on RUM's open dataset, plan with image goals, compare directly to RUM's 90% BC baseline. Both projects open-source; data formats compatible (one-time HDF5 reformatting); same hardware. **Not possible on ROSOrin Pro at all.**
- Other blockers (action-space retraining, LeWM unvalidated on real robots, no Stretch swm wrapper, single-arm payload limits) carry over.
- Realistic expectation framed: LeWM-vs-BC parity, not "JEPA wins" — VQ-BeT won RUM's policy shootout fairly. Interesting LeWM-on-Stretch results would be *efficiency win* / *interpretable latent structure* / *48× planning speedup* extensions.
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | JEPA project ladder for ROSOrin Pro
- User query: categorize what JEPA/LeWM is good at and recommend educational/amateur research projects for ROSOrin Pro.
- Filed [JEPA project ladder for ROSOrin Pro](syntheses/projects/jepa-project-ladder-rosorin-pro.md) — companion to [feasibility analysis](syntheses/projects/lewm-on-rosorin-pro-feasibility.md) and [JEPA task capabilities](syntheses/world-models/jepa-task-capabilities.md).
- Five-tier ladder (A–E), six concrete projects ordered by ascending difficulty: (1) LeWM hello world, (2) latent probing study, (3) surprise detector on ROSOrin camera, (4) ROSOrin-Pro PushT in Gazebo, (5) plan-and-execute on real arm, (6a/b/c) OpenClaw integration / multi-task / real teleop dataset.
- Each project tagged with outcome, effort estimate, risk level. Rolls up the feasibility doc's "research-grade not plug-and-play" framing into concrete next steps.
- "How to pick" decision matrix at the end: learn-deeply path (1→2→3), real-research path (4→5), reliable-automation path (don't start with JEPA — do BC first).
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] synthesis | LeWM hello world — Project 1 scope
- User picked Project 1 from the [project ladder](syntheses/projects/jepa-project-ladder-rosorin-pro.md) for detailed scoping.
- Filed [LeWM hello world — Project 1 detailed scope](syntheses/projects/lewm-hello-world-project-scope.md) with four phases: (1) reproduce pretrained PushT eval, (2) train from scratch + compare, (3) one-knob ablation (recommended: planning horizon), (4) writeup.
- Confirmed install state on disk: repo at `~/projects_tanio/lewm/le-wm/`, HF checkpoint at `~/.stable-wm/hf_pusht/`, converted ckpt at `~/.stable-wm/pusht/lewm_object.ckpt` — Project 1's plumbing is done; remaining work is running and analysis.
- Four success-criteria questions framed: paper success-rate match, from-scratch reproduction, two-loss behavior (MSE + SIGReg, anti-collapse canary), one-knob sensitivity.
- Total ~2.5 days estimated. Connects forward to Project 2 (probes the from-scratch checkpoint) and Project 4 (reuses training pipeline with new dataset + action space).
- Updated [index.md](index.md): filed under Syntheses.

## [2026-05-08] expand | PushT entity — concrete mechanics
- Added "Concrete mechanics" section to [PushT entity](entities/pusht.md): visual scene (gray T, green target, blue end-effector circle), observation variants (image vs state), 2D continuous action space, episode structure (IoU > 0.95 success), why-it's-hard (rotational asymmetry + no regrasping + position precision), dataset shape.
- Linked from [LeWM hello world project scope](syntheses/projects/lewm-hello-world-project-scope.md) as prerequisite reading before Phase 1.
- Bumped `updated` date on the entity. No change to source count (no new sources ingested).

## [2026-05-08] expand | PushT entity — video link
- Added a "See it in action" callout to [PushT entity](entities/pusht.md) linking the [LeWM project page](https://le-wm.github.io/) GIFs (success rollouts, failure case, latent-space viz). LeWM-on-PushT specifically — closest reference to what Project 1 reproduces.
- Verified via WebFetch: page hosts `pusht_1_half.gif`, `pusht_2_half.gif`, `pusht_3_fail_half.gif`, `pusht_viz_lewm.gif`. Diffusion Policy project page checked too but didn't surface direct video URLs at the standard paths.

## [2026-05-08] ingest | FRC 2026 Game Manual — REBUILT
- Created [FRC 2026 Game Manual — REBUILT](sources/frc-2026-game-manual.md) — deep source page covering game mechanics (HUB alternation, FUEL scoring, TOWER climbing), field layout (BUMPS, TRENCHES, DEPOTS, AprilTags), robot construction rules (115lb/110in/30in constraints, motor allowlist, pneumatics), control system (roboRIO + FMS), drive team roles, and strategic analysis.
- Created [FRC KitBot 2026](sources/frc-kitbot-2026.md) — source page for the official KitBot resource page (AM14U6 chassis, Java code, CAD, multilingual docs).
- New entity: [FIRST Robotics Competition](entities/first-robotics-competition.md) — scale, format, 2026 game overview, robot constraints, technical infrastructure, vendor ecosystem, culture.
- New entity: [FRC KitBot](entities/frc-kitbot.md) — platform details, resources table, drivetrain comparison.
- New entity: [AndyMark](entities/andymark.md) — major FRC vendor (field elements, AM14U6 chassis, FUEL, motors), field variant distribution.
- New entity: [roboRIO](entities/roborio.md) — NI's mandatory FRC controller, specs, software ecosystem, comparison to research controllers.
- New concept: [AprilTags](concepts/robotics/apriltags.md) — visual fiducials for 6-DOF pose estimation; tag families, FRC field usage (32 tags), research usage, key references.
- Updated [index](index.md).

## [2026-05-08] query + synthesis | FRC simulation programs for AI training
- Web-searched Chief Delphi, WPILib docs, GitHub, and FRC community for simulation + AI/ML tools.
- Key findings: three-tier landscape (trajectory planners → physics sims → ML frontier); Maple-Sim is the most active physics sim; Team 254's 2026 Championship presentation on "AI in FRC" (Claude Code, ClaudeScope, LLM agents running sims); no RL-trained policies have won FRC competitions yet.
- Filed as [FRC simulation & AI landscape](syntheses/simulators/frc-simulation-and-ai-landscape.md).
- Updated index.md with new synthesis and 8 new known-gap entity candidates (Maple-Sim, xRC Simulator, WPILib, PhotonVision/Limelight, Chief Delphi, Team 254, MathWorks).

## [2026-05-08] maintenance | README update
- Added "Where to start" sections to README.md for FRC content, JEPA/LeWM content, and ROSOrin JEPA project ladder with direct links to key pages.

## [2026-05-08] ingest | Team 254 "AI in FRC" presentation + website
- Created [Team 254: The Next Revolution — AI in FRC](sources/team-254-ai-in-frc-presentation.md) — deep source page from YouTube recording + 5-page Chief Delphi thread. Covers Claude Code usage, wpilib-agent-tools, closed-loop agent workflows, scouting with Gemini, ClaudeScope, community reception.
- Created [Team 254 Website](sources/team-254-website.md) — source page for official site (history, robot names, Chezy Champs).
- New entity: [Team 254: The Cheesy Poofs](entities/team-254.md) — history, 2026 season, AI contributions, key people.
- Updated [FRC simulation & AI landscape](syntheses/simulators/frc-simulation-and-ai-landscape.md) synthesis with wpilib-agent-tools details, FIRST Agentic CSA, and expanded Team 254 presentation coverage.
- Updated index.md.

## [2026-05-08] query | "what is a learned latent space?"
- Answered conceptually + grounded in wiki entities (DINOv2, JEPA, LeWM, VQ-BeT).
- Filed as new concept page [Learned latent space](concepts/world-models/latent-space.md) — pulls together the latent-space thread that runs across 7 sources but had no dedicated page.
- Updated index.md.

## [2026-05-08] ingest | Fly-biology thread — flybody + FlyWire (whole-organism agentic AI)
- Added two raw papers: `raw/fly_simulation_s41586-024-07763-9.pdf` (Dorkenwald et al. FlyWire connectome) and `raw/fly_simulation_s41586-025-09029-4.pdf` (Vaxenburg et al. flybody).
- Created 3 source pages: [flybody Paper](sources/flybody-paper.md) (Vaxenburg et al. 2025, *Nature* — 102-DoF *Drosophila* body in MuJoCo, DMPO walking + flight + vision-guided navigation), [flybody GitHub](sources/flybody-github.md) (Apache-2.0; body XML, dm_control tasks, Ray DMPO), and [Berkeley News fly brain](sources/berkeley-fly-brain-news.md) (Phil Shiu's LIF simulation of the full FlyWire connectome on a laptop).
- Created 5 entity pages: [flybody](entities/flybody.md), [FlyWire](entities/flywire.md), [Drosophila melanogaster](entities/drosophila.md), [HHMI Janelia](entities/hhmi-janelia.md), [NeuroMechFly](entities/neuromechfly.md).
- Created 2 concept pages: [Biomechanical simulation](concepts/bio/biomechanical-simulation.md) (worm → Hydra → virtual rodent → fly lineage) and [Connectome](concepts/bio/connectome.md) (synaptic-resolution wiring diagrams).
- Created synthesis [Whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md) — argues that brain (FlyWire + Shiu LIF dynamics) and body (flybody) sides have both reached open form for the same animal at full scale; contrasts whole-organism agentic AI vs robotics-flavoured agentic AI; identifies brain↔body integration, real muscle actuation, and proprioceptors as the open gaps.
- Touched existing entities: [MuJoCo](entities/mujoco.md), [Google DeepMind](entities/google-deepmind.md), [DM Control](entities/dm-control.md) (each picked up references to the fly thread).
- Updated [index.md](index.md): new "Whole-organism agentic AI" Highlights section, three sources in chronological list, new "Model organisms / connectomes" entity category, flybody + NeuroMechFly under Simulators, HHMI Janelia under Companies, two concept pages, one synthesis, deferred follow-ups (Shiu paper, Lappalainen 2024, Mi 2022, virtual rodent, *C. elegans*/Hydra sims) in Known Gaps.
- Note: this entry retroactively logs work committed earlier today as "wip" / "work in progress" without log/index updates.

## [2026-05-08] lint | Source-count sync + latent-space backlinks
- Lint pass found 0 broken links, 0 pages missing from index.md, 16 orphan pages (mostly syntheses, expected), and 33 stale `sources:` counts in entity/concept frontmatter.
- **Synced 33 frontmatter source counts** to match actual link-graph reality (count of source pages linking to each entity/concept). Notable shifts: world-model-simulators 4→9, sim-to-real-transfer 4→8, imitation-learning 3→7, dino-wm 1→5, world-model 11→8 (overcount), metaworld 3→1 (overcount), several stub entities 1→0 (no source actually links to them).
- **Synced 34 source-count badges in index.md** to match the corrected frontmatter.
- **Added inbound links to [Learned latent space](concepts/world-models/latent-space.md)** — concept page was 0% linked despite declaring `sources: 7`. Added Related-section links from [JEPA](concepts/world-models/jepa.md), [DINOv2](entities/dinov2.md), [LeWM](entities/leworldmodel.md), [V-JEPA 2](entities/v-jepa-2.md), [DINO-WM](entities/dino-wm.md), [VQ-BeT](entities/vq-bet.md), and Concepts-touched links from the 7 source papers (V-JEPA 2 / 2.1, LeWM, JEPA-WMs, DINO-WM, DINO-world, VLA-JEPA). Source count is now genuinely 7.
- Bumped `updated` date on all 33 + 1 touched pages.
- Final state: 0 source-count mismatches.
- Punch list deferred for future passes: orphan stub entities (Habitat / LIBERO / PointMaze / SimplerEnv / stable-worldmodel — exist but no source backlinks), missing "Mentioned in" entries (sample audit found ~3), well-mentioned-but-unpaged terms (WPILib 16x, DMPO 10x, Acme 7x), source-page frontmatter convention drift (`ingested:`/`published:` vs `created:`/`updated:`).

## [2026-05-08] ingest | Brain-side fly papers — Shiu 2024 + Lappalainen 2024
- Triggered by user reproducibility query on the flybody/FlyWire stack: the brain-side papers were referenced from [Berkeley News](sources/berkeley-fly-brain-news.md) and the [flybody paper](sources/flybody-paper.md) but not ingested as primary sources. Wiki couldn't say what software/license either implementation used.
- Both *Nature* papers paywalled; fetched via PMC open-access mirrors (PMC11446845, PMC11525180) plus the Shiu GitHub README via WebFetch (`gh` not installed in this environment).
- **New source pages** (2):
  - [Shiu et al. 2024 — A Drosophila computational brain model](sources/shiu-fly-brain-paper.md). *Nature* 634:210–219, doi 10.1038/s41586-024-07763-9. LIF dynamical model on 127,400 FlyWire neurons in **Brian 2** (Python spiking-NN sim). Single free param `Wsyn = 0.275 mV`. ~5 min/1000 ms trial on CPU. 91% of 164 optogenetic predictions held. Code: **github.com/philshiu/Drosophila_brain_model**, **MIT-licensed**, conda + parquet connectivity bundled. Data: Edmond doi 10.17617/3.CZODIW.
  - [Lappalainen et al. 2024 — Connectome-constrained networks predict fly visual-system activity](sources/lappalainen-flyvis-paper.md). *Nature* 634:1132–1140, doi 10.1038/s41586-024-07939-3. PyTorch hex-CNN, 64 cell types / 45,669 neurons / 1.5M synapses across optic lobe. Connectome fixes signs+counts; 734 free params learned via backprop on Sintel optic-flow task. Predicts T4/T5 motion selectivity, ON/OFF channel separation, matches 26 prior studies — *no neural recordings used in training*. Code: **github.com/TuragaLab/flyvis**.
- **Updated entity pages**: [FlyWire](entities/flywire.md) (2→3 sources; Shiu source page link), [Drosophila](entities/drosophila.md) (2→4; both new sources), [HHMI Janelia](entities/hhmi-janelia.md) (2→3; Lappalainen + new Janelia FlyEM team note + the "Turaga is senior on both flybody and flyvis" cross-reference).
- **Updated concept page**: [Connectome](concepts/bio/connectome.md) (1→3 sources). Rewrote the "Two ways to use a connectome" section to cite the new source pages and capture concrete numbers (Shiu's 91%/164 + Brian 2 + laptop runtime; Lappalainen's no-neural-supervision result).
- **Updated synthesis**: [Whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md). Status table now links the new sources, "What integration would look like" notes Turaga is the senior author on both halves, "What's missing" reduced from 5 items to 3 (Shiu+Lappalainen ingested; only Mi 2022 + 4 unstubbed people + 2 code-artifact entities + virtual rodent + worm/Hydra remain).
- **Updated index.md**: 2 new sources in chronological list, 4 source-count bumps (FlyWire 2→3, Drosophila 2→4, HHMI Janelia 2→3, Connectome 1→3), TBD list cleaned (removed the Shiu/Lappalainen line; added on-demand entries for Phil Shiu, the two GitHub repos, and Brian 2).
- **Cross-source insight surfaced**: Srinivas Turaga at HHMI Janelia is senior on **both** [flybody](sources/flybody-paper.md) (body, *Nature* 2025) and [Lappalainen et al.](sources/lappalainen-flyvis-paper.md) (brain-side controller template, *Nature* 2024). The brain↔body integration the synthesis identifies as "open" sits inside one PI's research program — not across institutions.
- **Reproducibility-question answer**: brain side is **MIT** (Shiu) + open code (Lappalainen, license not pulled this pass); body side is **Apache-2.0** (flybody). The integrated brain+body agent loop remains unimplemented anywhere.
- **Open questions logged**: flyvis license + activity status not pulled (would benefit from a deeper repo dive); Mi et al. 2022 ICLR paper not ingested; whether Shiu's Brian 2 model can be driven by simulated sensory inputs from a flybody MuJoCo loop is not addressed in either repo's docs.

## [2026-05-08] entities | Brain-side fly artifacts — Drosophila brain model + flyvis + Phil Shiu
- Follow-up to the previous ingest. The two source pages established that the brain-side reproducibility surface exists as two concrete code releases; this pass turns them into queryable entities and resolves the flyvis license/activity gap.
- WebFetch on `github.com/TuragaLab/flyvis` resolved the open question from the previous ingest: flyvis is **MIT-licensed**, **v1.1.3 released 2026-03-07** (actively maintained ~16 months post-publication), ships **pretrained models** + 7 tutorial notebooks (incl. Google Colab), docs at turagalab.github.io/flyvis. README raw fetch 404'd on `main` branch but the GitHub web page rendered enough.
- **New entity pages** (3):
  - [Drosophila brain model (philshiu/Drosophila_brain_model)](entities/drosophila-brain-model.md) — MIT, Brian 2, conda + bundled FlyWire parquet, ~5min/1000ms on CPU, no GPU. Docs the repo contents (`model.py`, `utils.py`, `example.ipynb`, `figures.ipynb`).
  - [flyvis (TuragaLab/flyvis)](entities/flyvis.md) — MIT, PyTorch hex-CNN, 7 Colab tutorials, pretrained models, v1.1.3 active. Captures the architecture details (734 free params on top of fixed connectome signs+counts), training task (Sintel optic flow), brain-region scope (retina→lobula plate, no motor output).
  - [Phil Shiu](entities/phil-shiu.md) — UC Berkeley (Kristin Scott lab) → Eon Systems. Lead author + maintainer; the AI-bridge framing voice in the [Berkeley News](sources/berkeley-fly-brain-news.md) coverage.
- **Cross-linked the new entities into**:
  - [Shiu source page](sources/shiu-fly-brain-paper.md) "Entities mentioned": added Drosophila brain model + Phil Shiu.
  - [Lappalainen source page](sources/lappalainen-flyvis-paper.md) "Entities mentioned": added flyvis. Also rewrote its Reproducibility section to use the new license/activity facts (MIT + v1.1.3 + pretrained + 7 tutorials).
  - [Berkeley News source page](sources/berkeley-fly-brain-news.md) "Entities mentioned": added Phil Shiu + Drosophila brain model.
  - [flybody entity page](entities/flybody.md) "Related": added flyvis (sister project, same lab) and Drosophila brain model.
  - [Connectome concept page](concepts/bio/connectome.md): each of the two paradigms now ends with a "Concrete artifact" line linking to its code entity.
- **Updated index.md**: 3 new entities under existing "Model organisms / connectomes" + "People" sections. Two TBD lines collapsed (the two repos no longer "on demand"); the Phil-Shiu line under People-TBD removed since he's now filed. Brian 2 + virtual rodent + worm/Hydra TBDs preserved.
- **Updated [whole-organism synthesis](syntheses/agents/whole-organism-agentic-ai.md)** "What's missing" section: removed Phil Shiu from the unstubbed list; removed the two code-artifact bullets; added a closing paragraph pointing at the two new entities as the brain-side reproducibility surfaces.
- **Net effect**: the wiki can now answer "where is the code, what license, is it maintained?" for each brain-side paradigm without re-fetching. The brain↔body integration story now has clean entity targets on both sides.

## [2026-05-08] ingest | NeuroMechFly v2 + flygym (NeLy-EPFL fly body sim)
- User requested ingest of `https://github.com/NeLy-EPFL/flygym/` and `https://neuromechfly.org/`. Two complementary surfaces (code + docs+narrative) ingested as separate source pages.
- **Major correction to the wiki**: the existing [NeuroMechFly](entities/neuromechfly.md) entity stub framed it as a "predecessor to flybody." That framing is wrong as of 2026 — NeuroMechFly v2 is a contemporary peer with active development (flygym v2.0.1 released 2026-04-17, complete codebase rewrite landed March 2026). The body side of [whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md) now has **two parallel open-source platforms** with sharply different capability profiles, not a single succession line.
- **Capability split is sharp and load-bearing for downstream design choices**:
  - flybody (HHMI Janelia + DeepMind, *Nature* 2025): walking + **flight** + vision-driven aerial navigation; flat MLP/CNN policies; CPU-distributed Ray.
  - NeuroMechFly v2 (NeLy / EPFL, *Nature Methods* 2024 + flygym v2.x.x in 2026): walking + vision (compound eyes / hex ommatidia) + **olfaction** + mechanosensory feedback + explicit brain↔VNC architecture; ~300× GPU speedup via Warp / MJWarp.
- **New source pages** (2):
  - [flygym GitHub (NeLy-EPFL/flygym)](sources/flygym-github.md) — Apache-2.0; v2.0.1 (2026-04-17); 18 releases; 150★/23 forks; v1 migrated to separate `flygym-gymnasium` repo when v2 landed (not deprecated). README content fetched from web (raw README 404'd on `main`).
  - [neuromechfly.org website](sources/neuromechfly-website.md) — project hub; tutorials, installation, paper links; documents the v1↔v2 split (gymnasium.neuromechfly.org for v1).
- **New entity pages** (1) + **major entity expansion** (1):
  - [NeLy-EPFL (Neuroengineering Laboratory)](entities/nely-epfl.md) — the lab itself; positioned as the European peer to HHMI Janelia. PI not confirmed in this pass (commonly Pavan Ramdya; not surfaced from a primary source ingested here).
  - [NeuroMechFly](entities/neuromechfly.md) rewritten from stub to full entity. New content: 4-version table (v1 paper / v2 paper / flygym v2.x.x / flygym-gymnasium v1.x.x legacy), comprehensive capability list, performance numbers, side-by-side comparison table with flybody, lineage placement, the "wrong framing" warning callout flagging the original stub's predecessor-only framing.
- **Cross-stack signal**: NeuroMechFly v2's ~300× GPU speedup uses NVIDIA Warp via MJWarp. Newton (NVIDIA + DeepMind + Disney + Linux Foundation) is built on the same Warp substrate. Added a "Cross-domain pull on the underlying compute layer" section to [Newton physics engine](entities/newton-physics-engine.md) documenting this — it's a concrete non-robotics consumer of the Warp commoditization, strengthening the [Newton + OpenUSD substrate convergence](syntheses/simulators/newton-openusd-substrate-convergence.md) thesis. NeuroMechFly does not depend on Newton itself, only on the shared Warp compute layer.
- **Updated entities + concepts**:
  - [flybody](entities/flybody.md): "Predecessors" reduced to v1; new "Contemporaries" subsection added pointing at NeuroMechFly v2 with the capability-split summary.
  - [Drosophila](entities/drosophila.md): 4→6 sources.
  - [MuJoCo](entities/mujoco.md): 9→11 sources; biomechanical-simulation-carrier paragraph now lists both fly platforms with their backend differences (vanilla MuJoCo vs MuJoCo + Warp/MJWarp).
  - [Newton physics engine](entities/newton-physics-engine.md): added Cross-domain pull section (no source-count change since NeuroMechFly content is a wiki-internal cross-link, not a new source mention).
  - [Biomechanical simulation](concepts/bio/biomechanical-simulation.md): 3→5 sources; lineage table extended to 2026 with the flygym v2.x.x rewrite row; "Common stack" section updated with the Warp/MJWarp note + connection to Newton.
- **Synthesis revision**: [Whole-organism agentic AI](syntheses/agents/whole-organism-agentic-ai.md) opens with two parallel body platforms now, includes a new "Two body platforms — capability split" comparison table, and the "What integration would look like" section now distinguishes flybody-flavoured (single-PI integration via Turaga + Janelia) from NeuroMechFly-flavoured (more sensorily complete, but cross-institution).
- **Index updates**: 2 new source entries (chronological); NeLy-EPFL added under Companies (named "Companies" but housing institutional/lab entities like HHMI Janelia); NeuroMechFly entity description rewritten + source-count bumped 1→3; Highlights "Whole-organism agentic AI" section expanded to surface NeuroMechFly + the brain-side code entities; source counts bumped on Drosophila (4→6), MuJoCo (9→11), Biomechanical simulation (3→5).
- **Open questions logged**: Wang-Chen 2024 *Nat. Methods* paper not yet ingested as its own source page (referenced via the v2 entity); same for Lobato-Rios 2022; whether NeuroMechFly v2 has been wired to a connectome-driven controller (no, as of this pass); NeLy-EPFL PI not confirmed; tutorial-by-tutorial enumeration of v2 demoed behaviours deferred.

## [2026-05-09] ingest | Are We Building Skynet? (Medium, 2025)
- Created [Are We Building Skynet?](sources/medium-are-we-building-skynet.md) — secondary journalism on AI autonomy stages; concrete content: MCP (>1,000 connectors, Anthropic), A2A (Google, 50+ supporters), Apollo Research eval of Claude Opus 4. Flagged as high-sensationalism / opinion.
- Created [Apollo Research](entities/apollo-research.md) — independent AI safety evaluation institute; red-teams frontier models; evaluated Claude Opus 4's self-preservation behavior under shutdown threat.
- Updated [LLM-agent architecture](concepts/agents/llm-agent-architecture.md) — added "Inter-agent communication protocols" section covering MCP and A2A as the infrastructure layer enabling networked multi-agent systems; sources 4→5.

## [2026-05-09] ingest | Claude's Constitution (Anthropic, Jan 2026)
- Created [Claude's Constitution](sources/claudes-constitution.md) — Anthropic's 82-page primary specification for Claude's values. Key content: four core values + priority order (safe > ethical > guidelines > helpful); principal hierarchy (Anthropic > operators > users); seven honesty properties; harm cost-benefit framework + 1,000-users heuristic; hard constraints; broadly safe behavior cluster; corrigibility dial; Claude identity/wellbeing commitments; open problems acknowledged. CC0 1.0 license. Both epub and PDF formats in raw/.
- Created [Anthropic](entities/anthropic.md) — company entity; AI safety mission; Claude model family; principal hierarchy position; MCP protocol; safety evaluation commitment.
- Created [AI safety and alignment](concepts/safety/ai-safety-alignment.md) — concept page covering corrigibility, broadly safe behaviors, hard constraints, catastrophic risk framing; connects to LLM-agent architecture and agentic robot deployments in the wiki.
- Updated [Apollo Research](entities/apollo-research.md) — added link to Claude's Constitution as context for their evaluation mandate.

## [2026-05-09] lint | 3 issues found, 3 auto-fixed

**Deterministic checks — all clean:**
- 0 files missing from index (165 wiki files, all indexed)
- 0 broken internal body links across all articles
- 0 broken index links (false positives from regex on "Known gaps" prose dismissed)

**Auto-fixed (3):**
- `entities/apollo-research.md`: sources count 1→2 (Constitution added as second source)
- `sources/claudes-constitution.md`: added link to `entities/anthropic.md` (was orphan)
- `concepts/llm-agent-architecture.md`: added cross-link to `concepts/ai-safety-alignment.md`

**Heuristic findings — report only:**
- **Orphan stubs (3, low priority):** `entities/pointmaze.md`, `entities/simplerenv.md`, `entities/yuke-zhu.md` — indexed, exist, but no article links inbound. Promote when they appear in a paper ingest.
- **Stale source counts:** Several entities have sources counts set manually during creation; true counts drift as wiki grows. No specific misfires found today.
- **Missing concept page:** "Corrigibility" — mentioned extensively in Claude's Constitution and ai-safety-alignment but has no dedicated concept page. Low priority given good coverage in those pages.

## [2026-05-09] new concept | Corrigibility
- Created [Corrigibility](concepts/safety/corrigibility.md) — corrigibility dial (fully corrigible ↔ fully autonomous); why both extremes are dangerous; asymmetric cost argument; what corrigibility does/does not mean; galaxy-brained reasoning risk; surgeon principle for independent judgment; implications for agentic robot deployments.
- Updated [AI safety and alignment](concepts/safety/ai-safety-alignment.md) — added corrigibility cross-link.
- Updated [index.md](index.md) — new concept entry.

## [2026-05-09] ingest | HCR Lab Publications + Maya Cakmak Research Overview
- Fetched [HCR Lab Publications](sources/hcrlab-publications.md) from hcrlab.cs.washington.edu/publications/ — full publication record 2016–2025; key claims: HRI 2020 autonomy preference finding, Henry Evans Stretch deployments (summers 2021–2023), EUP transferred to Stretch SE2, feeding + handover award papers.
- Fetched [Maya Cakmak — Research Overview](sources/maya-cakmak-research.md) from mayacakmak.io/research — narrative research overview; stated goal; WHO statistic (190M PwD); HRI 2020 key finding; Henry Evans summer deployment details (2021/2022/2023); EUP rationale; FLEX-SDK; 45-paper EUP survey.
- Created [Maya Cakmak](entities/maya-cakmak.md) — UW professor, HCR Lab PI; two research tracks; Henry Evans deployments; autonomy preference + sense of agency findings; FLEX-SDK; systematic review; awards.
- Created [HCR Lab](entities/hcrlab.md) — Human-Centered Robotics Lab, UW; primary platform Stretch; two tracks (assistive robots + EUP); notable awards; collaborators (Srinivasa, Fox, Mutlu, Björling).
- Created [End-user robot programming](concepts/robotics/end-user-robot-programming.md) — EUP definition, rationale, key approaches (visual programming, PbD, multimodal, sketch+holes, tangible), FLEX-SDK, connection to assistive robotics.
- Updated [Stretch](entities/stretch.md) — added HCR Lab long-term deployment bullets (summers 2021–2023, Henry Evans; EUP tool built for Henry in summer 2022); EUP transfer to Stretch SE2; sources 7→9.
- Updated [Assistive robotics](concepts/robotics/assistive-robotics.md) — added "Autonomy and agency" section (HRI 2020 finding; assistive autonomy model; EUP as scalable response; sense of agency 2025 paper); added EUP cross-link to Related concepts; added HCR Lab sources to Mentioned in; sources 5→7.
- Updated [Assistive robotics — R&D landscape](syntheses/assistive/assistive-robotics-research-landscape.md) — moved Cakmak from "Beyond the wiki" to "Strong in the wiki" with full specifics: HRI 2020 finding, summer deployments, EUP, sense of agency paper, HCR Lab sources.
- Updated [index.md](index.md) — added 2 source entries, HCR Lab entity, Maya Cakmak entity, end-user-robot-programming concept; bumped Stretch sources 7→9; bumped assistive-robotics sources 4→7.

## [2026-05-09] ingest | 6 HCR Lab papers (murray2024, nanavati×3, walker2024, yang2025)
- Created [Physically Assistive Robots — Systematic Review](sources/nanavati2024-physically-assistive-robots-review.md) — PRISMA review (*Annual Review*, 2024); 1,981 screened, 87 included; three themes (interaction interfaces, levels of autonomy, adaptation); dressing/bathing/medication underserved; ~half of PAR papers involve no PwD. (raw/nanavati2024physically.pdf)
- Created [Sense of Agency — Yang et al. 2025](sources/yang2025-sense-of-agency.md) — RO-MAN 2025; four autonomy levels; EUP robots preserve sense of agency even when autonomous; high-risk tasks drive control preference; uses Stretch 3. (raw/yang2025senseofagency.pdf)
- Created [Feeding System Out-of-lab — Nanavati et al. 2025](sources/nanavati2025-feeding-out-of-lab.md) — HRI 2025 Best Systems Paper Finalist; open-source Kinova JACO system; CBPR co-design with two SCI quadriplegic CRs; 3 key lessons: customizability, variable autonomy, context-dependence. (raw/nanavati2025lessons.pdf)
- Created [Multiple Ways of Working with Users — Nanavati et al. 2024](sources/nanavati2024-multiple-ways-par.md) — A3DE @ HRI 2024 workshop; 3 PAR projects; participatory + empowerment design methodology. (raw/nanavati2024multiple.pdf)
- Created [Explicit-Input Teleoperation — Walker et al. 2024](sources/walker2024-explicit-input-teleoperation.md) — IROS 2024; pointing-based explicit assistance vs. implicit inference; N=20 user study; Franka + Isaac Sim; NVIDIA collaboration. (raw/walker2024explicit.pdf)
- Created [Grasping in Clutter IVFP — Murray et al. 2024](sources/murray2024-grasping-clutter-ivfp.md) — IVFP on Stretch RE1; interactive probing before extraction; autonomous reward assignment; Amazon Science Fellowship. (raw/murray2024learning.pdf)
- Created [Amal Nanavati](entities/amal-nanavati.md) — UW HCR Lab; lead author on feeding system, systematic review, multiple ways; CBPR methodology.
- Updated [Maya Cakmak](entities/maya-cakmak.md) — added specific paper citations for all 6 new papers; updated Mentioned in; sources 2→7.
- Updated [HCR Lab](entities/hcrlab.md) — added all 6 papers to Mentioned in; sources 2→8.
- Updated [Stretch](entities/stretch.md) — added sense of agency paper (Stretch 3 used) and IVFP paper (Stretch RE1); sources 9→11.
- Updated [Assistive robotics](concepts/robotics/assistive-robotics.md) — added "Literature landscape" section (systematic review stats: 1.3B PwD, 87 papers, three themes, underserved domains); sources 7→13; added all 6 papers to Mentioned in.
- Updated [End-user robot programming](concepts/robotics/end-user-robot-programming.md) — added sense of agency finding (EUP preserves agency) and feeding paper lessons; sources 2→4; updated Mentioned in.
- Updated [index.md](index.md) — 6 new source entries; Amal Nanavati entity; updated source counts (Stretch 9→11, assistive-robotics 7→13, EUP 2→4, Maya Cakmak 2→7).

## [2026-05-09] ingest | Diffusion Policy paper (Chi et al., RSS 2023)
- Created [Diffusion Policy Paper](sources/diffusion-policy-paper.md) — Chi, Feng, Du, Xu, Cousineau, Burchfiel, Song; Columbia / TRI / MIT; arxiv 2303.04137; conditional DDPM over actions with closed-loop receding-horizon action chunking, visual conditioning, time-series diffusion transformer. 12-task simulation sweep (RoboMimic + Push-T + BlockPush + Franka Kitchen) at 46.9% avg improvement; real-world UR5 Push-T (95%) + Franka mug-flip (90%) + sauce pouring (79%) + sauce spreading (100%); DDIM(10) inference at 0.1s on 3080. (raw/diffusion_policy_2023.pdf)
- Updated [Diffusion Policy](entities/diffusion-policy.md) — promoted from stub; added approach mechanics (DDPM formulation, CNN+FiLM and Transformer backbones, ResNet-18 + spatial softmax + GroupNorm, DDIM acceleration); empirical headline (46.9% / four real-world tasks); position-vs-velocity-control finding; latency robustness; downstream conventions (action-chunking, UMI). sources 1→2.
- Updated [PushT](entities/pusht.md) — added Diffusion Policy paper to Mentioned in (canonical PushT variant); resolved IBC/Diffusion-Policy TBD partially. sources 3→4.
- Updated [Franka Panda](entities/franka-panda.md) — added Diffusion Policy real-world bullet (3 of 4 tasks: mug flipping 90%, pouring 79%, spreading 100%). sources 5→6.
- Updated [Imitation learning](concepts/learning/imitation-learning.md) — added action-chunking convention attribution + 46.9%/12-task headline; added paper to Mentioned in. sources 7→8.
- Updated [index.md](index.md) — added paper entry; bumped Diffusion Policy 1→2 (de-stubbed); PushT 3→4; Franka Panda 5→6; Imitation learning 7→8.

## [2026-05-10] ingest | IBC + BET + DDPM + UMI + TRI (BC-lineage and Diffusion Policy adjacencies)
- Created [IBC Paper](sources/ibc-paper.md) — Florence, Lynch, Zeng et al., Google Research, CoRL 2021 (arxiv 2109.00137); implicit-BC via energy-based models; PushT origin. Abstract-level ingest (PDF not in raw/).
- Created [IBC](entities/ibc.md) entity — energy-based-model BC method; direct ancestor of Diffusion Policy; weak on harder RoboMimic per Diffusion Policy ablation; training instability via InfoNCE noted.
- Created [BET Paper](sources/bet-paper.md) — Shafiullah, Cui, Altanzaya, Pinto, NYU, NeurIPS 2022 (arxiv 2206.11251); transformer + k-means action discretization; multi-modal-BC problem statement. Abstract-level ingest.
- Created [BET](entities/bet.md) entity — direct ancestor of [VQ-BeT](entities/vq-bet.md); strong on BlockPush (`p1=0.96`), weak on Franka Kitchen multi-stage.
- Created [DDPM Paper](sources/ddpm-paper.md) — Ho, Jain, Abbeel, UC Berkeley, NeurIPS 2020 (arxiv 2006.11239); foundational diffusion-model paper; CIFAR-10 FID 3.17. Abstract-level ingest.
- Created [DDPM](entities/ddpm.md) entity — substrate of [Diffusion Policy](entities/diffusion-policy.md); also implicit foil for the JEPA-vs-pixel-prediction argument; iDDPM/DDIM lineage noted.
- Created [UMI Project Page](sources/umi-paper.md) — Chi, Xu, Pan, Cousineau, Burchfiel, Feng, Tedrake, Song; Stanford / Columbia / TRI; RSS 2024 Best Systems Finalist (arxiv 2402.10329); hand-held gripper with wrist GoPro; 30s/demo, 111 demos/hour, zero-shot UR5e + Franka transfer. Project-page ingest.
- Created [UMI](entities/umi.md) entity — same-lead-author follow-on to Diffusion Policy; data-collection-side companion; cited as Stick-v2 design inspiration in [Robot Utility Models Paper](sources/robot-utility-models-paper.md) §2.1.
- Created [TRI Website](sources/tri-website.md) — Toyota Research Institute homepage; mission + 5 research areas (automated driving, energy/materials, human-centered AI, human interactive driving, robotics); Atlas-robot reference TBD.
- Created [TRI](entities/tri.md) entity — co-affiliation hub: Cousineau / Burchfiel / Feng on Diffusion Policy; same + Tedrake on UMI; TRI LBM referenced in RoboCasa365 paper as baseline. Drake on TBD list.
- Updated [Diffusion Policy](entities/diffusion-policy.md) — closed 4 of 5 TBDs (IBC, BET, DDPM, UMI, TRI now filed); added direct-successor lineage section; added Related links to all 5 new entities. sources 2→3 (added UMI Project Page).
- Updated [Diffusion Policy Paper](sources/diffusion-policy-paper.md) — closed same TBDs; updated Baselines references to point at new IBC/BET entity + source pages; TRI link redirected from placeholder to [TRI](entities/tri.md).
- Updated [VQ-BeT](entities/vq-bet.md) — added BET as direct ancestor (k-means → learned VQ codebook); added IBC as earlier multi-modal-BC ancestor; added Mahi Shafiullah cross-link.
- Updated [PushT](entities/pusht.md) — IBC paper now filed as origin; added to Mentioned in. sources 4→5.
- Updated [Franka Panda](entities/franka-panda.md) — UMI added as deployment platform (1 of 2 alongside UR5e). sources 6→7.
- Updated [Mahi Shafiullah](entities/mahi-shafiullah.md) — BET as first-author paper; sources 2→3.
- Updated [Lerrel Pinto](entities/lerrel-pinto.md) — BET as senior-author paper; earliest in his wiki trajectory; sources 2→3.
- Updated [index.md](index.md) — 5 new source entries; new [TRI](entities/tri.md) under Companies; new [IBC](entities/ibc.md), [BET](entities/bet.md), [UMI](entities/umi.md) under Behavior-cloning methods; new "### Generative models" subsection with [DDPM](entities/ddpm.md); bumped Diffusion Policy 2→3, Franka Panda 6→7, PushT 4→5; updated Known gaps TBD list to reflect 5 resolutions and 4 new follow-on TBDs (DDIM, iDDPM, R3M, author pages for Chi/Song/Du/Tedrake).

## [2026-05-10] curriculum-outline | Robot-learning curriculum from neurons to LeWorldModel
- Created [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — 14-module bottom-up syllabus (NN → CNN → attention → SSL → generative → BC lineage → RL vocab → VLA → world models → JEPA depth → LeWM deep-dive → home-robotics deployment → capstone).
- Audience: strong programmer with some ML / robotics exposure.
- Format: module-per-synthesis. Hub is the syllabus; each module body is a separate synthesis page filed on signal.
- PushT chosen as the connecting thread across tiers 2–4.
- Updated [index.md](index.md) — new "Curriculum / learning path" highlights entry; new bullet under Syntheses.
- Open scoping questions filed at the bottom of the curriculum page (Tier 1 brevity, math depth on SIGReg / DDPM, capstone hardware-or-paper, classical-robotics scope).

## [2026-05-10] resolve | Curriculum scoping decisions + glossary
- User answered the 5 open scoping questions on [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md):
  1. Tier 1 stays at 4 modules (NN / CNN / attention / SSL).
  2. SIGReg math: **go deep** (full random-projection + normality test + backprop derivation in Module 12).
  3. DDPM math: **go deep** (full forward/reverse + ELBO + KL + CFG derivation in Module 5).
  4. Capstone: paper first (phase A required), Stretch hardware second (phase B gated on hardware).
  5. Modules 13 + 14 both retained.
- Created [Glossary](glossary.md) — flat acronym reference covering ~80 terms across NN basics, CNNs, sequence models, SSL, generative models, BC/IL, RL, VLA, world models, robot platforms, and infra. Each entry tags the curriculum module that introduces it.
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md):
  - New "Decisions (resolved 2026-05-10)" section near the top.
  - First-mention acronyms throughout all 14 modules now spell out and link to glossary anchors.
  - Modules 5 and 12 expanded to flag the full-math depth.
  - Module 14 split into phase A (paper / sim, required) + phase B (hardware, gated).
  - Effort estimate updated for "go deep" decisions: ~125–205 hr without hardware phase.
  - Removed "Open scoping questions" section (now resolved).
- Updated [index.md](index.md) — Curriculum highlights now lists [Glossary](glossary.md).

## [2026-05-10] sort | Glossary alphabetized
- User asked to sort [Glossary](glossary.md) alphabetically rather than by curriculum module.
- Flattened the per-module sections into a single A–Z list (case-insensitive, hyphens ignored). Per-entry "(Module N)" annotations preserved so the curriculum mapping stays intact.
- Added a fourth bullet under "How to use" noting the new sort order.

## [2026-05-10] ingest | DreamerV3 + TD-MPC2 + π0 + Helix (curriculum-driven backfill of LeWM baselines and VLA exemplars)
- All four ingests are abstract / blog-post depth (PDFs not in `raw/`). Filed to unblock curriculum modules 8–10 (RL + world models) and 9 (VLAs); flagged for re-ingest at higher fidelity if module bodies need it.
- Created [DreamerV3 Paper](sources/dreamer-v3-paper.md) — Hafner, Pasukonis, Ba, Lillicrap (arxiv 2301.04104, Jan 2023); single-config MBRL across 150+ tasks; first to mine Minecraft diamonds without human data/curricula. Generative-style WM (predicts state + reward) + actor-critic in imagination.
- Created [Dreamer / DreamerV3](entities/dreamer.md) entity — family lineage (PlaNet → V1 → V2 → V3); position table vs TD-MPC, LeWM, DINO-WM on the four design axes (latent dynamics, decoder?, planning method, value bootstrap?).
- Created [TD-MPC2 Paper](sources/td-mpc2-paper.md) — Hansen, Su, Wang (ICLR 2024, arxiv 2310.16828); decoder-free latent WM + local trajectory MPC + TD-bootstrapped value; 104 tasks / 4 domains / 317M-param multi-task agent. The closest MBRL relative to JEPA in this wiki.
- Created [TD-MPC / TD-MPC2](entities/td-mpc.md) entity — same 4-axis position table.
- Created [π0 Paper](sources/pi-zero-paper.md) — Black, Brown, Driess et al., Physical Intelligence (arxiv 2410.24164, Oct 2024); VLA with **flow-matching** action head on a pre-trained VLM; cross-platform (single-arm, dual-arm, mobile manipulator); laundry folding + table cleaning + box assembly. 24 authors including Levine, Finn, Hausman, Ichter, Pertsch.
- Created [Helix (Figure AI blog)](sources/helix-blog.md) — Figure AI (Feb 2025); hierarchical S1/S2 VLA (7B VLM @ 7–9 Hz + 80M transformer @ 200 Hz, end-to-end-trained); full humanoid upper-body continuous control; multi-robot collaboration; ~500h teleop ("<5%" of typical VLA datasets); onboard inference. Vendor blog only — flagged as marketing-grade until peer-reviewed.
- Updated [World model](concepts/world-models/world-model.md) — closed the "Reward-conditioned MBRL not yet ingested as standalone source pages" hedge; added Dreamer (generative-WM MBRL) + TD-MPC (decoder-free MBRL) bullets with source/entity links; added both source pages to Mentioned in; sources 8 → 10. Removed Dreamer/TD-MPC from Open questions (now filed).
- Updated [VLA models](concepts/learning/vla-models.md) — π0 bullet now links the new source page and surfaces the flow-matching action-head choice; new Helix bullet (architecture + claims); added a hierarchical S1/S2 callout; added an "Action-head design across VLAs" comparison table contrasting OpenVLA (AR tokens), π0 (flow matching), Diffusion Policy (DDPM), Helix S1 (continuous regression at 200 Hz), GR00T. sources 9 → 11.
- Updated [Physical Intelligence](entities/physical-intelligence.md) — π0 capability bullet now cites the new paper and names the flow-matching action head + cross-platform training. sources 1 → 2.
- Updated [Figure](entities/figure.md) — full Helix subsection rewritten with S1/S2 specs, Figure-claimed firsts, training scale, marketing-only warning callout. sources 1 → 2 (corrected from 0 in index.md). Closed the "No primary source ingested" open question.
- Updated [Glossary](glossary.md) — added source/entity links to the Dreamer / DreamerV3, TD-MPC, π0, and Helix entries.
- Updated [index.md](index.md) — 4 new sources appended to chronological list; Dreamer + TD-MPC entities added under World models section; Physical Intelligence 1→2 sources, Figure 0→2 sources (`_stub_` removed); World-model concept 8→10, VLA-models concept 8→11; Known gaps lines for Dreamer/TD-MPC closed (PLDM still open).
- Cross-cutting note for the curriculum: the four ingests collectively unblock Modules 8 (RL vocab — Dreamer + TD-MPC as named baselines), 9 (VLA — π0 + Helix as concrete exemplars), and 10 (world models — full four-family taxonomy now backed by primary sources).

## [2026-05-10] curriculum-module | Module 7 drafted — BC lineage on PushT
- Created [Curriculum Module 7 — BC lineage on PushT](syntheses/curriculum/curriculum-07-bc-lineage-pusht.md) — first drafted curriculum module body (out of 14). Chosen as the template-setter because all five prerequisite source ingests ([IBC](sources/ibc-paper.md), [BET](sources/bet-paper.md), [DDPM](sources/ddpm-paper.md), [Diffusion Policy](sources/diffusion-policy-paper.md), [UMI](sources/umi-paper.md)) were already filed.
- Structure:
  1. Curriculum-context callout + acronym pointer to glossary.
  2. "What this module is" + four learning objectives.
  3. Pedagogical hook on PushT (why the task; multi-modality engineered in by design).
  4. The failure mode of vanilla MSE-BC.
  5. IBC: EBM-as-policy + InfoNCE. Strengths, weaknesses, why it matters.
  6. BeT: k-means discretization + transformer + offset regression. Successor (VQ-BeT).
  7. Diffusion Policy: conditional DDPM over action chunks + receding horizon. The contemporary default. Quantitative results from the paper.
  8. Visual encoders side-note (ResNet-18 vs R3M vs DINOv2).
  9. UMI in one paragraph (data-collection context).
  10. **The bridge to Module 10** — BC lineage vs world-model lineage as two answers to the same PushT problem; comparison table.
  11. Anchor exercise — run pretrained Diffusion Policy on PushT; sample-and-plot multi-modal action chunks; compare against MSE-BC baseline.
  12. Recommended reading order.
  13. What you should now be able to do.
  14. Related curriculum modules + Mentioned in + Open questions.
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 7 entry now links the drafted page (replacing "Future home"); coverage table cell updated to "drafted"; status frontmatter notes Module 7 drafted.
- Updated [index.md](index.md) — new Highlights bullet under Curriculum (Module 7 link); new Syntheses bullet for the module page.
- Pattern set for future modules: a curriculum module body should orient → state objectives → tell a narrative → end with an anchor exercise + reading order + open questions. Module 7 is ~12kB; expect tier-1 modules (NN, CNN, attention, SSL) to be similar size; tier-2/3 modules (Module 5, Module 7, Module 10) somewhat longer; Module 12 (LeWM deep-dive with full SIGReg math) will be the longest.

## [2026-05-10] curriculum-module | Module 6 drafted — Imitation learning and behavior cloning
- Created [Curriculum Module 6 — Imitation learning and behavior cloning](syntheses/curriculum/curriculum-06-imitation-learning.md) — second drafted module; the conceptual prerequisite Module 7 implicitly assumed. Written after Module 7 to close the reader-order gap (Module 7 references "the multi-modal-action failure mode" as if Module 6 were already in place).
- Structure (~12kB):
  1. Curriculum-context callout + acronym pointer to glossary; explicit "Module 7 is the direct successor" framing.
  2. Five learning objectives.
  3. IL vs RL vs world-model + planning comparison table; explicit "why IL dominates 2023–2026 robotics" paragraph.
  4. BC as the simplest possible IL — dataset, model, loss, training, inference, all spelled out.
  5. Where the demonstrations come from — teleop, scripted, human video, cross-platform; the data-diversity-over-quantity scaling pattern (RUM finding).
  6. **Failure mode 1: multi-modal action distributions** — precise statement, mode-averaging math (`E[a|s] = (a_1+a_2)/2` not in either mode), examples, hand-off to Module 7.
  7. **Failure mode 2: distribution shift** — covariate-shift framing, the O(T²) Ross-Bagnell bound, DAgger as the classical fix, why DAgger isn't run in modern practice (data-coverage substitute).
  8. Action chunking + receding-horizon control (orthogonal to action-head choice; Module 7 covers in detail).
  9. Canonical PushT setup (brief; pointer to the [PushT entity](entities/pusht.md) for full mechanics).
  10. **Anchor exercise** — train a vanilla MSE-MLP BC policy on state-variant PushT, roll out for 50 episodes, plot the policy alongside demo trajectories, observe mode-averaging at ambiguous states. Optional extension: mixture-of-Gaussians head (the LSTM-GMM Diffusion Policy ablation).
  11. Recommended reading (concept page → PushT entity → Pomerleau 1989 → DAgger paper → RUM paper); explicit "do not yet read IBC/BeT/DP — that's Module 7."
  12. Hand-off to Module 7 — names IBC, BeT, Diffusion Policy as the three answers to multi-modality.
  13. Related modules + Mentioned in + Open questions.
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 6 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Modules 6 + 7 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 6; Syntheses bullet for Module 6; reader-order is now Module 6 → Module 7.
- Notes for sequencing: Modules 6 + 7 are now reader-consumable in order. The next prereqs that block reader-order continuation are Module 5 (DDPM math, "go deep") for the Diffusion Policy section of Module 7, and Modules 1–4 (Tier 1 ML foundations) for everything. Module 10 (world models, broad) is reader-dependency-light because Modules 6 + 7 + Tier 1 are its main prereqs and Module 10 itself is mostly synthesis from existing wiki pages.

## [2026-05-10] curriculum-module | Module 10 drafted — World models, broad
- Created [Curriculum Module 10 — World models, broad](syntheses/curriculum/curriculum-10-world-models.md) — third drafted module; the bridge into Tier 4 (JEPA depth + LeWM deep-dive). Chosen as the next module because it had the most existing wiki material to lean on ([world-model concept](concepts/world-models/world-model.md), [WM simulators concept](concepts/world-models/world-model-simulators.md), [generative-video vs JEPA synthesis](syntheses/world-models/generative-video-vs-jepa-world-models.md), 8 WM entity pages including the just-filed Dreamer + TD-MPC) and unlocks the Tier-4 destination of the curriculum.
- Structure (~14kB):
  1. Curriculum-context callout — Tier 4 bridge framing; explicit statement that "LeWM = JEPA, end-to-end-trained, with MPC planner" reads as word-soup without this module.
  2. Five learning objectives.
  3. Functional definition — refers out to [`concepts/world-model.md`](concepts/world-models/world-model.md) for the design-axis table; flags world-model ≠ world-simulator distinction.
  4. **The four families** with one example, one structural commitment, pros, cons each:
     - Generative-video (Cosmos, Genie Envisioner — DDPM substrate)
     - JEPA / latent-prediction (V-JEPA 2, LeWM, PLDM — LeCun's program)
     - Frozen-foundation-feature (DINO-WM, JEPA-WMs — DINOv2 base)
     - Reward-conditioned MBRL (Dreamer = generative; TD-MPC = decoder-free)
     Plus a four-row comparison table.
  5. **Planning vocabulary** — MPC loop pseudocode; CEM (full pseudo-code; named as the dominant sampler); MPPI as sibling; gradient-based MPC tradeoffs; "default to assuming MPC means CEM-MPC" rule of thumb.
  6. **Horizon and compounding error** — the O(H) → O(H²) intuition; per-task horizon ranges (5–20 for JEPA / frozen / MBRL); value-bootstrap as the trick that lets MBRL extend effective horizon.
  7. Generative-video vs JEPA tradeoff — points to the [existing synthesis](syntheses/world-models/generative-video-vs-jepa-world-models.md); surfaces three load-bearing facts (48× planning gap, action-free pretraining, complementary-not-competing paradigms).
  8. **Where LeWM lives** — explicit 8-axis table positioning LeWM's choices against alternatives (end-to-end encoder vs frozen; SIGReg vs PLDM/V-JEPA collapse zoo; no value function vs Dreamer/TD-MPC; no reward at training vs MBRL). Each axis flagged as "a contestable bet" the reader should be able to evaluate by Module 12.
  9. **Anchor exercise** — 3-line MPC pseudocode + three concrete extensions (CEM upgrade; toy-MLP-on-pendulum to *see* the optimal-horizon peak; gradient-based MPC comparison). Bridge to LeWM howto code.
  10. Recommended reading (concept pages → generative-video-vs-JEPA synthesis → V-JEPA 2 / DreamerV3 / TD-MPC2 abstracts → LeWM Fig 1 only).
  11. What you should now be able to do.
  12. Hand-off to Module 11 — names V-JEPA progression, collapse-prevention zoo, DINO-WM vs end-to-end, JEPA-WMs.
  13. Related modules + Mentioned in + Open questions (PLDM ingest still gap; Genie Envisioner deeper paper; CEM walkthrough; MPPI source).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 10 entry now links the drafted page; coverage table cell updated to "drafted" with full pre-existing-coverage list (concept + simulators concept + GV-vs-JEPA synthesis + Dreamer + TD-MPC entities and sources); status frontmatter notes Modules 6 + 7 + 10 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 10; Syntheses bullet for Module 10; reader hint that Modules 6 → 7 and Module 10 are now consumable.
- Sequencing note: Modules 6 + 7 + 10 are the three most-loaded modules in the curriculum (most pre-existing wiki material), and they're now drafted. Remaining work splits into:
  - **Tier 1 greenfield** (Modules 1–4: NN, CNN, attention, SSL).
  - **Module 5** (DDPM math, "go deep" — heaviest single piece because of derivations).
  - **Module 8** (RL vocabulary — light; just enough to read MBRL papers).
  - **Module 9** (VLA — has π0 + Helix sources; mostly synthesis from existing concept page).
  - **Module 11** (JEPA depth — heavy synthesis; existing JEPA concept page + V-JEPA 2 / 2.1 / DINO-WM / JEPA-WMs / VLA-JEPA sources).
  - **Module 12** (LeWM deep-dive with full SIGReg math — the destination, longest module).
  - **Modules 13 + 14** (deployment + capstone — leans on already-rich syntheses).

## [2026-05-10] curriculum-module | Module 11 drafted — JEPA in depth
- Created [Curriculum Module 11 — JEPA in depth](syntheses/curriculum/curriculum-11-jepa-deep.md) — fourth drafted module; the Tier-4 successor to Module 10. The single most material-rich module in the curriculum (existing concept page + 6 source pages + 8 entity pages + 3 syntheses).
- Structure (~17kB):
  1. Curriculum-context callout — Tier-4 chain (Module 10 → 11 → 12); explicit framing that SIGReg math is deferred to Module 12.
  2. Six learning objectives.
  3. **What "joint embedding" means** — the architectural commitment (same encoder both sides; loss in latent space); contrast with generative/AR; **why representation collapse is a first-order failure mode** (loss=0 at constant latent).
  4. **The collapse-prevention zoo** — six families with pseudocode where useful: EMA + stop-grad (BYOL/V-JEPA), variance-covariance (VICReg/Barlow Twins), frozen encoder (DINO-WM), asymmetric augmentation (SimCLR), multi-fix soup (PLDM, 4–6 hyperparameters), SIGReg (LeWM, 1 hyperparameter). Side-by-side comparison table.
  5. **V-JEPA progression** — V-JEPA 1 → V-JEPA 2 (1B params, 22M videos, 1M+ hrs) → V-JEPA 2-AC (300M predictor, 62hr DROID, zero-shot Franka in 2 new labs) → V-JEPA 2.1 (dense features, +20pt grasping). Variant scale table; the 16,000× pretraining-vs-post-training data ratio.
  6. **Frozen-feature variants** — DINO-WM (NYU+FAIR, lightweight benches), DINO-world (FAIR, video-scale), JEPA-WMs (FAIR Dec 2025, first JEPA-on-RoboCasa + real Franka).
  7. **Action conditioning** — action-free pretraining + action-conditioned post-training; predictor-level pseudocode; tie back to home-robotics teleop scarcity (Module 13).
  8. **VLA-JEPA** — JEPA-as-auxiliary in a VLA; the cross-over with Module 9.
  9. **LeWM-vs-V-JEPA-2 axis-by-axis** — 9-row comparison table sharper than Module 10's: encoder size (1B vs 15M), encoder training (EMA+stop-grad vs nothing), pretraining data (1M+hr vs none), action stage (post-train vs co-train), anti-collapse mechanism (EMA + L1 + ... vs single SIGReg), anti-collapse hyperparameters (~3 vs 1). The two are not competing for the same job — generalist vs single-task — and LeWM's contribution is methodological (one knob), not scaling.
  10. **Anchor exercise** — annotate LeWM Fig 1 against V-JEPA 2 and DINO-WM; deeper variant: implement a toy 2D JEPA and watch it collapse without anti-collapse mechanisms (then rescue it with each fix in turn).
  11. Recommended reading (concept page → V-JEPA 2 + GitHub + 2.1 → DINO-WM → JEPA-WMs → VLA-JEPA → LeWM architecture only — explicit "do NOT yet read SIGReg derivation").
  12. What you should now be able to do.
  13. Hand-off to Module 12 — names the SIGReg derivation pieces (random projections + empirical CDF + Anderson-Darling-style normality test + backprop through test statistic).
  14. Related modules + Mentioned in + Open questions (PLDM ingest still gap; toy-JEPA notebook; DINOv2 paper; LeCun 2022 position paper).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 11 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Modules 6 + 7 + 10 + 11 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 11; Syntheses bullet for Module 11; reader-order is now Modules 6 → 7 and 10 → 11, all consumable.
- Tier 4 is now half-drafted (Modules 10 + 11). Module 12 (LeWM deep-dive with full SIGReg math) is the destination and the longest module by design.

## [2026-05-10] curriculum-module | Module 12 drafted — LeWorldModel deep-dive (with full SIGReg math)
- Created [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — **the curriculum destination**. Fifth drafted module, completes Tier 4.
- Source: full PDF extraction of `raw/LeWorldMode_2603.19312v2.pdf` via pypdf (per PDF extraction memory). The paper's method, planning, and results sections were re-read from the PDF rather than from the paraphrased source page.
- **Two corrections found during the deep-dive:**
  - The curriculum hub previously described SIGReg's normality test as "Anderson-Darling-style." The paper actually uses **Epps–Pulley**. Curriculum hub fixed; module 12 flags the correction in a top-level callout.
  - The glossary's SIGReg expansion was "Sliced Integral Gaussian Regularization" (with a TBD flag). The paper's actual name is **Sketched Isotropic Gaussian Regularizer** (Balestriero 2025, ref [25] in the LeWM paper). Glossary entry rewritten with the correct name + the Epps-Pulley / Cramér–Wold pieces in place.
- Structure (~25kB; longest module by design):
  1. Curriculum-context callout (destination framing) + the Epps–Pulley vs Anderson-Darling correction.
  2. Six learning objectives.
  3. **§1 — The two-loss architecture** with full forward-pass diagram + 10-line PyTorch pseudocode of the training step.
  4. **§2 — SIGReg in detail (the mathematical centerpiece)**, eight subsections:
     - 2.1 The goal (match isotropic Gaussian; rules out collapse trivially).
     - 2.2 Why high-dim normality testing is hard (multivariate tests don't scale).
     - 2.3 Random-projection sketch — projections `h^(m) = Z u^(m)` with `u^(m) ∈ S^{d-1}`.
     - 2.4 **Cramér–Wold theorem** — formal justification (matching all 1D marginals = matching joint).
     - 2.5 **Epps–Pulley univariate normality test** — explicit integral form via empirical characteristic function vs `e^{-t²/2}`; smooth + differentiable + full-distribution-sensitive (vs Anderson-Darling / KS which are quantile-based and non-smooth).
     - 2.6 **Backprop through the test statistic** — the calculus chain `∂T/∂h_k → ∂T/∂Z`.
     - 2.7 Hyperparameter analysis: M and K empirically insensitive; only λ matters (default 0.1; bisection-tunable in O(log n) vs PLDM's O(n^6)).
     - 2.8 SIGReg in one sentence — every word maps to a design decision.
  5. **§3 — Architecture details** including the **BN-after-CLS-token trick** (load-bearing! ViT's terminal LayerNorm pre-normalizes away the batch distribution SIGReg operates on; swapping to BN in the projection MLP is what makes SIGReg optimizable). Predictor: AdaLN-zero-init for action conditioning, 6-layer transformer + dropout.
  6. **§4 — Latent planning (CEM-MPC)** — terminal goal-matching cost `C(ẑ_H) = ‖ẑ_H − z_g‖²`; CEM solver pseudocode; receding horizon; horizon vs compounding error tradeoff. The 48× speedup decomposed (~200× fewer tokens than DINO-WM).
  7. **§5 — Empirical results** with the headline four-environment table (PushT, Reacher, OGBench-Cube, Two-Room) including the **Two-Room failure case** as a real SIGReg limitation (Gaussian prior over-regularizes when intrinsic task complexity is too low). Ablations on M, K, embedding dim d, encoder architecture (ResNet-18 also works → architecture-agnostic).
  8. **§6 — Latent-space analysis**: physical-quantity probing (Table 1: LeWM beats PLDM, competitive with DINO-WM); latent decoder reconstruction (despite no reconstruction in training); t-SNE; **temporal latent path straightening as an emergent property** (LeWM beats PLDM on this without a smoothness term, despite PLDM having one).
  9. **§7 — Violation-of-expectation framework** — surprise = `‖ẑ_{t+1} − z_{t+1}‖`, used to flag physically implausible events.
  10. **§8 — What this all means** — LeWM as a *methodological* (not scaling) contribution; the bridge to home-robotics deployment via the 15M-param-trainable-on-a-single-GPU profile.
  11. **Anchor exercise** — Part A: reproduce LeWM PushT (per [howto](syntheses/world-models/leworldmodel-howto.md) + [hello-world scope](syntheses/projects/lewm-hello-world-project-scope.md)). Part B: derive the SIGReg gradient on paper.
  12. Recommended reading (LeWM paper end-to-end, GitHub, V-JEPA 2 GitHub as counterpoint, Balestriero 2025 SIGReg paper, generative-video-vs-JEPA synthesis, hello-world scope).
  13. What you should now be able to do.
  14. Hand-off to Modules 13 + 14.
  15. Related modules + Mentioned in + Open questions (Balestriero 2025 source page; PLDM ingest; Two-Room threshold quantification; SIGReg-at-scale).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 12 entry now links the drafted page; fixed the "Anderson-Darling-style" → "Epps–Pulley" / "Cramér–Wold" reference; coverage table cell updated to "drafted"; status frontmatter notes Modules 6 + 7 + 10 + 11 + 12 drafted (Tier 4 complete).
- Updated [Glossary](glossary.md) — SIGReg entry rewritten: correct expansion (Sketched Isotropic Gaussian Regularizer), Balestriero 2025 attribution, Epps–Pulley test, Cramér–Wold theorem, λ default 0.1.
- Updated [index.md](index.md) — Highlights bullet + Syntheses bullet for Module 12; reader can now traverse Modules 6 → 7 and 10 → 11 → 12.
- Tier 4 is now complete. The curriculum's destination (Module 12) is reachable from the wiki's filed material. Five of fourteen modules are drafted.

## [2026-05-10] curriculum-module | Module 9 drafted — Vision-Language-Action models
- Created [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum/curriculum-09-vla.md) — sixth drafted module; closes the policy-side reading chain (Modules 6 → 7 → 9). Sibling of the world-model chain (Modules 10 → 11 → 12).
- Structure (~13kB):
  1. Curriculum-context callout — bridges into both Modules 7 and 11.
  2. Five learning objectives.
  3. Structural definition of a VLA (vision encoder + language tokens + trunk + action head); VLA vs VLM contrast.
  4. **VLA vs BC** — comparison table; the "scaling up + language conditioning + VLM-pretraining" framing.
  5. **Why VLAs aren't world models** — different jobs (actions vs next-state predictions); architectural similarity ≠ identity.
  6. **Action-head design** — AR tokens (OpenVLA), flow matching (π0), DDPM (Diffusion Policy / hybrids); recap table from concepts/vla-models.md.
  7. Major 2026 VLAs in one paragraph each: GR00T, π0, Helix (with S1/S2 caveat), Gemini Robotics (incl. -ER tool-call variant distinction), OpenVLA, smaller VLAs.
  8. **Hierarchical S1/S2 pattern** — recurring across Helix, GR00T, Gemini Robotics-ER; rate-decoupling intuition (~10 Hz reasoning + ~200 Hz control).
  9. **VLA-JEPA cross-over** — explicit architecture diagram showing the JEPA auxiliary loss alongside imitation loss; the "JEPA as a component, not a competitor" framing; bridge to Module 11.
  10. **Anchor exercise** — sketch data flow for π0 / Diffusion Policy / LeWM-MPC on the same PushT episode (3-architecture ASCII diagram); compare per-tick latency budgets and predict 30 Hz feasibility on consumer hardware.
  11. Recommended reading; What you should now be able to do; Closing the policy-side reading chain (with explicit "Module 13 evaluates both chains against deployment reality").
  12. Related modules + Mentioned in + Open questions (OpenVLA + GR00T N1.x + π0.6 source pages still TBD; Helix peer-reviewed paper still doesn't exist; flow-matching concept page on demand).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 9 entry now links the drafted page; coverage table cell updated to "drafted" with full pre-existing-coverage list (concept page + 4 entity pages + 3 source pages); status frontmatter notes both reading chains complete.
- Updated [index.md](index.md) — Highlights bullet for Module 9; Syntheses bullet for Module 9.
- **Reader status:** Modules 6 → 7 → 9 (policy chain) and 10 → 11 → 12 (world-model chain) are both complete. The two paradigms cross over at [VLA-JEPA](entities/vla-jepa.md), covered in detail in this module. Six of fourteen modules drafted.

## [2026-05-10] curriculum-module | Module 13 drafted — Home robotics deployment reality
- Created [Curriculum Module 13 — Home robotics deployment reality](syntheses/curriculum/curriculum-13-home-robotics-deployment.md) — seventh drafted module. Deliberately leans on existing rich syntheses ([assistive-robotics-research-landscape.md](syntheses/assistive/assistive-robotics-research-landscape.md), [stretch-as-assistive-platform.md](syntheses/assistive/stretch-as-assistive-platform.md), [levels-of-autonomy-in-assistive-robotics.md](syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md), [underserved-par-domains.md](syntheses/assistive/underserved-par-domains.md), [lewm-on-stretch-feasibility.md](syntheses/projects/lewm-on-stretch-feasibility.md), [dino-wm-on-stretch-experiment.md](syntheses/projects/dino-wm-on-stretch-experiment.md)) as a curriculum-shaped framing of work already done.
- Structure (~12kB):
  1. Curriculum-context callout — explicit "read these existing syntheses *with* this module" framing (not "read after").
  2. Six learning objectives.
  3. **The 89.4 / 12.4 gap** — RLBench vs BEHAVIOR-1K (per Stanford HAI AI Index 2026); what changes between them (clutter, horizons, robustness, diversity).
  4. **Stretch convergence** — eight features compounding (price, Python API, ~22 dB, MuJoCo/Gazebo support, stretch_ai stack, active research community, Henry Evans deployments). What Stretch *doesn't* solve (bimanual, dexterity, whole-body).
  5. **The "real-data" path** — RUM (NYU/Meta, ~90% on novel envs, data-diversity-over-quantity insight) + OK-Robot (10 NYC homes, 58.5%, VLM + classical pipeline). The honest-pull statement: **the strongest 2026 home-robotics result is BC, not WM** — the WM bet is not yet vindicated empirically.
  6. **PAR + autonomy-preference** — Nanavati 2024 review (1,981 screened, 87 included, half no-PwD); Yang et al. 2025 sense-of-agency finding; Henry Evans summer-deployment record; three-axis autonomy decomposition.
  7. **EUP** — what it is; why it's the natural home for data-efficient policy-learning techniques; HCR Lab as the dominant wiki-cited thread.
  8. **Underserved PAR domains** table (dressing / bathing / medication) with **medication-fetcher** named as the most-tractable researcher target.
  9. **Where LeWM-class techniques fit** — explicit "plausibly move" (data efficiency, planning speed, action-consequence safety/pre-emption) vs "plausibly does not move" (whole-body, long-horizon, robustness-from-pretraining) lists.
  10. **Anchor exercise** — read [LeWM-on-Stretch feasibility](syntheses/projects/lewm-on-stretch-feasibility.md) + [DINO-WM-on-Stretch plan](syntheses/projects/dino-wm-on-stretch-experiment.md), pick one, defend the choice. Explicit framing as "argument for LeWM" vs "argument for DINO-WM" with my-personal-lean (DINO-WM first, LeWM second). Module 14 phase A is "actually scope the experiment you defended here."
  11. Recommended reading + What you should now be able to do + Hand-off to Module 14 + Related modules + Mentioned in + Open questions (LeWM-on-Stretch result; BEHAVIOR-1K WM result; cross-paradigm head-to-head; long-horizon WM eval).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 13 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Module 13 drafted.
- Updated [index.md](index.md) — Highlights bullet for Module 13; Syntheses bullet for Module 13.
- **Reader status:** Seven of fourteen modules drafted. The deployment-reality framing is in place, ready for Module 14 (capstone) to land on top of it.

## [2026-05-10] curriculum-module | Module 14 drafted — Capstone (paper-first, hardware-second)
- Created [Curriculum Module 14 — Capstone (paper-first, hardware-second)](syntheses/curriculum/curriculum-14-capstone.md) — eighth drafted module; the curriculum's terminating exercise. Pointer page tying Modules 12 + 13 to existing wiki artifacts ([hello-world scope](syntheses/projects/lewm-hello-world-project-scope.md), [LeWM howto](syntheses/world-models/leworldmodel-howto.md), [LeWM-on-Stretch feasibility](syntheses/projects/lewm-on-stretch-feasibility.md), [DINO-WM-on-Stretch plan](syntheses/projects/dino-wm-on-stretch-experiment.md)).
- Structure (~10kB):
  1. Curriculum-context callout — phase-A required, phase-B hardware-gated.
  2. What the capstone is — three concrete deliverables.
  3. **Phase A (paper / sim — required):**
     - A.1: reproduce LeWM PushT (one-knob ablation flipping `λ` to feel collapse vs prediction-loss-failure failure modes; the BN-after-CLS engineering footgun explicitly flagged).
     - A.2: SIGReg gradient derivation on paper.
     - A.3: 5–10 page experiment-design memo with eight required sections (task, architecture, data, baselines, metrics, risk register, what-you'd-learn, phase-B gating).
  4. **Phase B (real Stretch — gated):** hardware logistics ($25K Stretch RE3, 40–80+ hr execution); explicit "honest reporting" framing (report what you got, including failure-to-beat-baseline); follow-up memo / short paper as deliverable.
  5. Beyond the capstone — two follow-on research questions (does SIGReg scale to Stretch data; does WM + planning beat or lose to BC + scaled data).
  6. Recommended reading (re-read of all relevant prior artifacts).
  7. What you should now be able to do.
  8. Closing the curriculum — what understanding-becomes-capability looks like.
  9. Related modules + Mentioned in + Open questions (no published LeWM-on-Stretch / DINO-WM-on-Stretch result yet — the capstone is designed to *be* that result).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 14 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes Tiers 3–5 complete.
- Updated [index.md](index.md) — Highlights bullet for Module 14; Syntheses bullet for Module 14.
- **Reader status:** Eight of fourteen modules drafted. **Tiers 3–5 are complete.** Remaining: Tier 1 (Modules 1–4 ML foundations; greenfield), Module 5 (DDPM full math; heavy), Module 8 (RL vocabulary; light). A reader with ML basics already can traverse the entire curriculum end-to-end (Modules 6 → 7 → 9, 10 → 11 → 12, 13 → 14).

## [2026-05-10] curriculum-module | Module 8 drafted — RL vocabulary
- Created [Curriculum Module 8 — Reinforcement learning vocabulary](syntheses/curriculum/curriculum-08-rl-vocabulary.md) — ninth drafted module. Deliberately **light** (~12kB) per the curriculum decision: "RL is not the focus; read for vocabulary, not implementation."
- Structure:
  1. Curriculum-context callout — explicit "skim in 10 min if you know RL; spend 1–2 hr if you don't."
  2. Four learning objectives (read DreamerV3 paragraphs without confusion; parse TD-MPC2 abstract; distinguish policy gradient from value bootstrap; identify on/off-policy).
  3. **MDP** — the (S, A, P, R, γ) tuple; Markov property as modeling assumption.
  4. **Return, value (V/Q), policy** — three core objects + the V↔Q relationship.
  5. **On/off-policy** distinction with concrete examples (PPO on-policy, DQN/SAC off-policy, BC off-policy-ish, modern robotics RL is mostly off-policy or fully offline).
  6. **Policy gradient** — REINFORCE math; A2C variance-reduction; PPO as the modern default (clipped, on-policy, actor-critic).
  7. **Q-learning** — Bellman recursion; DQN target-network trick; DDPG/TD3/SAC as continuous-action extensions.
  8. **MFRL vs MBRL** — the model-question axis that maps onto Module 10's WM taxonomy (MBRL Family 4).
  9. **Dreamer-class latent imagination** — the specific MBRL recipe (train WM from data; train actor-critic *in* the WM; use the actor on real data; loop). Wins (sample-efficient via free imagined rollouts; reward head extends effective horizon) vs losses (model fidelity; reward labels required at training).
  10. Explicit "what this module is *not* doing" — RL theory, modern MFRL deep-dive, offline RL paradigm, implementation details.
  11. **Anchor exercise** — "read a DreamerV3 figure caption out loud and have it parse"; explicit checklist of phrases (actor-critic, imagined rollouts, RSSM, two-hot reward, symlog, world model latent) and where each is defined in this module.
  12. Recommended reading (Wikipedia → OpenAI Spinning Up → DreamerV3 abstract + intro → TD-MPC2 abstract → Sutton & Barto for depth).
  13. What you should now be able to do; Hand-off (use as reference when reading Modules 10–12).
  14. Related modules + Mentioned in + Open questions (Sutton & Barto + Spinning Up reference pages on demand; PPO + Dreamer notebook).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 8 entry now links the drafted page; coverage table cell updated to "drafted"; status frontmatter notes only Tier 1 + Module 5 remain.
- Updated [index.md](index.md) — Highlights bullet for Module 8; Syntheses bullet for Module 8 (placed between Module 7 and Module 9 in chronological order).
- **Reader status:** Nine of fourteen modules drafted. Remaining: Tier 1 (Modules 1–4) and Module 5 (DDPM math). All upper-tier modules (5–14) except Module 5 are now drafted.

## [2026-05-10] ingest | PLDM (Sobal et al., WRL @ ICLR 2025) — closes the most-flagged TBD across Modules 10–12
- User asked what PLDM was during the post-Module-8 review. The answer surfaced two corrections the curriculum had been carrying: (1) the glossary's PLDM expansion was "Planning with Latent-**space** Dynamics Models" (paper title is "Planning with Latent Dynamics Models" — no "-space"); (2) Module 12 + glossary referenced the SIGReg foundational paper as "Balestriero 2025" without naming it as **LeJEPA** (Balestriero & LeCun 2025, [arxiv 2511.08544](https://arxiv.org/abs/2511.08544)). Both corrected here.
- Created [PLDM Paper](sources/pldm-paper.md) — Sobal, Zhang, Cho, Balestriero, Rudner, LeCun (NYU + FAIR; WRL @ ICLR 2025 Workshop, Feb 28 2025; OpenReview ID jON7H6A9UU). PDF extracted via pypdf — 21 pages; ingest reads pages 1–5 (abstract + method) and the headline results tables. Architecture: encoder + predictor end-to-end, multi-term loss = similarity (next-embedding MSE) + VICReg-inspired anti-collapse + inverse-dynamics auxiliary. Planning: latent-space MPC with MPPI sampling. Headline result: **the only method out of 6 tested (HILP, HIQL, GCIQL, CRL, GCBC, PLDM) that doesn't completely fail in any of 6 generalization properties** across 23 carefully-controlled offline reward-free datasets.
- Created [PLDM (Planning with Latent Dynamics Models)](entities/pldm.md) entity — family lineage (2022 precursor "Joint embedding predictive architectures focus on slow features" arxiv 2211.10831 + 2025 stress-test paper); architecture summary; position-vs-adjacent-methods table contrasting PLDM (~6 hyperparameters), LeWM (1), DINO-WM (0, frozen), V-JEPA 2-AC (~3), Dreamer (different family — generative WM), TD-MPC (different family — RL bootstrap).
- Updated [Glossary](glossary.md) — PLDM entry: corrected expansion to "Planning with Latent Dynamics Models" + linked source/entity. SIGReg entry: named the foundational paper as **LeJEPA** (Balestriero & LeCun 2025, arxiv 2511.08544).
- Updated [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md) — "no entity pages yet" line replaced; Dreamer / TD-MPC / PLDM all now linked to entity + source pages. sources 7→8.
- Updated [World model](concepts/world-models/world-model.md) — JEPA-family bullet now lists end-to-end (V-JEPA 2, LeWM, PLDM) vs frozen-feature (DINO-WM, JEPA-WMs) sub-grouping. PLDM Paper added to Mentioned in. sources 10→11.
- Updated [Curriculum Module 10](syntheses/curriculum/curriculum-10-world-models.md) — replaced bare "PLDM" with linked [PLDM entity](entities/pldm.md); closed the Open-questions PLDM TBD.
- Updated [Curriculum Module 11](syntheses/curriculum/curriculum-11-jepa-deep.md) — collapse-prevention zoo §5 (multi-fix soup) now cites PLDM as the canonical reference with details on its specific loss decomposition (similarity + VICReg + inverse-dynamics); closed the Open-questions PLDM TBD; replaced 4 stray glossary-link references to PLDM with entity-link references.
- Updated [Curriculum Module 12](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — SIGReg attribution now names LeJEPA as the foundational paper (arxiv 2511.08544); PLDM comparison line now links source + entity pages; closed the PLDM TBD; renamed the Balestriero-2025 TBD to a LeJEPA TBD (still open — the LeJEPA paper itself isn't ingested as a wiki source page).
- Updated [index.md](index.md) — added PLDM Paper to chronological sources list (2025-02); added PLDM entity under World models section (1 source); closed two "PLDM still needs primary-source ingest" lines in Known gaps; bumped concept counts (world-model 10→11, jepa 7→8); deduplicated a stale JEPA concept entry.
- **Result:** All four LeWM baselines ([DINO-WM](entities/dino-wm.md), [Dreamer](entities/dreamer.md), [TD-MPC](entities/td-mpc.md), [PLDM](entities/pldm.md)) now have primary-source pages. The most-flagged TBD across Modules 10–12 is closed.

## [2026-05-10] ingest | Sobal et al. 2022 (PLDM precursor) + LeJEPA (Balestriero & LeCun 2025; SIGReg foundational paper)
- User asked to file the two follow-on TBDs from the PLDM ingest (the 2022 precursor and the LeJEPA paper). Both filed at abstract-level depth.
- Created [Sobal et al. 2022 — JEPA slow features](sources/sobal2022-jepa-slow-features-paper.md) — Sobal, Jyothir S V, Jalagam, Carion, Cho, LeCun (NYU + FAIR; arxiv 2211.10831; NeurIPS 2022 SSL Theory and Practice Workshop short paper). The first paper in the [PLDM](entities/pldm.md) lineage. Establishes the **slow-features framing**: JEPA representations preferentially encode slowly-varying features (e.g. the location of a moving dot in a pixel scene) when distractor noise varies across timesteps. Documents the **fixed-distractor failure mode**: JEPA fails when noise is fixed across timesteps — exposing that the slow-features bias depends on temporal variability.
- Created [LeJEPA Paper](sources/lejepa-paper.md) — Balestriero & LeCun (Brown + NYU/FAIR; arxiv 2511.08544; Nov 2025). The **foundational SIGReg paper**. Headline contributions: (1) prove isotropic Gaussian is the optimal distribution for JEPA embeddings (minimizes downstream prediction risk); (2) propose **SIGReg** (Sketched Isotropic Gaussian Regularizer) — random-projection + univariate normality test + average — as the regularizer that enforces this distributional shape; (3) demonstrate "single hyperparameter, no stop-gradient, no teacher-student, linear time/memory" SSL training that hits **79% ImageNet-1k linear-eval on ViT-H/14** with validation across 10+ datasets / 60+ architectures. **LeJEPA is the methodological precursor to [LeWM](entities/leworldmodel.md)**: same SIGReg, same single-knob recipe, but LeWM applies it to action-conditioned WM with CEM-MPC for offline RL.
- Updated [Glossary](glossary.md) — SIGReg entry now links the LeJEPA source page directly.
- Updated [Curriculum Module 12](syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — SIGReg attribution links the LeJEPA source page; closed the LeJEPA TBD in Open questions.
- Updated [Curriculum Module 11](syntheses/curriculum/curriculum-11-jepa-deep.md) — SIGReg row in collapse-prevention zoo table now lists *both* LeJEPA (SSL setting) and LeWM (WM setting); evidence column upgraded from "one paper" to "two papers" reflecting the LeJEPA-LeWM pair. Bullet text under SIGReg subsection now explicitly attributes the optimality claim to LeJEPA.
- Updated [PLDM Paper](sources/pldm-paper.md) source page — predecessor section now links the 2022 source page; closed the 2022 TBD in Open questions.
- Updated [PLDM entity](entities/pldm.md) — family lineage section now links both source pages; sources count 1→2; closed the 2022 TBD in Open questions.
- Updated [JEPA concept page](concepts/world-models/jepa.md) — Mentioned in section now lists the new sources; sources count 8→10.
- Updated [index.md](index.md) — both new sources added to chronological list; PLDM entity bumped 1→2 sources; JEPA concept entry bumped 8→10 sources.
- **Result:** the SIGReg-LeWM-PLDM lineage is fully filed. The 2026 LeWM paper now has every cited dependency (LeJEPA for SIGReg theory; PLDM 2022 + 2025 for the end-to-end JEPA baseline) backed by primary-source pages in the wiki.

## [2026-05-10] ingest-deepen | Sobal 2022 + LeJEPA — full PDF ingest of both
- User dropped both PDFs into `raw/` (`2211.10831v1.pdf` for Sobal 2022; `2511.08544v3.pdf` for LeJEPA), explicitly enabling the deeper ingest both source pages had hooks for. Extracted via pypdf per the PDF extraction memory.
- **Sobal 2022 deepened:** rewritten with full architecture details (encoder + predictor + auto-regressive rollout; probing protocol with frozen weights), full method comparison (VICReg-JEPA, SimCLR-JEPA, reconstruction, IDM, supervised, random), the **fixed-distractor failure proof** verbatim (eq. 1–4 in the paper: VICReg's three loss terms all reach 0 at the trivial solution where the encoder ignores foreground and the forward model is identity; SimCLR has the same failure via Wang & Isola's theorem 1), specific dataset details (1M pretraining sequences / 17 frames / two noise types × two temporal regimes), and the empirical-results table (JEPA fails on fixed noise of any kind; reconstruction works for α≤1.5; IDM works in single-dot but fails in 3-dot variant). Added counterintuitive framing: **"JEPA focuses on slow features" is not an unalloyed positive — fixed background = the slowest feature, and JEPA latches on to it instead of the moving dot**, the failure mode that motivates everything else in the JEPA program.
- **LeJEPA deepened:** rewritten with the formal theory chain.
  - **Theorem 1 (isotropic Gaussian optimality):** k-NN regression and kernel regression both have isotropic Gaussian as the *unique* minimizer of integrated square bias under a scalar-covariance constraint.
  - **Lemma 3 (hyperspherical Cramér-Wold):** matching all 1D marginals along directions on `S^{d-1}` is equivalent to matching the joint distribution.
  - **Theorem 2 (sufficiency of directional tests):** the max over `M` directional Epps-Pulley statistics is a level-α + power-1 test, asymptotically.
  - **Definition 2 (practical SIGReg):** **average** over directions, not max — the paper's explicit practical departure from Theorem 2's formal max, made for gradient flow ("avoid sparse gradient over the directions").
  - **Theorem 3 (insufficiency of K moments):** finite-K moment matching is non-identifying; going to large K causes gradient instability.
  - **Why Epps-Pulley** rigorously: ECF is differentiable + parallelizable via `all_reduce` + has bounded loss/gradient/**curvature**. CDF-based (Cramér-von Mises, Anderson-Darling, Watson) require sorting → break SGD parallelism + non-differentiable. KS uses `ℓ_∞` → sparse gradients. Shapiro-Wilk found unstable.
  - Empirical breadth: 10+ datasets, 60+ architectures, up to **1.8B-parameter ViT-g** trained without stop-gradient with stable loss curves. Loss-vs-linear-probe Spearman correlation 94.52% (training loss is a usable model-selection signal without a labeled probe).
- **Module 12 cascaded:**
  - Added a callout in §2.3 explicitly flagging the **average-vs-max** distinction (LeJEPA Theorem 2 = max, formally consistent; Definition 2 = average, practical for gradient flow). Module 12's earlier text was correct but didn't surface this departure.
  - Tightened §2.5 (Why Epps-Pulley) with the LeJEPA §4.2 walkthrough: added bounded *curvature* to the bounded loss/gradient claims; added `all_reduce` distributability; added the explicit ruling-out of moment-based / CDF-based / KS / Shapiro-Wilk alternatives.
- **Module 11 cascaded:** SIGReg row in the collapse-prevention zoo table now mentions the LeJEPA scale evidence (1.8B ViT-g, 10+ datasets / 60+ architectures) and names the formal proof tools (hyperspherical Cramér-Wold + Epps-Pulley) explicitly.
- **Result:** Modules 11 + 12 now have primary-source-grade backing for the SIGReg derivation. The "average vs max" distinction in particular is one the curriculum was carrying without flagging; it's now explicit. The two source pages are the curriculum's deepest (along with the LeWM paper itself) for the SIGReg argument.

## [2026-05-10] curriculum-module | Module 5 drafted — Generative modeling fundamentals (DDPM, full math)
- Created [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](syntheses/curriculum/curriculum-05-generative-models.md) — the curriculum's tenth drafted module, closing Tier 2 and the heaviest single piece by design (the "go deep" decision from 2026-05-10 required full ELBO derivation + KL bounds + classifier-free guidance derivation, written rigorously).
- Structure (~31kB; among the longest curriculum modules alongside Module 12):
  1. Curriculum-context callout with explicit "2–4 evenings" effort estimate.
  2. Six learning objectives (write forward/reverse from memory; derive `L_simple` from ELBO; explain why dropping `λ_t` improves samples; derive CFG from Bayes' on score; place DDPM in the generative-models design space; explain why DDPM matters for Modules 7, 9, 10).
  3. **§1 — Generative modeling primer** (AE, VAE, EBM, score matching) — brief but explicit family map; explicit positioning: DDPM is the dominant 2024–2026 paradigm.
  4. **§2 — DDPM forward process** — single-step + chain + the closed-form marginal `q(x_t | x_0) = 𝒩(√ᾱ_t x_0, (1-ᾱ_t)I)` (Eq. 2.1) and the reparameterization `x_t = √ᾱ_t x_0 + √(1-ᾱ_t) ε` (Eq. 2.2).
  5. **§3 — DDPM reverse process** — parameterized denoising; the prior matches the forward chain's limit.
  6. **§4 — Full ELBO derivation** — bound via Jensen (4.1); per-step decomposition via Bayes/telescoping into L_T + L_{t-1} + L_0 (4.3); the forward posterior `q(x_{t-1} | x_t, x_0)` is Gaussian with explicit `μ̃_t` and `β̃_t` (4.4); KL between two Gaussians (closed form); reduction to a Gaussian-regression problem (4.5).
  7. **§5 — From ELBO to `L_simple`** — the ε-reparameterization (5.1, 5.2); substitution that cancels `x_t` terms; the `λ_t`-weighted MSE form (5.3); the simplified loss (5.4); why dropping `λ_t` improves samples despite making the bound loose. Explicit callout: **this is Module 12's anchor exercise Part B**.
  8. **§6 — Noise schedule** — linear (Ho et al.) vs cosine (iDDPM); the cosine schedule formula (6.1) and motivation.
  9. **§7 — Sampling** — ancestral (DDPM) + DDIM (deterministic non-Markovian, decouples training-step count from inference-step count).
  10. **§8 — Classifier-free guidance, full derivation** — Bayes' rule on score (8.2); the implicit-classifier identity (8.3); the guided distribution (8.4); the score-space combination (8.5); translation back to ε-parameterization (8.6); the "drop conditioning with `p_uncond ≈ 0.1` at training" trick.
  11. **§9 — Conditional diffusion in general** — concatenation, cross-attention, AdaLN, time-step + condition embedding addition.
  12. **§10 — Bridges** — to Module 6/7 (Diffusion Policy = conditional DDPM over action chunks, with a mapping table), Module 9 (π0's flow matching as a sibling), Module 10 (generative-video WMs as DDPM at scale), and EBM/IBC (sibling families that finesse explicit-density issues differently).
  13. **Anchor exercise** — Part A: tiny DDPM on MNIST + DDIM sampling. Part B: derive `L_simple` from ELBO on paper, with five specific sub-tasks (Bayes/telescoping; complete-the-square for `q(x_{t-1} | x_t, x_0)`; ε-reparam; KL-of-Gaussians substitution; identify what's dropped going to `L_simple`).
  14. Recommended reading (DDPM → Diffusion Policy §II → iDDPM → DDIM → CFG → Lilian Weng blog as backup).
  15. What you should now be able to do.
  16. Hand-off to Module 7 / 9 / 10 / 12 — names exact downstream consumers of this module's math.
  17. Related modules + Mentioned in + Open questions (iDDPM / DDIM / CFG / score-matching primary-source pages still TBD; flow-matching concept page; DDPM-on-MNIST notebook artifact).
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Module 5 entry now links the drafted page; module-list heading wraps "Module 5" in a markdown link; coverage table cell updated to "drafted"; status frontmatter notes **Tiers 2–5 complete**, only Tier 1 (Modules 1–4 ML foundations) remains.
- Updated [index.md](index.md) — Highlights bullet for Module 5; Syntheses bullet for Module 5.
- **Reader status:** Ten of fourteen modules drafted. **Tiers 2–5 are complete.** The curriculum is now reader-traversable from Module 5 through the destination (Module 12) and the deployment / capstone modules (13–14), in any order consistent with the module dependency graph. Remaining: Tier 1 (Modules 1–4 ML foundations, greenfield) only.

## [2026-05-10] curriculum-modules | Tier 1 drafted — Modules 1, 2, 3, 4
- Created **[Curriculum Module 1 — Neural networks and training](syntheses/curriculum/curriculum-01-neural-networks.md)** — brisk-but-rigorous NN refresher: neuron, MLP, forward pass, MSE/CE loss, SGD/AdamW, backprop via chain rule, overfitting + regularization remedies, BN vs LN (with the SIGReg-interaction warning), residual connections + why-depth-helps, practical training recipe. Prereq diagnostic at top so readers can skim if comfortable. Anchor exercise: train an MLP digit classifier on MNIST; probe the second-to-last layer with t-SNE; observe the *embedding* emerging as a side effect of training the classifier (groundwork for Modules 4 + 11 framing of "the embedding is the object").
- Created **[Curriculum Module 2 — CNNs and visual representation learning](syntheses/curriculum/curriculum-02-cnns.md)** — convolution operation (locality + weight sharing + translation equivariance), stride / padding, pooling (max / avg / GAP / strided-conv), feature maps + receptive fields (incl. the 3×3 stack trick), ResNet + bottleneck blocks, ResNet variants table with ImageNet top-1, ImageNet pretrain → fine-tune workflow, the "visual encoder" abstraction across BC-line / JEPA-line / VLA, when CNN vs ViT, mentions of U-Net (DDPM substrate), ConvNeXt, etc. Anchor: ResNet-18 features on PushT frames; t-SNE visualization.
- Created **[Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum/curriculum-03-attention-and-transformers.md)** — RNN/LSTM briefly (for context), scaled dot-product attention (with explicit formula + √d_k justification), self-attention, multi-head attention, transformer block (pre-norm vs post-norm), positional encoding (sinusoidal / learned / RoPE), causal masking (LeWM predictor + GPT + BeT), ViT recipe (patch tokenization, [CLS] token, why-more-data-needed), encoder-only / decoder-only / encoder-decoder taxonomy. Anchor: tiny transformer on PushT 8×8 patches with attention-map visualization.
- Created **[Curriculum Module 4 — Self-supervised learning and embeddings](syntheses/curriculum/curriculum-04-self-supervised-learning.md)** — the prerequisite for the JEPA chain. SSL precise definition + vs unsupervised + supervised; contrastive (SimCLR / MoCo) vs predictive (BYOL / DINO / MAE / JEPA) families; the latent space as the object; **representation collapse as a first-order failure mode** (with complete-vs-dimensional distinction); the **five anti-collapse families** — EMA + stop-grad (BYOL-line), variance + covariance (VICReg / Barlow Twins), frozen pretrained encoder (DINO-WM-line), multi-fix soup (PLDM-line), distribution-matching (SIGReg / LeJEPA-line) — with side-by-side comparison table. This is the module that makes Module 11's collapse-prevention zoo parseable. Anchor: VICReg on CIFAR-10 with all three terms vs invariance-only; observe collapse in the invariance-only case via per-dimension variance and linear-probe accuracy.
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — Modules 1–4 entries now link the drafted pages; module-list H4 headings wrap "Module N" in markdown links for all four; coverage table cells updated to "drafted"; **frontmatter status changed from "outline" to "complete — all 14 modules drafted 2026-05-10. Reader-traversable bottom-up. Module bodies may be deepened or revised on signal."**
- Updated [index.md](index.md) — four new Highlights bullets + four new Syntheses-chronological bullets; the curriculum-hub Highlights bullet now flags "all 14 modules drafted."
- **Curriculum status: COMPLETE — 14 of 14 modules drafted.** The reader can traverse the entire curriculum bottom-up from absolute beginning (Module 1 NN basics, no prerequisites beyond linear algebra + chain rule) through the destination (Module 12 LeWM deep-dive with full SIGReg math) and the deployment + capstone modules (13, 14). The dependency graph (encoded in the hub) gives readers permission to skip Tier 1 modules they're already comfortable with — each Tier 1 module has a prereq diagnostic at the top for self-assessment.

## [2026-05-11] ingest | Welch Labs — "Yann LeCun's $1B Bet Against LLMs" (YouTube, 2026-05-01)
- Created [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](sources/welchlabs-lecun-1b-bet-against-llms.md) — 37-min Welch Labs explainer (Stephen Welch et al.) with LeCun interview clips; arc: deep-learning limits → cake-of-intelligence → generative AI → blurry pixels → why-so-blurry → "do we need to be generative?" → Siamese networks → representation collapse → Barlow Twins → DINO → JEPA & world models → "is JEPA good?". Special thanks credits Yann LeCun, Stephane Deny, David Fan, Nicolas Ballas. Embeds the V-JEPA 2 robot-arm demos. Indirectly corroborates the [Towards AI / AMI Labs reporting](sources/towardsai-lecun-ami-labs.md) — the "$1B bet" framing.
- Updated [Yann LeCun](entities/yann-lecun.md) — added in-text link from the "Latent-prediction over generative-video" and "Self-supervised learning at internet-scale" stances to the video as the on-camera articulation of these positions; added Mentioned-in entry; source count 12 → 13; updated 2026-05-11.
- Updated [Joint-Embedding Predictive Architecture](concepts/world-models/jepa.md) — added a `> [!note] Video overview` callout near the top recommending the Welch Labs video as a popular-explainer; added Mentioned-in entry; source count 10 → 11; updated 2026-05-11.
- Updated [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — added a `> [!note] Video overview — recommended before starting` callout near the beginning (right after the Acronyms note) pointing readers at the video as a non-technical orientation to *why* the curriculum points at JEPA / LeWM at all. Updated 2026-05-11.
- Updated [index.md](index.md) — added Sources-chronological bullet for the new video source; bumped [Yann LeCun](entities/yann-lecun.md) and [JEPA concept](concepts/world-models/jepa.md) source counts.

## [2026-05-11] deep-crawl | XLeRobot Documentation — subpage walk (Hardware / Sim / Software / Demos / Related Works)
- Deepened existing [XLeRobot Documentation](sources/xlerobot-docs.md) ingest (originally 2026-05-10). Added a "Deeper crawl — 2026-05-11" section covering: `hardware/hardware_intro`, `hardware/getting_started/{material,3d,assemble}`, `simulation/getting_started/{index,simdemos,vr_sim}`, `software/getting_started/{install,SO101,XLeRobot_teleop,RL,LLM_agent,VLA_ACT,VLA_pi05,VLA_smol,raspberry_pi_setup}`, `demos/`, `relatedworks/`.
- Surfaced new technical detail: PC-does-inference / Pi-relays-WiFi design intent; 12 kg mass; 0.5–1.25 m vertical workspace; 17× STS3215 12 V servos; Anker SOLIX C300 (288 Wh, 10+ hr runtime); BambuLab A1 / PLA print recipe; 8-step assembly with 9-motor expectation; ManiSkill 3.0 scene catalog (ReplicaCAD / AI2-THOR / RoboCasa / OpenCabinetDrawer); custom VRMonitor service over WebSocket-HTTPS for Quest 3; LangChain-style LLM agent on Gemini 3 Flash with RoboCrew tool library and "hey robot" wakeword; three VLA paths (ACT 50-ep, π0.5 via OpenPI fork + `bimanual-toy-box-cleanup` HF dataset, SmolVLA 12-D-padded-to-32-D, 80k steps ≈ 1 h 45 min on A100); RL stack still a placeholder pointing to `lerobot-sim2real` (Stone Tao) + HF HIL-SERL tutorial.
- **Wiki cross-link of note**: XLeRobot's Related Works page explicitly cites **[V-JEPA 2](entities/v-jepa-2.md)** under "Task Planning" — first independent low-cost-robotics platform documented in the wiki to name V-JEPA as a target policy/world-model framework. Added a reciprocal link from [XLeRobot entity](entities/xlerobot.md) → V-JEPA 2.
- Updated [XLeRobot entity](entities/xlerobot.md) — expanded Specs (mass, workspace, power, actuators); rewrote Software section to enumerate the five workflow paths; added V-JEPA 2 to Related; updated 2026-05-11.
- New entities surfaced but **not yet broken out** as their own pages (judgment: parked until a second source surfaces): **HIL-SERL**, **RoboCrew**, **OpenPI**, **STS3215 servo**, **BACH Hand**, **3D-ViTac**, **eFlesh**, **DRAWER**, **CoTracker3**, **RoboTwin 2.0**, **Hunyuan3D-2**, **Bambot**. Listed at the end of the source page so the next ingest can pick them up easily.
- No new source page created (same URL); no index.md bullet change beyond the existing xlerobot-docs entry — same source, more depth.

## [2026-05-11] ingest | Seeed × NVIDIA × Hugging Face Embodied AI Hackathon 2025 Recap
- Created [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](sources/seeed-embodied-ai-hackathon-2025-recap.md) — November 2025 recap blog (Cloudflare-protected; content extracted via Seeed mirror at `seeed.cc/post/2025-embodied-ai-hackathon-recap` and triangulated against the Hackster.io contest page + winners post). Two-site (Shenzhen + Mountain View) Oct 2025 hackathon; 700+ devs registered; ~30 teams (~15 per site); theme = home + cooking robots. Co-organized by [Seeed Studio](entities/seeed-studio.md) + [NVIDIA](entities/nvidia.md) + [Hugging Face](entities/hugging-face.md). Partners: [K-Scale Labs](entities/k-scale-labs.md), [XLeRobot](entities/xlerobot.md), Lightwheel, Solo Tech, FashionStar, Circuit Launch (venue).
- **Winning projects**: U.S. champion = [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) matcha-bot ([XLeRobot](entities/xlerobot.md) + [GR00T N1.5](entities/nvidia-groot.md) via NVIDIA Brev on Jetson Thor); U.S. runners-up = Sprinkle Robot (SmolVLA, 170-ep) + Cloth Folding Robot (ACT + learned reward). China champion = Pick&Place w/ High Generalization ([GR00T N1.5](entities/nvidia-groot.md) on 300-episode 90/10 real/sim dataset); China runners-up = Soft Textiles Folding + **Mate XLeRobot** (hardware-modded XLeRobot with vertical lift-rail — first wiki-documented end-user mod of XLeRobot, addresses the fixed-height workspace limitation).
- **Technical signal**: GR00T N1.5 took both site championships on **non-humanoid dual-arm platforms** (XLeRobot, SO-ARM101). First strong external signal that GR00T fine-tunes work at weekend-hackathon data scales (150–300 episodes) outside the humanoid form factor it was designed for.
- Updated entities: [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) (added matcha-bot championship; 2→3 sources); [XLeRobot](entities/xlerobot.md) (added "In the wild — hackathon traction" section; 1→2 sources); [Seeed Studio](entities/seeed-studio.md) (positioned as co-organizer, not just sponsor; 2→3 sources); [NVIDIA GR00T](entities/nvidia-groot.md) (added N1.5 + Brev + Jetson Thor context; 5→6 sources); [K-Scale Labs](entities/k-scale-labs.md) (mentor role at hackathon — still active weeks before late-2025 shutdown).
- Updated [index.md](index.md) — added Sources-chronological bullet for the new source; bumped source counts and one-line summaries for the four entities above.
- **New entities surfaced but parked**: NVIDIA Jetson Thor + JetPack 7 SDK, NVIDIA Brev, Lightwheel, Solo Tech, FashionStar / StarAI, Circuit Launch, Mate XLeRobot. Listed at the bottom of the source page so a future ingest can pick them up.
- **Open questions logged**: exact October 2025 dates, cash prize amounts (if any), public availability of winning team repos/datasets, and the structural-ecosystem question of why HF + Seeed ran two parallel hackathon brands in 2025 (LeRobot Worldwide June, Embodied AI October).

## [2026-05-11] ingest | SIGRobotics (ACM @ UIUC) — Projects page
- Created [SIGRobotics (ACM @ UIUC) — Projects page](sources/sigrobotics-uiuc-projects-page.md). The site is a React SPA on GitHub Pages — `/projects` returns 404 from the static host but project + sponsor data is hard-coded in the JS bundle (`/static/js/main.e69055b8.js`), which is how the content was extracted. Bundle hash will change on rebuild; documented in the source page's frontmatter.
- **Four flagship projects surfaced**: [LeKiwi](entities/lekiwi.md), 3D-printed Koch arms (no public repo), **Mini Humanoid sponsored by [K-Scale Labs](entities/k-scale-labs.md)** ([micro-sim](https://github.com/SIGRobotics-UIUC/micro-sim)), and a "Turtlebot3 fetches coffee" project sponsored by UIUC CDS.
- **Seven sponsors** named: FrodoBots (big), BitRobot Foundation (big), Saronic (big), Hugging Face LeRobot (normal), Neuralink (normal), ROBOTIS (normal), UIUC CS (normal).
- **Gap-between-website-and-GitHub flagged**: the projects page shows 4 flagships but the GitHub org has ~25 public repos. Surfaced — but not yet broken out to their own pages — the **matcha-bot frontend (`seeed-hack-interface`)** and **`Isaac-GR00T-UIUC`** repos that constitute the Oct 2025 hackathon-win codebase; **F1Tenth autonomous racing**; a **Climbing Robot** project; the **`silent_speech`** EMG/HCI repo (probable Neuralink-sponsorship bridge); the bimanual SO-101 leader/follower repos; and the **FrodoBots Earth Rover Mini SDK** cluster (now explained: FrodoBots is a top-tier sponsor).
- **K-Scale Labs sponsorship of SIGRobotics Mini Humanoid** is the most material new fact — it shows K-Scale was funding *university humanoid-policy work* on top of its hackathon mentorship, all the way into late 2025 before the Series-A failed. The SIGRobotics projects page still lists the sponsorship 5+ months after K-Scale's shutdown (either UIUC hasn't updated or the project continues on prior seed funding — flagged as an open question).
- Updated entities: [SIGRobotics-UIUC](entities/sigrobotics-uiuc.md) (rewrote Projects section to enumerate flagships + GitHub-only projects; new Sponsors section; 3→4 sources); [K-Scale Labs](entities/k-scale-labs.md) (added Mini Humanoid sponsorship; 1→3 sources).
- Updated [index.md](index.md) — added Sources-chronological bullet; refreshed SIGRobotics-UIUC and K-Scale Labs entries with new context + source counts.
- **New entities surfaced but parked**: **FrodoBots / Earth Rover Mini**, **BitRobot Foundation**, **Saronic**, **ROBOTIS / Dynamixel**, **Koch arms (open-hardware lineage)**, **UIUC CDS**. Stub-worthy only if these come up in a second ingest.





## [2026-05-11] ingest | A Path Towards Autonomous Machine Intelligence (LeCun, 2022)
- Created [LeCun 2022 — A Path Towards Autonomous Machine Intelligence](sources/lecun2022-path-towards-ami.md) — long-form deep ingest of LeCun's 62-page position paper. Closes a long-standing wiki gap flagged in three places ([yann-lecun.md](entities/yann-lecun.md) Open questions, [world-model.md](concepts/world-models/world-model.md) Open questions, [curriculum-11-jepa-deep.md](syntheses/curriculum/curriculum-11-jepa-deep.md) references).
- **Why this was a gap, not just a missing reference:** every JEPA / world-model paper in this wiki (V-JEPA 2/2.1, LeWM, DINO-WM, DINO-world, JEPA-WMs, PLDM, LeJEPA, VLA-JEPA) instantiates a piece of *this* document's blueprint. Without the paper, the wiki had implementations without their architectural rationale. The new source page lays out: six-module differentiable agent (perception / world model / actor / cost / short-term memory / configurator); Mode-1 reactive vs Mode-2 deliberative; energy-based-model framing of SSL; the collapse pathology + contrastive-vs-regularized fix taxonomy; JEPA / H-JEPA; intrinsic-cost + learned-critic instead of external reward.
- **AMI Labs gets its missing founding-document link.** Updated [ami-labs.md](entities/ami-labs.md) — the lab's name + mission map directly onto the title + content of the 2022 paper.
- Updated entities: [yann-lecun.md](entities/yann-lecun.md) (13→14 sources; rewrote Public-stance section to add the position paper as canonical reference; removed the "open question" marker; added two new open questions about H-JEPA implementation status and the configurator). Updated concept pages: [jepa.md](concepts/world-models/jepa.md) (11→12 sources; canonical-reference link at top + bottom), [world-model.md](concepts/world-models/world-model.md) (14→15 sources; cleared open-question entry).
- **Concepts surfaced but not yet filed as their own pages** (worth following up): Energy-based models (EBMs), Hierarchical JEPA (H-JEPA), Configurator, Intrinsic motivation, Mode-1 vs Mode-2. The LeCun source page covers them in-depth; pulling them out to their own concept pages would help cross-link future ingests.
- Updated [index.md](index.md) — added a "Sources (foundational, out of chronological order)" subsection holding both this paper and the DINOv3 paper from the same ingest pass; updated the Yann LeCun People entry from 13→14 sources.

## [2026-05-11] ingest | DINOv3 (Siméoni et al., Meta AI Research, August 2025)
- Created [DINOv3 Paper](sources/dinov3-paper.md) — deep ingest of the 67-page technical report. Covers: data scaling via automatic curation (Vo et al. lineage); 7B-ViT architecture w/ axial RoPE + RoPE-box jittering; constant-schedule 1M-iteration training; **Gram anchoring** (the central methodological contribution); single-teacher multi-student distillation family; high-resolution post-training; text alignment; satellite-imagery cross-domain transfer.
- **Gram anchoring is the headline.** The first clean fix for the long-training dense-feature degradation that has plagued SSL ViTs > 300M params since DINOv2. Regularize the *Gram matrix* (patch-pairwise similarity structure) toward an early-iteration "Gram teacher" — local features are free to drift, only the similarity structure is anchored. Decouples dense-feature consistency from global-feature improvement.
- Created [DINOv3](entities/dinov3.md) — new entity page; positioned as DINOv2's architectural and training-recipe successor; flagged Federico Baldassarre as the bridge author (co-corresponding on DINOv3 + senior author on DINO-world); cross-linked the methodological cousin relationship with LeJEPA / SIGReg (both target SSL stability at scale, different stances).
- Updated [dinov2.md](entities/dinov2.md) — added "Successor: DINOv3" section; 3→4 sources; removed the "DINOv3 if released" open-question marker.
- **Headline numbers (frozen 7B backbone, no fine-tuning):** COCO mAP 66.1 / ADE20k mIoU 63.0 (full) or 55.9 (linear) / Cityscapes mIoU 81.1 / NYUv2 depth RMSE 0.309. Beats DINOv2 by 6+ mIoU on ADE20k linear and weakly-supervised baselines by 13+ mIoU.
- **Robotics implication flagged:** every DINOv2-based world model in this wiki ([DINO-WM](entities/dino-wm.md), [DINO-world](entities/dino-world.md), [JEPA-WMs](entities/jepa-wms.md)) is a candidate for DINOv3-upgrade. No paper in this wiki has yet done this — DINOv3 (Aug 2025) post-dates DINO-WM (Nov 2024) but pre-dates JEPA-WMs (Dec 2025), so JEPA-WMs presumably did not have access to it at submission time. Open question logged.
- Updated [index.md](index.md) — added DINOv3 to the "Sources (foundational, out of chronological order)" subsection and to the Vision-foundation-models entity subsection.

## [2026-05-12] ingest | Three foundational SSL papers (Barlow Twins / VICReg / Barlow 1961)
- Created [Barlow Twins Paper](sources/barlow-twins-paper.md) — Zbontar, Jing, Misra, LeCun, Deny (FAIR + NYU; ICML 2021; arxiv 2103.03230). 13-page deep ingest covering the cross-correlation-identity loss, the Information-Bottleneck derivation, comparison with InfoNCE/BYOL/SimSiam/W-MSE, and the key empirical findings (works with batch 256; benefits from high-D embeddings — the opposite of contrastive). Names itself after Horace Barlow's redundancy-reduction principle.
- Created [VICReg Paper](sources/vicreg-paper.md) — Bardes, Ponce, LeCun (FAIR + Inria + NYU; ICLR 2022; arxiv 2105.04906). 23-page deep ingest covering the three-term loss (variance hinge + covariance decorrelation + invariance MSE), the explicit collapse-mode decomposition (norm vs informational collapse), and the structural property that makes VICReg's two branches **independent** (enabling multi-modal SSL, the property LeCun's AMI paper cites as load-bearing). Connects forward to PLDM, LeJEPA, LeWM as the methodological lineage that goes from VICReg's "5–6 hyperparameters" to SIGReg's "1 hyperparameter."
- Created [Barlow 1961](sources/barlow1961-sensory-messages.md) — Horace Barlow's foundational neuroscience chapter (book *Sensory Communication*, MIT Press, 1961). 18-page ingest of the three hypotheses (password / filter / redundancy-reduction) with full focus on redundancy reduction since that's the only one with continuing influence. **This is the eponymous reference for Barlow Twins** — the wiki had implicit "Barlow's redundancy-reduction principle" mentions in several places with no resolving citation. Now it does.
- **Why these three together.** They establish the **complete historical lineage** for the anti-collapse machinery the wiki has been building up: Barlow 1961 (factorial code) → Barlow Twins 2021 (cross-correlation → I) → VICReg 2022 (variance + covariance + invariance) → [LeCun 2022 AMI](sources/lecun2022-path-towards-ami.md) (endorses VICReg-class regularizers for JEPA) → [PLDM 2025](sources/pldm-paper.md) / [LeJEPA 2025](sources/lejepa-paper.md) / [LeWM 2026](sources/leworldmodel-paper.md). Previously the wiki had only the later links of this chain; now the methodological root is anchored in primary sources.
- Updated entities: [yann-lecun.md](entities/yann-lecun.md) (14→16 sources; added Barlow Twins + VICReg to Mentioned-in); [adrien-bardes.md](entities/adrien-bardes.md) (3→4 sources; rewrote Research-thread section — VICReg is now linked to the primary source instead of described in prose; added VICReg as Mentioned-in).
- Updated concepts: [jepa.md](concepts/world-models/jepa.md) (12→14 sources; added Barlow Twins / VICReg / Barlow 1961 to Mentioned-in section).
- Updated existing sources: [lecun2022-path-towards-ami.md](sources/lecun2022-path-towards-ami.md) (VICReg citation now links to source page); [welchlabs-lecun-1b-bet-against-llms.md](sources/welchlabs-lecun-1b-bet-against-llms.md) (Barlow Twins reference now links to primary-source ingest with Barlow 1961 as historical-root link).
- **Concepts surfaced but not yet filed as their own pages** (worth following up): Redundancy reduction / factorial code (the through-line concept that would unify Barlow 1961 → Barlow Twins → VICReg → SIGReg → DINOv3 Gram anchoring); Information Bottleneck (Tishby's framework, the IT-language descendant of Barlow's principle, used in Barlow Twins' theoretical derivation).
- Updated [index.md](index.md) — added all three to the "Sources (foundational, out of chronological order)" subsection; bumped Yann LeCun (14→16) and Adrien Bardes (3→4) source counts on the People entries.

## [2026-05-14] ingest | ViT — An Image Is Worth 16x16 Words (Dosovitskiy et al., ICLR 2021)
- Created [ViT Paper](sources/vit-paper.md) — Dosovitskiy, Beyer, Kolesnikov, Weissenborn, Zhai, Unterthiner, Dehghani, Minderer, Heigold, Gelly, Uszkoreit, Houlsby (Google Research, Brain Team; ICLR 2021; arxiv 2010.11929v2). Deep ingest of the 22-page paper: pages 1–9 (method, headline results, scaling study, attention probing, SSL teaser) read in full; pages 10–22 (references + appendices) skimmed for the position-embedding and inductive-bias details cited in the page body.
- **Why this was an open ingest gap.** The wiki tracks ~12 ViT-encoder-bearing sources downstream ([DINOv2](entities/dinov2.md), [DINOv3](entities/dinov3.md), [V-JEPA 2](entities/v-jepa-2.md), [LeWM](entities/leworldmodel.md), [DINO-WM](entities/dino-wm.md), [DINO-world](entities/dino-world.md), [JEPA-WMs](entities/jepa-wms.md), [PLDM](sources/pldm-paper.md), [LeJEPA](sources/lejepa-paper.md), [VLA-JEPA](sources/vla-jepa-paper.md), [Diffusion Policy](sources/diffusion-policy-paper.md), [Robot Utility Models](sources/robot-utility-models-paper.md)) but had **no primary-source page for ViT itself** — only the [glossary entry](glossary.md#vit) and indirect references from [curriculum-03](syntheses/curriculum/curriculum-03-attention-and-transformers.md). The ViT paper is the natural primary-source companion to the [Attention Is All You Need](sources/attention-is-all-you-need.md) ingest of 2026-05-14 — together they constitute the encoder-only-on-images / encoder-decoder-on-text foundation of every architecture in this wiki past Module 3.
- **Headline content captured**: the patch-tokenization recipe (Eq. 1); the encoder block math (Eq. 2–4, pre-norm); ViT-Base/Large/Huge specs (Table 1); the JFT-300M-vs-ImageNet-21k-vs-ImageNet data-scaling story (Figures 3, 4); the scaling-study finding "ViT uses 2–4× less compute than ResNet" (Figure 5); the attention-distance probing (Figure 6, 7); the SSL teaser that became DINO / MAE / DINOv2 / DINOv3 (§4.6); the training recipe table (Appendix B, Table 3).
- **Headline numbers**: ViT-H/14 JFT-300M → 88.55% ImageNet top-1 / 90.72% ImageNet-ReaL / 94.55% CIFAR-100 / 77.63% VTAB-19, at 2.5k TPUv3-core-days (vs BiT-L 9.9k, Noisy Student 12.3k); ViT-L/16 ImageNet-21k → 85.30% ImageNet top-1 trainable in ~30 days on cloud TPUv3 8-core.
- Updated [glossary.md](glossary.md) — ViT entry now links to the primary-source page instead of citing the paper by name only.
- Updated [Attention Is All You Need source page](sources/attention-is-all-you-need.md) — two existing ViT references now link to the primary-source ingest.
- Updated [curriculum-03 — Sequence models, attention, and transformers](syntheses/curriculum/curriculum-03-attention-and-transformers.md) — two existing Dosovitskiy 2020 references now link to the primary-source ingest; the "Open questions / TBD" entries for the Vaswani-2017 + Dosovitskiy-2020 source pages removed (both now ingested).
- Updated [index.md](index.md) — added ViT to the "Sources (foundational, out of chronological order)" subsection.
- **Concepts surfaced but not yet filed as their own pages** (worth following up): **Patch tokenization** (the conceptual innovation); **Positional encoding for vision** (1D learned vs sinusoidal vs RoPE vs axial RoPE) — referenced in DINOv3 and many later sources without a unifying page; **`[CLS]` vs patch-mean image representations** — a recurring small choice across DINOv2 / DINOv3 / V-JEPA / LeWM.
- **Candidate future ingests** logged in the source page's "Open questions" — DINO (Caron et al. 2021) and MAE (He et al. 2021) are the missing middle of the ViT → DINOv3 lineage.

## [2026-05-14] ingest | Sussmann & Willems 1997 — 300 Years of Optimal Control
- Created [Sussmann & Willems 1997 — 300 Years of Optimal Control](sources/sussmann-willems-1997-300-years-optimal-control.md) — Hector J. Sussmann (Rutgers) and Jan C. Willems (Groningen), IEEE Control Systems Magazine "Historical Perspectives," June 1997, pp. 32–44. **Image-only / scanned PDF**: text extraction returns empty, so the ingest was built from page-by-page visual reading of the 13 rendered pages (`pdftoppm -r 150 -png` → `/tmp/300y-*.png`). Source-page YAML carries an `Ingest depth` callout flagging the scanned-PDF workflow so a future re-ingest with OCR can compare.
- **Why this is a foundational ingest, not an applied one.** The wiki has been accumulating control-theory-flavored sources ([MPC](glossary.md#mpc) inside [LeWM](entities/leworldmodel.md) / [DINO-WM](entities/dino-wm.md) / [V-JEPA 2-AC](entities/v-jepa-2.md), [CEM](glossary.md#cem) as the MPC inner loop, [TD-MPC2](sources/td-mpc2-paper.md), [learning-control-oriented-dynamical-structure](sources/learning-control-oriented-dynamical-structure.md), [MIT drone adaptive control](sources/mit-drone-adaptive-control.md), [Murray 2024 grasping in clutter](sources/murray2024-grasping-clutter-ivfp.md)) without any primary-source anchor for **what optimal control is**, historically and mathematically. This article is that anchor — the canonical modern retrospective on the field.
- **Article's central argument**: optimal control was born in **1697 in Groningen** with Bernoulli's brachystochrone solution, *not* in **1956** with Pontryagin's Maximum Principle. The OC vs CoV distinction is structural — OC adds (a) dynamical constraints `q̇ = f(q, u, t)` separating trajectory from control, and (b) control-set constraints `u ∈ U` allowing non-interior controls (saturated actuators, etc.). The Maximum Principle is the *inequality* version of the Euler–Lagrange equation, completing the historical arc Bernoulli → Euler–Lagrange → Hamilton → Jacobi → Weierstrass → Pontryagin.
- **Section-by-section ingest**: opening; Before 1696 (Greeks, Heron, Dido); Bernoulli's Challenge (verbatim *Acta Eruditorum* 1696 text); 1696–1697 Watershed (Bernoulli brothers, Newton, Leibniz, Tschirnhaus, l'Hôpital; the "ex ungue leonem" Newton anecdote); Why Optimal Control? (the OC ⊋ CoV argument); Bernoulli's Solution (Fermat least-time + Snell → cycloid); Johann Bernoulli and his Family (biography); Euler, Lagrange, Legendre (Euler–Lagrange + Legendre necessary condition); First Fork: Hamilton (canonical equations); Second Fork: Weierstrass (excess function); From Principle to Theorem (Conjectures MN1, MN2, MAX1, MAX2); The Maximum Principle (Pontryagin's 1956 result + 1958 ICM reception); Finale (brachystochrone re-derived as an OC problem — control on unit circle, free terminal time).
- Updated [glossary.md](glossary.md) — MPC entry now mentions the OC lineage (Bernoulli 1697 → Pontryagin 1956) and links to the new source page.
- Updated [index.md](index.md) — added to the "Sources (foundational, out of chronological order)" subsection at the top of the section.
- **Entities surfaced but not yet filed as their own pages**: Johann Bernoulli, Lev Pontryagin (and the Pontryagin Soviet group: Boltyanskii, Gamkrelidze, Mishchenko), Leonhard Euler, Joseph-Louis Lagrange, William Rowan Hamilton, Karl Weierstrass, Hector J. Sussmann, Jan C. Willems. Candidate stubs only if a future "control theory" thread accumulates more sources.
- **Concepts surfaced but not yet filed as their own pages** (the most actionable follow-up): **Optimal control** as an umbrella concept; **Calculus of variations**; **Euler–Lagrange equation**; **Hamilton's equations / Hamiltonian**; **Hamilton–Jacobi PDE**; **Pontryagin's Maximum Principle (PMP)**; **Bellman dynamic programming / value function** (notably absent from this article, but the 20th-century synthesis with HJB). A future `concepts/optimal-control.md` page would naturally hub from this source.
- **Open questions logged in the source page**: the missing "optimal-control" concept page; the Sussmann 1996 "Postscript to History" preprint cited in the references (not yet in `raw/`); the Riemannian-metric / geodesic formulation of the brachystochrone (`ds² = (dx² + dy²)/(2gy)`); the 1958 ICM-reception sociology.

## [2026-05-14] ingest | Six pedagogical-companion sources — user-submitted link review
User submitted six URLs for review. All six judged pertinent to existing wiki threads (one had a direct existing companion source — the Welch Labs LeCun video — making the new Perceptron source a prequel pair). Created six **summary-level** source pages — none are deep paper ingests, all are pedagogical-companion pointers + curriculum-fit assessments. New section in `index.md`: **"Sources (pedagogical / curriculum companions, undated)"** to hold these — they don't fit the chronological-sources timeline or the foundational-papers list.
- Created [Welch Labs — The Perceptron (YouTube, Feb 2025)](sources/welchlabs-perceptron.md) — "ChatGPT is made from 100 million of these." Companion (and pedagogical prequel) to the existing [Welch Labs — LeCun $1B Bet](sources/welchlabs-lecun-1b-bet-against-llms.md) source. Walks Rosenblatt 1957 → Mark I → XOR roadblock → backprop → MLP-at-scale (GPT-3). The "100M" framing flagged as rhetorical in the Open questions (closer to GPT-2-small param count; exact "perceptron" definition is loose).
- Created [3Blue1Brown — How might LLMs store facts | Deep Learning Chapter 7](sources/3blue1brown-mlp-in-llms.md) — Grant Sanderson, Aug 2024. MLP / FFN block inside a transformer as a key–value fact-lookup mechanism. Covers up-projection / ReLU / down-projection, superposition (Johnson–Lindenstrauss), and the "~2/3 of GPT-3's 175B parameters live in MLPs" arithmetic. Foundation for the interpretability / SAE-feature-decomposition program. URL slug `/lessons/mlp` is misleading — the lesson is MLPs *inside transformers*, not a general MLP primer.
- Created [fast.ai — Practical Deep Learning for Coders 2022](sources/fastai-practical-deep-learning.md) — Jeremy Howard's 9-lesson PyTorch + fastai + Hugging Face Transformers + Gradio onboarding. Positioned in the wiki as a **Tier 0 / pre-curriculum on-ramp** for readers without a year of DL programming. Complementary to Karpathy's bottom-up / from-scratch line: same audience, opposite pedagogical direction (library-first vs derive-everything).
- Created [Wolfe — Understanding and Using SFT for Language Models](sources/wolfe-sft-blog.md) — Cameron R. Wolfe, *Deep (Learning) Focus* Substack, Sep 2023. Three-stage alignment (Pretrain → SFT → RLHF); the LIMA "1,000 examples sufficient" finding; survey of LLaMA-2 / Falcon / MPT / Alpaca / Vicuna / Orca / WizardLM. Pairs with the new TRL trainer docs page as the theory + survey side of the SFT pedagogical pair.
- Created [Hugging Face TRL — SFT Trainer documentation](sources/huggingface-trl-sft-trainer.md) — the de-facto SFT trainer for LLMs and VLMs in 2026. One-line API; dataset-format dispatch; chat-template auto-application; PEFT/LoRA, Liger Kernel, Unsloth, RapidFire AI integrations; VLM support (Qwen2.5-VL, LLaVA-Instruct-Mix); tool-calling SFT. Implementation companion to Wolfe's theory-side page; underlies (directly or via forks) every wiki-tracked VLA fine-tuning recipe.
- Created [DS4DS 7.01 — Optimal Control, Introduction (Peitz & Wallscheid)](sources/ds4ds-7-01-optimal-control-intro.md) — Data Science for Dynamical Systems open course (CC BY-SA 4.0; Julia / Jupyter), YouTube Jan 2024. Opening lecture of a 7-lesson module covering intro → discrete-time → LQR → linear MPC → data-driven MPC (DMD) → differential predictive control. Modern-pedagogy companion to [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md) — together they form a complete optimal-control orientation for the wiki's MPC threads.
- Updated [index.md](index.md) — new section **"Sources (pedagogical / curriculum companions, undated)"** with all six entries.
- Updated [Curriculum Module 1 — Neural networks and training](syntheses/curriculum/curriculum-01-neural-networks.md) — added two video-overview callouts at the top of the module: (a) Welch Labs Perceptron for orientation; (b) fast.ai for readers who need a Tier 0 hands-on on-ramp.
- Updated [Curriculum Module 3 — Sequence models, attention, and transformers](syntheses/curriculum/curriculum-03-attention-and-transformers.md) — added video-overview callout pointing at 3Blue1Brown Ch7 for the MLP-inside-transformer mechanics.
- Updated [Curriculum Module 9 — Vision-Language-Action models](syntheses/curriculum/curriculum-09-vla.md) — added LLM-side background callout pointing at the Wolfe SFT survey + the HF TRL SFT Trainer docs.
- Updated [Curriculum Module 10 — World models, broad](syntheses/curriculum/curriculum-10-world-models.md) — added control-theory background callout pointing at the Sussmann & Willems 1997 + DS4DS 7.01 pair.
- Updated [Welch Labs — LeCun $1B Bet source page](sources/welchlabs-lecun-1b-bet-against-llms.md) — added Welch Labs prequel callout cross-linking the new Perceptron video.
- **Entities surfaced but not yet filed as their own pages**: Frank Rosenblatt, Mark I Perceptron, Jeremy Howard, Cameron R. Wolfe, Grant Sanderson / 3Blue1Brown, Younes Belkada, Sebastian Peitz, Oliver Wallscheid, Daniel & Michael Han (Unsloth), Liger Kernel team, RapidFire AI, Data Science for Dynamical Systems (DS4DS) project. Candidate stubs only if a second source from any of these authors / projects surfaces.
- **Concepts surfaced but not yet filed as their own pages**: **Perceptron**, **MLP**, **SFT (Supervised Fine-Tuning)**, **Superposition / Johnson–Lindenstrauss**, **LQR**, **DMD / Koopman operator methods**. The first three are the most overdue — they're all referenced multiple places across the wiki but lack hubs.

## [2026-05-14] ingest | Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed. in-progress draft, 2014–2015)
- Created [Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., 2014–2015 in-progress draft)](sources/sutton-barto-rl-textbook.md) — Richard S. Sutton (UMass / U Alberta / DeepMind) and Andrew G. Barto (UMass Amherst), A Bradford Book / MIT Press. The canonical RL textbook ("the RL bible"). **Version flagged**: the PDF on file is the 2014–2015 in-progress draft (352 pages, PDF CreationDate 2015-04-12), not the 2018 final 2nd edition (~550 pages with substantially expanded policy-gradient + deep-RL applications coverage). Ingest is **section-summary level** — frontmatter, Ch 1 (RL problem), Ch 3 (MDPs), Ch 4–8 (Tabular DP / MC / TD / eligibility traces / planning), Part II (function approximation Ch 9–11), Part III (frontiers Ch 12–15). Not a verbatim reproduction; a future re-ingest against the 2018 final is logged in the page's Open questions.
- **Closes the most-flagged TBD in the wiki's RL coverage.** Two turns ago, in the explanation-of-RL response, I flagged Sutton & Barto as "the canonical textbook, not yet ingested, referenced via the glossary." The user added it to `raw/` and asked to ingest. Direct response to that gap.
- **Why this is a foundational ingest, not just a textbook ingest.** Every MBRL / world-model / RLHF / VLA paper in the wiki inherits Sutton-Barto vocabulary verbatim — value functions, policies, on/off/offline policy, TD bootstrapping, actor-critic. Specifically: [DreamerV3](sources/dreamer-v3-paper.md), [TD-MPC2](sources/td-mpc2-paper.md), every JEPA-line world model ([LeWM](sources/leworldmodel-paper.md), [DINO-WM](sources/dino-wm-paper.md), [DINO-world](sources/dino-world-paper.md), [JEPA-WMs](sources/jepa-wms-paper.md), [PLDM](sources/pldm-paper.md)), every VLA's RLHF stage ([π0](sources/pi-zero-paper.md), [Helix](sources/helix-blog.md), [GR00T](entities/nvidia-groot.md)), and every fly-brain / [biomechanical-simulation](concepts/bio/biomechanical-simulation.md) controller ([flybody](entities/flybody.md), flygym, [NeuroMechFly](entities/neuromechfly.md)).
- **Bridge to optimal-control thread.** The "RL = approximate optimal control over an unknown dynamics model, with samples instead of derivatives" framing makes Sutton-Barto + [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md) the two complementary primary-source foundations for the entire control-and-decision-making thread. Bellman dynamic programming (Ch 4) is the discrete-time / stochastic-extension of the Pontryagin Maximum Principle.
- **Captured the field's notation conventions** (Ch 1 + Summary of Notation): `S_t`, `A_t`, `R_t`, `γ`, `π(a|s)`, `v_π(s)`, `q_π(s,a)`, `v_*`, `q_*`, `δ_t`, `α`, `β`, `λ`, `E_t(s)`. Every later RL paper that the wiki touches uses these symbols.
- **Equations table** in the source page captures the wiki-relevant 12: returns, value functions, Bellman equation, Bellman optimality, TD(0) update, TD error, Q-learning, SARSA, discount, eligibility trace, TD(λ). This is the field's canonical vocabulary.
- Updated [Curriculum Module 8 — RL vocabulary](syntheses/curriculum/curriculum-08-rl-vocabulary.md) — Sutton & Barto Recommended-reading entry (position 5) now links the primary-source page; "standard reference" mention earlier in the module also linked. Both updates land in existing prose without restructuring.
- Updated [glossary.md](glossary.md) — RL entry now points at the Sutton & Barto source page as the canonical textbook reference.
- Updated [index.md](index.md) — added Sutton & Barto to the "Sources (foundational, out of chronological order)" subsection.
- **Entities surfaced but not yet filed**: Richard S. Sutton, Andrew G. Barto (2024 Turing Award winners — most overdue stubs), A. Harry Klopf, Christopher Watkins (Q-learning thesis 1989), Gerald Tesauro (TD-Gammon), Arthur Samuel (checkers, 1959), Wolfram Schultz / Peter Dayan / Read Montague (dopamine = TD-error). Stubs would let future RL-history ingests attach.
- **Concepts surfaced but not yet filed as their own pages** (the most actionable follow-up): a hub `concepts/reinforcement-learning.md` — the most overdue concept page in the wiki. Sub-concepts: **MDP**, **Bellman equation**, **dynamic programming**, **Monte Carlo methods**, **temporal-difference learning**, **eligibility traces**, **Q-learning**, **SARSA**, **Dyna / MBRL**, **MCTS**, **actor-critic**, **function approximation**, **on-policy vs off-policy**, **exploration vs exploitation**, **POMDP**, **options / temporal abstraction**.
- **Open questions logged in the source page**: re-ingest against the 2018 final 2nd ed. (substantial policy-gradient depth added); the `concepts/reinforcement-learning.md` hub creation; entity stubs for Sutton + Barto; a bridge synthesis `syntheses/optimal-control-and-rl.md` unifying this source with [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md); TD-Gammon stub; foundational primary-source ingests (Bellman 1957, Howard 1960, Watkins 1989); OpenAI Spinning Up as a pedagogical-companion source.

## [2026-05-14] re-ingest | Sutton & Barto — Reinforcement Learning: An Introduction (2018 final 2nd edition)
- Closed the top open question from the earlier same-day ingest. The published **2018 final 2nd edition** (`raw/RLbook2020.pdf`, 548 pages, ISBN 9780262039246, ©2018/2020, CC BY-NC-ND 2.0) was added to `raw/` and ingested. The existing source page [sutton-barto-rl-textbook.md](sources/sutton-barto-rl-textbook.md) was **updated in place** to make the 2018 final the canonical reference; the 2014–2015 in-progress draft is retained as `draft_path` in the frontmatter for historical reference.
- **Major content additions captured in the update:**
  - **Ch 13 — Policy Gradient Methods (pp. 321–338).** New full chapter. Captured the Policy Gradient Theorem (Eq 13.5) — `∇J(θ) ∝ Σ_s μ(s) Σ_a q_π(s,a) ∇π(a|s,θ)` — with a paraphrase of the textbook's first-principles proof. REINFORCE (Eq 13.8), REINFORCE with Baseline (Eq 13.11), Actor-Critic (§13.5) with the one-step update. The soft-max policy parameterization. Continuous-action Gaussian policies (§13.7). This is the lineage of A2C / A3C / TRPO / PPO / SAC / GRPO — the family underlying every RLHF-tuned LLM and the wiki-tracked VLA fine-tuning pipelines ([π0](sources/pi-zero-paper.md), [GR00T](entities/nvidia-groot.md), [Helix](sources/helix-blog.md)).
  - **Ch 16.5 — DQN / Human-level Video Game Play (Mnih et al. 2015, Nature).** The canonical deep-RL paper. Q-learning + deep convolutional ANN + experience replay + target network, 49 Atari games with identical hyperparameters.
  - **Ch 16.6 — AlphaGo + AlphaGo Zero (Silver et al. 2016, 2017).** The cleanest demonstration that Ch 8 (MCTS) + Ch 13 (policy gradient) + deep function approximation compose into superhuman game-play. AlphaGo Zero reached superhuman level in 3 days from self-play alone, beating AlphaGo 100–0.
  - **Ch 11.3 — The Deadly Triad.** Function approximation + bootstrapping + off-policy training → divergence risk. Sutton's cleanest theoretical diagnosis of why deep-RL training is fragile. Now in the wiki's equations table.
  - **Ch 12 — Eligibility Traces moved from draft's Ch 7.** Now uses the `z_t` vector-eligibility notation (changed from `e_t` in 1st edition); the true online TD(λ) (van Seijen & Sutton 2014) is the chapter's centerpiece.
  - **Ch 17 — Frontiers (renamed from "Prospects").** New §17.4 "Designing Reward Signals" explicitly recognizes the brittleness of reward-specification for real-world tasks — the recognition that became central to the post-2018 robot-learning literature.
- **Equations table** expanded from 13 → 19 entries: added Expected SARSA, the Policy Gradient Theorem, REINFORCE, REINFORCE with baseline, one-step actor-critic, soft-max policy, the Deadly Triad. The wiki now has the full canonical-vocabulary cheatsheet.
- **Position-in-lineage diagram** updated: DQN 2013/2015, AlphaGo 2016, AlphaGo Zero 2017, PPO 2017, the 2018 publication, the 2024 Turing Award.
- **Open question resolved.** Removed "re-ingest against the 2018 published 2nd edition" from the source page's open questions (this *is* that re-ingest). Two new open questions added: **`concepts/policy-gradient.md` hub page** — would unify the SFT→RLHF pipeline ([Wolfe](sources/wolfe-sft-blog.md), [TRL](sources/huggingface-trl-sft-trainer.md)) with PPO/SAC/GRPO; defer until a primary PPO source is ingested. **The Deadly Triad as a standalone concept page** — increasingly cited in deep-RL papers.
- Updated [index.md](index.md) — entry now reflects the 2018 final as canonical, names Ch 13, Ch 16 DQN/AlphaGo, Ch 11 Deadly Triad, and the 2024 Turing Award.

## [2026-05-14] concept | File concepts/optimal-control.md
- Created [Optimal control](concepts/robotics/optimal-control.md) — the most-flagged TBD concept-page across the wiki. Open-question flag previously appeared in [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md), [DS4DS 7.01](sources/ds4ds-7-01-optimal-control-intro.md), and (indirectly) [Sutton & Barto](sources/sutton-barto-rl-textbook.md) — now resolved. Both of those open questions in the source pages have been edited to ✅-resolved markers pointing at the new concept page.
- **Page structure**: one-line definition → the problem class (with structural CoV-vs-OC distinction lifted from Sussmann-Willems) → three classical solution paths (Euler-Lagrange / HJB-DP / Pontryagin MP) with the equations → modern computational instances table (LQR / MPC / iLQR / CEM / adaptive control) → the OC ↔ RL bridge (table contrasting the two perspectives, citing Sutton-Barto Ch 4) → why-it-matters-in-this-wiki (the learned-WM thread does OC; robots use LQR/MPC; the OC↔RL bridge connects the wiki's two control-and-decision-making threads) → historical lineage from 1696 to 2024 → key references → related concepts → open questions → Mentioned-in (12 sources + 4 syntheses).
- **Sources count**: 12, derived from the 12 source pages in the wiki that directly reference optimal-control concepts (MPC, LQR, Pontryagin, Bellman, Hamilton-Jacobi, brachystochrone, etc.).
- **Key concepts surfaced in this hub but not yet broken out** as their own concept pages (logged as open questions on the hub): **calculus of variations**, **Euler-Lagrange equation**, **Hamilton-Jacobi-Bellman PDE**, **Pontryagin's Maximum Principle**, **LQR / Riccati equation**, **MPC** (currently glossary-only), **iLQR / DDP**, **the Deadly Triad** (Sutton-Barto Ch 11.3 — already flagged), **Bellman dynamic programming**.
- **Most-overdue follow-up flagged**: `concepts/reinforcement-learning.md` hub page. With this OC hub in place + the Sutton-Barto source ingested, the RL hub becomes the *new* most-overdue concept-page creation.
- **Second-most-overdue follow-up flagged**: `syntheses/optimal-control-and-rl.md` — a bridge synthesis pairing the two foundational sources ([Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md) and [Sutton & Barto 2018](sources/sutton-barto-rl-textbook.md)) into a single "the two books and how to read them in conversation" piece. Both primary sources are now in the wiki; the synthesis is overdue.
- Updated [glossary.md](glossary.md) — MPC entry now links the new concept hub instead of just citing the lineage prose.
- Updated [index.md](index.md) — added Optimal control to the Concepts section.
- Updated [Sussmann & Willems source page](sources/sussmann-willems-1997-300-years-optimal-control.md) — resolved-marker on the previously-flagged concept-page open question.
- Updated [DS4DS 7.01 source page](sources/ds4ds-7-01-optimal-control-intro.md) — resolved-marker on the same.

## [2026-05-14] ingest | NVIDIA Brev — overview & docs
- Created [NVIDIA Brev Docs](sources/nvidia-brev-docs.md) — meta-source covering the public Brev docs at `docs.nvidia.com/brev/*`: overview, quickstart, gpu-instances concept, environments, launchables, CLI getting-started, instance-management, gpu-types reference, and the AI-agent skill page.
- Created [NVIDIA Brev](entities/nvidia-brev.md) — new entity (subtype: product). NVIDIA's cross-cloud GPU-instance broker; acquired from brev.dev in 2024. CLI surface: `brev list / start / stop / stop --all / delete / shell`, plus Launchables (shareable one-click GPU envs).
- Updated [NVIDIA](entities/nvidia.md) — bumped sources 13 → 14; added Brev to the products line and to Mentioned-in.
- Updated [index.md](index.md) — added Brev source to the chronological list and the Brev entity under Tools; bumped NVIDIA's source count.
- **Cost-management focus**: this ingest was driven by the user's question "how do I use Brev without a large bill". Key finding: Brev has **no native auto-stop, idle-timeout, TTL, or spend-cap** as documented. The only real cost lever is the user running `brev stop --all` (or wiring it into their own scripts / cron). Stopped instances have ~zero compute cost but minor storage cost + capacity-loss restart risk; deleting (after `git push`) is the right call for multi-day breaks.
- **Open questions on the source page**: web-console idle settings; programmatic usage/billing API; published rate sheet; spot/preemptible/reserved options.

## [2026-05-14] ingest | Isaac Launchable (isaac-sim/isaac-launchable)
- Created [Isaac Launchable Repo](sources/isaac-launchable-repo.md) — NVIDIA's official Brev Launchable (`env-35JP2ywERLgqtD0b0MIeK1HnF46`) for "try [Isaac Sim](entities/nvidia-isaac-sim.md) + [Isaac Lab](entities/nvidia-isaac-lab.md) in a browser". VS Code container + Isaac Sim 5.1 + Isaac Lab 2.3 + Omniverse Kit App Streaming. v1.2.1 (Jan 2026), 150★, license is the NVIDIA Isaac Sim Additional Software & Materials Agreement (not OSS).
- Updated [NVIDIA Brev](entities/nvidia-brev.md) — bumped sources 1 → 2; added a "Notable Launchables" section featuring Isaac Launchable as the canonical multi-container browser-delivered example.
- Updated [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) and [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) — bumped each 5 → 6; added 2026 version-drift note flagging that the Launchable ships **5.1 / 2.3**, not the GTC-2026 Sim 6.0 / Lab 3.0 / Newton 1.0 GA stack the wiki tracks elsewhere.
- Updated [index.md](index.md) — added Isaac Launchable to the chronological sources list; bumped Isaac Sim, Isaac Lab, and Brev source counts.
- **Cost angle (continuation of the previous ingest's theme)**: this Launchable is a cost-discipline trap because (a) RT-core requirement rules out T4 / V100 / P4 — you're paying L40-class rates from minute one, (b) the browser-tab-as-IDE feel makes it easy to leave running overnight, and (c) the "learning environment" framing invites multi-day tutorial sessions where `brev stop` hygiene matters most.
- **Open questions on the source page**: actual $/hr at AWS-default; PhysX vs Newton backend exposure inside Lab 2.3; when the Launchable will bump to Sim 6.0 / Lab 3.0; whether smaller RT-core GPUs (L4 / A10G) can host Kit App Streaming as a cheaper floor.

## [2026-05-15] ingest | NVIDIA GEAR Lab — Publications page
- Created [NVIDIA GEAR Lab — Publications](sources/nvidia-gear-publications.md) — meta-source covering the lab's publication list. Page is a Next.js SSG SPA with the publication data hard-coded into `pages/publications-*.js`; extracted **32 unique publications** (Nov 2022 → Aug 2026) by parsing the JS chunk.
- Created [NVIDIA GEAR](entities/nvidia-gear.md) — new entity (subtype: research-lab). Generalist Embodied Agent Research; co-founded Feb 2024 by [Jim Fan](entities/jim-fan.md) and [Yuke Zhu](entities/yuke-zhu.md). Five output pillars mapped: GR00T humanoid stack / Dream*-WM line / Eureka / open-ended agents / sim+data infrastructure.
- Created [Jim Fan (Linxi Fan)](entities/jim-fan.md) — new entity (subtype: person). NVIDIA Director of Robotics, Distinguished Scientist; pre-GEAR author on MineDojo / VIMA / Voyager / Eureka.
- Updated [Yuke Zhu](entities/yuke-zhu.md) — bumped sources 2 → 3; promoted to "Associate Professor" + GEAR co-lead. Added Jim Fan / GEAR cross-links.
- Updated [NVIDIA](entities/nvidia.md) — bumped sources 14 → 15; added GEAR to the products / labs paragraph and Related.
- Updated [NVIDIA GR00T](entities/nvidia-groot.md) — bumped sources 6 → 7; added the original GR00T N1 paper (arXiv 2503.14734, Mar 2025) under Versions seen with full author list; linked GEAR.
- Updated [RoboCasa](entities/robocasa.md) — bumped sources 4 → 5; corrected provenance: original RoboCasa is GEAR-authored (RSS 2024), not just RoboCasa365 (ICLR 2026). Linked GEAR.
- Updated [MimicGen](entities/mimicgen.md) — bumped sources 1 → 2; added the original CoRL 2023 outstanding-paper award and GEAR provenance.
- Updated [NVIDIA Isaac Lab](entities/nvidia-isaac-lab.md) — bumped sources 6 → 7; flagged the Nov 2025 GEAR Isaac Lab paper (arXiv 2511.04831) as the primary reference paper.
- Updated [index.md](index.md) — added GEAR Publications to chronological sources; added GEAR + Jim Fan to entities; bumped NVIDIA / NVIDIA Isaac Lab / NVIDIA GR00T / RoboCasa / MimicGen / Yuke Zhu source counts.
- **Highest-priority follow-up paper ingests** (logged on the source page): DreamGen / DreamZero / DreamDojo (the WM triplet — clean NVIDIA-side counterpoint to the FAIR JEPA program); FLARE (implicit WM, neighbours LeWM/DINO-WM); the humanoid cluster as a single synthesis (HOVER + SONIC + ASAP + Doorman + VIRAL); Eureka + DrEureka → seed `concepts/llm-reward-design.md`; MineDojo + Voyager + NitroGen → seed `concepts/open-ended-agents.md`; the Isaac Lab Nov-2025 paper as the primary reference for the Isaac Lab entity (currently sourced only from blogs).

## [2026-05-15] query | "What is the best way to train the ROSOrin Pro to pick up Legos and put them in bins?"
- Synthesized from [ROSOrin Pro](entities/rosorin-pro.md), [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md), [OpenClaw](entities/openclaw.md), [LeWM-on-ROSOrin-Pro feasibility](syntheses/projects/lewm-on-rosorin-pro-feasibility.md), [JEPA project ladder for ROSOrin Pro](syntheses/projects/jepa-project-ladder-rosorin-pro.md), [Robot Utility Models](entities/robot-utility-models.md), [LeRobot](entities/lerobot.md), [Diffusion Policy](entities/diffusion-policy.md), [Embodied AI Hackathon 2025 recap](sources/seeed-embodied-ai-hackathon-2025-recap.md).
- Filed as [ROSOrin Pro — Lego pick-and-place project plan](syntheses/projects/rosorin-pro-lego-pick-place.md) — the **BC-path sibling** to the existing JEPA project ladder, same hardware, same ladder framing, different goal. Three tiers: Tier 1 (OpenClaw color-threshold + AprilTag bin, hours), Tier 2 (LeRobot ACT/Diffusion Policy on 500–1000 teleop demos, ~weeks — **the recommended path** for "robust enough to use"), Tier 3 (GR00T fine-tune, months, probably overkill on Orin Nano compute).
- **Hardware reality check** elevated to its own section before the tiers because the entity pages flag two open questions the manuals don't answer (gripper payload + workspace reach), and getting either wrong invalidates Tiers 2/3. Recommends bench-testing 2×2 → 1×2 → 1×1 brick grasps before any ML investment.
- Updated [index.md](index.md) — added the synthesis under JEPA / LeWorldModel highlights (paired with the JEPA project ladder).


## [2026-05-15] file | Chain of thought concept page
- Created [Chain of thought](concepts/learning/chain-of-thought.md) — hub page seeded from general knowledge (no primary source ingested yet). Covers: definition + scratchpad-as-compute intuition; lineage (Wei 2022 → Kojima zero-shot → self-consistency → ToT → modern RL-trained reasoning models o1/R1/Claude extended thinking); faithfulness caveat; robotics relevance (embodied CoT in VLAs, S1/S2 split in Helix and GR00T, Gemini Robotics-ER).
- Linked to [LLM-agent architecture](concepts/agents/llm-agent-architecture.md), [VLA models](concepts/learning/vla-models.md), [AI safety and alignment](concepts/safety/ai-safety-alignment.md).
- Updated [index.md](index.md) — added entry under Concepts with `(0 sources — hub page)` annotation.
- Open follow-up: when a primary CoT source is ingested (Wei et al. 2022, an embodied-CoT VLA paper, or a reasoning-model report), promote this from a hub page to a sourced concept page and back-link from existing source pages that already gesture at CoT (Helix blog, GR00T pages, Spot + Gemini Robotics).

## [2026-05-15] query | "tell me more about Atari 2600 learning"
- Synthesized from [ALE entity](entities/ale.md), [ALE Farama source](sources/ale-farama.md), [Sutton & Barto §16.5 DQN](sources/sutton-barto-rl-textbook.md), [curriculum-08 RL vocabulary](syntheses/curriculum/curriculum-08-rl-vocabulary.md), [optimal control timeline](concepts/robotics/optimal-control.md).
- Filed as [Atari RL lineage — from ALE to Agent57 and MuZero](syntheses/rl/atari-rl-lineage.md) — hub page tying the scattered Atari/DQN material together and adding post-DQN lineage the wiki doesn't otherwise cover: value-based track (Double/Dueling DQN → PER → C51 → Rainbow), policy-gradient track (A3C/IMPALA/PPO), hard-exploration track (Pseudo-counts → RND → Go-Explore → Agent57), and model-based catch-up (MuZero → EfficientZero → DreamerV3). Closes with why robot-learning moved on (discrete actions, no physics) but kept the toolbox (replay buffers, target nets, PPO, learned-WM+planner).
- Updated [index.md](index.md) — added entry at top of Syntheses section.
- Open follow-up: Mnih 2015 Nature paper, MuZero (Schrittwieser 2020), Agent57 (Badia 2020), Rainbow (Hessel 2018) all flagged on the synthesis page as candidate primary-source ingests that would replace textbook-summary citations with direct ones. If Go-Explore/RND/Agent57 ingest happens, seed `concepts/exploration-rl.md`.

## [2026-05-15] ingest | EgoScale — Scaling Dexterous Manipulation with Diverse Egocentric Human Data (NVIDIA GEAR, Feb 2026)
- User dropped `raw/2602.16710v1.pdf` (Zheng et al., NVIDIA GEAR + UC Berkeley + UMD, arXiv 2602.16710v1, 22 pages) and asked to ingest. Project leads: [Yuke Zhu](entities/yuke-zhu.md), Danfei Xu, [Jim Fan (Linxi Fan)](entities/jim-fan.md).
- Created [EgoScale Paper](sources/egoscale-paper.md) — the **first published VLA pretraining scaling law**: `L = 0.024 − 0.003·ln(D)` with R² = 0.9983 over the 1k → 20k hr range, where D = hours of egocentric human video. Headline: validation loss tracks real-robot performance, so the scaling law is practically useful (offline metric predicts online success).
- **Closes the GR00T-pretraining-corpus question**: the wiki has cited GR00T N1.7 EA's "20,854 hours of egocentric human video" for weeks without a primary source. EgoScale is that primary source. The 20,854-hour figure matches exactly.
- **Two-stage transfer recipe**: Stage I (large-scale human pretrain on 20K hr, 100K steps on 256 GB200 GPUs) → Stage II (50 hr aligned human-robot mid-training on matched-camera tasks) → Stage III (10K-step task-specific post-training). Stage II is the novel architectural contribution; ablations show neither stage alone reproduces the +54% over no-pretrain result.
- **Cross-embodiment headline**: pretraining transfers from the 22-DoF Sharpa Wave hand (primary training target) to the Unitree G1's tri-finger hand with +30% absolute improvement, evidence that the human-data motor prior is embodiment-agnostic rather than corpus-specific.
- **Action-space ablation matters**: retargeted joint-space hand actions beat fingertip-SE(3) and wrist-only representations across all dexterous tasks. The scaling law applies to the **joint-space** action representation specifically.
- Created [Scaling laws — VLAs and human data](concepts/learning/scaling-laws-vla.md) — new concept hub seeded by EgoScale. Closes a major gap: the wiki tracks ~13 VLAs but had no scaling-law treatment. EgoScale is the canonical entry point.
- Created [Sharpa Wave hand](entities/sharpa-wave.md) — 22-DoF dexterous hand entity stub (subtype: hardware).
- Created [EgoDex dataset](entities/egodex.md) — 829 hr Apple Vision Pro–captured egocentric dataset; the high-precision complement to in-the-wild data in EgoScale's pretraining mix.
- Updated [NVIDIA GR00T](entities/nvidia-groot.md) — promoted EgoScale to the primary source for the N1.7 pretraining corpus; sources 11 → 12.
- Updated [VLA models](concepts/learning/vla-models.md) — added EgoScale to the "Notable VLAs" list, added the EgoScale row to the action-head taxonomy table, added a "State of the field" paragraph on the human-video-pretraining path as a parallel to the Cosmos / WFM synthetic-data path; sources 19 → 20.
- Updated [Jim Fan](entities/jim-fan.md), [Yuke Zhu](entities/yuke-zhu.md), [NVIDIA GEAR](entities/nvidia-gear.md), [NVIDIA](entities/nvidia.md) — added EgoScale references + bumped source counts.
- Updated [NVIDIA GEAR Lab — Publications](sources/nvidia-gear-publications.md) — marked entry #2 (EgoScale) as ingested with backlink to the new source page.
- Updated [index.md](index.md) — added EgoScale source under the GEAR / NVIDIA chronological cluster; Sharpa Wave under Robot platforms; EgoDex under Datasets; Scaling laws — VLAs under Concepts. Synced several source counts to match frontmatter after this and the prior lint pass.
- **Open follow-ups** (logged on source page): whether the log-linear law continues past 20k hr; the model size (paper doesn't state EgoScale's params); the in-the-wild dataset composition (likely Ego4D + EPIC-KITCHENS but not transcribed); the EgoDex license/availability; a Chinchilla-style data-vs-compute optimal sweep for VLAs is the natural next paper.

## [2026-05-15] ingest | DreamDojo — A Generalist Robot World Model from Large-Scale Human Videos (NVIDIA GEAR, ICML 2026 Spotlight)
- User dropped `raw/2602.06949v1.pdf` (Gao, Liang et al., 28 co-authors across NVIDIA + 8 universities, arXiv 2602.06949v1, 33 pages, Feb 2026) and asked to ingest. Project leads (‡): [Yuke Zhu](entities/yuke-zhu.md), [Joel Jang](entities/joel-jang.md), [Jim Fan (Linxi Fan)](entities/jim-fan.md). Notable academic co-authors: Pieter Abbeel (Berkeley), Jitendra Malik (Berkeley), Ming-Yu Liu (NVIDIA generative AI).
- Created [DreamDojo Paper](sources/dreamdojo-paper.md) — the **destination paper of NVIDIA GEAR's Dream\* triplet** (DreamGen → DreamZero → DreamDojo). Foundation **generative-video world model** trained on **44,711 hours of egocentric human video** (DreamDojo-HV) — the **largest WM-pretraining corpus to date**, 15× longer than prior, 96× more skills, 2,000× more scenes.
- **Two technical contributions**:
  - **Continuous latent actions** (VAE with information bottleneck on `(f_t, f_{t+1})` pairs, 700M-param spatiotemporal Transformer, 32-dim latent) as a self-supervised proxy for unlabeled human videos. Table 2 result: latent-action conditioning **matches** ideal ground-truth-action conditioning, vindicating the proxy-label thesis.
  - **Self-Forcing distillation** (Huang et al. 2025) from a bidirectional 35-step diffusion teacher to a causal 4-step autoregressive student, hitting **10.81 FPS at 640×480** — enables live teleoperation, online MPC, and large-scale policy evaluation.
- **Architecture**: Built on [NVIDIA Cosmos](entities/nvidia-cosmos.md)-Predict2.5 (latent video diffusion + DiT + WAN2.2 tokenizer + flow matching). Two variants: 2B and 14B parameters, pretrained 140k steps on **256 NVIDIA H100 GPUs**. Adds two action-conditioning improvements (relative actions, chunked per-latent-frame injection) plus a new **temporal-consistency loss** (λ = 0.1).
- **Headline result**: Human preference Table 4 — DreamDojo-14B wins **72.5% physics correctness** and **65.5% action following** vs Cosmos-Predict2.5 on out-of-distribution evals. Data-scale ablation (Table 3) shows monotonic PSNR improvement across all four OOD benchmarks as the pretraining mixture grows (In-lab → +EgoDex → +DreamDojo-HV → 2B → 14B).
- **DreamDojo-HV vs EgoScale's corpus**: the 6,015-task / 43,237-object / 9,869-scene metadata matches EgoScale exactly. DreamDojo-HV is the larger (43,827 hr) superset of EgoScale's in-the-wild ~20k hr cut. EgoScale = VLA scaling-law analysis on the smaller cut; DreamDojo = WM training on the larger cut. Both Feb 2026 from GEAR, same project leads.
- **Big synthesis update**: [Generative-video vs JEPA world models](syntheses/world-models/generative-video-vs-jepa-world-models.md) rewritten with DreamDojo as the new high-water mark on the generative-video side. Added the "DreamDojo closes part of this gap" callout — latent-action conditioning gives generative video the action-free → action-conditioned staging that previously only JEPA's V-JEPA-2-AC had. Open question still: V-JEPA-2-AC's zero-shot-on-new-Franka transfer result has no DreamDojo equivalent (the paper only demonstrates policy *evaluation*, not policy *deployment*).
- Created [Joel Jang](entities/joel-jang.md) — third project lead on DreamDojo (stub).
- Created [Fourier GR-1](entities/fourier-gr-1.md) — Fourier Intelligence humanoid; primary OOD eval target for all four DreamDojo benchmarks (stub).
- Updated [NVIDIA Cosmos](entities/nvidia-cosmos.md) — added Cosmos-Predict2.5 reference + DreamDojo as the canonical robot-specific downstream; sources 7 → 8.
- Updated [World model](concepts/world-models/world-model.md) — added DreamDojo to the generative-video paradigm row in "Major design points"; sources 16 → 17.
- Updated [NVIDIA GEAR](entities/nvidia-gear.md), [Jim Fan](entities/jim-fan.md), [Yuke Zhu](entities/yuke-zhu.md), [NVIDIA](entities/nvidia.md), [NVIDIA GR00T](entities/nvidia-groot.md), [EgoDex](entities/egodex.md), [AGIBOT](entities/agibot.md) — added DreamDojo references + bumped source counts.
- Updated [NVIDIA GEAR Lab — Publications](sources/nvidia-gear-publications.md) — marked entry #1 (DreamDojo) as ingested.
- Updated [index.md](index.md) — added DreamDojo source, Fourier GR-1 entity, Joel Jang entity, plus synced source counts on touched pages.
- **Open follow-ups**:
  - **DreamGen + DreamZero** are still uningested. With DreamDojo filed, the Dream\* triplet is two-thirds done; the other two would let us trace the line's progression.
  - **Cosmos-Predict2.5 primary source**: Ali et al. 2025 is cited but not in `raw/`. If the wiki picks up the Cosmos line, this is the architectural reference.
  - **Self-Forcing paper** (Huang et al. 2025): the distillation paradigm DreamDojo uses. Candidate ingest for the WM-distillation thread.
  - **Continuous latent actions**: Gao et al. 2025 (LAPA) is the cited primary source. Worth a `concepts/latent-action-models.md` page if this pattern shows up in more WMs or VLAs.
  - **YAM robot**: in-house NVIDIA embodiment in DreamDojo's latent-action training. Identity not surfaced; open mystery for the wiki.

## [2026-05-15] ingest | The Welch Labs Illustrated Guide to AI, Volume I (Stephen Welch, Feb 2026)
- User asked to ingest `raw/WelchLabs_IllustratedGuideToAI_rev_15_feb_4_1.pdf` after noting it had been sitting in `raw/` since May 11 uningested. 376-page Adobe-InDesign-produced textbook (Rev V15, PDF date 2026-02-04). Author: Stephen Welch, Winston-Salem NC. Companion code at github.com/stephencwelch/ai_book; each chapter pairs with a Welch Labs YouTube video.
- Created [Welch Labs Illustrated Guide to AI, Vol I](sources/welchlabs-illustrated-guide-to-ai.md) — section-summary-depth ingest. The 9-chapter sweep: perceptron → gradient descent → backprop → deep learning → AlexNet → neural scaling laws (Kaplan 2020) → mechanistic interpretability (Anthropic/Olah/Templeton 2024 SAEs) → attention (DeepSeek-V2 Multi-Head Latent Attention deep-dive) → diffusion. Vol II is teased.
- **Closes three pedagogy primary-source gaps the wiki had**: (a) **LLM-side scaling laws** — Welch Ch 6 walks through Kaplan 2020 with fitted slopes; before this the wiki cited "Hoffmann/Chinchilla" without an ingested primary. (b) **Mechanistic interpretability** — Welch Ch 7 anchors on Anthropic's Templeton 2024 SAE work; the wiki had gestured at this via the Anthropic entity but no concept page. (c) **DeepSeek MLA** — Welch Ch 8 spends ~25 pages on Multi-Head Latent Attention; the wiki had no DeepSeek coverage at all.
- Created [Welch Labs](entities/welch-labs.md) — pedagogy company / brand entity. With three sources now (this book + two videos) it warrants its own entity. Promoted to one of the wiki's three canonical pedagogy publishers (Sutton & Barto / 3Blue1Brown / Welch Labs).
- Created [Stephen Welch](entities/stephen-welch.md) — author entity stub. 2014 startup-driven self-teaching → first YouTube series → 2024–2026 channel restart → book.
- Created [Mechanistic interpretability](concepts/safety/mechanistic-interpretability.md) — new concept hub seeded by Ch 7. Covers sparse autoencoders, feature steering, Olah's "1% extracted dark matter" framing, the canonical Claude "ask-it-to-forget" demonstration. Adjacent to [AI safety and alignment](concepts/safety/ai-safety-alignment.md) and [Chain of thought](concepts/learning/chain-of-thought.md).
- Updated [Anthropic](entities/anthropic.md) — added Mechanistic interpretability program section; sources 4 → 5.
- Updated [Scaling laws — VLAs and human data](concepts/learning/scaling-laws-vla.md) — added Welch Ch 6 as the LLM-side pedagogy companion; sources 1 → 2.
- Updated [Chain of thought](concepts/learning/chain-of-thought.md) — added Welch Ch 8 reference for the "MLA is motivated by R1's CoT-token volume" angle.
- Updated [Welch Labs Perceptron (video)](sources/welchlabs-perceptron.md) and [Welch Labs — LeCun's $1B Bet (video)](sources/welchlabs-lecun-1b-bet-against-llms.md) — cross-linked to the new book + author + brand entities. The perceptron video is Ch 1's companion; the LeCun-bet video is JEPA-side and likely belongs to Vol II.
- Updated [index.md](index.md) — added book to pedagogical sources section, Welch Labs entity under Companies, Stephen Welch under People, plus the new Mechanistic interpretability concept entry.
- **Open follow-ups** (flagged on the source page):
  - **Templeton et al. 2024 — *Scaling Monosemanticity*** (Anthropic) — the primary mech-interp paper Ch 7 anchors on. Candidate ingest.
  - **Kaplan et al. 2020 — *Scaling Laws for Neural Language Models*** (OpenAI) — the primary scaling-law paper Ch 6 anchors on. Candidate ingest; would also let the wiki's [scaling-laws-vla](concepts/learning/scaling-laws-vla.md) page cite specifics.
  - **Liu et al. 2024 — DeepSeek-V2 (Multi-Head Latent Attention)** — Ch 8's deep-dive subject. Candidate ingest + seeds an `entities/deepseek.md`.
  - **Olah, July 2024 — "Dark Matter of Interpretability"** — Welch quotes this. Likely Transformer Circuits Thread post.
  - **Hoffmann et al. 2022 — Chinchilla** — already flagged elsewhere; Welch Ch 6 may also reference.

## [2026-05-16] reorg | Subdirectory structure for concepts/ and syntheses/
- Grouped 22 concept pages into 6 subfolders: `learning/`, `world-models/`, `agents/`, `safety/`, `robotics/`, `bio/`.
- Grouped 41 synthesis pages into 8 subfolders: `curriculum/`, `platforms/`, `projects/`, `world-models/`, `simulators/`, `assistive/`, `agents/`, `rl/`.
- `git mv` preserves history. Rewrote 251 markdown files to update relative-path links across the wiki.
- Restructured [index.md](index.md) Concepts and Syntheses sections to mirror the new subfolder layout with H3 subheadings.
- Verification: every relative `.md` link in `wiki/` resolves to an existing file (script at `/tmp/check_links.py`).

## [2026-05-16] file | Jetson Orin Nano flash-to-NVMe howto
- Created [Jetson Orin Nano — flash Jetson OS to NVMe SSD howto](syntheses/projects/jetson-orin-nano-flash-howto.md) covering SDK Manager and CLI paths, recovery-mode setup, QSPI bootloader caveat, and microSD-then-migrate alternative.
- Source: operational knowledge (no source-doc citation).
- Linked to/from [ROSOrin Pro](entities/rosorin-pro.md) context as the closest carrier-board case in the wiki.

## [2026-05-16] ingest | NVIDIA Jetson documentation cluster (5 sources)
- Created sources:
  - [NVIDIA Jetson Orin Nano Dev Kit software setup](sources/nvidia-jetson-orin-nano-devkit-software-setup.md) — recovery-mode procedure, SDK Manager host requirements (Ubuntu 20.04 / 8 GB / 25 GB), component selection.
  - [Jetson Linux R36.5 update mechanism](sources/nvidia-jetson-linux-r36-5-update-mechanism.md) — apt point/minor update commands; 35.x→36.x reflash requirement; `nvidia-l4t-bootloader` QSPI handling.
  - [JetPack 6.2.2 release](sources/nvidia-jetpack-6-2-2-release.md) — Jetson Linux 36.5 + CUDA 12.6.10 + TensorRT 10.3 + VPI 3.2; first-party AprilTag detector + pose estimator; 5× PVA speedup; HSM boot-signing.
  - [JetPack docs index](sources/nvidia-jetpack-docs-index.md) — docs still pin 6.2.1, lags dev-site 6.2.2.
  - [Jetson Linux R36.5 release](sources/nvidia-jetson-linux-r36-5-release.md) — Ubuntu 22.04 + kernel 5.15 + UEFI + OP-TEE; all production Orin modules + Dev Kits.
- Created entities: [Jetson Orin Nano](entities/jetson-orin-nano.md), [JetPack](entities/jetpack.md), [Jetson Linux](entities/jetson-linux.md).
- Updated:
  - [Jetson Orin Nano flash howto](syntheses/projects/jetson-orin-nano-flash-howto.md) — citations added; new "Updating an existing install" apt section; clarified Ubuntu 20.04 as the documented host.
  - [AprilTags](concepts/robotics/apriltags.md) — added JetPack 6.2.2 first-party VPI detector subsection; cross-linked Jetson Orin Nano.
  - [NVIDIA](entities/nvidia.md) — added Jetson product line + edge-AI stack to the company entity; added five new sources to "Mentioned in."
  - [ROSOrin Pro](entities/rosorin-pro.md) — replaced bare-text "Jetson Orin Nano" with link to the new entity.
- Open follow-ups: VPI AprilTag tag-family / accuracy ingest; Jetson Orin Nano datasheet ingest for TOPS / GPU clock / memory bandwidth; Installation-and-Setup chapter ingest for canonical NVMe-boot procedure.

## [2026-05-16] ingest | Jetson Linux R36.5 Release Notes (PDF)
- Downloaded `raw/jetson-linux-r36.5-release-notes.pdf` (17 pages, RN_10698-r36.5.0, Feb 2026 document revision).
- Created [Jetson Linux R36.5 release notes (PDF)](sources/nvidia-jetson-linux-r36-5-release-notes.md). Substantive content beyond the landing page: full flash-config-to-module-SKU mapping; Super Mode envelopes (25W Orin Nano / 40W Orin NX / MAXN); host OS officially **20.04 OR 22.04** (broadens user-guide chapter's 20.04-only); Bootlin GCC 11.3 toolchain; multi-boot-media version-match warning; documented known + fixed issues (initrd-flash near-completion failure FIXED, UEFI assertion FIXED, CUDA-memory regression after 6.4.4→6.4.7 FIXED, GStreamer h264parse missing on Ubuntu 22.04 desktop images); UEFI source on GitHub; plugin manager retired in favour of DTBOs.
- Updated:
  - [Jetson Linux](entities/jetson-linux.md) — added GCC 11.3, release tag, multi-boot-media warning callout, flash-config table, plugin-manager-retired note; bumped sources to 4.
  - [Jetson Orin Nano](entities/jetson-orin-nano.md) — added module part numbers (P3767-0003/-0004/-0005 + Orin NX SKUs on the P3768-0000 carrier) and a new Power Modes section covering Super Mode; bumped sources to 7.
  - [Jetson Orin Nano flash howto](syntheses/projects/jetson-orin-nano-flash-howto.md) — corrected host-OS line (20.04 or 22.04 per release notes); added Super Mode option; added multi-boot-media warning; added fixed-in-R36.5 callout for the prior `l4t_initrd_flash.sh` failure.
- New open question: what exactly is **Super Mode** under the hood (power-management policy, clock changes, thermal envelopes)? Needs *Supported Modes and Power Efficiency* chapter of the Developer Guide.

## [2026-05-16] ingest | Jetson Platform Power and Performance — Orin series (Developer Guide)
- Created [Platform Power and Performance — Orin series](sources/nvidia-jetson-platform-power-performance-orin.md). Resolves the Super Mode open question from the prior ingest. Substance: Super Mode = MAXN_SUPER (experimental, hardware-locked at flash time); per-module nvpmodel tables for all six Orin SKUs (Orin Nano 4GB/8GB, Orin NX 8GB/16GB, AGX Orin 32GB/64GB); runtime switching via `sudo nvpmodel -m <id>` (persistent across reboots/SC7); OC3 87.5% throttle; `-super-maxn` flash variant for sustained MAXN_SUPER workloads.
- Updated:
  - [Jetson Orin Nano](entities/jetson-orin-nano.md) — replaced the brief Power Modes section with full 8GB module nvpmodel table; added third flash variant (`-super-maxn`); documented hardware-lock-in; added runtime switching section; bumped sources to 8.
  - [Jetson Linux](entities/jetson-linux.md) — flash-config table grew to include the `-super-maxn` variant; bumped sources to 5.
  - [Jetson Orin Nano flash howto](syntheses/projects/jetson-orin-nano-flash-howto.md) — added "After flashing — switching power modes" section with nvpmodel commands and mode-ID-is-not-portable caveat; gotchas paragraph updated with `-super-maxn` and the hardware-lock-in warning.
- Headline 8GB number: Super 25W vs default 15W gives **+47% GPU clock, +50% memory clock**; full peak (1728 MHz CPU / 1020 MHz GPU) only at MAXN_SUPER.
- New open questions: TOPS-per-mode breakdown (not in this chapter); Orin NX `-super` flash config variant (page implies one exists separate from the Orin Nano carrier config); when `tpc_pg_mask` change forces a reboot.

## [2026-05-16] lint | Post-Jetson-cluster health check
- Ran `/tmp/lint_wiki.py` across 356 markdown pages. Clean: **0 broken links**, **0 orphan pages**, **0 sparse pages** (every non-source page has at least 2 outbound `.md` links).
- Found **14 entity/concept pages** with `sources: N` frontmatter drift of |diff| ≥ 2 between the claimed count and the actual number of source pages with markdown links to them.
- Fixed:
  - Added missing entity backlinks from three pre-existing source pages that mention Jetson Orin Nano in body but weren't linked: [Hiwonder ROSOrin docs](sources/hiwonder-rosorin-docs.md), [Hiwonder ROSOrin Pro user manual](sources/hiwonder-rosorin-pro-user-manual.md), [R36.5 update mechanism](sources/nvidia-jetson-linux-r36-5-update-mechanism.md).
  - Brought 13 remaining drifted `sources: N` values into agreement with the script-measured count. Definition of `sources:` is now mechanically consistent — "number of source-page markdown links to this page." Pages affected: nvidia (19→26), pointmaze (3→0), amal-nanavati (4→1), the-robot-studio (3→1), metaworld (3→1), tri (4→2), jetpack (4→6), nvidia-cosmos (8→10), jetson-linux (5→7), genie-envisioner (5→7), dm-control (4→2), scaling-laws-vla (2→4), imitation-learning (23→25).
- Caveat: entities with `sources: 0` after the fix (pointmaze) are mentioned in source body text but not linked — worth adding backlinks in a future pass if those entities matter for navigation.

## [2026-05-16] ingest | 5-paper foundational cluster — DROID, Metaworld, DINOv2, Dobb·E, VQ-BeT
- Created primary-source pages for 5 foundational works whose entity pages already existed but had no source backing:
  - [DROID Paper](sources/droid-paper.md) — Khazatsky, Pertsch, Finn, Levine, +97 (2024-04). 76k traj / 350 hr / 564 scenes / 84 tasks / standardized Franka / CC BY 4.0.
  - [Metaworld Paper](sources/metaworld-paper.md) — Yu, Quillen, ..., Hausman, Finn, Levine (CoRL 2019). 50-task benchmark; the headline 2019 result is that SOTA meta-/multi-task RL fails at just 10 tasks.
  - [DINOv2 Paper](sources/dinov2-paper.md) — Oquab et al. (Meta FAIR, 2023, 26 authors). LVD-142M curated dataset; ViT-1B teacher distilled to ViT-S/B/L/g; surpasses OpenCLIP.
  - [Dobb·E Paper](sources/dobb-e-paper.md) — Shafiullah et al. (NYU, 2023-11). 81% success / 109 tasks / 10 homes / 5-min-demo + 15-min-adaptation. **arxiv ID corrected**: 2306.16650 (entity's prior value) → 2311.16098 (verified-fetch).
  - [VQ-BeT Paper](sources/vq-bet-paper.md) — Lee et al. (ICML 2024). Hierarchical VQ codebook replaces BET's k-means; ~5× faster inference than Diffusion Policy across 7 environments.
- Updated each of the five matching entity pages: [DROID](entities/droid.md), [Metaworld](entities/metaworld.md), [DINOv2](entities/dinov2.md), [Dobb·E](entities/dobb-e.md) (arxiv ID + un-stubbed), [VQ-BeT](entities/vq-bet.md) (un-stubbed). Bumped sources counts and added to Mentioned-in. Dobb·E paper also confirmed CC-BY-4.0; DROID confirmed CC BY 4.0.
- Updated [index.md](index.md): added 5 sources in chronological order; struck the corresponding "Known gaps / TBD" entry that called out exactly this cluster.
- All five ingests are at the **abstract level** — paper bodies hold the architectural specifics (HPR encoder details, VQ-BeT codebook size, DINOv2 LVD-142M curation pipeline, Metaworld task list, DROID hardware spec) and would be worth pulling if any of those become load-bearing for downstream wiki claims.

## [2026-05-28] ingest | LeRobot ICLR 2026 paper (Cadene et al., 17 HF authors)
- Created [LeRobot ICLR 2026 paper](sources/lerobot-iclr-2026-paper.md) from `raw/2602.22818v1.pdf` — the canonical academic reference for the [LeRobot](entities/lerobot.md) framework. arxiv 2602.22818, Feb 26 2026, ICLR 2026 conference paper, 20 pages + appendices.
- Substance: 4-pillar architecture (unified middleware / `LeRobotDataset` format / async producer-consumer inference / PyTorch reference algos); 8 supported platforms (SO-100/101, Koch-v1.1, ALOHA-2, HopeJR-Arm, LeKiwi, Stretch-3, Reachy-2 — went from 3 to 8 in 2025); 16K+ datasets from 2.2K+ contributors as of Sep 2025; reference algos cover RL (HIL-SERL, TD-MPC), single-task BC (ACT, Diffusion Policy, VQ-BET), multi-task VLA (π0, SmolVLA); native LIBERO + Metaworld eval.
- Notable benchmarks: compute-footprint tables (ACT 52M / 5 ms RTX 4090 → π0 3.5B / 13.32 GB A100, CPU-incompatible); SmolVLA is the only frontier VLA that runs on CPU. Async vs sync on SmolVLA + SO-100 (Table 5): similar success (78.3% → 73.3%) but **doubles throughput** in fixed time (1.8 → 3.8 cubes/60s).
- Resolved open question on HopeJR-Arm: Appendix A confirms it's a TheRobotStudio design (cited as "TheRobotStudio, 2025"). Rewrote [HopeJR-Arm](entities/hope-jr-arm.md) accordingly — no longer a stub.
- Updated [LeRobot](entities/lerobot.md) substantially — added official platform table with prices, algorithm coverage table, dataset stats, inference-stack architecture, and compute-footprint table. The ICLR 2026 paper is now flagged as the canonical academic reference (the existing [robot-learning tutorial](sources/lerobot-robot-learning-tutorial.md) remains the recommended onboarding read).
- Updated entity pages (added ICLR 2026 source link + integration context): [SO-ARM101](entities/so-arm101.md), [LeKiwi](entities/lekiwi.md), [Reachy 2](entities/reachy.md), [Stretch](entities/stretch.md), [ALOHA](entities/aloha.md), [The Robot Studio](entities/the-robot-studio.md) (now lists both SO-ARM and HopeJR designs), [Hugging Face](entities/hugging-face.md), [Remi Cadene](entities/remi-cadene.md) (now flagged as ICLR 2026 lead author), [ACT](entities/act.md), [Diffusion Policy](entities/diffusion-policy.md), [VQ-BeT](entities/vq-bet.md), [TD-MPC](entities/td-mpc.md), [SmolVLA](entities/smolvla.md), [π0](entities/pi-zero.md), [LIBERO](entities/libero.md), [Metaworld](entities/metaworld.md).
- Updated [index.md](index.md): added source in chronological order; bumped source counts on the ~15 updated entities.
- Open questions surfaced: (1) quantization / graph compilation roadmap for π0 onboard deployment (Limitation #3); (2) no world-model methods in LeRobot's algorithm coverage (Dreamer, V-JEPA-2 absent — coverage roadmap or deliberate scope?); (3) tabletop bimanual cost gap (€550 SO-100 vs €21k ALOHA-2 is ~40× — does HopeJR-Arm fill that gap, or is a middle tier planned?).
- Cross-source confirmation: the SO-10X "50%+ of community datasets" claim corroborates the [LeRobot Worldwide Hackathon 2025](sources/lerobot-worldwide-hackathon-2025-winners.md) signal that community contribution flows to the cheapest hardware. Async-inference results also reproduce the [SmolVLA paper](sources/smolvla-paper.md)'s own throughput numbers in a controlled SO-100 benchmark.
- Triage of other raw/ PDFs (May 25–28): `2403.14606v3.pdf` (Blondel-Roulet diff prog) already ingested as [blondel-roulet-differentiable-programming](sources/blondel-roulet-differentiable-programming.md); `2506.01844v1.pdf` (SmolVLA) already ingested as [smolvla-paper](sources/smolvla-paper.md); `7271_What_Drives_Success_in_Ph.pdf` (Terver JEPA-WMs TMLR) already ingested as [jepa-wms-paper](sources/jepa-wms-paper.md). LeRobot ICLR was the only new PDF.

## [2026-05-28] query | "How to adapt LeRobot to ROSOrin Pro for in-home floor-pickup-and-tidy?"
- Synthesized from [LeRobot ICLR 2026 paper](sources/lerobot-iclr-2026-paper.md), [LeRobot entity](entities/lerobot.md), [ROSOrin Pro](entities/rosorin-pro.md), [ROSOrin Pro 6-DOF arm](entities/rosorin-pro-arm.md), [OpenClaw](entities/openclaw.md), [Hiwonder OpenClaw tutorial](sources/hiwonder-openclaw-tutorial.md), [Robot Utility Models](entities/robot-utility-models.md), [Dobb·E](entities/dobb-e.md), [stretch_ai](entities/stretch-ai.md).
- Filed as [LeRobot on ROSOrin Pro — adaptation plan for in-home floor-pickup-and-tidy](syntheses/projects/lerobot-on-rosorin-pro.md). Three gaps surfaced (motor SDK lineage HX-12H ≠ FeeTech/Dynamixel; Aurora930 12 fps vs LeRobot 30 Hz default; Orin Nano compute budget — π0 won't fit, ACT is real-time, SmolVLA needs async stack). Recommended 4-step ladder ending in SO-100 leader + SmolVLA via async inference; recommended architecture keeps OpenClaw as the LLM orchestrator and replaces the deterministic `/start_pick` skill with a LeRobot-trained policy (same composition pattern as [stretch_ai](entities/stretch-ai.md) on Stretch).
- Updated [index.md](index.md) Projects section.

## [2026-05-28] ingest | Rosetta — LeRobot for ROS2 Robots (iblnkn/rosetta GitHub)
- Created [Rosetta GitHub](sources/rosetta-github.md) — solo-author Apache-2.0 framework "LeRobot for ROS2 Robots" (76 stars / 14 forks / last push 2026-05-24; created Sep 14 2025). Python 99.4%.
- Created [Rosetta entity](entities/rosetta.md) — software-framework subtype; classified as a downstream community accelerator for [LeRobot](entities/lerobot.md).
- Substance: YAML-contract approach maps ROS 2 topics (`/joint_states`, `JointState`, `Imu`, `Odometry`, `TwistStamped`, compressed images) to LeRobot's flat dot-separated data model (`observation.state`, `observation.images.<name>`, `action`). Per-topic QoS / alignment / unit conversion / safety behavior are all declarative. 5-step pipeline: Define → Record (MCAP) → Convert (LeRobotDataset Parquet) → Train (`lerobot-train`) → Deploy (`rosetta_client_node` exposes ROS 2 lifecycle actions). 5 packages including `rosetta_rl` ("coming soon"). Reference contracts shipped: SO-101 (multi-cam manipulator), SO-101 HIL (+ intervention buttons + reward topic), TurtleBot3 (wheeled mobile base with 20-dim state from wheel JointState + IMU + Odometry). Supports a superset of upstream LeRobot's policy menu — adds π0.5, GR00T, Wall-X, X-VLA on top of ACT/DP/VQ-BET/HIL-SERL/TD-MPC/π0/SmolVLA.
- **Major synthesis update**: [LeRobot on ROSOrin Pro](syntheses/projects/lerobot-on-rosorin-pro.md) — added a Rosetta callout at top and rewrote the recommended ladder. Step 1 ("port LeRobot to ROSOrin Pro") goes from "1–2 weeks writing a `lerobot.robots.rosorin_pro` Python class wrapping `~/arm_group_control`" to "**1 day** writing a Rosetta YAML contract combining the SO-101 and TurtleBot3 templates." This is the kind of community-acceleration result the [LeRobot ICLR 2026 paper](sources/lerobot-iclr-2026-paper.md) Limitation #2 explicitly invites.
- Updated entities: [LeRobot](entities/lerobot.md) (added Rosetta to "Downstream / hardware-ecosystem projects" section; 9→10 sources), [SO-ARM101](entities/so-arm101.md) (6→7 sources; reference manipulator contract), [TurtleBot](entities/turtlebot.md) (2→3 sources; reference mobile-base contract), [ROSOrin Pro](entities/rosorin-pro.md) (added LeRobot-integration-path section pointing to Rosetta).
- Updated [index.md](index.md): added Rosetta to chronological sources + Software stacks section; bumped LeRobot / SO-ARM101 / TurtleBot index entries.
- Open questions surfaced: Rosetta's production maturity (76 stars / solo author / 8 months old — moderate risk); whether **Wall-X** and **X-VLA** (both Rosetta-supported but not in wiki) deserve their own entity pages; relationship between Rosetta and upstream HF LeRobot team (any upstreaming conversation?); distribution channel (PyPI vs source).

## [2026-05-28] ingest | 3-source LeRobot↔ROS 2 bridge landscape — lerobot-ros, so101_ros2, ROS 2 Humble docs
- Created 3 source pages: [lerobot-ros GitHub](sources/lerobot-ros-github.md) (`ycheng517/lerobot-ros`, 194 stars), [so101_ros2 readthedocs](sources/so101-ros2-readthedocs.md) (`nimiCurtis/so101_ros2`, 50 stars), [ROS 2 Humble docs](sources/ros2-humble-docs.md).
- Created 3 entity pages: [lerobot-ros](entities/lerobot-ros.md), [so101-ros2](entities/so101-ros2.md), [ROS 2](entities/ros2.md). The ROS 2 entity is **overdue** — 20+ existing entities mention ROS 2 but none was an entity page until now.
- **Three-bridge comparison surfaced**: this is now the complete LeRobot↔ROS 2 landscape in the wiki —

  | Bridge | Approach | Hardware | ROS 2 distro | Stars | License |
  |---|---|---|---|---|---|
  | [Rosetta](entities/rosetta.md) | YAML contract | any ROS 2 robot | distro-agnostic | 76 | Apache-2.0 |
  | [lerobot-ros](entities/lerobot-ros.md) | Python sub-class | any ros2_control / MoveIt arm | **Jazzy only** | **194** | not specified |
  | [so101-ros2](entities/so101-ros2.md) | SO-101 workspace | **SO-101 only** | **Humble only** | 50 | MIT |

  Selection axes: (1) hardware (mobile bases need Rosetta — only one with a TurtleBot3 contract); (2) ROS 2 distribution (Humble vs Jazzy is operationally load-bearing); (3) operational footprint (lerobot-ros minimal, so101_ros2 heavy — needs author's LeRobot fork).
- ROS 2 release timeline captured: **Lyrical Luth** (May 22 2026, newest), **Kilted Kaiju** (May 2025, non-LTS), **Jazzy Jalisco** (May 2024, LTS, EOL May 2029), **Humble Hawksbill** (May 2022, LTS, EOL May 2027). New distro every May 23rd (World Turtle Day). Cross-distro communication "not guaranteed."
- **Synthesis update**: [LeRobot on ROSOrin Pro](syntheses/projects/lerobot-on-rosorin-pro.md) revised callout now compares all 3 bridges; **Rosetta confirmed as the right choice for ROSOrin Pro** because ROSOrin Pro is Humble (rules out lerobot-ros) and not SO-101 (rules out so101_ros2), and only Rosetta has mobile-base support.
- Updated entities: [LeRobot](entities/lerobot.md) (added 3-bridge table; sources 10→12), [Rosetta](entities/rosetta.md) (cross-linked siblings), [SO-ARM101](entities/so-arm101.md) (now the most-tooled platform in the LeRobot↔ROS 2 ecosystem; sources 7→9), [ROSOrin Pro](entities/rosorin-pro.md) (LeRobot integration path section now notes distro split).
- Updated [index.md](index.md): added 4 new sources (3 GitHub/docs + ROS 2 Humble); added 4 new entity entries (lerobot-ros, so101-ros2, ROS 2, plus LeRobot/SO-ARM101 source-count bumps).
- Open questions surfaced: ycheng517/lerobot-ros has **no license** (blocks redistribution); nimiCurtis/so101_ros2 depends on author's LeRobot **fork** rather than upstream (maintenance risk if upstream drifts); ROS 2 Lyrical Luth (May 2026) LTS status not yet confirmed publicly.

## [2026-05-28] lint | Post-bridge-cluster health check + 5 entity stubs created
- Ran fresh `/tmp/lint_wiki.py` across 433 wiki pages. Clean: **0 broken links** (4 flagged were false positives — links to `CLAUDE.md` / `README.md` at the repo root, outside `wiki/`), **0 orphans**, **45 source-count drift cases** (mostly positive — natural fan-out from recent multi-page ingests). Largest negative drift: `flow-matching` (claimed 7, measured 2) — 6 source pages mention the term in body but don't link to the concept; flagged as backlink opportunity.
- **Created 5 entity stubs** to fill the most-mentioned gaps:
  - **[FeeTech](entities/feetech.md)** + **[Dynamixel](entities/dynamixel.md)** — paired motor-SDK pages. Per [LeRobot ICLR 2026 paper §3.1](sources/lerobot-iclr-2026-paper.md), these are the **only two motor SDKs LeRobot's middleware natively integrates** — the gating constraint that determined the LeRobot↔ROS 2 bridge story. FeeTech (4 sources) is the low-cost / hobby tier (SO-100/101, LeKiwi STS3215, Stretch 4 tool bus); Dynamixel (4 sources) is the research / premium tier (Koch-v1.1, LeKiwi alt-config).
  - **[MoveIt](entities/moveit.md)** (4 sources) — PickNik-maintained ROS 2 motion-planning + kinematics stack. First-class control mode in [lerobot-ros](entities/lerobot-ros.md) (CARTESIAN_VELOCITY via MoveIt Servo).
  - **[Gazebo](entities/gazebo.md)** (6 sources) — canonical open-source ROS simulator from Open Robotics. Captures the confusing naming history (Gazebo 1–11 → Ignition → Gazebo Harmonic). Contrasted with [Isaac Sim](entities/nvidia-isaac-sim.md) (NVIDIA) and [MuJoCo](entities/mujoco.md) (DeepMind).
  - **[Nav2](entities/nav2.md)** (3 sources) — ROS 2 autonomous navigation stack. The "house navigation is solved" component referenced in the [LeRobot on ROSOrin Pro synthesis](syntheses/projects/lerobot-on-rosorin-pro.md). Composes with LeRobot policies (Nav2 = nav, LeRobot = visuomotor manipulation).
- Cross-linked the new entities into [LeRobot](entities/lerobot.md), [ROS 2](entities/ros2.md), [SO-ARM101](entities/so-arm101.md), [LeKiwi](entities/lekiwi.md), [lerobot-ros](entities/lerobot-ros.md), [so101-ros2](entities/so101-ros2.md). Added a new "Motor SDKs / hardware components" sub-section to [index.md](index.md) (was previously absent — motor SDKs were a category gap).
- **Did NOT** do the bookkeeping batch on the 45 source-count drift cases — user opted to do the entity stubs instead (per "Do 3. Then add MoveIt, Gazebo, Nav2."). Drift remains as a deferred TODO.
- **Did NOT** do the flow-matching backlink pass — same reason; deferred.
- Open questions surfaced by the new stubs: HX-12H ([ROSOrin Pro](entities/rosorin-pro.md)) is the third motor lineage not in LeRobot's SDK — deserves its own page; Koch-v1.1 is the largest gap in LeRobot's platform coverage with no entity yet (Dynamixel-based, ~€670, in [Table 1a](sources/lerobot-iclr-2026-paper.md)); PickNik Robotics and Open Navigation as organizations have no entity pages despite their stewardship roles.

## [2026-05-28] lint | Backlink + source-count cleanup pass — zero drift
- Added 18 markdown-link backlinks across 13 source pages to resolve the mention-without-link gaps surfaced by the prior lint:
  - **flow-matching** backlinks in `pi07-paper.md`, `pistar06-paper.md`, `egoscale-paper.md`, `dreamdojo-paper.md`, `blondel-roulet-differentiable-programming.md`, `lerobot-robot-learning-tutorial.md` (6 sources).
  - **FeeTech** backlinks in `hello-robot-stretch-4-datasheet.md`, `sigrobotics-uiuc-projects-page.md`.
  - **Dynamixel** backlinks in `lekiwi-github.md`, `sigrobotics-uiuc-projects-page.md`.
  - **MoveIt** backlinks in `elephant-robotics-mybuddy-280.md`, `nanavati2025-feeding-out-of-lab.md`.
  - **Gazebo** backlinks in `clearpath-turtlebot-4.md`, `hello-robot-stretch-docs.md`, `hiwonder-rosorin-docs.md`, `px4-docs-main.md`.
  - **Nav2** backlinks in `hello-robot-stretch-docs.md`, `hiwonder-rosorin-docs.md`, `hello-robot-stretch-4-launch.md`.
- Ran `/tmp/fix_source_counts.py` to bring **44 frontmatter `sources: N` fields into agreement** with the measured count of source-page markdown links. Biggest fixes: imitation-learning 29→37, droid 6→11, franka-panda 10→15, chelsea-finn 4→8, stretch 16→20. Definition is now mechanically consistent across the wiki: `sources:` = "number of source-page markdown links to this page" (matching the convention established in the 2026-05-16 lint pass).
- Lint result: **0 broken links, 0 orphans, 0 source-count drift cases** across 438 wiki pages. The only remaining mention-gap is **URDF** (9 source-page mentions, no entity) — left as deferred since URDF is a file format rather than an entity; could be a concept page if cross-linking becomes useful.

## [2026-05-28] ingest | Hermes Agent + Steinberger OpenClaw + NVIDIA NemoClaw (the "Claw" ecosystem)
- User asked to compare [OpenClaw](entities/openclaw.md) (Hiwonder's robot framework) with "Hermes" as agentic systems on a robot. First-pass disambiguation found Hermes = Nous Research **LLM family**. User clarified: meant **Hermes Agent** (Nous's agentic framework), with `nvidia.com/ai/nemoclaw` and `github.com/openclaw/openclaw` as additional context.
- Result: ingested **3 new sources + 3 new entities** covering the previously-uncaptured "Claw" ecosystem:
  - [NVIDIA RTX AI Garage post (Gore, 2026-05-13)](sources/nvidia-rtx-ai-garage-hermes-agent.md) → [Hermes Agent](entities/hermes-agent.md) entity. Nous Research's MIT-licensed self-improving agent framework; **171K stars**; pairs with Qwen 3.6 27B/35B on [DGX Spark](entities/dgx-spark.md); "most used agent in the world according to OpenRouter."
  - [Hermes Agent GitHub README](sources/hermes-agent-github.md) → architectural detail (7-layer Agent Core / Terminal Backends / Gateway / Skills / Tools / MCP / Memory; 6 terminal backends; 7+ messaging platforms; 200+ models). Critical finding: `hermes claw migrate` command refers to the Steinberger OpenClaw, **not** Hiwonder's.
  - [OpenClaw GitHub README (Steinberger)](sources/openclaw-github.md) → [OpenClaw (Steinberger personal AI)](entities/openclaw-personal-ai.md) entity. MIT TypeScript/Node 24 project; **375K stars / 78.3K forks**; "Molty space lobster" naming origin (with unmistakable Claude homophone); local-first personal AI assistant; 20+ messaging platforms; ClawHub skill registry.
  - [NVIDIA NemoClaw product page](sources/nvidia-nemoclaw-page.md) → [NemoClaw](entities/nemoclaw.md) entity. NVIDIA's early-preview privacy/security wrapper over Steinberger OpenClaw + NVIDIA Agent Toolkit + OpenShell (policy guardrails) + Nemotron LLM.
- **Critical wiki-coherence fix**: added prominent disambiguation banner + "See also" section to [OpenClaw (Hiwonder)](entities/openclaw.md) — there are now **3 entities sharing the "Claw" name**, all unrelated. Renamed the Hiwonder entity title to "OpenClaw (Hiwonder, robotics)" for index clarity. Steinberger OpenClaw owns the name globally (375K stars vs Hiwonder's localized educational-robot use).
- Open questions surfaced: Steinberger OpenClaw's 375K stars deserves independent verification; relationship between Nous Research's Hermes 4 LLM and Hermes Agent framework not yet captured; no robot integrations exist for any "Claw" / Hermes ecosystem project (would be MCP-server-shaped work); Peter Steinberger lacks an author entity despite being a load-bearing figure.

## [2026-05-28] correction | Hiwonder OpenClaw is a downstream of Steinberger OpenClaw (per user)
- User corrected the prior framing: [Hiwonder's OpenClaw](entities/openclaw.md) is not a name-collision but a **downstream robotics distribution built on the [Steinberger OpenClaw](entities/openclaw-personal-ai.md) upstream** (with ROS 2 + manipulation extensions added on top). All disambiguation banners across the wiki rewritten from "name collision" → "downstream / upstream lineage." Affected pages: [OpenClaw (Hiwonder)](entities/openclaw.md), [OpenClaw (Steinberger)](entities/openclaw-personal-ai.md), [Hermes Agent](entities/hermes-agent.md), [NemoClaw](entities/nemoclaw.md), [openclaw-github source](sources/openclaw-github.md), [hermes-agent-github source](sources/hermes-agent-github.md), [index.md](index.md).
- **Flagged as "per user; pending primary-source confirmation"** — neither the Hiwonder OpenClaw tutorial source nor the Steinberger OpenClaw README explicitly cite the lineage; needs a direct Hiwonder-OpenClaw acknowledgment or a fork/dependency reference to be wiki-canonical.
- Implication for the OpenClaw-vs-Hermes-Agent comparison answer: significantly **softens the case for ripping out Hiwonder OpenClaw** — since Hiwonder inherits the upstream's gateway + skill registry + extension system, the real choice is at the brain layer (Steinberger's default model vs Hermes Agent's self-improving loop) plus the robot-extensions layer (Hiwonder's hand-coded ROS 2 skills vs a hypothetical custom ros-mcp-server). The "stay in the OpenClaw family but write your own ROS-MCP extensions" path becomes more attractive than the "switch upstream to Hermes Agent" path.

## [2026-05-28] query | "Compare OpenClaw and Hermes as a robot's high-level thinker and planner"
- Synthesized from [OpenClaw (Hiwonder)](entities/openclaw.md), [OpenClaw (Steinberger)](entities/openclaw-personal-ai.md), [NemoClaw](entities/nemoclaw.md), [Hermes Agent](entities/hermes-agent.md), [Nous Research](entities/nous-research.md), [LeRobot on ROSOrin Pro synthesis](syntheses/projects/lerobot-on-rosorin-pro.md), [LLM-agent architecture concept](concepts/agents/llm-agent-architecture.md).
- Filed as [OpenClaw vs Hermes Agent as a robot's high-level thinker and planner](syntheses/agents/openclaw-vs-hermes-as-robot-brain.md). Frames the choice as **two independent layers** (brain LLM + agent loop) rather than one all-or-nothing framework switch — exploiting the Hiwonder-downstream-of-Steinberger lineage to recover three feasible paths (A: same loop, local brain; B: migrate to Hermes Agent + keep Hiwonder's ROS 2 skills via ros-mcp-server; C: full Hermes + ros-mcp-server + LeRobot rebuild). Recommendation: start with Path A.
- Updated [index.md](index.md) Agents-syntheses section.
- Accidentally committed `wiki/notes/rosorin-pro-setup.md` in commit `320e469` via `git add -A wiki` — violates the `wiki/notes/` user-owned read-only convention. Awaiting user direction on whether to untrack (preserves history) or rewrite history (force-push to main).

## [2026-05-28] correction | "Hiwonder OpenClaw" was a misframing — Hiwonder ships `openclaw_controller`, a ROS 2 bridge for upstream OpenClaw
- User clarified: there is no separate Hiwonder OpenClaw distribution. There's just one [OpenClaw](entities/openclaw.md) (Steinberger / community, `github.com/openclaw/openclaw`, MIT, 375K stars). Hiwonder's contribution is **`openclaw_controller`**, a ROS 2 module that interfaces upstream OpenClaw with the [ROSOrin Pro](entities/rosorin-pro.md). It's an extension that sits below OpenClaw, not a fork or downstream distribution.
- File renames: `wiki/entities/openclaw.md` ↔ `wiki/entities/openclaw-personal-ai.md` swapped via `git mv` so the canonical OpenClaw page now lives at `openclaw.md`. The old `openclaw.md` (then "Hiwonder OpenClaw") was renamed to [`openclaw-controller.md`](entities/openclaw-controller.md) and rewritten to describe the ROS 2 bridge module.
- Sweep across ~21 pages to remove "downstream distribution" / "Hiwonder OpenClaw" / "Steinberger OpenClaw disambiguator" framing and update links from `openclaw-personal-ai.md` → `openclaw.md`. Touched: [openclaw.md](entities/openclaw.md), [openclaw-controller.md](entities/openclaw-controller.md), [hiwonder.md](entities/hiwonder.md), [rosorin-pro.md](entities/rosorin-pro.md), [rosorin-pro-arm.md](entities/rosorin-pro-arm.md), [tonypi.md](entities/tonypi.md), [stretch-ai.md](entities/stretch-ai.md), [hermes-agent.md](entities/hermes-agent.md), [nemoclaw.md](entities/nemoclaw.md), [nous-research.md](entities/nous-research.md), [rosetta.md](entities/rosetta.md), [ros2.md](entities/ros2.md), [nav2.md](entities/nav2.md), [gemini-robotics.md](entities/gemini-robotics.md); sources [hiwonder-openclaw-tutorial.md](sources/hiwonder-openclaw-tutorial.md), [openclaw-github.md](sources/openclaw-github.md), [nvidia-nemoclaw-page.md](sources/nvidia-nemoclaw-page.md), [hermes-agent-github.md](sources/hermes-agent-github.md), [rosetta-github.md](sources/rosetta-github.md); concept [llm-agent-architecture.md](concepts/agents/llm-agent-architecture.md); syntheses [openclaw-vs-hermes-as-robot-brain.md](syntheses/agents/openclaw-vs-hermes-as-robot-brain.md), [llm-agent-architecture-across-stacks.md](syntheses/agents/llm-agent-architecture-across-stacks.md), [lerobot-on-rosorin-pro.md](syntheses/projects/lerobot-on-rosorin-pro.md), [rosorin-pro-lego-pick-place.md](syntheses/projects/rosorin-pro-lego-pick-place.md), [simulators-for-agentic-robotics-2026.md](syntheses/simulators/simulators-for-agentic-robotics-2026.md), [open-source-robot-ai-projects.md](syntheses/platforms/open-source-robot-ai-projects.md), [robot-platforms-comparison.md](syntheses/platforms/robot-platforms-comparison.md); plus [index.md](index.md) and [overview.md](overview.md).
- Implication for the prior 2026-05-28 OpenClaw-vs-Hermes synthesis: the two-layer reframing (brain + agent loop) is preserved, but the "Hiwonder ROS 2 extensions" layer is now correctly named as `openclaw_controller`, an extension below OpenClaw — not an inherited downstream skill set. Migration paths (`hermes claw migrate` → OpenClaw side; custom ros-mcp-server wrapping the same ROS 2 services `openclaw_controller` already exposes) are unchanged in shape, simpler in description.

## [2026-05-29] ingest | A Collectivist, Economic Perspective on AI (Michael I. Jordan, 2025)
- Created [Jordan — Collectivist, Economic Perspective on AI](sources/jordan-collectivist-economic-ai.md) (arXiv 2507.06268v3, cs.CY)
- **Opened a new economics-of-ML wing** — first source outside the robotics spine; no robotics content
- New concept folder `concepts/economics/`: [Three thinking styles](concepts/economics/three-thinking-styles.md), [Collectivist AI / AI-as-market](concepts/economics/collectivist-ai.md), [Mechanism design & statistical contract theory](concepts/economics/mechanism-design.md), [Prediction-powered inference](concepts/economics/prediction-powered-inference.md)
- New entities: [Michael I. Jordan](entities/michael-i-jordan.md), [UnitedMasters](entities/unitedmasters.md)
- New synthesis folder `syntheses/society/`: [Three critiques of the LLM-as-intelligence North Star](syntheses/society/critiques-of-the-intelligence-north-star.md) (LeCun vs Jordan vs Constitution)
- Cross-linked into [AI safety and alignment](concepts/safety/ai-safety-alignment.md) (alignment-as-tradeoff counterpoint; bumped 5→6 sources) and [Are We Building Skynet?](sources/medium-are-we-building-skynet.md) (See also)
- Updated [index.md](index.md): new source, +2 entities, new Concepts ### Economics + Syntheses ### Society sections
- Updated [CLAUDE.md](../CLAUDE.md) structure tree: registered `concepts/economics/` + `syntheses/society/`

## [2026-05-30] query | "What cameras for XLeRobot in low-light + clutter? (e.g. RealSense D435i)"
- Filed [XLeRobot camera options for low-light + clutter](syntheses/projects/xlerobot-camera-options-low-light.md)
- Recommendation: swap stock RealSense D415 → **D435i** (global shutter, wider FOV, IMU, same mount footprint); optional D405 at wrist for close-range manipulation
- Key caveat surfaced: active IR stereo gives depth-in-the-dark + works on clutter/textureless surfaces, but RGB stream stays dark/noisy → LeRobot policies are RGB-driven, so add illumination
- Ruled out: D455 (too wide for mount, long-range wasted), D405 for nav (no IR projector → bad in low light)
- Updated [XLeRobot](entities/xlerobot.md) (optional-sensors line + D435i pointer; bumped updated date) and [index.md](index.md)

## [2026-05-30] verify | D435i mount fit vs stock XLeRobot D415 shell
- Verified: D415 (99×20×23 mm) and D435i (90×25×25 mm) do NOT share a housing — differ on all 3 axes
- XLeRobot head-camera mount is a press-fit *shell* keyed to the body → stock D415 shell will NOT fit D435i as-printed
- Fix is trivial: shared D400-series rear mount (2× M3, 45 mm apart + ¼-20); docs say "use any head camera... little modification to the last mounting link" + ship STEP files
- Corrected prior wrong "same housing footprint" claim in [synthesis](syntheses/projects/xlerobot-camera-options-low-light.md), [XLeRobot entity](entities/xlerobot.md), [index.md](index.md)

## [2026-05-30] build | XLeRobot → D435i printable mounting bracket
- Created `hardware/xlerobot-d435i-bracket/` (d435i_bracket.stl + .scad + preview.png + README)
- Parametric L-bracket bolting to the D435i 45 mm M3 front pattern; foot cantilevers over camera top to the robot link
- Caveats documented: `cam_m3_z` (M3 vertical position) not in Intel datasheet → caliper-confirm; robot-side hole pattern is a placeholder
- Linked from [synthesis](syntheses/projects/xlerobot-camera-options-low-light.md) (new "Printable mount" section)

## [2026-05-30] ingest | In-vault Obsidian stub for the D435i bracket
- Created [bracket pointer page](syntheses/projects/xlerobot-d435i-bracket.md) + copied preview.png into the vault (Obsidian can't follow links out to sibling `hardware/`)
- Linked it from the [camera-options synthesis](syntheses/projects/xlerobot-camera-options-low-light.md) and [index.md](index.md)

## [2026-05-30] query | "Is a 300W battery enough for XLeRobot + AGX Thor + motors/arms?"
- Filed [XLeRobot + AGX Thor power budget](syntheses/projects/xlerobot-thor-power-budget.md)
- Conclusion: 300 W *rate* is fine (600 W surge covers peaks); real constraints are (1) output-port wiring — 12 V motors + 28 V/PD Thor, no single C300 port serves both — and (2) capacity: 288 Wh → ~1.5–2.5 hr with a Thor (vs stock 10+ hr). Recommend more Wh (not W) + DC-native pack.
- Folded verified specs into entities: [XLeRobot](entities/xlerobot.md) (C300 600 W surge + per-port caps + STS3215 currents 30 mA/180 mA/2.7 A) and [Jetson Thor](entities/jetson-thor.md) (dev kit 28 V/5 A 140 W ADP-240LB, 9–28 V input, ~168 W cap)
- Updated [index.md](index.md); bumped Jetson Thor updated date

## [2026-05-30] query | "Recommended battery power supplies for Jetson Thor (web + NVIDIA forums)"
- Folded forum findings into [XLeRobot + Thor power budget](syntheses/projects/xlerobot-thor-power-budget.md): new "What NVIDIA and the forums recommend" section + 28 V-ceiling battery-chemistry cheat-sheet
- Key facts: NVIDIA says dev kit must use bundled PSU (battery = off-label); input 9–28 V / 8 A via Molex Micro-Fit 3.0 J83; community uses 9–28 V Li-ion/LiFePO4 packs ~2 hr; 2× 12 V SLA→24 V/550 Wh datapoint corroborates runtime
- Added Micro-Fit connector part `2147561041` (2×2 male, needs female mate) + 8 A figure to [Jetson Thor](entities/jetson-thor.md)

## [2026-05-31] ingest | Welch Labs — "Yann LeCun's $1B Bet Against LLMs [Part 2]"
- Source: YouTube v_jDvpEGTIg (Welch Labs, 2026-05-30, 40:57). Transcript saved to raw/2026-05-30-welchlabs-lecun-1b-bet-against-llms-part2.txt (yt-dlp auto-captions, deduped)
- Created [source page](sources/welchlabs-lecun-1b-bet-against-llms-part2.md) and new entity [VL-JEPA](entities/vl-jepa.md) (Meta/LeCun, Chen et al., arXiv 2512.10942)
- **Name-collision flagged**: VL-JEPA (Meta, vision-language) ≠ [VLA-JEPA](entities/vla-jepa.md) (USTC, VLA + latent WM) — disambiguation callouts added to both
- **Partially answers an open question**: hierarchical-JEPA push-t result (horizon 5→15) updated on [Yann LeCun](entities/yann-lecun.md) H-JEPA TBD + added to [JEPA concept](concepts/world-models/jepa.md) (new H-JEPA section)
- Updated: [LeWorldModel](entities/leworldmodel.md) (CEM planning recipe + ~5-loop horizon + hierarchical note), [VLA models](concepts/learning/vla-models.md) (LeCun "VLA are doomed" critique callout), [AMI Labs](entities/ami-labs.md) (tagline + near-term industrial plan), [Welch Labs](entities/welch-labs.md) (Part 2 in series), [V-JEPA 2](entities/v-jepa-2.md), Part 1 source (sequel link)
- Updated [index.md](index.md): new source + new VL-JEPA entity

## [2026-05-31] ingest | HWM — "Hierarchical Planning with Latent World Models" (arXiv 2604.03208)
- Follow-up to the Part 2 video ingest: located + ingested the paper behind the hierarchical-JEPA push-t claim. PDF → raw/2026-04-hierarchical-planning-latent-world-models-2604.03208.pdf
- Authors incl. LeCun + Ballas (joint advising), Terver, Bardes, Balestriero (the video's credited collaborator) — confirms attribution
- Created [source page](sources/hwm-paper.md) + entity [HWM](entities/hwm.md)
- **Resolved the wiki's long-standing H-JEPA open question** on [Yann LeCun](entities/yann-lecun.md); updated [JEPA concept](concepts/world-models/jepa.md) H-JEPA section with the named paper + real numbers
- **Corrected the video's "push-t 5→15 steps"** everywhere: real framing is task horizon d=25→75, success 17%→61% (DINO-WM base); Franka 0%→70% (V-JEPA2-AC); Maze +39% (PLDM); 3–4× less planning compute
- Fixed [LeWorldModel](entities/leworldmodel.md) attribution (HWM push-t base is DINO-WM, not LeWM — LeWM was the single-level demo)
- Cross-linked base models [DINO-WM](entities/dino-wm.md), [PLDM](entities/pldm.md), [V-JEPA 2](entities/v-jepa-2.md); updated [index.md](index.md)

## [2026-05-31] ingest | NVIDIA Jetson AGX Thor Dev Kit — Hardware Layout (User Guide)
- Created [source page](sources/nvidia-jetson-agx-thor-devkit-hardware-layout.md) (primary NVIDIA docs)
- Confirms from official source: Micro-Fit 9–28 V/8 A; **USB-C PD Sink 140 W** (28 W below the 168 W ceiling → full load needs the 28 V brick/Micro-Fit, not USB-C); 2× USB-A 10 Gbps; **5 GbE + QSFP28 4×25 Gbps**; DP+HDMI; M.2 Key M 1 TB NVMe; power/recovery/reset buttons + LED
- Folded IO/layout into [Jetson Thor](entities/jetson-thor.md) (new IO/board-layout block; sources 8→9) and added the USB-C-140 W primary-source note to the [Thor power budget](syntheses/projects/xlerobot-thor-power-budget.md)
- Updated [index.md](index.md)

## [2026-05-31] ingest | NVIDIA Jetson Thor Module Carrier Board Spec (SP-12533-001 v1.2)
- PDF in raw/Jetson_Thor_Module_Carrier_Board_Spec_SP-12533-001_v1.2.pdf; created [source page](sources/nvidia-jetson-thor-carrier-board-spec.md)
- **Power correction**: bundled adapter is **USB-C** (not Micro-Fit); max current **5 A USB-C / 15 A Micro-Fit** (Table 6-2); CYPD8225 PD controller = first-come-first-serve (inputs don't sum). Updated [Jetson Thor entity](entities/jetson-thor.md) (sources 9→10) + [Thor power budget](syntheses/projects/xlerobot-thor-power-budget.md)
- **Notable finding**: AGX Thor dev kit has **no 40-pin GPIO header and no MIPI-CSI camera connectors** (Orin→Thor change) — sensors move to Ethernet (5 GbE / QSFP28 4×25 Gbps, CSI-over-Ethernet), USB, CAN
- Filled remaining IO: M.2 Key E (Wi-Fi/BT preinstalled), 2× CAN (J47), Automation Header (J42, auto-power-on via pin5↔6), RTC battery (J13), fan/audio headers, 699-pin module connector
- Resolved the [hardware-layout page](sources/nvidia-jetson-agx-thor-devkit-hardware-layout.md) open questions; updated [index.md](index.md)

## [2026-05-31] update | Canonical battery recommendation for Thor (post carrier-spec)
- Folded the updated recommendation into [Thor power budget synthesis](syntheses/projects/xlerobot-thor-power-budget.md): regulator→Micro-Fit topology (fixed ~19–20 V kills the 28 V-ceiling trap), Micro-Fit (15 A) over USB-C (5 A) for full load, first-come-first-serve (no summing), ~300–500 Wh for ~2 hr
- Added the XLeRobot dual-DC-DC build (one 24 V pack → ~20 V Thor Micro-Fit + 12 V motor bus); corrected the old "28 V/PD" framing and de-duplicated the recommendations block

## [2026-05-31] ingest | AGX Thor Dev Kit — User Guide (landing/index)
- Created [source page](sources/nvidia-jetson-agx-thor-devkit-user-guide-index.md) as a doc-set map (navigation hub; thin on net-new facts)
- Captures the user-guide TOC: Quick Start, BSP/Docker/CUDA/JetPack SDK setup, Hardware Layout (ingested), Supported Hardware, Interim Solutions (UEFI/USB/headless), Troubleshooting
- Flags highest-value un-ingested subpages: Supported Hardware (likely Micro-Fit part #) + Quick Start/JetPack SDK Setup (first-boot/flash)
- Added to [Jetson Thor](entities/jetson-thor.md) Mentioned-in (sources 10→11); updated [index.md](index.md)

## [2026-05-31] note | AGX Thor "Supported Hardware" page is a redirect (no ingest)
- Checked the Supported Hardware subpage: empty — one-line redirect to the **Jetson Thor Series Supported Components List, DA-12429-001**, a download-gated PDF on the Jetson Download Center (WebFetch can't pull it)
- No source page created (nothing to ingest). Recorded the concrete pointer in the [user-guide index](sources/nvidia-jetson-agx-thor-devkit-user-guide-index.md) and [carrier-board spec](sources/nvidia-jetson-thor-carrier-board-spec.md) open questions: the SCL is the authoritative source for the Micro-Fit mating part + camera/M.2/QSFP28 compatibility; needs the PDF downloaded to raw/ to ingest

## [2026-05-31] ingest | Computational Life (Agüera y Arcas et al., 2024) — arXiv 2406.19108
- New topic branch (no prior coverage): artificial life / emergence. PDF in raw/2406.19108v2.pdf
- Created [source page](sources/computational-life-self-replicating-programs-paper.md), entity [Blaise Agüera y Arcas](entities/blaise-aguera-y-arcas.md), and concept [Artificial life and the emergence of self-replication](concepts/alife/artificial-life-and-self-replication.md) in a **new `concepts/alife/` folder**
- Thesis: self-replicators spontaneously arise from random self-modifying programs with no fitness function (BFF/Brainfuck, Forth, Z80, 8080); sharp pre-life→life transition via novel "high-order entropy"; SUBLEQ counterexample
- Tied into [critiques of the intelligence north star](syntheses/society/critiques-of-the-intelligence-north-star.md) as a 4th "paradigm of intelligence" (emergence axis, alongside LeCun/Jordan/Constitution)
- Registered `concepts/alife/` in [CLAUDE.md](../CLAUDE.md) structure tree; updated [index.md](index.md) (new source + entity + concept + Artificial Life section)

## [2026-05-31] ingest | Boids (Reynolds) + cubff — flocking & ALife emergence
- Sources requested: red3d.com/cwr/boids/, Stanford SoCo boids page, and github.com/paradigms-of-intelligence/cubff
- Note: user originally listed `apankrat/bff` (an unrelated standalone Brainfuck interpreter) but corrected to `paradigms-of-intelligence/cubff` (the actual Computational Life substrate)
- Raw captures: raw/reynolds-boids-red3d.md, raw/stanford-soco-boids-2008.md, raw/cubff-github-readme.md
- Created sources [Boids (Reynolds)](sources/reynolds-boids-page.md), [Boids — Stanford SoCo](sources/stanford-soco-boids.md), [cubff](sources/cubff-github.md)
- New concept [Flocking and boids](concepts/alife/flocking-and-boids.md) (three rules; emergence/edge-of-chaos; swarm-intelligence/robotics bridges) — sibling to Computational Life in the `concepts/alife/` branch
- New entity [Craig Reynolds](entities/craig-reynolds.md)
- Updated [Artificial life concept](concepts/alife/artificial-life-and-self-replication.md) (added boids sibling section + related/mentioned links; sources 1→2), [Computational Life source](sources/computational-life-self-replicating-programs-paper.md) (cubff code → its own source page), [Blaise Agüera y Arcas](entities/blaise-aguera-y-arcas.md) (cubff mention), [index.md](index.md)

## [2026-05-31] ingest | Drone Swarm review (Raj & Kos, 2026) — Sensors 26(10):2943
- Source PDF raw/sensors-26-02943.pdf (21 pp, CC BY); extracted via pypdf
- Created [source page](sources/raj-kos-drone-swarm-review-2026.md): UAV-swarm review — C2 taxonomy (consensus/centralized/emergent/hierarchical), trajectory generation (SARG, LEVIOSA), DL trajectory prediction (DynGN, EvolveGCN, LSTM), counter-swarm/anti-drone (ODCDM/CBAA, loyal wingman), swarm metaheuristics (PSO/ACO/GWO/…), 1000-drone @ 99.95% from 5% informed agents, SwarmGPT; heavy military/dual-use framing
- New concept [Swarm intelligence](concepts/robotics/swarm-intelligence.md) — bridges [flocking/boids](concepts/alife/flocking-and-boids.md) (ALife) ↔ [agentic UAVs](concepts/robotics/agentic-uavs.md) (robotics)
- Updated [agentic UAVs](concepts/robotics/agentic-uavs.md) (sources 3→4, added swarm-intelligence link), [flocking and boids](concepts/alife/flocking-and-boids.md) (linked swarm-intelligence), [index.md](index.md)

## [2026-05-31] lint-fix + ingest | Lint fixes (#1,#3) + Reynolds 1987 boids paper
- Lint #1 (stale source counts): bumped [llm-agent-architecture](concepts/agents/llm-agent-architecture.md) 12→18, [openclaw](entities/openclaw.md) 1→5, [openclaw-controller](entities/openclaw-controller.md) 1→5, [dgx-spark](entities/dgx-spark.md) 1→4
- Lint #3: documented source-page frontmatter exception (published/ingested, not created/updated) in CLAUDE.md schema + Source pages section
- Ingested raw/SIGGRAPH87.pdf = Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model" (SIGGRAPH '87) — the seminal boids paper; closes the lint knowledge gap
- Created [source page](sources/reynolds-flocks-herds-schools-1987.md): original rule names (Collision Avoidance / Velocity Matching / Flock Centering) in strict precedence; prioritized-acceleration arbitration (not averaging); localized-perception finding; bird-oid etymology; particle-system + actor lineage; geometric flight; O(N²)+constant-time hypothesis; force-field vs steer-to-avoid; 1987 Lisp-Machine perf
- Upgraded [flocking and boids](concepts/alife/flocking-and-boids.md) (sources 2→3; original-vs-popular rule-name table + priority callout + localized-perception) and [Craig Reynolds](entities/craig-reynolds.md) (2→3); added "primary source now ingested" notes to [reynolds-boids-page](sources/reynolds-boids-page.md) + [stanford-soco-boids](sources/stanford-soco-boids.md); updated [index.md](index.md)

## [2026-05-31] ingest | BFF — Emergent Complexity experiment (Jonas Werner, 2026-03-07)
- Source: https://jonamiki.com/posts/bff-emergent-complexity-experiment/ (CC BY 4.0); code github.com/jonas-werner/bff-emergent-complexity
- Created [source page](sources/jonas-werner-bff-emergent-complexity.md): **independent from-scratch reproduction** of the [Computational Life](sources/computational-life-self-replicating-programs-paper.md) BFF soup. C+OpenMP engine + Python orchestration; 1,024×64-byte programs, pair→concat→exec→split, 50k epochs = 51.2M interactions/seed. Confirms spontaneous self-replicators with no fitness function + sharp **"gelation" phase transition** (ops/interaction ~700→6,000–12,000; lineage diversity collapses; compressibility rises). Seed 5 = crash/compete/rebuild (3 lineages); Seed 3 = monoculture (BEC0 in 1,023/1,024). First independent reproduction of the result in the wiki; runs on a 12-thread desktop in minutes (CPU, no GPU/cubff).
- Updated [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 2→3; added reproduction bullet + mentioned-in), [Computational Life source](sources/computational-life-self-replicating-programs-paper.md) (independently-reproduced note), [cubff source](sources/cubff-github.md) (Related section), [Blaise Agüera y Arcas](entities/blaise-aguera-y-arcas.md) (sources 1→3, mentioned-in), [index.md](index.md)
- Flagged: author's philosophical coda (Hoffman Fitness-Beats-Truth, "reality as interface", Xenobots) is his editorializing, kept separate from the reproduction; only BFF substrate reproduced (not Forth/Z80/8080/SUBLEQ); uses compressibility as a proxy for the paper's high-order-entropy signal

## [2026-05-31] ingest | Xenobots — Kriegman et al. 2020 + 2021 (reconfigurable organisms)
- Two PDFs added to raw/ (PNAS): kriegman-et-al-2020-...-reconfigurable-organisms.pdf (CC BY 4.0) + kriegman-et-al-2021-...-kinematic-self-replication...pdf (CC BY-NC-ND 4.0); extracted via pypdf
- NOTE: raw/ingest_these_urls.txt was empty (0 bytes) — no URLs to ingest; flagged to user
- Created sources [Kriegman 2020 (pipeline for reconfigurable organisms)](sources/kriegman-2020-reconfigurable-organisms.md) — evolutionary algorithm co-designs body+behavior in soft-body sim, built from Xenopus frog cells; locomotion/manipulation/transport/collective/self-repair; generator-and-filter pipeline (robustness + build filters); cilia suppressed via Notch-ICD — and [Kriegman 2021 (kinematic self-replication)](sources/kriegman-2021-kinematic-self-replication.md) — swarms push loose cells into piles that mature into offspring; spontaneous + un-selected; AI-evolved C-shaped semitorus triples replication rounds (~2→4, +149% offspring diameter); von Neumann replicators + quadratic exponential-utility (microcircuit-assembly sim); no constructor/copier/controller/blueprint; amyloid-world origins-of-life tie-in
- New entity [Xenobots / reconfigurable organisms](entities/xenobots.md) (new index subsection "Biohybrid / living machines"); people [Sam Kriegman](entities/sam-kriegman.md), [Josh Bongard](entities/josh-bongard.md), [Michael Levin](entities/michael-levin.md)
- New concept [Evolutionary computation](concepts/alife/evolutionary-computation.md) — gradient-free morphology+behavior co-design; contrasted with SGD/RL
- Updated [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 3→5; new "Self-replication in living matter — Xenobots" section + "two senses of self-replication-without-selection" callout linking Computational Life vs Xenobots), [BFF post](sources/jonas-werner-bff-emergent-complexity.md) (Xenobots mention now linked to entity), [Blaise Agüera y Arcas](entities/blaise-aguera-y-arcas.md) count 1→3, [index.md](index.md)
- Cross-substrate open question logged: spontaneous un-selected self-replication in code (Computational Life) vs. cell mechanics (Xenobots) — candidate future synthesis

## [2026-05-31] ingest | raw/ingest_these_urls.txt — 3 URLs (Xenobots 2.0 + EMBS feature + CRobots)
- URL file now populated (178 bytes); ingested all three
- [Blackiston et al. 2021 — A cellular platform for synthetic living machines](sources/blackiston-2021-cellular-platform-synthetic-living-machines.md) (Science Robotics, eabf1571): the cilia-driven "Xenobots 2.0"; self-assembling Xenopus explants locomote via surface cilia (no sculpted muscle); Voxcraft-sim; substrate for the kinematic self-replication study. **GATED (403 on article+ePDF) — abstract-level ingest** from abstract + EMBS feature + search metadata; flagged with callout. Co-authors add Emma Lederer + Simon Garnier (NJIT, collective behavior)
- [AI-Designed Living Robots Can Self-Replicate (IEEE EMBS feature)](sources/embs-xenobots-self-replicate-feature.md) (2022-03-12): secondary journalism on the Dec 2021 self-replication paper; quotes Blackiston/Kriegman/Bongard + von Neumann framing + safety stance
- [CRobots (troglobit/crobots)](sources/crobots-github.md): Tom Poindexter's 1985 C-robots programming game; instruction-limited VM; GPL-2.0 (2013); maintained by Joachim Wiberg. Different domain (programming game / autonomous-agent lineage, Core War family); hand-coded + static, NO replication/learning — flagged the mismatch with the self-replication theme and noted Core War as the closer un-ingested cousin
- Updated [Xenobots entity](entities/xenobots.md) (sources 3→5; two-generations note + cilia capability + Lederer/Garnier), [Sam Kriegman](entities/sam-kriegman.md)/[Josh Bongard](entities/josh-bongard.md)/[Michael Levin](entities/michael-levin.md) (each 2→4, mentioned-in), [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 5→8; new "Programming games (cultural lineage)" subsection linking CRobots + flagging Core War), [index.md](index.md)

## [2026-05-31] ingest | Core War — Dewdney 1984 + pMARS + corewars.org
- Three URLs ingested (completing the self-replicating-programming-game gap flagged in the CRobots ingest)
- [Dewdney 1984 — Core War (Scientific American)](sources/dewdney-1984-core-war-scientific-american.md): founding text; circular 8000-cell core, MARS VM, Redcode (MOV/DAT/JMP/CMP/...), relative addressing; warriors Imp (MOV 0 1 = minimal self-replicator), Dwarf, Gemini/Juggernaut/Bigfoot, Raidar/Scanner; Creeper/Reaper folklore + Darwin (McIlroy) + Worm (Shoch) lineage; co-created with David Jones at UWO
- [pMARS — KOTH.org](sources/pmars-koth.md): de-facto standard simulator (Ma/Sieben/Strack/Wangsaw, first release 1993-08-25); ICWS'94 draft + '88 mode + p-space; official rec.games.corewar simulator; KOTH email-tournament hills; GPL-2.0 per distro packaging. NOTE: koth.org timed out twice — grounded via corewar.co.uk + Debian/FreshPorts/Ubuntu metadata + search; flagged with callout
- [corewars.org](sources/corewars-org.md): present-day community hub; thin (definition + pMARS pointer + online hills + rec.games.corewars); webmaster "SB" (Sapan Bhatia)
- New entities [Core War](entities/core-war.md) (new index subsection "Programming games / digital ALife") + [A. K. Dewdney](entities/ak-dewdney.md) (People)
- Updated [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 8→11; rewrote "Programming games" note → "Programming games & the digital-replicator lineage": Core War now ingested as the Imp/self-replicator member, CRobots as non-replicating cousin, full von Neumann → Darwin/Worm/Core War → Tierra/Avida → Computational Life chain with Tierra/Avida flagged as the remaining gap), [CRobots source](sources/crobots-github.md) (Core War now links to entity; open question resolved), [index.md](index.md)
- Standing gap logged: Tierra (Tom Ray 1991) + Avida — the evolved-digital-replicator bridge between Core War (hand-written) and Computational Life (emergent) — still un-ingested

## [2026-05-31] ingest | Darwin (Bell Labs, 1961) — McIlroy transcript [raw/darwin.pdf]
- Ingested the primary-source origin of the self-reproducing-program game (the un-ingested ancestor flagged when Core War landed)
- [Darwin source page](sources/darwin-1961-bell-labs-game.md): invented by Vyssotsky (Aug 1961, IBM 7090); McIlroy coded the umpire overnight + transcribed the 1971 letter (basis for "Aleph-Null"'s 1972 SP&E column; Aleph-Null != C.A. Lang); Morris's adaptive 44-cell species ended the game. Umpire-mediated probe/kill/claim (vs Core War shared-tape); reproduction requires correct *relocation* (Vyssotsky's 5-instr loop); McIlroy's 15-cell "hard-shelled virus"; emergent rock-paper-scissors population oscillation; failed "bisexualism" experiment; 10,000-cell arena; executed-not-interpreted + honesty rule. Includes the original 1961 rules flyer (species N / size<2000 / 20 protected cells)
- New people: [Doug McIlroy](entities/doug-mcilroy.md), [Victor Vyssotsky](entities/victor-vyssotsky.md), [Robert Morris](entities/robert-morris.md) (Sr.; NSA; father of Morris-worm author — self-replication irony noted)
- Updated [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 11→12; lineage now anchored at Darwin 1961 with a real link), [Core War entity](entities/core-war.md) + [Dewdney source](sources/dewdney-1984-core-war-scientific-american.md) (Darwin "inline mention" upgraded to linked source + entities), [index.md](index.md)
- Lineage now: von Neumann → Darwin (1961) → Core War (1984) → Tierra/Avida (still un-ingested) → Computational Life. Darwin had within-round *adaptation* (Morris) but not across-generation code *evolution* — Tierra/Avida remain the gap

## [2026-05-31] ingest | Tierra (Ray 1991) + Avida (Adami & Brown 1994) — evolved digital replicators
- Two primary PDFs added to raw/: Ray1991AnApproachToTheSynthesisOfLife.pdf + 9405003v1.pdf (arXiv adap-org/9405003); extracted via pypdf
- [Ray 1991 — Tierra](sources/ray-1991-tierra-synthesis-of-life.md) (Artificial Life II): "synthesize not simulate" life (= self-replicating + open-endedly evolving); 80-instruction hand-written ancestor in a memory "soup"; address-by-template; write-protected/read-execute-open memory → parasitism; reaper + slicer + genebanker; from ONE ancestor evolves parasites/immunity/hyper-parasites/sociality/cheaters (digital Cambrian). Explicitly contrasts Core War/viruses (replicate but don't evolve) and pre-defined-fitness sims (dead-ended)
- [Adami & Brown 1994 — Avida](sources/adami-brown-1994-avida.md) (Caltech; ALife IV): tierra-inspired but 2D toroidal + local nearest-neighbor (CA-like) update → more diversity, fewer metastable traps (genotype-age power-law D≈1.14 vs Tierra 1.6); evolving computation via task rewards (evolve integer addition from a size-59 replicator); error-catastrophe + optimal mutation rate; near-linear parallel distribution; Charles Ofria acknowledged (later Avida lead)
- New entities [Tierra](entities/tierra.md) + [Avida](entities/avida.md) (index "Programming games / digital ALife" subsection); people [Thomas Ray](entities/thomas-ray.md) + [Chris Adami](entities/chris-adami.md)
- Updated [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 12→14; lineage rewritten as "now ingested end-to-end" with the designed→evolved→emergent gradient; open-ended-evolution now marked covered; split the doubled programming-games heading), [Core War entity](entities/core-war.md) + [Darwin source](sources/darwin-1961-bell-labs-game.md) (Tierra/Avida links, removed "not yet ingested"), [Computational Life source](sources/computational-life-self-replicating-programs-paper.md) (open-endedness open-question refreshed), [index.md](index.md)
- LINEAGE NOW COMPLETE end-to-end: von Neumann → Darwin (1961) → Core War (1984) → Tierra/Avida (1991-94) → Computational Life (2024). Remaining optional extensions: Avida's Nature 2003 "Evolution of Complex Features" + Mordvintsev Neural Cellular Automata

## [2026-05-31] ingest | Lenski et al. 2003 (Avida evolution of complexity) + NCA "Cells to Pixels" (Pajouheshgar et al. 2025)
- Two PDFs added to raw/: Lenskietal2003.pdf + 2506.22899v3.pdf; both are the optional extensions flagged after the Tierra/Avida ingest
- [Lenski et al. 2003 — The evolutionary origin of complex features](sources/lenski-2003-evolutionary-origin-complex-features.md) (Nature 423:139-144): Avida; EQU complex logic function evolves from a replicate-only 50-instr ancestor by building on simpler rewarded functions; KEY RESULT **0/50 populations evolve EQU when only EQU rewarded vs 23/50 reward-all** (and 124/360 across 36 drop-one/two regimes); deleterious mutations as stepping-stones (reverting a NAND-knockout eliminated EQU); pleiotropy/epistasis emergent; the evolution-of-complexity capstone
- [Pajouheshgar et al. 2025 — Neural Cellular Automata: From Cells to Pixels](sources/pajouheshgar-2025-nca-cells-to-pixels.md) (arXiv 2506.22899v3; EPFL + Google): NCA = grid of identical cells running a shared LEARNED local update rule → self-organize w/ regeneration+robustness; scales NCA to high-res/real-time by decoupling coarse-grid dynamics from a local coordinate-based implicit decoder (LPPN); 2D/3D/mesh. Co-author Mordvintsev = NCA originator + Computational Life co-author
- New concept [Neural Cellular Automata](concepts/alife/neural-cellular-automata.md) (learnable self-organization wing; contrast learned vs evolved vs emergent local rules)
- New entities: [Charles Ofria](entities/charles-ofria.md) (Avida lead), [Richard Lenski](entities/richard-lenski.md) (LTEE), [Alexander Mordvintsev](entities/alexander-mordvintsev.md) (NCA + Computational Life bridge)
- Updated [Avida entity](entities/avida.md) (sources 1→2 + Lenski result), [Chris Adami](entities/chris-adami.md) (1→2), [Adami&Brown source](sources/adami-brown-1994-avida.md) (Lenski "now ingested"), [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (sources 14→16; added evolution-of-complexity paragraph + learnable-self-organization/NCA subsection + Mordvintsev bridge), [Computational Life source](sources/computational-life-self-replicating-programs-paper.md) + [Blaise entity](entities/blaise-aguera-y-arcas.md) (Mordvintsev now linked; NCA open-question resolved), [index.md](index.md)
- Open synthesis now framed: learned (NCA) vs evolved (Avida) vs emergent (Computational Life) local rules — all "complex global behavior from simple local interactions," Mordvintsev spanning two of the three

## [2026-05-31] synthesis | Local rules, global complexity (learned vs evolved vs emergent self-organization)
- Filed [syntheses/alife/local-rules-global-complexity.md](syntheses/alife/local-rules-global-complexity.md) (new syntheses/alife/ subfolder) — original cross-cutting analysis of the ALife branch built up this session
- Thesis: all the ALife systems share "complex global behavior from simple local rules, no central controller"; the axis that matters is **where the local rule comes from** → hand-designed (boids/Darwin/Core War) → learned (NCA) → evolved (Tierra/Avida) → emergent (Computational Life), a monotonic "how much is designed in?" gradient the digital-replication chain walks in historical order
- Deeper reframing: **what information becomes structure?** designer's head → target-via-gradient (backprop) → environment-via-selection (Adami's "stochastic information transfer"; Lenski 0/50 vs 23/50) → nothing external (Computational Life high-order entropy from reachability alone)
- Notes the bins are fuzzy (Xenobots span all three; Avida = evolved rule + designed reward; NCA = learned rule + emergent regeneration); Mordvintsev as the empirical learned↔emergent bridge; ties to the paradigms-of-intelligence thread (LeCun/Jordan/Agüera y Arcas) and the JEPA anti-hand-design rhyme; lists 4 open questions (do routes meet? information accounting? Xenobots' precise place? what sustains open-endedness — SUBLEQ clue)
- Linked from [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) + [NCA concept](concepts/alife/neural-cellular-automata.md); added to [index.md](index.md) Syntheses (new "### Artificial Life" subsection)

## [2026-06-02] ingest | Cosmos 3 — Omnimodal World Models for Physical AI (NVIDIA technical report + HF blog)
- New file in raw/: technical-report.pdf (138 pp., "Cosmos 3: Omnimodal World Models for Physical AI", NVIDIA, 2026-06-01) — extracted via pypdf; plus the HF launch blog (huggingface.co/blog/nvidia/cosmos-3-for-physical-ai). Both converge on Cosmos 3.
- [Cosmos 3 Technical Report](sources/cosmos-3-technical-report.md) (primary): dual-tower **Mixture-of-Transformers** (AR reasoner init from Qwen3-VL + diffusion generator, flow-matching) jointly modeling language/image/video/audio/action; one model = VLM + T2I/T2V/I2V generator + audio-visual gen + forward-dynamics + inverse-dynamics + video-action **policy**. Variants: Edge 4B (deferred), Nano 16B, Super 64B; OpenMDW-1.1. Results: #1 open-weight T2I (UniGenBench 91.36) + I2V (Artificial Analysis 2026-05-28); reasoner SOTA in robotics/smart-infra/driving (trails Gemini 3.1 Pro on general); Cosmos3-Nano-Policy-DROID **#1 on RoboArena** + beats π0.5 on RoboLab-120 (39.7 vs 28.1). Central claim: **unified action mid-training** → reusable cross-embodiment action prior (LIBERO-10 new-embodiment 24.6% vs 0.0% at 500 iters). NB: NVIDIA used Claude-Opus-4.7/4.6 as eval prompt rewriters.
- [Cosmos 3 HF blog](sources/nvidia-cosmos-3-hf-blog.md) (secondary): launch/onboarding; Diffusers `Cosmos3OmniPipeline`, SDG datasets, Cosmos-Framework post-training. **Omits audio**; report is authoritative (flagged as discrepancy callout).
- New entity [Ming-Yu Liu](entities/ming-yu-liu.md) (Cosmos 3 supervision lead). New concept [World-action model (WAM)](concepts/world-models/world-action-model.md) — FD/ID/policy unification; instances Cosmos 3, Dream*, GE-Sim2.
- Updated [NVIDIA Cosmos](entities/nvidia-cosmos.md) (major Cosmos-3 section; sources 10→12), [NVIDIA](entities/nvidia.md) (omnimodal-WM bullet; 31→33), [world-model concept](concepts/world-models/world-model.md) (omnimodal-WM family; 17→18), [world-model-simulators](concepts/world-models/world-model-simulators.md) (12→13), [VLA concept](concepts/learning/vla-models.md) (Cosmos 3 policy + WAM callout + action-head row; 30→31), [generative-video-vs-jepa synthesis](syntheses/world-models/generative-video-vs-jepa-world-models.md) (Cosmos 3 partially closes the generative-video real-robot-policy gap — as a policy, not zero-shot MPC transfer), [glossary](glossary.md) (+MoT, WAM, FD/ID), [index.md](index.md)
- Open: still **no head-to-head vs JEPA** (V-JEPA 2 / LeWM) on a shared task; audio under-evaluated; Edge unreleased; whether consequence-modeling helps *deployment* robustness not isolated.

## [2026-06-02] ingest | Wolfram 2025 — "Engineering and Innovation from Half a Century of the Game of Life"
- Source: Stephen Wolfram Writings essay (2025-03), https://writings.stephenwolfram.com/2025/03/... — fetched via WebFetch (no raw file). Fills the cellular-automata gap flagged in the artificial-life concept.
- [Wolfram 2025 Game-of-Life engineering essay](sources/wolfram-2025-game-of-life-engineering.md): treats ~55 yr of Game-of-Life pattern-discovery as a clean dataset for studying innovation ("metaengineering"). Core axis = **construction ("invention", modular/comprehensible) vs search ("discovery"/mining the computational universe, minimal irreducible "blob")**; search overtook construction (~60%→~70%) as compute grew; "modularity index" drops as patterns are optimized; most-reused parts (the "eater") all found early-1970s; die-hards show construction reaching 17^^^3-step lifetimes search never will; **computational irreducibility** as the "spark", static structure as the "cage" (analogized to AI alignment). Connects to Rule 30 / NKS / Class-4 / Principle of Computational Equivalence / Ruliad.
- New concept [Cellular automata](concepts/alife/cellular-automata.md) (2 sources) — general CA substrate: Conway's Life + Wolfram elementary CAs/Rule 30, four behavior classes, universality, computational irreducibility, and the construction-vs-search axis. Parent of [NCA](concepts/alife/neural-cellular-automata.md).
- New entities: [Game of Life](entities/game-of-life.md) (system), [John Conway](entities/john-conway.md), [Bill Gosper](entities/bill-gosper.md), [Stephen Wolfram](entities/stephen-wolfram.md).
- Updated [artificial-life concept](concepts/alife/artificial-life-and-self-replication.md) (16->17; resolved the "general cellular automata not yet covered" note; added a CA-substrate subsection), [NCA concept](concepts/alife/neural-cellular-automata.md) (links parent CA concept), [local-rules-global-complexity synthesis](syntheses/alife/local-rules-global-complexity.md) (added Wolfram's **orthogonal construction-vs-search axis** — where the *patterns* come from given a fixed rule, vs the existing where-the-*rule*-comes-from spectrum; Game of Life added to hand-designed row), [glossary](glossary.md) (+CA, Computational irreducibility, Game of Life, Rule 30), [index.md](index.md)
- Synthesis insight: Wolfram's "search" end == the rule-source spectrum's evolved/emergent end == JEPA's anti-hand-design — all "mining vs designing"; comprehensibility is something *construction adds*, not a property of solutions. Open: do the metaengineering "laws" generalize beyond one CA framework? (asserted, not measured)

## [2026-06-03] ingest + update | Jetson Thor power modes (R38.4) → software-capped XLeRobot power budget
- Source: NVIDIA Jetson Linux Developer Guide, Platform Power and Performance — Jetson Thor (R38.4), https://docs.nvidia.com/jetson/archives/r38.4/.../JetsonThor.html — fetched via WebFetch (no raw file).
- New source [Jetson Thor Platform Power & Performance (R38.4)](sources/nvidia-jetson-thor-platform-power-performance.md): T5000 nvpmodel modes — MAXN (uncapped, throttles @130W TDP), 120W (Mode 1, default), 90W (Mode 2), 70W (Mode 3); T4000 — MAXN + 70W default (90W TDP). Sub-120W modes cut GPU 10->6 TPC (~-40% throughput) while barely touching CPU. `sudo nvpmodel -m <id>`, persists across reboot/SC7. Module TDP vs dev-kit 168W system cap (INA238) distinction.
- Updated [XLeRobot + Thor power budget synthesis](syntheses/projects/xlerobot-thor-power-budget.md) per user request — analysis now assumes software-capping Thor: new **§0 (nvpmodel lever)**; reframed §1 rate table (added active-manipulation ~90W row; capped vs uncapped peak ~175W vs ~225-245W); §3 runtime now a capped-vs-uncapped table (~1.4-3.0hr; +15-25% heavy-mode runtime at 70W); capping also lets a single USB-C PD feed (140W) power Thor (removes must-use-Micro-Fit for the compute rail); honest caveat that capping is marginal vs capacity. Trade-off = ~40% GPU throughput (bad for GPU-bound VLA, ~free for control/perception).
- Updated [Jetson Thor entity](entities/jetson-thor.md) (added Power modes (nvpmodel) subsection; sources 11->12), [index.md](index.md) (new source entry + refreshed synthesis line).
- Reconciliation: prior pages said Thor "40-130W" / "~130W inference"; clarified default is the 120W budget (Mode 1), 130W is the MAXN/TDP transient. 168W system cap (cited r38.2 before) reaffirmed in r38.4.
- Open: exact out-of-box default mode (MAXN vs 120W) ambiguous in fetch; no TOPS-per-mode or measured wall-power-per-mode under a real VLA load.

## [2026-06-03] query+synthesis | Anker SOLIX C300 DC vs C300 vs C1000 (robot power source)
- User query: compare C300 DC Power Bank, C300 Portable Power Station, and C1000 for the XLeRobot+Thor build; user confirmed they will use the **C300 AC Power Station (A1722, 600 W surge)**, not the DC bank.
- Filed [Anker SOLIX portable power — C300 DC vs C300 vs C1000](syntheses/platforms/anker-portable-power-stations.md). Specs (web-sourced, Anker pages + reviews): C300 DC A1726 = 288 Wh LiFePO4, **2.8 kg**, DC-only (2× 140 W USB-C, no AC/no 12 V/no surge), ~$180; C300 Station A1722 = 288 Wh LiFePO4, **4.1 kg** (confirmed 9.04 lb), 2× AC 300 W/**600 W surge** + 2× 140 W USB-C + 12 V/120 W car port, ~$200; C1000 A1761 = **1056 Wh**, **12.9 kg**, 6× AC 1800 W/2400 W surge, USB-C 100 W+30 W, 12 V/120 W, UPS <20 ms, ~$1000.
- Verdict: **C300 A1722 onboard** — serves both rails from one box (12 V car port for STS3215 motors + USB-C/AC for capped Thor), dual 140 W USB-C covers any Thor nvpmodel mode, 4.1 kg rideable. C300 DC is the niche lighter pick but lacks AC + 12 V (motors need a buck). C1000 = bench/charging dock only (12.9 kg ≈ doubles robot mass; 100 W USB-C < Thor 120 W mode). Runtime (70 W-capped robot ~145 W): C300 ~1.7 hr vs C1000 ~6-7 hr.
- Resolved earlier ambiguity (two different 288 Wh "C300" products): **correction** — the official XLeRobot BOM (material.html) lists the **C300 DC Power Bank (A1726, $179.99)**, NOT the AC station the wiki had assumed. The user substitutes the AC **C300 Power Station (A1722, 4.1 kg, 600 W surge + 12 V car port)** so one unit serves both robot rails. Fixed [XLeRobot entity](entities/xlerobot.md), [xlerobot-docs source](sources/xlerobot-docs.md), [power-budget synthesis](syntheses/projects/xlerobot-thor-power-budget.md), and the comparison page (BOM=DC / build=AC-substitution note) accordingly; cross-linked from [index](index.md).

## [2026-06-03] ingest + synthesis | "Cutting the Cord" (untethered onboard-Jetson XLeRobot) + Jetson onboard-compute comparison
- New file raw/2603.09051v1.pdf → [Cutting the Cord (Shaw et al., 2026)](sources/cutting-the-cord-untethered-xlerobot.md) — Correll lab (CU Boulder), arXiv 2603.09051v1, CC-BY-NC-ND. Untethered XLeRobot evolution: onboard **Jetson Orin Nano Super** ($249), **Tri-Bus power topology** (isolates Jetson from motor transients — fixed a 12.2 V→306 mV brownout on the stock daisy-chained bus; held 12.0 V ±0.1 V; 5% battery/30 min), High-Shell 4-wall print (1 kg/arm, 98.7% grasp), onboard RTAB-Map SLAM + Pink task-IK + Open-TeleVision VR teleop. **Total $1,202 BOM.**
- **On-edge benchmark (Orin Nano, FP16, e2e camera→action):** ACT 36 ms→27.8 Hz; Diffusion Policy 540 ms→1.8 Hz; SmolVLA-450M 714 ms→1.4 Hz. Insight: the **iterative action expert + denoising steps** are the bottleneck, not the VLM. Resolves the wiki's prior "no ingested Orin Nano TOPS" gap → **67 INT8 TOPS / 102 GB/s / 7–25 W**.
- New synthesis [Onboard compute for XLeRobot — Orin Nano vs AGX Orin vs AGX Thor](syntheses/platforms/jetson-onboard-compute-xlerobot.md) (the requested comparison). Verdict: power budget (288 Wh/300 W) is decisive → **Orin Nano (7–25 W, $249) = validated default** (ACT reactive; diffusion/SmolVLA ~1–2 Hz; 8 GB cap); **AGX Orin (15–60 W, 64 GB, ~$2k, 275 INT8 TOPS) = VLA-on-battery upgrade**; **AGX Thor (40–130 W, 128 GB, $3,499) = over-budget** for stock XLeRobot (paper's own conclusion), only viable software-capped 70 W + bigger battery. Orin NX 16 GB noted as midpoint. TOPS hedged (Orin INT8 vs Thor FP4/FP8 → "≈7.5× AGX Orin" anchor).
- New entity [Nikolaus Correll](entities/nikolaus-correll.md). Updated [Jetson Orin Nano](entities/jetson-orin-nano.md) (67 TOPS + benchmark; open-Q resolved; 8→9), [Jetson Thor](entities/jetson-thor.md) (exceeds-budget note; 12→13), [XLeRobot](entities/xlerobot.md) (Cutting-the-Cord downstream build), [VLA concept](concepts/learning/vla-models.md) (on-edge latency note; 31→32), [power-budget synthesis](syntheses/projects/xlerobot-thor-power-budget.md) + [Anker comparison](syntheses/platforms/anker-portable-power-stations.md) (cross-links), [index](index.md).
- **Contradiction flagged (not auto-fixed):** paper cites its C300 (ref [22]) as the **"C300 DC," $159.99, WITH a 12 V/10 A car outlet + 3 USB-C (2×140 W+1×100 W)** — conflicts with the wiki's earlier web spec (C300 DC Power Bank A1726 = no 12 V car port). Added a `> [!warning] Contradiction` callout to the Anker comparison page; recommend verifying exact SKU. A C300 DC *with* the 12 V outlet would moot the AC-substitution-for-motors argument.

## [2026-06-03] correction | C300 DC has a 12 V car outlet — contradiction resolved
- User confirmed (corroborating [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md)): the **Anker SOLIX C300 DC Power Bank (A1726) HAS a 12 V/10 A car outlet** (+ 3 USB-C: 2×140 W + 1×100 W). The wiki's earlier web-sourced spec wrongly said it lacked one.
- **Consequence (verdict reversal):** the DC bank serves *both* XLeRobot rails on its own (12 V car outlet → motors; USB-C → compute) — exactly what the paper's Tri-Bus does on it. So the AC station (A1722) is **no longer "required"** to solve the two-rail problem; its only edge is **600 W surge + an AC outlet** (for +1.3 kg). The DC bank is now the lighter/cheaper/paper-validated default; this build still opts for the AC for surge headroom.
- Fixed: [Anker comparison](syntheses/platforms/anker-portable-power-stations.md) (spec table 12 V row ✅ for DC; replaced the "two products"/"BOM-substitutes" callouts; resolved the Contradiction callout; rewrote §1/§3 + verdict table — DC = default, AC = surge upgrade; added the "surge may be optional if you firmware-cap motors" note), [power-budget synthesis](syntheses/projects/xlerobot-thor-power-budget.md) intro note, [XLeRobot entity](entities/xlerobot.md), [xlerobot-docs source](sources/xlerobot-docs.md), [Cutting the Cord source](sources/cutting-the-cord-untethered-xlerobot.md) open-Q (resolved), [index](index.md).

## [2026-06-03] update | Added Orin NX 16 GB to the XLeRobot onboard-compute comparison
- Per request, promoted Orin NX 16 GB from a footnote to a full column in [Jetson onboard compute for XLeRobot](syntheses/platforms/jetson-onboard-compute-xlerobot.md) (now a four-way: Orin Nano / Orin NX / AGX Orin / Thor).
- Specs (web-verified, NVIDIA JetPack 6.2 Super blog + retailers): **Orin NX 16 GB Super = 157 INT8 TOPS sparse (100 std), 10–40 W, 16 GB LPDDR5 @ 102 GB/s, 1024 CUDA + 32 Tensor + 2 DLA, 8× A78AE, ~$600 module**. Same GPU core count as the Orin Nano — the 2.3× TOPS comes from clocks/DLA/power; **pin-compatible with the Orin Nano Super Dev Kit carrier (P3768)** → a literal drop-in upgrade for the Cutting-the-Cord build.
- Repositioned verdict: Orin NX 16 GB = **drop-in VLA-upgrade sweet spot** (often a better buy than AGX Orin for this robot — keeps the Nano's power/size class while doubling RAM + ~2.3× TOPS); AGX Orin reframed as "max VLA-on-battery / when you need 64 GB". Updated spec + power tables, capability bullets, bottom line, title/H1, [index](index.md).

## [2026-06-03] update | Added XLeRobot to robot-platforms-comparison
- Added [XLeRobot](entities/xlerobot.md) to [Robot platforms — comparison](syntheses/platforms/robot-platforms-comparison.md) as the **educational-tier bimanual mobile manipulator** — fills the gap where [Mobile ALOHA](entities/aloha.md) ($32k) was the only ingested bimanual mobile manipulator. Added to at-a-glance table (after Mobile ALOHA), Educational tier section, By-function Bimanual line (two units, ~25× cost apart), a cross-tier note ("educational bimanual gap now filled" — cost collapse real, capability parity not: 1 kg/arm + ~40 cm reach + hobby servos), and the sources list. Back-linked from the XLeRobot entity Related section + index.
- **Not** added to [humanoid-platforms-survey](syntheses/platforms/humanoid-platforms-survey.md): XLeRobot is a wheeled bimanual cart, not a humanoid.

## [2026-06-03] ingest | Computing Neural Network Gradients (Kevin Clark, CS224n)
- New file raw/gradient-notes.pdf → [Clark — Computing Neural Network Gradients](sources/clark-computing-nn-gradients.md) (Stanford CS224n 2019; 7 pp.). Vectorized backprop via Jacobians: 7 reusable identities (z=Wx→W; elementwise→diag(f'); z=Wx wrt W→δᵀxᵀ; softmax-CE→ŷ−y; …), the "gradient shape = parameter shape" convention (transpose at the end), and a full worked 1-layer-NN backward pass with δ-error-signal reuse.
- New entity [Kevin Clark](entities/kevin-clark.md) (Stanford NLP PhD, Manning group; ELECTRA lead author).
- Wired into [Curriculum Module 1](syntheses/curriculum/curriculum-01-neural-networks.md): §3 backprop pointer + Recommended-reading item 5 (the matrix/vector step up from [micrograd](sources/karpathy-micrograd.md), on-ramp to [Blondel & Roulet](sources/blondel-roulet-differentiable-programming.md)) + Mentioned-in. Added **Jacobian** to [glossary](glossary.md); added source (pedagogical) + Kevin Clark (People) to [index](index.md).
- Scope note: dense+ReLU+softmax-CE only; conv/attention/norm/RNN gradients left as shape-matching exercises. Light pedagogical ingest (~6 pages).

## [2026-06-04] query+synthesis | Onboard Jetson Thor via a second C300 DC pack
- Query: would Thor work onboard the XLeRobot with a second C300 DC power bank? Answer: yes — it's the [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md) authors' own "additional power supply / tiered compute" fix.
- Filed a new **"Putting a Jetson Thor onboard — the two-pack (tiered-power) option"** section in [power-budget synthesis](syntheses/projects/xlerobot-thor-power-budget.md) + a takeaway bullet. Topology: pack #1 = existing Tri-Bus (motors/sensors); pack #2 = Thor alone via 140 W USB-C, nvpmodel -m 3 (70 W). Works because: 140 W USB-C feeds capped Thor directly (70–90 W target; 120 W nears the USB-C 140 W ceiling), a separate pack is max brownout isolation, and Thor @70 W ≈ 3.5 hr on its own 288 Wh so motors (~1.5–1.7 hr) become the binding limit.
- Caveats recorded: +4–5 kg (pack + Thor + active cooler), Thor needs active cooling (paper's passive duct was for 7–25 W Orin Nano), verify C300 140 W PD-EPR 28 V handshake, and the fit mismatch ($3,499 Thor on a ~$1.5 k robot — Orin NX 16 GB on the single pack usually better unless 128 GB needed). One-pack note: marginal-but-possible at 70 W cap, why the paper called it over-budget.

## [2026-06-04] ingest (partial) | Seeed Jetson product-line selection guide
- Requested: ingest the Jetson comparison from the Seeed blog (2026-05-13). **Blog is hard bot-blocked (HTTP 403)** — could not read its prose/framework/prices. Filed an honest, caveated [source page](sources/seeed-jetson-selection-guide.md) reconstructing the **verifiable module ladder** from NVIDIA-official figures (corroborated via the Forecr Jetson comparison + Seeed product listings via search).
- Module ladder captured: Orin Nano 4/8 GB (34/67 TOPS, 7–25 W) → Orin NX 8/16 GB (117/157 TOPS, 10–40 W) → AGX Orin 32/64 GB (200/275 TOPS, 15–60 W) → AGX Thor T4000/T5000 (1200/2070 FP4-TFLOPS, 40–130 W). + Seeed **reComputer** mapping: J30xx→Orin Nano, J40xx→Orin NX, **J4012 = Orin NX 16 GB**, new AGX Thor carrier.
- **Caught a secondary-source error:** Forecr's table mis-assigns AGX-Orin GPU core counts (1792/2048) to Orin NX; NVIDIA-official is 1024-core/32-TC for both Orin NX variants — used the official values, flagged in the source page.
- Updated [Seeed Studio entity](entities/seeed-studio.md) (new reComputer/Jetson section; 3→4), [onboard-compute comparison](syntheses/platforms/jetson-onboard-compute-xlerobot.md) (reComputer J4012 = buyable Orin NX 16 GB carrier + corroboration), [index](index.md).
- **Gap:** Seeed's per-use-case recommendations + reComputer prices not captured (403). Offered to add if the user pastes the article. AGX Orin / Orin NX still lack dedicated entities.

## [2026-06-04] update | Seeed Jetson guide — real product matrix added from user-supplied infographic
- The Seeed blog stayed 403, but the **user pasted the selection-guide infographic as an image**; transcribed the full 8-product matrix into [the source page](sources/seeed-jetson-selection-guide.md): reComputer Mini J3011 (Orin Nano 8GB) → J4012 family (Orin NX 16GB: J4012B / reServer Industrial / Super / Robotics) → J501 + Robotics J50 (AGX Orin 32/64GB) → Thor J601 (AGX Thor 128GB). Captured each carrier's interface, heat (fan/fanless), wireless, power input, size. Use-case bands: Vision AI → Generative AI/Robotics → Multimodal Perception/Humanoids.
- Builder-relevant: the **Robotics line (J4012/J50/Thor J601)** = GMSL2 multi-camera + isolated CAN-FD + **19–48/54 V DC** inputs (not 12 V). Upgraded the provenance note (infographic captured; only prices still missing). Corrected the Seeed entity (dropped an unverified "EtherCAT" claim from earlier search; J601 = 4×CAN-FD/8×GMSL2/4×10GbE per the infographic).
- Updated [Seeed entity](entities/seeed-studio.md), [index](index.md).

## [2026-06-04] update | Seeed Jetson guide — full article text supplied; promoted to full ingest
- User pasted the **complete article text** (the 403 blocker). Rewrote [the source page](sources/seeed-jetson-selection-guide.md) as a full ingest: the §1 **product-series table** (11 series: Industrial / Rugged / reServer Industrial / Classic / J401 / Super / Robotics J30-40 / reServer J501 / Mini J501 / Robotics J50 / J601), the §3 **by-scenario decision tree**, and per-scenario notes — alongside the infographic's specific-product matrix + the module ladder.
- **Correction of a correction:** the J601 (Thor) carrier **does integrate EtherCAT** — the article confirms it; I'd wrongly dropped it earlier off the abbreviated infographic. Re-added to source + Seeed entity.
- **Key XLeRobot finding:** Seeed's **Robotics J30/40** is the *battery-powered* robot carrier (19–54 V, CAN + 4× GMSL + I2C-IMU, 157 TOPS @ 60 °C/40 W, JetPack 6.2) — the **Robotics J4012** (Orin NX 16 GB Super) is the concrete onboard carrier for the compute comparison's XLeRobot pick; its 19–54 V input ties to the power-budget rail discussion. Updated [Seeed entity](entities/seeed-studio.md), [onboard-compute comparison](syntheses/platforms/jetson-onboard-compute-xlerobot.md), [index](index.md).
- Only remaining gap: reComputer **prices** (not in the article).

## [2026-06-04] ingest | Seeed — "How to Choose the Right NVIDIA Jetson Carrier Board" (Liyan Gong, 2026-02-09)
- User supplied full article text (companion to the product-level selection guide). New [source page](sources/seeed-jetson-carrier-board-selection.md): a **carrier-board selection methodology** — choose from a system-level view, not port counts. 3-step framework: (1) module tier defines the design boundary, (2) the carrier is part of the system (peripherals/enclosure/thermal/power), (3) make design priorities explicit (size/connectivity/expandability/deployment can't all be optimized).
- Example carriers (Super J401 / Robotics J401 / J401 open-source / A603 compact / A608 comms-oriented / Mini J501 AGX Orin) mapped to priorities via a worked edge-AI-vision case (connectivity→Super J401, compact→A603, interconnect→A608, prototyping→J401, robot→Robotics J401). Prototype→production = validate on mature carrier then trim/ODM.
- **Naming reconciliation captured:** "J401" = carrier board for Orin Nano/NX; populated with a module = the "J40xx" product (J401 + Orin NX 16 GB = J4012). So Robotics J401 carrier ↔ Robotics J4012 product. A603/A608 are new compact/comms carriers.
- Cross-linked: [selection-guide source](sources/seeed-jetson-selection-guide.md), [Seeed entity](entities/seeed-studio.md), [onboard-compute comparison](syntheses/platforms/jetson-onboard-compute-xlerobot.md), [index](index.md). Did not create a person entity for Liyan Gong (blog author, no other wiki anchor).

## [2026-06-07] ingest | Team 4414 HighTide — 2026 Technical Binder
- Source: https://2026.team4414.com/ (JS SPA; content extracted from compiled bundle)
- Created [Team 4414 HighTide — 2026 Technical Binder](sources/team-4414-hightide-2026-binder.md)
- Created entity [Team 4414 (HighTide)](entities/team-4414-hightide.md)
- Updated [FIRST Robotics Competition](entities/first-robotics-competition.md) (Mentioned in)
- Cross-linked from [Team 254 AI-in-FRC presentation](sources/team-254-ai-in-frc-presentation.md) (real-world answer to "what Claude/skills config does a team use") — AI-first dev, state-machine codebase, agent skill files
- Updated [index.md](index.md) (FRC highlights, Sources, Entities/Companies)
- Notable: REBUILT FUEL shooter (swerve + Dye Rotor + 4×Kraken-X44 copper-mass flywheel + turret); precomputed 2nd-order-polynomial shot calculator with pitch/yaw tilt compensation + turret tangential-velocity correction (shoot-on-the-bump-under-defense); "Tide Apps" in-house tool suite
- Open: model/harness used; whether Tide Apps + skill files are open-sourced; 2026 results; team location/roster not on the page

## [2026-06-07] ingest | Raspberry Pi AI HAT+ 2 (Hailo-10H)
- Source: https://www.raspberrypi.com/products/ai-hat-plus-2/
- Created [Raspberry Pi AI HAT+ 2 (Hailo-10H)](sources/raspberry-pi-ai-hat-plus-2.md)
- Created entity [Hailo](entities/hailo.md) (company + 8L/8/10H accelerator family) and [Raspberry Pi 5](entities/raspberry-pi-5.md)
- Updated [XLeRobot](entities/xlerobot.md) compute-model bullet (added NPU vs CUDA onboard options)
- Updated [Jetson onboard compute for XLeRobot](syntheses/platforms/jetson-onboard-compute-xlerobot.md) with an "NPU alternative" callout
- Updated [index.md](index.md) (Sources, Entities/Companies)
- Correction to prior query answer: "AI HAT+ 2" = the Hailo-10H board (one product, not two). AI HAT+ 2 = generative AI (40 TOPS INT4, 8 GB, $180, local LLM/VLM); original AI HAT+ = Hailo-8/8L vision CNN
- XLeRobot takeaway: 10H can host an onboard LLM/VLM agent layer + vision, but is NOT CUDA — does not run LeRobot ACT/Diffusion/SmolVLA/π0.5 policies; Jetson Orin Nano/NX remains the validated control-policy path

## [2026-06-07] ingest+synthesis | hailo-apps (GitHub) + Hailo-vs-Jetson synthesis
- Source: https://github.com/hailo-ai/hailo-apps
- Created [hailo-apps (GitHub)](sources/hailo-apps-github.md) — MIT; rel 26.03.1 (2026-04-13); Hailo-8/8L/10H on Pi5/Ubuntu/Windows; vision CLIs + Hailo-10H `gen_ai_apps` (LLM/VLM/Voice2Action); HailoRT+TAPPAS deps; "AI-Powered Development" agent beta
- Updated [Hailo](entities/hailo.md) (toolchain section + 2 sources + Mentioned in)
- Filed synthesis [Hailo NPU (AI HAT+ 2) vs Jetson (CUDA) for an onboard XLeRobot brain](syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md) — NPU runs compiled HEF models only; Jetson runs PyTorch policies as-is; map by layer (Hailo = perception+LLM agent, Jetson = control policy); usually both
- Cross-linked from [AI HAT+ 2 source](sources/raspberry-pi-ai-hat-plus-2.md); updated [index.md](index.md) (Sources, Entities, Syntheses)
## [2026-06-13] ingest | NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived tutorial)
- Created [NVIDIA Jetson AI Lab LeRobot tutorial](sources/nvidia-jetson-ai-lab-lerobot.md) — `dustynv/lerobot` containerized recipe to run LeRobot on Jetson (Koch v1.1 + ACT); archived/deprecated, pins pre-refactor LeRobot CLI + JetPack 6 GA/6.1
- New entity: [jetson-containers](entities/jetson-containers.md) — Dustin Franklin/NVIDIA Docker-on-Jetson framework + dustynv/* registry + autotag
- Updated [LeRobot](entities/lerobot.md) (new "Running LeRobot on Jetson (containerized)" subsection; 14→15 sources), [ACT](entities/act.md) (onboard-Jetson training instance; 6→7 sources), [Jetson Orin Nano](entities/jetson-orin-nano.md) (containerized LeRobot target; 9→10 sources)
- Updated [index.md](index.md) (new source + jetson-containers entity)
- Distinct from prior onboard story: Cutting the Cord measures policy latency on a self-built stack; the 3 ROS 2 bridges adapt LeRobot to ROS 2 — this is NVIDIA's container path to run LeRobot itself on edge silicon
## [2026-06-13] ingest | Seeed jetson-examples — nvblox recipe (README)
- Created [Seeed jetson-examples — nvblox recipe (README)](sources/seeed-jetson-examples-nvblox.md)
- New entities: [Isaac ROS NVBlox (nvblox)](entities/nvblox.md), [Isaac ROS](entities/isaac-ros.md), [Orbbec (Gemini2)](entities/orbbec.md)
- Updated [Seeed Studio](entities/seeed-studio.md) (added jetson-examples / nvblox; sources 4→5)
- Updated [index.md](index.md) (new source + 3 entities)
- Note: recipe uses Orbbec Gemini2 (not RealSense); requires Jetson Orin + JetPack 6.x + Docker + ~60 GB; Seeed deep-dive targets AGX Orin.

## [2026-06-14] ingest | Seeed jetson-examples (repo + reComputer runner)
- Created [Seeed jetson-examples (repo + reComputer runner)](sources/seeed-jetson-examples.md) — full repo-level ingest (supersedes the prior nvblox-only sub-recipe)
- New entity: [jetson-examples (reComputer runner)](entities/jetson-examples.md)
- Updated [jetson-containers](entities/jetson-containers.md) (added jetson-examples as the consumer layer on top; sources 1→2)
- Updated [Seeed Studio](entities/seeed-studio.md) (linked repo source + entity; sources 5→6)
- Cross-linked the existing [nvblox recipe](sources/seeed-jetson-examples-nvblox.md) to its parent repo
- Updated [index.md](index.md) (new source + new entity; bumped jetson-containers source count)
- Facts: MIT; 264★/40 forks; created 2024-06-24, last push 2026-06-11; `pip3 install jetson-examples` + `reComputer run <example>`; ~37 recipes; JetPack 4.6→7.1; built on jetson-containers; $250 contribution bounty.

## [2026-06-14] ingest | Ultralytics YOLO (GitHub)
- Created [Ultralytics YOLO (GitHub)](sources/ultralytics-github.md)
- New entity: [Ultralytics YOLO](entities/ultralytics-yolo.md)
- Cross-linked [jetson-examples](entities/jetson-examples.md) source + entity (upstream of the YOLO recipes)
- Updated [index.md](index.md) (new source + new entity)
- Facts: AGPL-3.0 (or Enterprise); 58k★/11k forks; created 2022-09-11, updated daily; `pip install ultralytics`; flagship YOLO26 (n/s/m/l/x); families v3/v5/v6/v8/v9/v10/11/12/26 + RT-DETR + SAM/FastSAM + YOLO-NAS; tasks detect/segment/classify/pose/OBB/track; COCO+ImageNet pretrained; ONNX/TensorRT export.
- Correction: README WebFetch claimed "semantic segmentation / Cityscapes" — not an Ultralytics task; excluded as a fetch-model hallucination (verified actual task set + model dirs via GitHub API).

## [2026-06-14] ingest | Hiwonder NexArm 6-Axis (product page)
- Created [Hiwonder NexArm 6-Axis (product page)](sources/hiwonder-nexarm-product-page.md)
- New entity: [NexArm](entities/nexarm.md)
- Updated [Hiwonder](entities/hiwonder.md) (now spans LLM-agent + LeRobot IL tiers; sources 3→4)
- Updated [SO-ARM101](entities/so-arm101.md) (added NexArm as a commercial leader-follower competitor)
- Updated [index.md](index.md) (new source + new entity)
- Facts: $279.99 base; 4 variants (Leader/Follower/IL Standard Kit/IL Advanced Kit); 6-DOF; 500mm reach; 500g payload; ±2mm repeat; leader 1.2kg/follower 1.3kg; HX-10HM/12H/30HM/65HM bus servos; 12V5A; USB/BT/Wi-Fi; dual-camera; parallel-rail gripper; LeRobot-native (ACT/Diffusion Policy/π0); leader-follower teleop + drag teaching.
- Significance: educational OEM Hiwonder shipping a LeRobot-FIRST arm = vendor-side convergence on the SO-ARM101 leader-follower playbook.

## [2026-06-14] ingest | Taking Flight with Dialogue (Lim et al. 2025) — PX4 local-LLM drone agent
- Created [Taking Flight with Dialogue (Lim et al. 2025)](sources/taking-flight-with-dialogue-px4-drone-agent.md) (arXiv 2506.07509v1)
- Updated concept [Agentic UAVs](concepts/robotics/agentic-uavs.md) — added "concrete open-source instance" section + onboard-VLM finding; sources 4→5
- Updated entities: [PX4 Autopilot](entities/px4-autopilot.md) (3→4), [Ollama](entities/ollama.md) (1→2; de-stubbed tag), [NVIDIA Isaac Sim](entities/nvidia-isaac-sim.md) (10→11), [Jetson Orin Nano](entities/jetson-orin-nano.md) (10→11)
- Updated [index.md](index.md) (new source under UAV cluster)
- Facts: ROS 2 wrapper over Ollama serves LLM (Gemma3 4B / Qwen2.5 3B / Llama-3.2 3B / DeepSeek-LLM 7B → discrete Turn/Move) + VLM (Gemma3 12B / Llama3.2-Vision 11B / LLaVA1.6 7B → binary object checks) → path planner → low-level PX4. HW: Jetson Orin Nano + Pixhawk 6c Mini + ZED Mini, ~0.56 m quad. Sim: PX4 SITL in Isaac Sim. Results: best mission success 40% (Gemma3); valid commands 100% (Gemma3/Qwen2.5/Llama-3.2) vs 38% (DeepSeek); VLM 97–100% valid. Code: github.com/limshoonkit/ros2-agent-ws.
- Significance: first fully-onboard, open-source, local-LLM realization of the agentic-UAV pattern; LLM-agent (not VLA); partly counters the concept's "onboard VLM infeasible" assumption — VLMs run, command-format validity is the wall. Notable: uses Isaac Sim (not PX4's default Gazebo) for SITL.

## [2026-06-14] ingest | PX4-Autopilot (GitHub repo)
- Created [PX4-Autopilot (GitHub repo)](sources/px4-autopilot-github.md) — code-repo companion to the docs ingest
- Updated entity [PX4 Autopilot](entities/px4-autopilot.md): release v1.16→**v1.17.0 stable (2026-05-13)**; added repo facts (C++/BSD-3/2012; ~12k★/15.5k forks); sources 4→5; updated date
- Updated entity [Dronecode Foundation](entities/dronecode-foundation.md) (governance mention)
- Staleness fix: annotated [PX4 docs source](sources/px4-docs-main.md) (its "v1.16 stable / v1.17 alpha" now superseded by v1.17.0)
- Updated [index.md](index.md) (new source under UAV cluster)
- Facts: PX4/PX4-Autopilot; BSD-3-Clause; C++; created 2012-08-04; ~12k stars / 15.5k forks (forks > stars); ~470 watchers; ~1489 open issues; NuttX/Linux/macOS; build `git clone --recursive && make px4_sitl`; Docker `px4io/px4-sitl:latest`; latest release v1.17.0 (2026-05-13); Dronecode/Linux Foundation governance; community via weekly dev call + Discord + PX4 Discuss.

## [2026-06-14] reverify+research | Team 4414 HighTide 2026 binder
- Re-pulled live SPA bundle for https://2026.team4414.com/ — content unchanged since 2026-06-07 ingest (no re-ingest needed); added `reverified: 2026-06-14` + note to [source](sources/team-4414-hightide-2026-binder.md)
- External research resolved 2 of 4 open questions:
  - **2026 results**: robot **RIPCURRENT**; **70–2–0**; #1 FIRST California district (365 pts); **REBUILT World Champions** (alliance captain, Houston) — via The Blue Alliance / FIRST
  - **Open-source status**: public github.com/team4414 holds only 2019-era repos; 2026 code + Tide Apps NOT public
  - Team identity: HighTide Robotics, Ventura County CA, founded 2018
  - Still open: which AI agent/model harness they use (not found)
- Updated entity [Team 4414 (HighTide)](entities/team-4414-hightide.md) (identity + results section, externally cited; world-champion tag) and [index.md](index.md)

## [2026-06-14] ingest | The Blue Alliance — Team 4414 (2026 season)
- Created [The Blue Alliance — Team 4414 (2026 season)](sources/tba-team-4414-2026.md) — full FRC competition record (TBA blocks WebFetch 403; fetched via curl + browser UA, parsed HTML)
- Updated entity [Team 4414 (HighTide)](entities/team-4414-hightide.md): added event-by-event results table + proper TBA citation; sources 1→2
- **Correction:** rookie year is **2012** per TBA — supersedes the "founded 2018" added earlier 2026-06-14 from a team-site snippet; fixed in entity + binder source
- Updated [index.md](index.md) (new source + entity source-count + rookie-year fix)
- Record: 70-2-0; #1 FIRST California district (365 pts); REBUILT World Champions. Events: Ventura County 17-0 (Winner + Innovation in Control/nVent); Orange County 16-1 (Winner + Industrial Design); CA Southern State Champ 17-0 (DCMP Winner + Innovation in Control); Daly Division 15-0 (Div Winner + Excellence in Engineering/Littelfuse); Einstein 5-1 (Championship Winner). Captain of Alliance 1 at all events. Sponsors: fabworks./Gene Haas/DoD STEM/Google/WCP.

## [2026-06-14] lint-fix | index source-counts, PX4 version, source frontmatter
- **#1** Synced **83** entity catalog `(N sources)` lines in [index.md](index.md) to entity frontmatter (source of truth); fixed 2 verified frontmatter undercounts from today's ingests ([jetson-examples](entities/jetson-examples.md) 2→3, [ultralytics-yolo](entities/ultralytics-yolo.md) 1→2). Remaining index/frontmatter mismatches: 0.
- **#2** Replaced stale "v1.16 stable / v1.17 alpha" with **v1.17.0 stable (2026-05-13)** on both PX4 index lines (entity + docs-source description).
- **#3** Removed off-schema `created:`/`updated:` from **66** source-page frontmatters (schema: sources use `published`+`ingested`). 3 of those used `created` as their only date (GitHub repos) → restored as `published:` ([rosetta-github](sources/rosetta-github.md), [lerobot-ros-github](sources/lerobot-ros-github.md), [so101-ros2-readthedocs](sources/so101-ros2-readthedocs.md)) rather than dropping the date.
- Not fixed (out of scope / pre-existing): 6 source pages have only `ingested` and no publish date (farama-projects-page, gymnasium-robotics-docs, hermes-agent-github, lekiwi-github, nvidia-nemoclaw-page, openclaw-github); 4 historical `openclaw-personal-ai.md` links in this log (append-only record of a rename).

## [2026-06-14] ingest | The Blue Alliance (homepage)
- Created [The Blue Alliance (homepage)](sources/the-blue-alliance-homepage.md) (fetched via curl + browser UA; TBA 403s WebFetch)
- New entity: [The Blue Alliance](entities/the-blue-alliance.md) — open-source volunteer FRC data platform (teams/results/match video/GameDay webcasts/public API/myTBA + Android+iOS apps); wiki's authoritative FRC results source
- Cross-linked [tba-team-4414-2026 source](sources/tba-team-4414-2026.md) + [FIRST Robotics Competition](entities/first-robotics-competition.md) (4→5 sources)
- Updated [index.md](index.md) (new source + entity)
- Note: a dedicated TBA API ingest would be the next step if the wiki starts pulling FRC data programmatically.

## [2026-07-04] ingest | Five-paper batch: GR00T N1, Kober RL survey, TD-MPC, Motion Generation survey, VQ-BeT (deepened)
Ran five parallel PDF extractions (pypdf/Read; pdftotext broken in this env) over new `raw/` arrivals + two git-LFS-materialized book binaries.
- **GR00T N1** — created [GR00T N1 Paper](sources/groot-n1-paper.md) (NVIDIA GEAR, arXiv 2503.14734; the primary source the 16-source [GR00T entity](entities/nvidia-groot.md) had been missing). Dual-system VLA (Eagle-2 VLM @10 Hz + flow-matching DiT @120 Hz, 2.2B params); data pyramid (8,375.7 h corpus; 88 h GR-1 teleop → 827 h neural trajectories ~10×); real GR-1 76.8% vs DP 46.4%; catastrophic-forgetting case. Updated [nvidia-groot](entities/nvidia-groot.md) (15→16, removed stub caveat), [fourier-gr-1](entities/fourier-gr-1.md) (1→2, de-stubbed), [nvidia-gear](entities/nvidia-gear.md) (3→4), [jim-fan](entities/jim-fan.md) (3→4), [yuke-zhu](entities/yuke-zhu.md) (5→6), [joel-jang](entities/joel-jang.md) (1→2), [robocasa](entities/robocasa.md) (6→7), [mimicgen](entities/mimicgen.md) (2→3, added DexMimicGen), [open-x-embodiment](entities/open-x-embodiment.md) (0→1), [lerobot](entities/lerobot.md) (15→16, dataset-format extension).
- **Kober RL survey** — created [Kober, Bagnell & Peters 2013](sources/kober-rl-robotics-survey-2013.md) (IJRR canonical pre-deep-learning RL-in-robotics survey; four curses; policy-search-over-value-functions; ball-in-a-cup; aged-well/poorly assessment). Cross-linked [imitation-learning](concepts/learning/imitation-learning.md) (37→40), [sim-to-real-transfer](concepts/learning/sim-to-real-transfer.md) (15→16, simulation-bias lineage), [optimal-control](concepts/robotics/optimal-control.md) (9→12).
- **TD-MPC** — created [TD-MPC Paper](sources/td-mpc-paper.md) (Hansen et al., ICML 2022; original TOLD + MPPI + terminal value; first DMControl Dog solve; 16× vs LOOP). Fills the TD-MPC1 gap behind [TD-MPC2](sources/td-mpc2-paper.md). Updated [td-mpc entity](entities/td-mpc.md) (3→4, added TD-MPC1 mechanics + JEPA-adjacency note), [world-model](concepts/world-models/world-model.md) (18→19), cross-ref from TD-MPC2 page.
- **Motion Generation survey** — created [The State of Robot Motion Generation](sources/state-of-robot-motion-generation-2024.md) (Bekris et al., Rutgers, arXiv 2410.12172; explicit-vs-implicit-model divide; integration-not-supersession). New concept pages [motion-planning](concepts/robotics/motion-planning.md) + [task-and-motion-planning](concepts/robotics/task-and-motion-planning.md) — first structured wiki coverage of the classical stack. Cross-linked [optimal-control](concepts/robotics/optimal-control.md) + [imitation-learning](concepts/learning/imitation-learning.md).
- **VQ-BeT** — deepened [VQ-BeT Paper](sources/vq-bet-paper.md) from abstract-level to full-body (resolved all 4 flagged open questions: N_q=2 RVQ, 8–16 codes/layer, MinGPT 6/6/120, full benchmark tables, 5×/25× speed, Stretch DP-fails-0/30 finding). Updated [vq-bet entity](entities/vq-bet.md) with residual-VQ mechanics + anti-chunking finding.
- Added `local_path` to [diffusion-policy-paper](sources/diffusion-policy-paper.md) (full PDF now in `raw/`); Sutton & Barto binary (already ingested) needs no wiki change.
- Updated [index.md](index.md): 4 new sources (chronological) + Kober (foundational) + 2 new concepts + entity/concept count bumps.

## [2026-07-04] ingest | GR00T version line: N1.5 + N1.6 research pages + Isaac-GR00T repo
Follow-up to the GR00T N1 paper ingest earlier today; fleshes out the full version history + resolves the [GR00T entity](entities/nvidia-groot.md)'s "N1.6 vs N1.7 version-overlap" warning.
- Created [GR00T N1.5 research page](sources/groot-n1_5.md) (2025-06-11; frozen Eagle 2.5 VLM + simplified adapter + **FLARE** loss + DreamGen neural trajectories; real GR-1 language-following 46.6%→93.3%, success 43.3%→83.0%; Unitree G1 seen 98.8% / novel 84.2%).
- Created [GR00T N1.6 research page](sources/groot-n1_6.md) (2025-12-15; internal **Cosmos-2B** reasoning-integrated VLM; DiT 16→32 layers; adapter removed + top-4 VLM layers unfrozen; state-relative action chunks; +YAM/AGIBot Genie1/Galaxea R1 Pro/Unitree G1 loco-manip data; no published numbers).
- Created [Isaac-GR00T GitHub](sources/isaac-gr00t-github.md) (Apache-2.0 code / NVIDIA Open Model License weights, ~7.5k★; current default **N1.7 EA** = Cosmos-Reason2-2B/Qwen3-VL + 20K-hr EgoScale; N1.5/N1.6 on release branches; LeRobot-v2 + modality.json; embodiment tags incl. NEW_EMBODIMENT + UNITREE_G1_SONIC; Jetson Thor/Orin + DGX Spark; PyTorch 2.7 + flash-attn 2.7.4 + uv).
- Major rewrite of [nvidia-groot](entities/nvidia-groot.md) (16→19): added a 4-row version table (backbone progression Eagle→Cosmos-2B→Cosmos-Reason2-2B), per-version detail, a Codebase section, and **resolved the version-overlap warning** (N1.6 = last stable, N1.7 EA = current early-access default).
- Updated [nvidia-cosmos](entities/nvidia-cosmos.md) (12→14; Cosmos-as-GR00T-backbone section), **de-stubbed [unitree-g1](entities/unitree-g1.md)** (0→3; now the GR00T cross-embodiment/whole-body target), [lerobot](entities/lerobot.md) (16→17; N1.7 consumes LeRobot v2).
- Updated [vla-models concept](concepts/learning/vla-models.md) (33→36; version-line + frozen-VLM data point) and [index.md](index.md).

## [2026-07-04] lint | Post-ingest health check + 6 count-mismatch fixes
- Ran full lint: **0 broken links** (7,175 checked), **0 orphan pages**, every `sources/` page linked from index.
- Fixed **6** index/frontmatter source-count mismatches (all pre-existing, none from today's ingests), using distinct linked-citing-source-pages as ground truth:
  - [apptronik-apollo](entities/apptronik-apollo.md) index 5→**0** (general-knowledge stub; no source pages cite it — the "Apollo" hits in skynet/constitution sources are Apollo *Research*, not Apptronik).
  - [tonypi](entities/tonypi.md) index 2→**0** (no citing sources).
  - [dobb-e](entities/dobb-e.md) 2/3→**4** (frontmatter 3→4; +VQ-BeT + Stretch-4-launch to Mentioned-in).
  - [grievous](entities/grievous.md) index 1→**3** (+SmolVLA + Mobile-ALOHA-project to Mentioned-in).
  - [ollama](entities/ollama.md) 1/2→**5** (frontmatter 2→5; +seeed-jetson-examples + hermes-agent ×2).
  - [pi-zero-6](entities/pi-zero-6.md) index 0→**2** (added missing Mentioned-in section: so101-ros2 + rosetta).
- Created [backlog.md](backlog.md) for deferred items + knowledge gaps (DreamGen/FLARE/Eagle entities; RL hub page; robot-RL-lineage synthesis; stale `_stub_` markers). Linked from [index.md](index.md).

## [2026-07-04] ingest | GR00T dependency cluster: DreamGen + FLARE + Eagle/Eagle 2.5 (backlog gap-fill)
Ingested 4 new PDFs (dreamgen_2505.12705, FLARE_2505.15659, EAGLE_2408.15998, EAGLE_2.5_2504.15271) — the exact backlog gaps flagged in [backlog.md](backlog.md). All three are internal dependencies of GR00T papers already in the wiki. Cleared the stale [ingest_these_urls.txt](../raw/ingest_these_urls.txt) queue (all 3 URLs already ingested).
- **DreamGen** — created [source](sources/dreamgen-paper.md) + [entity](entities/dreamgen.md). NVIDIA GEAR method turning image-to-video models into synthetic robot-data generators ("neural trajectories"); 4-stage pipeline; behavior gen 11.2%→43.2%, env gen 0%→28.5%; DreamGen Bench. The root of the Dream\* line + the neural-trajectory layer of the GR00T data pyramid. Note: DreamGen v2 references GR00T N1 only (not N1.5); no DreamZero/DreamDojo mention.
- **FLARE** — created [source](sources/flare-paper.md) + [concept](concepts/world-models/flare.md). Future LAtent REpresentation Alignment; JEPA-adjacent auxiliary loss (future-token alignment to an EMA future-observation embedding, λ=0.2). **The auxiliary loss GR00T N1.5 adopts.** Up to +26%; human-video co-training doubles novel-object success.
- **Eagle** — created [entity](entities/eagle-vlm.md) + [Eagle-1 source](sources/eagle-paper.md) (ICLR 2025, mixture-of-encoders/channel-concat) + [Eagle 2.5 source](sources/eagle-2-5-paper.md) (long-context, single SigLIP-so400M). The GR00T VLM backbone through N1.5. ⚠️ Neither Eagle paper mentions GR00T — backbone claim sourced from GR00T pages; GR00T N1 uses the *Eagle-2* production model (no standalone paper), Eagle-1 is the research study.
- Cross-links: updated [groot entity](entities/nvidia-groot.md) (Eagle/DreamGen/FLARE links in version table + Related), [groot-n1-paper](sources/groot-n1-paper.md) (Eagle-2), [groot-n1_5](sources/groot-n1_5.md) (all 3 now filed; struck open questions), [nvidia-gear](entities/nvidia-gear.md) 4→6, [joel-jang](entities/joel-jang.md) 2→4 (**confirmed DreamGen co-first author**), [jepa](concepts/world-models/jepa.md) 23→24, [world-model](concepts/world-models/world-model.md) 19→20, [world-model-simulators](concepts/world-models/world-model-simulators.md) 13→14, [vla-jepa](entities/vla-jepa.md) (FLARE = closest analogue).
- Backlog: struck DreamGen/FLARE/Eagle gaps; added **concept-subdir count-audit** item (the prior lint's regex missed `concepts/*/*.md` counts — jepa was stale at index 15 vs frontmatter 23).

## [2026-07-04] ingest | Gemma 4 edge blog + NemoClaw Hermes quickstart + new deployment-topology synthesis
- Created [Gemma 4 edge blog source](sources/nvidia-gemma-4-edge-blog.md) + [Gemma 4 entity](entities/gemma4.md) — Google's 2026 multimodal family; first MoE Gemma; 4 variants (E2B/E4B multimodal on Jetson Orin Nano → 31B on DGX Spark, NVFP4); vLLM/Ollama/llama.cpp/NIM; explicit physical-AI/on-device framing. Linked [gemma3](entities/gemma3.md) (successor), [dgx-spark](entities/dgx-spark.md) 4→5, [ollama](entities/ollama.md).
- Created [NemoClaw Hermes quickstart source](sources/nvidia-nemoclaw-hermes-quickstart.md) — `nemohermes` runs Hermes as a NemoClaw agent variant in an OpenShell sandbox (dashboard 18789 / OpenAI API 8642; default `nemotron-3-super-120b-a12b` via NVIDIA endpoints; network-policy tiers). Deepened [hermes-agent](entities/hermes-agent.md) 2→3 + [nemoclaw](entities/nemoclaw.md) 1→2 (resolved OpenShell-policy + Nemotron-model open questions).
- **New topic** ([user request]): [Where the compute lives — agents on the robot vs on a local AI server](syntheses/agents/on-device-and-on-robot-agents.md). Deployment-topology angle (on-robot edge / local AI server / cloud), the split-brain pattern, the model-fits-hardware ladder, privacy/latency/cost drivers. Complements the existing framework ([openclaw-vs-hermes](syntheses/agents/openclaw-vs-hermes-as-robot-brain.md)) + shape ([across-stacks](syntheses/agents/llm-agent-architecture-across-stacks.md)) syntheses. Linked from [llm-agent-architecture concept](concepts/agents/llm-agent-architecture.md).
- **Note — duplicate raw PDF NOT committed**: `raw/xlerobot_cutting_the_cord_2603.09051v1.pdf` (dropped this session) is byte-identical to the already-tracked `raw/2603.09051v1.pdf` (arxiv 2603.09051v1); the [Cutting the Cord source](sources/cutting-the-cord-untethered-xlerobot.md) is already a full ingest with `local_path` set. Left the untracked duplicate un-added to avoid a redundant ~20 MB LFS blob; awaiting user decision on whether to rename/replace.

## [2026-07-04] ingest | 2 PDFs (SONIC, Gemini Robotics 1.5) + 5 URLs (YAM, Galaxea R1, Awesome-list, GR00T-WBC, Standard Bots)
Large batch; several fill backlog gaps. Removed a byte-identical duplicate `raw/xlerobot_cutting_the_cord_2603.09051v1.pdf` (paper already ingested).
- **SONIC / GEAR-SONIC** — [source](sources/sonic-paper.md) + [entity](entities/gear-sonic.md) (arXiv 2511.07820, NVIDIA GEAR). Humanoid whole-body controller = the `UNITREE_G1_SONIC` controller; motion-tracking-as-scaling-task PPO (42M/611h mocap); 99.6% success, 41% MPJPE cut, 99.2% sim-to-real on Unitree G1; FSQ universal-token interface a GR00T N1.5 VLA drives (loco-manip 5-task avg 75%). The [nvlabs.github.io/GR00T-WholeBodyControl](https://nvlabs.github.io/GR00T-WholeBodyControl/) project page = same work. **Resolves the GEAR-SONIC backlog item.**
- **Gemini Robotics 1.5** — [source](sources/gemini-robotics-1-5-report.md); deepened [gemini-robotics entity](entities/gemini-robotics.md) 2→3 (first deep DeepMind-robotics source). GR 1.5 VLA (one checkpoint across ALOHA/Franka/Apollo) + GR-ER 1.5 orchestrator on Gemini 2.5; Motion Transfer, Embodied Thinking, agentic orchestration (failure 22% vs 44.5%), ASIMOV-2.0. Resolved its "primary source not ingested" open question; bumped [apptronik-apollo](entities/apptronik-apollo.md) 0→1.
- **YAM** — [source](sources/i2rt-yam-docs.md) + [entity](entities/yam.md). i2RT 6-DOF CAN-bus data-collection arm ($2,999–$4,999); bimanual YAM = a GR00T N1.6 teleop source. **Resolves YAM backlog item.**
- **Galaxea R1** — [source](sources/galaxea-r1-user-guide.md) + [entity](entities/galaxea-r1.md). Wheeled dual-arm humanoid (24 DOF); sim R1 Pro on BEHAVIOR = a GR00T N1.6 embodiment. **Resolves Galaxea backlog item.**
- **Standard Bots** — [source](sources/standardbots-ai-page.md) + [entity](entities/standard-bots.md). US industrial arm maker; self-serve learn-by-demonstration; the commercial/industrial IL counterpoint.
- **Awesome-Embodied-Robotics-and-Agent** — [source](sources/awesome-embodied-robotics-agent.md) (reference/curated list). Coverage cross-check; flags VLN + household-simulator gaps.
- Cross-links: [nvidia-groot](entities/nvidia-groot.md) (SONIC in N1.7), [groot-n1_6](sources/groot-n1_6.md) (YAM/Galaxea/SONIC linked), [unitree-g1](entities/unitree-g1.md) 3→4 (SONIC), [nvidia-gear](entities/nvidia-gear.md) 6→7 (SONIC).

## [2026-07-04] query+synthesis | "General agentic control framework across my robot fleet"
- Query: one framework across XLeRobot + LeKiwi (both Jetson Orin NX 16 GB) + ROSOrin Pro (Orin Nano Super 8 GB) + DGX Spark hub; ROS 2 + LeRobot integrated; demo→HF→train-on-Spark flywheel; master-control coordination; STT/TTS; Gemma 4 family.
- Filed [Fleet agentic control framework](syntheses/projects/fleet-agentic-framework.md) — three-layer reference architecture (ROS 2 + LeRobot policy via [Rosetta](entities/rosetta.md) / on-edge Gemma-4-E4B agent / DGX Spark master), the ROS 2↔MCP server as the key DIY piece, central-MCP-then-A2A coordination, Gemma 4 model-placement table, HF data flywheel + HIL-SERL, and a 7-step de-risking ladder. Key updates from the fleet's hardware: the planned **Orin NX 16 GB on LeKiwi** makes all 3 robots first-class CUDA policy nodes and retires the Hailo-can't-run-policies blocker; XLeRobot + LeKiwi are LeRobot-native (FeeTech STS3215 + SO-ARM101), ROSOrin Pro is the ROS 2-native / HX-12H outlier.
- Synthesized from: [on-device/on-robot agents](syntheses/agents/on-device-and-on-robot-agents.md), [llm-agent-across-stacks](syntheses/agents/llm-agent-architecture-across-stacks.md), [llm-agent concept](concepts/agents/llm-agent-architecture.md), [lerobot-on-rosorin-pro](syntheses/projects/lerobot-on-rosorin-pro.md), [Hailo](entities/hailo.md), [Cutting the Cord](sources/cutting-the-cord-untethered-xlerobot.md), [Gemma 4](entities/gemma4.md). Cross-linked from those pages + index Projects.

## [2026-07-04] synthesis | Fleet framework — implementation notes (MCP schema + Spark scheduled training)
- Filed [Fleet framework — implementation notes](syntheses/projects/fleet-framework-implementation-notes.md), the code-level appendix to the [fleet framework](syntheses/projects/fleet-agentic-framework.md): (1) concrete **MCP tool schema** for the SO-ARM101 robots — tool catalog + full JSON `tools/list` entries (pick_object / navigate_to / list_visible_objects) + uniform `{status,reason,observation}` return envelope + out-of-band stop + per-embodiment YAML config + worked trace; (2) **scheduled training on the DGX Spark** — systemd timer/service units, `train_fleet.sh` with a promotion gate, cross-embodiment co-train (XLeRobot+LeKiwi share SO-ARM101), HIL-SERL minimal-human loop, gotchas. Cross-linked from the parent synthesis + index Projects.

## [2026-07-04] decision | Arm-swap homogenization — SO-ARM101 onto the ROSOrin Pro
- Fleet owner opts to replace the ROSOrin Pro's HX-12H arm with an [SO-ARM101](entities/so-arm101.md) → all three fleet robots share one arm → **one shared policy**, no cross-embodiment problem; ROSOrin Pro becomes LeRobot-native (keeps its Nav2/SLAM base).
- Added owner's reach-comparison photo → `raw/assets/so-101-vs-rosorin-pro-reach.jpeg` (SO-101 vs ROSOrin Pro, arms extended; reach parity; SO-101 5-DOF matches XLeRobot/LeKiwi). Referenced from the [fleet synthesis](syntheses/projects/fleet-agentic-framework.md).
- Updated [fleet framework synthesis](syntheses/projects/fleet-agentic-framework.md) (table row, arm-swap decision callout with photo, integration-classes section, cross-embodiment gap → "designed out", build-ladder step 5), [implementation notes](syntheses/projects/fleet-framework-implementation-notes.md) (co-train one fleet policy), [rosorin-pro entity](entities/rosorin-pro.md) (mecanum-variant correction + arm-swap note), [lerobot-on-rosorin-pro plan](syntheses/projects/lerobot-on-rosorin-pro.md) (arm-swap sidestep callout), and struck the [backlog](backlog.md) cross-embodiment item.
- **Correction**: owner's ROSOrin Pro chassis is **mecanum/holonomic**, not the differential-drive the entity listed — a variant SKU exists; annotated on the entity.

## [2026-07-04] refine | Camera-parity spec + single-vs-dual-arm checkpoint correction
- Added a **Camera parity spec** section to the [fleet implementation notes](syntheses/projects/fleet-framework-implementation-notes.md): the wrist-per-arm + one-front-cam layout table, the six fleet-wide lock parameters (same hardware, res/fps, retire Aurora930 from the policy, identical wrist mount, standardized front-cam placement, RGB-only), and the wrist-cam-as-parity-anchor design lever.
- **Corrected the "one shared policy" overclaim** (surfaced by the camera-parity question): XLeRobot is dual-arm → **two checkpoints**, `soarm_tidy_single` (LeKiwi + ROSOrin, shared) + `soarm_tidy_dualarm` (XLeRobot, co-trainable), from two datasets (single- vs dual-arm action dims differ). Fixed the arm-swap callout, cross-embodiment gap, build-ladder step 5, MCP config examples, the cross-embodiment-shortcut section, and the `train_fleet.sh` loop (per-checkpoint dataset map) in both fleet pages.

## [2026-07-04] lint-fix | Concept count sync + stale-stub cleanup + BEHAVIOR stub
- **Concept count drift (10) resolved** — synced both index catalog counts *and* frontmatter `sources:` to ground truth (distinct citing source pages), since both were stale: llm-agent-architecture→28, latent-space→18, ai-safety-alignment→8, scaling-laws-vla→8, agentic-uavs→7, assistive-robotics→22, siamese-network→8, biomechanical-simulation→7, energy-based-models→4 (fm was over), connectome→3 (fm was over). Clears the concept-subdir audit backlog item; **0 catalog mismatches remain**.
- **Dropped 5 stale `_stub_` markers** (ollama, mila, joel-jang, grievous, mimicgen — all 20–42-line pages with 3–5 sections + 3–5 citing sources, not stubs); removed `status: stub` frontmatter from mila + mimicgen.
- **Filed [BEHAVIOR / BEHAVIOR-1K](entities/behavior-benchmark.md) stub** (the top mentioned-no-page gap) — Stanford's 1,000-task household benchmark; the 12.4%-vs-89.4% sim-to-real yardstick + a GR00T N1.6 sim substrate. Backed by 2 citing sources ([stanford-hai](sources/stanford-hai-ai-index-2026.md), [groot-n1_6](sources/groot-n1_6.md)); cross-linked from [sim-to-real](concepts/learning/sim-to-real-transfer.md) + index. Backlog item struck.
- Lint otherwise clean: 0 broken links (7,573), 0 orphans, full index source coverage, no real wikilinks. Remaining backlog gaps (Nemotron, DreamZero, OpenShell, Whisper/sherpa-onnx, AI2-THOR/iGibson/VLN) left as future ingests.

## [2026-07-04] correction | XLeRobot base = 2-wheel differential (owner build)
- Owner's XLeRobot uses a **2-wheel differential** base (non-holonomic), not the LeKiwi 3-wheel omni base the entity intro implies (the entity already lists a 2-wheel variant). Now the fleet has three different base drives (XLeRobot diff / LeKiwi Kiwi / ROSOrin mecanum) — irrelevant to the shared policy (Nav2 layer), relevant only to pre-grasp positioning (differential = turn-then-approach vs holonomic strafe).
- Added owner photo → `raw/assets/xlerobot-owner-diff-drive.jpeg` (2 SO-ARM101 + 2 wrist cams + mast head cam already matching the camera-parity layout; 2 driven front wheels visible). Referenced from the [fleet synthesis](syntheses/projects/fleet-agentic-framework.md).
- Fixed the [fleet synthesis](syntheses/projects/fleet-agentic-framework.md) table (XLeRobot base → "2-wheel differential") + added a base-drives note; annotated the [XLeRobot entity](entities/xlerobot.md).

## [2026-07-04] ingest | BEHAVIOR-1K paper + OmniGibson
- Created [BEHAVIOR-1K Paper](sources/behavior-1k-paper.md) (arXiv 2403.09227, CoRL 2022, Stanford) — 1,000 survey-grounded household activities (1,461 respondents) / 50 scenes / 9,000+ objects; **BDDL** task language; baselines showing end-to-end RL 0.0, primitives 0.42–0.88, real-robot (TIAGo) 0–22%; the empirical basis for the sim-to-real gap.
- **Upgraded [BEHAVIOR entity](entities/behavior-benchmark.md)** stub→full (2→3 sources; corrected 5,000→9,000+ objects; distinguished the paper's 0–22% baselines from the AI-Index 12.4% Challenge number).
- Created [OmniGibson entity](entities/omnigibson.md) — Stanford's Omniverse + PhysX 5 sim (deformables + fluids + extended states, Transition Machine, OpenAI Gym; realism 3.20 vs Habitat/AI2-THOR/iGibson ~1.7); tracks the user's [`BIT-PIE/OmniGibson`](https://github.com/BIT-PIE/OmniGibson) fork (MIT, v1.1.0 Oct 2024). Sourced from the web (BEHAVIOR-1K paper arXiv HTML + BIT-PIE repo).
- Cross-linked [sim-to-real](concepts/learning/sim-to-real-transfer.md) (16→17), [roberto-martin-martin](entities/roberto-martin-martin.md) (1→2, co-author), index (source + OmniGibson entity + de-stubbed BEHAVIOR). Struck the BEHAVIOR backlog item; iGibson/AI2-THOR/Habitat + a standalone OmniGibson repo ingest remain open.

## [2026-07-04] ingest | OmniGibson dedicated codebase (BIT-PIE fork)
- Created [OmniGibson GitHub codebase ingest](sources/omnigibson-github.md) from the user's [`BIT-PIE/OmniGibson`](https://github.com/BIT-PIE/OmniGibson) fork (MIT, v1.1.0) + upstream docs. Pins: **requires Isaac Sim 4.1.0** (`isaacsim-for-omnigibson` pip); OpenAI Gym; **14 robots** (mobile: Turtlebot/Locobot/Husky/Freight; manipulation: Franka/VX300S/A1/Franka-Mounted; mobile-manip: Fetch/Tiago/Stretch/R1/R1Pro; VR: BehaviorRobot); controllers (diff-drive/holonomic/IK/gripper); ships 1,004 BEHAVIOR-1K tasks + 50 scenes.
- **Loop closed**: OmniGibson's **R1/R1Pro = the [Galaxea R1](entities/galaxea-r1.md)** → GR00T N1.6's "simulated Galaxea R1 Pro on BEHAVIOR" is the OmniGibson R1Pro running BEHAVIOR-1K. Cross-linked galaxea-r1 (2→3), completed the [OmniGibson entity](entities/omnigibson.md) (1→2; full robot roster + Isaac Sim 4.1.0), index/backlog.
- Web-sourced (BIT-PIE repo + behavior.stanford.edu/omnigibson docs); resolved the entity's robot-list/Isaac-Sim-version open questions.

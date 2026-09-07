---
title: "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models (Zhang et al., 2025/2026)"
type: source
url: https://arxiv.org/abs/2512.11908
fetch_url: https://arxiv.org/pdf/2512.11908v2
local_path: raw/2512.11908v2.pdf
sha256: ff2d6331247a93b78323050f46a6bc9f0f927267bbc362b78e5cb4a0515a0c4a
author: "Heng Zhang, Rui Dai, Gokhan Solak, Pokuang Zhou, Nikos Tsagarakis, Yu She, Arash Ajoudani (IIT HRII + HHCM labs, Genova; Università di Genova / DRIM; Purdue Edwardson School of IE)"
published: 2025-12-10
venue: "arXiv preprint (v1 2025-12-10; **v2 2026-01-26**, the version read here), 68 pp., cs.RO"
format: survey (PDF/HTML, ~400 references)
tags: [contact-rich-manipulation, safe-learning, safe-rl, impedance-control, control-barrier-functions, reachability, passivity, tactile-sensing, vla, safety, iso-ts-15066, survey, physical-hri]
ingested: 2026-09-07
---

## Summary

**The wiki's first survey of the physical half of robot safety** — the tradition that was already mature when [semantic safety](../concepts/safety/semantic-safety.md) was invented, and that this wiki had covered only through three individual filter papers. Zhang et al. review ~400 works (2018–2025) on learning-based control for **contact-rich** tasks under the organizing question of how safety is *formulated, enforced, and evaluated*, and split the field on one axis: **safe exploration** (don't break anything while learning) versus **safe execution** (don't break anything while deployed). A third block covers the certificate families — Lyapunov, [control barrier functions, contraction metrics, reachability](../concepts/robotics/safety-certificates.md) — that both phases draw on.

The stated differentiator is the [VLM/VLA](../concepts/learning/vla-models.md) material, and that is also its weakest section (see the caveat below). What the survey delivers unambiguously is the **operational definition of the task class**, the **taxonomy of where safety gets enforced** (abstraction level × enforcement space), a **structural argument about contact data that bears directly on VLA scaling**, and a set of **evaluation conventions** the wiki can steal.

Its practical recommendation, repeated in five sections and named in the Outlook, is a layered stack: **plan → parameterize → enforce**, or in its longer form *"plan–learn–filter–execute."* A semantic layer proposes; a learned policy emits **pose / force / impedance references** rather than torques; a certified low-level layer projects whatever comes out onto the admissible set.

> [!note] Version and authorship bookkeeping
> Read at **v2** (2026-01-26), which rewrites the abstract to claim priority — *"the first safety-centric survey that places safety at the core of learning for contact-rich robotic tasks"* — where v1 said only *"a comprehensive overview."* The v2 PDF's own author list includes **Nikos Tsagarakis**; the arXiv listing metadata does not, and still shows the six-author v1 list. The PDF is the version cited here.

## The definition, which is narrower than the wiki has been using

> A task is **contact-rich** when its successful execution requires **dynamic and sustained physical contact** with the environment, where **motion and force are tightly coupled through contact constraints**.

The exclusions are what make it useful, and they are stated explicitly (§2.1):

- **Obstacle avoidance** is not contact-rich — the task is achievable without contact at all.
- **Simple pick-and-place is not contact-rich** — the contacts are *fixed* after the grasp.
- **Throwing, hitting, catching** are not contact-rich — the contact is momentary, not extended. Dynamic ≠ contact-rich.
- **In-hand manipulation and tool use are**, because the contacts move.

> [!warning] This disqualifies most of the manipulation benchmarks in this wiki
> LIBERO, most of RoboCasa, and the bulk of the pick-and-place tasks behind the [VLA success-rate tables](../syntheses/platforms/vla-success-rate-audit.md) are, by this definition, **not contact-rich** — the grasp closes and the contact set stops changing. That is not a criticism of those benchmarks; it is a boundary. It means the entire literature this wiki tracks on generalist manipulation policies has been evaluated almost entirely *outside* the regime where force control, compliance, and physical-safety guarantees are load-bearing. See [contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md).

The four task categories it sorts the literature into: **assembly/insertion** (most common by count), **surface interaction** (polishing, grinding, wiping, stirring — split into *surface-altering*, *non-altering*, and *particle interaction*), **object manipulation** (prehensile/non-prehensile; constrained, articulated, deformable), and **physical HRI**.

## Six axes for comparing safety methods

§3.1.1 introduces a comparison frame (rendered as hexagonal radar plots, Fig. 4) that is the most portable thing in the survey, precisely because the authors admit *why* they needed it: **"the literature lacks a unified benchmark that evaluates different safety paradigms on the same contact-rich task under matched conditions,"** so the comparison is *synthesis-based* rather than measured.

| Axis | Question |
|---|---|
| **A1** Guarantee strength | hard invariance/reachability → probabilistic → empirical |
| **A2** Model independence | requires accurate model → black-box / learned |
| **A3** Online efficiency | heavy online optimization → lightweight runtime (compute pushed offline) |
| **A4** Conservatism / tunability | worst-case with no knobs → explicitly risk-tunable |
| **A5** Scalability / real-time viability | fails in high-dim contact → scales and runs real-time |
| **A6** Data efficiency | data-hungry → little data needed to be safe |

The recurring trade-off it reports: **guarantee strength buys itself with adaptability and compute**. Reachability safeguards give the hardest runtime behavior and the most predictable cost (everything precomputed) but degrade under model mismatch; CBF/MPC shields adapt but pay online optimization and go infeasible in high dimensions; learned compliant skills adapt best and have the weakest guarantees.

> [!warning] The axis the survey does not have
> A1–A6 contains **no axis for what the filter costs the policy it wraps**. This wiki's [safety-filters](../concepts/robotics/safety-filters.md) page has the measurement the survey lacks: on identical constraints and hardware, a CBF filter drops a diffusion policy to **0.04** task success where a path-consistent reachability filter holds **0.72** ([PACS](pacs-paper.md), ICRA 2026 — postdates v2). By A1 those two methods are near-equivalent. **The survey's framework cannot see an 18× difference in outcome**, because it evaluates filters as controllers rather than as interventions on a learned distribution.

## The contact-data argument, which is the most consequential claim here

§3.4 states it plainly, and it is a structural claim about scaling rather than an observation about current datasets:

> Unlike the vast text and image corpora scraped from the Internet to train LLMs and VLAs, **physical interaction data — specifically high-fidelity contact forces, torques, and safety-critical failure modes — cannot be obtained from the web.** This scarcity of contact data in foundation models creates a significant gap in their ability to reason about physical dynamics and safety.

The **data pyramid** (Fig. 6) makes the ordering explicit: internet/shared datasets at the base (abundant, only indirectly about contact), simulation in the middle (contact under controllable but imperfect dynamics), **real-world contact data at the apex — scarce and irreplaceable**, ordered *within* the layer from generic execution logs up to explicit failure and near-miss cases.

What this predicts, and what §4.6 confirms as the current state: public datasets rarely contain **(i)** high-frequency wrench traces aligned with failure annotations, **(ii)** near-miss episodes, or **(iii)** semantic safety labels (forbidden regions, fragile surfaces). Note that **(ii) and (iii) are exactly the two things the whole "plan–learn–filter" architecture consumes.**

This is the sharpest available answer to a question the wiki keeps circling from the video-pretraining side — [what a video-trained world model cannot learn](../concepts/world-models/world-model-evaluation.md), and whether the [synthetic-data flywheel](../concepts/learning/synthetic-data-flywheel.md) reaches everything. **Force is not recoverable from pixels.** No amount of internet video, and no generative video model trained on it, produces a wrench trace.

## Sensing: the modality table

Table 1 tallies which modality the reviewed policies actually consume. The distribution is itself the finding — **force/torque dominates by a very wide margin** (≈60 works listed), vision is second (≈30), and **natural language appears in exactly four**.

| Modality | Safety leverage | Count in table |
|---|---|---|
| Proprioceptive/kinematic only | contact reasoning from configuration; conservative motion | ~11 |
| **Force/torque** | real-time force & impedance limits, slip detection, compliant correction | **~60** |
| Vision | contact evaluation, feature localization, global context | ~30 |
| **Language** | LMM interprets instruction, then checks internal low-level safety | **4** |
| Tactile | contact localization, pressure distribution, incipient slip | 5 |
| Multimodal fusion | precision under occlusion | ~20 |

Read against the survey's own framing, this is a quiet contradiction of its headline: a survey whose stated emphasis is VLM/VLA safety finds **four** language-conditioned works in a corpus of ~400, three of which it cites for the VLA sections everywhere else. See [tactile sensing](../concepts/robotics/tactile-sensing.md) for the touch column, which is where the newest work is.

## Where safety gets enforced: two orthogonal taxonomies

The survey's most reusable structure is that it separates **abstraction level** (§3.7) from **enforcement space** (§3.8). These are independent, and most papers pick one cell of each without saying so.

**Abstraction level** — high-level planning (symbolic/HRL/logic, now LLM/VLM planners; interpretable, poor reactivity to contact) · low-level control (impedance learning, CBFs, MPSF, robust/adaptive; reactive, no task semantics) · end-to-end (safety as regularizer or safety critic inside one model; scalable, unverifiable) · **hybrid**, which the survey endorses.

**Enforcement space** — task space (Cartesian force/pose bounds, compliance, passivity) · joint space (torque/velocity/angle limits, self-collision, singularity) · **dual-space** (both loops; the survey's argument is that either alone leaves a blind spot — task-space control can command infeasible joint configurations, joint-space safety can miss end-effector pressure) · **policy space** (CMDP with a cost threshold, Lagrangian relaxation, safety critics, latent-space barriers for visual tasks, human-in-the-loop).

> [!note] The action-abstraction claim, and what it does to the wiki's control-level page
> The single most-repeated practical recommendation in the survey is that a learned policy should emit **pose / force targets / impedance gains, not raw torques** — because that (a) preserves passivity and stability margins by construction, (b) gives runtime safety layers an interpretable hook to modify, and (c) transfers sim-to-real better.
>
> The wiki's [control abstraction levels](../concepts/robotics/control-abstraction-levels.md) page treats abstraction level as an axis of **capability and access**. This survey adds the orthogonal claim that it is also an axis of **intrinsic safety**: level-1 raw-torque output is not merely harder for a model to do well, it removes the hooks that any physical-safety argument needs. Two independent literatures reaching the same recommendation from opposite directions.

## Evaluation conventions worth stealing

§3.6 is short and unusually practical.

- **Three objectives that conflict**: safety (violations, cost, force/accel/velocity magnitudes, stability via convergence rate or energy flow, human perceived safety), task (success rate, task reward, *progress* metrics — dressing rate, slicing progress, mass of powder ground), efficiency (energy, wall-clock, data-collection and training time, planning latency).
- **Report the trade-off, not the safety number alone.** Some works use a combined ratio (safe-and-successful over violating); others print successes and violations side-by-side; learning curves of success, violation, *and their ratio* through training are the survey's preferred display.
- Where the objectives are **physically interpretable**, they stop conflicting: force-velocity behavior, tracking error, and energy consumption are simultaneously safety, task-quality, and efficiency metrics.
- **Robustness testing**: inject noise in observation space or action space, test under disturbance, cluttered/changing backgrounds, sampled simulation parameters, non-stationary environments.

**Three levels of results analysis** (Fig. 8), proposed as a reporting convention:

| Level | Content | Buys you |
|---|---|---|
| **Global** | aggregated summary stats — max force, total violations, mean ± var tracking error | general, memorable |
| **Variational** | trends across episodes/seeds — learning curves, histograms, success-vs-violation scatter | system behavior over time/seeds |
| **Exemplar** | a single episode in detail — force traces, trajectories, video | *why* it works, and how it fails |

They recommend all three. The wiki's [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) page argues the same thing from the statistical side (a headline success rate with ~70 rollouts supports almost nothing); this is the same argument made as a presentation convention, and the **exemplar** level is the one the VLA literature almost never reports.

## Key claims

- **Safe exploration and safe execution are different problems with different tools.** Exploration is the safety-critical phase — *"naive probing causes jamming, surface damage, or tool wear"* — and its methods (reachability projection, model-predictive shielding, advantage-based intervention, safe-set construction) buy hard guarantees with conservatism. Execution is dominated by **compliant control**: impedance/admittance with learned parameters. (§3.1)
- **Compute placement is the practical selector.** Reachability filters suit *fixed platforms with stable dynamics and tight real-time budgets*; MPC/CBF suits *environments where constraints and intent change quickly and online compute is available*. (§3.1.1)
- **Lyapunov stability does not imply safety.** *"A Lyapunov-stable controller may drive a robot back to its desired equilibrium after a disturbance but still allow temporary violations of safe force or workspace limits."* Stability is about the destination; safety is about the transient. (§3.1.3)
- **CBFs are hardest exactly where contact lives**: force and contact constraints are **high relative degree** (they depend on higher derivatives of the state), which is the case CBF design handles worst. (§3.1.3)
- **RL for compliant-controller *parameters*, not actions, is the mainstream of safe execution.** Learn stiffness/damping/inertia online; keep a classical controller in the loop. (§3.1.2)
- **pHRI changes the definition of safety, not just its threshold.** Perceived safety (trust, predictability, comfort) becomes a metric — one dressing-assistance work measures it on a 7-point Likert scale — and one bathing-assistance system *deliberately downgrades its vision system to LIDAR for ethical reasons*. (§3.2.4)
- **VLM/VLA safety opportunities**: language-level constraint specification, multimodal grounding of safety signals, schema-conformant action spaces with pre-execution checks, conservative default caps. **Amplified risks**: mis-grounding force/region/tolerance constraints, hallucinated contact strategies, overconfident execution, and *"weak uncertainty estimation, making it difficult to detect when a contact-rich interaction is entering an unsafe regime."* (§2.2.6, §4.7)
- **Benchmark gap.** Existing suites under-represent deformables, multi-stage processes, tool use, and human-adjacent tasks, and **no standardized contact-force evaluation protocol exists**. (§4.6, §5.1)

## Where it is weak, and it should be said plainly

> [!warning] The foundation-model half is a position, not a review
> Three things make the VLA sections thinner than they present as:
>
> 1. **Imitation learning is excluded by design** (§1.2) — *"we deliberately exclude imitation learning methods, as their primary objective is to replicate demonstrated behaviors rather than actively managing safety."* Nearly every VLA this wiki tracks is trained by imitation. So the survey's scope excludes the dominant construction of the models its headline is about, and defers to a companion IL survey by an overlapping author set.
> 2. **The evidence base is a handful of papers cited many times.** The VLM/VLA claims rest largely on **SafeVLA** (Zhang et al. 2025, ref [23]) and **"Towards safe robot foundation models"** (Tölle et al., Peters group, ref [4]), each cited across ~10 sections, plus the authors' own **SRL-VIC**, **OmniVIC**, and **CompliantVLA-adaptor**. [SafeVLA is now ingested](safevla-paper.md) and turns out to work **outside this survey's own definition of contact-rich**, on collision costs rather than forces — so the anchor does not bear on the regime the chapter is about. Tölle et al. remains unread here. Note also that the survey cites it as *"SafeVLA"*, a name that as of the current version no longer denotes a method in that paper.
> 3. **Several foundation-model citations do not support the claim they are attached to.** Ref [26] is an *optimization-based TAMP survey*, cited repeatedly in lists framed as VLM/VLA safety. More clearly, §3.7.3 states that *"Bahl et al. [33] proposed a neural network-based approach that learns to predict safe actions directly from raw sensory inputs"* — [33] is **Neural Dynamic Policies** (NeurIPS 2020), which embeds dynamical-system structure in policy networks and is not about safety; the same reference is also cited in §2.2.1 for grounding *natural-language* force limits, which it contains nothing of. Treat the survey's foundation-model citations as leads to check, not as attributions.
>
> The control-theoretic and task-taxonomy material, by contrast, is careful and reads as first-hand.

> [!warning] "Semantic safety" is used here in a different sense than elsewhere in this wiki
> §2.2.6 defines semantic safety as **grounding task semantics and safety rules into actionable physical constraints and monitors** — compiling "do not exceed 5 N on the cable" into an enforceable force bound. The [ASIMOV / DeepMind sense](../concepts/safety/semantic-safety.md) this wiki has been carrying is **common-sense harm avoidance** — don't put the soft toy on the hot stove — which is about *goals*, not about compiling constraints.
>
> These are not the same problem. The survey's version is a **translation** problem with an enforcement layer downstream; the ASIMOV version is a **judgment** problem with no enforcement layer at all. Both are real, the term is now overloaded, and a reader who imports one paper's usage into the other's argument will get it wrong. Recorded on the concept page.

Also worth noting: the survey's own text has internal section-numbering errors (§2.3.1 forward-references "Sec. 3" for the background it just presented), and Fig. 2's illustrations of the canonical task set are **generated with ChatGPT 5.1** — noted here only because a taxonomy figure that has never been photographed is a small sign of how the field's survey layer is now assembled.

## Entities mentioned

- [Arash Ajoudani](../entities/arash-ajoudani.md) — senior author; head of HRII at IIT. [Istituto Italiano di Tecnologia](../entities/istituto-italiano-di-tecnologia.md) — HRII and HHCM labs, and the institutional home of most of the self-cited work.
- Simulators tabulated (Table 2): [MuJoCo](../entities/mujoco.md) / MJX, [Genesis](../entities/genesis.md), PyBullet, [Isaac Gym](../entities/isaac-gym.md), [Isaac Sim](../entities/nvidia-isaac-sim.md), [Isaac Lab](../entities/nvidia-isaac-lab.md), Orbit, Factory, RoboAssembly, [Drake](../entities/drake.md).
- Benchmarks tabulated (Table 3): RoboVerse, [RoboCasa](../entities/robocasa.md), [robosuite](../entities/robosuite.md), [ManiSkill](../entities/maniskill.md), Meta-World, RLBench, [Gymnasium](../entities/gymnasium.md), **Safety Gymnasium**, Robust Gymnasium, safe-control-gym — the last three being the only *safety*-specific entries, and none of them contact-force-aware.

## Concepts touched

- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — **new page**: the definition, the exclusions, and the four task categories.
- [Impedance and admittance control](../concepts/robotics/impedance-control.md) — **new page**: the workhorse of safe execution, and what "variable impedance" means as a learned action space.
- [Safety certificates](../concepts/robotics/safety-certificates.md) — **new page**: Lyapunov / CBF / contraction metrics / reachability, what each certifies, and what each costs.
- [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) — **new page**: CMDPs, Lagrangian relaxation, safety critics, recovery, shielding, safe exploration.
- [Tactile sensing](../concepts/robotics/tactile-sensing.md) — **new page**: GelSight-family vision-based tactile, what touch gives that a wrist F/T sensor cannot.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — the survey supplies the classical taxonomy; the wiki supplies the cost measurement it is missing.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — ISO 10218 and ISO/TS 15066 appear as the human-centered axis of the safety definition.
- [Semantic safety](../concepts/safety/semantic-safety.md) — the terminology collision above.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — action abstraction as a safety mechanism, not only a capability variable.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the three-level reporting convention.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) · [synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — what the contact-data argument bounds.
- [SafeVLA](safevla-paper.md) — this survey's most-cited external anchor, ingested immediately after it.

## Open questions

- **Is there any contact-force benchmark at all?** The survey says no standardized contact-force evaluation protocol exists and names it as future direction #1. If that is still true in late 2026 it is a concrete, unclaimed piece of work.
- **What does a safety filter cost a *contact-rich* policy?** The wiki's path-consistency result was measured on free-space and quasi-static tasks. In sustained contact, "brake along the intended path" and "deviate from the path" are not obviously the same distinction — braking mid-insertion can itself jam the part. **Nobody has measured this**, and the survey does not raise it.
- **Can force/torque be predicted well enough to substitute for measuring it?** The survey treats web-scale data as structurally unable to supply wrenches. Learned observers that estimate contact wrench from proprioception exist (§2.3.1) — how far do they close the gap, and is a *predicted* wrench admissible in a safety argument?
- **CompliantVLA-adaptor** (ref [5], arXiv 2601.15541, same group, Jan 2026): VLM-guided variable impedance for safe contact-rich manipulation. Together with **OmniVIC** (2510.17150) it is the concrete instance of "the VLM sets the stiffness," which is the survey's central architectural bet. Neither is ingested; both are one fetch away.
- **SafeVLA** (2503.03480) was the single most load-bearing external citation here. **Now ingested, and it does not carry the weight** — [see the source page](safevla-paper.md). Its tasks are object navigation and pick-and-place, which this survey's own §2.1 excludes from contact-rich; its five safety predicates are discrete collision events with simulator ground truth; **there is no force anywhere in it.** The survey's foundation-model chapter is anchored on work from a different regime with a different hazard model — which strengthens rather than weakens the survey's own complaint that no contact-force evaluation protocol exists.
- **Does the exclusion of imitation learning survive contact?** The survey's justification is that IL "replicates behaviors rather than actively managing safety." But a demonstration set contains only safe episodes by construction — which is exactly the training signal the [runtime failure detection](../concepts/robotics/runtime-failure-detection.md) line exploits. The survey never considers that IL's safety property might be *distributional* rather than absent.

---
title: "HAI Issue Brief — The World Model and Spatial Intelligence Era: Governing AI Beyond Language"
type: source
url: https://hai.stanford.edu/policy
local_path: raw/hai-issue-brief-the-world-model-and-spatial-intelligence-era.pdf
author: Daniel Zhang, Russell Wald (equal contribution), Ehsan Adeli, Elena Cryst, Daniel E. Ho, Caroline Meinhardt, Jiajun Wu, Amy Zegart, Li Fei-Fei
venue: Stanford HAI Policy & Society — Issue Brief
published: 2026-07
ingested: 2026-08-07
format: pdf
tags: [policy, governance, world-model, spatial-intelligence, national-security, privacy, evaluation, stanford-hai]
---

## Summary

The first **policy** document in this wiki, and the first source here that treats world models as a governance object rather than an architecture. Its thesis: language-centered AI governance has organized itself around two questions — *what does the system generate?* (foundation-model rules) and *what is the system permitted to do?* (agentic-AI rules) — and world models introduce a third that neither covers: **is the learned environment valid for the use it is being put to?** A world model's error is "a counterfeit of physical reality that can look flawless while being wrong," and every policy trained inside it, every certification that relies on it, and every decision informed by it inherits that flaw silently and at scale.

From that the brief derives three governance pillars — **infrastructure and incentives** (shared action-labeled data and compute so the capability is not captured by whoever already deploys fleets), **proportional safeguards** (stringency scales with proximity to safety-critical simulation or real-world action, attached to *deployment context* rather than model class), and **public sector capacity** (measurement science and independent evaluation, because today the tools to evaluate these systems sit almost entirely with their developers). The brief is explicitly *not* a regulatory proposal: it argues a rigid playbook would be "premature and ill-conceived" at this stage of the frontier.

> [!note] Declared conflicts
> The brief carries its own disclosure: Stanford HAI receives financial support from companies named in it, **including [NVIDIA](../entities/nvidia.md) and Google**; and co-author [Fei-Fei Li](../entities/fei-fei-li.md) is on partial leave from Stanford as co-founder and CEO of **[World Labs](../entities/world-labs.md)**, whose product Marble is cited as an example of a commercially mature renderer. The authors state they retained full editorial authority. Worth carrying forward: the brief's central policy ask — public investment in shared simulation infrastructure and action-labeled data — is one that would also relieve a competitive disadvantage faced by a startup without a deployed robot fleet.

## Key claims

### The technical framing

- **Definition** — a world model is "an AI system that builds and maintains a working representation of an environment to predict how conditions may change **in response to action**." The contrast drawn with language models is the action-conditioning: an LM predicts what comes next in text; a world model predicts how an environment changes if an object is moved or a door opened (p. 3).
- **Spatial intelligence** is the *capability* — "to understand a physical environment and use that information to guide action." World models are "one technical pathway toward achieving that capability," not the capability itself (p. 2). See [spatial intelligence](../concepts/world-models/spatial-intelligence.md).
- **Counterfactual reasoning is the central goal** — "predicting the consequences of an action, including actions the model was never explicitly trained on" (p. 3).
- **Intellectual lineage** — Kenneth Craik's 1943 "small-scale model" of reality; 1960s symbolic internal models confined to rule-governed narrow environments; unlocked recently by (1) RL showing agents can learn to act through internal simulation and (2) multimodal AI grounding systems in how the world looks, moves, and sounds (pp. 2–3).
- **The consistency test** — a proposed informal progress benchmark: can an agent "move an object, leave the scene, and return to find it where it was left"? The brief's point is that in a world model this consistency is *learned from observation*, whereas in a game engine every object is placed in advance (p. 3).
- **Functional taxonomy** — renderers (see), simulators (understand), planners (act), borrowed from Fei-Fei Li's June 3, 2026 World Labs Substack post. Maturity ordering is explicit: **renderers most mature, planners least** (pp. 3–5). See [world-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md).
- **The category boundaries are dissolving** — "at the research frontier, unified models increasingly combine rendering, simulation, and control within a single network," and the brief draws the policy consequence directly: "capability thresholds defined per category are easily gamed or outgrown; consequently, safeguards must attach to the deployment context rather than to the model class" (p. 5). It also notes that recent **unified world-action models** learn rendering, dynamics and control jointly, "with planning capability emerging directly from learned visual dynamics rather than from an intermediate simulator" (p. 4) — i.e. explicit simulation is *a* path to physical validity, not the only one.
- **Named systems** — [World Labs](../entities/world-labs.md)' **Marble** and **Tencent's HY-World 2.0** as commercially mature renderers producing explorable scenes from text/image prompts; [NVIDIA](../entities/nvidia.md) **Omniverse** as conventional (hand-built, specialist, slow) simulation; **[Genie 3](../entities/genie-3.md)** as the frontier interactive case. Industry landscape: [Google DeepMind](../entities/google-deepmind.md), NVIDIA, Alibaba, Tencent among incumbents; World Labs, **AMI Labs**, **Odyssey** among startups (pp. 3–4).

### The risk analysis

- **The visual plausibility trap** — "renderers are optimized for plausibility rather than underlying truth." A generated building can look sound without a stable underlying structure (pp. 4, 7).
- **Each architecture fails differently, so each demands a different evaluation** (p. 7) — video generators without a persistent scene representation lose consistency over time; 3D-native systems get spatial consistency from explicit geometry but "still fail to capture how a world changes"; latent state-space models prioritize predicting change over visual detail. This is the brief's sharpest technical claim and it maps directly onto this wiki's [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) split.
- **Genie 3 datapoint** — "can generate an explorable scene in real time, but at its 2025 release, the world stayed coherent for only a **few minutes** before objects began to shift or vanish" (p. 7).
- **Teaching to a flawed test** — the failure mode unique to world models: using a learned model both to *train* a system and to *judge* it. "If the model understates the risk of skidding in rain, a vehicle trained in that model may learn to drive too fast and still score well when the same flawed model is used to test it. The score would reflect an error in the model, not readiness for a real road" (pp. 7–8).
- **No adequate benchmark exists.** Named landscape: **VBench** (visual quality, prompt alignment, temporal smoothness — but not physical law); **VideoPhy** and **PhyGenBench** (physical commonsense in generated video); **WorldScore** (controllability, quality, dynamics in world generation); **WorldModelBench** (judging video models *as* world models); **WorldArena** (perceptual quality plus usefulness for training, testing and planning robot behavior); and **[LIBERO](../entities/libero.md)** for simulated manipulation. Verdict: "a research patchwork rather than a settled standard — none gives policymakers an adequate basis to assess a world model for safety-critical deployment" (p. 8).
- **Evaluation should match function** — a renderer for concept art can be judged on how convincing it looks; a simulator for infrastructure planning must have geometry and physics that are *actually correct*; a planner in a robot must be tested repeatedly across varied real-world conditions. "The closer a system comes to real-world actions, the more its evaluation should weigh physical validity, robustness, and transfer beyond the test setting" (p. 8).
- **Liability shifts what responsibility depends on**, rather than eliminating it: did the deployer use it outside the setting where it was tested? did the operator have enough information to override it? did the hardware provider build a sensor configuration the model could not handle? (pp. 8–9).
- **Spatial privacy** — the harder problem is *inference*, not raw feeds: a model trained on multimodal spatial data may infer home routines, workplace patterns, health-related behavior, social relationships, or sensitive locations that were never explicitly labeled, and can hold "a continuously updated picture of who is where and how a space is used over time" (p. 9). Countervailing: simulation can *substitute* for real-world monitoring — AV developers training in simulated road environments collect less public-road footage.
- **Action-labeled interaction data is the scarce input** — robot trajectories, teleoperation logs, fleet sensor streams paired with control signals. "Cannot simply be scraped from the internet"; developers must gather them by operating physical machines in the real world. Passive visual data is abundant; this is not. Each deployment compounds the incumbent's advantage (pp. 9, 12–13).
- **Labor** — earlier AI waves hit knowledge work; world models extend automation into "jobs that require judgment in unstructured, changing environments that have resisted automation, such as driving, warehousing, and construction." And expertise migrates: as how a plant runs or how a crane operator executes a lift gets captured in simulation, "that knowledge moves from the workers who hold it toward the firms that build the models" (p. 10).

### National security

- **Dual use, stated plainly** — "a model that navigates aid through a disaster zone can guide a weapon through the same environment" (p. 10).
- **Advantages**: readiness/mission rehearsal (notably, this "could shift geopolitical power by enabling countries with limited operational experience to effectively test military plans under unfamiliar combat conditions"); contested logistics under degraded comms; intelligence decision support — with the caveat that simulation "may make uncertain forecasts appear more precise than they are"; and cost/scale for large quantities of cheap adaptive systems (pp. 11).
- **Risks**: new cyber-physical attack surface — the target becomes "the system's picture of its surroundings rather than the data it holds," so corrupting that picture "can turn a breach into a misguided maneuver or strike"; false readiness; **miscalculation and escalation** because countries will draw the human/machine control line differently and "because human-autonomy handoffs are hidden for security, neither side may know how the other system operates"; and strategic dependence on uninspectable proprietary simulation (pp. 11–12).
- **Export controls may be aimed at the wrong chokepoint** — controls have focused on compute and briefly model weights, but "world-model advantage may also depend on physical-world data and the ability to deploy systems at scale, putting key inputs outside that frame" (p. 12).
- **Interoperability is a live standards fight** — if coalition operations depend on shared simulations, allies trained on incompatible proprietary systems may not be able to operate together (p. 12).
- **State of play** — China has made embodied intelligence a strategic industry in its latest Five-Year Plan with state funds and shared data infrastructure directed at physical AI, emphasizing physical-world data and deployment (the brief hedges on whether that reduces reliance on frontier compute). The US has led "largely through private labs and research on physical AI rather than federal industrial policy," with a reported late-2025 White House robotics executive order under consideration and a 2026 congressional bill to establish a **National Commission on Robotics** (p. 11).

### The framework

Three pillars (pp. 12–14):

1. **Infrastructure and incentives** — shared pools of action-labeled data (robot trajectories, teleoperation logs) plus public-interest simulation environments "should be an explicit target" of the **National AI Research Resource (NAIRR)** led by NSF; NSF coordinates, sector agencies contribute domain testbeds, states support real-world testing through procurement. Build on already-emerging open ecosystems — open world-model weights, training recipes, evaluation tools.
2. **Proportional safeguards**, four elements — **build measurement science** (NIST develops shared evaluation methods; sector agencies define operating conditions and reporting; until those mature, existing physical-safety regimes keep requiring rigorous field testing); **ensure independent evaluation** (independence extends to *who defines the test conditions*, not just who runs the test); **protect spatial privacy** (data minimization is genuinely hard here because "the relevant data elements may not be known until the model takes shape" — hence *staged* application of minimization, retaining raw sensor data only for validation); **document perception and action** (a time-stamped record of what the system perceived, the state it inferred, and the action it took, so a physical incident can be reconstructed and duty of care assigned across developer, deployer, operator, and integrator).
3. **Public sector capacity** — governments as demanding customers using procurement to fund independent testing and shared benchmarks, "provided the work is funded as research rather than expected on demand." An agency relying on a vendor's proprietary simulator must be able to inspect that environment. Closing line: "countries that build robust public ecosystems around simulation, robotics, and safety testing will outpace those focused exclusively on frontier model releases."

## Entities mentioned

- [Stanford HAI](../entities/stanford-hai.md) — publisher
- [Fei-Fei Li](../entities/fei-fei-li.md) — co-author; source of the functional taxonomy
- [World Labs](../entities/world-labs.md) — Marble; Li's company
- [NVIDIA](../entities/nvidia.md) — Omniverse as the conventional-simulation reference point
- [Google DeepMind](../entities/google-deepmind.md) — incumbent; [Genie 3](../entities/genie-3.md)
- [AMI Labs](../entities/ami-labs.md) — named among world-model startups
- [LIBERO](../entities/libero.md) — named as the robotics benchmark in the evaluation landscape
- Tencent (HY-World 2.0), Alibaba, Odyssey — no wiki pages yet

## Concepts touched

- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md)
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md)
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md)
- [World-model governance](../concepts/safety/world-model-governance.md)
- [World model](../concepts/world-models/world-model.md) / [world-model simulators](../concepts/world-models/world-model-simulators.md) / [world-action model](../concepts/world-models/world-action-model.md)
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) / [robot safety standards](../concepts/robotics/robot-safety-standards.md)

## Open questions

- **Does the wiki's technical evidence support the brief's maturity ordering?** The brief says planners are least mature. This wiki holds ~77 sources on VLA models with LIBERO scores above 90% — and also holds [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md), which argues those scores don't support their own rankings. See the synthesis: [world-model policy claims vs. this wiki's evidence](../syntheses/society/world-model-policy-vs-wiki-evidence.md).
- **Who actually holds the action-labeled data?** The brief names the scarcity but not the holders. This wiki tracks [Open X-Embodiment](../entities/open-x-embodiment.md), [DROID](../entities/droid.md), and the [LeRobot](../entities/lerobot.md) Hub as *open* action-data efforts — the brief's claim that "the market may still underprovide shared action data" deserves testing against what is already public.
- **What is WorldArena?** Named as evaluating "usefulness in training, testing, and planning robot behavior" — the only benchmark in the list that scores a world model by its downstream utility rather than its outputs. No primary source ingested; this is the highest-value follow-up.
- **Does the "few minutes of coherence" figure for Genie 3 still hold in 2026?** The brief cites the 2025 release. No newer measurement is in the wiki.
- **Is "document perception and action" implementable at 30–200 Hz?** The brief asks for a time-stamped record of perceived observation, inferred state, and action taken. For a learned end-to-end policy, "the state it inferred" may not exist as an inspectable object at all — the wiki's [latent space](../concepts/world-models/latent-space.md) and [mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) pages both say this is unsolved. The brief acknowledges internal reasoning is "only partly interpretable" but still lists the requirement.
- **No cost figures anywhere.** The brief argues world models will *lower* simulation cost. It gives no numbers, and neither does most of the technical literature in this wiki.

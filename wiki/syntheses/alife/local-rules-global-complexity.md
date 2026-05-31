---
title: "Local rules, global complexity: learned vs. evolved vs. emergent self-organization"
type: synthesis
created: 2026-05-31
updated: 2026-05-31
tags: [artificial-life, alife, self-organization, self-replication, emergence, digital-evolution, neural-cellular-automata, complexity, paradigms-of-intelligence]
---

> Cross-cutting analysis of the wiki's [artificial-life branch](../../concepts/alife/artificial-life-and-self-replication.md). Every system in it shares one commitment — **complex global behavior from simple local interactions, with no central controller** — yet they differ on the question that actually matters: **where does the local rule come from, and what information turns into structure?**

## The shared commitment

Boids, Core War, Tierra, Avida, Neural Cellular Automata, Computational Life, and Xenobots look unrelated — flocking birds, battling assembly programs, evolving digital organisms, neural-net cells, random code soups, frog-cell robots. But they are all instances of the **same bet**: that **coherent macro-structure emerges from many identical/simple components following local rules**, never from top-down planning. [Reynolds' boids](../../concepts/alife/flocking-and-boids.md) made this concrete for motion; [NCA](../../concepts/alife/neural-cellular-automata.md) for morphogenesis; the [digital-evolution lineage](../../concepts/alife/artificial-life-and-self-replication.md) for replication and adaptation.

The interesting structure isn't in *that* they self-organize — it's in **what supplies the local rule**. That gives a clean spectrum.

## The "where does the rule come from?" spectrum

| Route | Rule source | Objective | Ancestor needed? | "Complexity" lives in | Exemplars |
|---|---|---|---|---|---|
| **Hand-designed** | a human writes it | implicit (designer's intent) | n/a | the *dynamics* the rule produces | [Boids](../../concepts/alife/flocking-and-boids.md); [Darwin](../../sources/darwin-1961-bell-labs-game.md) (1961); [Core War](../../entities/core-war.md) (1984) |
| **Learned** | gradient descent toward a target | a **designed target** (image / texture / shape) | seed pattern | the *learned local rule* | [Neural Cellular Automata](../../concepts/alife/neural-cellular-automata.md) ([Pajouheshgar 2025](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md)) |
| **Evolved** | mutation + selection discover it | a **designed fitness/reward** (often) | a hand-written **self-replicator** | the *evolved ecology / genome* | [Tierra](../../entities/tierra.md) ([Ray 1991](../../sources/ray-1991-tierra-synthesis-of-life.md)); [Avida](../../entities/avida.md) ([Adami 1994](../../sources/adami-brown-1994-avida.md), [Lenski 2003](../../sources/lenski-2003-evolutionary-origin-complex-features.md)) |
| **Emergent** | a random walk through program space | **none at all** | none | the *emergence event itself* | [Computational Life / BFF](../../sources/computational-life-self-replicating-programs-paper.md) (2024) |

Read top-to-bottom, this is a **"how much is designed in?" gradient** that *decreases* monotonically — and the digital-self-replication chain happens to walk it in historical order:

**[Darwin](../../sources/darwin-1961-bell-labs-game.md) (1961, hand-written, no evolution) → [Core War](../../entities/core-war.md) (1984, hand-written, no evolution) → [Tierra](../../entities/tierra.md)/[Avida](../../entities/avida.md) (1991–94, designed ancestor + selection → evolution) → [Computational Life](../../sources/computational-life-self-replicating-programs-paper.md) (2024, no ancestor, no fitness → emergence).**

## The real axis: where does the information come from?

The deeper way to read the spectrum is **information-theoretic** — what is the *source* of the complexity that ends up in the structure?

- **Hand-designed:** the information is **in the designer's head**, transcribed into the rule. Boids look alive, but the three steering rules carry all the design; the run only *unfolds* them.
- **Learned (NCA):** information flows **from a target pattern, through backprop**, into the shared update rule. The rule is discovered, but the *answer* (the target image) was supplied. NCA's achievement is robustness/regeneration "for free" once the rule is learned — the self-organizing *process* generalizes beyond the single training target.
- **Evolved (Avida):** [Adami](../../entities/chris-adami.md)'s framing is **"stochastic information transfer from the environment into the genome"** via selected mutations. [Lenski et al. 2003](../../sources/lenski-2003-evolutionary-origin-complex-features.md) pin this down: the complex EQU function only assembles when the **environment rewards simpler stepping-stone functions** — information enters the genome *incrementally* from a structured reward landscape. Remove the gradient (reward only EQU) and **0/50** populations find it; supply it and **23/50** do. The environment is the information source.
- **Emergent (Computational Life):** the striking case — there is **no external information source at all**. No target, no fitness, no ancestor. Complexity (measured by rising **high-order entropy**) appears from **the reachability of short self-replicators under random self-modification** plus the shared-tape substrate. The information comes from *nowhere external* — it's manufactured by the dynamics once a replicator is stumbled upon. This is why the result is surprising in a way the others are not.

So the branch isn't really "four kinds of ALife." It's **one question — what authors the structure? — answered at four removes from the designer:** human → target-via-gradient → environment-via-selection → nothing.

## Why the bins are fuzzy (and that's the point)

The spectrum is a lens, not a taxonomy. The most interesting systems **straddle** it:

- **[Xenobots](../../entities/xenobots.md)** are the clearest hybrid: their *bodies* are **evolved** ([evolutionary computation](../../concepts/alife/evolutionary-computation.md) on a soft-body sim), their *behavior* relies on **emergent** cellular self-organization (cilia coordination, self-repair), and their **kinematic self-replication arises spontaneously** — un-selected — yet AI is then used to *amplify* it ([Kriegman 2021](../../sources/kriegman-2021-kinematic-self-replication.md)). One system, three routes.
- **Avida** evolves rules but under a **hand-designed reward** — evolved mechanism, designed objective.
- **NCA** learns a rule by gradient but the *behavior* (regeneration after damage) is **emergent**, never explicitly trained.

The fuzziness is the substance: real systems mix authorship of structure across these modes.

## The Mordvintsev bridge

The clearest empirical sign that these are facets of one inquiry: **[Alexander Mordvintsev](../../entities/alexander-mordvintsev.md)** originated **Neural Cellular Automata** (the *learned* corner) *and* co-authored **[Computational Life](../../sources/computational-life-self-replicating-programs-paper.md)** (the *emergent* corner). The same researcher works both ends of the spectrum — strong evidence the learnable-self-organization and emergent-self-replication communities are converging on a shared object of study.

## Connection to the wiki's "paradigms of intelligence" thread

This branch is the mechanical underside of one of the wiki's three alternative-paradigm voices (see [critiques of the intelligence north star](../society/critiques-of-the-intelligence-north-star.md)):

- [LeCun](../../entities/yann-lecun.md) — intelligence as **world models** ([JEPA](../../concepts/world-models/jepa.md)).
- [Michael I. Jordan](../../entities/michael-i-jordan.md) — intelligence as **collectives + economic mechanisms**.
- [Agüera y Arcas](../../entities/blaise-aguera-y-arcas.md) — intelligence/life as **emergent from simple interaction** — *this branch.*

There's also a methodological rhyme with [JEPA](../../concepts/world-models/jepa.md): both reject hand-designed objectives. JEPA predicts in latent space instead of reconstructing pixels; NCA learns a process instead of a mapping; Computational Life gets structure with **no objective at all** — the logical extreme of the same anti-hand-design instinct.

## Open questions this synthesis surfaces

- **Do the routes formally meet?** Can you *evolve* an NCA rule (selection over learned rules), or *learn* to predict an emergent soup's dynamics? Mordvintsev's own **self-replicating-NCA** work hints at learned + replicating; nobody (in the ingested set) has unified learned/evolved/emergent under one formalism.
- **Information accounting.** Is there a single measure — high-order entropy? mutual information between environment and genome? — that quantifies "how much structure each route manufactures vs. is handed"? Adami's information-theoretic program and the Computational Life high-order-entropy metric are the obvious starting points.
- **Where do Xenobots sit precisely?** A biological system spanning all three routes is either a category error or the most honest example — worth its own deeper treatment.
- **Open-endedness.** Tierra/Avida are open-ended-ish but plateau; Computational Life keeps producing structure. What substrate property (reachability? shared read/write? no fitness?) actually sustains open-endedness? The [SUBLEQ counterexample](../../sources/computational-life-self-replicating-programs-paper.md) is the sharpest clue.

## See also
- [Artificial life and the emergence of self-replication](../../concepts/alife/artificial-life-and-self-replication.md) — the concept page this synthesizes.
- [Neural Cellular Automata](../../concepts/alife/neural-cellular-automata.md), [Evolutionary computation](../../concepts/alife/evolutionary-computation.md), [Flocking and boids](../../concepts/alife/flocking-and-boids.md).
- [Critiques of the intelligence north star](../society/critiques-of-the-intelligence-north-star.md) — the paradigms-of-intelligence framing.

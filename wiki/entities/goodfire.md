---
title: Goodfire
type: entity
subtype: company
created: 2026-08-30
updated: 2026-08-30
sources: 7
tags: [company, interpretability, mechanistic-interpretability, sparse-autoencoders, silico, neural-geometry, safety, san-francisco, public-benefit-corporation]
---

**Goodfire** — San Francisco research company and public benefit corporation building **interpretability as a product**. Its self-description: *"a research company using interpretability to understand, learn from, and design AI systems. Our mission is to build the next generation of safe and powerful AI—not by scaling alone, but by understanding the intelligence we're building."*

In this wiki it is the **first independent commercial interpretability company**, and the counterweight to a [mechanistic-interpretability](../concepts/safety/mechanistic-interpretability.md) page that until now described the field as an [Anthropic](anthropic.md) research programme. Goodfire's bet is that interpretability is not only a safety activity but a **model-design and scientific-discovery tool** — sold to biotech, robotics and enterprise customers rather than practised internally by a frontier lab.

## The positioning argument

Two sentences from the company page carry the thesis:

> "Treating models as black boxes is an unnecessary handicap."

> "Understanding those structures lets us steer what models learn, make them safer and more useful, and extract the vast knowledge they contain."

That last clause is the non-obvious half. The usual pitch for interpretability is defensive — *know when the model is lying*. Goodfire's is also **extractive**: a model trained on more genomics or echocardiography than any human has read knows things nobody has written down, and interpretability is the instrument for getting them out. Their [Series B post](../sources/goodfire-series-b.md) calls interpretability *"the toolset for a new domain of science: a way to form hypotheses, run experiments, and ultimately design intelligence."*

## Silico

**[Silico](../sources/goodfire-silico-robotics-vision.md)** — the product, described as *"your interpretability agent"* that lets you *"explain, debug, and precisely control model behavior"* and *"build AI models with the precision of written software."*

It is an **agent**, not a library: it *"develops experimental plans, runs work in parallel, monitors progress, and returns inspectable results,"* orchestrating long-running experiments across nodes with multi-stage guardrails on its own behaviour. The bundled methods are the field's current toolkit — auto-interp, probe and SAE training, **model diffing**, causal analysis, data attribution, **neural geometry**, and activation verbalizers.

Three named verticals: **Life Sciences**, **Robotics & Vision**, and **LLMs**. Distributed as a **macOS download** plus enterprise deployment.

Named customers and partners across the site and the Series B announcement: **Arc Institute, Basecamp Research, Mayo Clinic, Microsoft, Prima Mente, Prime Intellect, Rakuten, Valinor Discovery**.

> [!note] Why an agent, and what it implies
> Interpretability work is a long tail of small experiments — train a probe, sweep a layer, diff two checkpoints, test a causal hypothesis. That shape is unusually well suited to delegation, and Silico's design concedes the point that the bottleneck in interpretability is **researcher hours, not methods**. It also means the wiki should treat its outputs the way it treats any agent's: the [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) caveats apply, and "the agent found a feature" is a claim needing the same verification as any other.

## Robotics relevance

Not incidental — **Robotics & Vision is one of three named Silico verticals**, and the framing is one this wiki has been circling from the other direction:

> "Vision and robotics models often fail in the real world because they learned brittle shortcuts instead of generalizable concepts."

Their published robotics case study traces unstable behaviour in a **robotics foundation model** to an **information bottleneck midway through the network**, by inspecting latent policy structure and representational geometry directly, and proposes targeted corrections **without full retraining**. See the [Silico robotics & vision page](../sources/goodfire-silico-robotics-vision.md).

This is the wiki's first source describing **interpretability applied to a robot policy's internals** rather than to its success rate. It is the natural methodological complement to [LIBERO-PRO](../sources/libero-pro-paper.md)'s finding that >90% benchmark scores collapse to 0.0% under perturbation: LIBERO-PRO establishes that policies memorize, and this line of work is about looking inside to see *what* they memorized.

## Funding

| Round | Amount | Date | Notes |
|---|---|---|---|
| Seed | ~$7M | 2024 | Reported by VentureBeat |
| Series A | $50M | 2025 | Per the company's own announcement post |
| **Series B** | **$150M** at a **$1.25B** valuation | **2026-02-05** | Led by **B Capital** |

Series B investors: DFJ Growth, Salesforce Ventures, **Eric Schmidt**, and existing backers Juniper Ventures, Menlo Ventures, Lightspeed, South Park Commons, Wing Venture Capital. Amount, valuation, date and lead are from [the company's own post](../sources/goodfire-series-b.md) and corroborated by the PR Newswire release.

## People

> [!warning] Founder details are secondary-sourced
> Goodfire's own company page gives **no founding date, founder names, headcount or location**. The details below come from press coverage of the Series B and are **not** confirmed against a Goodfire primary in this wiki. Treat as reported, not established.
>
> Reported: founded **June 2024** by **Eric Ho** (CEO, previously founder of RippleMatch), **Dan Balsam** (CTO), and **Tom McGrath** (Chief Scientist).

What the company page *does* state, and what is therefore first-party: the team includes *"founding members of interpretability efforts at Google DeepMind and OpenAI, professors on leave, and engineers who have built and deployed large-scale ML systems at organizations like OpenAI, Google, and Palantir,"* with contributions to sparse autoencoders, automated feature interpretation, and knowledge extraction from superhuman models.

**Tom McGrath** is independently corroborated as Goodfire-affiliated by his authorship on [The World Inside Neural Networks](../sources/goodfire-research-index.md) and by his listing as founder of DeepMind's mechanistic-interpretability team. **Nick Cammarata** (a core contributor to OpenAI's original interpretability work) and **Leon Bergen** (UC San Diego, on leave) are named in coverage and appear as authors in the [research corpus](../sources/goodfire-research-index.md).

## Mentioned in

- [Silico for Robotics & Vision](../sources/goodfire-silico-robotics-vision.md)
- [Goodfire research index (2024–2026)](../sources/goodfire-research-index.md)
- [Verbalized Eval Awareness Inflates Measured Safety](../sources/goodfire-verbalized-eval-awareness.md) — with [UK AISI](uk-aisi.md).
- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](../sources/goodfire-reasoning-theater.md) — with Harvard; arXiv primary.
- [Goodfire Series B announcement](../sources/goodfire-series-b.md)
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) and [neural geometry](../concepts/safety/neural-geometry.md) (concepts, not sources)
- [Proposed experiment: latent inspection vs policy collapse](../syntheses/projects/latent-inspection-policy-collapse.md) — the testable version of its robotics claim.

## Open questions / TBD

- **No robotics result is quantified anywhere public.** The robotics case study describes a method and an outcome ("traced unstable behaviors to brittle internal features") with **no model named, no benchmark, no numbers**. It is a marketing case study, not a result, and the wiki should not cite it as evidence that the technique works — only that the technique is being attempted.
- **Silico is closed and macOS-first**, so none of it is independently reproducible. Its *research*, by contrast, is not — [Reasoning Theater](../sources/goodfire-reasoning-theater.md) is on arXiv with released code, and the [eval-awareness work](../sources/goodfire-verbalized-eval-awareness.md) is co-authored with [UK AISI](uk-aisi.md). **The research programme and the product have different openness postures**, and the research is the stronger evidence that the methods work.
- **The safety-vs-capability tension is unexamined.** "Steer what models learn" and "make them safer" are the same toolset; a company selling model-editing to enterprises is also selling the ability to remove behaviours a lab installed deliberately. No source here addresses that.
- **Whether the robotics vertical has a real customer.** Prime Intellect is the closest thing to one in the named list, and it is a distributed-training company rather than a robotics company.

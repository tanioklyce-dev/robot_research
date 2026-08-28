---
title: "Introducing Portable Computer for local-first AI (Perplexity)"
type: source
url: https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai
author: Perplexity
affiliation: Perplexity AI
published: 2026-08-25
ingested: 2026-08-28
venue: Perplexity Blog (News)
format: product announcement blog post
tags: [perplexity, portable-computer, local-first, dgx-spark, qwen, nemotron, edge-agents, llm-agent-architecture, privacy, escalation, marketing-source]
---

# Introducing Portable Computer for local-first AI

> [!note] Provenance — retrieved via the Wayback Machine
> `perplexity.ai` is behind Cloudflare and returns **403** to `curl`, to WebFetch, and to text proxies. The text here comes from the **Internet Archive snapshot of 2026-08-26** ([web.archive.org/web/20260826085451/…](https://web.archive.org/web/20260826085451/https://www.perplexity.ai/hub/blog/introducing-portable-computer-for-local-first-ai)), which is the primary as published. Ingested because [NVIDIA's roundup](nvidia-local-ai-blog-series-2026-08.md) paraphrases this post and **drops several material facts** — see the comparison below.

## Summary

**Portable Computer** is a version of Perplexity Computer that *"runs entirely on a local machine,"* built with NVIDIA for the **[DGX Spark](../entities/dgx-spark.md)**. The pitch is local-first rather than local-only: private data stays on the device, and the agent **escalates to the cloud only when a task needs it, with the user's authorization**.

The framing is aimed squarely at work people won't send to an API: *"Some of the most valuable work people have for AI agents includes data they'd rather keep on their own machines. Whether it's private codebases or confidential material, local models are now getting strong enough to work on them right where they are."*

## The architecture, which is the part worth having

The single most useful sentence for this wiki, because it says *what* is local rather than just "the model":

> "Portable Computer runs on the NVIDIA DGX Spark with Qwen 3.8 27B or with **PPLX 27B**, a post-trained version of the Qwen model. NVIDIA Nemotron 3.5 Lightning, a 30B open model, is coming soon to the model picker. **The orchestrator, planner, tool router, scheduler, durable task queue, and local search index all run on device.**"

That list is a specification for an on-device agent runtime, not a model deployment. Compare the wiki's [LLM agent architecture](../concepts/agents/llm-agent-architecture.md) coverage: the components normally assumed to be server-side — planning, routing, scheduling, a **durable task queue**, and a search index — are all named as local. The durable queue is what makes *"keeps jobs running"* and long-horizon autonomy possible without a backend.

**The escalation policy is a post-training objective, not a config flag:** *"The Qwen model is post-trained to complete as much of each task locally as possible and to escalate to the cloud when the task needs it."* So *when to escalate* is learned behaviour in the local model. Escalation targets *"current information, browser use, connected apps, or one of **15+ frontier models** for advanced reasoning."*

**Consent is explicit and per-transfer:** *"When a task needs to send content from the device to a cloud service, Portable Computer asks the user for permission before moving forward."*

**Security:** *"Code and tool execution run in isolated sandbox environments with controlled access to files and connected apps"* — matching the cloud product.

## Other specifics

- **Local dictation** via the **NVIDIA Nemotron 3.5 ASR model** — *"the transcription and actions on files all stay on the machine… without the audio touching the cloud."*
- **App connectors**: Google Drive, Gmail, Slack, GitHub. Worked example given: triage new GitHub issues against overnight Gmail bug reports on device, then post the top three to Slack with suggested owners.
- **Economics**: *"on-device work doesn't consume credits"* and *"work handled by the local models has no per-credit charge."* The stated consequence — *"people no longer have to ration what they use intelligence for"* — is the actual product thesis.
- **Availability**: **Pro and Max subscribers only**, on DGX Spark, **Linux first with Windows coming soon**. One-click install from the Perplexity app.
- **Hardware as described**: GB10 Grace Blackwell, *"a 20-core Arm CPU and NVIDIA GPU with 128 GB of unified memory"* — consistent with the wiki's [DGX Spark](../entities/dgx-spark.md) page.

> [!warning] The benchmarks are in a document not ingested here
> The post claims *"outperformance across benchmarks for accuracy, speed, and credit efficiency"* and points to a **separate research blog, "A Local-First Agent for Private and Cost-Effective Knowledge Work" (2026-08-25)**. **No number appears in this post.** Any performance claim about Portable Computer should be sourced from that research post, which is not ingested — the same Cloudflare block applies.

## What NVIDIA's version dropped

Both were published 2026-08-25. [NVIDIA's item](nvidia-local-ai-blog-series-2026-08.md) is shorter and loses things that change the picture:

| NVIDIA's version | The primary |
|---|---|
| *"a specially post-trained Qwen 3.8 27B model"* | **two choices** — stock **Qwen 3.8 27B** *or* **PPLX 27B**, the post-trained one |
| *"don't count towards token limits"* | *"doesn't consume **credits**"* / *"no per-credit charge"* — a different billing unit |
| silent | **Pro and Max subscribers only** — it is behind a paid tier |
| silent | **Linux first**, Windows later |
| silent | the **local orchestrator / planner / tool router / scheduler / durable task queue / search index** — the actual architecture |
| silent | **per-transfer user permission** before anything leaves the device |
| silent | **sandboxed** code and tool execution |
| silent | **Nemotron 3.5 ASR** for on-device dictation |
| silent | escalation reaches **15+ frontier models** |
| *"working on a fine-tuned Nemotron 3.5 Lightning variant"* | Nemotron 3.5 Lightning *"coming soon **to the model picker**"* — an option, not necessarily a Perplexity fine-tune |

The pattern is the one this wiki keeps finding: the secondary keeps the headline (*local agent on DGX Spark*) and drops the qualifiers that decide whether it applies to you — the subscription gate, the OS limitation, and the consent model.

## Entities mentioned

- [Portable Computer](../entities/perplexity-portable-computer.md) · [DGX Spark](../entities/dgx-spark.md) · [Qwen](../entities/qwen.md) · [Nemotron](../entities/nemotron.md)

## Concepts touched

- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md)
- [On-device and on-robot agents](../syntheses/agents/on-device-and-on-robot-agents.md)

## Open questions

- **No numbers here at all.** Everything quantitative is deferred to the research blog. Until that is read, "outperformance across benchmarks" is an unverifiable claim.
- **What is PPLX 27B, exactly?** Post-trained from Qwen 3.8 27B, but no weights, recipe, licence or evaluation are given. Whether it is redistributable matters if anyone wants to reuse it.
- **How is the escalation decision made and audited?** It is described as learned post-training behaviour. There is no statement of how a user inspects *why* the model wanted to escalate, which is exactly the accountability question a robot version would raise.
- **Nothing robotic.** The workloads are documents, email, Slack and code. Its relevance here is **architectural** — this is the wiki's first shipped example of a local-first agent with a durable on-device task queue and a learned escalation policy, which is the shape an on-robot agent would need.

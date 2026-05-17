---
title: Wiki-query agent on DGX Spark — deployment plan
type: synthesis
created: 2026-05-17
updated: 2026-05-17
tags: [deployment, llm-wiki, queryable-agent, dgx-spark, qwen, vllm, ollama, local-llm, hosting]
---

A scoping plan for making this LLM-wiki **queryable online as an agent**, served from a **local [DGX Spark](../../entities/dgx-spark.md)** running an open-source LLM. Captures the design decisions from a 2026-05-17 conversation so the rationale doesn't get lost if execution drifts later.

## The question

The wiki is hosted on GitHub as ~384 cross-linked markdown files. A visitor can browse it, but there's no "ask a question, get a wiki-grounded answer" interface. How do you add that?

## Three deployment options (ordered by build effort)

| Option | Effort | Reach | Recurring cost |
| --- | --- | --- | --- |
| **Anthropic Claude API + file_search + small frontend** | ~½ day | anyone with a browser | per-query API fees |
| **Static site + RAG chat widget** | 1–3 days | anyone with a browser | API fees + embedding maintenance |
| **MCP server, readers connect their own Claude Code** | a few hours | Claude Code / Desktop users only | $0 — visitors use their own keys |

A fourth option **also chosen here**: run the inference **locally on owned hardware** with an open-source LLM. Zero per-query fees, full control, no API-key trust friction, and the hardware doubles as a training / sim / fine-tuning box.

## The decision: local inference on DGX Spark

**[DGX Spark](../../entities/dgx-spark.md) is the inference server.** The choice isn't purely about wiki queries — Spark also handles training, fine-tuning, and Isaac Sim / Isaac Lab work the wiki cares about ([Jetson Thor vs DGX Spark synthesis](../platforms/jetson-thor-vs-dgx-spark.md)). Wiki-query inference is one of many workloads the box justifies.

### Why Spark over Thor for this role

Both Thor and Spark share **128 GB LPDDR5X unified memory at 273 GB/s**, so model fit and quantized-inference performance are roughly comparable for a Q4 / NVFP4 wiki-query workload — the [JetPack 7 reference](../../sources/nvidia-jetpack-7-thor-whitepaper.md) reports Llama 3.3 70B at **41.5 tok/s on a single Thor** (88.62 tok/s with EAGLE-3 specdec). The asymmetric reason to pick Spark is **RT cores**: it can also run Isaac Sim / Isaac Lab and fine-tune larger models. Thor categorically cannot. If the inference box is also the dev box, Spark is the only answer.

### Why not just use the Anthropic API on someone else's metal

- Per-query API fees scale linearly with usage — not a problem at low traffic, but unbounded if the wiki picks up readers.
- Forces a trust decision: pay yourself (your key on a server) or push trust to visitors (BYOK with the phishing-shaped UI failure mode).
- The wiki already endorses local-LLM infrastructure ([stretch_ai](../../entities/stretch-ai.md) ships Qwen 2.5 + [Ollama](../../entities/ollama.md); the [ROSOrin](../../entities/rosorin.md) curriculum has an offline track). Self-hosting the wiki agent matches that pattern.

## Recommended model

**Default: [Qwen](../../entities/qwen.md) 2.5 72B at Q8 quantization** (~75 GB) — leaves ~50 GB for KV cache + long context. Matches the wiki's existing Qwen precedent ([stretch_ai](../../entities/stretch-ai.md), [ROSOrin](../../entities/rosorin.md)) and runs comfortably on Spark with room for full-context queries (loading CLAUDE.md + index.md + several wiki pages at once).

**Strong alternatives**:

| Model | Why pick it |
| --- | --- |
| **Llama 3.3 70B at FP8 / Q8** | Comparable quality to Qwen 72B; slightly behind on code / agentic tasks. |
| **DeepSeek R1 / V3** (671B MoE, ~37B active) | Fits at Q4 on a single Spark; noticeably stronger reasoning for cross-page synthesis queries; harder to serve. |
| **Qwen 2.5 32B (Q8 or FP16)** | If concurrent-user throughput matters more than ceiling quality — smaller model, more headroom for batching. |

**The load-bearing tradeoff**: Spark's 273 GB/s memory bandwidth is **~1/12 of an H100's HBM3** (3.35 TB/s), so inference is bandwidth-bound and slower than a data-center card. Fine for a small-team / personal-research wiki-query workload; constraining if many users query concurrently. **vLLM with batching** is the mitigation if it becomes a problem.

## Serving stack

| Component | Choice | Rationale |
| --- | --- | --- |
| Inference server | **vLLM** (default) or **[Ollama](../../entities/ollama.md)** for zero-ops | vLLM gives proper batching for concurrent queries; Ollama is the wiki's current local-LLM precedent. JetPack 7 supports both ([JetPack 7 reference](../../sources/nvidia-jetpack-7-thor-whitepaper.md)). |
| Retrieval / context loading | Direct file load of CLAUDE.md + index.md + on-demand pages (Qwen 2.5 72B handles ~128k context, the wiki's CLAUDE.md + index is ~80k) | Avoids embedding-pipeline maintenance. Falls back to chunked RAG only if model size drops below 32B. |
| Frontend | Static HTML page, plain `fetch` to local vLLM endpoint | Hosted on the same Spark or on a small VPS. No login. |
| Public exposure | Cloudflare Tunnel or Tailscale Funnel to expose the local server | Spark stays behind a residential / lab firewall. |

## Architecture sketch

```
Visitor browser
      │
      ▼ HTTPS
[Cloudflare Tunnel / Tailscale Funnel]
      │
      ▼
[Spark — vLLM serving Qwen 2.5 72B Q8]
      │ wiki files mounted read-only
      ▼
[robot_research/wiki/ on local disk]
```

At query time: the frontend sends the user question + the relevant wiki pages (loaded by simple keyword retrieval against `index.md`) to vLLM, which returns a citation-grounded answer following the [CLAUDE.md](../../../CLAUDE.md) wiki-query conventions.

## Cost ballpark

- **Hardware**: Spark already justified by other workloads (training, Isaac Sim, fine-tuning) — wiki query is a free additional use.
- **Electricity**: Spark idles low; under load it draws roughly 250–400 W for inference. Negligible at residential rates.
- **Ongoing**: $0 / month per query. Just the box.

vs Anthropic-API-on-a-VPS path: Anthropic Claude Sonnet at ~$0.005–$0.02 per query with caching = **$15–$60/month at 100 queries/day**, scaling linearly. Spark wins on TCO once query volume crosses a threshold the wiki could plausibly reach.

## Open questions / TBD

- **Retrieval strategy**: full-context load (CLAUDE.md + index + on-demand pages) vs proper RAG with embeddings. Default plan is full-context since Qwen 2.5 72B handles 128k. Revisit if quality is poor.
- **Conversation memory**: stateless per-query or thread-state across questions? Stateless is simpler; threaded gives a better agent feel.
- **Tool use**: should the agent be able to call wiki-side tools (e.g., a `find_page` function, a `git_log` reader)? MCP-style tool exposure would lift this from "RAG chatbot" to "true agent."
- **Update cadence**: how the served wiki state stays in sync with the GitHub repo. Cron-based `git pull` is the simplest answer.
- **Public-facing UX**: cap concurrent connections, rate-limit per IP, log queries (anonymized) for prompt-improvement iteration.
- **Comparison evaluation**: run a small benchmark of "wiki questions" against Qwen 2.5 72B locally vs Claude Sonnet API to confirm quality is acceptable before committing.

## Related

- [Jetson Thor vs DGX Spark](../platforms/jetson-thor-vs-dgx-spark.md) — the train-on-Spark / deploy-on-Thor decision tree this synthesis sits downstream of.
- [DGX Spark entity](../../entities/dgx-spark.md) — hardware specs.
- [JetPack 7 software-stack reference](../../sources/nvidia-jetpack-7-thor-whitepaper.md) — vLLM / SGLang / Ollama support on Blackwell platforms.
- [Qwen](../../entities/qwen.md) — model family.
- [Open-source robot AI research projects](../platforms/open-source-robot-ai-projects.md) — broader open-source landscape this deployment sits inside.

## Provenance

This page exists because a 2026-05-17 conversation walked through how to make the wiki queryable, who pays the fees in each option, BYOK trust dynamics, local-LLM model choice on consumer + server tiers, and the Thor-vs-Spark comparison for inference. The decision (Spark + Qwen 2.5 72B Q8 + vLLM) is captured here so future re-decisions inherit the rationale.

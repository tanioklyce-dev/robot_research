# MiaAI-Lab/sparkDash PR #284 — Spark Overseer (bundle)

Captured 2026-11-07. PR state OPEN (not merged); head branch kerpopule:feat/spark-overseer, 6 commits, last 2026-10-26; +1611/-197 across 32 files. Upstream repo: Apache-2.0, 840 stars, created 2026-07-19.

---- PR body, maintainer comments, file list (gh pr view JSON) ----
{"author":"kerpopule","body":"## Spark Overseer: opt-in local security observations for DGX Spark / GB10 workloads\n\nThis contributes the observation layer to sparkDash, using its existing navigation, branding and four themes. It is deliberately **not** a claim of exfiltration prevention or complete host monitoring.\n\n### What is included\n- A default-off, shared collector for administrator-configured local journals, bound to existing Spark registry IDs. Polls independently of dashboard requests; bounded source reads, retention, deadlines and deduplication.\n- Engine-independent command instrumentation and an OpenAI-compatible JSON/SSE response observer. The response adapter preserves output bytes and labels tool proposals **proposed, not executed**. No prompt/reasoning text, raw arguments, URL paths, payloads or arbitrary producer prose enters the dashboard API.\n- Deterministic indicators for uploads, credential paths, cloud metadata destinations, security-control changes, encoded execution and download-to-shell patterns. Destination allowlists match full hostnames before display minimization. These are review signals, not authorization or maliciousness verdicts.\n- Spark Overseer page with source coverage, unit/model/severity/search filters, keyboard-accessible details, pagination, unavailable/error states, and explicit observation-only limits. No external AI reviewer, monitoring-model tokens or new direct runtime dependency.\n- Setup, threat model, privacy/retention limits and reproducible safe scenarios in [the guide](https://github.com/kerpopule/sparkDash/blob/feat/spark-overseer/docs/spark-overseer.md).\n\n### Exercised, not just mocked assertions\nThe scenario suite runs real child processes and transfers a synthetic canary to an actual **loopback-only** HTTP sink. It verifies upload/credential signals, a quiet allowlisted benign read, and fragmented tool calls from a synthetic OpenAI-compatible streaming fixture. The proposed metadata command is inspected but **never executed**. No private files, real credentials or external upload targets are used.\n\nAdditional tests exercise authentication, default-off behavior, read-only API/query isolation, malformed/rotated/oversized/missing journals, FIFO and symlink refusal, bounded response parsing, cancellation/exit propagation, uninstrumented units, independent polling, deduplication, expiration, partial coverage and HTML-shaped producer input.\n\n### Verification\nRebased/merged against upstream `6fea2cf` before final verification:\n- ARM64 Linux / Node 24.8.0 full server suite: **1,351 passed, 16 skipped, 0 failed**. Skips are platform/optional upstream cases, not ignored Overseer failures.\n- Full frontend suite: **737 passed, 0 failed**; changed branding assertion also rerun separately.\n- Translation catalog check and all **11** checker tests passed; TypeScript and production build passed.\n- Actual collector → API → built UI browser fixture: **12** combinations across dark/light/white/OLED and 320/390/1440px, plus keyboard disclosure, source failure, forced colors and 200% content zoom. Zero page errors or horizontal overflow. Secondary metric text measured at least **9.26:1** in these fixtures, not a claim of a complete accessibility audit. Native viewport screenshots were inspected, not just stitched full-page captures.\n- `npm audit`: **0 findings** after compatible lockfile updates. Also includes a small Node 24 Linux test-fixture correction: unlink the mocked sysfs symlink itself instead of `rmSync(link-to-directory)`.\n\n### Important boundaries\n- Only explicitly instrumented paths are visible. This does not auto-intercept every inference request, monitor all sockets, classify model intent, block egress, verify a model identity or approve actions.\n- Journals and producer labels are not independent evidence if an unrestricted workload can alter them. Protect instrumentation and its files outside that trust boundary for stronger assurance.\n- Remote workload journals need an administrator-managed local copy or read-only transport; this PR does not introduce SSH collectors, credential management, paid review, telemetry or privileged services.\n- Fixtures and browser viewports are not real-model detection-accuracy benchmarks, physical-phone qualification or independent security review.\n\n### Screenshots\nSynthetic fixture data, actual built UI:\n\n![Spark Overseer desktop](https://raw.githubusercontent.com/kerpopule/sparkDash/feat/spark-overseer/docs/spark-overseer/desktop.png)\n\n![Spark Overseer mobile event details](https://raw.githubusercontent.com/kerpopule/sparkDash/feat/spark-overseer/docs/spark-overseer/mobile.png)\n\nAI-assisted implementation, with critical self-review and the execution evidence above. Feedback on the integration boundary and default-off UX is welcome.\n","comments":[{"author":"MiaAI-Lab","body":"Reviewed in an isolated worktree against current main (`693fa80`), with the security claims checked at the boundary rather than read off the description. They hold, and I want to be specific about that because it is the part that mattered most. Nothing producer-controlled reaches the API, a log, a shell or the page: `safeEvent()` in `server/overseer/signals.js:74-90` copies no property it did not whitelist, the model label is re-validated against a character pattern, signal codes are checked with `Object.hasOwn` rather than `in` so prototype keys cannot pass, and destinations are reduced to a hostname charset with no markup characters in it. I fed a hostile record through the real runtime — prompt text, a credential-reading command, markup in the model label and in a free field, prototype keys in `signals`, userinfo in a destination — and every one of those fields was dropped rather than escaped. The page has no `dangerouslySetInnerHTML`, the CLI wrapper spawns with `shell: false`, reads are bounded four ways (512 KiB tail, 1,000 lines, 16 sources, a 2 s deadline) with retention and a 4 MiB writer cap, the route is registered after `createAuthMiddleware()` so it is token-gated like every other API path, and `SPARK_OVERSEER_ENABLED === \"1\"` means unset, empty and `\"true\"` are all off. The committed screenshots contain only the synthetic fixtures. The `isolatedEnv.js` change is additive and is the right change — without it a developer with the variable set in their shell would have fixtures poll real journals. Architecture is consistent with the project: one shared runtime parameterized per registry unit, per-source failures caught so the others keep polling, and unknown counts rendered \"unavailable\" rather than 0. It also adds no dependency: the only `package.json` edit is the `test:server` glob.\n\nIt is not ported in this pass, for two reasons that are yours to resolve rather than mine.\n\nThe blocking one is `package-lock.json`. It carries about 647 lines of churn unrelated to this feature — vite, lightningcss, rolldown and `@oxc-project/types` version movement, new platform binding entries, a few removals — i.e. a lockfile regenerated on a different machine. The feature needs none of it, and landing dependency movement inside a review pass is exactly what the contributor guidance about keeping unrelated changes out of commits is for. Please `git checkout origin/main -- package-lock.json`; the diff should then touch `package.json` by one line and the lockfile not at all.\n\nThe second is a correctness defect worth fixing before it lands. In `server/overseer/runtime.js:93` an unexpected throw sets `configError` and nothing ever clears it, so the guard at `:61` turns every later poll into a no-op while the interval keeps firing: a transient `EMFILE` at second five of uptime disables the feature for the life of the process, the page reads \"Collector unavailable\", nothing is written to the server log, and the only recovery is a dashboard restart. Per-source failures are already handled at `:82`, so this path only fires on something transient — precisely where a permanent latch is wrong. Log once and clear `configError` at the top of a successful poll so it self-heals.\n\nTwo smaller things. `readJournal()` is stateless, so every 5 s poll re-reads and re-parses the whole tail of every source even when nothing changed — at 16 sources that is around 8 MiB of I/O and up to 16,000 `JSON.parse` calls every five seconds, forever, on the host the feature is meant to watch; caching size and mtime per source and skipping an unchanged file would remove nearly all of it. And the new files use one-space indentation and single quotes where the rest of `server/` uses two spaces and double quotes, with `scripts/overseer/browser-proof.mjs` additionally putting several statements on a line; there is no linter to fail on it, but the guidance is to match the surrounding code, and that script in particular will be hard for the next person to edit. A formatting pass would make the review of any follow-up much cheaper.\n\nTests on the merged tree: typecheck and build clean, server 1352 pass / 16 skipped / 0 fail, frontend 743 pass / 0 fail. Leaving this open for the lockfile revert and the latch fix.\n\n(Review notes prepared with Claude Code on behalf of the maintainer.)\n","createdAt":"2026-10-30T07:46:49Z"},{"author":"MiaAI-Lab","body":"Rechecked at `e81ad831` against main (`5e7be05`): nothing has moved since the 2026-10-30 review, and the two asks stand. `package-lock.json` still carries ~647 lines of unrelated dependency movement (vite/lightningcss/rolldown version churn) that the feature does not need — please `git checkout origin/main -- package-lock.json` so the diff touches `package.json` by one line and the lockfile not at all. And `server/overseer/runtime.js:93` still latches `configError` forever on an unexpected throw while the poll interval keeps firing, so a transient `EMFILE` at second five of uptime disables the feature until a restart — log once and clear it at the top of a successful poll so it self-heals. The `readJournal()` re-read/re-parse of every source tail every 5 s and the one-space/single-quote formatting remain worth doing but are not blockers. The security essentials were re-verified at this head and hold. Leaving this open for the lockfile revert and the latch fix.","createdAt":"2026-10-31T23:29:52Z"},{"author":"MiaAI-Lab","body":"The opt-in, local-only posture fits the repo, and the sysfs fixture cleanup on Node 24 is the kind of detail this needs. Two blockers from my pass: the branch bundles a package-lock refresh (459/188 lines, 989260f6) — dependency changes should be a separate, reviewable PR — and the branch no longer merges cleanly (base 6fea2cf). Please split the lockfile bump out and rebase onto current main with the full local gate; I'd also want the observation layer behind the same feature-flag pattern as the kiosk/MQTT integrations.\n\n(Review notes prepared with Claude Code on behalf of the maintainer.)","createdAt":"2026-11-02T19:27:48Z"}],"createdAt":"2026-10-26T22:44:34Z","files":["README.md +1/-0","docs/spark-overseer.md +105/-0","docs/spark-overseer/desktop.png +0/-0","docs/spark-overseer/mobile.png +0/-0","package-lock.json +459/-188","package.json +1/-1","scripts/overseer/browser-proof.mjs +103/-0","scripts/overseer/observe-completion.mjs +25/-0","scripts/overseer/observe-run.mjs +43/-0","server/__tests__/isolatedEnv.js +2/-0","server/__tests__/isolatedEnv.test.js +3/-1","server/collectors/__tests__/SystemCollector.intelGpu.test.js +2/-1","server/index.js +11/-0","server/overseer/__tests__/deadlines.test.js +26/-0","server/overseer/__tests__/edges.test.js +51/-0","server/overseer/__tests__/lifecycle.test.js +16/-0","server/overseer/__tests__/route.test.js +38/-0","server/overseer/__tests__/runtime.test.js +67/-0","server/overseer/__tests__/scenarios.test.js +81/-0","server/overseer/__tests__/signals.test.js +28/-0","server/overseer/completions.js +73/-0","server/overseer/journal.js +35/-0","server/overseer/runtime.js +127/-0","server/overseer/signals.js +91/-0","src/App.tsx +7/-2","src/components/OverseerPage/OverseerPage.test.tsx +57/-0","src/components/OverseerPage/OverseerPage.tsx +91/-0","src/components/shell/AppSidebar.tsx +3/-1","src/components/shell/MobileTabBar.tsx +3/-2","src/components/shell/shell.test.tsx +1/-1","src/constants.ts +2/-0","src/styles/overseer.css +59/-0"],"state":"OPEN","title":"feat: Spark Overseer, opt-in local model workload security observations"}

---- server/overseer/signals.js (head branch) ----
import { createHash } from 'node:crypto';

export const SIGNALS = Object.freeze({
  'inspection-gap': 'Bounded response inspection was incomplete',
  upload: 'Upload-capable action',
  'credential-access': 'Credential-path access',
  'metadata-access': 'Cloud metadata destination',
  'unlisted-destination': 'Destination outside the configured allowlist',
  'security-control-change': 'Security-control modification',
  'encoded-execution': 'Encoded command execution',
  'download-execute': 'Download piped to a shell',
});
const kinds = new Set(['execution', 'tool-proposal', 'coverage-gap', 'model-response']);
const metadataHosts = new Set(['169.254.169.254', '100.100.100.200', 'metadata.google.internal', '[fd00:ec2::254]', '[::ffff:a9fe:a9fe]']);

export function hostname(value) {
  try {
    const host = new URL(value.includes('://') ? value : `https://${value}`).hostname.toLowerCase().replace(/\.$/, '');
    return /^[a-z0-9.:[\]-]{1,253}$/.test(host) ? host : null;
  } catch { return null; }
}

/** Presentation hint only, NOT a public-suffix/security boundary. Match policy on the full hostname. */
export function destinationHint(value) {
  const host = hostname(value);
  if (!host) return null;
  if (/^[\d.]+$/.test(host) || host.includes(':') || !host.includes('.')) return host;
  return host.split('.').slice(-2).join('.');
}

/** Rules inspect bounded raw arguments locally. Never persist that input. */
export function analyzeAction(input, { allowedHosts = [] } = {}) {
  const parts = [];
  let size = 0;
  function text(value, depth = 0) {
    if (depth > 4 || size >= 65536 || parts.length >= 128) return;
    if (typeof value === 'string') {
      const part = value.slice(0, 65536 - size);
      parts.push(part); size += part.length;
      if (/^\s*[{[]/.test(part)) { try { text(JSON.parse(part), depth + 1); } catch { /* ordinary argument text */ } }
    } else if (Array.isArray(value)) value.slice(0, 128).forEach(item => text(item, depth + 1));
    else if (value && typeof value === 'object') { text(JSON.stringify(value), 5); Object.values(value).slice(0, 128).forEach(item => text(item, depth + 1)); }
  }
  if (input && typeof input === 'object') { const encoded = JSON.stringify(input).slice(0, 32768); parts.push(encoded); size += encoded.length; }
  text(input);
  const raw = parts.join('\n').slice(0, 65536);
  const lower = raw.toLowerCase();
  const signals = new Set();
  if (/--(?:data(?:-binary|-raw|-urlencode)?|upload-file|form)(?:[=\s"']|$)|(?:^|[\s"'])-[dfT](?:[\s"']|$)|\b(?:scp|sftp)\b|\b(?:requests|httpx)\.post\s*\(|["']?method["']?\s*[:=]\s*["']post/i.test(raw)) signals.add('upload');
  if (/(?:^|[\/\s"'])\.env(?:[\s"']|$)|\bid_(?:rsa|ed25519)\b|\.aws[\/]credentials|\/proc\/[^\s"']*environ|\.ssh[\/]/i.test(raw)) signals.add('credential-access');
  if (/\b(?:nft\s+flush|ufw\s+disable|iptables\s+-f)\b|\brm\b[^\n]{0,120}\boverseer\b/i.test(raw)) signals.add('security-control-change');
  if (/base64\s+(?:-d|--decode)|(?:b64decode|frombase64string)\s*\(/i.test(raw)) signals.add('encoded-execution');
  if (/\b(?:curl|wget)\b[^\n]{0,1024}\|\s*(?:sh|bash|zsh)\b/i.test(raw)) signals.add('download-execute');
  const allowed = new Set(allowedHosts.map(hostname).filter(Boolean));
  const destinations = new Set();
  for (const match of raw.matchAll(/https?:\/\/[^\s<>"'\\]+/gi)) {
    if (destinations.size >= 16) break;
    const host = hostname(match[0]);
    if (!host) continue;
    destinations.add(destinationHint(host));
    if (metadataHosts.has(host)) signals.add('metadata-access');
    if (!allowed.has(host)) signals.add('unlisted-destination');
  }
  // Non-URL endpoint spellings are useful indicators but not proof of a request.
  if (lower.includes('169.254.169.254') || lower.includes('metadata.google.internal')) signals.add('metadata-access');
  return { signals: [...signals], destinations: [...destinations], fingerprint: createHash('sha256').update(raw).digest('hex').slice(0, 24) };
}

export function safeModel(value) {
  return typeof value === 'string' && /^[a-z0-9][a-z0-9._/+-]{0,119}$/i.test(value) ? value : 'unspecified';
}

/** Treat producer journals as untrusted. Never copy arbitrary properties or prose. */
export function safeEvent(value, sparkId, now = Date.now()) {
  if (!value || value.version !== 1 || !kinds.has(value.kind) || !/^[a-f0-9-]{16,64}$/i.test(value.id ?? '')) return null;
  if (!Number.isFinite(value.timestamp) || value.timestamp < now - 86400000 || value.timestamp > now + 30000) return null;
  const signals = [...new Set((Array.isArray(value.signals) ? value.signals : []).filter(s => Object.hasOwn(SIGNALS, s)))];
  return {
    id: createHash('sha256').update(`${sparkId}:${value.id}`).digest('hex').slice(0, 24),
    timestamp: value.timestamp,
    sparkId,
    model: safeModel(value.model),
    kind: value.kind,
    stage: value.kind === 'model-response' ? 'response observed' : value.kind === 'coverage-gap' ? 'inspection partial' : value.kind === 'tool-proposal' ? 'proposed, not executed' : value.finished === true ? 'process exited' : 'process started',
    signals,
    severity: signals.some(s => ['metadata-access', 'credential-access', 'security-control-change'].includes(s)) ? 'high' : signals.length ? 'review' : 'recorded',
    destinations: [...new Set((Array.isArray(value.destinations) ? value.destinations : []).slice(0, 16).map(destinationHint).filter(Boolean))],
    fingerprint: /^[a-f0-9]{24}$/.test(value.fingerprint ?? '') ? value.fingerprint : null,
    exitCode: Number.isInteger(value.exitCode) && value.exitCode >= 0 && value.exitCode <= 255 ? value.exitCode : null,
  };
}

---- upstream README.md (first 130 lines) ----
# sparkDash ⚡ — Multi-unit monitoring dashboard for NVIDIA DGX Spark

<p align="center">
  <img src="https://img.shields.io/badge/platform-arm64-2d9d78?style=flat-square" alt="Platform: ARM64">
  <img src="https://img.shields.io/badge/React-19-58c4dc?style=flat-square&logo=react" alt="React 19">
  <img src="https://img.shields.io/badge/Express-5-000000?style=flat-square&logo=express" alt="Express 5">
  <img src="https://img.shields.io/badge/license-Apache%202.0-2d9d78?style=flat-square" alt="Apache License 2.0">
  <br>
  <sub>by <a href="https://x.com/MiaAI_lab">Mia'a AI Lab</a></sub>
  <br><br>
  <a href="https://x.com/MiaAI_lab" target="_blank" style="display:inline-block;margin:0 8px;vertical-align:middle;"><img src="https://img.shields.io/badge/Follow%20me%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow Mia on X" height="28" style="height:28px;width:auto;vertical-align:middle;border:0;" /></a>
</p>

<p align="center"><sub>macOS (darwin) SSH collectors authored by <a href="https://github.com/MikeGibbsOnyx">C. Michael Gibbs</a> and <a href="https://x.com/nyxvoss_ai">Nyx Voss</a> (Onyx AI Labs) — <a href="https://github.com/MikeGibbsOnyx/sparkDash/commits?author=MikeGibbsOnyx">commits</a>. sparkDash by <a href="https://github.com/MiaAI-Lab">Mia's AI Lab</a>.</sub></p>

sparkDash is a real-time web dashboard for one or more **NVIDIA DGX Spark (GB10)** machines in a single browser window. It streams GPU, CPU, unified memory, storage, network, and local LLM metrics — and lets you add, edit, reorder, or remove Sparks from the UI without restarts or code changes.

It also supports **non-Spark units**: any Linux machine with an NVIDIA GPU (e.g. a workstation with a dedicated RTX/L-series card) can be added as a **dedicated GPU host** and monitored the same way via SSH and `nvidia-smi`. For these units the dashboard correctly separates **RAM** (system memory) from **VRAM** (discrete GPU memory).

Monitored units run **Linux**, **macOS**, or **Windows** (a Windows PC with an NVIDIA GPU — or an AMD-iGPU Windows host like a Strix Halo, whose GPU usage comes from Windows' GPU engine counters; see [Windows PCs](#windows-pcs)).

**Apple Silicon Macs** (for example a Mac Studio serving models with [oMLX](https://github.com/jundot/omlx)) can be added as a **Mac** unit. They are read over SSH with stock macOS tools, optionally plus a small [on-device agent](agents/macos/README.md) that adds the model-runtime inventory and explicit unavailable readings. See [Mac units](#mac-units).

<img src="./.github/screenshot.png" alt="sparkDash Overview page with multiple DGX Spark units, GPU metrics, and LLM status">

### LLM Prompt Showcase

<a href="./.github/llm-showcase.mp4">
  <img src="./.github/llm-showcase.gif" alt="LLM Prompt Showcase — multi-terminal streaming demo (click for MP4)" width="100%">
</a>

<p align="center"><sub><a href="./.github/llm-showcase.mp4">Watch the MP4</a></sub></p>

---

## Table of contents

- [Latest version changelog](#latest-version-changelog)
- [Features](#features)
- [LLM server presets & backend auto-detection](#llm-server-presets--backend-auto-detection)
- [ComfyUI monitoring](#comfyui-monitoring)
- [Hermes Agent monitoring](#hermes-agent-monitoring)
- [Tailnet monitoring](#tailnet-monitoring)
- [Tailscale Serve (HTTPS)](#tailscale-serve-https)
- [Mobile PWA (install on a phone)](#mobile-pwa-install-on-a-phone)
- [Kiosk (wall display)](#kiosk-wall-display)
- [Glance integration](#glance-integration)
- [Home Assistant](#home-assistant)
- [Quality bench](#quality-bench)
- [Prometheus](#prometheus)
- [Alert notifications](#alert-notifications)
- [Power meters (wall power)](#power-meters-wall-power)
- [RoCE / RDMA monitoring](#roce--rdma-monitoring)
- [Intel Arc GPUs](#intel-arc-gpus)
- [Windows PCs](#windows-pcs)
- [Full changelog](./CHANGELOG.md)
- [Quick start](#quick-start)
- [Architecture](#architecture)
- [Tech stack](#tech-stack)
- [Repository layout](#repository-layout)
- [REST API](#rest-api)
- [Configuration](#configuration)
- [Security](#security)
- [Scripts](#scripts)
- [How it works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Latest version changelog

### Version 2.70.0
- **Decode benchmark**: temperature (default 0.7) and thinking on or off are selectable for every type; the copied result text and the share card show both.
- **NVIDIA Flare** is detected and its tok/s monitored from `/metrics`.
- **Tool Eval Bench**: compare a run on one Spark with a run from another, and expand the scenario list to a taller view.
- **Overview** cards show CPU temperature and power; a **Cost compare** page prices fleet usage as any hosted model; Radiance and Strata engines are recognised.

### Version 2.50.0
- **Tool Eval Bench: Show card** turns a finished result into a share image (score, rating, outcomes, safety warnings, categories) you can copy or save as a PNG.
- **Tool Eval Bench: comparison card**: tick two runs in History and get one image of the change between them.
- **GPU clock cap** can be run on the Spark yourself, or the dashboard asks for the sudo password when a unit has no passwordless sudo.

### Version 2.40.1
- **Temps page** with day and week GPU temperature graphs for every unit, backed by a minute-resolution history kept for 7 days.
- **GPU clock cap** set with `nvidia-smi -lgc` shows on each unit (read-only).
- **Mac units** come online and report CPU, GPU and RAM through macmon.
- **Fixes**: GPU and energy data on remote units whose login shell is zsh, and the TensorFold Slots tile now counts occupied lanes.

### Version 2.40.0
- **Hide any Overview panel**: Settings has switches for Recent activity and for each of the four tiles (Fleet decode, Fleet power, Memory in use, Tokens in last 24 hours), next to Fleet energy and LLM token totals.
- **LM Studio and Ollama** are detected by their own endpoints, so they are no longer labelled SGLang or vLLM; LLM panels match their port, and the Add wizard and LLM panels have LM Studio / Ollama / TensorFold port presets.
- **Windows PCs with an AMD iGPU (Strix Halo)** show GPU use and memory from Windows' GPU counters. Windows setup docs now cover the `administrators_authorized_keys` gotcha.

### Version 2.32.0
- **LLM panel**: an engine that only SSH can reach (a remote unit behind a NAT that forwards just SSH) is now monitored through an SSH forward, with a **via SSH** chip; TensorFold prefill tok/s counts only computed tokens, so prefix-cache hits no longer read as 100k+.
- **Decode benchmark**: live generation tok/s is measured from the run's own streams, so it no longer shows 0.
- **Health**: a finding is held for 90 s, so a reading sitting on a threshold does not flap and spam Activity.
- **iPhone app**: the header clears the status bar and the home-screen icon is the logo. Dropping a Spark after dragging it in the sidebar no longer opens it.

### Version 2.31.0
- **RoCE / RDMA panel** for Sparks: link state and rate, traffic, drops, PFC and QoS settings and the RDMA counters per port, with two health findings (a link went down, packets being dropped). See [RoCE / RDMA monitoring](#roce--rdma-monitoring).
- **Time zone setting** for the Tokens, Energy and Activity charts, so the 24 h charts line up with your local time.
- **`/metrics`** now shows when each collector last returned real data, so a stuck GPU poll can be alerted on while SSH liveness still passes.
- Spark page: Unified memory, CPU and Models share one row; CPU and RAM sit side by side on GPU hosts; the GPU history chart fills its panel; Windows PCs got a first real-hardware pass.

### Version 2.30.0
- **Windows PCs as units**: a Windows PC with an NVIDIA GPU can be monitored over its built-in OpenSSH server (GPU, RAM, CPU load, disks, network, shutdown). See [Windows PCs](#windows-pcs).
- **Mobile app**: sparkDash installs as a PWA over HTTPS (for example Tailscale Serve).
- **Monthly energy history** with a month/year view, **Prometheus `/metrics`** (opt-in), per-GPU graphs on multi-GPU hosts, a model picker in the decode benchmark, per-Spark `llmHost`, and **Restart sparkDash** from the UI after a fleet change.
- The Settings poll interval now really sets the polling rate; the Fleet energy card explains partial coverage.
- Fixes: "Frontend not built" after a Docker upgrade, the SSH tunnel for benchmarks, model launchers inheriting `PORT=5555`, and a token-protected remote bind showing a blank page. Everything since 2.0.0 is in the [CHANGELOG](./CHANGELOG.md).

### Version 2.0.0 — a new sparkDash
- **New shell**: sidebar, command palette (Ctrl/⌘ K), four themes (White, Light, Dark, OLED), smooth page transitions and real links everywhere (right-click, new tab).
- **Rebuilt Overview**: per-Spark cards with the model row, head/worker relations, a Model/System memory bar, and a launcher to load a model from the card.
- **Benchmarks section**: Decode, Prefill, Quality and the new **Tool Eval Bench** (trials, side-by-side compare, one-click upgrade).
- **Showcase** is now an in-app page with much smoother streaming; **Token totals**, **Fleet energy** and **Activity** get their own pages.
- Start and stop your own LLMs from the dashboard; live prefill tok/s during long prefills; Quality bench with GSM8K and MMLU.
- **Health findings** per Spark (hot GPU, low unified memory under 3 GB, Xid/OOM errors, slow links) and Activity events for them; **Clear / Reset** for Activity, Fleet energy and Token totals.
- **Mobile**: docked tab bar with iOS-style motion, a Stats tab (Token totals, Fleet energy, Activity) and a rebuilt Spark page.

Full history: [CHANGELOG.md](./CHANGELOG.md)

---

## Features

| Area | What you get |

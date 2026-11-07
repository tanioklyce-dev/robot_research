---
title: "XPolicyLab/XPolicyLab — a unified standard and open ecosystem for robot policy evaluation and deployment (GitHub README)"
type: source
url: https://github.com/XPolicyLab/XPolicyLab
fetch_url: https://raw.githubusercontent.com/XPolicyLab/XPolicyLab/main/README.md
local_path: raw/2026-11-07-xpolicylab-readme.md
sha256: 91e73acf5fd260d220754840b4ade375579b551017f144d622a3b064bf0ba5aa
author: "XPolicyLab Community; core lead authors Tianxing Chen, Yue Chen, Tian Nian, Zijian Cai, Guangyu Chen, Wenwei Lin, Qiwei Liang (MMLab@HKU and THU)"
published: 2026-02-08
venue: "GitHub repository (Apache-2.0); paper arXiv 2608.09892; Best Tool Paper, IROS 2026 'Building Scalable Infrastructure for Robot Learning' workshop"
format: "README (551 lines), plus a bundle of AGENTS.md, CONTRIBUTING.md, both coding-agent skills, model_template.py, setup_policy_server.py, the websocket codec, demo deploy.yml, robot-info table, the GPT-6 Astra adapter README and GitHub API metadata"
license: Apache-2.0
related_raw: "raw/2026-11-07-xpolicylab-bundle.md"
github_stats: "541 stars, 200 forks, 46 open issues; created 2026-02-08; main head 6baccd5 (2026-11-03); ~376 commits; top committers TianxingChen 164, yuechen0614 33, FlowsMple 18"
tags: [xpolicylab, robodojo, robotwin, rmbench, policy-serving, evaluation-infrastructure, benchmark, leaderboard, vla, world-action-model, websocket, msgpack, lerobot, adapter, coding-agents, agent-skills, gpt-6-astra, apache-2]
ingested: 2026-11-07
---

# XPolicyLab/XPolicyLab

## Summary

**[XPolicyLab](../entities/xpolicylab.md)** is the policy-side half of the [RoboDojo](../entities/robodojo.md) and [RoboTwin](../entities/robotwin.md) leaderboards. It is a repository of **adapters**, one directory per robot policy, plus a websocket policy server that lets each model run in its own conda or uv environment while the simulator or robot client runs in another, on the same machine or a different one. The pitch is on the teaser figure: connecting N policies to M evaluation environments *"from O(N×M) down to O(N+M)."*

As of November 2026 the README lists **77 integrated policies** plus a reference `demo_policy`. They span VLAs, world-action models, imitation-learning baselines and memory-augmented policies. That number has grown fast: the RoboDojo paper (frozen 2026-07-03) integrated 30, and RoboDojo's branch README says *"40+"*. A PR to this repo, with a downloadable checkpoint, is the **only** way onto either official leaderboard.

The repository's most instructive content is not the policy list. It is the set of contracts the maintainers had to write down after things went wrong: one image codec that every path must use, two robot-dimension files that must agree, and a transport that answers retried requests from a cache. It also ships its own coding-agent skills, so new adapters are increasingly written by Claude Code, Codex or Cursor against a written standard.

## Key claims

### Architecture
- **Two sides, one wire.** `policy/<POLICY>/model.py` is served by a policy server. `deploy.py` is the environment-side loop that turns benchmark observations into server calls. They talk over **websocket** (`protocol: ws`); a `legacy_tcp` path remains only for unmigrated adapters.
- **One adapter shape.** Each `policy/<POLICY>/` holds `install.sh`, optional `process_data.sh` and `train.sh`, `eval.sh`, `setup_eval_policy_server.sh`, `setup_eval_env_client.sh`, `deploy.yml`, `deploy.py` and `model.py`. `bash scripts/create_policy.sh <NAME>` copies `demo_policy`.
- **The model contract.** `Model(ModelTemplate)` implements `__init__(model_cfg)`, `update_obs`, `update_obs_batch`, `get_action` (one **action chunk** as a list of dicts), `get_action_batch(env_idx_list)` and `reset()`. Optional hooks are `prepare_case` and `on_trial_end`. `reset()` takes no arguments; a policy that needs a first observation resets and then takes a normal `update_obs`.
- **Ten positional arguments, everywhere.** `eval.sh` takes `bench_name task_name ckpt_name env_cfg_type action_type seed policy_gpu_id env_gpu_id policy_env eval_env`. The same names flow through data conversion and training, and checkpoints land in `checkpoints/<bench>-<ckpt>-<env_cfg>-<action>-<seed>/`.
- **`EVAL_ENV_TYPE`.** `sim` (default) is simulator-backed, `debug` is an offline wiring check with *"no Isaac, no robot, just shapes and IO,"* and `real` is the real-robot client where the hardware integration exists.
- **Packaging.** The `xpolicylab` package (v0.0.1, Python ≥ 3.10) depends only on numpy, PyYAML, OpenCV-headless, h5py, websockets, msgpack, msgpack-numpy and pydantic. The checkout is always used as a subpackage inside a parent workspace, which owns `env_cfg/`.

### Transport
- **Retries are idempotent.** Each request carries a `request_id`. The client reuses it across reconnects, and the server answers duplicates from a cache instead of running a non-idempotent call twice.
  - A `timeout` is the exception: the server may still be running the call, so it is fatal for that trial.
  - If a reconnect lands on a **different server process**, the client raises `ServerRestartedError`, because the model state is gone.
- **Cold start.** The server loads the model before opening its port. Clients retry for up to 15 minutes by default, and `eval.sh` waits on `wait_for_policy_server.sh`.
- **Serialization** is msgpack with numpy support. Three quirks are documented: tuples arrive as lists, decoded arrays are read-only, and int dict keys arrive as strings (to match the old JSON codec).
  - **Object-dtype arrays are refused in both directions** (codec.py). That closes off msgpack-numpy's pickle path, so a hostile frame cannot reach `pickle.loads`. The legacy TCP server has `pickle.loads` commented out and uses JSON.
- **Split-machine deployment.** Start the policy server with host `0.0.0.0` on the GPU machine, and point the client at its real IP. That keeps Isaac Sim or robot drivers on one box and a heavy VLA on another.
  - **No authentication or TLS.** A search of the websocket server, client and codec, and the TCP server, finds no auth, token or TLS handling (my own check of the bundle; the README doesn't discuss it). The server code also falls back to `0.0.0.0` when `host` is unset, though `demo_policy/deploy.yml` sets `localhost`.
  - **Implication.** In split mode, anyone who can reach the port can drive the model's `update_obs` and `get_action`.

### Data contracts
- **Observation and trajectory formats.** Both are standardized as nested dicts:
  - `vision/<camera>/{color, depth, intrinsic_matrix, extrinsics_matrix}` and `state/{left,right}_{arm_joint,ee_joint,ee,tcp,delta_ee}_*`, plus a `mobile/` block for base pose and twist.
  - Poses are `[x, y, z, qw, qx, qy, qz]`.
  - Runtime observations say `extrinsics_matrix`, while trajectory files say `extrinsic_matrix`.
- **The RGB rule and why it is so loud.** Stored JPEG bits come in two byte formats:
  - **Legacy:** an RGB array handed to `cv2.imencode`, which reads it as BGR, so the bytes are channel-reversed.
  - **Standard:** written by `encode_image_bit`, which stamps a JPEG `COM` segment containing `XPL-RGB1`.
  - Legacy data can't be migrated losslessly, so both formats coexist in the same training runs.
  - **The consequence.** Decoded pixels look the same to the eye, so any caller-side `COLOR_BGR2RGB` is right on one format and silently wrong on the other. *"A PIL-based loader tested against fresh data looks perfect and then quietly corrupts older episodes."*
  - **The enforced rule.** `cv2.imdecode` may not appear outside `utils/process_data.py`. The commit history shows the rule arriving in three steps: RGB unified 2026-08-04, restated 08-07, marker added 09-09. That matches the RGB fix RoboDojo and RoboTwin shipped together in September.
- **Robot dimensions live in two files** that must agree. `<parent>/env_cfg/robot/_robot_info.json` is read at runtime and during conversion, and `utils/robot/_robot_info.json` is read by `train.sh`; the two `get_action_dim` entry points read different files. The bundled table covers Piper, ARX X5 and Piper X (6+1 per arm), Franka (7+1), ALOHA-AgileX, and `tianji_marvin_wuji` (7-DoF arms with **20-DoF** hands).
- **Official LeRobot converters (v2.1 and v3.0).** They emit `observation.state`, `action` and three camera keys.
  - State is the concatenation left arm, left gripper, right arm, right gripper. It is zero-padded to the widest matched robot under `robot_type: unified_robot`, so one dataset can mix embodiments.
  - Missing cameras are filled with black frames, and the default codec is AV1.
  - They handle **joint-space bimanual only.**
- **Data without a simulator.** `download_robodojo_data.sh` pulls RoboDojo simulator exports (HDF5, LeRobot v2.1, LeRobot v3.0) and the real-world HDF5 set, so model-side development can start without Isaac Sim.

### Benchmarks served
- **RoboDojo:** 42 sim tasks on five capability dimensions, plus 18 real tasks on three bimanual embodiments.
- **RoboTwin 2.0:** 50 tasks, clean and randomized.
- **RMBench:** nine memory-dependent dual-arm tasks on RoboTwin 2.0 (arXiv 2603.01229), with reference policy Mem-0.
- **Infrastructure targets:** RLinf (*"coming soon"*) and StarVLA.

### The policy zoo (78 directories, including `demo_policy`)
- **Familiar names with wiki pages:**
  - π0, π0-FAST and π0.5;
  - OpenVLA-OFT, SmolVLA, X-VLA, RDT-1B, GR00T-N1.7 and MolmoAct2;
  - DreamZero, Evo-1, ACT and DP.
- **At least ten world-action models by name:** AHA-WAM, FastWAM, X-WAM, UniWAM, OpenWAM, PatchWAM-Lite, HWM-CogWAM, EWAM, PICA-WAM and PrismWAM. GigaWorld-Policy, LingBot-VA and CloudRobo-WM are video-model policies too.
- **The rest are mostly 2026 Chinese industrial and academic releases:** Xiaomi-Robotics-0/1, Meituan-Robotics-0, Hy-Embodied-0.5-VLA (Tencent), InternVLA-A1/A1.5, GO-1, G0/G0.5 (Galaxea), LingBot-VLA, Spirit v1.5, Wall-X, DM0 and others.
- **`GPT-6-Astra-Direct-EEF`: a frontier LLM as a leaderboard policy.** It comes from the RoboProbe / RoboDojo team, with the paper *"An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond"* (arXiv 2609.24170, not ingested).
  - **How it acts.** It is eval-only and RGB-only, with no checkpoint and no training. The model calls a single `move_eef` tool naming world-frame grasp-point poses, and RoboDojo's local Cartesian planner turns them into joint paths. `L4_INSPECT_PLANNER` switches between `gpt-6-astra` and `gpt-5.5-2026-04-24`.
  - **Where inference runs.** The LLM runs on the **eval client**, not the policy server, keyed by `ARK_API_KEY`.
  - **The API path is a third-party gateway.** The shared helper `utils/openai_responses.py` documents two quirks *"observed against ByteDance AIDP,"* which load-balances across Azure OpenAI resources. One rule follows: do not replay server-assigned item IDs. The helper also explains why it uses the Responses API: *"chat/completions rejects any `reasoning_effort` other than `none` alongside tools."*

### Contributions and coding agents
- **PR checklist.** A submission must carry the decode/encode grep, `bash -n` plus `py_compile`, an `EVAL_ENV_TYPE=debug` closed-loop log, and, for the leaderboards, a **checkpoint download script** (Hugging Face or ModelScope).
- **Two in-repo skills.** `xpolicylab-model-integration` (*"Integrate <POLICY> into XPolicyLab"*) and `xpolicylab-adapter-check` (a nine-point audit) live in `.agents/skills/`, symlinked from `.claude/skills` and `.cursor/skills`.
  - **AGENTS.md** is the always-on rule set. The root `CLAUDE.md` is a single line, `@AGENTS.md`.
  - **What the rule set covers.** It repeats the image, path and dimension rules with the reasons attached, and requires bilingual README edits (English wins on conflict).
- **Recent commits** include *"Delete Useless SHA256 Information"* (#227, 2026-11-03) and renaming physicalRSI to PhysicalRSI while *"list[ing] the 77 integrated policies."*

## Entities mentioned
- [XPolicyLab](../entities/xpolicylab.md) · [RoboDojo](../entities/robodojo.md) · [RoboTwin](../entities/robotwin.md)
- Policies with pages: [π0](../entities/pi-zero.md), [π0.5](../entities/pi-zero-5.md), [OpenVLA-OFT](../entities/openvla-oft.md), [SmolVLA](../entities/smolvla.md), [X-VLA](../entities/x-vla.md), [RDT](../entities/rdt.md), [GR00T](../entities/nvidia-groot.md), [MolmoAct2](../entities/molmoact2.md), [DreamZero](../entities/dreamzero.md), [Evo-1](../entities/evo-1.md), [ACT](../entities/act.md), [Diffusion Policy](../entities/diffusion-policy.md)
- Embodiments: [AgileX Piper](../entities/agilex-piper.md), [Franka Panda](../entities/franka-panda.md), [ALOHA](../entities/aloha.md); ARX X5 (no page)
- [LeRobot](../entities/lerobot.md) (official v2.1 and v3.0 converters) · [OpenAI](../entities/openai.md) (GPT-6 Astra adapter)
- No pages: RMBench, RLinf, StarVLA, most of the 77 policies

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): the serving layer and submission rules behind two leaderboards.
- [World-action model](../concepts/world-models/world-action-model.md): ten-plus WAM adapters sharing one harness with VLAs.
- [Agent skills](../concepts/agents/agent-skills.md): repo-shipped skills that turn a written standard into the instructions an agent follows when building or checking an adapter.
- [Code as policy](../concepts/agents/code-as-policy.md): a frontier LLM entered on a VLA leaderboard through a single end-effector tool and a planner.

## Open questions
- **What does GPT-6 Astra score on RoboDojo,** and how much of that is the Cartesian planner? The adapter is a textbook case of the code-as-policy [abstraction confound](../concepts/agents/code-as-policy.md#the-abstraction-confound--the-finding-that-reframes-the-lineage-above). Ingest 2609.24170 and the leaderboard row together.
- **Are early leaderboard entries affected by the legacy-JPEG problem?** Before 2026-08-04, any adapter that "fixed" colors by hand could have trained or evaluated on channel-swapped images. The repo doesn't say whether any reported numbers were affected.
- **The policy server has no authentication.** For real-robot evaluation in split mode, the network between policy and robot client is the only boundary. Run it on a private link or behind an authenticated tunnel.
- **How faithful are the adapters?** Each one re-implements a model's preprocessing outside its home repo, and community adapters are reviewed against a checklist rather than against upstream numbers. The single-digit RoboDojo scores need adapter fidelity ruled out before they can be read as model capability. One test would be per-adapter parity on the model's own benchmark.
- **The paper (2608.09892) is not yet ingested.**

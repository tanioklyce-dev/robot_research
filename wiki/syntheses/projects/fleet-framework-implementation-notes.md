---
title: Fleet framework — implementation notes (MCP tool schema + scheduled training on the Spark)
type: synthesis
created: 2026-07-04
updated: 2026-07-04
tags: [project-scope, implementation, mcp, tool-schema, so-arm101, lerobot, rosetta, dgx-spark, scheduled-training, hil-serl, systemd, async-inference, fleet]
---

# Fleet framework — implementation notes

Two concrete build-outs of the [Fleet agentic control framework](fleet-agentic-framework.md): the **ROS 2↔MCP tool schema** for the SO-ARM101 robots ([XLeRobot](../../entities/xlerobot.md), [LeKiwi](../../entities/lekiwi.md)), and the **scheduled-training pipeline** on the [DGX Spark](../../entities/dgx-spark.md). The parent page has the architecture; this page has the code shapes.

> [!note] Version caveat
> [LeRobot's CLI was refactored across versions](../../sources/nvidia-jetson-ai-lab-lerobot.md) — treat exact `lerobot-train` flag names as *current-version, verify against your install*. The shapes are stable; the spellings drift. Likewise the MCP wire format follows Anthropic's Model Context Protocol (`tools/list` / `tools/call`, tool = `{name, description, inputSchema}`).

---

## Part 1 — MCP tool schema for the SO-ARM101 robots

### Design principles

1. **Semantic tools only; no raw joint control on the default surface.** The tool set *is* the safety boundary — the [Gemini-ER-on-Spot property](../../entities/gemini-robotics.md) ("can't invent capabilities beyond the API"). `move_joint(angles)` lives behind a gated `admin` toolset.
2. **Every action tool returns a structured `{status, reason, observation}` envelope**, not prose — this is what enables the [closed-loop replanning that's under-documented in every deployed stack](../agents/llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources).
3. **Deterministic dispatch** — validate args against the JSON Schema, call a ROS 2 action; never `eval` on model output (the [RCE hazard both Hiwonder kits have](../agents/llm-agent-architecture-across-stacks.md#implementation-hazards-visible-in-the-sources)).
4. **One server binary, config-parameterized per embodiment** — the arm set (`["left","right"]` for XLeRobot, `["main"]` for LeKiwi) drives which tools appear in `tools/list`.
5. **Long-running actions block with a server-side timeout**; `stop` is out-of-band.

### Tool catalog

| Tool | Kind | Underlying ROS 2 |
|---|---|---|
| `get_robot_state` | read, fast | `/joint_states`, `/odom`, `/battery` |
| `list_visible_objects` | read, fast | detector/VLM service over camera topics |
| `capture_view` | read, returns image | camera topic → MCP image content |
| `navigate_to` | action, long | Nav2 `NavigateToPose` |
| `explore` | action, long | frontier explorer node |
| `pick_object` | action, long | [Rosetta](../../entities/rosetta.md) `rosetta_client_node` (ACT/SmolVLA policy) |
| `place_object` | action, long | Rosetta `rosetta_client_node` |
| `handover` | action, long | **dual-arm only** (XLeRobot); absent on LeKiwi |
| `say` | action, fast | TTS node |
| `record_episode` | control | Rosetta `episode_recorder_node` → MCAP |
| `report_outcome` | control | HIL-SERL reward channel |
| `stop` | out-of-band | e-stop / action-cancel on all servers |

### Full schemas (`tools/list` entries)

The description field is prompt-visible, so it encodes hardware facts (the [Spot lesson: docstrings carry hardware facts](../../entities/gemini-robotics.md)).

```json
{
  "name": "pick_object",
  "description": "Grasp a single object with one arm using the learned manipulation policy. The object must currently be visible (call list_visible_objects first). Blocks until the grasp completes or times out (~30s). On XLeRobot, omit 'arm' to let the server pick the nearer arm. Returns whether the gripper is holding the object.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "object_id": {"type": "string", "description": "An id returned by list_visible_objects (e.g. 'obj_3'), NOT a free-text name."},
      "arm": {"type": "string", "enum": ["left", "right"], "description": "Which arm. Omit to auto-select. (XLeRobot only; absent on single-arm robots.)"}
    },
    "required": ["object_id"]
  }
}
```
```json
{
  "name": "navigate_to",
  "description": "Drive the mobile base to a named location or an (x,y,theta) map-frame pose. Blocks until arrival or failure. Does NOT move the arm. Use before pick/place when the target is out of reach.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "location": {"type": "string", "description": "A named waypoint from the semantic map (e.g. 'kitchen_counter'). Prefer this over raw poses."},
      "pose": {"type": "object", "properties": {"x": {"type": "number"}, "y": {"type": "number"}, "theta": {"type": "number", "description": "yaw in radians"}}, "required": ["x", "y", "theta"]}
    },
    "oneOf": [{"required": ["location"]}, {"required": ["pose"]}]
  }
}
```
```json
{
  "name": "list_visible_objects",
  "description": "Detect objects currently in view across all cameras. Returns ids, labels, confidences, base-frame positions. Call before any pick; ids are ephemeral and expire when the scene changes.",
  "inputSchema": {
    "type": "object",
    "properties": {"query": {"type": "string", "description": "Optional open-vocabulary filter (e.g. 'sock', 'anything on the floor'). Omit to list everything."}}
  }
}
```

### Uniform return envelope

Every action tool returns this as MCP structured content (plus a short text block). It is what makes replanning possible:

```json
{
  "status": "success | failed | timeout | rejected",
  "reason": "ok | object_not_visible | no_grasp_found | gripper_slipped | unreachable | path_blocked | precondition_failed",
  "observation": {
    "gripper_holding": true,
    "base_pose": {"x": 2.1, "y": 0.4, "theta": 1.57},
    "image_ref": "frame://wrist/17234.jpg",
    "duration_s": 8.3
  }
}
```

A failed `pick_object` returns `{"status":"failed","reason":"gripper_slipped","observation":{"gripper_holding":false}}` — and the agent's next thought becomes "re-detect and retry with the other arm," the [error-recovery-via-replanning](../../sources/gemini-robotics-1-5-report.md) behavior Gemini Robotics 1.5 gets from thinking traces.

### Long-running actions & the stop path

`pick`/`navigate` take seconds; MCP is request/response, so **block until done** (agent loops are turn-based; a `task_id`+poll design just adds round-trips). The catch: a blocking call can't also receive a cancel — so **`stop` is out-of-band** (a ROS 2 topic / second MCP session / hardware e-stop) that cancels the in-flight action and the policy server. Never route emergency-stop through the channel that's blocked on the action.

### Per-embodiment parameterization

One server, config-driven; `tools/list` is generated from it, so the LLM only sees tools the robot can do:

```yaml
# xlerobot.mcp.yaml
embodiment: xlerobot
arms: [left, right]                              # pick/place expose 'arm'; handover listed
policy_endpoint: grpc://spark.local:8080/soarm_tidy_act
cameras: [head, left_wrist, right_wrist]
```
```yaml
# lekiwi.mcp.yaml
embodiment: lekiwi
arms: [main]                                     # 'arm' enum omitted; handover NOT listed
policy_endpoint: grpc://spark.local:8080/soarm_tidy_act   # same checkpoint — shared SO-ARM101
cameras: [head, wrist]
```

Because XLeRobot and LeKiwi share the SO-ARM101 arm, they can point at the **same policy checkpoint** — the cross-embodiment bet from the parent synthesis.

### Worked trace ("put the sock in the hamper")

```
STT → agent goal: "put the sock in the hamper"
1. list_visible_objects{query:"sock"}       → {obj_5: sock, conf .91}
2. pick_object{object_id:"obj_5"}           → {failed, no_grasp_found}     # too far
3. navigate_to{location:"floor_near_couch"} → {success}
4. list_visible_objects{query:"sock"}       → {obj_2: sock, conf .88}
5. pick_object{object_id:"obj_2"}           → {success, gripper_holding:true}
6. navigate_to{location:"laundry_hamper"}   → {success}
7. place_object{target:"laundry_hamper"}    → {success, gripper_holding:false}
8. say{text:"Done — the sock is in the hamper."}
```

The [Gemma-4-E4B](../../entities/gemma4.md) agent only emits these calls; Nav2 + the LeRobot policy do the work below the MCP line.

---

## Part 2 — Scheduled training on the DGX Spark

### Pipeline

```
robots ──push episodes──▶ HF Hub (per-robot dataset repos)
                               │
        DGX Spark nightly ◀────┘  (systemd timer)
        1. pull + diff (enough new episodes?)
        2. assemble mix (community pretrain + this robot's data)
        3. lerobot-train (ACT / SmolVLA fine-tune), log to W&B
        4. offline eval on a held-out split
        5. PROMOTION GATE: new ≥ deployed baseline?  ──no──▶ alert, keep old
                                   │yes
        6. push checkpoint to HF Hub (model repo)
        7. hot-swap the async policy server ──▶ robots pull on next idle
```

A **timer + a gate + HF-as-the-bus** — that's the "minimal human interaction" property. Humans touch it only on gate failures or curation.

### Trigger: systemd timer (over cron or webhook)

A systemd timer gives logs (`journalctl`), ordering, and `Persistent=true` catch-up. HF webhooks couple training to collection timing + network reachability; nightly batching matches "collect all evening, train overnight."

```ini
# /etc/systemd/system/fleet-train.timer
[Unit]
Description=Nightly fleet policy retraining
[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
[Install]
WantedBy=timers.target
```
```ini
# /etc/systemd/system/fleet-train.service
[Unit]
Description=Fleet retraining job
After=network-online.target
[Service]
Type=oneshot
User=fleet
Environment=HF_TOKEN=%S/fleet/hf_token WANDB_API_KEY=%S/fleet/wandb
ExecStart=/opt/fleet/train_fleet.sh
TimeoutStartSec=6h
```

### The job (`train_fleet.sh`) with a promotion gate

```bash
#!/usr/bin/env bash
set -euo pipefail
ROBOTS=(soarm_tidy rosorin_tidy)          # XLeRobot+LeKiwi co-trained as soarm_tidy
CKPT_ROOT=/spark/checkpoints
MIN_NEW_EPISODES=25

for task in "${ROBOTS[@]}"; do
  repo="myfleet/${task}"
  new=$(python /opt/fleet/count_new_episodes.py "$repo" "$CKPT_ROOT/$task/last_trained.json")
  [ "$new" -lt "$MIN_NEW_EPISODES" ] && { echo "skip $task ($new new)"; continue; }

  out="$CKPT_ROOT/$task/$(date +%F_%H%M)"
  lerobot-train \
    --dataset.repo_id="$repo" \
    --policy.type=act --policy.device=cuda \
    --batch_size=64 --steps=100000 \
    --output_dir="$out" \
    --wandb.enable=true --job_name="$task"

  score=$(python /opt/fleet/eval_policy.py "$out" "$repo:val")
  base=$(cat "$CKPT_ROOT/$task/deployed_score" 2>/dev/null || echo 0)
  if python -c "import sys; sys.exit(0 if $score >= $base else 1)"; then
      hf upload "myfleet/${task}_act" "$out/pretrained_model"
      echo "$score" > "$CKPT_ROOT/$task/deployed_score"
      systemctl restart "policy-server@${task}"     # Rosetta gRPC / LeRobot PolicyServer
      echo "promoted $task @ $score ($new new episodes)"
  else
      echo "GATE FAIL $task: new=$score < deployed=$base — kept old" | /opt/fleet/notify.sh
  fi
done
```

The **promotion gate** ("new must beat deployed on a held-out split") is the safety valve for unattended auto-deploy. Pair it with a periodic *real* smoke test — offline metrics under-predict real success.

### DGX Spark specifics

- **Stack**: aarch64, CUDA 13, Python 3.12 ([per the Isaac-GR00T platform matrix](../../sources/isaac-gr00t-github.md)) — ARM+CUDA-13 PyTorch wheels; bf16.
- **Capacity**: 128 GB unified. ACT (52 M) trains in minutes; SmolVLA (450 M) fine-tune ~1–2 h; even a π0-class (3.5 B) fine-tune fits thanks to unified memory. All robots train sequentially in one overnight window on a single Spark.
- **Double duty**: the Spark also *serves* the [async policy](../../entities/lerobot.md) (`policy-server@task`), so retrain + serve are co-located and `systemctl restart` is the hot-swap.

### Cross-embodiment shortcut

All three robots share the SO-ARM101 arm (ROSOrin Pro [after the arm swap](fleet-agentic-framework.md)) → **co-train one policy** on the union of all dataset repos (`myfleet/soarm_tidy`) and deploy the same checkpoint fleet-wide, pooling every robot's data into one model. This is why the loop above lists a single `soarm_tidy` task instead of one per robot — hardware homogenization turned the [GR00T-style cross-embodiment problem](../../entities/nvidia-groot.md) into a config detail. (Match the camera setup across robots so the shared observation space lines up.)

### The minimal-human loop, closed

The nightly job consumes whatever the fleet produced. To keep producing useful data without teleoperating every episode: **[HIL-SERL](../../entities/lerobot.md)** via [Rosetta's HIL contract](../../entities/rosetta.md) (intervention buttons + reward) — robots run autonomously, a human occasionally taps "intervene" / thumbs-up-down, and those reward-labeled episodes flow into the same HF repos the nightly job reads. Human effort drops from "collect N demos" to "correct the occasional failure."

### Gotchas

- **Flag drift** — verify `lerobot-train` flags against your installed version.
- **Dataset versioning** — pin the HF dataset revision per run; `count_new_episodes.py` should compare commit hashes, not just counts, so a promoted checkpoint is reproducible.
- **Gate metric ≠ real success** — offline val is a proxy; weekly real-robot smoke test before trusting auto-promotion near breakables.
- **Silent data poisoning** — an autonomous collection loop can flood the repo with bad episodes; sanity-filter (episode length, gripper activity, reward) before training ingests them.

## Related
- [Fleet agentic control framework](fleet-agentic-framework.md) — the parent architecture (this page is its implementation appendix).
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — MCP + the tool-call pattern.
- [Rosetta](../../entities/rosetta.md) — the LeRobot↔ROS 2 bridge these tools + the recorder sit on.
- [LeRobot on ROSOrin Pro](lerobot-on-rosorin-pro.md) — the per-robot recipe (HX-12H contract, compute budget).

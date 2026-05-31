# XLeRobot → RealSense D435i bracket

A printable L-bracket that bolts to the **D435i's two front-face M3 holes
(45 mm pitch)** and presents a flat foot to the XLeRobot "last mounting link."
Built because the stock XLeRobot press-fit camera *shell* is keyed to the
slimmer D415 body (99 × 20 × 23 mm) and will not accept the D435i
(90 × 25 × 25 mm) — see
[`wiki/syntheses/projects/xlerobot-camera-options-low-light.md`](../../wiki/syntheses/projects/xlerobot-camera-options-low-light.md).

## Files
- `d435i_bracket.scad` — parametric source (edit this).
- `d435i_bracket.stl` — generated from the defaults below; print this to test-fit.
- `preview.png` — iso / front / side views.

## ⚠️ Two dimensions to confirm before the final print

| Parameter | Default | Status |
|---|---|---|
| `m3_pitch` = 45 mm (camera M3 horizontal spacing) | 45 | Community-sourced, widely consistent. |
| `cam_m3_z` = 17 mm (M3 hole **height** above camera bottom edge) | 17 | **NOT in the Intel datasheet — measure your unit with calipers.** |
| robot-side hole pattern (`robot_hole_*`) | 20 mm ± X, Y={16,32} | **Placeholder — set to your actual XLeRobot mounting-link bolt pattern.** |

The Intel D400 datasheet (337029-005) publishes the body size and the bottom
**1/4-20 tripod hole** (17.5 mm from the left imager), but **not** the front M3
holes' vertical position. The M3 holes sit close to the IR imagers
(50 mm baseline → imagers at ±25 mm; holes at ±22.5 mm), so the `strap` is kept
short (12 mm) to stay clear of the optical band. **Print the strap alone first
(or the whole part) and offer it up to the camera** — confirm the holes line up
and nothing occludes the two IR imagers, the IR projector, or the RGB lens
before committing to a final print. If your unit's M3 holes are in the *lower*
half of the front face, mirror the part in Z (or set `cam_m3_z` low and route
the foot under the camera instead of over it).

## Print settings (suggested)
- Material: PETG or PLA. Orientation: lay the **foot flat on the bed**, strap
  pointing up — the gussets then print without support and the layer lines run
  across the load.
- 3–4 perimeters, ≥30% infill. No support needed in that orientation.
- Hardware: 2× **M3** screws into the camera (the camera holes are tapped
  ~2.5 mm deep — don't over-torque); robot-side fasteners per your link.

## Regenerate
```
openscad -o d435i_bracket.stl d435i_bracket.scad      # from the parametric source
# or re-run the trimesh generator used here: /tmp/gen_bracket.py
```

Bracket bounding box (defaults): 64 × 42 × 16 mm; ~14.7 cm³ of plastic.

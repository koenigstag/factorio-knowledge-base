# Beacon effect stacking (diminishing returns, "Diminishing beacons", FFF #409)

How much a module's effect gets multiplied when broadcast by N beacons
affecting the same machine.

Formula: `formulas/beacon_effect.py:beacon_effect_multiplier` —
`distribution_effectivity × profile[n-1] × n`.

Inputs, both directly from `datapacks/dump/vanilla/beacon/beacon.json`:
- `distribution_effectivity = 1.5` — matches FFF #409's own number exactly ("I settled on 3x which results in transmission power of 1.5").
- `profile` — a 100-entry lookup table. Confirmed by direct computation: `profile[n-1]` equals `1/sqrt(n)` to rounding precision (max deviation ~0.0001 across all 100 entries) — the sqrt(n) diminishing-returns formula FFF describes in prose is *exactly* what this table encodes, not an approximation of it.

## total_multiplier_by_beacon_count

| n beacons | multiplier | 1.5×√n (for comparison) |
|---|---|---|
| 1 | 1.5 | 1.5 |
| 8 | 4.242 | 4.243 |
| 12 | 5.195 | 5.196 |
| 16 | 6.0 | 6.0 |
| 20 | 6.708 | 6.708 |

All 5 values verified by running the formula against the actual
`profile` table, not the sqrt approximation directly.

## Context (FFF #409, not independently re-verified against data.raw)

The old (pre-2.0) system had a flat `distribution_effectivity=0.5` per
beacon with no diminishing returns — linear, unbounded scaling with
beacon count. FFF #409 also gives per-building-size beacon caps:
2×2–4×4 buildings fit up to 12 beacons, 5×5–7×7 up to 16, 8×8–10×10 up
to 20 — cited here as context for why 8/12/16/20 were chosen as the
worked examples above, but these specific caps weren't found as a
`data.raw` field during this session, so they're not held to the same
confidence as the multiplier table itself.

## Which modules can actually go in a beacon

`beacon.allowed_effects = ["consumption", "speed", "pollution"]` —
**no `productivity` and no `quality`**. Productivity and quality
modules cannot be placed in a beacon at all (only directly in a
crafting machine) — checked directly against the datapack, not cited
from prose.

Verified: 2026-08-06

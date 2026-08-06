# Train max speed by fuel

Formula: `formulas/train_max_speed.py:train_max_speed` — direct wiki
quote confirming the formula shape: *"The calculated train_speed is
also capped to max_speed = 1.2 * fuel_top_speed_multiplier."*

Inputs:
- `locomotive_max_speed=1.2` — `datapacks/dump/vanilla/locomotive/locomotive.json`'s
  `max_speed` (not yet extracted as a file at time of writing this
  relation, checked directly against `data.raw`; this is a `data.raw`
  field, not a hardcoded engine constant — the "1.2" the wiki quotes
  is specifically the vanilla locomotive's own value, a different
  locomotive prototype would have a different base).
- `fuel_top_speed_multiplier` — `datapacks/dump/vanilla/item/*.json`.
  Confirmed directly: `coal`/`wood` have no such field (default 1.0),
  `solid-fuel`=1.05, `rocket-fuel`=1.15, `nuclear-fuel`=1.15.

## max_speed_tiles_per_tick

| fuel | multiplier | max_speed (tiles/tick) |
|---|---|---|
| coal | 1.0 (default) | 1.2 |
| wood | 1.0 (default) | 1.2 |
| solid-fuel | 1.05 | 1.26 |
| rocket-fuel | 1.15 | 1.38 |
| nuclear-fuel | 1.15 | 1.38 |

Kept in tiles/tick (this project's usual native unit) rather than
converting to km/h — the wiki displays these in km/h (e.g. "259 km/h"
for coal) but a reliable tiles-to-km conversion factor wasn't
confirmed here, so no conversion is claimed; multiply by 60 for
tiles/sec if needed, consistent with every other tick-based field in
this project.

All 5 values verified by running the formula, not by hand.

Verified: 2026-08-06

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

## km/h conversion (resolved 2026-08-08): 1 tile = 1 meter

Previously left unconverted — "a reliable tiles-to-km conversion
factor wasn't confirmed here." Resolved by cross-multiplying against
`factoriocheatsheet.com`'s cited km/h figures (`vehicle-fuel-bonus.data.ts`):
`tiles/tick × 60 (tick→sec) × 3.6 (m/s→km/h) = km/h` reproduces every
one of its 5 values exactly (coal `1.2 × 216 = 259.2`, solid-fuel
`1.26 × 216 = 272.16`, rocket/nuclear-fuel `1.38 × 216 = 298.08`) —
which only works if 1 tile = 1 meter, confirming that community
convention rather than assuming it.

| fuel | max_speed (tiles/tick) | max_speed (km/h) |
|---|---|---|
| coal | 1.2 | 259.2 |
| wood | 1.2 | 259.2 |
| solid-fuel | 1.26 | 272.16 |
| rocket-fuel | 1.38 | 298.08 |
| nuclear-fuel | 1.38 | 298.08 |

## Not covered: speed degradation with wagon count

The same cheat-sheet source also tabulates top speed *dropping* as
wagons are added (e.g. coal/wood: 259.2 km/h unloaded down to 170 km/h
at 7 wagons, 50 km/h at 15), with higher-force fuels (rocket-fuel)
holding top speed unchanged much longer as wagons are added. This is
real train physics (weight/friction/braking-force interaction) this
project doesn't model at all yet — `mechanics/trains.md` only covers
`max_inserters_per_wagon` and confirms cargo-wagons have no cargo
*weight* limit, not the wagons' own mass affecting train acceleration/
top speed. Flagged as an identified, deferred gap (like
`layouts/`-scale planet/surface mechanics), not derived here — would
need `locomotive`/`cargo-wagon` `weight`, `friction_force`, and
`air_resistance_multiplier` fields, none pulled yet.

All 5 values verified by running the formula, not by hand.

Verified: 2026-08-06 (base), 2026-08-08 (km/h conversion)

# Units reference for datapacks/dump/vanilla/

Bare numeric fields in this dump carry no unit of their own — this file
is the shared lookup so no one has to guess (or worse, assume the wrong
one 60x off). Applies to this `vanilla` mod-set at the game version
recorded in `source.json`.

## Base rate: 60 ticks per second

Factorio's simulation runs at a fixed 60 UPS (updates per second). Any
`.../tick` value below is turned into `.../second` by multiplying by 60.

## Per-tick rate fields (× 60 → per-second)

| Field | Prototype types | Unit | Verification |
|---|---|---|---|
| `speed` | `transport-belt`, `underground-belt`, `splitter` | tiles/tick | **Confirmed**: `transport-belt.speed = 0.03125` × 60 = 1.875 tiles/s, matches the independently wiki-sourced figure exactly (see `constraints/`-adjacent research in project history). |

## "Base time at speed=1" ÷ speed = actual seconds

These come in pairs: a base-cost field on the *product/resource* side
(calibrated in seconds assuming a reference speed of 1), divided by a
speed multiplier on the *machine* side.

| Base field | Speed field | Formula | Verification |
|---|---|---|---|
| `recipe.energy_required` | `furnace.crafting_speed` / `assembling-machine.crafting_speed` | `energy_required / crafting_speed` = seconds per craft | **Confirmed**: iron-plate `energy_required=3.2` ÷ steel-furnace `crafting_speed=2` = 1.6s, matches the wiki's "~1.6s/plate" for steel furnace. |
| `resource.minable.mining_time` | `mining-drill.mining_speed` | `mining_time / mining_speed` = seconds per mining cycle | **Inferred, not independently re-verified**: same field-naming/schema convention as recipes (`iron-ore.mining_time=1` ÷ `electric-mining-drill.mining_speed=0.5` = 2s/ore = 0.5 ore/s, plausible against commonly-cited electric-drill baseline) — but this pair hasn't had its own dedicated wiki cross-check the way belt speed and furnace crafting time did. Re-verify before relying on it for a `formulas/` derivation. |

Note: despite the field name, `energy_required` is not an energy unit in
the everyday sense — numerically it behaves as seconds-at-reference-speed.
`crafting_speed` and `mining_speed` are dimensionless multipliers against
that reference, not standalone rates.

## Already per-minute — do NOT multiply by 60

| Field | Prototype types | Unit | Verification |
|---|---|---|---|
| `energy_source.emissions_per_minute.pollution` | `furnace`, `mining-drill`, `assembling-machine`, ... (any `energy_source`) | pollution units per minute, at full power | **Confirmed via wiki.factorio.com/Pollution + dev history**: this field literally means what its name says — no tick conversion. It replaced an older `emissions_per_second_per_watt` field specifically because that one was "fundamentally flawed"; `emissions_per_minute` was added as the direct, self-sufficient replacement. "Pollution" itself has no official named unit and no tie to a real physical quantity — the wiki describes it only as an abstract "cloud". Opposite direction from `speed`: don't ×60 this one. |

## Not a flat unit conversion — needs a formula (`formulas/`, not a datapack fact)

| Field | Prototype type | Why it's not a simple conversion |
|---|---|---|
| `rotation_speed`, `extension_speed` | `inserter` | Per-tick fractional progress, but the total angle/distance to cover depends on that inserter's own `pickup_position`/`insert_position`/`starting_distance` geometry — there's no single fixed "base time" to divide, unlike recipes or mining. Computing actual cycle time needs a geometry-aware formula. |

## Self-documented (unit embedded in the string, no ambiguity)

`energy_usage`, `energy_per_movement`, `energy_per_rotation`, `drain` —
e.g. `"90kW"`, `"5kJ"`. Parse the suffix, no external lookup needed.

## Plain counts / already unambiguous

`stack_size`, `module_slots`, `filter_count`, `inventory_size` (item
count), `max_distance` (tiles), `tier` (ordinal) — no time component,
nothing to convert.

## Not yet checked

`item.weight` — commonly assumed to be grams, but that assumption
hasn't been verified against a primary source in this project; treat
as unconfirmed until it is.

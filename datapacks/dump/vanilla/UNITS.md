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
| `resource.minable.mining_time` | `mining-drill.mining_speed` | `mining_time / mining_speed` = seconds per mining cycle | **Confirmed** via wiki.factorio.com/mining, quoted formula: *"Mining time / Mining speed = Seconds for one resource item"*. `iron-ore.mining_time=1` ÷ `electric-mining-drill.mining_speed=0.5` = 2s/ore = 0.5 ore/s. |
| `technology.unit.time` | `lab.researching_speed` (not `crafting_speed` — labs use their own field name) | `unit.time / researching_speed` = seconds per research unit at base speed, × `unit.count` for total | **Confirmed** via wiki.factorio.com/lab, quoted formula: adjusted cycle time = *"T[r]"* (research cycle time) *"/ ERS"* (effective research speed, `researching_speed` before module/tech bonuses). `lab.researching_speed=1`, `biolab.researching_speed=2` — cross-checks the wiki's own claim that biolab researches twice as fast as a regular lab. Now extracted as `datapacks/dump/vanilla/lab/`. |

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

`energy_usage`, `energy_per_movement`, `energy_per_rotation`, `drain`,
`fluid.heat_capacity`, `item.fuel_value` — e.g. `"90kW"`, `"5kJ"`,
`"100MJ"`. Parse the suffix, no external lookup needed.
`heat_capacity` **confirmed** via the official `FluidPrototype` docs
(lua-api.factorio.com/latest/prototypes/FluidPrototype.html), quoted
verbatim: *"Joule needed to heat 1 Unit by 1 °C"* — energy per degree
per fluid unit, default `"1kJ"` if unspecified. (The docs' own example
value, `"0.2kJ"`, is just generic syntax illustration, not tied to any
real fluid — our `water.heat_capacity=2kJ`/`steam.heat_capacity=0.2kJ`
are the actual in-game values, unrelated to that example.)

## Temperature — degrees Celsius

`fluid.default_temperature`, `max_temperature`, `gas_temperature`.
**Confirmed by internal consistency**: `water.default_temperature=15`,
`max_temperature=100` — matches water's real-world boiling point at
100, the value the game is clearly keyed to. `steam.max_temperature=5000`
is a gameplay figure (turbine mechanics), not physically real, but
still on the same °C scale.

## Spatial fields — tiles

`collision_box`, `selection_box` (pairs of [x,y] corners relative to
entity center), `resource_searching_radius`. This is Factorio's
universal spatial unit for all entity geometry — same unit as
`constraints/rails.json`'s tile-based facts. Cross-checked:
`cargo-wagon.collision_box = [[-0.6,-2.4],[0.6,2.4]]` → 1.2×4.8 tiles,
matches the commonly-cited cargo wagon footprint.

Note `selection_box` is a UI click-target box, not a reliable footprint
— e.g. `stone-furnace.selection_box` is `[[-0.8,-1],[0.8,1]]` (1.6×2.0,
not square) even though the building occupies a square 2×2 grid. Use
`collision_box` for footprint, not `selection_box`.

**`tile_box`** — `[width, height]` in whole tiles, added alongside
`collision_box` on grid-placed buildings (`furnace`,
`assembling-machine`, `mining-drill`, belt family, `inserter`).
Computed as `ceil(collision_box width)` × `ceil(collision_box height)`
— cross-checked against 8 independently-known footprints (stone-furnace
2×2, electric-furnace/assembling-machine-*/pumpjack 3×3,
electric-mining-drill 3×3, foundry 5×5, transport-belt/inserter 1×1),
all matched exactly.

**Exception: `cargo-wagon.tile_box = [2, 6]`, `fluid-wagon.tile_box =
[2, 6]`** — neither is `ceil(collision_box)` (that would wrongly give
`[2, 5]` from their identical 1.2×4.8 collision box — both wagon types
share the same `collision_box`). Rail vehicles don't follow the
building grid-snap rule the other entities use. `[2, 6]` instead comes
from the wiki's own `Dimensions: 2×6` infobox value on each entity's
page — see the derivation note in `constraints/trains.md` (it lines up
with the 12-inserters-per-wagon cap: 6 tiles × 2 sides, though the
wiki doesn't confirm that's the actual cause — and that reasoning is
cargo-wagon-specific anyway, since fluid wagons load via pipes, not
inserters). `locomotive.tile_box` doesn't need this exception: its
collision box is 1.2×5.2, and `ceil(5.2)=6` already lands on the
correct value without an override. Every other `tile_box` in this dump
is dump-derived; these two fields are the only ones sourced from the
wiki instead — flagged here since `cargo-wagon.json`/`fluid-wagon.json`'s
own provenance is otherwise entirely the dump manifest, not a wiki
citation.

## item.weight — grams

**Confirmed**: `iron-ore`/`copper-ore`/`coal`/`stone`/`wood` all have
`weight=2000`, matching Friday Facts #382's "base ore weight is set to
2kg per item" exactly (2000 g = 2 kg). Important gap: `weight` is only
set explicitly on some items (raw materials, fuel, space-relevant
items) — it's `None`/absent on manufactured items like
`iron-plate`/`copper-plate`. Per FFF #382, absence doesn't mean zero
weight — the game derives a weight for those automatically from their
recipe chain, which this static dump does not capture. `utility-constants/default.json`'s
`default_item_weight=100` is a separate, flat fallback value — not
confirmed to be the same thing as that recipe-chain derivation, don't
conflate the two without checking further.

Same scale: `utility-constants/default.json`'s `rocket_lift_weight=1000000`
= 1000 kg, confirming FFF #382's "rocket cargo capacity 1000 kg"
figure directly against `data.raw` rather than the FFF post alone.

## fluid_box.volume — Factorio's own "fluid units"

**Confirmed** (wiki.factorio.com/Fluid_system + forums): not liters,
not any real-world volume unit — the game's own internal scale. A pipe
segment holds 100 units, a storage tank holds 25,000. Connected
pipes/tanks equalize by *percentage* of their own capacity, not
absolute amount. `mining-drill.input_fluid_box.volume=200` and
`pumpjack.output_fluid_box.volume=1000` are on this same scale.
`fluid-wagon/fluid-wagon.json`'s `capacity=50000` (2× a storage tank)
is too — wiki-confirmed at normal quality (higher quality tiers hold
more; not covered here since `quality` isn't extracted as a datapack
yet).

## utility-constants.max_fluid_flow / pump.pumping_speed — per tick (× 60 → per second)

Same fluid-unit scale as `fluid_box.volume`, same tick convention as
`speed`. **Confirmed**: `utility-constants/default.json`'s
`max_fluid_flow=100` × 60 = 6000/s, matching the wiki's *"theoretical
maximum throughput limit of 6000 fluid per second (100 fluid per
tick)"* exactly — this is the per-*connection* cap (each unique
input/output connection point, not per pipe or per distance; Factorio
2.0's "Fluids 2.0" rework removed the old distance-dependent pipe
throughput entirely, see FFF #416). `pump/pump.json`'s
`pumping_speed=20` × 60 = 1200/s, also wiki-confirmed.

(The softer "~4200/s practical" figure the wiki also mentions isn't a
`data.raw` value at all — not a unit-conversion question for this
file, see `constraints/fluids.md` instead.)

## pipe_connections.direction — 16-direction enum, cardinals spaced 4 apart

**Confirmed**: Factorio 2.0 expanded from the old 8-direction system to
a 16-direction enum (to support diagonal/elevated rail, see FFF #377),
where `0`=north, `4`=east, `8`=south, `12`=west (each step = 22.5°; odd
values are the diagonals in between). All `pipe_connections.direction`
values actually present in `datapacks/dump/vanilla/mining-drill/` are
pure cardinals (0/4/8/12) — no diagonal fluid connections in this set.

## Dimensionless multipliers / fractions — not a unit at all

`module.effect.*` (e.g. `productivity: 0.04` = +4% to the base stat),
`item.fuel_acceleration_multiplier`/`fuel_top_speed_multiplier` (e.g.
`1.8` = 80% bonus), `lab.science_pack_drain_rate_percent` (`biolab=50`
means it consumes science packs at half the normal rate per research
cycle — confirmed via wiki.factorio.com/lab: "consumes packs half as
fast", matching the field exactly). These scale a base value
multiplicatively; there's nothing to convert, just don't mistake them
for absolute quantities.

## Plain counts / already unambiguous

`stack_size`, `module_slots`, `filter_count`, `inventory_size` (item
count), `max_distance` (tiles), `tier` (ordinal) — no time component,
nothing to convert.

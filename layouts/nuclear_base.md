# Nuclear base: uranium mining, refining, enrichment, reactor grid

A [nuclear base](../glossary/invented/nuclear-base.md) —
[outpost](../glossary/canonical/outpost.md) dedicated to uranium
mining and nuclear power, separate from `layouts/scalable_main_base.md`
for the same class of reason `layouts/scalable_chem_base.md` is: a real
external input requirement (`sulfuric-acid`, below) and a large,
independently-scalable footprint (reactor grid + heat-pipe network).
Same module/port philosophy as the other layouts in this project.

## The analogy, and where it breaks

Requested as: *ore drills = uranium drills + sulfuric acid, furnaces =
refining, then reactor/enrichment/sub-products.* Mostly holds, with one
real difference worth stating up front: **uranium mining itself needs a
fluid**, which ordinary ore mining never does. Checked directly against
`data.raw`:

- `resource/uranium-ore.json`: `mining_time=2`, **`required_fluid:
  "sulfuric-acid"`, `fluid_amount: 10`** per mining cycle — this is the
  actual sourced fact behind "uranium drills need sulfuric acid," not
  an assumption.
- `mining-drill/electric-mining-drill.json` and `.../big-mining-drill.json`
  both carry an `input_fluid_box` specifically for this — an ordinary
  iron/copper drill has no fluid input at all, so the "furnace needs a
  fluid" framing has no equivalent on the plate-mining side of this
  project's other layouts.

## Uranium mining

Rate (`mining_speed / mining_time`, same formula shape as
`relations/mining_belt_ratios.md`, just with a fluid side-input added):

| drill | uranium-ore/sec | sulfuric-acid/sec |
|---|---|---|
| electric-mining-drill (`mining_speed=0.5`) | 0.25 | 2.5 |
| big-mining-drill (`mining_speed=2.5`) | 1.25 | 12.5 |

Both ratios are fixed at **10 sulfuric-acid per uranium-ore**,
independent of drill tier (the fluid-per-cycle and ore-per-cycle scale
together).

## Refining: uranium-processing (centrifuge)

`recipe/uranium-processing.json`: 10 uranium-ore → 1 uranium-235
(`probability=0.007`) + 1 uranium-238 (`probability=0.993`),
`energy_required=12`, category `centrifuging` (`centrifuge`,
`crafting_speed=1`). Per machine: `10/12` = 0.833 ore/sec consumed,
expected `0.000583` uranium-235/sec, `0.0828` uranium-238/sec — the
overwhelming byproduct skew (99.3% U-238) is exactly why enrichment
exists: raw processing alone is a poor source of U-235.

## Enrichment: Kovarex (centrifuge)

`relations/uranium_enrichment.md` (already derived): `kovarex-enrichment-process`
(`energy_required=60`) nets **+1 uranium-235, −3 uranium-238** per
cycle — per machine, `+1/60` = 0.0167 U-235/sec, `−3/60` = 0.05
U-238/sec. This is the deterministic alternative to relying on raw
processing's 0.007 probability (`expected_crafts_per_unit(0.007) ≈
142.86` crafts needed per U-235 without it).

## Fuel cells

`recipe/uranium-fuel-cell.json`: 10 iron-plate + 1 uranium-235 + 19
uranium-238 → 10 uranium-fuel-cell, `energy_required=10`
(`assembling-machine`-capable at AM1, same tier as
`layouts/scalable_main_base.md`). Per machine (AM1,
`crafting_speed=0.5`): 0.5 fuel-cell/sec, consuming 0.05 U-235/sec +
0.95 U-238/sec + 0.5 iron-plate/sec.

## Reactor

`reactor/nuclear-reactor.json`: `consumption=40MW`,
`neighbour_bonus=1`. `item/uranium-fuel-cell.json`: `fuel_value=8GJ`.
**Burn time = `8,000,000 kJ / 40,000 kW` = 200 sec/cell/reactor**
(0.005 fuel-cell/sec/reactor) — fixed per reactor regardless of
neighbor bonus, since `neighbour_bonus` scales heat *output* (MW), not
each reactor's own fuel draw (`relations/reactor_neighbor_output.md`'s
formula only touches output) — this is the whole reason multi-reactor
grids are fuel-*efficient*: more heat per fuel cell burned, not more
fuel needed. Heat-exchanger/turbine sizing per reactor (4
heat-exchangers, ~6.87 turbines) is already derived in
`relations/nuclear_power_chain.md` — not repeated here.

## Reference cell: 2×2 grid (4 reactors, 480 MW)

Matching `relations/reactor_neighbor_output.md`'s own grid table.
Fuel-cell demand: `4 × 0.005` = **0.02/sec**. Solving the two-isotope
mass balance (uranium-processing supplies both isotopes at their
natural ratio; Kovarex only moves U-238 into U-235, net) for the
machine counts that supply exactly this demand:

| stage | machines needed |
|---|---|
| uranium-processing (centrifuge) | 0.52 |
| kovarex-enrichment (centrifuge) | 0.10 |
| uranium-fuel-cell (AM1) | 0.04 |

All comfortably under 1 machine — **nuclear fuel demand is tiny
relative to a single centrifuge's output**, even for a real
480MW reactor grid; this matches widely-repeated community experience
that fuel production is a minor, easily-overbuilt side process, now
shown as an actual derived number rather than folklore. Scales
linearly with reactor count for larger grids (e.g. the 2×6/12-reactor,
1760MW grid in `relations/reactor_neighbor_output.md` needs exactly 3×
these figures).

**Upstream of that**: ore demand = `0.52 × 0.833` ≈ **0.434
uranium-ore/sec**, needing **2 electric-mining-drill** (`0.434/0.25` =
1.74, rounds up) and, at the fixed 10:1 ratio above, **≈4.34
sulfuric-acid/sec**.

## Sulfuric acid from the chem base

This is the concrete answer to "how much, and how does it get here":
**≈4.34 sulfuric-acid/sec** for a modest 480MW reactor grid — a third
consumer for `layouts/scalable_chem_base.md`'s sulfuric-acid module,
alongside `battery` and the small `processing-unit` trickle already
documented there, of comparable magnitude to that trickle (not
negligible against the module's `battery`-dominated bulk output
either). Reconciled into that file as of this revision — see its
"Sulfuric acid" and "Rail stations" sections. Delivered by a
**dedicated fluid-wagon line straight from the chem-base's rail
infrastructure to this site** — its own line, not routed through the
main base or sharing the `processing-unit` trickle's station, same
point-to-point [train-base](../glossary/canonical/train-base.md)
pattern as every other rail connection in this project. Re-deriving
sulfuric-acid production locally instead (its own sulfur/water/
petroleum-gas chain) would mean duplicating a whole chem-base module
for a site that doesn't otherwise need any other chemistry product.

## Sub-products

Two recipes give U-238 (the abundant, otherwise-excess byproduct) and
enriched U-235 somewhere useful beyond fuel cells:

- **`uranium-rounds-magazine`** (`recipe/uranium-rounds-magazine.json`):
  1 piercing-rounds-magazine + 1 uranium-238 → 1 uranium-rounds-magazine.
  A direct sink for the U-238 surplus raw processing produces regardless
  of how much Kovarex enrichment is running.
- **`atomic-bomb`** ("uranium rocket head" in the request that framed
  this file — actually a player-carried weapon, not a rocket-silo
  launch): `recipe/atomic-bomb.json` — 10 processing-unit + 10
  explosives + 100 uranium-235 → 1 atomic-bomb. Needs both other
  outposts: `processing-unit` from the main base
  (`layouts/main_bus.md`'s corrected conclusion — assembled there, not
  the chem base) and `explosives` from the chem base
  (`layouts/scalable_chem_base.md`, itself framed as a low-volume
  logistics-network sub-product, not a bus export). 100 uranium-235 per
  bomb is a large ask relative to this file's reference cell's own net
  enrichment rate (0.002 U-235/sec, sized exactly to the 480MW grid's
  fuel-cell demand above) — at that rate, one bomb's 100 uranium-235
  would take `100/0.002` = 50,000 sec (≈13.9 hours) to accumulate;
  sized here for the recipe relationship, not a production target —
  a dedicated bomb build would need its own, much larger enrichment
  capacity, not a diversion from the reactor's own fuel supply.

Neither is exported anywhere by default in this design — both are
low-volume, logistics-network items the same way
`layouts/scalable_chem_base.md`'s `explosives` module is, not bus/rail
freight.

## What's still open

- Heat-pipe routing from the reactor grid to the heat-exchanger block
  — `relations/nuclear_power_chain.md`'s `min_heat_pipe_paths_by_reactor_grid`
  table already covers the pipe-count side; this file doesn't add a
  physical layout for it.
- Whether the nuclear base needs its own local mall/construction
  supply or imports everything (mirrors the same open question in
  `layouts/scalable_chem_base.md`).
- Exact train/wagon sizing for the sulfuric-acid fluid-wagon run —
  same "derive the ratio, don't fix a target" stance as every other
  layout in this project; the 4.34/sec figure is a reference-cell
  illustration, not a fixed requirement.
- Whether uranium mining should use `big-mining-drill` instead of
  `electric-mining-drill` at scale (5× the rate, 5× the sulfuric-acid
  draw per drill) — not decided here.

Verified: 2026-08-09

# Steel smelting module (belt-saturated, sized via smelting_ratios)

A derived layout, not an imported blueprint — sized entirely from
`relations/smelting_ratios.md`'s `steel-plate` row
(`energy_required=16`) plus `formulas/recipe_ingredient_ratio.py`, in
the spirit of
[blueprints/curated/earlygame/24x2-stone-furnaces-module.md](../blueprints/curated/earlygame/24x2-stone-furnaces-module.md)
(same "N furnaces per row" framing) but for `steel-plate` instead of
`iron-plate`/`copper-plate`. No real blueprint string backs this yet —
it belongs here, not in `blueprints/curated/`, until someone actually
builds and exports it (see `blueprints/README.md`'s curated-entries
convention).

## Why steel-plate doesn't scale like the 24×2 module

`steel-plate`'s recipe consumes **iron-plate**, not ore
(`datapacks/dump/vanilla/recipe/steel-plate.json`:
`ingredients: [{"iron-plate", amount: 5}]`, `results: [{"steel-plate",
amount: 1}]`, `energy_required: 16`). That 5:1 ingredient ratio
(`recipe_ingredient_ratio.ingredient_ratio(5, 1) = 5`) means the input
side needs **5x** the belt throughput of the output side — unlike
`iron-plate`/`copper-plate` (ore:plate is 1:1), the 24×2 module's
"one input side, one output side" single-flow shape doesn't carry over
as a single-lane-in/single-lane-out design here.

## Derivation

Using `formulas/production_rate.py` (`production_rate`,
`machines_to_saturate`) and `recipe_ingredient_ratio.py`, belt
throughput 15 items/sec (`transport-belt`, per
`mechanics/belt-item-density.md`'s conversion):

| furnace | crafting_speed | furnaces to saturate 1 **output** belt (steel-plate) | furnaces to saturate 1 **input** belt (iron-plate) | input belts needed per output belt |
|---|---|---|---|---|
| stone-furnace | 1 | 240 | 48 | 5 |
| steel-furnace | 2 | 120 | 24 | 5 |

(`electric-furnace` shares `steel-furnace`'s `crafting_speed=2`, so its
row is identical to `steel-furnace`'s — omitted as redundant, same as
`relations/smelting_ratios.md`'s own table.) The "input belts needed"
column is tier-independent (always 5) because it's driven purely by
the recipe's ingredient ratio, not by furnace speed — a faster furnace
needs proportionally more iron-plate per second, but also produces
proportionally more steel-plate per second, so the 5:1 ratio between
them cancels the tier out.

## Design: 5 rows, each row a self-contained input-belt-saturated unit

Pick a furnace tier — **steel-furnace** below (the practical choice
once steel-plate production is running at any real scale; a
stone-furnace variant is the same shape at 2x the furnace count, see
the alternative below) — then build **5 identical rows of 24
steel-furnaces**, not one combined block:

- Each row has its **own dedicated iron-plate import belt**, fully
  saturated by that row alone (24 steel-furnaces exactly consumes one
  `transport-belt` of iron-plate — see table above) — this is a
  deliberate echo of the 24×2 module's own "24" count, just applied to
  the input side instead of the output side.
- Coal (fuel) is **not** a per-row concern here, unlike the iron-plate
  lane. Per
  [relations/furnace_fuel_consumption.md](../relations/furnace_fuel_consumption.md),
  a `steel-furnace` burns only 0.0225 coal/sec at 100% uptime; all 120
  furnaces across all 5 rows together need just 2.7 coal/sec — **under
  a fifth of one `transport-belt`'s throughput**. A single shared coal
  lane (e.g. routed once across all 5 rows, or split off a main-bus
  coal lane) comfortably fuels the entire module; there's no need to
  size or duplicate it per row the way the iron-plate lane needs to
  be.
- Each row's 24 furnaces produce exactly 3 steel-plate/sec
  (`24 x 0.125`), i.e. 1/5 of a saturated output belt.
- All 5 rows' output merges onto **one shared central steel-plate
  belt**, reaching full saturation (15 items/sec = 5 x 3) only once
  all 5 rows are built.

This is the same general "raw material outside, product inside" shape
as [smelter_module_ports.md](smelter_module_ports.md)'s "Plate on the
inside" pattern, generalized from 2 rows to 5 — but the 2-row version's
free self-balancing trick (via
[mechanics/inserter-belt-lane-placement.md](../mechanics/inserter-belt-lane-placement.md)'s
far-lane placement rule) only works for exactly 2 symmetric sources
sharing one belt's two lanes. With 5 rows feeding one belt, that's a
genuine multi-belt merge, not a 2-lane trick — and 5 isn't a power of
two, so `relations/balancer_splitter_count.md`'s formula (which only
covers n = power of two) doesn't directly size it. Simplest correct
option: a plain sequential splitter cascade (row 1 + row 2 -> merge,
+ row 3 -> merge, ...) — not formally "throughput-unlimited" per
`glossary/canonical/belt-balancer.md`'s definitions, but sufficient
here since all 5 rows produce identically and simultaneously, so
backpressure imbalance isn't a real risk. A full power-of-two balancer
would need scaling to 8 rows (192 furnaces, well past what the ratio
actually calls for) purely to fit the formula — not worth it just to
combine 5 already-equal sources.

## Stone-furnace alternative (matching the 24×2 module's own tier)

Same shape, doubled: **5 rows of 48 stone-furnaces** (240 total), each
row saturating its own iron-plate belt exactly the same way (48
stone-furnaces per input belt, per the table). Bootstrap cost is real
— unlike `iron-plate`, this module's *input* is already a processed
good, so a stone-furnace version of it can't be the very first thing
built; it needs an upstream iron-plate-producing module (e.g.
[blueprints/curated/earlygame/4x2-stone-furnaces-w-upgrade-spacing.md](../blueprints/curated/earlygame/4x2-stone-furnaces-w-upgrade-spacing.md))
already running at 5-belt scale to feed it. Coal is still trivial at
this size: 240 stone-furnaces need 5.4 coal/sec, still just over a
third of one `transport-belt` — see
[relations/furnace_fuel_consumption.md](../relations/furnace_fuel_consumption.md).

## Simpler framing: 1 iron-furnace per 1 steel-furnace, same tier

A community thread raised the natural first guess — "steel needs 5
iron-plate per craft, so I need a 5:1 ratio of iron-smelting to
steel-smelting furnaces" — and corrected it: that's wrong, because
`steel-plate` also takes 5x longer to craft (`energy_required=16` vs
`iron-plate`'s `3.2` — exactly 5x), which exactly cancels the 5:1
ingredient ratio. The corrected rule: **build exactly 1 iron-smelting
furnace per 1 steel-smelting furnace, as long as both stages use the
same furnace tier** — no belt-throughput math required at all if the
goal is just "keep the steel furnaces fed," rather than "saturate a
specific belt tier."

Verified directly against this project's own formulas, tier by tier
(`production_rate(speed, 3.2)` vs `production_rate(speed, 16) x
ingredient_ratio(5, 1)`):

| furnace tier | iron-plate/sec per iron-furnace | iron-plate/sec consumed per same-tier steel-furnace |
|---|---|---|
| stone-furnace | 0.3125 | 0.3125 |
| steel-furnace | 0.625 | 0.625 |
| electric-furnace | 0.625 | 0.625 |

Exactly equal in every row — confirming the 1:1 rule holds regardless
of tier, since it falls out of `steel-plate.energy_required` being
exactly 5x `iron-plate.energy_required` (a property of this specific
recipe pair, not a general law).

This is consistent with, not a contradiction of, the belt-saturation
design above: the stone-furnace alternative's upstream module (5
belts of iron-plate via stone-furnace = 5 x 48 = 240 furnaces) matches
this module's own 240 stone-furnaces exactly 1:1, because both stages
use the same tier there. The steel-furnace-tier primary design above
only comes out to a *different* ratio (2 stone-furnace : 1
steel-furnace) because it deliberately mixes tiers — a stone-furnace
upstream module feeding a steel-furnace downstream module. Building
the upstream module in steel-furnace too would restore the 1:1 ratio
(120 iron-smelting steel-furnaces : 120 steel-plate-smelting
steel-furnaces) at half the footprint of the stone-furnace upstream
option.

Source: https://steamcommunity.com/app/427520/discussions/0/3112519113936187296/
(community Q&A thread; the 5:1-ingredient-ratio misconception and its
correction, re-verified here against this project's own recipe data
rather than taken on the thread's word).
Verified: 2026-08-22

## Open items

- Not yet built/exported as an actual blueprint; numbers here are
  derived, not blueprint-verified. If someone builds this in-game, it
  belongs in `blueprints/curated/{earlygame,midgame}/` per that
  folder's convention (raw string + decode + provenance), cross-linked
  back to this file the way
  [24x2-stone-furnaces-module.md](../blueprints/curated/earlygame/24x2-stone-furnaces-module.md)
  now cross-links to `relations/smelting_ratios.md`.

Verified: 2026-08-22 (derivation re-run directly against
`formulas/production_rate.py` and `recipe_ingredient_ratio.py`, not
hand arithmetic).

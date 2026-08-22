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
  belt.
- Each row also needs its own coal (fuel) lane — `steel-furnace` is a
  burner machine (`datapacks/dump/vanilla/furnace/steel-furnace.json`:
  `energy_source.type: "burner"`). **Left open, not guessed**: this
  project doesn't yet hold a sourced coal-consumption-rate formula for
  burner furnaces, so the coal lane's exact throughput requirement
  isn't stated here — needs `mechanics/`-level sourcing before it can
  be sized the same rigorous way as the plate/ore lanes.
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
already running at 5-belt scale to feed it.

## Open items

- Coal lane sizing (see above) — needs a sourced fuel-consumption
  formula before it can join this derivation.
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

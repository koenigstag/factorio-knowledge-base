# Example: sizing bus lanes for a specific target (not a fixed template)

**Question**: there's no single "ideal" main bus — `layouts/main_bus.md`'s
practical template is a community starting point, not a derived
answer, because the right lane count depends on what the base actually
needs to produce. This walks through the *method* that gives an exact
answer once a target is chosen, using primitives this project already
holds instead of guessing or re-citing someone else's total.

**Concrete target for this walkthrough**: a base wants its bus to
simultaneously supply enough iron/copper/plastic to sustain **2 full
express-belt lanes of steel-plate** and **1 full express-belt lane of
advanced-circuit**, with both bussed at the same tier.

## Step 1 — get the ratios (already cached)

`relations/bus_lane_ratios.md`, derived via
`formulas/recipe_ingredient_ratio.py`:
- `steel-plate`: 5.0 iron-plate
- `advanced-circuit`: 2.0 iron-plate, 5.0 copper-plate, 2.0 plastic-bar

These ratios are belt-tier-independent (see that file for why) — they
apply the same whether the target lanes are transport-belt or turbo.

## Step 2 — combine demands linearly

Ratios are per-lane consumption rates, so simultaneous demands just
sum (this is superposition, not a new formula — consumption rates
add):

- iron-plate lanes needed = `2 × 5.0` (for steel) `+ 1 × 2.0` (for
  advanced-circuit) = **12 lanes**
- copper-plate lanes needed = `1 × 5.0` (advanced-circuit only) =
  **5 lanes**
- plastic-bar lanes needed = `1 × 2.0` (advanced-circuit only) =
  **2 lanes**

## Step 3 — if tiers differ, convert to items/sec first, not lanes directly

The lane-sum in step 2 only works because every lane in this example
is the same belt tier (express, 45 items/sec — see
`datapacks/dump/vanilla/UNITS.md`'s belt `speed` conversion). If the 2
steel lanes ran on turbo belts (60 items/sec) while the advanced-circuit
lane stayed express (45 items/sec), lane counts aren't directly
additive across tiers — convert each to items/sec first
(`lanes × belt_throughput`), sum in items/sec, then divide by
whichever tier the *ingredient* lanes will actually use:

```
iron_items_per_sec = 2×60 (steel, turbo) × 5.0 + 1×45 (circuit, express) × 2.0
                    = 600 + 90 = 690 items/sec
iron_lanes_if_bussed_on_express = 690 / 45 ≈ 15.3 -> 16 lanes (round up)
```

Not computed further here since this walkthrough's actual target
(Step 2) is single-tier; this step exists to flag the tier-mixing trap
before it produces a silently wrong lane count.

## Result

For the stated target (2 express steel-plate lanes + 1 express
advanced-circuit lane, all one tier): **12 iron-plate lanes, 5
copper-plate lanes, 2 plastic-bar lanes** — an exact, derived answer
for *this* target, not a citation of someone else's total.

## What this method still can't fully answer

**Partially resolved**: `relations/science_pack_ratios.md` now has
direct ingredient ratios for 6 of 7 science packs (all but
`space-science-pack`, which turned out to be a different, unmodeled
space-platform mechanic entirely — not just "not dumped yet"), so this
method can be applied to a science-pack target directly for
`automation-science-pack` (fully resolves to iron/copper) and
partially for `chemical-science-pack`/`utility-science-pack`. Still
open: `logistic-science-pack`, `military-science-pack`, and
`production-science-pack` bottom out at undecomposed leaf ingredients
(`inserter`, `transport-belt`, `piercing-rounds-magazine`, `grenade`,
`stone-wall`, `electric-furnace`, `productivity-module`, `rail`) whose
own recipes aren't dumped yet. Until those are pulled,
`layouts/main_bus.md`'s community-sourced starting template remains
the practical default for those three packs; this method is how to
move off it once both a specific target rate and the missing recipes
are in hand, one recipe at a time, the same way this walkthrough did
for steel + advanced-circuit.

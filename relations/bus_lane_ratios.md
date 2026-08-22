# Main-bus lane ratios (iron/copper-plate equivalent per downstream item)

How many belt-lanes of iron-plate/copper-plate (or other direct
ingredient) one full lane of a downstream item consumes — the number
that answers "if I run a full belt of X, how many belts of its
ingredients do I need to keep it fed."

Formula: `formulas/recipe_ingredient_ratio.py:ingredient_ratio`
(`ingredient_amount / result_amount`). This ratio is belt-tier- and
machine-speed-independent: if the downstream item flows at a full
belt's items/sec, the ingredient is consumed at `ratio × that same
items/sec` — exactly `ratio` lanes of the ingredient, assuming both
sides use the same belt tier. No `formulas/production_rate.py` call
needed; crafting speed cancels out of a pure consumption-per-output
ratio. See `examples/main_bus_lane_sizing.md` for a worked walkthrough
combining several of these ratios into an exact lane count for a
chosen target.

Inputs: `datapacks/dump/vanilla/recipe/{copper-cable,electronic-circuit,
advanced-circuit,processing-unit,iron-gear-wheel,stone-brick,plastic-bar,
sulfuric-acid,battery,pipe,low-density-structure}.json` — all a
documented `source.json` exception (third-party 2.0.65 dump, not this
project's own 2.0.77 run), added specifically to derive this table
instead of citing community-published ratios uncrossed.
`recipe/steel-plate.json` (this project's own 2.0.77 dump) is used
directly, no exception needed.

## Steel: the ratio the "4 iron / 2 steel" template hides

`steel-plate`: **5.0 iron-plate** per steel-plate (`recipe/steel-plate.json`
— `energy_required=16`, 5 `iron-plate` → 1 `steel-plate`). This is the
sharpest ratio in the whole table, and it's easy to misread the
practical template in `layouts/main_bus.md` because of it: "4 lanes
iron-plate, 2 lanes steel-plate" are **two separate finished-product
streams off the smelting stage, not sequential** — the 2 steel lanes
aren't carved out of the 4 iron lanes, they're smelted from *additional*
iron-plate (or iron ore) that never touches the bus as plain
iron-plate at all. Total iron-plate-equivalent smelting capacity
needed to support that template is `4 + (2 × 5.0) = 14` lanes, not 4 —
the 4 is only what's left over as unconverted plate for direct
consumption (circuits, gears, pipes). Undercounting this is a common
practical mistake: sizing the ore patch/furnace array off the bus's
visible "4 iron" figure alone leaves no headroom for steel, since
steel's real iron appetite is 2.5× the visible iron-plate lane count
in this particular template.

This is the item-flow (belt-lane) side of the ratio. For the
*furnace-count* side — how many iron-plate-smelting furnaces feed one
steel-plate-smelting furnace — see
`relations/iron_to_steel_furnace_ratio.md`: a clean 1:1 when both
stages use the same furnace tier (the `5.0` iron-plate-per-steel-plate
ratio and steel-plate's `energy_required=16` exactly cancel), only
diverging from 1:1 when the two stages deliberately use different
furnace tiers.

## Circuit chain (multi-hop, expanded through copper-cable)

| item | iron-plate | copper-plate | other |
|---|---|---|---|
| copper-cable | — | 0.5 | — |
| electronic-circuit (green) | 1.0 | 1.5 | — |
| advanced-circuit (red) | 2.0 | 5.0 | 2.0 plastic-bar |
| processing-unit (blue) | 24.0 | 40.0 | 4.0 plastic-bar, 5.0 sulfuric-acid (fluid, not a belt lane) |

The green-circuit row matches a figure independently cited in
community sourcing ("one lane of green circuit boards equals 1 lane
of iron plates and 1.5 lanes of copper plates") — this project derived
it from recipe data rather than taking that citation at face value,
per Hard rule 3, and it checks out exactly.

**Processing units are extremely iron/copper-hungry per lane** — 24
iron-plate-lanes and 40 copper-plate-lanes for one full blue-circuit
lane. This is *why* bases rarely dedicate a full bus lane to blue
circuits: even a large base's actual processing-unit demand is
normally a small fraction of one lane's worth, not a full lane — see
`layouts/main_bus.md`.

## low-density-structure: where copper overtakes iron

`low-density-structure` (rocket part / space-age structural item): 2
`steel-plate` + 20 `copper-plate` + 5 `plastic-bar` → 1
`low-density-structure`. Expanded through steel's 5:1 ratio, that's
**10.0 iron-plate-equivalent vs 20.0 copper-plate direct** — copper
demand is **2×** iron demand for this single item, the opposite
direction from steel (which is iron-only). This is the recipe-level
mechanism behind a community-cited aggregate figure for rocket
construction ("one rocket needs roughly 89.1k iron plates vs 92.5k
copper plates" — copper edging out iron), and it's why "iron is the
most-consumed ingredient" stops holding once low-density-structure /
rocket-part production becomes a meaningful share of total output —
see the summary below.

## Other items (single-hop)

| item | ratio |
|---|---|
| steel-plate | 5.0 iron-plate (see dedicated section above) |
| iron-gear-wheel | 2.0 iron-plate |
| stone-brick | 2.0 stone |
| plastic-bar | 10.0 petroleum-gas (fluid), 0.5 coal |
| sulfuric-acid (fluid) | 0.1 sulfur, 0.02 iron-plate (negligible), 2.0 water (fluid) |
| battery | 1.0 iron-plate, 1.0 copper-plate, 20.0 sulfuric-acid (fluid) |
| pipe | 1.0 iron-plate |
| low-density-structure | 10.0 iron-plate (via steel), 20.0 copper-plate, 5.0 plastic-bar (see dedicated section above) |

## Is iron really "the most consumed ingredient"? Not unconditionally

Not this project's own conclusion to assert outright — the honest
answer is stage-dependent, and this project's own ratios above only
explain *why*, not settle it on their own (a full answer needs the
complete science-pack recipe tree, not dumped here). What's
established:
- **Iron-leaning recipes**: steel (5:1, iron-only) has no copper
  counterpart of equivalent lopsidedness among the items covered here.
- **Copper-leaning recipes**: every circuit tier pulls more copper
  than iron per unit (1.5×/2.5×/1.67× for green/red/blue), and
  low-density-structure pulls 2× copper vs iron-equivalent.
- A community forum analysis (older game version — thread context
  suggests ~0.15-era, **not re-verified against 2.0.77**, treat as
  directional only) found iron leading copper by ~21% in aggregate
  across "red" through "grey"/"violet" science packs specifically, but
  the two highest tiers in that analysis ("yellow"/"white" — roughly
  today's utility/space science) flipped to **copper-leading**, one of
  them by more than 2:1 (44 iron : 101.8 copper).

Net: iron leads in early-to-mid game (automation/logistic/production-
science-heavy play), but copper closes the gap or overtakes once
circuit-heavy and especially rocket/space-content production becomes
significant — "iron is definitely the most consumed" is a reasonable
early/mid-game heuristic, not a universal rule, and this project
doesn't hold a full science-pack-tree derivation to state a precise
2.0.77 crossover point.

Fluids (`petroleum-gas`, `water`, `sulfuric-acid`) are marked
explicitly — they're pipe throughput, not belt lanes, and don't
compete for main-bus width the way solid items do.

See `relations/science_pack_ratios.md` for the same method applied one
level further downstream — science packs as the "output," these
items as ingredients among others.

Verified: 2026-08-08

# Iron-plate furnaces needed per steel-plate furnace

How many iron-plate-smelting furnaces are needed to keep one
steel-plate-smelting furnace fed — a furnace-*count* ratio, distinct
from `relations/bus_lane_ratios.md`'s `steel-plate: 5.0 iron-plate`
(that's a belt-lane/item-flow ratio, tier-independent by construction;
this one is furnace-count, which depends on which furnace tier each
stage uses).

Formula: reuses `formulas/production_rate.py` entirely, no new code —
`iron_furnaces = machines_to_saturate(steel_iron_consumption_rate,
crafting_speed_iron_furnace, 3.2, 1)`, where
`steel_iron_consumption_rate = production_rate(crafting_speed_steel_furnace,
16, 5)` (passing the recipe's `iron-plate` ingredient amount, 5, as
the third argument — same trick `mining_furnace_ratios.md` uses for
consumption rates).

Inputs: `recipe/steel-plate.json` (`energy_required=16`, 5
`iron-plate` → 1 `steel-plate`), `recipe/iron-plate` implicitly via
`smelting_ratios.md`'s `energy_required=3.2` group,
`furnace/*.json`'s `crafting_speed` (stone=1, steel=2, electric=2).

## The general rule: `iron_furnaces_per_steel_furnace = crafting_speed_steel / crafting_speed_iron`

Every `energy_required`/`ingredient_amount` term cancels out — the
ratio only depends on the two stages' relative furnace *speed*, not on
either recipe's specific numbers. This isn't a coincidence: steel-plate's
`energy_required=16` is *exactly* `5 × 3.2` (5 = the iron-plate
ingredient amount, 3.2 = iron-plate's own `energy_required`) — a
deliberate Wube balance choice, not something this project assumed.
Confirmed by direct computation (not just algebra): 9 furnace-tier
combinations all landed on exactly `1.0`, `0.5`, or `2.0`, matching
`crafting_speed_steel / crafting_speed_iron` in every case.

## iron_furnaces_per_steel_furnace

| iron stage furnace ↓ / steel stage furnace → | stone-furnace | steel-furnace | electric-furnace |
|---|---|---|---|
| stone-furnace | 1.0 | 2.0 | 2.0 |
| steel-furnace | 0.5 | 1.0 | 1.0 |
| electric-furnace | 0.5 | 1.0 | 1.0 |

**Same tier on both stages (the common case) is always exactly 1:1** —
1 iron-plate-smelting furnace feeds 1 steel-plate-smelting furnace of
the same tier, regardless of which tier. Only matters when the two
stages deliberately use *different* furnace tiers (e.g. upgrading iron
smelting to electric before steel smelting catches up) — then the
faster stage needs proportionally more/fewer partners.

Verified: 2026-08-08

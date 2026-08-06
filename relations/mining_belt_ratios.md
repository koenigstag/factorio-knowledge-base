# Mining drill → belt ratios

How many mining drills (of a given tier) are needed to saturate one
belt (of a given tier) with raw resource, keyed by `resource.minable.mining_time`
— same reasoning as `relations/smelting_ratios.md` keying by
`energy_required`: multiple resources share a `mining_time`, so this
avoids storing the same table under five different resource names.

Formula: `formulas/production_rate.py:machines_to_saturate`, with
`mining_speed`/`mining_time` in place of `crafting_speed`/`energy_required`
(same pattern, confirmed in `datapacks/dump/vanilla/UNITS.md`).

Drills included per `mining_time` group only where their
`resource_categories` actually cover it (checked against
`datapacks/dump/vanilla/mining-drill/*.json`): `electric-mining-drill`
and `burner-mining-drill` cover `basic-solid` only; `big-mining-drill`
covers both `basic-solid` and `hard-solid`, so it's the only one able
to mine `tungsten-ore` (`mining_time=5`, `category: hard-solid`).
`pumpjack` (fluid-only, `basic-fluid`) is excluded — see
`relations/basic_oil_processing_ratio.md` for its chain instead.

## mining_time = 1 (iron-ore, copper-ore, coal, stone, calcite)

| drill | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| electric-mining-drill | 30 | 60 | 90 | 120 |
| burner-mining-drill | 60 | 120 | 180 | 240 |
| big-mining-drill | 6 | 12 | 18 | 24 |

## mining_time = 0.5 (scrap)

| drill | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| electric-mining-drill | 15 | 30 | 45 | 60 |
| burner-mining-drill | 30 | 60 | 90 | 120 |
| big-mining-drill | 3 | 6 | 9 | 12 |

## mining_time = 2 (uranium-ore)

| drill | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| electric-mining-drill | 60 | 120 | 180 | 240 |
| burner-mining-drill | 120 | 240 | 360 | 480 |
| big-mining-drill | 12 | 24 | 36 | 48 |

## mining_time = 5 (tungsten-ore, hard-solid — big-mining-drill only)

| drill | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| big-mining-drill | 30 | 60 | 90 | 120 |

All 44 values verified by actually running `machines_to_saturate()`
against the real datapack values.

Verified: 2026-08-06

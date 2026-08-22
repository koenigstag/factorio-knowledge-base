# Rocket part ingredient ratio

`rocket-part` (crafted inside a `rocket-silo`, not a bus item):
1 `processing-unit` + 1 `low-density-structure` + 1 `rocket-fuel` → 1
`rocket-part` (`energy_required=3`). `rocket-fuel`: 10 `solid-fuel` +
10 `light-oil` (fluid) → 1 `rocket-fuel` (`energy_required=15`).

Formula: `formulas/recipe_ingredient_ratio.py:ingredient_ratio` — all
three main ingredients are 1:1 with `rocket-part` itself (trivial,
`amount=1` on every ingredient).

Inputs: `datapacks/dump/vanilla/recipe/{rocket-part,rocket-fuel}.json`
— `source.json` exception, same third-party 2.0.65 batch as
`bus_lane_ratios.md`'s recipes.

## Assembling-machine-3 count per rocket-silo (resolved)

Previously blocked on `rocket-silo.crafting_speed`, not in
`datapacks/dump/vanilla/` (only `rocket-silo-rocket`, a different
prototype — the flying rocket itself, not the silo building). Found
directly in `kirkmcdonald.github.io`'s own game-data file
(`github.com/KirkMcDonald/kirkmcdonald.github.io`, `data/
space-age-2.0.55.json`): `rocket-silo.crafting_speed = 1`.

`rocket-silo` making `rocket-part`: `production_rate(1, 3, 1)` =
0.3333 rocket-part/sec. Each ingredient (`processing-unit`,
`low-density-structure`, `rocket-fuel`, all `amount=1`) needs that
same 0.3333/sec from `assembling-machine-3` (`crafting_speed=1.25`,
confirmed matching this project's own dump):

| ingredient | `production_rate(1.25, energy_required, 1)` | assemblers per rocket-silo |
|---|---|---|
| processing-unit | 0.125/sec (`energy_required=10`) | 2.667 |
| low-density-structure | 0.0833/sec (`energy_required=15`) | 4.0 |
| rocket-fuel | 0.0833/sec (`energy_required=15`) | 4.0 |

Simplified ratio: **2 : 3 : 3**. This matches the ratio implied by a
community-cited figure ("~20:30:30 per silo," via
`factoriocheatsheet.com`'s citation of `kirkmcdonald.github.io/calc.html`
— also 2:3:3 once simplified) — the absolute counts differ because
that figure is scaled to some other reference rate (likely "per
rocket launch," which needs `rocket_parts_required` — not found in
`kirkmcdonald`'s data file, still not modeled here), but the ratio
between the three assembler counts, which is what actually matters for
layout, is independently confirmed.

Verified: 2026-08-08

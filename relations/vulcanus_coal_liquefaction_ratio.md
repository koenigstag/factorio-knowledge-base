# Vulcanus coal-liquefaction ratios: simple-coal-liquefaction → lubricant / cracking

`simple-coal-liquefaction` (oil-refinery, Vulcanus's substitute for
crude-oil-based `basic-oil-processing` where no oil field exists) feeds
two separate downstream chains: straight into `lubricant`, or into the
existing heavy/light oil cracking chain
(`relations/oil_cracking_ratio.md`). Both ratios below are cleanly
derived and match `factoriocheatsheet.com`'s Vulcanus `commonRatios`
citations exactly — unlike `vulcanus_power_chain.md`'s steam-turbine
ratio, no discrepancy here.

Formula: `formulas/production_rate.py:production_rate`.

Inputs: `datapacks/dump/vanilla/recipe/simple-coal-liquefaction.json`,
`recipe/lubricant.json`, `recipe/heavy-oil-cracking.json` /
`light-oil-cracking.json` (amounts already used by
`oil_cracking_ratio.md`) — all `crafting_speed=1`
(`oil-refinery`/`chemical-plant`, same assumption used throughout
`relations/`).

## 1 simple-coal-liquefaction : 1 lubricant

- `simple-coal-liquefaction`: `production_rate(1, 5, 50)` = 10
  heavy-oil/sec produced per refinery.
- `lubricant`: consumes 10 heavy-oil per craft at `energy_required=1`
  → 10 heavy-oil/sec consumed per chemical plant.
- 10/sec produced = 10/sec consumed → **1:1**, exact.

## 2 simple-coal-liquefaction : 1 heavy-oil-cracking : 1 light-oil-cracking

- 2 refineries → `2 × 10` = 20 heavy-oil/sec produced.
- `heavy-oil-cracking`: consumes 40 heavy-oil per craft at
  `energy_required=2` → 20 heavy-oil/sec consumed per chemical plant —
  matches the 2 refineries' output exactly. Produces `production_rate(1,
  2, 30)` = 15 light-oil/sec.
- `light-oil-cracking`: consumes 30 light-oil per craft at
  `energy_required=2` → 15 light-oil/sec consumed per chemical plant —
  matches the heavy-oil-cracking output exactly.
- **2:1:1**, exact, both links balanced.

## Verification

Independently derived from `data.raw` recipe amounts, not copied — and
matches `vulcanus.data.ts`'s `commonRatios` (1:1 for
liquefaction:lubricant, 2:1:1 for liquefaction:heavy-crack:light-crack)
exactly on both counts. `simple-coal-liquefaction` itself produces only
heavy-oil (no light-oil/petroleum-gas byproduct, unlike
`advanced-oil-processing`), which is why the downstream cracking ratio
here (2:1:1) differs in shape from the Nauvis `oil_cracking_ratio.md`
figure (20:5:17) despite sharing the same two cracking recipes — a
different, byproduct-free upstream input changes the balance point.

Verified: 2026-08-08

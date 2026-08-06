# Oil cracking ratio

Balanced ratio of `advanced-oil-processing` (oil-refinery) :
`heavy-oil-cracking` (chemical-plant) : `light-oil-cracking`
(chemical-plant) such that heavy-oil and light-oil have zero net
accumulation — all excess converges to petroleum-gas.

Formula: `formulas/cracking_ratio.py:cracking_ratio`, built on
`formulas/production_rate.py:production_rate`.

## advanced_oil_processing_heavy_oil_cracking_light_oil_cracking.ratio = [20, 5, 17]

Recipe rates (`crafting_speed`=1 for both `oil-refinery` and
`chemical-plant` — `datapacks/dump/vanilla/assembling-machine/`),
each via `production_rate(1, energy_required, amount)`:

| recipe | energy_required | in/out | amount | rate/machine |
|---|---|---|---|---|
| advanced-oil-processing | 5 | heavy-oil out | 25 | 5.0/s |
| advanced-oil-processing | 5 | light-oil out | 45 | 9.0/s |
| advanced-oil-processing | 5 | petroleum-gas out | 55 | 11.0/s |
| heavy-oil-cracking | 2 | heavy-oil in | 40 | 20.0/s |
| heavy-oil-cracking | 2 | light-oil out | 30 | 15.0/s |
| light-oil-cracking | 2 | light-oil in | 30 | 15.0/s |
| light-oil-cracking | 2 | petroleum-gas out | 20 | 10.0/s |

Balance: `heavy_crackers = heavy_produced / heavy_consumed_per_cracker`
= 5/20 = 0.25 per refinery; `light_crackers = (light_produced +
heavy_crackers × light_from_heavy_cracker) / light_consumed_per_cracker`
= (9 + 0.25×15)/15 = 0.85 per refinery. At 20 refineries: 20 × 0.25 =
**5** heavy-crackers, 20 × 0.85 = **17** light-crackers → **20:5:17**.

**total_petroleum_gas_per_sec_at_ratio = 390** — at this ratio: 20
refineries × 11/s direct + 17 light-crackers × 10/s = 220 + 170 = 390
petroleum-gas/sec total.

## Verification

Independently derived from `data.raw` recipe amounts (not copied from
a community source) — confirmed by running `cracking_ratio()` with an
assertion that it reproduces 20:5:17 exactly. This ratio is also
independently published by the Factorio community (e.g. Factorio
Forums "wiki on oil cracking ratios" thread, cited as the standard
"petroleum-focused" ratio, with 8:2:7 given as a simplified
approximation) — matching community consensus is a good sign, but per
CLAUDE.md rule 3 the number here is trusted because we derived it
ourselves from sourced recipe data, not because someone else also
publishes it.

This is also the same "20:5:17" example already named (without a
derivation) in this project's original `ARCHITECTURE.md` draft (not
yet imported into this repo) — this is the first time it's been
actually computed rather than just cited as an example.

Verified: 2026-08-06

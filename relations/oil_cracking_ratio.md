# Oil cracking ratio

Balanced ratio of `advanced-oil-processing` (oil-refinery) :
`heavy-oil-cracking` (chemical-plant) : `light-oil-cracking`
(chemical-plant) such that heavy-oil and light-oil have zero net
accumulation — all excess converges to petroleum-gas.

Formula: `formulas/cracking_ratio.py:cracking_ratio`, built on
`formulas/production_rate.py:production_rate`.

## advanced_oil_processing_heavy_oil_cracking_light_oil_cracking.ratio

`{"advanced-oil-processing": 20, "heavy-oil-cracking": 5, "light-oil-cracking": 17}`

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

**Further cross-check (2026-08-08)**: `factoriocheatsheet.com`'s
source (github.com/deniszholob/factorio-cheat-sheet) independently
lists both this exact 20:5:17 ratio ("perfectCrackingRatio") and the
8:2:7 simplified one ("simpleCrackingRatio") — third source agreeing
with both this project's own derivation and the forum citation above.
That same source also lists a "moduled" ratio (15:6:22) and separate
ratios for the `coal-liquefaction` path — `coal-liquefaction`'s recipe
(distinct from Vulcanus's `simple-coal-liquefaction`, see
`relations/vulcanus_coal_liquefaction_ratio.md`) still isn't in
`datapacks/dump/vanilla/recipe/`, so that half stays a known gap. The
moduled ratio is addressed below.

Verified: 2026-08-06

## Moduled cracking ratio (15:6:22) — assumption sourced, result not reproduced exactly

Formula: `formulas/production_rate.py:production_rate` (now takes an
optional `productivity_multiplier`).

Inputs: `datapacks/dump/vanilla/recipe/advanced-oil-processing.json`,
`recipe/heavy-oil-cracking.json`, `recipe/light-oil-cracking.json`
(same recipes as above, unchanged), plus
`datapacks/dump/vanilla/module/productivity-module-3.json`
(`effect.productivity=0.10`).

The cheat sheet's own page (`oil-refining.component.html`'s
`note_oil_ratio` footnote) states its methodology explicitly — not
guessed here: *"modified to use v[current] recipe data with 1.3
productivity and 5.55 craft speed for Refineries (10 beacons) and 5
craft speed for Chemical Plants (8 beacons)."* `1.3` productivity
matches exactly 3× `productivity-module-3` in each machine (`1 + 3 ×
0.10`) — confirming the guess that started this: the moduled ratio's
productivity does come from productivity modules, tier 3, one per
module slot (both `oil-refinery` and `chemical-plant` have
`module_slots=3`, `datapacks/dump/vanilla/assembling-machine/`). The
5.55/5.0 crafting speeds come from beacon-transmitted speed-module
effects — this project *does* now have a beacon-diminishing-returns
formula (`formulas/beacon_effect.py`/`relations/beacon_effect.md`,
FFF #409, derived independently of this file) — but running it doesn't
reproduce the cited speeds exactly either: `beacon_effect_multiplier(10,
1.5, profile)` × 2 `speed-module-3`/beacon × 0.5 effect/module = 4.743
bonus → **5.743** crafting speed for a 10-beacon refinery (cited 5.55,
+3.5%); the same for 8 beacons → **5.242** for chemical plants (cited
5.0, +4.8%). Close, directionally consistent with the "2 modules per
beacon" assumption (`beacon.module_slots=2`), but not exact — a third
data point (alongside the heavy-cracker mismatches below) that this
source's own build likely includes some unstated adjustment (fewer
than 2 modules in some beacons, a different beacon count than
literally stated, etc.), not that this project's formula is wrong: the
same `beacon_effect_multiplier` function's worked table in
`relations/beacon_effect.md` is independently verified against the
actual `data.raw` `profile` array, not just the sqrt approximation.

Plugging those exact stated numbers into `production_rate`
(`productivity_multiplier=1.3`, `crafting_speed=5.55` for the refinery
recipe, `crafting_speed=5.0` for both cracking recipes) and solving the
same balance used for the 20:5:17 case above:

`heavy_crackers_per_refinery` = 0.36075, `light_crackers_per_refinery`
= 1.33478 → at 15 refineries: **5.41 heavy-crackers, 20.02
light-crackers** — not the cited **6** and **22**. The shortfall is
consistent (heavy at 90.2% of cited, light at 91.0%), which rules out
simple independent rounding of two unrelated numbers, but no single
extra factor found here (a bigger beacon count, a different
productivity tier, main-vs-secondary-product handling) closes a ~10%
gap cleanly.

**Closed as an accepted discrepancy (2026-08-09), not left pending.**
Two further hypotheses were tested before closing this out, both ruled
out with exact-fraction arithmetic (`fractions.Fraction`, not decimal
rounding, to eliminate float-precision as a cause):

- **Productivity applies to the refinery only, not the crackers**
  (re-reading the cheat sheet's footnote as scoping "1.3 productivity"
  to refineries alone). Doesn't change the heavy-cracker figure at
  all — heavy-cracker count is driven purely by heavy-oil
  *consumption* (input side), which productivity never affects
  regardless of which machine has it — so this can't be the source of
  even the heavy-cracker gap (5.41 vs 6), let alone light's. Makes the
  light-cracker gap worse (1.2265/refinery vs the needed 1.4667), not
  better.
- **Back-solving for a refinery count that hits 6 and 22 exactly**
  under this project's per-refinery rates: `6/0.36075 ≈ 16.63`
  refineries from the heavy side, `22/1.334775 ≈ 16.49` from the light
  side — not equal to each other, not equal to 15, and not clean
  integers. If the cited ratio were this project's same rates at some
  different refinery count, both sides would back-solve to the *same*
  N; they don't, which means at least one of the three per-machine
  rates in the source's own build differs from what this project
  computed from the stated 1.3/5.55/5.0 inputs — not just a scaling or
  rounding choice.

**Independent second source, found searching for corroboration
(2026-08-09) rather than to reopen this**: forums.factorio.com t=100021
("Are production ratios changed by modules and why?") —
**astroshak** independently works the same kind of moduled example,
different but comparable inputs (refinery speed 5.55 — matching this
project's figure exactly; chemical-plant speed 4.55, not this
project's 5.0; "productivity bonus of 30%," matching 1.3), starting
from the same unmoduled 20:5:17 base, and states the result as **20
refineries : 9 heavy-crackers : 29 light-crackers**. Re-running this
project's own formula with astroshak's exact stated inputs (5.55/4.55
speeds, 1.3 productivity on both machine types) gives **7.93
heavy-crackers, 29.34 light-crackers** at 20 refineries — light lands
within ~1.2% of astroshak's cited 29 (29.34 vs 29, essentially a
rounding-level difference), but heavy again falls well short of the
cited figure (7.93 vs 9, 88%) — the same lopsided
pattern (light reproduces closely, heavy doesn't) seen against the
cheat sheet's 15:6:22. Two independent community sources, two
different speed assumptions, the same specific shape of mismatch — this
reads as corroboration that the *heavy-cracker* figure specifically is
where community-published moduled ratios diverge from a pure
continuous-balance derivation (both likely rounding it up for a
practical safety margin, or building for an additional heavy-oil
consumer like lubricant alongside cracking, rather than a pure
zero-net-accumulation ratio), not evidence of an error in this
project's own math. Strengthens the closure below rather than
reopening it.

**Conclusion**: the recipe math itself is identical to the
already-verified 20:5:17 case, and the productivity-module assumption
is directly sourced and confirmed (3× productivity-module-3, matching
the user's initial guess) — but the source's own stated methodology
does not reproduce its own published 15:6:22 figure under this
project's formula, and no tested adjustment closes the gap cleanly.
The page's own caution note (*"if you use the original spreadsheet as
is, it will not produce correct results... you would need to make the
modified copy"*) is the most likely explanation: an undocumented
manual adjustment in the source's own spreadsheet beyond its stated
inputs. Per CLAUDE.md rule 3, this project's own 5.41:15:20.02 stands
as the trusted figure — derived from primitives, not cited — and
15:6:22 is recorded here as a sourced-but-unreproduced community
number, not adopted. Not pursued further; closed, same pattern as
`vulcanus_power_chain.md`'s turbine-ratio flag.

Verified: 2026-08-09

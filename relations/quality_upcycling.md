# Quality upcycling: module chance, tier cascade, recycler yield

Formulas: `formulas/quality_upgrade_chance.py` (`module_quality_chance`,
`tier_jump_distribution`), `formulas/recycler_yield.py`
(`recycler_ingredient_amount`).

## module_quality_chance_fraction

`module.effect.quality` in `data.raw` (see
`datapacks/dump/vanilla/module/quality-module*.json`) is stored at
×10 its actual in-game percentage — see `UNITS.md`'s "Dimensionless
multipliers" exception note. Derived by cross-checking all 3 tiers
against wiki-stated real percentages, not assumed from one data point:

| tier | data.raw `effect.quality` | wiki % | `module_quality_chance(x)` |
|---|---|---|---|
| quality-module | 0.1 | +1% | 0.01 ✓ |
| quality-module-2 | 0.2 | +2% | 0.02 ✓ |
| quality-module-3 | 0.25 | +2.5% | 0.025 ✓ |

All three divide out exactly, confirming the ×10 convention rather
than assuming it. Not covered: a module's own *quality* (e.g. a
legendary quality-module) further increases this effect — the wiki
confirms the behavior (+2.5%/+5%/+6.2% for legendary-quality
tier-1/2/3 modules) but the module-quality → effect-multiplier
formula isn't stated here, since it wasn't found directly in
`data.raw`.

## tier_jump_distribution_fraction_given_upgrade

Given a quality upgrade was triggered (by `module_quality_chance`
above — a separate, prior roll), how far it cascades:
`tier_jump_distribution([0.1, 0.1, 0.1, 0.1])` = `[0.9, 0.09, 0.009,
0.001]`.

Inputs: `quality.<tier>.next_probability=0.1`, present on
`normal`/`uncommon`/`rare`/`epic` (`datapacks/dump/vanilla/quality/`)
— `legendary` has none, being the terminal tier the leftover 0.1%
collapses onto (its `level=5`, not `4`, skipping a number — cosmetic,
not a computed field, noted here since it's the kind of thing that
looks like a bug on first read). This is a real 4-gate Markov chain,
not a single lookup: at each tier, 90% chance the cascade stops there,
10% chance it continues to check the next tier's own
`next_probability`.

| jump | probability |
|---|---|
| +1 (e.g. normal→uncommon) | 90% |
| +2 | 9% |
| +3 | 0.9% |
| +4 (normal straight to legendary) | 0.1% |

Matches the commonly-cited community "90/9/0.9%" figure, but derived
here from the actual `next_probability` field chain rather than cited
directly.

## recycler_ingredient_return_fraction = 0.25

Confirmed against 3 concrete recipes in
`datapacks/dump/vanilla/recipe/`, not just the wiki's stated "25%":

| recipe | ingredient's amount in its real crafting recipe | recycling result amount | fraction |
|---|---|---|---|
| `iron-plate-recycling` | 1 (iron-plate is itself a base item) | 0.25 (via `probability`) | 25% |
| `iron-gear-wheel-recycling` | 2 iron-plate | 0.5 iron-plate | 25% |
| `electronic-circuit-recycling` | 1 iron-plate / 3 copper-cable | 0.25 / 0.75 | 25% / 25% |

`recycler_ingredient_amount(2, 0.25)=0.5`,
`recycler_ingredient_amount(1, 0.25)=0.25`,
`recycler_ingredient_amount(3, 0.25)=0.75` — all three reproduce the
actual recipe result amounts exactly, not just the wiki quote.

The `recycler` entity itself (`datapacks/dump/vanilla/furnace/
recycler.json` — it's a `furnace`-type prototype, not its own type)
has `allowed_effects` including `quality` but not `productivity`,
which is why the loop below can concentrate quality without also
duplicating matter.

## The upcycling loop (not modeled numerically here)

Combine both mechanics: craft with quality modules (chance to output a
higher tier) → recycle non-target-quality output with quality modules
too (chance the *returned ingredients* are already a higher tier) →
craft again with those. Both stages independently roll
`module_quality_chance` + `tier_jump_distribution`, so quality
accumulates over repeated passes — this is why a closed
craft-then-recycle loop trends toward Legendary given enough cycles,
even though each individual roll is small.

This file stops at the two per-stage mechanics; it doesn't attempt a
full loop-convergence number (expected passes to legendary, steady-
state legendary fraction). That depends on which modules are installed
where and isn't a single derivable constant the way the rest of this
file is — a genuine absorbing Markov chain over the full loop, not
scoped here.

Verified: 2026-08-07

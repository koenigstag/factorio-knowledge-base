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
than assuming it.

**Module-quality effect on chance (resolved 2026-08-08)**: a
quality-module's own *quality* (e.g. a Legendary-quality
quality-module) further increases its upgrade-chance percentage.
Previously only the Legendary-tier endpoints were confirmed (via the
wiki: +2.5%/+5%/+6.2% for tier-1/2/3). `factoriocheatsheet.com`'s
source (`github.com/deniszholob/factorio-cheat-sheet`,
`quality-quality-table.data.ts`, uncited in-repo but matching this
project's wiki-confirmed Legendary values exactly) gives the full
table:

| module quality → | Normal | Uncommon | Rare | Epic | Legendary |
|---|---|---|---|---|---|
| quality-module (tier 1) | 1% | 1.3% | 1.6% | 1.9% | 2.5% |
| quality-module-2 (tier 2) | 2% | 2.6% | 3.2% | 3.8% | 5% |
| quality-module-3 (tier 3) | 2.5% | 3.2% | 4% | 4.7% | 6.2% |

Normal-quality and Legendary-quality columns match this project's own
`module_quality_chance` table above and the wiki's cited endpoints
exactly — no clean multiplicative pattern connects the columns
(Uncommon isn't a fixed ×N of Normal across rows, e.g. tier-1 is
1×1.3=1.3 but tier-3 is 2.5×1.3=3.25≠3.2), so this is recorded as an
empirical table, not a formula — no `formulas/` function added since
there's no clean closed form found to encode.

## tier_jump_distribution_fraction_given_upgrade

Given a quality upgrade was triggered (by `module_quality_chance`
above — a separate, prior roll), how far it cascades:
`tier_jump_distribution([0.1, 0.1, 0.1, 0.1])` = `[0.9, 0.09, 0.009,
0.001]`.

Inputs: `quality.<tier>.next_probability=0.1`, present on
`normal`/`uncommon`/`rare`/`epic` (`datapacks/dump/vanilla/quality/`)
— `legendary` has none, being the terminal tier the leftover 0.1%
collapses onto (its `level=5`, not `4`, skipping a number — **not just
cosmetic**, see `relations/quality_stat_bonus.md`: `level` drives the
stat-bonus formula too, and `5` is what lands legendary's bonus on a
round `+150%` instead of `+120%`). This is a real 4-gate Markov chain,
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

Second, independent corroboration: FFF #375 ("Quality") states the
design intent directly — recycling returns *"25% of the original
ingredients back"* — matching the recipe-derived figure above from a
primary source, not just the wiki.

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
scoped here. FFF #375 states its own rough estimate for context (not
independently derived by this project, so not adopted as a project
fact): producing a legendary item through this loop is *"about 56
times more expensive"* than a normal one.

**Why the loop doesn't run away to infinite productivity**: quality
modules stack with productivity modules, and productivity compounds
across upcycling passes the same way quality chance does — so nothing
here structurally stops a factory from stacking arbitrarily many
productivity sources. The actual limiter is `RecipePrototype.
maximum_productivity` (`lua-api.factorio.com/latest/prototypes/
RecipePrototype.html`), a real `data.raw` field defaulting to `3.0`
(+300%) per recipe — confirmed by FFF #375's plain-English statement of
*"a machine limit on productivity to be +300%."* Not independently
cross-checked against this project's own dump: none of the 47 recipes
in `datapacks/dump/vanilla/recipe/` show an explicit
`maximum_productivity` override, consistent with all of them relying
on the schema default rather than proof the default is actually 3.0 in
this game version — recorded here from the official docs + FFF, the
same confidence tier as `mechanics/rails.md`'s elevated-rail
tall-entity note.

Verified: 2026-08-07 (original), 2026-08-09 (FFF #375 corroboration + productivity-cap note)

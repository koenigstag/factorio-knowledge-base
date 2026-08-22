# Quality tier stat bonus, derived from `quality.level`

Formula: `formulas/quality_stat_bonus.py` (`default_stat_multiplier`,
`linear_stat_multiplier`, `capped_range_multiplier`).

Input: `quality.<tier>.level` — already in
`datapacks/dump/vanilla/quality/*.json` (`normal=0`, `uncommon=1`,
`rare=2`, `epic=3`, `legendary=5`). The per-level multiplier constants
themselves (0.3, 1, 0.1, and the 3.0 cap) are **not** present in this
project's own dump — none of the five `quality/*.json` files override
them, meaning vanilla relies on `QualityPrototype`'s own schema
defaults rather than setting explicit values. Sourced instead from the
official Lua API prototype docs
(`lua-api.factorio.com/latest/prototypes/QualityPrototype.html`),
which state the defaults directly:

- `default_multiplier`: *"Default: `1 + 0.3 * level`"* — the generic
  bonus (health, and any stat without its own override field).
- `tool_durability_multiplier`, `accumulator_capacity_multiplier`,
  `flying_robot_max_energy_multiplier`: each *"Default: `1 + level`"*
  — steeper than the generic formula, +100% per level instead of +30%.
- `range_multiplier` (e.g. electric-pole wire reach):
  *"Default: `min(1 + 0.1 * level, 3)`"* — the one family with a
  documented ceiling, though at vanilla's max level (5, legendary) it
  only reaches 1.5×, nowhere near the 3.0× cap (would need level ≈ 20).

## default_stat_bonus_percent (health, generic stat)

| tier | level | multiplier | bonus |
|---|---|---|---|
| normal | 0 | 1.0 | +0% |
| uncommon | 1 | 1.3 | +30% |
| rare | 2 | 1.6 | +60% |
| epic | 3 | 1.9 | +90% |
| legendary | 5 | 2.5 | +150% |

Cross-checked against FFF #375 ("Quality"), which states these exact
percentages in plain English for the generic quality bonus: *"+30%
bonus"* (uncommon) through *"+150% bonus"* (legendary) — matches
`default_stat_multiplier` computed from `level` alone, confirming the
formula rather than just the endpoints.

## Why legendary's `level=5`, not `4` — no longer just "cosmetic"

`relations/quality_upcycling.md` previously flagged `legendary.level=5`
(skipping `4`) as looking like a bug with no stated reason. Given
`default_stat_multiplier = 1 + 0.3 * level`, the skip has a clear
purpose: level 4 would only give `1 + 0.3*4 = 2.2` (+120%), a small
step up from epic's +90%. Using `5` instead lands legendary at exactly
`2.5` (+150%) — a full extra 0.3 step, matching the "5-tier" quality
ladder's other round numbers (30/60/90/**150**, not 30/60/90/120) and
FFF #375's own stated figure. Still not explicitly confirmed by Wube as
*the* reason (no direct quote saying "we skipped 4 for this reason"),
but it's no longer an unexplained coincidence — the numbers land
exactly where this reading predicts them to.

## linear_stat_bonus_percent (durability / accumulator capacity / robot energy)

| tier | level | multiplier | bonus |
|---|---|---|---|
| normal | 0 | 1 | +0% |
| uncommon | 1 | 2 | +100% |
| rare | 2 | 3 | +200% |
| epic | 3 | 4 | +300% |
| legendary | 5 | 6 | +500% |

Notably steeper than the generic bonus — a legendary accumulator holds
6× a normal one's charge, not 2.5×. Not independently cross-checked
against a real accumulator/tool entity file in this project's own dump
(no `accumulator`/tool-type prototypes extracted yet) - recorded here
from the Lua API docs' stated defaults only.

## range_stat_bonus_percent (e.g. wire reach)

| tier | level | multiplier | bonus |
|---|---|---|---|
| normal | 0 | 1.0 | +0% |
| uncommon | 1 | 1.1 | +10% |
| rare | 2 | 1.2 | +20% |
| epic | 3 | 1.3 | +30% |
| legendary | 5 | 1.5 | +50% |

Source: https://lua-api.factorio.com/latest/prototypes/QualityPrototype.html,
https://factorio.com/blog/post/fff-375
Verified: 2026-08-09

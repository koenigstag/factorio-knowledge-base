# Science pack ingredient ratios

Directly resolves the gap flagged in
`examples/main_bus_lane_sizing.md` ("a genuinely complete ideal-bus
derivation needs all 7 science-pack recipes, not dumped yet") — 6 of 7
now are (`space-science-pack` excluded, see below).

Formula: `formulas/recipe_ingredient_ratio.py:ingredient_ratio`, same
method as `relations/bus_lane_ratios.md`. Inputs:
`datapacks/dump/vanilla/recipe/{automation,logistic,military,chemical,
production,utility}-science-pack.json` — `source.json` exception, same
third-party 2.0.65 batch as `bus_lane_ratios.md`'s recipes. Cross-checked
against `factoriocheatsheet.com`'s `common-ratios.data.ts` science
section (same source tier) at the recipe level, not copied — the
site's numbers are machine-count ratios (needs `crafting_speed`,
computed differently); this file's ratios are pure ingredient-per-pack
amounts, tier/speed-independent like `bus_lane_ratios.md`.

## direct_ingredient_ratio (1 lane of pack → N lanes of each direct ingredient)

| pack | ingredients |
|---|---|
| automation-science-pack | 1.0 copper-plate, 1.0 iron-gear-wheel |
| logistic-science-pack | 1.0 inserter, 1.0 transport-belt |
| military-science-pack | 0.5 piercing-rounds-magazine, 0.5 grenade, 1.0 stone-wall |
| chemical-science-pack | 1.0 engine-unit, 1.5 advanced-circuit, 0.5 sulfur |
| production-science-pack | 0.333 electric-furnace, 0.333 productivity-module, 10.0 rail |
| utility-science-pack | 1.0 low-density-structure, 0.667 processing-unit, 0.333 flying-robot-frame |

## fully_decomposed_bus_lane_equivalent (where this project already holds the sub-recipe)

| pack | iron-plate | copper-plate | plastic-bar | other |
|---|---|---|---|---|
| automation-science-pack | 2.0 | 1.0 | — | — |
| logistic-science-pack | 5.5 | 1.5 | — | — |
| chemical-science-pack | 3.0 | 7.5 | 3.0 | + undecomposed: 1.0 engine-unit, 0.5 sulfur |
| utility-science-pack | 26.0 | 46.67 | 7.67 | 3.33 sulfuric-acid (fluid) + undecomposed: 0.333 flying-robot-frame |

`automation-science-pack` fully resolves (`iron-gear-wheel` = 2.0
iron-plate, already in `bus_lane_ratios.md`). `chemical-science-pack`
and `utility-science-pack` partially resolve through
`advanced-circuit`/`low-density-structure`/`processing-unit` (already
held), with one undecomposed leaf ingredient each. `military-science-pack`
and `production-science-pack` don't decompose further yet —
`piercing-rounds-magazine`, `grenade`, `stone-wall`, `electric-furnace`,
`productivity-module`, `rail` recipes aren't in
`datapacks/dump/vanilla/recipe/` yet. Left as named leaf ingredients
rather than guessed.

### logistic-science-pack: resolved 2026-08-08

Needed `recipe/inserter.json` (1 electronic-circuit + 1 iron-gear-wheel
+ 1 iron-plate → 1 inserter) and `recipe/transport-belt.json` (1
iron-plate + 1 iron-gear-wheel → 2 transport-belt) — both pulled from
the same third-party Bilka2 2.0.65 gist used throughout this file.
`electronic-circuit` itself decomposes further (1.0 iron-plate + 1.5
copper-plate, `bus_lane_ratios.md`), so `inserter` fully decomposes to
`1.0×(1.0+1.0) + 2.0(iron-gear-wheel) + 1.0(direct)` = **4.0
iron-plate** + **1.5 copper-plate**; `transport-belt` (per output item,
recipe gives 2/craft) decomposes to `0.5(direct) + 0.5×2.0(gear)` =
**1.5 iron-plate** + 0 copper. Summing `1.0 inserter + 1.0
transport-belt`: **5.5 iron-plate + 1.5 copper-plate** per
logistic-science-pack — this project's first fully independent
resolution of this pack (no cheat-sheet citation existed to cross-check
against; `factoriocheatsheet.com`'s `commonRatios` doesn't cover
logistic-science-pack's own ingredient chain, only assembler-count build
ratios elsewhere). Used directly in
`layouts/scalable_main_base.md`'s green-science module
sizing, which keeps `electronic-circuit` as a bus-tapped intermediate
rather than decomposing it locally — see that file for the
port-level (not fully-decomposed) ratio.

## space-science-pack: excluded, different mechanic entirely

Not what `factoriocheatsheet.com`'s citation (rocket-part/processing-
unit/rocket-fuel/low-density-structure/solar-panel/accumulator via a
rocket silo) suggested — pulling the actual current recipe from the
same third-party dump shows `space-science-pack` is instead: 2
`iron-plate` + 1 `carbon` + 1 `ice` → 5 `space-science-pack`, gated by
`surface_conditions: gravity = 0` (crafted in zero gravity — a space
platform, not a rocket silo on a planet surface) — see
`mechanics/surface-conditions.md` for how this gating mechanism works
generally and `glossary/canonical/surface.md` for why space-platform
specifically is the only surface with `gravity=0`.

**Resolved 2026-08-08**: the cheat sheet's citation is confirmed
stale, not describing a different mechanic. Checked
`kirkmcdonald.github.io`'s own game-data file
(`github.com/KirkMcDonald/kirkmcdonald.github.io`, `data/
space-age-2.0.55.json` — a primary source for that widely-used
calculator, and the tool the cheat sheet's own citations point to)
directly: even at 2.0.55 — older than either dump this project has
used — its `space-science-pack` recipe already matches this project's
2 iron-plate + 1 carbon + 1 ice exactly, `surface_conditions` included.
The cheat sheet's rocket-part-based entry for this pack was simply
never updated after Wube's recipe change (that section of its source
carries a `// TODO: Calculate?` and a neighboring commented-out
"Purple Science" block, consistent with being known-incomplete).
Space-platform crafting still isn't modeled anywhere in this project
(no `surface`/`space-platform` mechanics recorded), so still excluded
here — but now confirmed to be a stale citation, not an open question.

**Cross-validation bonus**: the same `kirkmcdonald.github.io` data file
was checked against all 6 packs above plus `rocket-part`/`rocket-fuel`
(`relations/rocket_part_ratio.md`) — every ingredient, amount, and
`energy_required` matches this project's own third-party-dump-derived
values exactly. Independent confirmation from a second, differently-sourced
third party, not just internal consistency.

Verified: 2026-08-08

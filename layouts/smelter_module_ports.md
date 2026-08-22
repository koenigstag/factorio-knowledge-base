# Smelter module ports: ore/coal outside, result inside

A tileable multi-row furnace module (two furnace rows flanking a
shared belt) has two ways to arrange its ore/coal/result lanes, and
one is meaningfully better than the other — not just a stylistic
choice.

## "Plate on the inside" — the recommended pattern

Ore and coal run on the **outer** belts (one ore + one coal lane per
furnace row, on the side facing away from the module's center); the
smelted result (plates/steel/bricks) runs on a **single shared belt
down the center**, collecting output from both rows at once.

**Why this is better, not just different**: with two symmetric furnace
rows producing at the same rate, their combined output balances onto
the single center belt automatically — no separate balancer entity
needed, and no "recombine two output lines into one" problem down the
line. The source guide states this directly: *"Truly inherently
balanced because of the way the ore/coal is distributed with the
Splitters on the right, and will automatically balance the plate belt
if you build the same amount of furnaces on each side."* Fewer
inserters than the alternative, too.

Mechanically, the balancing isn't magic: each row's output inserters
drop plates onto the shared center belt from their own side, and per
[mechanics/inserter-belt-lane-placement.md](../mechanics/inserter-belt-lane-placement.md)
an inserter always places onto the *far* lane from itself — so each
row fills the lane closer to the *other* row. With equal furnace counts
on both rows, the inserters themselves fill both lanes of that belt
evenly as they place items — no splitter or dedicated balancer entity
is doing the work on the *output* side; the splitters in the source
guide's setup are on the *input* (ore/coal) side instead.

## "Plate on the outside" — the alternative, and why it's worse

Inverts the arrangement: plates go on the outer belts, ore/coal come
in through the center. More compact, but per the same source: *"creates
a disadvantage: combining two separate plate lines into one output can
be problematic"* — the exact balancing problem "inside" avoids for free
has to be solved by hand instead.

## Confirmed against two real curated blueprints

[blueprints/curated/earlygame/4x2-stone-furnaces-w-upgrade-spacing.md](../blueprints/curated/earlygame/4x2-stone-furnaces-w-upgrade-spacing/4x2-stone-furnaces-w-upgrade-spacing.md)
follows this pattern exactly, verified tile-by-tile (not just visually
similar): outer lanes `x=-6.5`/`x=5.5` carry ore, inner lanes
`x=-5.5`/`x=4.5` carry coal, and the shared center lane `x=-0.5`
carries the combined result from both furnace rows — all 5 lanes pass
straight through top-to-bottom so the module tiles vertically, each
copy's export row feeding the next copy's import row.

[blueprints/curated/midgame/4x2-electrical-furnaces-w-tier2-belts.md](../blueprints/curated/midgame/4x2-electrical-furnaces-w-tier2-belts/4x2-electrical-furnaces-w-tier2-belts.md)
is the same author's midgame upgrade of the same module — same
outer-ore/center-result arrangement, minus the coal lanes entirely
(`electric-furnace` runs on electricity, not burned fuel), confirming
the pattern holds independent of furnace tier and that "outer" isn't
specifically "ore + coal" so much as "whatever the furnace consumes."

Contrast: [24x2-stone-furnaces-module.md](../blueprints/curated/earlygame/24x2-stone-furnaces-module/24x2-stone-furnaces-module.md)
in the same `curated/` collection is a *different* shape of module
entirely — one input side, one output side (not two rows flanking a
center), ore combined via a `splitter` before the furnace rows rather
than kept parallel, single result lane. Not a counter-example to the
inside/outside principle above; it's a single-direction-flow design
the two-rows-plus-shared-center question doesn't apply to.

Source: https://steamcommunity.com/sharedfiles/filedetails/?id=862972621
(community guide, "Plate on the inside" vs "Plate on the outside"
comparison) — cross-checked against this project's own curated
blueprint rather than taken on the guide's word alone.
Verified: 2026-08-09

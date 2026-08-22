# 0001 — Inserter throughput: cited constraint, not a derived formula

## Status
Accepted

## Context

`datapacks/dump/vanilla/UNITS.md` flagged `inserter.rotation_speed`/
`extension_speed` early on as needing "a geometry-aware formula" to
convert into actual items/sec — unlike `recipe.energy_required` ÷
`furnace.crafting_speed`, which is a clean continuous division that
matched wiki-published values exactly. This was picked up as a
candidate for `formulas/`, following the same pattern as
`formulas/production_rate.py` and `formulas/cracking_ratio.py`. It
would also complete the wagon-loading-throughput picture: the count in
`mechanics/trains.json` (12 / 24 inserters per wagon) needs a
matching per-inserter rate to produce a total throughput number.

## Alternatives considered

**Derive our own formula from inserter geometry**, the same way
`production_rate()`/`cracking_ratio()` were built.
- Con: research turned up a specific complication that breaks the
  clean-continuous-math approach used elsewhere — rotation timing is
  tick-discretized. A naive `1 / rotation_speed` gives a non-integer
  tick count that the engine can't actually run; e.g. fast-inserter's
  rotation_speed implies 25 ticks for a full turn, but the engine can
  only do whole-tick half-turns, so it actually takes 24
  (`floor(0.5 / rotation_speed) * 2 + 2`, not continuous division).
  There's also a separate extension/retraction component, and it's
  not confirmed here whether the two run sequentially (sum) or
  in parallel (max) — found conflicting-looking formula fragments,
  not a single authoritative equation.
- Stronger con: the one dedicated open-source library built
  specifically for this problem, `JanSharp/inserter-throughput-lib`,
  states outright that it does *not* fully simulate the mechanic
  (belt item-availability timing makes that impractical to reproduce)
  and instead uses a parametrized estimate whose "magic values" are
  iteratively tuned by comparing against *real measured in-game
  values*. If the best existing community tool needs empirical
  calibration against live gameplay, a formula built here without
  the same calibration ability would be materially less trustworthy
  than `production_rate()`/`cracking_ratio()`, which were verified
  against independently-published clean values (24/48 furnaces per
  belt, 20:5:17 cracking ratio) with no such caveat.

**Skip inserter throughput entirely for now**, revisit later.
- Con: leaves `mechanics/trains.json`'s inserter counts without a
  matching rate, silently. Someone hitting this gap later would have
  to redo the same research to find out why nothing exists.

**Cite the wiki's own published reference figures as a constraint,
don't derive.**
- Pro: matches how `max_inserters_per_wagon` is already handled —
  an empirically-tested fact from Wube/the community, not something
  this project derives from primitives. The wiki's own
  `Inserters#Inserter_Throughput` page publishes cycles/sec by tier
  for the chest-to-chest case (the cleanest, least setup-dependent
  scenario) directly.
- Con: the wiki itself states chest-to-belt/belt-to-chest throughput
  depends on belt saturation and timing, so even citing doesn't give
  one fixed number for the cases that matter most for factory
  planning (loading a wagon from a belt, feeding an assembler from a
  belt).

## Decision

Third alternative, refined after the initial pass. `mechanics/inserters-throughput.md`
cites the wiki's chest-to-chest cycles/sec figures, explicitly flagged
as **not independently re-verified to exact precision**, and notes
chest-to-belt throughput is scenario-dependent, not a fixed constant.
`formulas/inserter_cycle_time.py` (deriving cycles/sec from
`rotation_speed`/`extension_speed` ourselves) is still not written,
for the reasons above.

However, a second, smaller formula turned out to be legitimate:
`items/sec = cycles/sec × items_per_cycle` is plain multiplication,
not a derivation of cycles/sec itself — no calibration risk. For 4 of
the 6 inserter tiers (`inserter`, `burner-inserter`,
`long-handed-inserter`, `fast-inserter`), `items_per_cycle=1` is
unambiguous (checked directly against `datapacks/dump/vanilla/inserter/*.json` —
none of the four have a `stack_size_bonus` field), so citing
cycles/sec *is* citing items/sec for those tiers specifically.
Written as `formulas/inserter_throughput.py`, combined with
`mechanics/trains.json`'s per-tier count into
`relations/wagon_loading_throughput.*` — `inserter`/`transport-belt`
= 12 × 0.86 = **10.32 items/sec**, matching this project's own
founding architecture discussion exactly (see that relation's `.md`).

**Update**: `bulk-inserter`/`stack-inserter`'s *base* (unresearched)
`items_per_cycle` was later resolved via
`wiki.factorio.com/Inserter_capacity_bonus_(research)`'s stated base
grab sizes (regular=1, bulk-inserter=2, stack-inserter=6) — this also
explained why `bulk-inserter` has no `stack_size_bonus` field at all
(its base of 2 is an implicit engine default for `bulk: true`
inserters, not a stored value) and why `stack-inserter`'s
`stack_size_bonus=4` didn't match the wiki's "6" alone (`4` is added
*to* the same implicit base of 2). Both tiers are now in
`mechanics/inserters-throughput.md` and
`relations/wagon_loading_throughput.*` at the unresearched baseline.
What's still unresolved is the *researched* value: `inserter-capacity-bonus-1..7`
add two separate effects (`bulk-inserter-capacity-bonus` summing to
+10, `inserter-stack-size-bonus` summing to +2) whose combination
with the base grab size isn't documented anywhere found — the
dedicated wiki page for this exact topic states the formula isn't
described.

## Consequences

- The wagon-loading-throughput relation is now complete for all 6
  inserter tiers at the unresearched baseline
  (`relations/wagon_loading_throughput.*`) — not the "stays
  incomplete" outcome originally expected when this decision was
  first drafted.
- **Resolved 2026-08-08**: the researched grab-size combination
  formula was found in `factoriocheatsheet.com`'s source
  (community-maintained, wiki-derived) and independently cross-checked
  by summing this project's own already-held
  `datapacks/dump/vanilla/technology/inserter-capacity-bonus-*.json`
  modifiers — both agree exactly at every tech level. See
  `mechanics/inserters-throughput.md`'s "Researched grab size" section
  and `formulas/inserter_capacity_bonus.py`. The wiki's own
  "formula not described" statement stands for the wiki itself; this
  project no longer depends on the wiki for this specific gap.
- Revisiting the *cycles/sec-from-geometry* question (not the
  multiplication) still needs one of: (a) access to a live Factorio
  instance to calibrate a formula the way `inserter-throughput-lib`
  does, since pure kinematics from `rotation_speed`/`extension_speed`
  demonstrably isn't enough on its own, or (b) a direct (non-summarized)
  pull of the wiki's full throughput table for exact-precision citable
  numbers.
- This is the first entry in `decisions/` in this repo — the domain
  didn't exist before this decision needed recording.

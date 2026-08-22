# 0003 — Main bus as an early-game bootstrap; city-block + train-bus as the long-game target

## Status
Accepted

## Context

`layouts/scalable_main_base.md`'s "Design choice" section already
laid out the sourced tension in full: community opinion on
main-bus-vs-city-block is genuinely split. Nilaus and burenning
(mechanical adjacency argument) push toward city-blocks scaling
better; Carl and mmmPI push back (main bus is fine if sized correctly;
city-blocks just relocate the bottleneck to train pathfinding). That
section deliberately stopped short of picking a side for the *project*
— it documented the belt-through-gaps pattern
(`layouts/main_bus_consumer_layout.md`) because it had citable math
ready, not as an endorsement.

The project needed its own stated position, distinct from "what does
the community think" (genuinely split, documented as such) — this
project's own base-building templates have to pick *something* to
build toward as the default recommendation.

## Alternatives considered

**Main bus only, no city-block/train-bus story.**
- Con: simplest to document, but contradicts this project's own
  sourced finding that main-bus is widely reported to scale poorly
  toward megabase size (`layouts/main_bus.md`'s "bus is early/mid-game
  infrastructure" section, DeadMG: *"by the time this becomes a
  serious problem, you should be training ores anyway"*).

**City-blocks + trains from the very start, no main-bus phase at all.**
- Con: matches the long-game target but skips the bootstrap problem —
  early game (before enough steel for rail infrastructure — rails,
  locomotives, and wagons are all steel-heavy,
  `datapacks/dump/vanilla/recipe/rail.json` et al.) needs *some*
  transport pattern in the meantime, and main-bus is the
  well-documented, low-tech-prerequisite option for that window. Also
  contradicted by this project's own citation: Steam Community's
  brian_va frames the prerequisite as construction robots, not "skip
  belts entirely from minute one."

**[Chosen] Main-bus as an explicit early-game bootstrap; city-block +
train-bus as the stated long-game target.**

## Decision

Project owner's stated position (2026-08-09): **city-blocks are the
preferred structural pattern outright**, and **train-bus, not
main-bus, is the target for the long game**. Main-bus is accepted
specifically as an early-game bootstrap — useful only until there's
enough steel to make rail infrastructure practical — not as a
permanent architecture. This matches
`layouts/scalable_main_base.md`'s own already-cited **68Cadillac**
quote (r/factorio thread `gnolui`): *"You use the Main Bus as the
starting point to the City Block base. Once the Mainbus Area starts
outputting enough assemblers, inserters, rails, modules, and all the
various parts needed to set up your City Block you move to City
Block... Main bus is just a stepping stone."*

## Consequences

- `layouts/main_bus_consumer_layout.md` (the belt-through-gaps
  composition) is documented as the bootstrap/early-game pattern, not
  a competing permanent alternative to `layouts/city_block_grid.md`
  (the rail-connected pattern).
- `layouts/scalable_main_base.md` — which concretely instantiates the
  belt-through-gaps pattern for red/green science — should be read as
  the early-game/bootstrap instance specifically, not this project's
  end-state recommendation. It isn't rewritten by this decision (its
  math is still correct and still the citable worked example for that
  stage), just recontextualized.
- ~~No existing layout doc yet shows the actual *transition*~~ —
  resolved by
  [layouts/main_bus_to_city_block_transition.md](../layouts/main_bus_to_city_block_transition.md)
  (2026-08-09): build bootstrap-phase blocks already positioned/sized
  to the target grid, so the transition is an edge-interface swap
  (tap-module → rail station) per block, not an interior rebuild.
- `layouts/scalable_chem_base.md` and `layouts/nuclear_base.md`
  already connect by dedicated point-to-point rail
  (`train-base`, not `train-bus`) — consistent with this decision's
  long-game target, no changes needed there.
- Doesn't resolve `glossary/invented/train-bus.md`'s own open point
  that this project has never actually built a *true* train-bus
  (shared line, multiple stations tapping in) anywhere — every rail
  connection so far is point-to-point `train-base`. This decision sets
  the target; a concrete train-bus layout is still unwritten.

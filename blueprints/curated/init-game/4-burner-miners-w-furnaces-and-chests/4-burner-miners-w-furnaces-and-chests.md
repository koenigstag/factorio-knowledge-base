# 4 Burner Miners with Furnaces and Chests

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 16 entities:
`burner-mining-drill` (4), `stone-furnace` (4), `burner-inserter` (4),
`wooden-chest` (4) — one step up from
[4-burner-miners-w-chests.md](../4-burner-miners-w-chests/4-burner-miners-w-chests.md): each
drill's ore now feeds a furnace (via a burner inserter) instead of
going straight to a chest, with the chest catching the smelted plates.

This is a real instance of the "early transitional automation" idea
noted in `4-burner-miners-w-chests.md`: furnaces placed immediately
after the drills, rather than as their own separate module downstream
— not the "correct at scale" arrangement per
[layouts/smelter_module_ports.md](../../../../layouts/smelter_module_ports.md),
but a deliberate init-game stopgap before a proper smelting module
(like [4x2-stone-furnaces-w-upgrade-spacing.md](../../earlygame/4x2-stone-furnaces-w-upgrade-spacing/4x2-stone-furnaces-w-upgrade-spacing.md))
replaces it.

## Ports: none (author-confirmed, by design)

No import: drills, furnaces, and burner-inserters are all fuelled by
hand (coal placed directly into each fuel slot), not by belt. No
export: the `wooden-chest`s are manual-collection buffers for smelted
plates, not feeding anything downstream — same reasoning as
`4-burner-miners-w-chests.md`, one step later in the chain (plates
instead of raw ore). A `transport-belt` could replace the chests as an
export port in a future revision; not something this blueprint
currently has.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/init-game/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 4
warnings**, all `UnknownKeywordWarning` on `Container` for an
unrecognized `direction` key (same suspected schema-version gap as
`4-burner-miners-w-chests.md`), not an entity/placement problem.
`codec.py`'s own decode succeeds cleanly.

Verified: 2026-08-09

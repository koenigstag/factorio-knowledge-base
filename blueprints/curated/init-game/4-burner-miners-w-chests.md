# 4 Burner Miners with Chests

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 8 entities:
`burner-mining-drill` (4), `wooden-chest` (4) — the most minimal
possible mining tile, drills dumping straight into adjacent chests, no
belts/inserters at all. The very first thing placeable at game start.

## Ports: none (author-confirmed, by design)

No import: the drills are fuelled by hand (coal placed directly into
each drill's fuel slot), not by belt. No export: the `wooden-chest`s
aren't feeding anything downstream — they're manual-collection buffers
the player empties by hand to hand-craft the next tier of bootstrap
items (belts, drills, boilers, inserters), not a production module
with an output.

Author's own noted possibility, not something this blueprint currently
does: a `transport-belt` could replace the chests as an export port
(or sit right after them, buffer-then-belt), as an early *transitional*
step toward automation — smelting furnaces placed immediately after
the drills rather than as their own separate module downstream, which
would be the "correct at scale" arrangement per
[layouts/smelter_module_ports.md](../../../layouts/smelter_module_ports.md).
Recorded as a stated idea for a future revision, not a claim about
what this specific blueprint currently has.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/init-game/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **OK — 0 errors, 4
warnings**, all `UnknownKeywordWarning` on `Container` (the wooden
chests) for an unrecognized `direction` key (same suspected
schema-version gap as the other `direction`-warning entries here), not
an entity/placement problem. `codec.py`'s own decode succeeds cleanly.

Verified: 2026-08-09

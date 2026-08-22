# 4×2 Electrical Furnaces with Tier-2 Belts

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 66 entities:
`fast-transport-belt` (36), `fast-inserter` (16), `electric-furnace`
(8), `small-electric-pole` (6) — the midgame successor to
[4x2-stone-furnaces-w-upgrade-spacing.md](../earlygame/4x2-stone-furnaces-w-upgrade-spacing.md):
same 4×2 furnace layout, upgraded to electric furnaces and tier-2
(fast) belts/inserters throughout.

**Tileable for scaling** (author-confirmed, same pattern as the
stone-furnace version): each copy's export row feeds the next copy's
import row directly.

## Ports

Structured, author-confirmed data:
[4x2-electrical-furnaces-w-tier2-belts.ports.json](4x2-electrical-furnaces-w-tier2-belts.ports.json).
Same "Plate on the inside" pattern and port layout as
[4x2-stone-furnaces-w-upgrade-spacing.md](../earlygame/4x2-stone-furnaces-w-upgrade-spacing.md)
(outer lanes = ore, shared center lane = result, all pass-through
top-to-bottom) — just **no coal lanes**, since `electric-furnace` runs
on electricity rather than burned fuel, so only 3 lanes instead of 5.
See [layouts/smelter_module_ports.md](../../../layouts/smelter_module_ports.md)
for why this arrangement is the recommended pattern generally.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/midgame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse**
(`list index out of range`, an internal draftsman error). `codec.py`'s
own decode succeeds cleanly — same suspected schema-version-gap cause
as the other entries here that fail the same way.

Verified: 2026-08-09

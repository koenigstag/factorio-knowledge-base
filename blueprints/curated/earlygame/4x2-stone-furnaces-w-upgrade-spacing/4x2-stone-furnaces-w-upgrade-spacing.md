# 4×2 Stone Furnaces with Upgrade Spacing

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (generic `"Blueprint"`). 91 entities:
`transport-belt` (55), `inserter` (16), `stone-furnace` (8),
`long-handed-inserter` (8), `small-electric-pole` (4) — a small
stone-furnace smelting block, deliberately spaced (per the filename)
to allow upgrading `stone-furnace` → `steel-furnace`/`electric-furnace`
in place later without needing to rebuild belt/inserter positions.

**Tileable for scaling** (author-confirmed, same pattern as
[4-boilers-w-burner-inserters.md](../4-boilers-w-burner-inserters/4-boilers-w-burner-inserters.md)):
each copy's export row feeds the next copy's import row directly.

## Ports

Structured, author-confirmed data:
[4x2-stone-furnaces-w-upgrade-spacing.ports.json](4x2-stone-furnaces-w-upgrade-spacing.ports.json).
Unlike the boilers module (ports on `x_min`/`x_max`), this one's ports
run top/bottom: 5 parallel pass-through lanes, each an unbroken
11-tile `transport-belt` run (checked directly) from `y=-5.5` (import
edge) to `y=4.5` (export edge), all facing South. Furnaces sit in two
rows, each row between an outer ore lane and the shared central lane;
ore comes in on the outside of each row, coal on the inside, and both
rows' output lands on one shared central result lane rather than each
row having its own.

`classify_edge_ports` (`blueprints/codec.py`) found the 10 candidate
tiles correctly (5 import, 5 export) from direction alone, but — per
`blueprints/README.md`'s "Import/export port heuristic" rule — neither
which resource each lane carries, nor the ore/coal/result role split,
came from the geometry; both are author-confirmed.

This exact ore/coal-outside, result-inside arrangement is a named,
sourced community best practice, not just this module's own choice —
see [layouts/smelter_module_ports.md](../../../../layouts/smelter_module_ports.md)
("Plate on the inside") for why it's the recommended pattern over the
alternative, and how this blueprint serves as this project's own
confirmed real-world example of it.

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse**
(`list index out of range`, an internal draftsman error). `codec.py`'s
own decode succeeds cleanly — same suspected schema-version-gap cause
as the other entries here that fail the same way, not evidence of a
corrupt blueprint.

Verified: 2026-08-09

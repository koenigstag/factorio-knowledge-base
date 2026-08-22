# 4 Boilers with Burner Inserters

Personal blueprint, not a third-party design — the project owner's own
build.

No blueprint-internal label set (decodes to the generic `"Blueprint"`).
37 entities: `transport-belt` (13), `steam-engine` (8), `boiler` (4),
`small-electric-pole` (5), `burner-inserter` (4), `pipe` (3) — a basic
early-game power block, 4 boilers feeding 8 steam engines (the
standard 1:2 ratio, see
[relations/steam_power_chain.md](../../../../relations/steam_power_chain.md)),
fuelled by burner inserters rather than a belt-fed/electric setup.

**Tileable for scaling** (author-confirmed): meant to be placed
edge-to-edge with identical copies of itself, export butted directly
against the next copy's import, so the coal lane continues unbroken
across an arbitrary run of these modules rather than needing a
separate distribution belt alongside them.

## Ports

Structured, author-confirmed data:
[4-boilers-w-burner-inserters.ports.json](4-boilers-w-burner-inserters.ports.json).
Not two separate ports for different resources — both ends belong to
the same single, unbroken `transport-belt` lane at `y=6.5` (13 tiles,
`x=5.5` down to `x=-6.5`, all facing West): coal enters on the right,
the 4 `burner-inserter`s along the way pull from it to feed the
boilers, and whatever's left continues out the left edge toward the
next tiled copy. Confirmed by the author, not assumed from
`blueprints/codec.py`'s `classify_edge_ports` output alone, per
`blueprints/README.md`'s "Import/export port heuristic" rule
(candidates require confirmation, not just a matching direction).

## Provenance

- Author: project owner (self-authored).
- Filed under `blueprints/curated/earlygame/` — game-stage folders
  organize the project owner's personal collection; third-party
  entries stay flat at `curated/`'s root.
- Added to the repository: 2026-08-09.

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse**
(`list index out of range`, an internal draftsman error, not a
reported entity/placement problem). `blueprints/codec.py`'s own decode
succeeds cleanly and reproduces the entity counts above without issue
— treated as a draftsman-side limitation for this blueprint
specifically (schema-version gap, same suspected cause as the
`direction`-key warnings on other entries here), not evidence the
blueprint itself is corrupt.

Verified: 2026-08-09

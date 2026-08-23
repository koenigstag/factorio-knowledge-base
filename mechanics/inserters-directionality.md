# Inserter directionality (axis-locked pickup/drop)

An inserter interacts along a single fixed axis determined by its
placement direction: it picks items up from the tile/entity in the
direction it's facing (its `direction` field) and drops them on the
tile/entity on the **opposite** side. It cannot pick up from or drop
to a tile that is perpendicular (to either side) of that axis —
rotating an inserter changes which axis it uses, but at any given
moment it only ever has one pickup position and one drop position,
both on that same line, on opposite ends of it.

`direction` points toward the pickup side; drop is on the opposite
side. Confirmed from `datapacks/dump/vanilla/inserter/inserter.json`:
`"pickup_position": [0, -1]`, `"insert_position": [0, 1.2]` — at
`direction=0` (North, unrotated), pickup is offset north (negative Y)
and drop is offset south (positive Y), so pickup sits on the facing
side. Same pattern for every inserter tier (`fast-inserter`,
`bulk-inserter`, `stack-inserter`, `burner-inserter`: pickup
`[0,-1]`/drop `[0,1.2]`; `long-handed-inserter`: pickup `[0,-2]`/drop
`[0,2.2]`, same sides, double reach).

No `data.raw` field states the axis-lock behavior itself as a rule
directly — it falls out of how the engine applies
`pickup_position`/`insert_position` (vectors relative to the
inserter's current facing) combined with placement being restricted
to the four cardinal directions (see below).

Practical consequence for layout design: an inserter servicing a belt,
chest, or machine must be oriented so both its source and destination
sit on that front-back line — you cannot "reach around a corner" with
a single inserter. Getting an item to turn a corner requires either
two inserters (one per leg) or routing the item via a belt/pipe that
itself turns.

## Placement is cardinal-only

Inserters can only be placed facing the four cardinal directions
(`direction` 0/4/8/12 — North/East/South/West); the building-placement
logic itself enforces this. There's no `data.raw` field to check,
since it's pure engine behavior, same as the axis-lock rule above.

A brief exception: in Factorio 2.0.47–2.0.53, a bug let players
force-build over an existing inserter using a blueprint whose entity
had a non-cardinal `direction` (e.g. `6` = southeast), producing a
genuinely functional diagonal inserter. Fixed in 2.0.54 (developer
boskid) — a blueprint with a non-cardinal inserter `direction` now
imports as a straight (cardinal) inserter instead of a diagonal one.

A non-cardinal `direction` on an `inserter`/`*-inserter` entity in a
blueprint is therefore either a leftover from a pre-2.0.54 exploit
placement, or — far more commonly — an unrescaled pre-2.0 value (see
below). Check the blueprint's `version` field before assuming either
cause.

## Pre-2.0 blueprints use a different `direction` scale

Factorio changed the `direction` field's numeric scale at 2.0.0 (FFF
#377): pre-2.0, an 8-value enum with cardinals spaced 2 apart
(North=0, East=2, South=4, West=6); 2.0+, a 16-value enum with
cardinals spaced 4 apart (North=0, East=4, South=8, West=12) — same
four compass directions, just double the raw integer. This applies to
every directional entity, not just inserters.

`codec.py` doesn't rescale `direction` on decode (it's a faithful,
format-preserving transcode), so any caller computing geometry from
`direction` must rescale pre-2.0 values itself first, using the
blueprint's own `version` field (packed uint64:
`main<<48 | major<<32 | minor<<16 | developer`) to decide whether to
apply it.

`build_vectors.py`'s `normalize_pre_2_0_directions()` (mirrored in
`pages/index.html` as `normalizePre20Directions()`) does this
automatically: doubles every entity's `direction` in place when the
blueprint's `version` is pre-2.0, before any geometry is computed.

Source: `datapacks/dump/vanilla/inserter/inserter.json` (and the
other inserter-tier files, same pattern) — `pickup_position`/
`insert_position` fields.
Verified: 2026-08-22

Cardinal-only-placement/diagonal-inserter-bug source:
https://forums.factorio.com/viewtopic.php?p=673349 ("[2.0.47]
Inserters can face diagonally" bug report, developer boskid confirming
the fix landed in 2.0.54).
Verified: 2026-08-23

Pre-2.0 direction-scale source: Friday Facts #377. Cross-checked
against `github.com/FactoryGameFan/factorio-blueprint-editor`'s
`packages/editor/src/core/Blueprint.ts`, which applies the same
`direction * 2` rescale on import for pre-2.0 blueprints.
Verified: 2026-08-23

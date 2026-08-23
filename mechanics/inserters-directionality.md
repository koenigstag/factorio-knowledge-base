# Inserter directionality (axis-locked pickup/drop)

An inserter interacts along a single fixed axis determined by its
placement direction: it picks items up from the tile/entity in the
direction it's facing (its `direction` field) and drops them on the
tile/entity on the **opposite** side. It cannot pick up from or drop
to a tile that is perpendicular (to either side) of that axis —
rotating an inserter changes which axis it uses, but at any given
moment it only ever has one pickup position and one drop position,
both on that same line, on opposite ends of it.

**Correction (2026-08-22)**: this file previously stated the reverse
— pickup=behind/drop=in front of the `direction` value — based on a
paraphrase of the wiki's "move items from behind and place them in
front of them." That reading is backwards for how the `direction`
field itself maps to pickup/drop. Confirmed directly from this
project's own dump,
`datapacks/dump/vanilla/inserter/inserter.json`:
`"pickup_position": [0, -1]`, `"insert_position": [0, 1.2]` — at
`direction=0` (North, unrotated), pickup is offset **north**
(negative Y) and drop (`insert_position`) is offset **south**
(positive Y, and slightly longer reach: 1.2 vs 1 tile). Since negative
Y is north in Factorio's map coordinates, this means: **`direction`
points toward the pickup side; drop is on the opposite side** — not
the other way around. Same pattern holds for every inserter tier
checked (`fast-inserter`, `bulk-inserter`, `stack-inserter`,
`burner-inserter`: pickup `[0,-1]`/drop `[0,1.2]`;
`long-handed-inserter`: pickup `[0,-2]`/drop `[0,2.2]`, same sides,
just double reach).

This mistake wasn't caught by re-deriving from primitives — it was
caught twice, empirically, on real blueprints: the port-flow analysis
for `blueprints/curated/earlygame/iron-gear-tileable/iron-gear-tileable.md` came out
backwards on the first pass and had to be corrected by the project
owner, and a second, independent blueprint (a third-party "Basic
steel smelting" find) produced the same wrong-direction reading again
before being corrected a second time — at which point checking this
file's own cited source directly (not just its prose) surfaced the
error. Two independent corrections against the same standing "hard
rule 6" (consult `mechanics/` before reasoning) is itself the lesson:
having a mechanics file isn't enough if the file is wrong — this one
was checked, applied, and still gave the wrong answer twice because
nobody had re-verified its source against primitives already sitting
in this project's own `datapacks/`.

No `data.raw` field states the axis-lock behavior itself as a rule
directly — it falls out of how the engine applies
`pickup_position`/`insert_position` (vectors relative to the
inserter's current facing) combined with placement being restricted
to the four cardinal directions (see below). There's nothing to
extract from a dump for *that* part; the rule itself is what's worth
recording. The pickup/drop-side mapping, though, **is** directly
checkable against the dump, and should be checked there first, not
assumed from prose.

## Placement is cardinal-only — diagonal inserters are a patched bug, not a feature

Inserters can only be placed facing the four cardinal directions
(`direction` 0/4/8/12 — North/East/South/West); the building-placement
logic itself enforces this, there's no `data.raw` field to check since
it's pure engine behavior, same as the axis-lock rule above.

A real exception existed briefly and is worth recording because a
blueprint can still carry evidence of it: in Factorio 2.0.47–2.0.53, a
bug let players force-build over an existing inserter using a
blueprint whose entity had a non-cardinal `direction` (e.g. `6` =
southeast), producing a genuinely functional diagonal inserter — not a
visual glitch, it actually picked up and dropped diagonally. Reported
on the official bug forum, confirmed and fixed by developer boskid in
2.0.54: re-testing the same bug-report blueprint in 2.0.54 imports it
as a straight (cardinal) inserter instead. So as of current versions,
pasting a blueprint with `direction: 2` or `direction: 6` on an
inserter does **not** produce a diagonal inserter — the game silently
snaps it to a cardinal direction on import.

Practical upshot for this project's tooling: a blueprint can still
contain a non-cardinal `direction` value on an `inserter`/
`*-inserter` entity — either exported from an old save that still has
a bugged diagonal inserter placed before 2.0.54 (those keep working
once already placed, per the same bug thread), or a blueprint string
someone hand-edited attempting the now-dead exploit. Either way, that
value does not describe a valid diagonal placement in current
Factorio — `build_vectors.py`/the visualizer should treat it as an
anomaly to flag, not a direction to compute pickup/insert geometry
for (see the linked forum thread for the primary source before
assuming any specific snap-to-cardinal rule if this needs handling
precisely).

Practical consequence for layout design: an inserter servicing a belt,
chest, or machine must be oriented so both its source and destination
sit on that front-back line — you cannot "reach around a corner" with
a single inserter. Getting an item to turn a corner requires either
two inserters (one per leg) or routing the item via a belt/pipe that
itself turns.

Source: `datapacks/dump/vanilla/inserter/inserter.json` (and the
other inserter-tier files, same pattern) — `pickup_position`/
`insert_position` fields, checked directly rather than inferred from
wiki prose. Cross-referenced against
https://wiki.factorio.com/Inserters ("When placed, they have a fixed
direction. They can move items from behind and place them in front of
them.") — the wiki's "front"/"behind" phrasing is evidently not
describing the `direction` field the way this file first assumed; the
dump values are the authoritative, checkable source and take
precedence.
Verified: 2026-08-22

Cardinal-only-placement/diagonal-inserter-bug section source:
https://forums.factorio.com/viewtopic.php?p=673349 ("[2.0.47]
Inserters can face diagonally" bug report, developer boskid confirming
the fix landed in 2.0.54, and a commenter confirming the same
bug-report blueprint imports as a straight inserter once patched).
Prompted by a real blueprint pasted into this project with `inserter`/
`long-handed-inserter` entities carrying `direction: 2`/`direction: 6`
and no other entity type in that same blueprint using non-cardinal
values — initially misread as an intentional 2.0 diagonal-placement
feature before being corrected; this is the verified account.
Verified: 2026-08-23

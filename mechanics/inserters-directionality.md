# Inserter directionality (axis-locked pickup/drop)

An inserter interacts along a single fixed axis determined by its
placement direction: it picks items up from the tile/entity directly
**behind** it and drops them on the tile/entity directly **in front**
of it. It cannot pick up from or drop to a tile that is perpendicular
(to either side) of that axis — rotating an inserter changes which
axis it uses, but at any given moment it only ever has one pickup
position and one drop position, both on that same line.

No `data.raw` field states this as a rule directly — it falls out of
how the engine applies `pickup_position`/`drop_position` (vectors
relative to the inserter's current facing) combined with placement
being restricted to the four cardinal directions. There's nothing to
extract from a dump; the rule itself is what's worth recording.

Practical consequence for layout design: an inserter servicing a belt,
chest, or machine must be oriented so both its source and destination
sit on that front-back line — you cannot "reach around a corner" with
a single inserter. Getting an item to turn a corner requires either
two inserters (one per leg) or routing the item via a belt/pipe that
itself turns.

Source: https://wiki.factorio.com/Inserters — "When placed, they have
a fixed direction. They can move items from behind and place them in
front of them."
Verified: 2026-08-08

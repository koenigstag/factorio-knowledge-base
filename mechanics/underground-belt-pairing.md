# Underground belt entrance/exit pairing rules

Two rules govern which underground-belt entrance connects to which
exit — both matter for reconstructing flow from blueprint entity data
alone, since the blueprint JSON stores no explicit link between a
paired entrance and exit; the pairing has to be re-derived from
position + direction + tier + `max_distance`
(`relations/underground_belt_crossing_gap.md`).

## Same-tier only — different tiers pass through each other

An underground-belt entrance only pairs with an exit of the **same
tier** (`underground-belt`, `fast-underground-belt`,
`express-underground-belt`, `turbo-underground-belt` never cross-pair
with each other). Multiple tiers can be laid along the exact same line
of tiles independently — this is the "braiding" the wiki describes:
each tier's items stay in their own tier's belt, tiers placed along a
shared line don't interfere with or block each other at all, as if
each tier's tunnel were on its own separate layer.

## Nearest-match, no skip-over

Within its own tier, an entrance always connects to the **closest**
compatible exit within `max_distance` — it cannot skip past a nearer
same-tier exit to reach a farther one, even if the nearer one "should"
belong to a different logical belt run. Placing a same-tier entrance
in between an existing entrance/exit pair breaks the original pair and
reconnects to the new, closer one instead (this is also why
mid-game blueprint edits or bot-placed belts can unexpectedly
"steal" a connection from an existing underground-belt pair).

## Dead-end entrances (no paired exit)

An entrance with **no compatible same-tier exit within range** simply
has no output — it acts as a sink/buffer, not a through-connection.
This is a deliberate, common technique: terminating a belt into an
unpaired underground-belt entrance instead of letting it run off the
end, specifically to avoid an unwanted direct hand-off onto a
perpendicular belt or open space at the belt's end.

## Practical consequence for reconstructing flow from blueprint data

When pairing underground-belt entities found in a blueprint's entity
list (e.g. for `blueprints/codec.py`'s flow-graph construction):
group candidates by tier (`name`) first, then within each tier match
each `type: "input"` entity to the nearest `type: "output"` entity in
its facing direction within that tier's `max_distance` — never across
tiers, and never to a farther exit if a nearer one of the same tier
exists. An input with no such match is a dead end, not a parsing
error — record it as a sink, don't force-pair it to the nearest
candidate regardless of tier or distance.

Source: https://wiki.factorio.com/Belt_transport_system — "Different
types of underground belts can be braided together along the same
line of tiles, with items staying in their respective belt types."
(same-tier-only pairing). Nearest-match/no-skip-over behavior
corroborated via Factorio Forums discussion of automatic underground
belt placement (e.g. the "[2.0.21] Automatic underground belt
placement connects to and interrupts other transport lines" report
thread) — community-confirmed engine behavior, not an official wiki
quote for this specific sub-claim; lower confidence tier than the
braiding fact above, flagged accordingly.
Verified: 2026-08-22

# Cliffs block direct surface construction across their own tile

A cliff has no real elevation — it's a visual trick, the terrain
underneath is flat — but it still blocks placement of rails, belts,
and most buildings directly on/through the cliff tile itself. Other
entities can be built *around* a cliff normally, and underground
belts/pipes can tunnel *underneath* one without needing it removed,
but nothing can be placed *on* the cliff tile while it exists.

Removing a cliff requires `cliff-explosives` (an item used on the
cliff itself) or a sufficiently large explosion (a nuclear detonation
also clears cliffs in its blast radius). A removed cliff drops no
resources. Since 0.17, construction robots can also remove a
deconstruction-planner-marked cliff, provided cliff explosives are
available in the logistic network.

Practical consequence for layout design: a rail or main-bus route that
would otherwise cross a cliff either has to route around it or budget
cliff-explosives into the build plan — it isn't a routing obstacle
that resolves itself the way water can be piped/bridged.

No `data.raw` field encodes the placement-blocking behavior itself —
`cliff` is a `data.raw` prototype (footprint, explosive item
requirement), but "why can't I build here" is engine collision logic,
not a stored rule.

Source: https://wiki.factorio.com/Cliff
Verified: 2026-08-08

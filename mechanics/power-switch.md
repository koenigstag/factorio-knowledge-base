# Power switch merges two electric networks into one

Closing a `power-switch` (turning it on) creates a conductive link
between the two copper-wire networks attached to its two sides,
merging them into a single electric network for power-balancing
purposes — production and consumption on both former networks are now
pooled together. Opening it (turning it off) splits them back into two
independent networks.

Caveat from the wiki: the switch has no effect if another connection
already exists between the two sides — e.g. if the two networks are
also joined by an ordinary pole-to-pole wire elsewhere, toggling the
switch doesn't isolate them, since that other path still merges them
regardless of the switch's state.

Practical consequence for layout design: a power switch is how two
otherwise-separate power grids (e.g. a main base grid and a
remote/outpost grid) get selectively pooled or isolated — commonly
used to let an accumulator-backed grid disconnect from the main grid,
or to keep a segment isolatable for maintenance without cutting power
elsewhere.

No `data.raw` field encodes network-merging — it's electric-network
simulation behavior, not a stored per-prototype value (the switch
prototype only stores things like its footprint/graphics).

Source: https://wiki.factorio.com/Power_switch
Verified: 2026-08-08

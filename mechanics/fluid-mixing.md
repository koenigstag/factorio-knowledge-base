# Pipes never mix two fluid types

A single connected pipe network can hold exactly one fluid type at a
time. The game enforces this at placement time, not by silently
blending: attempting to place a pipe that would connect two networks
already carrying different fluids fails outright — the pipe is not
placed.

Practical consequence for layout design: a pipe network's fluid
identity is fixed by whatever first fills it, and merging two
different-fluid systems isn't something that can be corrected after
the fact by disconnecting — the wrong fluid already in a segment has
to be manually flushed (via the pipe's trash button, which deletes it)
before that segment can carry a different fluid. This is why fluid
buses need dedicated, never-crossing pipe runs per fluid type, unlike
a belt bus lane which can be repurposed by just changing what's placed
on it.

No `data.raw` field encodes this — it's fluidbox simulation behavior,
not a stored per-prototype value.

Source: https://wiki.factorio.com/Pipe
Verified: 2026-08-08

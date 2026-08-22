# Splitter priority & filter routing

Complements `glossary/canonical/lane-balancer.md` (which covers lane
*preservation*) — this covers how a splitter decides which **output**
gets an item, a separate axis of behavior.

## No priority set (default)

Items split evenly between the two outputs. If one output backs up
(its belt is full) so the split can't stay even, the splitter routes
everything to the other, non-backed-up output instead of stalling.

## Output priority set

The splitter tries to send **all** incoming items to the specified
output first, only spilling over to the other output once the
specified one is completely full (backed up).

## Input priority set

The splitter tries to draw **all** its input from the specified input
side first, only pulling from the other input side once a gap opens up
on the prioritized input belt.

## Filter set

Restricts one output to a single specified item type: every item of
that type is routed to that output, and everything else goes to the
other output. Filter and input-priority settings operate
independently of each other — both can be active on the same splitter
at once.

None of this routing logic is a `data.raw` field — a splitter's
priority/filter are per-instance blueprint/entity state set by the
player at build time, not prototype data, and the routing algorithm
itself (how ties/backpressure resolve) is pure engine behavior.

Source: https://wiki.factorio.com/Belt_transport_system
Verified: 2026-08-08

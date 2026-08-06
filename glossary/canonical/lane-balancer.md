# lane balancer

A belt has two lanes (left/right); a plain `splitter` **preserves**
lanes rather than mixing them — an item on the right lane stays on
the right lane through the splitter, never crossing to the left. If
items get onto a belt unevenly (e.g. from how inserters place them,
or from naively merging several sources), the two lanes can end up
unbalanced — one nearly full, the other nearly empty — so the belt
runs below its rated throughput even though it isn't "full" by simple
item count. A lane balancer is a specific splitter arrangement built
to redistribute items evenly across both lanes, restoring the belt's
full rated throughput.

Direct wiki quotes:
> "Splitters preserve the lanes of the items, by moving through the
> splitter an item on the right lane will not be moved to the left
> lane, and vice versa."
> "In order to maintain throughput, balancing the lanes may be
> necessary."

This project's [city-block gap](../invented/city-block-gap.md) already
referenced "balancers" needing space in the gap zone.

Source: https://wiki.factorio.com/Belt_transport_system
Verified: 2026-08-06

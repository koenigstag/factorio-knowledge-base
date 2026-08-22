# belt balancer

A splitter/belt arrangement that distributes items evenly across
multiple *separate belts* (e.g. 4 ore-patch output belts, or several
main-bus lanes of the same item) — a different scope from
[lane balancer](lane-balancer.md), which fixes left/right lane
imbalance *within* a single already-existing belt. The two are related
(a belt balancer is typically built from the same splitter primitives)
but solve different problems and aren't interchangeable terms.

Official wiki page (`Balancer_mechanics`), not just community usage.
Formal properties a balancer can have, in increasing strength:

- **Input balanced** — takes evenly from all input belts/lanes.
- **Output balanced** — distributes evenly to all output belts/lanes.
- **Output balanced under backpressure** — stays evenly distributed
  even when one or more output belts are blocked/backed up, not just
  under free-flowing conditions.
- **Throughput unlimited** — 100% throughput at full load, *and* any
  arbitrary subset of input belts can feed any arbitrary subset of
  output belts without an internal bottleneck reducing total flow.
  Failing this (but still balancing correctly under normal conditions)
  makes a design "throughput limited."

A design can be balanced without being throughput-unlimited, or
throughput-unlimited without handling backpressure — these are
independent axes, not a single pass/fail rating, per the wiki's own
framing (summarized, not verbatim-quoted — re-pull the page directly
before citing an exact sentence).

Practical use cited directly on the wiki page: ore-patch output belts,
and the main-bus split-off point (`layouts/main_bus.md`'s tap-off
section) — a plain splitter is the default there, with a full belt
balancer reserved for when lane/belt imbalance is actually measured,
not applied preemptively (see `mechanics/splitter-priority.md`).

See `relations/balancer_splitter_count.md` for the derivable
power-of-two splitter-count formula.

Source: https://wiki.factorio.com/Balancer_mechanics
Verified: 2026-08-08

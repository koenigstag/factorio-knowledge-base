# Belt balancer splitter count (power-of-two, throughput-unlimited)

How many splitters a throughput-unlimited N→N belt balancer needs
(see `glossary/canonical/belt-balancer.md` for what "throughput
unlimited" means), for N a power of two.

Formula: `formulas/balancer_splitter_count.py:power_of_two_balancer_splitter_count`
(`n × log2(n) − n/2`) — cited directly from the wiki
(`wiki.factorio.com/Balancer_mechanics`, credited there to Beneš
network topology), not independently re-derived from first principles
by this project. Only valid for N a power of two; the wiki doesn't
state a general formula for non-power-of-two N, and this project
doesn't have one either.

## power_of_two_balancer_splitter_count

| N (belts) | splitters |
|---|---|
| 2 | 1 |
| 4 | 6 |
| 8 | 20 |
| 16 | 56 |
| 32 | 144 |

This is splitter *count* only — not a layout/footprint (no tile
dimensions are implied), and not a claim that every arrangement using
this many splitters is automatically balanced; the formula gives the
minimum count a correctly-designed Beneš-topology balancer needs, not
a guarantee for an arbitrary splitter graph of that size.

Verified: 2026-08-08

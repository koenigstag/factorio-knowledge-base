# gap-chunk (gap zone)

Empty space between two neighboring city-block modules along the main
bus, reserved for: (1) tap-in/tap-out infrastructure, (2) `lane
balancer`s (see `glossary/canonical/lane-balancer.md`), (3) an
optional rail siding.

Width: not finalized. An initial 2-3 chunk estimate was proposed but
not yet re-derived as a formula — see open questions below.

**Open questions (unresolved):**
- Exact tile budget per sub-purpose (belts/pipes vs balancer vs rail
  siding) is not derived from a formula yet.
- Whether a rail export siding needs a dedicated additional gap or
  reuses the standard tap gap is unresolved.

Coined during initial architecture discussion (not yet backed by a
written decision record in this repo). See `layouts/city_block_grid.md`
for how this composes with `city-block`/`main-bus`/`export-block`.

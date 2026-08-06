# city-block gap (gap zone)

Empty space between two neighboring city-block modules along the main
bus, reserved for: (1) tap-in/tap-out infrastructure, (2) `lane
balancer`s (see [lane balancer](../canonical/lane-balancer.md)), (3)
an optional rail siding. Named for what it separates, not for a fixed
unit — width is expressed in chunks (see below) but isn't itself one.

Width: 1-3 chunks by practical convention, not a `formulas/`-derived
figure. 1 chunk is the most common case, 2 chunks less common. 3
chunks was given as an example of a fuller case: 1 chunk export
storage + 1 chunk single-track railway + 1 chunk for the next block's
import belts.

**Open questions (unresolved):**
- The 1/2/3-chunk figures above are practical/community convention,
  stated by the project owner as working knowledge — not independently
  sourced to a specific publication, and not derived from primitives
  the way `relations/` entries are. A formal derivation would still
  need to check them against real component sizes, e.g.
  [constraints/rails.json](../../constraints/rails.json)'s
  `curve_radius_tiles` for the railway chunk specifically.
- Whether a rail export siding needs a dedicated additional gap or
  reuses the standard tap gap is unresolved.

Coined during initial architecture discussion (not yet backed by a
written decision record in this repo). See
[layouts/city_block_grid.md](../../layouts/city_block_grid.md) for how
this composes with `city-block`/`main-bus`/`export-block`.

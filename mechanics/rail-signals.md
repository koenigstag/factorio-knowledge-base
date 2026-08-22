# Rail signal blocks & chain-signal look-ahead

## Rail signal: red/yellow/green is a block-occupancy state, not a per-signal setting

A `rail-signal` divides connected track into **blocks** — a block spans
all rails connected between signals, regardless of whether a train can
actually travel between all of them. A signal's color is derived
entirely from its monitored block's occupancy, never set directly:

- **Green** — the monitored block is empty.
- **Yellow** — a train has already been authorized into the block (the
  block is reserved), so this signal and every other entrance signal
  to that same block turn red for everyone else.
- **Red** — the monitored block is occupied by a train, or the
  situation above (another entrance signal to it is yellow).

A locomotive always stops before a red signal. This is why two trains
can never physically collide on signaled track that has no gaps: the
block a train currently occupies is red on every entrance, by
construction.

## Chain signal: looks one block further than its own

A `rail-chain-signal` doesn't just check whether its own block is
clear — it also checks the state of the **exit signal of the next
block down the line**. If that further-out exit signal would stop the
train, the chain signal itself turns red and stops the train too, even
though the chain signal's own block is empty.

Practical consequence: a chain signal prevents a train from entering
an intersection/junction it wouldn't be able to fully clear, which is
why intersections and junctions are signaled with chain signals on the
approach and regular signals on the exit — a plain rail signal has no
such look-ahead and would let a train enter a shared junction block
even if it's about to be stuck there blocking cross traffic.

Neither rule has a `data.raw` representation — signal *placement* and
*type* (`rail-signal` vs `rail-chain-signal`) are entities, but the
block-occupancy/look-ahead logic that decides red/yellow/green is pure
engine simulation, not a stored value.

Source: https://wiki.factorio.com/Rail_signal,
https://wiki.factorio.com/Rail_chain_signal
Verified: 2026-08-08

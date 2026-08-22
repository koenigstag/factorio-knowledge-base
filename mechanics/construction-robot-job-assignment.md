# Construction robot job assignment isn't nearest-job-first

Construction jobs (blueprint ghosts, deconstruction orders) are
**not** dispatched in distance order from a roboport or in any
spatially-sorted order at all — this is a common misconception the
in-game behavior actively contradicts.

## The actual algorithm (community-reverse-engineered, not an official Wube statement)

Per a detailed, consistent explanation from forum user `mrvn`, given
independently in two separate threads:

> "The game has a list of ghost entities. Every tick it looks at
> **one** ghost, determines the logistic network the ghost is in,
> finds an item for the entity, finds the closest idle construction
> bot and if both work out it tasks the bot to do the work."

> "They have a single big list of ghost entities and deconstruction
> jobs. Every tick one item in the list is looked at."

So the loop is: pick the next job off one shared list (list order
itself isn't distance-sorted — nothing found confirms whether it's
insertion order, hash order, or something else, flagged as an open
question below), check whether the required item is available in that
ghost's logistic network, and if so assign the **closest currently
idle** bot to it. "Closest idle bot for this one job," not "closest
job for this network's bots."

## Why this produces the near-random, far-before-near behavior observed in play

Two compounding effects:
- **Job order isn't spatial.** Which ghost gets checked on a given
  tick has nothing to do with how close it is to the roboport network
  center or to any particular bot — a far ghost can simply come up in
  the list before a near one.
- **No reassignment once dispatched.** A bot already tasked with a
  distant job keeps that job even if a closer bot becomes idle a tick
  later — the game never re-evaluates "would swapping these two bots'
  jobs be faster." So once a distant bot gets picked (because it
  happened to be the closest *idle* one at that specific tick), it
  commits to the long flight even while nearer jobs sit unclaimed
  waiting for their own turn in the list.

Together these mean build order is effectively decoupled from spatial
layout — matches this project's own observation that bots "build far
away while close jobs are still undone," not a bug or randomness in
the RNG sense, but a consequence of a per-job (not per-network)
greedy-nearest-bot assignment with no global optimization pass.
Community sources attribute the design to keeping the check cheap
(one list-item scan per tick) rather than sorting or re-optimizing the
whole job set, which would cost more UPS at scale.

## Practical consequence / mitigation

Smaller, more segmented logistic networks reduce the effect — fewer
distant idle bots exist to wrongly out-compete for a nearby job in the
first place. This connects directly to
`mechanics/roboport-network-connection.md`: merging many roboports
into one giant network (which that file's border-touching rule makes
easy to do unintentionally) is exactly what makes this assignment
quirk more visible, since the pool of "idle bots that could be
anywhere in the network" grows with network size.

## Confidence & open questions

- Source tier: community forum explanation (`mrvn`, consistent across
  two threads), not an official Wube developer statement or a wiki
  page — lower confidence than this project's usual wiki-sourced
  facts, flagged the same way `max_inserters_per_wagon_long_handed_double_row`
  is in `mechanics/trains.md`.
- **Open**: the exact ordering of the shared job list itself (why one
  ghost is "next" before another) isn't confirmed anywhere found this
  session.
- Related, wiki-confirmed (`Construction_robot`, version history
  2.0.7): construction robots can now be assigned multiple queued
  tasks instead of only receiving a new one after finishing the
  current one, and they "attempt to always charge at a roboport closer
  to their final destination" — both plausibly interact with the
  effect above but aren't confirmed to change the core one-job-per-tick
  assignment loop itself.

Sources: https://forums.factorio.com/viewtopic.php?t=103317,
https://forums.factorio.com/viewtopic.php?t=87539,
https://wiki.factorio.com/Construction_robot
Verified: 2026-08-08

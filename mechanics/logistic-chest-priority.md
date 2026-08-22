# Logistic chest roles and pickup priority

The 5 logistic-chest variants are already in
`datapacks/dump/vanilla/logistic-container/*.json`, distinguished by
their `logistic_mode` field (`active-provider`, `buffer`,
`passive-provider`, `requester`, `storage`) — but what each mode does,
and the order logistic robots pick between them, is engine behavior
with no further `data.raw` representation.

## What each mode does

- **`active-provider`** (active provider chest) — actively pushes its
  stored items into the network; the highest-priority pickup source.
- **`passive-provider`** (passive provider chest) — makes its stored
  items available to the network, but isn't emptied proactively; the
  lowest-priority pickup source of the four "provides items" modes.
- **`storage`** (storage chest) — network-wide overflow: holds items
  "currently not requested" anywhere else. Empties itself into
  requester/buffer demand like a provider, but is also where
  logistic robots dump surplus when idle (see below).
- **`buffer`** (buffer chest) — dual-role: acts as a requester chest
  for filling, and as a passive-provider-like source for others, but
  only once regular requester-chest demand is already satisfied (see
  below) — an "on-demand reserve," not a first-choice source.
- **`requester`** (requester chest) — pure sink: filled by logistic
  robots up to its configured request amount, never a pickup source
  for other requesters.

## Pickup priority order (sourced, not derived)

> "Logistic robots will pick up items in the following priority:
> active provider chests > storage chests, buffer chests > passive
> provider chests"

Storage and buffer chests are checked at the same priority tier,
below active providers and above passive providers.

## Storage chest fill order (which specific storage chest gets an item)

When multiple storage chests could receive the same item, robots
prefer, in order:
1. A storage chest with a matching logistics filter that already
   contains that item.
2. An empty storage chest with a matching filter.
3. An unfiltered storage chest that already contains that item.
4. An empty, unfiltered storage chest.
5. An unfiltered storage chest already holding a *different* item
   (last resort).

Also: logistic robots start moving items from active provider chests
into storage chests specifically when they have no other task
available — storage absorption is a fallback behavior, not a
standing priority.

## Buffer chest: gated behind requester demand, and not chained to other buffers

Two extra rules apply only to buffer chests, beyond the shared
priority order above:
- A buffer chest's contents are only offered up once **all** requester
  chests requesting that item are already satisfied — buffer chests
  are a reserve tapped after standing demand, not a competing source.
- A requester chest only pulls from buffer chests if its own "Request
  from buffer chests" option is explicitly enabled — it's opt-in per
  requester, not automatic.
- Buffer chests never fulfill other buffer chests' requests, even
  with that option on — the reserve doesn't refill itself from another
  reserve.

Source: https://wiki.factorio.com/Logistic_network,
https://wiki.factorio.com/Storage_chest,
https://wiki.factorio.com/Buffer_chest
Verified: 2026-08-08

# Inserter throughput (cited, not derived)

See `decisions/0001-inserter-throughput-not-derived.md` for why this
is cited from the wiki instead of computed from
`datapacks/dump/vanilla/inserter/*.json`'s `rotation_speed`/
`extension_speed` the way `formulas/production_rate.py` handles
recipes.

## Chest-to-chest cycles/sec (clean baseline case)

The wiki states chest-to-chest transfer moves a full hand's worth of
items in a single tick, so nearly all cycle time is the swing there
and back — the cleanest, least setup-dependent throughput number the
wiki publishes. Approximate cycles/sec by tier (Normal quality):
burner ≈0.79, regular ≈0.86, long-handed ≈1.25, fast/bulk/stack ≈2.5.

**Not independently re-verified to exact precision** — pulled via a
summarized fetch of wiki.factorio.com/Inserters#Inserter_Throughput.
Treat as directionally correct, not exact — before using a precise
figure for anything sensitive, re-pull the raw table directly.

## items/sec = cycles/sec × items per cycle (`formulas/inserter_throughput.py`)

For 4 of the 6 tiers, `items_per_cycle=1` unambiguously (checked
against `datapacks/dump/vanilla/inserter/*.json`: `inserter`,
`burner-inserter`, `long-handed-inserter`, `fast-inserter` have no
`stack_size_bonus`/multi-item hand), so `items/sec` equals the cited
`cycles/sec` directly:

| tier | items/sec (base, unresearched) |
|---|---|
| burner-inserter | 0.79 |
| inserter | 0.86 |
| long-handed-inserter | 1.25 |
| fast-inserter | 2.5 |
| bulk-inserter | 5.0 |
| stack-inserter | 15.0 |

`bulk-inserter`/`stack-inserter` resolved via
`wiki.factorio.com/Inserter_capacity_bonus_(research)`'s stated
**base** (unresearched) grab sizes: regular inserters=1,
`bulk-inserter`=2, `stack-inserter`=6 item(s) per cycle. This also
explains the `data.raw` field directly: `bulk-inserter` has no
`stack_size_bonus` because its base of 2 is an implicit engine
default for any `bulk: true` inserter, not a stored per-tier value;
`stack-inserter`'s `stack_size_bonus=4` is *added to* that same
implicit base of 2, giving `2+4=6` — exactly the wiki's cited base.
`bulk-inserter items/sec = inserter_throughput(2.5, items_per_cycle=2) = 5.0`;
`stack-inserter items/sec = inserter_throughput(2.5, items_per_cycle=6) = 15.0`.

**Still open**: research (`inserter-capacity-bonus-1..7` in
`datapacks/dump/vanilla/technology/`) adds two *separate* effects —
`bulk-inserter-capacity-bonus` (sums to +10 at full research) and
`inserter-stack-size-bonus` (sums to +2, only from techs 2 and 7) —
but how these combine with the base grab size, and whether they apply
identically to `bulk-inserter` vs `stack-inserter`, isn't documented
anywhere found this session: the dedicated wiki page for this exact
topic states outright that "the specific formula for combining these
effects is not described." The table above is the *unresearched*
baseline only — don't extrapolate a researched value from it.

## Chest-to-belt / belt-to-chest — not a single number

The wiki explicitly states throughput here depends on belt
saturation, lane position, and timing between the inserter and items
already moving on the belt — it is not reducible to one fixed
items/sec per tier the way chest-to-chest is. Range observed in
research: roughly 0.78–3.27 items/sec for basic inserters up to
~17/sec for a fully upgraded stack inserter on a turbo belt, but these
are scenario-dependent, not fixed constants.

Source: https://wiki.factorio.com/Inserters#Inserter_Throughput
Verified: 2026-08-06

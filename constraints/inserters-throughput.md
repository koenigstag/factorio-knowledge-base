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

| tier | items/sec |
|---|---|
| burner-inserter | 0.79 |
| inserter | 0.86 |
| long-handed-inserter | 1.25 |
| fast-inserter | 2.5 |

`bulk-inserter` and `stack-inserter` are excluded here on purpose:
`bulk-inserter` has no `stack_size_bonus` field in `data.raw` at all,
and `stack-inserter`'s `stack_size_bonus=4` doesn't cleanly reproduce
the wiki's cited "stack size 6" chest-to-chest figure either — both
tiers' actual items-per-cycle depend on researched "inserter capacity
bonus" technology level (`inserter-capacity-bonus-1` through `-7` in
`datapacks/dump/vanilla/technology/`), not a fixed datapack constant.
Don't assume a value for these two without that research-level input.

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

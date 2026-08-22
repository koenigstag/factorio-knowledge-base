# Scalable chem base: remote oil/chemistry site on its own chem bus

A companion site to
[layouts/scalable_main_base.md](scalable_main_base.md),
not part of that grid — this is where oil gets turned into everything
downstream of it (plastic, batteries, explosives, electric motors, and
the `sulfuric-acid` feed for `processing-unit`), connected to the main
base by rail rather than belt. Same black-box-module philosophy as the
science layout: each module is a city-block or micro-factory with
defined [ports](../glossary/invented/port.md), composed along a
[chem bus](../glossary/invented/chem-bus.md) instead of the main bus.

## Why a separate site at all

Two independent, sourced reasons, both established in prior discussion
now folded in here:

1. **Crude-oil is an "infinite resource" with yield decay**
   (`datapacks/dump/vanilla/resource/crude-oil.json`: `infinite: true,
   minimum: 60000, normal: 300000`) — pumpjack output degrades toward a
   floor of `60000/300000 = 20%` of fresh-patch yield as the field
   depletes, unlike ore patches which just run out. A site built for
   this needs room to keep *adding* pumpjacks over its lifetime, not a
   fixed footprint.
2. **Everything downstream of oil is a fluid until it isn't** — fluids
   don't travel by belt at all, and converting them to a solid
   (`plastic-bar`, `battery`, `electric-engine-unit`) before shipping
   avoids needing fluid-wagons on the main line. Doing that conversion
   next to the wellhead, not at the main base, is the whole reason this
   site exists.

## Machine tier: assembling-machine-2, not assembling-machine-1

Unlike `scalable_main_base.md` (which had to justify staying
on `assembling-machine-1`), this site can assume
**`assembling-machine-2`** is already unlocked, and this follows
necessarily rather than by assumption. Checked the technology
prerequisite chain directly
(`datapacks/dump/vanilla/technology/`): `advanced-circuit` requires
`plastics` → `oil-processing` → `oil-gathering` → `fluid-handling` →
**`automation-2`** (+ `engine`). `automation-2` is what unlocks
`assembling-machine-2` in the first place — so by the time any oil
processing exists at all, `automation-2` is necessarily already
researched. This matters concretely for `electric-engine-unit`, whose
recipe category `crafting-with-fluid` isn't in
`assembling-machine-1.json`'s `crafting_categories` at all (confirmed
directly against the file) — it's physically impossible on `-1`,
not just impractical.

Note: most chem-base modules (sulfur, sulfuric-acid, lubricant,
plastic, battery, explosives) run in a `chemical-plant`
(`crafting_speed=1`, single tier, no AM-tier question). Only
`engine-unit` and `electric-engine-unit` are `assembling-machine`
recipes, hence the AM2 discussion above applies specifically to them.

## Grid order along the chem bus

```
(off-site)                                                (on-site, along the chem bus)                                          (rail to main base)

[pumpjack field] --pipe--> [oil processing core:          [sulfur] --> [sulfuric-acid] --> [battery]  ---------------------\
 (expands over                advanced-oil-processing         |              |                                              \
  patch lifetime,              + heavy/light cracking,         v              v (small export)                               [rail station] --rail--> main base
  off-grid like drills)        ratio 20:5:17)               [explosives]  (to main base,                                     /
                                    |         \              (local use)   processing-unit)                                 /
                                    v          v                                                                            /
                              [lubricant]  [plastic] -------------------------------------------------------------------->/
                                    |                                                                                     /
                                    v                                                                                    /
                              [electric-engine-unit] <--engine-unit, electronic-circuit-- [rail station, import side] --/
```

Fluids (petroleum-gas, water, heavy-oil, lubricant, sulfuric-acid)
travel by pipe between adjacent modules; sulfur is the one solid
intermediate and travels a short belt hop from its own module to
whichever consumer needs it. Nothing here needs to be a strict
left-to-right line the way the main bus is — modules cluster around
the oil processing core more like a hub than a corridor, since most
connections are point-to-point pipes, not shared lanes. See
`glossary/invented/chem-bus.md` for why pipes change the shape of this
compared to `layouts/main_bus_consumer_layout.md`'s belt-only pattern.

## Oil processing core

The foundation everything else depends on:
`advanced-oil-processing` (oil-refinery) + `heavy-oil-cracking` +
`light-oil-cracking` (chemical-plant) at the already-derived **20:5:17**
ratio (`relations/oil_cracking_ratio.md`), chosen to convert all
heavy/light oil fully into `petroleum-gas`.

**Crude-oil demand**: `production_rate(1, 5, 100)` = 20 crude-oil/sec
per refinery × 20 refineries = **400 crude-oil/sec**.

**Water demand**: 10/sec/refinery × 20 (advanced-oil-processing itself)
+ 15/sec/machine × 5 (heavy-cracking) + 15/sec/machine × 17
(light-cracking) = 200 + 75 + 255 = **530 water/sec** — comfortably
under a single offshore pump's `1200 water/sec`
(`relations/steam_power_chain.md`), so water supply is never the
bottleneck here, same conclusion `relations/basic_oil_processing_ratio.md`
already reached about pipe throughput generally.

**Pumpjack count — a range, not a number**, because of the yield-decay
mechanic above: `production_rate(1, 1, 10)` = 10 crude-oil/sec/pumpjack
at fresh-patch (`normal`) yield, falling to `10 × (60000/300000)` = 2
crude-oil/sec/pumpjack at the depletion floor. For 400 crude-oil/sec:
**40 pumpjacks** (day one) up to **200 pumpjacks** (fully depleted) to
sustain the same 20:5:17 core. This is the concrete number behind "the
oil processing module is very large" — not just refinery/cracker count
(42 machines already), but a pumpjack field that has to grow 5× over
its own lifetime to hold throughput steady. **The curve between those
two endpoints is now derived too**: `relations/pumpjack_depletion_curve.md`
— the decay is linear, reaching the floor after exactly **24000
seconds (400 min ≈ 6.67 hours)** of continuous extraction, not some
front-loaded or exponential falloff.

## Sulfur

`recipe/sulfur.json`: 30 water + 30 petroleum-gas → 2 sulfur,
`chemical-plant`, `energy_required=1`. Rate: `production_rate(1, 1,
2)` = 2 sulfur/sec/machine. Feeds two local downstream consumers
(sulfuric-acid, explosives) via a short internal belt hop — the one
solid intermediate in this chain, per **Hedning1390**'s forum comment
already cited in `layouts/main_bus.md` (*"Sulfur is like copper wire...
should avoid belts"*), which this project reads as "don't belt it
far," not "never belt it at all" — a few tiles to an adjacent module on
a compact site is a different case than a base-spanning bus lane.

**A third destination leaves the site entirely**: `layouts/main_bus.md`'s
"Chemical science pack" section resolves that recipe's placement at
the main base, importing **0.5 sulfur/pack** as a new bus lane — unlike
the two local consumers, this slice rides the same rail line already
carrying `plastic-bar`/`battery` out (see "Rail stations" below), not
a belt hop.

## Sulfuric acid

`recipe/sulfuric-acid.json`: 5 sulfur + 1 iron-plate + 100 water → 50
sulfuric-acid, `energy_required=1`. Rate: `production_rate(1, 1, 50)` =
50 sulfuric-acid/sec/machine, consuming 5 sulfur/sec/machine.

**Tile**: 1 sulfuric-acid machine needs `5 / 2` = 2.5 sulfur machines
→ **5 sulfur machines : 2 sulfuric-acid machines** (clearing the
fraction). Small `iron-plate` tap (1/sec/machine) rides in on the same
import as everything else needing a trickle of it (battery, the
sulfuric-acid recipe itself) — not worth its own port.

**Three destinations**: most output feeds the local `battery` module;
a small slice exports to the main-base rail station for
`processing-unit` — see `layouts/main_bus.md`'s "Red vs blue circuit"
section for why that specific 5-sulfuric-acid-per-unit trickle is
worth shipping as a fluid rather than re-deriving `advanced-circuit`
at the chem-base instead; and a third, separate fluid-wagon run
supplies `layouts/nuclear_base.md`'s uranium mining (**≈4.34
sulfuric-acid/sec** for that file's 480MW reference reactor grid) —
of comparable magnitude to the `processing-unit` trickle, not
negligible against `battery`'s bulk draw either. This third
destination previously sat as an unreconciled open item in
`nuclear_base.md`; folded in here as of this revision — see "Rail
stations" below for how it's actually routed (a separate line from the
main-base connection, not through the main base).

## Lubricant

`recipe/lubricant.json`: 10 heavy-oil → 10 lubricant,
`energy_required=1`. Rate: `production_rate(1, 1, 10)` = 10
lubricant/sec/machine (1:1 with heavy-oil consumed). Single consumer:
`electric-engine-unit`, below.

## Plastic

`recipe/plastic-bar.json`: 20 petroleum-gas + 1 coal → 2 plastic-bar,
`energy_required=1`. Rate: `production_rate(1, 1, 2)` = 2
plastic-bar/sec/machine, consuming 20 petroleum-gas + 1 coal/sec/machine.
Ships to the main base as a bus lane (`layouts/main_bus.md`: 1-2 lanes)
— this project's answer to the "where should red circuit be made"
question from that file: plastic travels, `advanced-circuit` is
assembled at the main base, not here.

## Battery

`recipe/battery.json`: 20 sulfuric-acid + 1 iron-plate + 1 copper-plate
→ 1 battery, `energy_required=4`. Rate: `production_rate(1, 4, 1)` =
0.25 battery/sec/machine, consuming 5 sulfuric-acid/sec/machine.

**Tile**: 1 battery machine needs `5 / 50` = 0.1 sulfuric-acid machines
→ **1 sulfuric-acid machine : 10 battery machines**. Matches
`layouts/main_bus.md`'s existing `battery | 0-1` bus-lane figure and
its note that the recipe is sulfuric-acid-dominated, not iron/copper-
dominated — confirmed here from the production-rate side, not just the
per-craft ingredient list.

## Explosives

`recipe/explosives.json`: 1 sulfur + 1 coal + 10 water → 2 explosives,
`energy_required=4`. Rate: `production_rate(1, 4, 2)` = 0.5
explosives/sec/machine, consuming 0.25 sulfur/sec/machine.

**Tile**: 1 explosives machine needs `0.25 / 2` = 0.125 sulfur machines
→ **1 sulfur machine : 8 explosives machines**.

**A sub-product, not a bus/train export.** Demand is rare and small —
occasional cliff/rock clearing to grow the pumpjack field or add a
module, not a continuous consumer — so this doesn't get a port onto the
chem bus or the rail station at all. Instead it sits on the
**logistics network** as a passive/active-provider chest: a
construction robot pulls from it automatically when a clear-cliff order
needs explosives, and the player can pull a stack on request via a
requester chest, logistic robots ("transport drones") carrying it to
wherever it's asked for — matching **zOldBulldog**'s already-cited
approach (`layouts/main_bus.md`) of distributing low-volume explosives
locally by bot rather than shipping them. The **1 sulfur machine : 8
explosives machines** tile above is almost certainly oversized for this
role in practice — a single explosives machine, run intermittently,
likely covers real demand; sized here for ratio completeness, not
because a dedicated production line is actually warranted.

**Decision (2026-08-09): stays purely local to the chem-base, no
main-base export lane.** If the main base separately wants explosives
for its own cliff-clearing, it gets its own small local production the
same way, rather than importing them — matching the sub-product framing
above; a rare, low-volume item isn't worth a dedicated rail/bus lane
just to centralize it at one site.

## Electric engine unit

Split across two sites, established in prior discussion:

- **`engine-unit`** (`recipe/engine-unit.json`: 1 steel-plate + 1
  iron-gear-wheel + 2 pipe → 1 engine-unit, `advanced-crafting`
  category, `assembling-machine-1`-capable) is assembled **at the main
  base** — no fluid, no chemistry, everything it needs is already
  there. Ships to the chem-base as a finished solid.
- **`electric-engine-unit`** (`recipe/electric-engine-unit.json`: 1
  engine-unit + 15 lubricant + 2 electronic-circuit → 1
  electric-engine-unit, `crafting-with-fluid` category,
  `assembling-machine-2` minimum) is assembled **at the chem-base**,
  where `lubricant` already is.

Rates at `assembling-machine-2` (`crafting_speed=0.75`):
`engine-unit` = `production_rate(0.75, 10, 1)` = 0.075/sec/machine;
`electric-engine-unit` = same rate (1:1 ratio, `energy_required=10`
both sides, same reasoning as `relations/iron_to_steel_furnace_ratio.md`'s
same-tier cancellation) — **1 engine-unit machine : 1
electric-engine-unit machine**, exactly.

Lubricant demand: 1 electric-engine-unit machine needs `9/8` = 1.125
lubricant/sec, against 1 lubricant (`chemical-plant`) machine's 10/sec
→ 1 lubricant machine covers `10 / 1.125` ≈ 8.9 electric-engine-unit
machines. Clearing the fraction: **9 lubricant machines : 80
electric-engine-unit machines** (and 80 engine-unit machines to match,
1:1). This is the largest tile in the whole chem-base — electric-engine-unit's
own crafting is comparatively slow (`energy_required=10` at AM2 speed),
so it takes many machines to keep up with one lubricant plant's output.

## Rail stations

Two separate stations, not one shared line — matches this project's
established pattern of dedicated point-to-point
[train-base](../glossary/canonical/train-base.md) connections rather
than a [train-bus](../glossary/invented/train-bus.md) (see that file's
own note that this project hasn't built a true train-bus anywhere
yet). The chem-base sits between two independent outposts here, each
gets its own line.

**Main-base station** — two-sided, same shape as
`scalable_main_base.md`'s ore-train and pack-train stations:

- **Import** (from main base): `coal` (plastic + explosives),
  `iron-plate`/`copper-plate` (small catalyst amounts across several
  recipes), `electronic-circuit` (electric-engine-unit), `engine-unit`
  (electric-engine-unit).
- **Export** (to main base): `plastic-bar` (bus lane), `battery` (bus
  lane), `electric-engine-unit` (wherever it's consumed — not modeled
  yet, see open questions), a small `sulfuric-acid` fluid trickle for
  `processing-unit`, and `sulfur` (bus lane, 0.5/pack) for
  `chemical-science-pack`.

**Nuclear-base station** — one-sided, export only: a dedicated
fluid-wagon run carrying `sulfuric-acid` to `layouts/nuclear_base.md`'s
uranium mining (≈4.34/sec at that file's reference grid, see "Sulfuric
acid" above). No return cargo modeled — the nuclear base's own
outputs (enriched uranium products) don't route back through the
chem-base in this design.

**Not sized here**: exact wagon/train counts for either station —
unlike `scalable_main_base.md`'s reference cell, this file doesn't
fix a target output, so per-item throughput (and therefore wagon
counts, `relations/cargo_capacity.md` figures, loading-inserter tiers)
is left as a follow-up once a specific production target is chosen,
same "derive the ratio, don't cite a magic total" stance
`layouts/main_bus.md` already takes.

## What's still open

- Exact train/wagon counts at the rail station (needs a target output
  first, see above).
- Where `electric-engine-unit` is actually consumed at the main base
  (car/tank/spidertron production, robots — not modeled in this
  project yet) — this file only gets it to the rail station, not to
  its final consumer.
- Exact pumpjack depletion curve over time (only the fresh/floor
  endpoints are derived here, not the rate of decay between them).

Verified: 2026-08-09

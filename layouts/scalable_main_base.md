# Scalable main base: city-block grid, extensible science row, ore-train head, remote labs

The heart of a multi-site base (see `glossary/canonical/megabase.md`
for how this fits alongside `layouts/scalable_chem_base.md`,
`layouts/solar_base.md`, `layouts/nuclear_base.md`) — where the mall
lives, ore becomes plate, and science packs get made. A concrete
instance of [layouts/main_bus_consumer_layout.md](main_bus_consumer_layout.md):
city-block modules, tap-modules in the gaps, main bus through the gaps
— not `layouts/city_block_grid.md`'s own (more common, rail-connected)
variant, stated plainly since the two are easy to conflate.
`automation-science-pack` (red) and `logistic-science-pack` (green) are
worked out in full below as the first two science blocks, but this is a
**template** — later science tiers slot in further east the same way,
without touching anything already built.

Each block is a black box (internal belt/inserter layout unspecified)
except for its [ports](../glossary/invented/port.md) (item, direction,
tap ratio). One hard rule fixes block order: **a block can only tap an
item some earlier block already produced.** That's what determines the
sequence below, not aesthetics — and it's what lets the template extend
cleanly (a new science block just needs a free gap further east).

## Design choice: main bus first, not the only option

This file builds on `layouts/main_bus.md` running through the gaps
because that's the pattern with clear step-by-step belt math already
worked out, not because it's the only valid starting point — the
community record on bus-vs-city-block is genuinely split, and it's
worth stating plainly rather than presenting main bus as the default:

- **Main bus is a strong *early* pattern, widely reported to scale
  poorly toward megabase size.** Forums.factorio.com t=37024:
  **Nilaus** (thread starter) — *"using a Main Bus or Central Bus is
  all the rave these days... but to me it doesn't scale well and
  doesn't lend itself easily to robotic transition."* **Carl**, same
  thread, narrows the failure mode — it's a *sizing* problem more than
  a concept problem: main bus *"works perfectly so long as you aren't
  putting too much iron or copper in to start with."*
- **Starting directly as city-blocks, no main-bus phase at all, is
  also viable** — nothing about red/green (or later steel-age)
  research requires a bus-shaped base first. Forums.factorio.com
  t=126785: **Maltar Draco** frames the actual payoff as
  *expandability*, not throughput: bolt on another block instead of
  re-routing a bus. Steam Community discussion (id
  `600764072244289772`): **brian_va** — practical prerequisite is
  construction robots, *"I would hold off until you get bots"*, not a
  specific tech tier.
- **Neither pattern scales without limit.** The same t=126785 thread's
  **mmmPI** warns city-blocks shift the bottleneck rather than remove
  it: *"City blocks are 'best avoided' because they complicate a lot
  the pathfinding for trains"* — at megabase scale, train count/
  signaling becomes the ceiling instead of belt length.
- **The specific mechanical reason main bus and city-block resist
  combining** (not just stated preference): r/factorio thread `gnolui`
  ("Where do I put the main bus if I'm trying a city block base?") —
  **burenning** — *"every single city block design has to be adjacent
  to the bus, and the majority of the bus will be wasted belt buffers
  as the products aren't used by the adjacent blocks. Use trains,
  transport drones, or logistics bots..."* — a physical-adjacency
  constraint, which is also why this project's train-bus pattern
  exists as the thing that actually fills that role once a base goes
  city-block.
- **Main bus as an explicit bootstrap, not a permanent structure**:
  same `gnolui` thread — **68Cadillac** — *"You use the Main Bus as
  the starting point to the City Block base. Once the Mainbus Area
  starts outputting enough assemblers, inserters, rails, modules, and
  all the various parts needed to set up your City Block you move to
  City Block... Main bus is just a stepping stone. City Block uses
  rail to move items to and from itself."*

Net read, matching the balance struck in
[glossary/invented/train-bus.md](../glossary/invented/train-bus.md):
both patterns trade one scaling ceiling for another, but main bus has
**more** reported cons specifically at megabase scale. This project's
own stated position, beyond just summarizing the community split:
[decisions/0003](../decisions/0003-main-bus-as-bootstrap-city-block-train-bus-as-target.md) —
city-blocks are the preferred structural pattern outright, and
train-bus (not main-bus) is the long-game target; main-bus is an
explicit early-game bootstrap, matching 68Cadillac's framing above.
This file documents the belt-first version because it's the one with
citable math already available (`layouts/main_bus.md`) and it's this
project's own documented bootstrap stage, not because main-bus is the
end-state recommendation; a city-block-from-the-start version of the
same red/green science modules would tap the same ports, just without
ever running a bus through the gaps.

Sources: forums.factorio.com topic 37024 ("City Blocks instead of
Main Bus" — Nilaus, Carl), topic 126785 ("Looking for advice on my
city block setup" — mmmPI, Maltar Draco); Steam Community discussion
427520/0/600764072244289772 (brian_va); r/factorio thread `gnolui`
("Where do I put the main bus if I'm trying a city block base?", 2020
— burenning, 68Cadillac).
Verified: 2026-08-09

## Grid order

```
(bus origin / raw end)                                                                            (bus continues east, reserve for growth)

 [drills, off-grid] --rail--> [ore train station] -> [iron/copper/brick furnaces] -> [steel furnace] -> [green circuit] -> [red science] -> [green science] -> ...
                                                              |                                                                  |               |
                                                              v (tap-out: iron/copper-plate,                          taps: iron-plate,   taps: iron-plate,
                                                                 stone-brick — main bus begins here)                  copper-plate         electronic-circuit
                                                                                                                                                    |
                                                                                                                                                    v
                                                                                                        [science bus] -> [pack train station] --rail--> [labs, remote site]
```

- **Drills** are off-grid at the ore patch, rail-connected only —
  [train-base](../glossary/canonical/train-base.md) pattern, same shape
  as a [micro-factory](../glossary/canonical/micro-factory.md) outpost.
- **Ore train station** sits first, at the bus's source end (matches
  `layouts/main_bus.md`'s "closest-to-source first" convention). Ore
  never rides the bus itself — one hand-off to the furnace block.
- Everything downstream of the furnace block only taps what it (or an
  earlier block) produced — why steel/circuit/science all sit after it.
- **Green circuit precedes green science** (which taps
  `electronic-circuit`); red science doesn't need circuit at all, so
  its position relative to circuit is cosmetic, kept here for
  plates→intermediates→science readability.
- **Steel furnace is its own block** — see "Steel and brick" below for
  why it's included despite not being on red/green's critical path.

## Drills (off-grid)

One outpost per ore type, each with its own rail line to the station.
`relations/mining_belt_ratios.md`'s `mining_time=1` table sizes drills
per outpost belt; loading inserters use the same mechanism as
`relations/wagon_loading_throughput.md`, run in reverse. **Open**: train
paths/wagons per outpost depend on route distance — no formula for that
here.

## Ore train station

Unloads ore via inserters onto the furnace block's feed belts.
`long-handed-inserter` (not `bulk-inserter`, which needs
`advanced-circuit` + `logistics-2` — well past red/green science) is
unlocked by the same `automation` tech as `assembling-machine-1`
(`technology/automation.json`), so it's available at this stage. Against
this file's own reference-cell demand (iron-ore 15.0/s, copper-ore
5.0/s, from the furnace section below): `relations/wagon_loading_throughput.md`'s
1.25/s/inserter needs **12 long-handed-inserter** (iron) and **4**
(copper) — both well under the tier's 24/wagon cap.
`relations/cargo_capacity.md`: `iron-ore` 2000/wagon. Scales by adding
unloading bays, not belt width — ore doesn't travel far enough here to need it.

## Iron / copper / brick furnaces — scalable

One grid position, three parallel independently-scalable furnace
row-sets (iron-plate, copper-plate, stone-brick), each on its own
main-bus lane. Scaling adds rows *away* from the bus, so the block's
bus-facing width never changes — same principle as
`layouts/main_bus.md`'s "build off one side only."

Per-row throughput: `relations/smelting_ratios.md`'s `energy_required=3.2`
table (e.g. 24 `electric-furnace`/belt). Ore per added row:
`relations/mining_furnace_ratios.md` — 1.25 `electric-mining-drill`/furnace
for plate, double (2.5) for stone-brick (2 stone/craft, not 1).

## Steel furnace — separate block

Taps `iron-plate` from the bus (not its own ore), taps `steel-plate`
back. Kept separate so its furnace count scales against steel's own
demand without touching the plate block's count —
`relations/bus_lane_ratios.md`'s steel ratio is steep (5.0 iron-plate/
steel-plate); `relations/iron_to_steel_furnace_ratio.md` gives the
furnace-count side, exactly **1:1** at matching tiers.

**Neither `automation-science-pack` nor `logistic-science-pack` needs
steel or brick** (checked against both recipes' full decomposition).
Both blocks are here for the base's general architecture (steel for
later science/buildings, brick for concrete), not a red/green
dependency — stated plainly rather than implied.

## Machine tier: assembling-machine-1

All tileable modules below run on `assembling-machine-1`
(`crafting_speed=0.5`). Checked against the tech tree
(`datapacks/dump/vanilla/technology/`), not assumed:
`automation` (unlocks AM1) needs only `automation-science-pack` — day
one. `automation-2` (AM2) requires `logistic-science-pack` as a
*prerequisite tech*, so green science must already be running on AM1
before AM2 is even researchable. `automation-3` (AM3) requires
`production-science-pack`, a tier this base doesn't produce — AM3 is
simply unreachable here, not a judgment call.

All three tiers share the `crafting_categories` this file needs
(`crafting`, `electronics`, `pressing`), so the choice is purely about
unlock timing. **Tile ratios below are tier-independent** — uniform
`crafting_speed` scaling cancels out of any machine-count ratio, same
algebra as `relations/iron_to_steel_furnace_ratio.md`; only the
absolute rates change with tier. Upgrading a built module to AM2 later
is a drop-in speed increase, not a redesign.

## Tileable green circuit module

Ports: taps `iron-plate` + `copper-plate` in, `electronic-circuit` out
(standard bus item, per `layouts/main_bus.md`). `copper-cable` is
local, not tapped (single-craft-step convention).

**Tile**: **2 electronic-circuit machines : 3 copper-cable machines**
(5 total). `production_rate(0.5, 0.5, 1)` = 1.0 circuit/s/machine
(needs 3 copper-cable/craft); `production_rate(0.5, 0.5, 2)` = 2.0
cable/s/machine — 2 circuit-machines' `6`/s cable demand exactly
matches 3 cable-machines' output.

Tile output: **2.0 electronic-circuit/s**. Bus taps
(`relations/bus_lane_ratios.md`: 1.0 iron, 1.5 copper per circuit):
**2.0 iron-plate/s, 3.0 copper-plate/s**.

## Tileable red science module (automation-science-pack)

Ports: taps `copper-plate` + `iron-plate` in, `automation-science-pack`
out — to the **science bus**, not the main bus (spends its output-side
port on that instead of rejoining the main bus). `iron-gear-wheel` is
local.

**Tile**: **10 pack machines : 1 gear machine** (11 total).
`production_rate(0.5, 5, 1)` = 0.1 pack/s/machine (needs 1
gear/craft); gear rate 1.0/s/machine — 10 machines' 1.0/s gear demand
exactly matches.

Tile output: **1.0 pack/s**. Bus taps
(`relations/science_pack_ratios.md`: 2.0 iron, 1.0 copper/pack): **2.0
iron-plate/s, 1.0 copper-plate/s**.

## Tileable green science module (logistic-science-pack)

Ports: taps `iron-plate` + `electronic-circuit` in, `logistic-science-pack`
out (science bus, not the main bus). `iron-gear-wheel`, `inserter`,
`transport-belt` are all local.

**Tile**: **24 pack : 2 inserter : 1 transport-belt : 3 iron-gear-wheel
machines** (30 total). Pack rate `production_rate(0.5, 6, 1)` = 1/12 s;
inserter 1.0/s (needs 1 circuit + 1 gear + 1 iron-plate/craft);
transport-belt 2.0/s (needs 1 iron-plate + 1 gear/craft, 2 out).
Clearing denominators on the 24-pack base gives the 2:1 inserter:belt
ratio; combined gear demand (2×1.0 + 1×1.0 = 3/s) matches 3 gear
machines exactly.

Tile output: **2.0 pack/s**. Bus taps (cross-checked two ways —
per-machine sum, and `relations/science_pack_ratios.md`'s decomposition
minus the circuit share): **9.0 iron-plate/s, 2.0 electronic-circuit/s**.

**One green-circuit tile's output (2.0/s) exactly meets one green-science
tile's circuit demand (2.0/s)** — a 1:1 pairing that fell out of the
independent calculations, not designed in, and holds at any AM tier.

## Reference cell: balancing red and green output

Tiles aren't naturally 1:1 in output (red = 1.0/s, green = 2.0/s — tier-
independent ratio). For equal throughput: **2 red tiles + 1 green tile**
(+ its 1 green-circuit tile) = 2.0 pack/s each.

| block | tiles | iron-plate tap | copper-plate tap |
|---|---|---|---|
| red science ×2 | 22 AM1 | 4.0/s | 2.0/s |
| green circuit ×1 | 5 AM1 | 2.0/s | 3.0/s |
| green science ×1 | 30 AM1 | 9.0/s | — |
| **total** | **57 AM1** | **15.0/s** | **5.0/s** |

Furnaces (`electric-furnace`, `production_rate(2,3.2,1)` = 0.625/s):
**24 iron + 8 copper = 32 furnaces**. Drills
(`relations/mining_furnace_ratios.md`'s 1.25/furnace): **30 iron-ore +
10 copper-ore = 40 drills**, across ≥2 outposts — modest, consistent
with an AM1-stage base. Illustrative sizing only; the tile ratios are
what's load-bearing, and scale linearly to any target.

## Science bus

A dedicated second bus (`glossary/invented/science-bus.md`) carrying
only science packs from the red/green blocks to the pack train station
— doesn't need to run far, since it only has to reach the station at
the grid's edge, not a labs block. Extends to more pack types the same
way as later science blocks are added.

## Labs: remote site via dedicated pack train

Packs are train-base cargo, same shape as the drills at the other end
of this layout — the labs field lives on its own remote site, arbitrarily
far away, connected by a two-sided station (mirrors the ore station,
just outbound instead of inbound and carrying packs instead of ore).

- **Base-side station**: science bus's endpoint, one dedicated wagon
  per pack type.
- **Labs-side station**: unloads onto a short belt feeding the labs
  field.

**Wagon capacity**: `relations/cargo_capacity.md` — science packs are
`stack_size=200`, no wagon weight limit → **8000 packs/wagon**.
**Loading**: at the 2.0/s + 2.0/s reference cell, 3 plain `inserter`
(2.58/s) already covers it — no research needed; 1 `fast-inserter`
(also unlockable on red science alone, `technology/fast-inserter.json`)
would do it in one. **Fill time**: `8000/2.0` = 4000s (≈67 min) — an
infrequent shuttle, not an ore-train-style rush. **Train**: small
dedicated, e.g. `1-2-1` (`glossary/canonical/train-configuration-notation.md`)
or `L2CL`.

`lab.json`: `researching_speed=1`, `module_slots=2`, `inputs` includes
both packs among 12 possible types — a lab fed only these two is valid,
if research-limited.

**Labs field size**: `relations/lab_pack_consumption_rate.md` —
**30 labs** fully consumes the reference cell's 2.0/s red + 2.0/s
green supply while researching `automation-2` (the representative
both-pack-types tech; single-pack-type techs like `automation` need
only 20, `logistic-science-pack` only 10). Not a fixed number for the
whole game, though — `unit.time` ranges 5–120s across the tech tree,
so lab count has to grow as research reaches costlier techs even
though pack production never changes; 30 is this reference cell's
early-game figure, not an end-game one.

**Why remote, not just detached-on-site**: an on-site labs block still
shares the grid's footprint — a large labs field could eventually
approach it. A remote site removes that risk *by construction*, with
its own power/roboport grid, at the cost of a second rail line and two
stations — worth it once labs are expected to grow large, not
necessarily for a small early setup.

## City-block size

No fixed requirement, but `glossary/canonical/city-block.md`'s 100×100
is the one candidate with an independent derivation (roboport
logistic-network spacing) rather than cited convention;
`relations/roboport_area_coverage.md` gives its roboport count (4
logistic, 1 construction).

## What's still open

- Ore/pack train routing (path/wagon count) — site-distance dependent,
  no formula held.
- Exact lab-count growth curve across the full tech tree (only the
  30/20/10-lab early-game snapshot is derived,
  `relations/lab_pack_consumption_rate.md`) — not how much to
  overbuild upfront vs. scale incrementally.
- Gap width between blocks for science-bus vs. main-bus lanes —
  inherits the open question in
  `layouts/main_bus_consumer_layout.md`'s "Gap width" section.
- Whether green-circuit output should cover more than the green-science
  tile alone (real bases also feed red circuits, inserters elsewhere).
- Remote labs' own power/roboport infrastructure — not addressed here.

Verified: 2026-08-09

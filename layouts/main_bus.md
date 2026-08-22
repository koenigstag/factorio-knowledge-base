# Plain main bus: a set of parallel belts, tapped by adjacent factories

The bus itself as a standalone layout pattern — no `city-block` grid,
no tap-module: just parallel belts running from raw production toward
the base, with assembly setups placed alongside and tapping in
directly. See
[layouts/main_bus_consumer_layout.md](main_bus_consumer_layout.md) for
the composed variant where the bus runs through repeatable blocks
instead of ad-hoc production setups, including the practical
convention for the space between modules along the bus (a property of
that composed pattern, not this standalone one) — distinct from
[layouts/city_block_grid.md](city_block_grid.md), which is the (more
common, rail-connected) city-block pattern without a bus running
through it at all.

## Belt grouping: multiples of 4

Belts are conventionally grouped in fours, with underground belts used
to route perpendicular crossings under a whole group at once. This
isn't arbitrary: the basic-tier `underground-belt`'s `max_distance=5`
(`datapacks/dump/vanilla/underground-belt/underground-belt.json`)
gives a **crossing gap of exactly 4 tiles** — `max_distance − 1`, since
the entrance/exit tiles themselves aren't free surface space, see
`relations/underground_belt_crossing_gap.md` — precisely enough for a 4-wide belt group in one hop, not
merely "close enough." Every higher tier's crossing gap (fast=6,
express=8, turbo=10) covers 4 comfortably too, so the grouping-by-4
convention holds regardless of belt tier.

## Spacing between groups: 2 tiles

The wiki tutorial's stated convention: "two free spaces for every
group of four belts," so underground belts within a group can surface
to cross other groups, and so foot/vehicle traffic and cross-bus
piping have room.

## Distance from the bus to production modules

At least 3 tiles between the bus and adjacent builds, 6–10 more
comfortable — room for the tap-in infrastructure itself (splitters,
inserters, a short belt run) plus later expansion, per the wiki
tutorial. This is the *perpendicular* distance, bus to module — the
*longitudinal* spacing between two repeatable modules placed along the
bus one after another is `layouts/main_bus_consumer_layout.md`'s own
concern, not this standalone pattern's (this file doesn't assume
modules are identical/repeatable at all).

## Item ordering: convention, not a rule

A commonly cited progression, closest-to-source first: iron plate,
copper plate, steel, then intermediates (iron gear wheel, electronic
circuit, advanced circuit, processing unit), then optional extras
(battery, plastic bar, stone, sulfur) if produced centrally rather
than locally. The wiki is explicit that this is preference-driven, not
an engine rule or a single correct ordering — no lane-by-lane
assignment is prescribed.

**Correction (2026-08-09): the "optional extras" framing puts plastic
bar in the wrong place.** Read literally as physical bus position,
this ordering puts `plastic bar` *after* `advanced circuit` — but
`plastic bar` is an ingredient *of* `advanced-circuit`
(`recipe/advanced-circuit.json`: 2 electronic-circuit + 2 plastic-bar +
4 copper-cable → 1 advanced-circuit). A block producing advanced
circuits has to tap plastic bar from somewhere already upstream of it,
per this file's own hard ordering rule (a block can only tap what an
earlier block already produced) — placing plastic bar downstream as an
"extra" creates exactly the reverse-lane problem this project ran into
designing `layouts/scalable_main_base.md`. Same issue one
step further back: `coal` is an ingredient of `plastic-bar`
(`relations/bus_lane_ratios.md`: 0.5 coal per plastic-bar) and isn't
even mentioned in this ordering paragraph at all, only in the table
below. **Corrected order**: iron/copper/steel → coal → plastic bar →
green circuit → red circuit → blue circuit. `stone`/`stone-brick`
depend on nothing else in this list (smelted straight from its own
ore), so its position is free.

## Tap-off convention: plain splitter by default

Per the wiki tutorial and corroborating forum consensus: use an
ordinary (no-priority) splitter for a normal tap — see
`mechanics/splitter-priority.md` for what "no priority" actually does
(even split, spills to the other output only once one side backs up).
Reserve **output priority** for an intentional "serve this consumer
first" rule, and a dedicated **lane balancer**
(`glossary/canonical/lane-balancer.md`, or a full multi-belt
**belt balancer** — `glossary/canonical/belt-balancer.md` — for
imbalance across several bus lanes of the same item rather than within
one belt) only once imbalance is actually measured, not preemptively
on every tap. Over-applying balancers/priority where a plain splitter
would do is called out directly in community sourcing as unnecessary
complexity.

## Bus width: derive the ratio, don't cite a magic total

Community-cited totals range widely — a "flexible starter" bus with 4
iron + 4 copper + 1-2 green-circuit lanes plus single lanes for
everything else, up to "24, maybe 32" belts on a large 800-SPM bus —
because total width depends on the base's actual target output, which
this layout doesn't fix. What *doesn't* depend on target output is the
**ratio** between an item and its ingredients, and this project
already holds the primitives to derive that exactly instead of citing
someone else's number, per Hard rule 3: see
`relations/bus_lane_ratios.md`, derived straight from recipe
ingredient/result amounts (`formulas/recipe_ingredient_ratio.py`), not
a community estimate — e.g. 1 lane of green circuits needs 1
iron-plate-lane + 1.5 copper-plate-lanes, cross-checked exactly against
independent community sourcing. For per-item throughput at a smelting/
mining level, `relations/smelting_ratios.md`,
`relations/mining_belt_ratios.md`, and `relations/mining_furnace_ratios.md`
already give machines/belts-saturated. See
`examples/main_bus_lane_sizing.md` for the full worked method — how to
turn a specific target output into exact lane counts, including the
tier-mixing trap (lane counts across different belt tiers aren't
directly additive; convert to items/sec first).

### A practical starting template, synthesized from multiple independent community configs

No single source is authoritative here — five experienced-player
configurations (from two forum threads) were compared; the table below
is their common ground, in lanes, for a base heading toward
red/blue-science-pack-level automation (not a full 800-SPM megabase,
which scales every number up further):

| item | lanes on the bus | note |
|---|---|---|
| iron plate | 4 | *direct-consumption plate only* — see the smelting-capacity caveat below, this is not total iron demand |
| copper plate | 4 | see "iron vs copper" below — the cited configs run it equal to iron, not above it |
| steel plate | 2 | smelted from *separate* iron-plate/ore, not carved out of the 4 iron-plate lanes above |
| green circuit (electronic-circuit) | 2-4 | some configs smelt it locally instead of bussing it — see `mechanics/logistic-chest-priority.md`-adjacent point below about not bussing everything |
| red circuit (advanced-circuit) | 2 | added once oil processing is online — see "Red vs blue circuit" below for why this one gets a real lane and blue circuit doesn't |
| blue circuit (processing-unit) | 0 (not a lane) | not bussed at all by community consensus, not just "rarely a full lane" — see "Red vs blue circuit" below |
| plastic bar | 1-2 | shipped in as a solid from wherever it's cracked/made, not produced locally on the main bus itself — see "Fluids and chemistry intermediates" below |
| stone / stone brick | 1 (often shared as half-lane) | |
| coal | 1 | |
| battery | 0-1 | dominated by sulfuric-acid (`recipe/battery.json`: 20 sulfuric-acid + 1 iron-plate + 1 copper-plate), same "stay near the acid" reasoning as blue circuit below, not an iron/copper-driven item despite its ingredient list |

**The "4 iron plate" row is not the base's total iron demand.** Steel
is smelted from iron-plate at a steep **5:1** ratio
(`relations/bus_lane_ratios.md`) — the 2 steel-plate lanes above
consume `2 × 5 = 10` iron-plate-lane-equivalents of *additional*
smelting capacity, on top of (not instead of) the 4 lanes that reach
the bus as plain iron-plate. Total iron-plate-equivalent output the
furnace array/ore patch must support for this template is
`4 + 10 = 14` lanes, not 4. Sizing smelting capacity off the visible
bus figure alone is a common practical mistake this ratio explains —
the two product streams (plain plate vs. steel) split off from ore
independently, upstream of where either reaches the bus.

Iron gear wheels, copper cable, and other single-craft-step items are
**not** recommended for a permanent bus lane by this same community
consensus — cheap enough, and used unevenly enough, that producing
them beside the consumer is preferred over dedicating bus width.

### Red vs blue circuit: why one gets a lane and the other doesn't (2026-08-09)

Both circuits looked similar at first — each just another intermediate
in the "then optional extras" pile — but community sourcing on the two
is not symmetric at all, and it doesn't come down to which is more
expensive per item; it comes down to how much of the base actually
consumes each one.

**Red circuit (advanced-circuit): genuinely bussed.** Multiple
independent threads treat it as real bus/train infrastructure, not
something to tuck away locally: *"Red and blue circuits are used
massively and not only deserve a lane/train but eventually even get
their own train outpost to produce them in massive quantities"*
(forum aggregate, high-volume claim). **Tertius**'s optimized 5k-SPM
design (`forums.factorio.com/viewtopic.php?t=105184`, "Bus/Rail oil
products") ships **plastic bars by train exclusively** as a
high-demand item, while keeping lower-volume intermediates (sulfuric
acid, lubricant) local — directly supporting this project's own
`layouts/scalable_main_base.md` design (ship the solid
`plastic-bar`, assemble `advanced-circuit` on the main bus, not the
other way around).

**Blue circuit (processing-unit): not bussed by community consensus,
full stop** — stronger than this file's older "0-1, rarely a full
lane" hedge. From `forums.factorio.com/viewtopic.php?t=45799` ("Main
bus, a whole belt of processing units?"): **Mehve** — *"even with my 2
rocket/minute build, I was only using half a blue belt of processing
units"* and *"a full belt of processing units is ridiculous"*;
**Hannu** — *"Most players do not fill even one half of yellow belt.
Filled belt is needed only if you are going to do one rocket per
minute base or use end game mods"*; **iceman_1212** — *"2 full blue
belts of blue circuits is just about good for ~10RPM, which is
obviously well beyond the limits of a main bus type base."* **sparr**
notes the reason demand stays low: a full belt of processing units
would need roughly 24 belts of upstream green circuits feeding it —
matching this project's own independently-derived figure in
`relations/bus_lane_ratios.md` (24 iron-plate-lanes / 40
copper-plate-lanes of upstream demand per blue-circuit lane) from a
completely different method (recipe-amount decomposition vs.
forum-reported build experience), not just citing the forum number.

**Practical consequence for this project's chem-base design (corrected
2026-08-09)**: an earlier version of this section concluded
`processing-unit` should be assembled at/near the chem-base, reasoning
only from its `sulfuric-acid` ingredient — that skipped the fact that
`processing-unit` also needs **2 `advanced-circuit`** directly
(`recipe/processing-unit.json`: 20 electronic-circuit + 2
advanced-circuit + 5 sulfuric-acid), and `advanced-circuit` is *itself*
a chain (2 electronic-circuit + 2 plastic-bar + 4 copper-cable each,
`recipe/advanced-circuit.json`) that this file already puts on the main
bus, not at the chem-base. Comparing what actually has to physically
travel, per 1 `processing-unit`, for each place it could be assembled:

| assembled at | what ships in | total units |
|---|---|---|
| main base | 5 `sulfuric-acid` (fluid) only — electronic-circuit and advanced-circuit are already bussed there | **5** |
| chem-base, shipping in finished green circuit | 24 electronic-circuit (20 direct + 4 for the 2 advanced-circuit) + 4 copper-plate (for the copper-cable) | 28 |
| chem-base, shipping in raw plate instead | 24 iron-plate + 40 copper-plate (electronic-circuit's own 1.0 iron-plate + 1.5 copper-plate per unit, `bus_lane_ratios.md`) | 64 |

**Corrected conclusion: `processing-unit` is assembled at the main
base**, tapping the already-bussed `electronic-circuit`/
`advanced-circuit` lanes — the chem-base only ships in the 5
`sulfuric-acid` per unit, a trivial fluid volume given
`processing-unit`'s own demand is already small
(`bus_lane_ratios.md`'s 24/40 iron/copper-lane-equivalent figure
above). This is the one concrete case in this file where the "ship the
fluid" side of the "Fluids and chemistry intermediates" debate below
(DaveMcW/Ranakastrasz/JimBarracus) wins outright rather than staying
genuinely contested — not because centralizing sulfuric-acid
production is wrong in general, but because the *alternative* here
means re-deriving an entire circuit's worth of already-bussed
intermediates at a second site, not just moving one fluid instead of
one solid.

### Fluids and chemistry intermediates: contested, not settled (2026-08-09)

Unlike solids, this project's `bus_lane_ratios.md` explicitly excludes
fluids from lane counts (they're pipe throughput, not belt width) —
but whether chemistry fluids belong on the bus *at all*, even as
pipes, turns out to be a genuine, unresolved community split, not a
one-sided convention like the "don't bus copper-cable" case above.

**The case for keeping sulfur/sulfuric-acid off the bus entirely**
(`forums.factorio.com/viewtopic.php?t=60758`, "Sulfur vs Sulfuric Acid
on Main Bus"): **Hedning1390** — *"Sulfur is like copper wire,
expanding with a very rapid production, and like copper wire should
avoid belts"* (note: about `sulfur` specifically, the solid
intermediate one step before sulfuric acid — not about the acid
itself); **bobucles** — *"Pro: It's on the bus. Con: Stop putting
intermediates on the bus"*; **zOldBulldog** — builds `explosives` next
to the sulfur plant and distributes them by logistics bots since
they're *"fairly low volume items,"* rather than piping/busing
anything. This is the view this project's earlier chem-base discussion
(`layouts/scalable_main_base.md`) leaned on: convert fluids
to a solid before they ever have to travel.

**The case for a fluid on the bus anyway** (same thread): **DaveMcW**
— *"A sulfuric acid pipe can move 2.5 times as much sulfur [in acid
form] as a blue belt,"* an efficiency argument for the fluid over its
solid precursor; **Ranakastrasz** runs *"4 pipes as part of my
bus... Sulfuric acid and Lubricant"* alongside oil and water, treating
fluids as first-class bus lanes, not an exception; **JimBarracus**
recommends *"centralized production with train distribution"* for
sulfuric acid specifically — i.e. produce it at one chem site and ship
the *fluid itself* (fluid-wagon) to consumers, not just its downstream
solid products.

**Not resolved here**: this project doesn't pick a side in general.
Both are real, cited, working community approaches, and nothing in
this project's own sourced data (data.raw doesn't encode "where should
this be built") settles it as a blanket rule — it's a genuine tradeoff
between fewer wagon/pipe types (convert-to-solid-first) and fewer
separate production sites per fluid (centralize-and-ship-the-fluid).
This project's own chem-base discussion has been assuming
convert-to-solid-first for concreteness, not because the alternative
was ruled out. Two concrete cases *do* resolve cleanly by direct
comparison rather than staying a matter of taste: `processing-unit`
above, and `chemical-science-pack` below.

### Chemical science pack: sulfur joins the bus (2026-08-09)

Same method as `processing-unit`, applied to `chemical-science-pack`
(`recipe/chemical-science-pack.json`: 2 `engine-unit` + 3
`advanced-circuit` + 1 `sulfur` → 2 packs) — per pack, that's 1.0
`engine-unit` + 1.5 `advanced-circuit` + 0.5 `sulfur`
(`relations/science_pack_ratios.md`'s `direct_ingredient_ratio`,
already held). Both `engine-unit` and `advanced-circuit` are already
produced/bussed at the main base (`layouts/scalable_chem_base.md`'s
"Electric engine unit" split, and "Red vs blue circuit" above) —
`sulfur` is the only ingredient that isn't.

| assembled at | what ships in | total units/pack |
|---|---|---|
| main base | 0.5 `sulfur` (solid) only — engine-unit and advanced-circuit already bussed there | **0.5** |
| chem-base | 1.5 `advanced-circuit` + 1.0 `engine-unit` (sulfur stays local) | **2.5** |

**Resolved: `chemical-science-pack` is assembled at the main base**,
importing `sulfur` as a new bus lane — a 5× smaller shipped-unit count
than the alternative, and unlike `processing-unit`'s `sulfuric-acid`
trickle, `sulfur` is a **solid**, so this doesn't even need a
fluid-wagon — an ordinary belt lane or wagon slot on the same rail
line already carrying `plastic-bar`/`battery` in from the chem-base
covers it. Confirms this project's own earlier instinct
(`layouts/scalable_chem_base.md`'s "chemical science pack" open item:
*"первая мысль возить sulfur на main bus"* — first thought was to ship
sulfur to the main bus) rather than overturning it.

### Iron vs copper: what the community actually reports (corrected)

An earlier version of this file claimed copper "consistently runs
equal-to-or-above iron" — that overstated what the sources actually
say, and is corrected here. The five named per-poster configs behind
the template above, in iron:copper lanes:

| poster | iron | copper |
|---|---|---|
| Rjskeet | 4 | 4 |
| astroshak | 8 | 8 |
| Saemj | 4 | 4 |
| CJ5Boss (KatherineOfSky) | 4 | 4 |
| Vanatteveldt (800 SPM target) | 8 | 6 |

Four of five run iron and copper **equal**; the one config with an
explicitly stated target output (Vanatteveldt, 800 science packs/min)
runs iron **above** copper, not below. None of the cited configs put
copper ahead of iron. A separate, lower-confidence forum comment
("one lane of green circuit boards equals 1 lane of iron plates and
1.5 lanes of copper plates" — unattributed in-thread, but this project
independently confirmed the exact figure via recipe data, see
`relations/bus_lane_ratios.md`) is real and correct at the
single-recipe level: circuits alone do pull more copper than iron.
But that per-recipe fact doesn't win out in the observed totals above,
most plausibly because steel pulls exclusively on iron (5:1, zero
copper — see below) while nothing on the copper side has an equivalent
lopsided sink. Whether copper ever overtakes iron in total bus lanes
depends on a specific base's relative steel-vs-circuit production
volume — not stated as a fixed rule by any source found, and not
something this project derives here since it needs a target output to
resolve (same caveat as bus width generally, above).

It does overtake for one concrete case this project *can* point to:
`low-density-structure` (rocket parts) pulls 2× more copper than
iron-equivalent (`relations/bus_lane_ratios.md`), matching a
community-cited rocket-construction figure where copper plates
slightly exceed iron plates overall. So "iron is the most-consumed
ingredient" holds for early/mid-game science-pack-driven templates
like the one above, but stops holding once rocket/space-content
production becomes a meaningful share of output — this is a
game-stage-dependent fact, not a fixed ranking.

### Mods change the ingredient list, not the method

A modded item set adds recipes/ingredients this exact template doesn't
know about — the fixed lane counts above stop applying, but the
*method* doesn't: pull the new recipe's ingredient/result amounts and
apply `formulas/recipe_ingredient_ratio.py` the same way
`bus_lane_ratios.md` did for vanilla. This is the concrete reason Hard
rule 3 rejects citing someone else's fixed total in the first place —
a hardcoded "24-32 belts" number silently stops being valid the moment
the recipe graph changes underneath it, while a ratio derived from
held primitives doesn't.

## Reserve for growth: the recipe for not having to rebuild

A specific, repeated failure mode in practice: under-provisioning bus
width up front, then having to tear out and rebuild one side to widen
it later. None of what follows is an engine rule — it's load-bearing
community convention, sourced the same way
`layouts/main_bus_consumer_layout.md`'s gap-width figures are: stated
as working knowledge from experienced players, not derived from
primitives.

### The margin: "take the width you think you'll need and double it"

Direct quote, forum user **kpreid**
(https://forums.factorio.com/viewtopic.php?t=120647): *"Take the
width you think you'll need and double it!"* — a concrete, named
rule of thumb for how much slack to reserve, not just "some." Paired
with **astroshak**'s complementary point in the same thread: *"don't
build more of the bus than you need at any one time"* — the margin is
reserved *space*, not built-and-idle belts; empty reserved tiles cost
nothing, a built-but-unused belt array still costs the initial
construction effort for no return yet.

A second, independent margin figure — for expansion space generally,
not specifically bus width (lower confidence, r/factorio, unattributed
username): a troubleshooting checklist for scaling a stuck factory
ends with *"What's the next step for your factory? How much space do
you think you need to build it? Multiply it by 4."* Same direction as
kpreid's 2× (reserve more than the naive estimate), but a different
multiplier for a different question (general next-build footprint, not
this section's specific bus-width margin) — cited separately rather
than merged into one number.

### Technique 1: lay out the full pattern in the reserved space, as ghosts

Follow the 4-belt-group + 2-tile-gap pattern from the start across the
*entire* doubled width, including lanes with nothing running through
them yet. Placing blueprint-ghost belts (not real belts) in reserved
lanes keeps the intended layout visible and prevents stray items from
accumulating there in the meantime, without spending the resources to
build belts nothing uses yet.

### Technique 2: build off one side only

**astroshak**: *"Building on one side of the bus"* leaves the other
side free to *"add more material, whatever type you want, to the
other side"* later. Building both sides symmetrically looks efficient
short-term, but the moment the bus needs to widen, the side actually
built on requires crossing the live bus to reach from the far side —
friction this project has already seen the shape of elsewhere (e.g.
`mechanics/construction-robot-job-assignment.md`'s no-reassignment
behavior: once committed, undoing a placement decision is never free).
One-sided building trades early density for never having to relocate
a working factory row. The freed side isn't only for belt lanes,
either — it doubles as space for train unloading, fluid pipes, or a
full redesign later.

### Technique 3: inject mid-bus, don't just extend from the start

If a new item needs to join the bus partway along its length rather
than at the very start, **HadesSupreme**: *"inject at any place in a
bus, simply have a splitter send materials down both ways"* — a
splitter at the injection point feeding both directions avoids routing
the new supply all the way back to the bus's origin.

### The counter-view: some experienced players don't pre-reserve at all

Not universal advice — **ChoMar**, same thread as kpreid/astroshak:
*"The Thing about the Bus is: Its easy to expand,"* framing the bus as
inherently adaptable rather than something requiring proactive
over-sizing; **PunkSkeleton** (a different thread) similarly reports
not running a fixed belt count, just adding lanes as needed with gaps
left for more. The double-the-width convention and the "it's easy to
expand anyway" view aren't contradictory so much as different risk
tolerances — reserving up front avoids ever hitting the rebuild case
this section opened with, at the cost of committing more space early
than might end up used.

### The bus is early/mid-game infrastructure, not a permanent structure

**DeadMG**, same thread: *"by the time this becomes a serious problem,
you should be training ores anyway"* — pushing bus-widening past a
certain scale is itself a signal to move to train-fed delivery
(`glossary/canonical/train-base.md`) instead of continuing to expand
belt width. Relatedly (lower-confidence source — a blog aggregator,
not forum/wiki, flagged accordingly): if a `city-block` grid
(`layouts/city_block_grid.md`) is the eventual target architecture,
reserving that grid's footprint as empty space early — even while
still running a plain bus — avoids needing to demolish bus-era
construction when transitioning later.

Sources: https://wiki.factorio.com/tutorial:main_bus (official Wube
tutorial — grouping, spacing, distance-from-bus, item-ordering
figures); https://forums.factorio.com/viewtopic.php?t=64355,
https://forums.factorio.com/viewtopic.php?t=100199, and
https://forums.factorio.com/viewtopic.php?t=120647 (community forum —
per-item lane configs, expansion-margin and injection techniques,
named per quote above); https://forums.factorio.com/viewtopic.php?t=105184,
https://forums.factorio.com/viewtopic.php?t=45799, and
https://forums.factorio.com/viewtopic.php?t=60758 (community forum —
red/blue circuit and chemistry-fluid bus placement, named per quote in
"Red vs blue circuit" and "Fluids and chemistry intermediates" above)
Verified: 2026-08-09

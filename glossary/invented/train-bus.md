# train bus (railbus)

The rail analog of a [main bus](../canonical/main-bus.md): instead of
parallel belts multiple blocks tap into along their length, one or a
few standardized rail lines carry trains that multiple stations pick
up from and drop off onto — community term "railbus," not this
project's own coinage, formalized here because this project's own
outpost connections turned out to need the contrast.

Community usage, not an official Wube term — "railbus" describes
trains moving items almost the way a main bus's belts do, each
production submodule tapping the shared line for its next subproduct;
several independent community sources describe this as an emerging
"meta" for very large bases. Directly attributable use of "train bus"
as a term (not just this project's own coinage): r/factorio thread
`gnolui` ("Where do I put the main bus if I'm trying a city block
base?") — **Hoshi711**: *"most city blocks use a train bus"* — a named
poster using the exact term, upgrading this beyond the aggregate/
no-single-thread citation this entry started with.

A working railbus needs stations sized to buffer input/output against
train travel time, and — the recurring practical complaint across
sources — standardized train length and one agreed signaling strategy,
since every station on a shared line has to interoperate with every
other one, the same "changing it later is expensive" property
`layouts/main_bus.md`'s reserve-for-growth section already documents
for belts.

## Train bus vs. train-base: not the same claim

Easy to conflate with [train-base](../canonical/train-base.md), but
they answer different questions. **Train-base** is about *discrete
delivery* — trains instead of continuous belt flow between modules,
with no requirement that those routes share a line (`train-base.md`'s
own cited example, *"squares only connected via 1-8 trains,"* describes
point-to-point routes, not one shared bus). **Train bus** is
specifically about *sharing one line* the way a main bus shares one set
of belts — multiple stations, one continuous rail backbone, trains
picking up/dropping off along it like belt taps.

**What this project actually builds is train-base, not train-bus**:
every rail connection so far (`layouts/scalable_chem_base.md`'s rail
station, `layouts/scalable_main_base.md`'s remote labs pack train,
`layouts/nuclear_base.md`'s sulfuric-acid run) is a dedicated
point-to-point route between exactly two stations, not a shared line
multiple outposts tap into. Stated plainly rather than implied — this
project hasn't designed a true train bus anywhere yet, and doing so
would need the standardized-train-length/signaling decisions above,
which none of the point-to-point routes required.

## Vanilla 2.0 tools that would support building one

Not something this project has used yet (no train-bus layout exists
here to apply it to), but worth recording since it directly answers
part of the "signaling strategy" gap above: Factorio 2.0 added
built-in tools that reduce exactly the per-item-type routing
complexity a real train-bus needs, without a mod.

**Generic interrupts with wildcard signals** (FFF #395, "Generic
interrupts and Train stop priority"): a single interrupt using a
wildcard signal (*"Any item," "Any Fluid," "Any Fuel," "Any Signal"*)
checks its condition *"against each item in the cargo, and the first
one that passes will be the 'passing item'"* for that train, then
substitutes that item into the interrupt's target station name and
wait conditions. Concretely: one interrupt reading *"if Any item, go
to `[item name] dropoff`"* handles iron plates, copper wire, batteries,
etc. automatically — no separate hand-built interrupt per cargo type,
which is exactly the kind of per-stop manual configuration that would
otherwise not scale as a train-bus grows more tap points.

**Train stop priority** (same FFF #395): a 0-255 value (default 50, max
255 reserved for manual player dispatch and "no path"/"destination
full" emergencies) that does two things at once — trains prefer
higher-priority stops as destinations, *and* trains already waiting at
higher-priority stops get dispatched first. This is a built-in
mechanism for exactly the "one agreed signaling/coordination strategy"
multiple stations on a shared line need, without hand-rolled circuit
logic.

**Same-named stops** (FFF #403, "Train stops 2.0"): multiple physical
stations can share one name; a train routed to that name picks *"the
existing stop with the lowest train limit"* first — a safety-first
default for distributing trains across several physical taps on what
is effectively one logical line/destination, relevant to how a
train-bus's multiple pickup/dropoff points along a shared line might
be named consistently.

**Honest limits of this as a source**: FFF #403 was checked directly
for train-bus-specific guidance and explicitly does *not* address
shared-line/multi-station-tap designs or train-length standardization
— these are this project's own inference that the interrupt/priority
tools *would help* with the train-bus problem, not Wube stating they
built these features for that purpose. Whether they're actually
sufficient (vs. still needing a mod like Logistic Train Network for
genuine on-demand dispatch) is untested — no train-bus layout exists
in this project yet to find out.

**Why trains fill the role a bus can't, for city-blocks**: same
`gnolui` thread, **burenning** — *"main bus and city block designs
don't mesh together particularly well... every single city block
design has to be adjacent to the bus, and the majority of the bus will
be wasted belt buffers as the products aren't used by the adjacent
blocks. Use trains, transport drones, or logistics bots..."* — a
mechanical reason (physical adjacency requirement), not just stated
preference, for why a train-bus-shaped pattern tends to replace a
belt-bus once a base goes city-block.

Sources: community forum/discussion aggregate (railbus terminology and
practical tradeoffs); r/factorio thread `gnolui` ("Where do I put the
main bus if I'm trying a city block base?", 2020) — Hoshi711 (named
"train bus" usage), burenning (mechanical rationale) — treat both at
the same community-tier confidence bar as other lower-confidence
citations in this project, e.g.
`layouts/main_bus_consumer_layout.md`'s practical gap-width figures.
Official, primary-source tier: factorio.com/blog/post/fff-395
("Generic interrupts and Train stop priority") and
factorio.com/blog/post/fff-403 ("Train stops 2.0").
Verified: 2026-08-09

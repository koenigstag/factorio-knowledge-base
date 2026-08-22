# Inserter belt-lane placement

A belt has two lanes (left/right — see
[glossary/canonical/lane-balancer.md](../glossary/canonical/lane-balancer.md)).
Which lane an inserter's dropped item lands on depends on the
inserter's orientation *relative to the belt*, not on a single fixed
rule:

- **Perpendicular** (the common case — inserter facing across the
  belt, e.g. feeding a belt from the side): item lands on the **far
  lane**, the lane on the side opposite the inserter, never the near
  lane. Not configurable in vanilla (a mod, "Side Inserters", exists
  specifically to add near-side placement, which isn't otherwise
  possible).
- **Same/opposite orientation as the belt** (inserter facing along the
  belt's own travel axis, parallel to it): item lands on the belt's
  **right-hand lane, relative to the belt's own direction of travel** —
  independent of which side the inserter physically sits on. E.g. a
  belt flowing West lands items on its own right hand facing West,
  which is the North/"top" lane; a belt flowing East lands on the
  South/"bottom" lane. Author-confirmed against in-game testing,
  matching the wiki's own phrasing for this case.
- **Curves**: always the far lane, same as the perpendicular case.

Pickup follows different rules than placement: perpendicular to the
belt, an inserter prefers the **near** lane, falling back to the far
lane only if the near lane is empty (near-lane pickup is also slightly
faster). Same/opposite orientation or on a curve, it prefers the
**left** lane relative to the belt's own direction of travel, falling
back to the right lane if the left is empty.

## Practical consequence

Two rows of machines flanking a shared center belt from opposite sides,
perpendicular to it (e.g. the furnace modules in
[layouts/smelter_module_ports.md](../layouts/smelter_module_ports.md)
and [blueprints/curated/earlygame/iron-gear-tileable.md](../blueprints/curated/earlygame/iron-gear-tileable.md)),
each drop onto the *far* lane from their own side — i.e. each row fills
the lane closer to the *other* row, not its own. With equal machine
counts on both rows, both lanes still end up evenly filled; which
physical lane ends up "row A's" vs "row B's" is swapped from what a
naive near-side assumption would predict, but the overall lane balance
outcome is the same.

Source: https://forums.factorio.com/viewtopic.php?t=26645 ("Why do
inserters prefer far side of the belt?"),
https://forums.factorio.com/viewtopic.php?t=62256 ("Inserters Belt
Placement location"), and https://forums.factorio.com/viewtopic.php?t=49059
("Consistent, relative lane-placement by inserters") — quoting the
wiki's Inserters page: "Inserters place the item on the furthest lane.
If a belt is in the same orientation as the inserter, the item will be
placed on the right-hand lane, from the belt's perspective. In curves
the inserter always places on the far side." / "If the belt is
perpendicular to the inserter, inserters prefer taking items from the
nearest lane. If the nearest lane is empty, the inserter will take
from the far lane. If the belt is the same/opposite orientation of the
inserter or a curve, the inserter prefers taking from the left lane,
from the belt's perspective. If the left lane is empty it will take
from the right lane." The same/opposite-orientation rule was
independently confirmed by the project owner's own in-game testing on
a horizontal belt.
Verified: 2026-08-09

# belt side-loading

Feeding a belt from the side (perpendicular to its direction of
travel) rather than end-to-end (in-line) or through a `splitter`.
Commonly used to merge one belt into another without spending a
splitter, or to have an inserter/underground-belt-exit push items
directly onto an existing belt's flow.

Mechanically:
- Side-loaded items get forced into whatever gaps already exist on
  the receiving belt — density temporarily compresses at the merge
  point, then relaxes back to normal further along.
- On an underground belt specifically, only the half of the tile with
  visible belt graphics accepts side-loaded input; the tunnel-entrance
  half does not — so a side-load onto an underground belt exit
  reliably reaches only one of the two lanes, not both.
- Interacts directly with `lane balancer` (see
  `glossary/canonical/lane-balancer.md`): side-loading to fill *both*
  lanes of the receiving belt doesn't work reliably unless the lane
  being fed from is already running fully compressed — otherwise the
  second lane doesn't get "topped up" the way a proper lane balancer
  would.

**Confidence caveat**: the general mechanism above is corroborated by
multiple independent sources, but the more precise numeric details
found this session (exact compression distances, a reference to FFF
#231 "Belt compression") trace back to 0.16-era discussions — a very
old version. Nothing found this session confirms or denies whether
those specific numbers still hold in 2.0; treat the mechanism as
solid and the fine-grained numbers as unconfirmed for the current
version until checked separately.

Source: https://forums.factorio.com/viewtopic.php?t=79064 (underground belt side-loading), general community usage
Verified: 2026-08-06

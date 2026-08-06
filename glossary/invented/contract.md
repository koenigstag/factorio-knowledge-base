# contract

An abstract interface spec: a set of [[port]]s (resource, side,
offset, direction) plus throughput as a reference to a function in
`formulas/`, without being tied to a concrete implementation. Meant to
be created only once ≥2 interchangeable tiers implementing the same
slot exist ("extract when duplicated", not upfront).

Coined during initial architecture discussion.

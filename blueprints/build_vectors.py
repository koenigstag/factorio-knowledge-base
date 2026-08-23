"""Reduce a blueprint's entities to a flat list of directed vectors
(belt_runs, inserters, underground tunnels, splitters) instead of a
tile-by-tile adjacency list. Written to stop mistakes from manual
belt1->belt2->beltN tracing (see CLAUDE.md hard rule 6's inserter-
directionality history for why that manual tracing is error-prone).

Usage: python blueprints/build_vectors.py <blueprint.txt> <out.vectors.json>

Mirrored in pages/index.html's inline JS (a client-side port used for the
`?source=` query-string path, so a blueprint string can be vectorized
in-browser without a server round-trip) - keep the two in sync if the
geometry or merge rules here change.
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codec import decode_blueprint_string

# Geometry sourced from datapacks/dump/vanilla/inserter/*.json (pickup_position/insert_position,
# North/direction=0 frame, unrotated). Cross-check against mechanics/inserters-directionality.md.
INSERTER_GEOMETRY = {
    "inserter": {"pickup": (0, -1), "insert": (0, 1.2)},
    "fast-inserter": {"pickup": (0, -1), "insert": (0, 1.2)},
    "bulk-inserter": {"pickup": (0, -1), "insert": (0, 1.2)},
    "stack-inserter": {"pickup": (0, -1), "insert": (0, 1.2)},
    "burner-inserter": {"pickup": (0, -1), "insert": (0, 1.2)},
    "long-handed-inserter": {"pickup": (0, -2), "insert": (0, 2.2)},
}

BELT_NAMES = {"transport-belt", "fast-transport-belt", "express-transport-belt", "turbo-transport-belt"}
UNDERGROUND_NAMES = {"underground-belt", "fast-underground-belt", "express-underground-belt", "turbo-underground-belt"}
# max_distance per relations/underground_belt_crossing_gap.md
UNDERGROUND_MAX_DISTANCE = {
    "underground-belt": 5,
    "fast-underground-belt": 7,
    "express-underground-belt": 9,
    "turbo-underground-belt": 11,
}

DIR_UNIT = {0: (0, -1), 4: (1, 0), 8: (0, 1), 12: (-1, 0)}

# Factorio changed the `direction` field's own scale at 2.0.0 (FFF #377):
# pre-2.0, an 8-value enum with cardinals spaced 2 apart (N=0,E=2,S=4,W=6);
# 2.0+, a 16-value enum with cardinals spaced 4 apart (N=0,E=4,S=8,W=12) -
# same cardinal compass directions, just double the raw integer. A
# blueprint's `version` field (packed uint64: main<<48 | major<<32 |
# minor<<16 | developer) says which scale its own entities were written
# in; this project's codec.py deliberately does NOT rescale on decode (it
# promises a faithful, format-preserving transcode - see its own
# round-trip guarantee), so any caller that computes geometry from
# `direction` needs to rescale pre-2.0 values itself first.
#
# Confirmed against a real pre-2.0 blueprint (version 0.17.79.0) pasted
# into this project: un-rescaled, several inserters and belts had
# non-cardinal-looking direction values that were first (wrongly)
# investigated as the unrelated, genuinely-real pre-2.0.54 diagonal-
# inserter placement bug (see mechanics/inserters-directionality.md) -
# rescaling by this exact factor turned every single one into a clean
# cardinal with zero remaining ambiguity, independently matching a
# constraint-satisfaction resolution worked out by hand beforehand.
# Cross-checked against github.com/FactoryGameFan/factorio-blueprint-
# editor's own Blueprint.ts, which does precisely this: `dirMult = pre_2_0
# ? 2 : 1` applied to every entity's raw `direction` on import.
FACTORIO_2_0_0 = (2, 0, 0)


def unpack_factorio_version(version_int):
    """(main, major, minor) from a blueprint's packed `version` uint64.
    Drops the low 16 bits (developer/build number) - not needed for the
    pre/post-2.0 comparison this exists for."""
    return (version_int >> 48, (version_int >> 32) & 0xFFFF, (version_int >> 16) & 0xFFFF)


def normalize_pre_2_0_directions(entities, version_int):
    """Doubles every entity's `direction` field in place if `version_int`
    indicates a pre-2.0.0 blueprint. No-op (including when `version` is
    absent) for 2.0+ blueprints, where direction is already in the modern
    scale. Entities with no `direction` field are untouched either way -
    Factorio omits the field entirely for direction=0 in both eras, and
    0*2 is still 0, so there's nothing to change even if it were present."""
    if version_int is None:
        return
    if unpack_factorio_version(version_int) >= FACTORIO_2_0_0:
        return
    for e in entities:
        if "direction" in e:
            e["direction"] = e["direction"] * 2


def rotate(vec, direction):
    x, y = vec
    if direction == 0:
        return (x, y)
    if direction == 4:
        return (-y, x)
    if direction == 8:
        return (-x, -y)
    if direction == 12:
        return (y, -x)
    raise ValueError(f"unsupported direction {direction}")


def snap_to_cardinal(direction):
    """Floor a 16-way direction value (0-15) down to its enclosing cardinal
    (0/4/8/12). Only meant for inserters: per mechanics/inserters-
    directionality.md, the game engine never allows a real inserter to be
    placed facing a non-cardinal direction - a blueprint carrying one is
    either an old save re-exported from before the 2.0.47-2.0.53 diagonal-
    inserter bug was fixed in 2.0.54, or a hand-edited attempt at the same
    dead exploit. Confirmed from the primary source (the bug report) is
    only that current Factorio imports such a blueprint "as a straight
    inserter" - NOT which specific cardinal it snaps to, so floor-to-
    nearest-lower-cardinal here is this project's own deterministic
    choice for producing a plotable vector, not a verified replica of the
    engine's exact tie-breaking rule. Flag it (see build_inserter_vectors)
    rather than presenting it as equivalent to a real cardinal placement."""
    return (direction % 16) - (direction % 16) % 4


def build_inserter_vectors(entities):
    out = []
    for e in entities:
        geo = INSERTER_GEOMETRY.get(e["name"])
        if geo is None:
            continue
        raw_d = e.get("direction", 0)
        d = snap_to_cardinal(raw_d)
        px, py = rotate(geo["pickup"], d)
        ix, iy = rotate(geo["insert"], d)
        pos = e["position"]
        vec = {
            "entity_numbers": [e["entity_number"]],
            "entity": e["name"],
            "from": [round(pos["x"] + px, 3), round(pos["y"] + py, 3)],
            "to": [round(pos["x"] + ix, 3), round(pos["y"] + iy, 3)],
        }
        if d != raw_d:
            vec["note"] = (
                f"non-cardinal direction {raw_d} in source data - the game engine "
                f"does not allow diagonal inserter placement (mechanics/"
                f"inserters-directionality.md); snapped to {d} for this vector, "
                f"exact in-game snap behavior unconfirmed"
            )
        out.append(vec)
    return out


def build_belt_runs(entities):
    by_name = {}
    for e in entities:
        if e["name"] not in BELT_NAMES:
            continue
        by_name.setdefault(e["name"], {})[(e["position"]["x"], e["position"]["y"])] = e

    out = []
    for name, tiles in by_name.items():
        # index by exact position for successor lookup
        has_predecessor = set()
        for pos, e in tiles.items():
            d = e.get("direction", 0)
            dx, dy = DIR_UNIT[d]
            nxt = (pos[0] + dx, pos[1] + dy)
            succ = tiles.get(nxt)
            if succ is not None and succ.get("direction", 0) == d:
                has_predecessor.add(nxt)

        for pos, e in tiles.items():
            if pos in has_predecessor:
                continue  # not a run start
            # walk the chain
            chain = [e]
            cur_pos = pos
            d = e.get("direction", 0)
            while True:
                dx, dy = DIR_UNIT[d]
                nxt = (cur_pos[0] + dx, cur_pos[1] + dy)
                succ = tiles.get(nxt)
                if succ is None or succ.get("direction", 0) != d:
                    break
                chain.append(succ)
                cur_pos = nxt
                d = succ.get("direction", 0)
            start = chain[0]["position"]
            end = chain[-1]["position"]
            end_d = chain[-1].get("direction", 0)
            edx, edy = DIR_UNIT[end_d]
            out.append({
                "entity_numbers": [c["entity_number"] for c in chain],
                "entity": name,
                "from": [start["x"], start["y"]],
                "to": [end["x"] + edx, end["y"] + edy],  # end of the LAST tile's own output edge
                "direction": chain[0].get("direction", 0),
                "length": len(chain),
            })
    return out


def build_underground_vectors(entities):
    """Pairing rules: mechanics/underground-belt-pairing.md - same-tier only,
    nearest-match with no skip-over, unpaired entrance = dead-end sink."""
    out = []
    for name in UNDERGROUND_NAMES:
        candidates = [e for e in entities if e["name"] == name]
        inputs = [e for e in candidates if e.get("type") == "input"]
        outputs = [e for e in candidates if e.get("type") == "output"]
        max_dist = UNDERGROUND_MAX_DISTANCE[name]
        claimed_outputs = set()
        # sort inputs for determinism; ties broken by position
        for inp in sorted(inputs, key=lambda e: (e["position"]["x"], e["position"]["y"])):
            d = inp.get("direction", 0)
            dx, dy = DIR_UNIT[d]
            pos = inp["position"]
            best = None
            best_dist = None
            for out_e in outputs:
                if out_e["entity_number"] in claimed_outputs:
                    continue
                if out_e.get("direction", 0) != d:
                    continue
                opos = out_e["position"]
                # must lie exactly along the direction ray
                ddx = opos["x"] - pos["x"]
                ddy = opos["y"] - pos["y"]
                if dx != 0:
                    if ddy != 0 or ddx * dx <= 0:
                        continue
                    dist = ddx * dx
                else:
                    if ddx != 0 or ddy * dy <= 0:
                        continue
                    dist = ddy * dy
                if dist > max_dist:
                    continue
                if best is None or dist < best_dist:
                    best = out_e
                    best_dist = dist
            if best is not None:
                claimed_outputs.add(best["entity_number"])
                out.append({
                    "entity_numbers": [inp["entity_number"], best["entity_number"]],
                    "entity": f"{name}-tunnel",
                    "from": [pos["x"], pos["y"]],
                    "to": [best["position"]["x"], best["position"]["y"]],
                    "interactable": False,
                })
            else:
                out.append({
                    "entity_numbers": [inp["entity_number"]],
                    "entity": f"{name}-dead-end",
                    "from": [pos["x"], pos["y"]],
                    "to": None,
                    "interactable": False,
                    "note": "no matching output within max_distance - sink, not a parse error",
                })
    return out


def build_splitter_nodes(entities):
    """input_priority/output_priority/filter are omitted from the blueprint
    entity entirely when unset (wiki.factorio.com/Blueprint_string_format),
    not present with a "none" default - so their absence IS the fact that
    this splitter is an unconfigured balancer, not just missing data.
    Per mechanics/splitter-priority.md (sourced from the wiki's belt
    transport system page): no priority set means items split evenly
    between both outputs, a fully deterministic behavior - only a splitter
    that actually sets one of these three is genuinely unresolved from
    geometry alone (routing then depends on runtime backpressure too)."""
    out = []
    for e in entities:
        if e["name"] not in {"splitter", "fast-splitter", "express-splitter", "turbo-splitter"}:
            continue
        input_priority = e.get("input_priority")
        output_priority = e.get("output_priority")
        item_filter = e.get("filter")
        configured = input_priority is not None or output_priority is not None or item_filter is not None
        if configured:
            note = "priority/filter configured - routing depends on that plus runtime backpressure, not fixed geometry"
        else:
            note = "balancer - no priority/filter set, splits input evenly between both outputs (mechanics/splitter-priority.md)"
        out.append({
            "entity_numbers": [e["entity_number"]],
            "entity": e["name"],
            "position": [e["position"]["x"], e["position"]["y"]],
            "direction": e.get("direction", 0),
            "input_priority": input_priority,
            "output_priority": output_priority,
            "filter": item_filter,
            "configured": configured,
            "note": note,
        })
    return out


def vectorize(bp: dict) -> dict:
    """bp is a decoded blueprint dict (the `blueprint` value, not the
    outer wrapper) - same shape `codec.decode_blueprint_string` returns
    for a lone blueprint, or one entry from `codec.walk_blueprints` for
    a book."""
    entities = bp["entities"]
    normalize_pre_2_0_directions(entities, bp.get("version"))
    return {
        "label": bp.get("label"),
        "entity_count": len(entities),
        "inserters": build_inserter_vectors(entities),
        "belt_runs": build_belt_runs(entities),
        "underground": build_underground_vectors(entities),
        "splitters": build_splitter_nodes(entities),
    }


def main(path, out_path):
    with open(path) as f:
        bp_str = f.read().strip()
    data = decode_blueprint_string(bp_str)
    bp = data["blueprint"]
    result = vectorize(bp)
    with open(out_path, "w") as f:
        json.dump(result, f, indent=1)
    print(f"wrote {out_path}")
    print(f"inserters={len(result['inserters'])} belt_runs={len(result['belt_runs'])} "
          f"underground={len(result['underground'])} splitters={len(result['splitters'])}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

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


def build_inserter_vectors(entities):
    out = []
    for e in entities:
        geo = INSERTER_GEOMETRY.get(e["name"])
        if geo is None:
            continue
        d = e.get("direction", 0)
        px, py = rotate(geo["pickup"], d)
        ix, iy = rotate(geo["insert"], d)
        pos = e["position"]
        out.append({
            "entity_numbers": [e["entity_number"]],
            "entity": e["name"],
            "from": [round(pos["x"] + px, 3), round(pos["y"] + py, 3)],
            "to": [round(pos["x"] + ix, 3), round(pos["y"] + iy, 3)],
        })
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
    out = []
    for e in entities:
        if e["name"] not in {"splitter", "fast-splitter", "express-splitter", "turbo-splitter"}:
            continue
        out.append({
            "entity_numbers": [e["entity_number"]],
            "entity": e["name"],
            "position": [e["position"]["x"], e["position"]["y"]],
            "direction": e.get("direction", 0),
            "note": "unresolved junction - routing depends on priority/filter settings, not fixed geometry",
        })
    return out


def vectorize(bp: dict) -> dict:
    """bp is a decoded blueprint dict (the `blueprint` value, not the
    outer wrapper) - same shape `codec.decode_blueprint_string` returns
    for a lone blueprint, or one entry from `codec.walk_blueprints` for
    a book."""
    entities = bp["entities"]
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

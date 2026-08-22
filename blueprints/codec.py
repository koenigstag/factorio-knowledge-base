import base64
import json
import zlib


def decode_blueprint_string(blueprint_string: str) -> dict:
    """Decode a Factorio blueprint/blueprint-book export string into its
    underlying JSON structure. Format is Factorio's own (not specific to
    any hosting site): a version byte (currently always "0") followed by
    base64-encoded, zlib-deflated JSON.
    """
    payload = blueprint_string[1:]
    raw = base64.b64decode(payload)
    decompressed = zlib.decompress(raw)
    return json.loads(decompressed)


def encode_blueprint_dict(data: dict, version: str = "0") -> str:
    """Inverse of decode_blueprint_string: JSON -> zlib -> base64,
    prefixed with the version byte, ready to paste back into the game.
    Round-trips decode_blueprint_string(encode_blueprint_dict(x)) == x,
    but the string itself won't be byte-identical to an original capture
    (compression level / key order aren't guaranteed to match).
    """
    payload = json.dumps(data, separators=(",", ":")).encode("utf-8")
    compressed = zlib.compress(payload, level=9)
    return version + base64.b64encode(compressed).decode("ascii")


def walk_blueprints(node: dict):
    """Yield every individual `blueprint` dict inside a decoded
    structure, recursing into `blueprint_book.blueprints` - handles a
    lone blueprint, a book, or nested books-of-books uniformly.
    """
    if "blueprint" in node:
        yield node["blueprint"]
    if "blueprint_book" in node:
        for child in node["blueprint_book"].get("blueprints", []):
            yield from walk_blueprints(child)


def entity_bounding_box(entities: list, names: set = None) -> dict:
    """Min/max x/y among a blueprint's `entities` list, optionally
    restricted to a subset of prototype names (e.g. rail-only). Returns
    None if no matching entities are present. Positions are in the
    blueprint's own local coordinate frame (tile units), as used
    throughout layouts/city_block_grid.md's rail-spacing cross-check.
    """
    matching = [e for e in entities if names is None or e["name"] in names]
    if not matching:
        return None
    xs = [e["position"]["x"] for e in matching]
    ys = [e["position"]["y"] for e in matching]
    return {"x_min": min(xs), "x_max": max(xs), "y_min": min(ys), "y_max": max(ys)}


BELT_PORT_TYPES = {
    "transport-belt", "fast-transport-belt", "express-transport-belt",
    "underground-belt", "fast-underground-belt", "express-underground-belt",
    "splitter", "fast-splitter", "express-splitter",
}

# 16-direction encoding (0=N, 4=E, 8=S, 12=W - cardinals spaced 4 apart,
# confirmed in UNITS.md's "pipe_connections.direction" note). Per edge,
# the direction a belt needs to face to be flowing INTO the schema
# (import) vs OUT of it (export).
_INWARD_DIRECTION = {"x_min": 4, "x_max": 12, "y_min": 8, "y_max": 0}
_OUTWARD_DIRECTION = {"x_min": 12, "x_max": 4, "y_min": 0, "y_max": 8}


def classify_edge_ports(entities: list, bbox: dict) -> dict:
    """Classify belt/underground-belt/splitter entities sitting exactly
    on a blueprint's bounding-box edge as import or export candidates,
    per the project owner's own two-rule heuristic (not an official
    Factorio concept - see blueprints/README.md "Import/export port
    heuristic"): a belt AT the edge coordinate, facing INTO the schema,
    is an import candidate (material entering from whatever connects
    outside); a belt AT the edge, facing OUT of the schema, is an
    export candidate. A belt that sits at the edge coordinate but faces
    parallel to that edge (perpendicular to the crossing axis) is
    neither - it doesn't cross the boundary at all, so it's unrelated
    internal routing that happens to share the coordinate, not a port.

    Only checks entities whose `name` is in BELT_PORT_TYPES - this
    rule is specifically about belts/underground-belts/splitters, not
    e.g. inserters or pipes.

    Returns {"import": [...], "export": [...]}; each entry is the
    original entity dict plus an "edge" key (which of x_min/x_max/
    y_min/y_max it was matched against - a corner tile can appear
    under two edges if it qualifies for both independently).
    """
    result = {"import": [], "export": []}
    for e in entities:
        if e["name"] not in BELT_PORT_TYPES:
            continue
        direction = e.get("direction", 0)
        x, y = e["position"]["x"], e["position"]["y"]
        for edge, coord in (("x_min", x), ("x_max", x), ("y_min", y), ("y_max", y)):
            if coord != bbox[edge]:
                continue
            if direction == _INWARD_DIRECTION[edge]:
                result["import"].append({**e, "edge": edge})
            elif direction == _OUTWARD_DIRECTION[edge]:
                result["export"].append({**e, "edge": edge})
    return result

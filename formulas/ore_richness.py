def ore_richness_multiplier(distance_tiles):
    """Vanilla ore-patch richness multiplier as a function of distance from
    the map origin (0,0), from the shared `autoplace.richness_expression`
    pattern found on iron-ore/copper-ore/uranium-ore/stone/coal:
    max((1000 + distance) / 2600, 1).

    Flat at 1.0 for distance <= 1600 tiles, then grows linearly. Doesn't
    include the per-resource `control:<name>:richness` map-generator
    slider, which multiplies this result further and defaults to 1.
    """
    return max((1000 + distance_tiles) / 2600, 1)

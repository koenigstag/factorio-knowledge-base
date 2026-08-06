def train_max_speed(locomotive_max_speed, fuel_top_speed_multiplier=1.0):
    """Max train speed in tiles/tick.

    locomotive_max_speed: locomotive.max_speed (e.g. 1.2 for the
        vanilla locomotive) - a data.raw field, not an engine constant.
    fuel_top_speed_multiplier: the fuel item's fuel_top_speed_multiplier
        (datapacks/dump/vanilla/item/*.json). Defaults to 1.0 - most
        fuels (coal, wood) have no such field at all, meaning no bonus.
    """
    return locomotive_max_speed * fuel_top_speed_multiplier

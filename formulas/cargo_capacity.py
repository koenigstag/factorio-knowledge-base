import math


def cargo_capacity(slots, stack_size, item_weight=None, weight_limit=None):
    """Max count of one item that fits in a container, given its slot count
    and (optionally) a total weight limit - whichever binds first.

    slots: container's inventory_size (e.g. cargo-wagon.inventory_size=40,
        rocket-silo-rocket.inventory_size=20).
    stack_size: the item's own stack_size (datapacks/dump/vanilla/item/*.json).
    item_weight / weight_limit: both required together to apply a weight
        cap (e.g. utility-constants.rocket_lift_weight for rockets); leave
        both None for containers with no weight limit at all (e.g.
        cargo-wagon - checked, it has no cargo weight cap field, only its
        own vehicle weight for train physics).
    """
    slot_limited = slots * stack_size
    if item_weight is None or weight_limit is None:
        return slot_limited
    weight_limited = math.floor(weight_limit / item_weight)
    return min(slot_limited, weight_limited)

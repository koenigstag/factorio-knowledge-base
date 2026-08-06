def recycler_ingredient_amount(original_amount: float, return_fraction: float = 0.25) -> float:
    """Expected amount of an ingredient returned by recycling an item,
    given that ingredient's amount in the item's normal crafting recipe.

    return_fraction=0.25 is the recycling category's fixed return rate —
    confirmed directly against 3 recycling recipes in
    datapacks/dump/vanilla/recipe/ (iron-plate-recycling,
    iron-gear-wheel-recycling, electronic-circuit-recycling all give
    exactly 25% of each original ingredient amount).
    """
    return original_amount * return_fraction

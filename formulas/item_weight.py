import math


def item_weight(has_recipe, default_item_weight, recipe_weight, product_count,
                 recipe_supports_productivity, rocket_lift_weight, stack_size,
                 only_in_cursor_and_spawnable=False, ingredient_to_weight_coefficient=0.5):
    """Weight the game assigns an item that has no explicit `weight` field,
    per lua-api.factorio.com/latest/auxiliary/item-weight.html.

    recipe_weight: sum over the item's (first-sorted) recipe's ingredients of
        item_weight(ingredient) * count for item ingredients, plus
        fluid_amount * 100 for fluid ingredients - a separate, recursive
        computation over the recipe graph, not part of this function.
    product_count: sum of expected item-product counts of that recipe
        (fluid products skipped).
    recipe_supports_productivity: the recipe's `allow_productivity` field.
    rocket_lift_weight / stack_size: datapacks/dump/vanilla/utility-constants/default.json
        and the item's own `stack_size`.
    """
    if only_in_cursor_and_spawnable:
        return 0
    if not has_recipe:
        return default_item_weight
    if recipe_weight == 0:
        return default_item_weight
    if product_count == 0:
        return default_item_weight

    intermediate_result = (recipe_weight / product_count) * ingredient_to_weight_coefficient

    if not recipe_supports_productivity:
        simple_result = rocket_lift_weight / stack_size
        if simple_result >= intermediate_result:
            return simple_result

    stack_amount = rocket_lift_weight / intermediate_result / stack_size
    if stack_amount <= 1:
        return intermediate_result
    return rocket_lift_weight / math.floor(stack_amount) / stack_size

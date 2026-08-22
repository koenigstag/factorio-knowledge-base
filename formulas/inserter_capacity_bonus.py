def nonstack_items_per_cycle(stack_size_bonus_total: float) -> float:
    """items_per_cycle for inserter/burner-inserter/long-handed-inserter/fast-inserter.

    stack_size_bonus_total: sum of "inserter-stack-size-bonus" effect
        modifiers across researched technologies (see
        datapacks/dump/vanilla/technology/inserter-capacity-bonus-*.json).
        Base grab size is 1 item/cycle (see mechanics/inserters-throughput.md).
    """
    return 1 + stack_size_bonus_total


def bulk_items_per_cycle(capacity_bonus_total: float) -> float:
    """items_per_cycle for bulk-inserter.

    capacity_bonus_total: sum of "bulk-inserter-capacity-bonus" effect
        modifiers across researched technologies. Base grab size is 2
        items/cycle (implicit engine default for any bulk:true inserter).
    """
    return 2 + capacity_bonus_total


def stack_items_per_cycle(capacity_bonus_total: float) -> float:
    """items_per_cycle for stack-inserter.

    capacity_bonus_total: same "bulk-inserter-capacity-bonus" accumulator
        as bulk_items_per_cycle - stack-inserter is also bulk:true, so it
        shares the same research bonus. Base grab size is 6 items/cycle
        (2 implicit bulk base + inserter.stack_size_bonus=4, see
        mechanics/inserters-throughput.md).
    """
    return 6 + capacity_bonus_total

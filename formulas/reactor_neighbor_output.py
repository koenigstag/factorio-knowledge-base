def reactor_grid_output(rows, cols, base_output_mw, neighbour_bonus):
    """Total heat output (MW) of a fully-populated rows x cols grid of
    reactors, where each reactor's output is multiplied by
    (1 + neighbour_bonus * count_of_adjacent_reactors) - orthogonal
    adjacency only (up/down/left/right), no diagonals.
    """
    total = 0.0
    for r in range(rows):
        for c in range(cols):
            neighbours = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbours += 1
            total += base_output_mw * (1 + neighbour_bonus * neighbours)
    return total

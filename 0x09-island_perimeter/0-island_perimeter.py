#!/usr/bin/python3
"""This will show solve the island perimeter task """


def island_perimeter(grid: list) -> int:
    """
    this will use the grid which is a
    list of list and returns the perimeter
    of the island given from the grids
    Args:
        grids: This is a list of list
    Returns:
        This will returns integer of the perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over the entire grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # We found a land cell
                # Check the four adjacent cells (up, down, left, right)

                # Check above
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1

                # Check below
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1

                # Check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1

                # Check right
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter

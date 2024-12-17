#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid (list): 2D list of integers where 0 is water, 1 is land
    Returns:
        int: Perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if grid else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for the current land cell
                perimeter += 4

                # Check for adjacent land cells (shared sides)
                if i > 0 and grid[i - 1][j] == 1:  # Top neighbor
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Bottom neighbor
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left neighbor
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right neighbor
                    perimeter -= 1

    return perimeter


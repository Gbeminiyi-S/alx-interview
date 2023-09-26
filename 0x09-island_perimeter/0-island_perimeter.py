#!/usr/bin/python3
"""This module defines the function `island_perimeter`"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    size = len(grid)
    perimeter = 0

    for i in range(size):
        for j in range(size):
            if grid[i][j]:
                if (0 <= i <= size - 1) and (0 <= j <= size - 1):
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                    if grid[i][j + 1] == 0:
                        perimeter += 1
                    if grid[i + 1][j] == 0:
                        perimeter += 1
    return perimeter

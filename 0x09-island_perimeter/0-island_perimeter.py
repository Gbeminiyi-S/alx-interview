#!/usr/bin/python3
"""This module defines the function `island_perimeter`"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    if grid == []:
        return 0

    col_size = len(grid[0])
    row_size = len(grid)
    perimeter = 0

    for i in range(row_size):
        for j in range(col_size):
            if grid[i][j]:
                if (0 < i < row_size) or (0 < j < col_size):
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    if j + 1 >= col_size or grid[i][j + 1] == 0:
                        perimeter += 1
                    if i + 1 >= row_size or grid[i + 1][j] == 0:
                        perimeter += 1
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        perimeter += 1
    return perimeter

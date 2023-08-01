#!/usr/bin/env python3
# character_picture_grid.py — An exercise in understanding lists.
# For more information, see README.md

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.

grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "0", "0", ".", ".", "."],
    ["0", "0", "0", "0", ".", "."],
    ["0", "0", "0", "0", "0", "."],
    [".", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "."],
    ["0", "0", "0", "0", ".", "."],
    [".", "0", "0", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

row_count = len(grid[0])
column_count = len(grid)

for i in range(row_count):
    for j in range(column_count):
        print(grid[j][i], end="")
    print()

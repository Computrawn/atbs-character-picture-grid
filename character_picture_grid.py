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


def rotate90():
    """Rotate grid 90 degrees clockwise"""

    for y, _ in enumerate(grid[0]):
        for x, _ in enumerate(grid):
            print(grid[x][y], end="")
        print()


def main():
    rotate90()


if __name__ == "__main__":
    main()

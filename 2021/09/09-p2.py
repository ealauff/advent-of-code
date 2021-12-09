# --- Part Two ---
# Next, you need to find the largest basins so you know what areas are most important to avoid.

# A basin is all locations that eventually flow downward to a single low point.
# Therefore, every low point has a basin, although some basins are very small.
# Locations of height 9 do not count as being in any basin,
# and all other locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point.
# The example above has four basins.

# The top-left basin, size 3:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The top-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The middle basin, size 14:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The bottom-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

# What do you get if you multiply together the sizes of the three largest basins?

# Your puzzle answer was XXXXXXX.

###########################################################################################################################################################################

import pathlib


def basin_size(row, col):

    if (row, col) in visited or heightmap[row][col] == 9:
        return 0

    size = 1
    visited.add((row, col))

    if row != 0:
        size += basin_size(row - 1, col)

    if row != num_rows - 1:
        size += basin_size(row + 1, col)

    if col != 0:
        size += basin_size(row, col - 1)

    if col != num_cols - 1:
        size += basin_size(row, col + 1)

    return size


f = open(pathlib.Path(__file__).parent / 'input.txt', "r").read().splitlines()

heightmap = [list(map(int, list(x))) for x in f]
visited = set()
three_largest_basins = []

num_rows = len(heightmap)
num_cols = len(heightmap[0])
product = 1

for row in range(num_rows):
    for col in range(num_cols):

        if (row, col) in visited or heightmap[row][col] == 9:
            continue

        size = basin_size(row, col)

        if len(three_largest_basins) < 3:
            three_largest_basins.append(size)

        else:
            if size > three_largest_basins[0]:
                three_largest_basins[0] = size

        three_largest_basins.sort()

for basin in three_largest_basins:
    product *= basin

print(product)

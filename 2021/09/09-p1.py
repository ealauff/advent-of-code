# --- Day 9: Smoke Basin ---
# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

# Your puzzle answer was XXX.

###########################################################################################################################################################################

import pathlib

f = open(pathlib.Path(__file__).parent / 'input.txt', "r").read().splitlines()

heightmap = [list(map(int, list(x))) for x in f]

num_rows = len(heightmap)
num_cols = len(heightmap[0])
risk_level = 0

for row in range(num_rows):
    for col in range(num_cols):
        val = heightmap[row][col]

        if row != 0:
            above = heightmap[row - 1][col]
            if val >= above:
                continue

        if row != num_rows - 1:
            below = heightmap[row + 1][col]
            if val >= below:
                continue

        if col != 0:
            left = heightmap[row][col - 1]
            if val >= left:
                continue

        if col != num_cols - 1:
            right = heightmap[row][col + 1]
            if val >= right:
                continue

        risk_level += val + 1

print(risk_level)

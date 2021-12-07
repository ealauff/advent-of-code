# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

# Your puzzle answer was 18065.

########################################################################################################################################################################################################################################################

import pathlib


def lineLow(p0, p1):

    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]

    dx = x1 - x0
    dy = y1 - y0
    y_i = 1

    if dy < 0:
        y_i = -1
        dy = -dy

    D = 2 * dy - dx
    y = y0

    for x in range(x0, x1 + 1):

        if not '{}:{}'.format(x, y) in points:
            points['{}:{}'.format(x, y)] = 1
        else:
            points['{}:{}'.format(x, y)] += 1

        if D > 0:
            y += y_i
            D -= 2 * dx
        D = D + 2 * dy


def lineHigh(p0, p1):

    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]

    dx = x1 - x0
    dy = y1 - y0
    x_i = 1

    if dx < 0:
        x_i = -1
        dx = -dx

    D = 2 * dx - dy
    x = x0

    for y in range(y0, y1 + 1):

        if not '{}:{}'.format(x, y) in points:
            points['{}:{}'.format(x, y)] = 1
        else:
            points['{}:{}'.format(x, y)] += 1

        if D > 0:
            x += x_i
            D -= 2 * dy
        D = D + 2 * dx


f = open(pathlib.Path(__file__).parent / 'input.txt', "r").read().splitlines()

points = {}

lines = list(map(lambda x: x.split(' -> '), f))

for line in lines:
    p0 = list(map(int, line[0].split(',')))
    p1 = list(map(int, line[1].split(',')))

    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]

    # Non-steep line (ie. -1<slope<1)
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            lineLow(p1, p0)
        else:
            lineLow(p0, p1)

    # Steep line (ie. slope<=-1 or slope>=1)
    else:
        if y0 > y1:
            lineHigh(p1, p0)
        else:
            lineHigh(p0, p1)

overlapping_lines = 0
for i in points.values():
    if i >= 2:
        overlapping_lines += 1

print(overlapping_lines)


# MAKE THIS LOOK NICER

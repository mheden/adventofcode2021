from utils import slurp, unpack
import math


def neighbours(x, y, grid):
    n = set()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            n.add((x + dx, y + dy, grid[(x + dx, y + dy)]))
        except KeyError:
            pass
    return n


def is_lowpoint(x, y, grid):
    return all(grid[(x, y)] < v for _, _, v in neighbours(x, y, grid))


def populate_grid(data):
    data = unpack(data)
    grid = {}
    y = 0
    maxx = len(data[0])
    maxy = len(data)
    for row in data:
        x = 0
        for v in row:
            grid[(x, y)] = int(v)
            x += 1
        y += 1
    return maxx, maxy, grid


def part1(data):
    maxx, maxy, grid = populate_grid(data)
    return sum(
        1 + grid[(x, y)]
        for x in range(maxx)
        for y in range(maxy)
        if is_lowpoint(x, y, grid)
    )


def updatebasin(x, y, grid, basin):
    height = grid[(x, y)]
    for x_, y_, height_ in neighbours(x, y, grid):
        if (x_, y_) not in basin:
            if height_ > height and height_ != 9:
                basin.add((x_, y_))
                updatebasin(x_, y_, grid, basin)


def part2(data):
    maxx, maxy, grid = populate_grid(data)
    lowpoints = set(
        (x, y) for x in range(maxx) for y in range(maxy) if is_lowpoint(x, y, grid)
    )
    basins = []
    for x, y in lowpoints:
        basin = set()
        basin.add((x, y))
        updatebasin(x, y, grid, basin)
        basins.append(len([grid[(x, y)] for x, y in basin]))
    return math.prod(sorted(basins, reverse=True)[0:3])


print("#--- Day 9: Smoke Basin: part1:", end=" ")

testdata = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

assert part1(testdata) == 15
print(part1(slurp("09.txt")))

print("#--- Day 9: Smoke Basin: part2:", end=" ")

assert part2(testdata) == 1134
print(part2(slurp("09.txt")))

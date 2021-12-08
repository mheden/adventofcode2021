from utils import P2d, slurp, sign, unpack
from collections import defaultdict


def part1(data):
    data = unpack(data)
    lines = []
    for row in data:
        p1, _, p2 = row.split(" ")
        p1x, p1y = p1.split(",")
        p2x, p2y = p2.split(",")
        lines.append((P2d(*p1.split(",")), P2d(*p2.split(","))))

    grid = defaultdict(int)
    for line in lines:
        start, end = line
        if not (start.x == end.x or start.y == end.y):
            continue
        dx = sign(end.x - start.x)
        dy = sign(end.y - start.y)
        p = start
        while p.pos() != end.pos():
            grid[p.pos()] += 1
            p.x += dx
            p.y += dy
        grid[p.pos()] += 1
    return len([x for x in grid.values() if x > 1])


def part2(data):
    data = unpack(data)
    lines = []
    for row in data:
        p1, _, p2 = row.split(" ")
        p1x, p1y = p1.split(",")
        p2x, p2y = p2.split(",")
        lines.append((P2d(*p1.split(",")), P2d(*p2.split(","))))

    grid = defaultdict(int)
    for line in lines:
        start, end = line
        dx = sign(end.x - start.x)
        dy = sign(end.y - start.y)
        p = start
        while p.pos() != end.pos():
            grid[p.pos()] += 1
            p.x += dx
            p.y += dy
        grid[p.pos()] += 1
    return len([x for x in grid.values() if x > 1])


print("#--- Day 5: Hydrothermal Venture: part1 ---#")

testdata = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

assert part1(testdata) == 5
print(part1(slurp("05.txt")))

print("#--- Day 5: Hydrothermal Venture: part2 ---#")

assert part2(testdata) == 12
print(part2(slurp("05.txt")))

from utils import slurp, unpack, neighbours, BIGNUM
from collections import defaultdict
from queue import PriorityQueue


def get_weight(start, end, edges):
    paths = {start: (None, 0)}
    Q = PriorityQueue()
    visited = set()
    current = start
    while current != end:
        visited.add(current)
        current_weight = paths[current][1]
        for node, weight in edges[current].items():
            total = current_weight + weight
            if node not in paths:
                # first visit
                paths[node] = (current, total)
            elif total < paths[node][1]:
                # better path
                paths[node] = (current, total)
            else:
                # do nothing
                pass
            Q.put((total, node))
        _, next_ = Q.get()
        while next_ in visited:
            _, next_ = Q.get()
        current = next_
    current = end
    path = []
    while current != start:
        path.append(current)
        current = paths[current][0]
    return paths[end][1]


def part1(data):
    grid = {}
    y = 0
    start = (0, 0)
    end = (0, 0)
    for row in unpack(data):
        x = 0
        for level in row:
            grid[(x, y)] = int(level)
            end = (x, y)
            x += 1
        y += 1

    edges = defaultdict(dict)
    for point, weight in grid.items():
        for x, y, w in neighbours(*point, grid):
            edges[point][(x, y)] = w
    return get_weight(start, end, edges)

def part2(data):
    grid = {}
    y = 0
    start = (0, 0)
    end = (0, 0)
    for row in unpack(data):
        width = len(row)
        x = 0
        for level in row:
            level = int(level)
            for yy in range(5):
                for xx in range(5):
                    l = level + yy + xx
                    if l > 9:
                        l -= 9
                    grid[(x + xx * width, y + yy * width)] = l
                    end = (x + xx * width, y + yy * width)
            x += 1
        y += 1

    edges = defaultdict(dict)
    for point, weight in grid.items():
        for x, y, w in neighbours(*point, grid):
            edges[point][(x, y)] = w
    return get_weight(start, end, edges)


testdata = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
filedata = slurp("15.txt")

print("#--- Day 15: Chiton: part1:", end=" ")
assert part1(testdata) == 40
print(part1(filedata))

print("#--- Day 15: Chiton: part2:", end=" ")
assert part2(testdata) == 315
print(part2(filedata))

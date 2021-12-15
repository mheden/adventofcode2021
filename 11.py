from utils import slurp, unpack


class Octopus:
    def __init__(self, level):
        self.level = level
        self.has_flashed = False


def populate_grid(data):
    grid = {}
    y = 0
    for row in unpack(data):
        x = 0
        for c in row:
            grid[(x, y)] = Octopus(int(c))
            x += 1
        y += 1
    return grid


def neightbours(x, y, grid):
    n = []
    for dy, dx in [
        (1, -1),
        (1, 0),
        (1, 1),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]:
        try:
            n.append(grid[(x + dx, y + dy)])
        except KeyError:
            pass
    return n


def iterate(grid):
    flashes = 0
    for octo in grid.values():
        octo.level += 1
        octo.has_flashed = False
    sum_, last_sum = -2, -1
    while last_sum != sum_:
        last_sum = sum_
        for pos, octo in grid.items():
            if octo.level > 9:
                x, y = pos
                if not octo.has_flashed:
                    octo.has_flashed = True
                    flashes += 1
                    for o in neightbours(x, y, grid):
                        o.level += 1

        for octo in grid.values():
            if octo.has_flashed:
                octo.level = 0

        sum_ = sum(octo.level for octo in grid.values())
    return flashes


def part1(data, steps):
    grid = populate_grid(data)
    return sum(iterate(grid) for _ in range(steps))


def part2(data):
    grid = populate_grid(data)
    f = len(grid)
    step = 0
    while True:
        step += 1
        if f == iterate(grid):
            return step


testdata = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
filedata = slurp("11.txt")

print("#--- Day 11: Dumbo Octopus: part1:", end=" ")
assert part1(testdata, 100) == 1656
print(part1(filedata, 100))

print("#--- Day 11: Dumbo Octopus: part1:", end=" ")
assert part2(testdata) == 195
print(part2(filedata))

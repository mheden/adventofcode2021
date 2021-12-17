from utils import slurp, unpack


def fold(grid, axis, foldpoint):
    grid_ = {}
    points = list(grid.keys())
    for x, y in points:
        x_, y_ = x, y
        if axis == "x" and x > foldpoint:
            x_ = foldpoint - (x - foldpoint)
            try:
                value = grid[(x_, y)] | grid[(x, y)]
            except KeyError:
                value = grid[(x, y)]
            del grid[(x, y)]
        elif axis == "y" and y > foldpoint:
            y_ = foldpoint - (y - foldpoint)
            try:
                value = grid[(x, y_)] | grid[(x, y)]
            except KeyError:
                value = grid[(x, y)]
            del grid[(x, y)]
        else:
            value = grid[(x, y)]
        grid_[(x_, y_)] = value
    return grid_


def printgrid(grid):
    for y in range(6):
        for x in range(40):
            if (x, y) in grid and grid[(x, y)]:
                print("█", end="")
            else:
                print(" ", end="")
        print()


def part1(data):
    dots, folds = unpack(data, sep="\n\n")
    dots = unpack(dots)
    folds = unpack(folds)
    grid = {}
    for dot in dots:
        x, y = map(int, dot.split(","))
        grid[(x, y)] = True

    f = []
    for fold_ in folds:
        axis, foldpoint = fold_.split(" ")[-1].split("=")
        f.append((axis, int(foldpoint)))
    grid = fold(grid, *f[0])
    return sum(grid.values())


def part2(data):
    dots, folds = unpack(data, sep="\n\n")
    dots = unpack(dots)
    folds = unpack(folds)
    grid = {}
    for dot in dots:
        x, y = map(int, dot.split(","))
        grid[(x, y)] = True

    for fold_ in folds:
        axis, foldpoint = fold_.split(" ")[-1].split("=")
        grid = fold(grid, axis, int(foldpoint))
    return grid


testdata = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
filedata = slurp("13.txt")

print("#--- Day 13: Transparent Origami: part1:", end=" ")
assert part1(testdata) == 17
print(part1(filedata))

print("#--- Day 13: Transparent Origami: part2:")
printgrid(part2(filedata))

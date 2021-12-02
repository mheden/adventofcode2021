from utils import read_file

movements = {
    "down": (0, 1),
    "up": (0, -1),
    "forward": (1, 0),
}


def move(instructions):
    hpos, depth = 0, 0
    for ins in instructions:
        move, amount = ins.split(" ")
        h, d = movements[move]
        hpos += h * int(amount)
        depth += d * int(amount)
    return hpos * depth


def move_with_aim(instructions):
    hpos = 0
    depth = 0
    aim = 0
    for ins in instructions:
        move, amount = ins.split(" ")
        h, d = movements[move]
        hpos += h * int(amount)
        if move == "forward":
            depth += aim * int(amount)
        aim += d * int(amount)
    return hpos * depth


print("#--- Dive: part1 ---#")

testdata = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]
assert move(testdata) == 150
print(move(read_file("02.txt")))


print("#--- Dive: part2 ---#")

assert move_with_aim(testdata) == 900
print(move_with_aim(read_file("02.txt")))

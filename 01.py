from utils import read_file_int


def increases(data):
    n = 0
    last = data[0]
    for value in data[1:]:
        if value > last:
            n += 1
        last = value
    return n


def slidingsum(data):
    sums = []
    for i in range(len(data) - 2):
        sums.append(sum(data[i : i + 3]))
    return increases(sums)


print("#--- Sonar Sweep: part1 ---#")

testdata = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]
assert increases(testdata) == 7
print(increases(read_file_int("01.txt")))

print("#--- Sonar Sweep: part2 ---#")

assert slidingsum(testdata) == 5
print(slidingsum(read_file_int("01.txt")))

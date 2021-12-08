from utils import slurp, unpack


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


print("#--- Day 1: Sonar Sweep: part1 ---#")

testdata = """
199
200
208
210
200
207
240
269
260
263
"""

assert increases(unpack(testdata, fn=int)) == 7
print(increases(unpack(slurp("01.txt"), fn=int)))

print("#--- Day1: Sonar Sweep: part2 ---#")

assert slidingsum(unpack(testdata, fn=int)) == 5
print(slidingsum(unpack(slurp("01.txt"), fn=int)))

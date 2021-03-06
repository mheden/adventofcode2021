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
filedata = slurp("01.txt")

print("#--- Day 1: Sonar Sweep: part1:", end=" ")
assert increases(unpack(testdata, fn=int)) == 7
print(increases(unpack(filedata, fn=int)))

print("#--- Day 1: Sonar Sweep: part2:", end=" ")
assert slidingsum(unpack(testdata, fn=int)) == 5
print(slidingsum(unpack(filedata, fn=int)))

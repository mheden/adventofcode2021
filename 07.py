from utils import slurp, unpack
from statistics import median, mean


def part1(data):
    data = unpack(data, sep=",", fn=int)
    m = int(median(data))
    return sum(abs(x - m) for x in data)


def part2(data):
    def consumption(x, a):
        if x == a:
            return 0
        else:
            diff = abs(x - a)
            return int(diff * (diff + 1) / 2)

    data = unpack(data, sep=",", fn=int)
    m = mean(data)
    hi = int(m + 1)
    lo = int(m)
    sum_hi = sum(consumption(x, hi) for x in data)
    sum_lo = sum(consumption(x, lo) for x in data)
    return min(sum_hi, sum_lo)


print("#--- Day 7: The Treachery of Whales: part1 ---#")

testdata = "16,1,2,0,4,2,7,1,2,14"

assert part1(testdata) == 37
print(part1(slurp("07.txt")))

print("#--- Day 7: The Treachery of Whales: part2 ---#")

assert part2(testdata) == 168
print(part2(slurp("07.txt")))

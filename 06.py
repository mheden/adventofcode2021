from utils import lmap, slurp, unpack


def num_fishes(data, days=80):
    fishes = [0] * 9
    for i in unpack(data, sep=",", fn=int):
        fishes[i] += 1

    for _ in range(days):
        fishes_ = [0] * 9
        for i in reversed(range(1, 9)):
            fishes_[i - 1] = fishes[i]
        fishes_[8] += fishes[0]
        fishes_[6] += fishes[0]
        fishes = fishes_
    return sum(fishes)


print("#--- Day 6: Lanternfish: part1 ---#")

testdata = "3,4,3,1,2"

assert num_fishes(testdata) == 5934
print(num_fishes(slurp("06.txt")))


print("#--- Day 6: Lanternfish: part2 ---#")

assert num_fishes(testdata, 256) == 26984457539
print(num_fishes(slurp("06.txt"), 256))

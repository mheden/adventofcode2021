from utils import slurp, unpack
from collections import defaultdict, Counter
from copy import deepcopy
from functools import reduce


def total(chain):
    return reduce(lambda a, b: a + b, chain.values())


def solve(data, iterations):
    template, rules = unpack(data, sep="\n\n")
    rules = [row.split(" -> ") for row in unpack(rules)]
    rules = {k: v for k, v in rules}

    chain = defaultdict(Counter)
    for i in range(len(template) - 1):
        current = template[i]
        next_ = template[i + 1]
        chain[current][next_] += 1

    for _ in range(iterations):
        chain_ = deepcopy(chain)
        for first in chain:
            for second, count in chain[first].items():
                middle = rules[f"{first}{second}"]
                chain_[first][second] -= count
                chain_[first][middle] += count
                chain_[middle][second] += count
        chain = chain_
    summary = total(chain)
    # don't forget the first letter of the template
    summary[template[0]] += 1
    common = summary.most_common()
    return common[0][1] - common[-1][1]


testdata = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
filedata = slurp("14.txt")

print("#--- Day 14: Extended Polymerization: part1:", end=" ")

assert solve(testdata, 10) == 1588
print(solve(filedata, 10))

print("#--- Day 14: Extended Polymerization: part2:", end=" ")

assert solve(testdata, 40) == 2188189693529
print(solve(filedata, 40))

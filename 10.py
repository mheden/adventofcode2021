from utils import slurp, unpack
from statistics import median


POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

POINTS2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

MATCH = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def score(line):
    stack = []
    for c in line:
        if c in MATCH:
            stack.insert(0, c)
        else:
            if c != MATCH[stack[0]]:
                return POINTS[c]
            else:
                stack.pop(0)
    return 0


def seq(line):
    stack = []
    for c in line:
        if c in MATCH:
            stack.insert(0, c)
        else:
            if c != MATCH[stack[0]]:
                return []
            else:
                stack.pop(0)
    return [MATCH[c] for c in stack]


def part1(data):
    sum_ = 0
    for row in unpack(data):
        sum_ += score(row)
    return sum_


def part2(data):
    scores = []
    for row in unpack(data):
        total = 0
        for s in seq(row):
            total = total * 5 + POINTS2[s]
        if total != 0:
            scores.append(total)
    return median(scores)


print("#--- Day 10: Syntax Scoring: part1:", end=" ")

testdata = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

assert part1(testdata) == 26397
print(part1(slurp("10.txt")))

print("#--- Day 10: Syntax Scoring: part2:", end=" ")
assert part2(testdata) == 288957
print(part2(slurp("10.txt")))

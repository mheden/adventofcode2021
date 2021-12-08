from utils import slurp, unpack


def part1(data):
    data = unpack(data)
    count = 0
    for d in data:
        _, digits = unpack(d, sep="|")
        digits = unpack(digits, sep=" ")
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                count += 1
    return count


print("#--- Day 8: Seven Segment Search: part1:", end=" ")

testdata = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

assert part1(testdata) == 26
print(part1(slurp("08.txt")))


print("#--- Day 8: Seven Segment Search: part2:", end=" ")

#  assert part2(testdata) == 61229
#  print(part2(slurp("08.txt")))

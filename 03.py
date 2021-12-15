from utils import slurp, unpack


def power_consumption(data):
    data = unpack(data)
    sums = [0] * len(data[0])
    threshold = len(data) / 2
    for d in data:
        for i, c in enumerate(d):
            sums[i] += int(c)
    gamma, epsilon = "", ""
    for s in sums:
        if s > threshold:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def life_support_rating(data):
    def ogr(data, pos):
        if len(data) == 1:
            return data
        threshold = len(data) / 2
        count = 0
        for row in data:
            count += int(row[pos])
        if count >= threshold:
            filter = "1"
        else:
            filter = "0"
        res = []
        for row in data:
            if row[pos] == filter:
                res.append(row)
        return res

    def csr(data, pos):
        if len(data) == 1:
            return data
        threshold = len(data) / 2
        count = 0
        for row in data:
            count += int(row[pos])
        if count >= threshold:
            filter = "0"
        else:
            filter = "1"
        res = []
        for row in data:
            if row[pos] == filter:
                res.append(row)
        return res

    data = unpack(data)
    width = len(data[0])
    data_ogr = data.copy()
    data_csr = data.copy()
    for pos in range(width):
        data_ogr = ogr(data_ogr, pos)
        data_csr = csr(data_csr, pos)
    return int(data_ogr[0], 2) * int(data_csr[0], 2)


testdata = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
filedata = slurp("03.txt")

print("#--- Day 3: Binary Diagnostic: part1:", end=" ")
assert power_consumption(testdata) == 198
print(power_consumption(filedata))

print("#--- Day 3: Binary Diagnostic: part2:", end=" ")
assert life_support_rating(testdata) == 230
print(life_support_rating(filedata))

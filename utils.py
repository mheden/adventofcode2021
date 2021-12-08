from collections import namedtuple

BIGNUM = 10 ** 100


class P2d:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def pos(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"P2d(%d, %d)" % (self.x, self.y)


def lmap(op, array):
    return list(map(op, array))


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def manhattan_distance(p0, p1):
    return sum(abs(a - b) for a, b in zip(p0, p1))


def unpack(data, sep="\n", fn=str):
    sections = data.strip().split(sep)
    return [fn(section) for section in sections]


def slurp(filename):
    with open(filename) as f:
        return f.read().rstrip()


def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def read_file_int(filename):
    return list(map(int, read_file(filename)))


def xor(a, b):
    return bool(a) ^ bool(b)

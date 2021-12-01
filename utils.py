from collections import namedtuple

BIGNUM = 10 ** 100

Point2d = namedtuple("Point2d", ["x", "y"])
Point3d = namedtuple("Point3d", ["x", "y", "z"])


def manhattan_distance(p0, p1):
    return sum(abs(a - b) for a, b in zip(p0, p1))


def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def read_file_int(filename):
    return list(map(int, read_file(filename)))


def xor(a, b):
    return bool(a) ^ bool(b)

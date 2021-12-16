BIGNUM = 10 ** 100


class P2d:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def pos(self):
        return (self.x, self.y)

    def __repr__(self):
        return "P2d(%d, %d)" % (self.x, self.y)


def neighbours(x, y, grid):
    """Return the coordinates and value of all neighbours of (x, y)"""
    n = set()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            n.add((x + dx, y + dy, grid[(x + dx, y + dy)]))
        except KeyError:
            pass
    return n


def nibble_to_bin(hexchar):
    return bin(int(hexchar, 16))[2:].zfill(4)


def lmap(op, array):
    return list(map(op, array))


def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def unique(lst):
    return list(dict.fromkeys(lst))


def manhattan_distance(p0, p1) -> int:
    return sum(abs(a - b) for a, b in zip(p0, p1))


def unpack(data: str, sep="\n", fn=str):
    sections = data.strip().split(sep)
    return [fn(section) for section in sections]


def slurp(filename: str) -> str:
    with open(filename) as f:
        return f.read().rstrip()


#  def read_file(filename):
#      with open(filename) as f:
#          lines = f.read().splitlines()
#      return lines


#  def read_file_int(filename):
#      return list(map(int, read_file(filename)))


def xor(a, b):
    return bool(a) ^ bool(b)

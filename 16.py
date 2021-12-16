from utils import slurp, unpack, nibble_to_bin
from functools import reduce


class Packet:
    def __init__(self, bits):
        self.bits = list(bits)

    def take(self, n):
        s = "".join(self.bits.pop(0) for _ in range(n))
        return s

    def takeint(self, n):
        return int(self.take(n), 2)

    def version(self):
        return int(self.take(3), 2)

    def type(self):
        return int(self.take(3), 2)

    def literal(self):
        more = True
        value = 0
        while more:
            more = self.take(1) == "1"
            value = value * 16 + int(self.take(4), 2)
        return value

    def __str__(self):
        return "".join(self.bits)


def parse(packet, versions):
    p = Packet(packet)
    versions.append(p.version())
    if p.type() == 4:
        p.literal()
        return str(p)
    else:
        if p.take(1) == "0":
            packetlen = p.takeint(15)
            subpacket = p.take(packetlen)
            while len(subpacket) != 0:
                subpacket = parse(subpacket, versions)
        else:
            numsubpackets = p.takeint(11)
            subpacket = str(p)
            for i in range(numsubpackets):
                subpacket = parse(subpacket, versions)
            p = Packet(subpacket)
    return str(p)


def parse2(packet, result):
    p = Packet(packet)
    p.version()
    type_ = p.type()
    if type_ == 4:
        result.append(p.literal())
        return str(p)
    else:
        subpackets = []
        if p.take(1) == "0":
            packetlen = p.takeint(15)
            subpacket = p.take(packetlen)
            while len(subpacket) != 0:
                subpacket = parse2(subpacket, subpackets)
        else:
            numsubpackets = p.takeint(11)
            subpacket = str(p)
            for i in range(numsubpackets):
                subpacket = parse2(subpacket, subpackets)
            p = Packet(subpacket)
        if type_ == 0:
            result.append(sum(subpackets))
        elif type_ == 1:
            result.append(reduce(lambda a, b: a * b, subpackets))
        elif type_ == 2:
            result.append(min(subpackets))
        elif type_ == 3:
            result.append(max(subpackets))
        elif type_ == 5:
            result.append(subpackets[0] > subpackets[1])
        elif type_ == 6:
            result.append(subpackets[0] < subpackets[1])
        elif type_ == 7:
            result.append(subpackets[0] == subpackets[1])
        else:
            assert False, f"Should not happen: {type_}"
    return str(p)


def hextobin(hexstr):
    return "".join(nibble_to_bin(n) for n in hexstr)


def part1(packet):
    packet = hextobin(packet)
    versions = []
    parse(packet, versions)
    return sum(versions)


def part2(packet):
    packet = hextobin(packet)
    result = []
    parse2(packet, result)
    return result[0]


filedata = unpack(slurp("16.txt"))[0]

print("#--- Day 16: Packet Decoder: part1:", end=" ")
assert part1("8A004A801A8002F478") == 16
assert part1("620080001611562C8802118E34") == 12
assert part1("C0015000016115A2E0802F182340") == 23
assert part1("A0016C880162017C3686B18A3D4780") == 31
print(part1(filedata))

print("#--- Day 16: Packet Decoder: part1:", end=" ")
assert part2("C200B40A82") == 3
assert part2("04005AC33890") == 54
assert part2("880086C3E88112") == 7
assert part2("CE00C43D881120") == 9
assert part2("D8005AC2A8F0") == 1
assert part2("F600BC2D8F") == 0
assert part2("9C005AC2F8F0") == 0
assert part2("9C0141080250320F1802104A08") == 1
print(part2(filedata))

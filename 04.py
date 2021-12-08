from utils import unpack, lmap, slurp
import re


def get_boards(data):
    boards = []
    for b in data:
        b = lmap(int, re.split(r"\s+", b.replace("\n", " ").strip()))
        board = {}
        for col in range(1, 6):
            for row in range(1, 6):
                board[b.pop(0)] = (row, col)
        boards.append((board, {}))
    return boards


def sum_of_umarked_numbers(board, drawn):
    sum_ = 0
    for number, pos in board.items():
        if pos not in drawn:
            sum_ += number
    return sum_


def got_bingo(drawn):
    # vertical
    for row in range(1, 6):
        count = 0
        for col in range(1, 6):
            if (row, col) in drawn:
                count += 1
        if count == 5:
            return True
    # horizontal
    for col in range(1, 6):
        count = 0
        for row in range(1, 6):
            if (row, col) in drawn:
                count += 1
        if count == 5:
            return True
    return False


def part1(data):
    data = unpack(data, sep="\n\n")
    numbers = unpack(data[0], sep=",", fn=int)
    boards = get_boards(data[1:])
    for number in numbers:
        for board, drawn in boards:
            if number in board:
                drawn[board[number]] = number
            if got_bingo(drawn):
                return number * sum_of_umarked_numbers(board, drawn)


def part2(data):
    data = unpack(data, sep="\n\n")
    numbers = unpack(data[0], sep=",", fn=int)
    boards = get_boards(data[1:])
    boards_left = set(range(len(boards)))
    for number in numbers:
        for i, bd in enumerate(boards):
            board, drawn = bd
            if number in board:
                drawn[board[number]] = number
            if got_bingo(drawn):
                try:
                    boards_left.remove(i)
                except KeyError:
                    pass
                if len(boards_left) == 0:
                    return number * sum_of_umarked_numbers(board, drawn)


print("#--- Day 4: Giant Squid: part1 ---#")

testdata = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

assert part1(testdata) == 4512
print(part1(slurp("04.txt")))


print("#--- Day 4: Giant Squid: part2 ---#")

assert part2(testdata) == 1924
print(part2(slurp("04.txt")))

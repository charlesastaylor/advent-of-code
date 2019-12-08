from common import _intcode as intcode


with open('day5_1.txt') as f:
    TEST = [int(c) for c in f.readline().strip().split(",")]

# Part one solved with input 0, part 2 with 5
intcode(TEST, debug=False)

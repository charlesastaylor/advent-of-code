from common import _intcode as intcode


with open('day2_1.txt') as f:
    data = [int(c) for c in f.readline().strip().split(",")]

data[1] = 12
data[2] = 2

intcode(data)
print(data[0])

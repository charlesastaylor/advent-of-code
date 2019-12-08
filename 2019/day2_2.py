from common import _intcode as intcode


with open('day2_1.txt') as f:
    input = [int(c) for c in f.readline().strip().split(",")]

def ans():
    for noun in range(100):
        for verb in range(100):
            data = input[:]
            data[1], data[2] = noun, verb
            intcode(data)
            if data[0] == 19690720:
                return noun, verb
    return "No answer found..."

n, v = ans()
print(100 * n + v)

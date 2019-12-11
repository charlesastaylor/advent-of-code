from common import intcode, tadd


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('day11.txt') as f:
    paint = [int(c) for c in f.readline().strip().split(",")]

rob = intcode(paint)
rob.send(None)

pos, direction = (0, 0), (0, 1)

painted = dict()

try:
    while True:
        painted[pos] = rob.send(painted.get(pos, 0))
        if next(rob) == 0:
            direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]
        else:
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
        pos = tadd(pos, direction)
        next(rob) # advance to next input
except StopIteration:
    print(len(painted))
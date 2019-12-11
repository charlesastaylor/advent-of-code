from common import intcode, tadd


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('day11.txt') as f:
    paint = [int(c) for c in f.readline().strip().split(",")]

rob = intcode(paint)
rob.send(None)

pos, direction = (0, 0), (0, -1)

painted = {(0, 0): 1}

try:
    while True:
        painted[pos] = rob.send(painted.get(pos, 0))
        if next(rob) == 0:
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
        else:
            direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]
        pos = tadd(pos, direction)
        next(rob) # advance to next input
except StopIteration:
    pass

max_x, max_y = float('-inf'), float('-inf')
min_x, min_y = float('inf'), float('inf')
for coord in painted:
    x, y = coord
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    min_x = min(x, min_x)
    min_y = min(y, min_y)

for j in range(max_y + 1):
    s = ""
    for i in range(max_x + 1):
        val = painted.get((i, j), 0)
        s += '#' if val == 1 else ' '
    print(s)

from common import intcode, tadd

with open('day19.txt') as f:
    program_input = [int(c) for c in f.readline().strip().split(",")]

def is_pulled(x, y):
    program = intcode(program_input)
    program.send(None)
    program.send(x)
    val = program.send(y)
    return val == 1

def grid_to_string(grid, x2, y2, x1=0, y1=0):
    s = ""
    for j in range(y1, y2):
        for i in range(x1, x2):
            s += '#' if grid.get((i, j), False) else '.'
        s += '\n'
    return s

if __name__ == "__main__":
    grid = {}
    row, left, right = 4, 3, 3
    target = 99 # off by one xd
    while True:
        row += 1
        if not is_pulled(left, row):
            left += 1
        if is_pulled(right + 1, row):
            right += 1
        for i in range(left, right + 1):
            grid[(i, row)] = True
        if (left, row - target) in grid and (left + target, row - target) in grid:
            break
    print(left * 10000 + (row - target))
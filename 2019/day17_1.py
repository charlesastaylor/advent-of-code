from common import intcode, tadd, grid_to_string

with open('day17.txt') as f:
    aft = [int(c) for c in f.readline().strip().split(",")]

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

if __name__ == "__main__":
    s = ''.join(chr(i) for i in list(intcode(aft)))
    s = s.rstrip() # remove trailing new lines
    grid = [[c for c in row] for row in s.split('\n')]
    intersections = []
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            if cell == "#":
                try:
                    if all([grid[y][x] == "#" for x, y in [tadd(d, (i, j)) for d in DIRECTIONS]]):
                        intersections.append((i, j))
                except IndexError:
                    pass

    print(grid_to_string(grid))
    # print(intersections)
    ans = sum(x * y for x, y in intersections)
    print(ans)
    print(len(grid[0]), len(grid))
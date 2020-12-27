from common import intcode, tadd, grid_to_string

with open('day19.txt') as f:
    program_input = [int(c) for c in f.readline().strip().split(",")]

if __name__ == "__main__":
    grid = []
    for j in range(50):
        grid.append([])
        for i in range(50):
            program = intcode(program_input)
            program.send(None)
            program.send(i)
            val = program.send(j)
            grid[j].append('#' if val == 1 else '.')

    print(grid_to_string(grid))
    print(sum(row.count('#') for row in grid))

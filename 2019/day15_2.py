import curses
import time

from common import intcode, tadd

WALL = u"\u23F9"
WALL = '#'
EMPTY = ' '
UNDISCOVERED = '?'
DRONE = 'D'
OXYGEN = 'O'

DIRECTIONS = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
REVERSE_DIRECTIONS = {1: 2, 2: 1, 3: 4, 4: 3}
DINPUT = {258: 2, 259: 1, 260: 3, 261: 4}

class Drone:
    def __init__(self, program):
        self.map = {(0, 0): EMPTY}
        self.location = (0, 0)
        self.program = intcode(program)
        self.program.send(None) # Initialize
        self.target_found = False
        self.counter = 0
        self.moves = []

    def move(self, direction):
        assert direction in DIRECTIONS, "Invalid direction"
        res = self.program.send(direction)
        new = tadd(self.location, DIRECTIONS[direction])
        if res == 0:
            self.map[new] = WALL
        elif res == 1:
            self.map[new] = EMPTY
            self.location = new
            self.counter += 1
        elif res == 2:
            self.map[new] = OXYGEN
            self.location = new
            self.target_found = True
            self.counter += 1
        next(self.program)
        return res

    def get_map_string(self):
        max_x = max_y = float('-infinity')
        min_x = min_y = float('infinity')
        for location in self.map:
            max_x = max(max_x, location[0])
            max_y = max(max_y, location[1])
            min_x = min(min_x, location[0])
            min_y = min(min_y, location[1])
        s = ""
        for j in range(min_y, max_y + 1):
            for i in range(min_x, max_x + 1):
                if self.location == (i, j):
                    s += DRONE + ' '
                else:
                    s += self.map.get((i, j), UNDISCOVERED) + ' '
            s+= '\n'
        s += str(self.counter) + '\n'
        return s

    def get_grid(self):
        max_x = max_y = float('-infinity')
        min_x = min_y = float('infinity')
        for location in self.map:
            max_x = max(max_x, location[0])
            max_y = max(max_y, location[1])
            min_x = min(min_x, location[0])
            min_y = min(min_y, location[1])
        return [[self.map.get((i, j), UNDISCOVERED) for i in range(min_x, max_x + 1)] for j in range(min_y, max_y + 1)]

    def explore(self, stdscr=None, delay=0.1):
        if stdscr:
            stdscr.addstr(0, 0, self.get_map_string())
            stdscr.refresh()
            if self.map[self.location] == OXYGEN:
                stdscr.addstr(f'\nTarget Found in {self.counter} steps!')
                stdscr.refresh()
                time.sleep(5)
            else:
                time.sleep(delay)
        to_search = []
        # search around self
        for d in DIRECTIONS:
            if tadd(self.location, DIRECTIONS[d]) not in self.map:
                res = self.move(d)
                if res == 1 or res == 2:
                    to_search.append(d)
                    self.move(REVERSE_DIRECTIONS[d])
                    self.counter -= 2
        # search each unexplored path
        for d in to_search:
            self.move(d)
            self.explore(stdscr, delay)
            self.move(REVERSE_DIRECTIONS[d])
            self.counter -= 2


with open('day15.txt') as f:
    DRONE_PROGRAM = [int(c) for c in f.readline().strip().split(",")]

# def main(stdscr):
#     drone = Drone(DRONE_PROGRAM)
#     stdscr.clear()
#     drone.explore(stdscr, 0.001)
#     map_ = drone.map
#     print(map)

def get_grid_string(grid):
    s = ""
    for row in grid:
        for cell in row:
            s += cell + ' '
        s += '\n' 
    return s

def main(stdscr):
    stdscr.clear()
    drone = Drone(DRONE_PROGRAM)
    drone.explore()
    grid = drone.get_grid()
    w, h = len(grid[0]), len(grid)
    print(get_grid_string(grid))
    
    
    fronts = [(7, 37)]
    OLD_OXYGEN = 'o'
    steps = 0
    while len(fronts) > 0:
        new_fronts = []
        for front in fronts:
            for d in DIRECTIONS.values():
                x, y = tadd(front, d)
                if grid[y][x] == EMPTY:
                    grid[y][x] == OXYGEN
                    new_fronts.append((x, y))
            grid[front[1]][front[0]] = OLD_OXYGEN
        fronts = new_fronts
        steps += 1
        stdscr.addstr(0, 0, get_grid_string(grid) + f'\n Steps: {steps}')
        stdscr.refresh()
        time.sleep(0.05)
    time.sleep(10)

# program gets to 345 steps but answer is 344, not sure why...
                    

if __name__ == "__main__":
    curses.wrapper(main)
    
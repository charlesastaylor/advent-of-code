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

    def explore(self, stdscr):
        stdscr.addstr(0, 0, self.get_map_string())
        stdscr.refresh()
        if self.map[self.location] == OXYGEN:
            time.sleep(10)
        else:
            time.sleep(0.1)
        to_search = []
        # search around self
        for d in DIRECTIONS:
            if tadd(self.location, DIRECTIONS[d]) not in self.map:
                res = self.move(d)
                if res == 1 or res == 2:
                    to_search.append(d)
                    self.move(REVERSE_DIRECTIONS[d])
                    self.counter -= 2
        # stdscr.addstr(0, 0, str(to_search))
        # stdscr.refresh()
        # time.sleep(10)

        for d in to_search:
            self.move(d)
            self.explore(stdscr)
            self.move(REVERSE_DIRECTIONS[d])
            self.counter -= 2


with open('day15.txt') as f:
    DRONE_PROGRAM = [int(c) for c in f.readline().strip().split(",")]

def main(stdscr):
    drone = Drone(DRONE_PROGRAM)
    stdscr.clear()
    drone.explore(stdscr)
    time.sleep(100)

if __name__ == "__main__":
    curses.wrapper(main)
        
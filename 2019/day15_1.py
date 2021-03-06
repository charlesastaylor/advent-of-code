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
DINPUT = {258: 2, 259: 1, 260: 3, 261: 4}

class Drone:
    def __init__(self, program):
        self.map = {(0, 0): EMPTY}
        self.location = (0, 0)
        self.program = intcode(program)
        self.program.send(None) # Initialize
        self.target_found = False
        self.counter = 0

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


with open('day15.txt') as f:
    DRONE_PROGRAM = [int(c) for c in f.readline().strip().split(",")]

def main(stdscr):
    drone = Drone(DRONE_PROGRAM)
    stdscr.clear()
    c = 0
    while True:
        stdscr.addstr(0, 0, drone.get_map_string())
        stdscr.refresh()
        c = stdscr.getch()
        if chr(c) == 'r':
            drone.counter = 0
        elif c in DINPUT: 
            drone.move(DINPUT[c])

if __name__ == "__main__":
    curses.wrapper(main)
        
import curses
import time

from common import intcode, tadd, grid_to_string


with open('day17.txt') as f:
    aft = [int(c) for c in f.readline().strip().split(",")]
aft[0] = 2
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
W, H = 41, 39

class Robot:
    def __init__(self, routine, A, B, C, live_feed):
        self.routine = routine
        self.functions = [A, B, C]
        self.live_feed = live_feed
        self.program = intcode(aft)
        # self.program.send(None)
        self.buffer = []
        self.grid = [['.' for _ in range(W)] for __ in range(H)]
        self.dust = 0
        
    def __str__(self):
        s = ''
        for row in self.grid:
            for cell in row:
                s += cell + ' '
            s += '\n'
        return s

    def start(self):
        self._update_grid()
        self._send_input()        

    def _update_grid(self):
        for j in range(H):
            for i in range(W):
                val = '\n'
                while val == '\n':
                    if self.buffer:
                        val = chr(self.buffer.pop())
                    else:
                        val = chr(next(self.program))
                if val not in ['#', '.', '\n', '^', 'v', '<', '>']:
                    self.dust = ord(val)
                    return False
                self.grid[j][i] = val
        next(self.program) # trailing new line character
        return True

    def _send_input(self):
        self._receive()
        for i, function in enumerate(self.routine):
            self._send(function)
            self._send('\n' if i == len(self.routine) - 1 else ',')
        for function in self.functions:
            self._receive()
            for i, command in enumerate(function):
                self._send(command)
                self._send('\n' if i == len(function) - 1 else ',')
        self._receive()
        self._send('y' if self.live_feed else 'n')
        self._newline()
        
    def _receive(self):
        '''Take output from program until receve None. Return as string'''
        try:
            out = []
            new = self.buffer.pop() if self.buffer else next(self.program)
            while new is not None:
                out.append(chr(new))
                new = next(self.program)
        except StopIteration:
            print("Stop iteration")
        return ''.join(c for c in out)

    def _send(self, c):
        if type(c) is int:
            c = str(c)
        val = self.program.send(ord(c))
        if val is not None:
            self.buffer.append(val)

    def _comma(self):
        return self._send(',')

    def _newline(self):
        return self._send('\n')


def main(stdscr):
    stdscr.clear()
    A, B, C, L, R = 'A', 'B', 'C', 'L', 'R'

    a = [R, 6, L, 6, L, 4, 6]
    b = [L, 8, L, 6, L, 9, 1, L, 6]
    c = [R, 6, L, 8, L, 9, 1, R, 6]
    r = [A, B, A, B, C, A, B, C, A, C]

    robot = Robot(r, a, b, c, True)
    robot.start()
    while robot._update_grid():
        stdscr.clear()
        stdscr.addstr(f'r: {r}, a: {a}, b: {b}, c: {c}\n')
        stdscr.addstr(str(robot))
        stdscr.refresh()
        time.sleep(0.05)

    stdscr.clear()
    stdscr.addstr(f'r: {r}, a: {a}, b: {b}, c: {c}\n')
    stdscr.addstr(str(robot))
    stdscr.addstr(f'Dust collected = {robot.dust}')
    stdscr.refresh()
    time.sleep(500)
    ## TODO brute force a solution
    
if __name__ == "__main__":
    curses.wrapper(main)
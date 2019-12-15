import curses
import time

from common import intcode


def boardstring(board):
    s = ""
    for row in board:
        for cell in row:
            s += cell + ' '
        s += '\n'
    return s

with open('day15.txt') as f:
    drone_program = [int(c) for c in f.readline().strip().split(",")]

drone = intcode(drone_program)
w, h = 20, 20   
board = [['x' for _ in range(w)] for _ in range(h)]
print(boardstring(board))

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
    stdscr.refresh()
    stdscr.getkey()
    
# scr = curses.initscr()
# curses.echo()

# try:
#     while True:
#         pass
# except:
#     curses.endwin()
    
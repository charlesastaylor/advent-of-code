import curses
import time
from itertools import islice

from common import intcode


with open('day13.txt') as f:
    game_input = [int(c) for c in f.readline().strip().split(",")]

game_input[0] = 2 # add quarters

TILES = {
    0: ' ',
    1: u"\u25A0", # wall
    2: u"\u25A1", # block
    3: u"\U0001F3D3", # paddle
    4: u"\u2299" # ball
}
NUM_TILES = 2640 // 3
WIDTH, HEIGHT = 44, 20
class Game:
    def __init__(self, game_input):
        self.board = [[0 for _ in range(WIDTH)] for __ in range(HEIGHT)]
        self.game = intcode(game_input)
        self.buffer = []
        self.score, self.ball_x, self.paddle_x, self.num_blocks = 0, 0, 0, 341
    
    def __str__(self):
        return self._get_board_string() + f'Score: {self.score}'

    def _get_board_string(self):
        out = ""
        for row in self.board:
            s = ""
            for cell in row:
                s += TILES[cell] + " "
            out += s + '\n'
        return out

    def update_board(self):
        while True:
            if self.buffer:
                x = self.buffer.pop()
            else:
                x = next(self.game)
                if x is None:
                    break # watiing for input
            y, val = next(self.game), next(self.game)
            if x == -1:
                self.score = val
            else:
                if val == 4:
                    self.ball_x = x
                elif val == 3:
                    self.paddle_x = x
                elif self.board[y][x] == 2:
                    self.num_blocks -= 1
                self.board[y][x] = val
    
    def set_joystick(self, position):
        next(self.game)
        self.buffer.append(self.game.send(position)) # give input - note this throws away a value

game = Game(game_input)
window = curses.initscr()
frame_delay = 0.01
try:
    while True:
        game.update_board()
        window.addstr(0, 0, str(game))
        # window.addstr(HEIGHT + 1, 0, f'\n{game.num_blocks}')
        window.refresh()
       
        if game.num_blocks == 0:
            time.sleep(1)
            break
        if game.ball_x > game.paddle_x:
            pos = 1
        elif game.ball_x < game.paddle_x:
            pos = -1
        else:
             pos = 0
        game.set_joystick(pos)
        time.sleep(frame_delay)
except:
    curses.endwin()
print(game.score)

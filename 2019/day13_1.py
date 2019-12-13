from common import intcode


with open('day13.txt') as f:
    game_input = [int(c) for c in f.readline().strip().split(",")]

TILES = {
    0: ' ',
    1: u"\u25A0", # wall
    2: u"\u25A1", # block
    3: u"\U0001F3D3", # horizontal paddle
    4: u"\u2299" # ball
}

board = []
game = intcode(game_input)
for x in game:
    y, val = next(game), next(game)
    if y >= len(board):
        board.append([])
    board[y].append(val)

no_blocks = 0

for row in board:
    s = ""
    for cell in row:
        s += TILES[cell] + " "
        if cell == 2:
            no_blocks +=1
    print(s)
print(no_blocks)
# print(board)


from copy import deepcopy


ASTEROID = "#"

def print_map(m):
    print(' ')

    for line in m:
        s = ""
        for cell in line:
            s += str(cell) + ' '
        print(s)
    print(' ')

def num_in_los(coords, map_):
    def is_on_line(a, b):
        ax, ay = a
        bx, by = b
        if ((ax < 0 and bx > 0) or (ax > 0 and bx < 0) or
            (ay < 0 and by > 0) or (ay > 0 and by < 0) or
            (ax == 0 and bx != 0) or (ax != 0 and bx == 0) or
            (ay == 0 and by != 0) or (ay != 0 and by == 0)):
            return False
        if ax < bx:
            if ax != 0 and ay != 0 and bx / ax != by / ay:
                return False
        else:
            if bx != 0 and by != 0 and ax / bx != ay / by:
                return False
        return True
    deltas = []
    w, h = len(map_[0]), len(map_)
    for j in range(h):
        for i in range(w):
            if map_[j][i] is ASTEROID and (i, j) != coords:
                deltas.append((i - coords[0], j - coords[1]))
    # print(deltas)
    lines = []
    for delta in deltas:
        # print(lines)
        new = True
        for line in lines:
            if is_on_line(delta, line[0]):
                line.append(delta)
                new = False
                break
        if new:
            lines.append([delta])
    return len(lines)

fname = 'day10.txt'
# fname = 'day10example_1.txt'
# fname = 'day10example_2.txt'
# fname = 'day10example_3.txt'
# fname = 'day10example_4.txt'
# fname = 'day10example_5.txt'

with open(fname) as f:
    map_ = [[c for c in line.strip()] for line in f]

w, h = len(map_[0]), len(map_)
out = deepcopy(map_)
max_ = 0

for j in range(h):
    for i in range(w):
        if map_[j][i] is ASTEROID:
            out[j][i] = num_in_los((i, j), map_)
            max_ = max(max_, out[j][i])

print_map(map_)
print_map(out)
print(max_)
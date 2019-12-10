import math


ASTEROID = "#"

def print_map(m):
    print(' ')

    for line in m:
        s = ""
        for cell in line:
            s += str(cell) + ' '
        print(s)
    print(' ')

def dist_squared(v):
    return v[0]**2 + v[1]**2

def first_element_angle(list_):
    return angle(list_[0])

def angle(v):
    at = math.atan2(v[1],v[0])
    at = at + math.pi * 2 if at < 0 else at
    return norm(math.degrees(at - 3 * math.pi / 2))

def norm(theta):
    while theta >= 360:
        theta -= 360
    while theta < 0:
        theta += 360
    return theta

def add(a, b):
    return [sum(x) for x in zip(a,b)]

def los(coords, map_):
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
    return lines

fname = 'day10.txt'
# fname = 'day10example_5.txt'
# fname = 'day10example_6.txt'

with open(fname) as f:
    map_ = [[c for c in line.strip()] for line in f]

mon = (26, 28)
# mon = (11, 13)
# mon = (8, 3)

w, h = len(map_[0]), len(map_)

lines = los(mon, map_)
# Put each line of sight into order, closest to monitoring station first
for line in lines:
    line.sort(key=dist_squared)
# Sort lines of sight by angle from vertically up
lines.sort(key=first_element_angle)

vaporized = []
while any([len(line) != 0 for line in lines]):
    for line in lines:
        try:
            vaporized.append(line.pop(0))
        except IndexError:
            pass

ans = add(vaporized[199], mon)
print(ans[0] * 100 + ans[1])
 
with open('day3_1.txt') as f:
    wires = [line.strip().split(',') for line in f]

#wires = [s.split(',') for s in ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]]

points = [set(), set()]

DIRECTIONS = {'U': (0, 1),'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def add(v1, v2):
    return tuple(sum(x) for x in zip(v1, v2))

def manhattan_dist(v1, v2=(0, 0)):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

for i, wire in enumerate(wires):
    cur = (0, 0)
    for path in wire:
        dir, val = path[0], int(path[1:])
        for _ in range(val):
            cur = add(cur, DIRECTIONS[dir])
            points[i].add(cur)

min_ = None
for intersection in (points[0] & points[1]):
    if min_ is None:
        min_ = manhattan_dist(intersection)
    else:
         min_ = min(min_, manhattan_dist(intersection))
print(min_)

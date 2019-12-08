with open('day3_1.txt') as f:
    wires = [line.strip().split(',') for line in f]

#wires = [s.split(',') for s in ["R8,U5,L5,D3", "U7,R6,D4,L4"]]
#wires = [s.split(',') for s in ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]]
#wires = [s.split(',') for s in ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]]

points = [set(), set()]

DIRECTIONS = {'U': (0, 1),'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def add(v1, v2):
    return tuple(sum(x) for x in zip(v1, v2))

def manhattan_dist(v1, v2=(0, 0)):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

# Find intersections
for i, wire in enumerate(wires):
    cur = (0, 0)
    for path in wire:
        dir, val = path[0], int(path[1:])
        for _ in range(val):
            cur = add(cur, DIRECTIONS[dir])
            points[i].add(cur)
intersections = points[0] & points[1]

steps = [{}, {}]

for i, wire in enumerate(wires):
    cur = (0, 0)
    _steps = 0
    for path in wire:
        dir, val = path[0], int(path[1:])
        for _ in range(val):
            cur = add(cur, DIRECTIONS[dir])
            _steps += 1
            if cur in intersections:
                steps[i][cur] = _steps

min_ = None
for intersection in steps[0]:
    if min_ is None:
        min_ = steps[0][intersection] + steps[1][intersection]
    else:
        min_ = min(min_, steps[0][intersection] + steps[1][intersection])
print(min_)

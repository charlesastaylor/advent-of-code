from itertools import combinations

from common import tadd, lcm


class Moon:
    def __init__(self, pos, vel=None):
        self.pos = pos
        self.vel = vel if vel else [0, 0, 0]

    def __str__(self):
        return 'pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>'.format(*self.pos, *self.vel)

    def _potential(self):
        return sum([abs(x) for x in self.pos])

    def _kinetic(self):
        return sum([abs(x) for x in self.vel])
    
    def energy(self):
        return self._potential() * self._kinetic()

    def state(self):
        return tuple(self.pos) + tuple(self.vel)

positions = [[5, -1, 5], [0, -14, 2], [16, 4, 0], [18, 1, 16]]
# positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
# positions = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

moons = [Moon(pos) for pos in positions]
states = set()
initial_state = tuple(moon.state() for moon in moons)

steps = 0

def get_state_of_axis(state, axis):
    return tuple((moon[axis], moon[axis + 3]) for moon in state)
cycles = {}
while len(cycles) < 3:
    # gravity
    for m1, m2 in combinations(moons, 2):
        for i in range(3):
            if m1.pos[i] < m2.pos[i]:
                m1.vel[i] += 1
                m2.vel[i] -= 1
            elif m1.pos[i] > m2.pos[i]:
                m1.vel[i] -= 1
                m2.vel[i] += 1
    # velocity
    for moon in moons:
        moon.pos = tadd(moon.pos, moon.vel)
    steps += 1
    current_state = tuple(moon.state() for moon in moons)

    for i in range(3):
        if get_state_of_axis(current_state, i) == get_state_of_axis(initial_state, i):
            if i not in cycles:
                cycles[i] = steps

print(lcm(lcm(cycles[0], cycles[1]), cycles[2]))
from itertools import combinations

from common import tadd


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

positions = [[5, -1, 5], [0, -14, 2], [16, 4, 0], [18, 1, 16]]
# positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

moons = [Moon(pos) for pos in positions]
steps = 1000

for _ in range(steps):
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

    # output
    # print(f'After {_ + 1} steps:')
    # for moon in moons:
    #     print(moon)
    
# for moon in moons:
#     print(moon.energy())
print(sum(moon.energy() for moon in moons))
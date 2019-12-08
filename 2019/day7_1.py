from itertools import permutations

from common import intcode


with open('day7.txt') as f:
    acs = [int(c) for c in f.readline().strip().split(",")]

# acs = [int(c) for c in "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")]
# acs = [int(c) for c in "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")]
# acs = [int(c) for c in "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")]

max_ = 0
for phase in permutations(range(5)):
    amp_input = 0
    for amp in range(5):
        gen = intcode(acs[:])
        gen.send(None)
        gen.send(phase[amp])
        amp_input = gen.send(amp_input)
    max_ = max(max_, amp_input)
print(max_)
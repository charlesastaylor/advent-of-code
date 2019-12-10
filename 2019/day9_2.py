from common import intcode


with open('day9.txt') as f:
    boost = [int(c) for c in f.readline().strip().split(",")]

gen = intcode(boost, False)
gen.send(None)
print(gen.send(2))
for out in gen:
    print(out)

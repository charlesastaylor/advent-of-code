from common import intcode


with open('day9.txt') as f:
    boost = [int(c) for c in f.readline().strip().split(",")]

# boost = [int(c) for c in "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(",")]
# boost = [int(c) for c in "104,1125899906842624,99".split(",")]
# boost = [int(c) for c in "1102,34915192,34915192,7,4,7,99,0".split(",")]

gen = intcode(boost, False)
gen.send(None)
print(gen.send(1))
for out in gen:
    print(out)

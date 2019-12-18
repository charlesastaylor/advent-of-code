with open('day16.txt') as f:
    in_ = f.read()

# in_ = '80871224585914546619083218645595' # 24176176.
# in_ = '19617804207202209144916044189917' # 73745418.
# in_ = '69317163492948606335995924319873' # 52432133
# in_ = '12345678'

in_ = [int(c) for c in in_]

base_pattern = [0, 1, 0, -1]
num_phases = 100
for _ in range(num_phases):
    next_ = []
    for i in range(1, len(in_) + 1):
        # caculate pattern
        pattern = []
        for x in base_pattern:
            pattern.extend([x]*i)
        pattern = pattern[1:] + pattern[0:1]
        val = 0
        for i, x in enumerate(in_):
            val += x * pattern[i % len(pattern)]
        next_.append(int(str(val)[-1]))
    in_ = next_
    # print(''.join(in_))
print(''.join(str(i) for i in in_[:8]))
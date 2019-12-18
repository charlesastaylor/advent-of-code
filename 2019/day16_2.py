with open('day16.txt') as f:
    in_ = f.read()

in_ = '3036732577212944063491565474664' # becomes 84462026.
in_ = '02935109699940807407585447034323' # becomes 78725270.
in_ = '03081770884921959731165446850517' # becomes 53553731

in_ = [int(c) for c in in_]
in_ = in_ * 10000
message_offset = int(''.join(str(c) for c in in_[:7]))

base_pattern = [0, 1, 0, -1]
num_phases = 100
for phase in range(num_phases):
    # print(f'{phase} / {num_phases} - {phase * 100 / num_phases:.2f}%', end='\r')
    next_ = []
    for i in range(1, len(in_) + 1):
        print(f'{i} / {len(in_) + 1} - {i * 100 / (len(in_) + 1):.2f}%', end='\r')
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

print(' ')
print(message_offset)
print(''.join(str(i) for i in in_[message_offset:message_offset + 8]))
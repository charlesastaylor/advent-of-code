def increasing_digits(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def has_pair_digits(n):
    s = str(n)
    return len(s) != len(set(s))

pos = []
for i in range(254032, 789860):
    if increasing_digits(i) and has_pair_digits(i):
        pos.append(i)

print(len(pos))


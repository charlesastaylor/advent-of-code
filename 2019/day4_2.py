def increasing_digits(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def has_pair_digits(n):
    s = str(n)
    return len(s) != len(set(s))

def has_strict_pair(n):
    s = str(n)
    if len(s) == len(set(s)):
        return False
    counts = [1]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counts[-1] += 1
        else:
            counts.append(1)
    return 2 in counts

pos = []
for i in range(254032, 789860):
    if increasing_digits(i) and has_strict_pair(i):
        pos.append(i)

print(len(pos))


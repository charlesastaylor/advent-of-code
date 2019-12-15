def fuel_required(mass):
    return mass // 3 - 2

if __name__ == "__main__":
    total = 0
    with open('1-1.txt') as f:
        for line in f:
            total += fuel_required(int(line.strip()))
    print(total)
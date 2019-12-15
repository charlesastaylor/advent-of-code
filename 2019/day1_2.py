def fuel_required(mass):
    required = 0
    while mass // 3 - 2 > 0:
        mass = mass // 3 - 2
        required += mass
    return required

if __name__ == "__main__":
    total = 0
    with open('1-1.txt') as f:
        for line in f:
            total += fuel_required(int(line.strip()))
    print(total)
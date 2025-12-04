#!/usr/bin/env python3

def get_banks(filename):
    banks = []
    with open(f"{filename}", "r") as f:
        lines = f.readlines();
        for line in lines:
            banks.append(line.strip())
    return banks

## Part 1
def get_total_joltage(banks):
    total = 0
    for bank in banks:
        total += get_largest_joltage(bank)
    return total

def get_largest_joltage(bank):
    l = largest = 0
    size = len(bank)

    for r in range(l + 1, size):
        num = int(bank[l] + bank[r])
        largest = max(num, largest)
        if int(bank[r]) > int(bank[l]):
            l = r

    return largest

## Part 2
def get_total_joltage_two(banks):
    total = 0
    for bank in banks:
        total += get_n_joltage(bank, 12)
    return total
    
def get_n_joltage(bank, n):
    jolts = []
    size = len(bank)
    l = 0

    while len(jolts) < n:
        r = l + 1
        limit = size - (n - (len(jolts) + 1))
        while r < limit:
            if int(bank[r]) > int(bank[l]):
                l = r
            r += 1

        jolts.append(bank[l])
        l += 1

    return int("".join(jolts))
                        


if __name__ == "__main__":
    banks = get_banks("input.txt")
    total_joltage = get_total_joltage(banks)
    print(f"For part 1 the total joltage is {total_joltage}")

    total_joltage_two = get_total_joltage_two(banks)
    print(f"For part 2 the total joltage is {total_joltage_two}")

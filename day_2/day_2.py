#!/usr/bin/env python3

def parse_ranges(filename):
    ranges = []
    with open(f"{filename}", "r") as f:
        lines = f.readlines()
        for line in lines:
            product_ranges = line.split(",")
            for product_range in product_ranges:
                range_start, range_end = product_range.split("-")
                ranges.append([int(range_start), int(range_end)])
    return ranges

## PART 1 ##
def find_double_repeat_numbers(ranges):
    repeats = []
    for product_range in ranges:
        for i in range(product_range[0], product_range[1] + 1):
            if is_double_repeat_number(i):
                repeats.append(i)
    return repeats

def is_double_repeat_number(num):
    snum = str(num)
    size = len(snum)
    mid = size // 2

    return (size > 0 and size % 2 == 0) and (snum[0:mid] == snum[mid:])


## PART 2 ##
def find_any_repeat_number(ranges):
    repeats = []
    for product_range in ranges:
        for i in range(product_range[0], product_range[1] + 1):
            if is_any_repeat_number(i):
                repeats.append(i)
    return repeats

def is_any_repeat_number(num):
    snum = str(num)
    size = len(snum)
    mid = size // 2

    if size == 1:
        return False

    # Get all the possible valid partition sizes
    partition_sizes = []
    for i in range(2, mid + 1):
        if size % i == 0:
            partition_sizes.append(size // i)
    partition_sizes.append(1)

    # Check if those partitions are equal
    for size in partition_sizes:
        if is_equal_partitions(snum, size):
            return True
    
    return False

def is_equal_partitions(s, size):
    # Partition string
    partitions = []
    for i in range(0, len(s), size):
        partitions.append(s[i:i+size])

    # Checks if all partitions equal
    for partition in partitions:
        if partition != partitions[0]:
            return False
    return True


if __name__ == "__main__":
    ranges = parse_ranges("input.txt")
    double_repeat_numbers = find_double_repeat_numbers(ranges)
    print(f"Adding up all the double repeat numbers in part 1 gives a sum of {sum(double_repeat_numbers)}")

    any_repeat_numbers = find_any_repeat_number(ranges)
    print(f"Adding up all the repeat numbers in part 2 gives a sum of {sum(any_repeat_numbers)}")

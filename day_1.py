#!/usr/bin/env python3

"""
Problem description
- Dial numbers 0-99 in order
- L = left rotation
- R = right rotation

Sample rotation
- R88 = right 88
- L50 = left 50
- Left from 0 goes to 99
- Right from 99 goes to 0
- Dial starts at 50
- Actual password number of times dial left pointing at zero after any rotation in the sequence

Example
- Dial at 5
- L10 input

5 4 3 2 1 0 99 98 97 96 95

Naiive solution:
- Left = subtract the number
- Right = add the number

How to cover boundary?
- 5 L10 = 5 - 10 = -5
- 100 - 5 = 95 = CORRECT
- 100 L99 = 100 - 99 = 1
- 1 L99 = 1 - 99 = -98 = 2

Strategy
- Positive number = modulus 100
- Negative number = modulus 100, 100 - number

Full example (start 50)
- L68, 50 - 68 = -18 = 100 - 18 = 82
- L30, 82 - 30 = 52
- R48, 52 + 48 = 100 % 100 = 0 (1)
- L5, 0 - 5 = -5 = 100 - 5 = 95
- R60, 95 + 60 = 155 % 100 = 55
- L55, 55 - 55 = 0 % 100 = 0 (2)
- L1, -1 = 100 - 1 = 99
- L99 = 99 - 99 = 0 (3)
- R14 = 0 + 14 = 14
- L82 = 14 - 82 = 100 - 68 = 32
"""

def read_input(filename):
    input = []
    with open(f"{filename}", "r") as f:
        lines = f.readlines()
        for line in lines:
            input.append(line.strip())
    return input

def transform_input(input):
    numbers = []
    for instruction in input:
        if instruction[0] == "L":
            numbers.append(-int(instruction[1:]))
        else:
            numbers.append(int(instruction[1:]))
    return numbers

def count_zero_rotations(rotations):
    result = 0
    number = 50
    for rotation in rotations:

       # Apply rotation
        number = (number + rotation) % 100

        # Count the zeroes
        if number == 0:
            result += 1

    return result

"""
Similar idea to count zero, but we also need a way to determine when a click occurs

Example
- 50 R1000 would cause ten clicks, how?
- 50 -> 0 = costs 50 = 1 click
- 0 -> 0 = costs 100 = 1 click

How to figure out number of clicks
- Number of rotations can always be figured out by abs(rotation) // 100
- Then need to figure out if the remainder is big enough to get us past zero

Example
- Start: 50
- L68 = 68 // 100 = 0
- Then see if remainder greater than 50
= 68 > 50 = true, so add 1
- 82
- L30 = 32 / 100 = 0
- 32 > 82 = 0
- 52
- R48 = 48 / 100 = 0
- 48 > (100 - 52) = 48
- 0
- L5 = 5 / 100 = 0
- 5 > 0 = true, but don't count since zero

"""
def count_zero_clicks(rotations):
    result = 0
    number = 50
    for rotation in rotations:
        result += abs(rotation) // 100
        leftover = abs(rotation) % 100

        if number != 0 and ((rotation < 0 and leftover > number) or (rotation > 0 and leftover > (100 - number))):
            result += 1

       # Apply rotation
        number = (number + rotation) % 100

        # Count the zeroes
        if number == 0:
            result += 1

    return result


if __name__ == "__main__":
    input = read_input("input.txt")
    rotations = transform_input(input)

    part_one_answer = count_zero_rotations(rotations)
    print(f"For part one, the dial was left pointing at zero {part_one_answer} times")

    part_two_answer = count_zero_clicks(rotations)
    print(f"For part two, the dial was pointed at or passed zero {part_two_answer} times")

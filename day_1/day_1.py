#!/usr/bin/env python3

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

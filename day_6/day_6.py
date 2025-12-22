#!/usr/bin/env python3

def parse_input(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            row = []
            for part in line.split():
                stripped = part.strip()
                if stripped in "+*":
                    row.append(stripped)
                else:
                    row.append(int(stripped))
            grid.append(row)
    return grid

def simple_parse(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append(line.strip("\n"))
    return grid

def solve_vertical_grid(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    total = 0
    for c in range(COLS):
        operation = grid[ROWS - 1][c]
        sub_total = grid[0][c]
        for r in range(1, ROWS - 1):
            if operation == "+":
                sub_total += grid[r][c]
            else:
                sub_total *= grid[r][c]
        total += sub_total
    return total

def multiply(arr):
    total = arr[0]
    for i in range(1, len(arr)):
        total *= arr[i]
    return total

def solve_simple_grid(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    # Parse operators out of grid
    operators = [part.strip() for part in grid[-1].split()]

    # Parse numbers out of grid
    problems = []
    buffer = []
    for c in range(COLS):
        curr_num = 0
        space_count = 0
        modifier = 1
        for r in range(ROWS - 2, -1, -1):
            num = 0
            if grid[r][c] == " ":
                space_count += 1
            else:
                num = int(grid[r][c]) * modifier
                modifier *= 10

            curr_num += num

        if (space_count != ROWS - 1): 
            buffer.append(curr_num)

        if (space_count == ROWS - 1) or (c == COLS - 1):
            problems.append(buffer.copy())
            buffer.clear()
    
    # Compute problems and get total
    total = 0
    for i in range(len(problems)):
        problem = problems[i]
        operator = operators[i]
        if operator == "*":
            total += multiply(problem)
        else:
            total += sum(problem)

    return total


if __name__ == "__main__":
    grid = parse_input("input.txt")
    total = solve_vertical_grid(grid)
    print(f"The total for part 1 is {total}")

    simple_grid = simple_parse("input.txt")
    total_two = solve_simple_grid(simple_grid)
    print(f"The total for part 2 is {total_two}")

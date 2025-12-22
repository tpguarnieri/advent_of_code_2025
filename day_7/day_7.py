#!/usr/bin/env python3

START = "S"
SPLITTER = "^"

def read_input(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]

def count_splits(grid):
    split_count = 0
    ROWS = len(grid)
    COLS = len(grid[0])

    positions = set()

    # Get starting position
    for c in range(COLS):
        if grid[0][c] == START:
            positions.add(c)

    # Find splits
    for r in range(1, ROWS):
        buffer = set()
        for c in positions:
            if grid[r][c] == SPLITTER:
                split_count += 1
                for dc in [-1, 1]:
                    new_c = c + dc
                    if 0 <= new_c < COLS:
                        buffer.add(new_c)
            else:
                buffer.add(c)
        positions = buffer

    return split_count

def count_unique_timelines(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    start_position = grid[0].index(START)
    mem = {}

    def count_paths(r, c):
        if (r, c) in mem:
            return mem[(r, c)]
        if r == ROWS:
            return 1
        
        total = 0
        if grid[r][c] == SPLITTER:
            for dc in [-1, 1]:
                new_c = c + dc 
                if 0 <= new_c < COLS:
                    total += count_paths(r + 1, new_c)
        else:
            total += count_paths(r + 1, c)

        mem[(r, c)] = total
        return total

    return count_paths(0, start_position)


if __name__ == "__main__":
    grid = read_input("input.txt")
    split_count = count_splits(grid)
    print(f"The split count for part 1 is {split_count}")

    unique_timeline_count = count_unique_timelines(grid)
    print(f"The number of unique timelines for part 2 is {unique_timeline_count}")

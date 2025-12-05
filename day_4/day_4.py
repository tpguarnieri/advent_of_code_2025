#!/usr/bin/env python3
from collections import deque

PAPER = "@"
EMPTY = "."
ADJACENT = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]]


def fetch_grid(filename):
    grid = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            row = list(line)
            grid.append(row)
    return grid

def count_movable_paper(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == PAPER and count_paper_neighbors(r, c, grid) < 4:
                result += 1

    return result

def count_removable_paper(grid):
    rows = len(grid)
    cols = len(grid[0])
    neighbor_map = {}
    q = deque()

    # Setup map showing count of neighbors for paper and initial BFS queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == PAPER:
                neighbor_count = count_paper_neighbors(r, c, grid)
                neighbor_map[(r, c)] = neighbor_count
                if neighbor_count < 4:
                    q.append((r, c))

    # BFS counting how much we can remove
    removable_count = 0
    seen = set()
    while q:
        r, c = q.popleft()
        if (r, c) in seen:
            continue
        
        removable_count += 1
        seen.add((r, c))
        
        for dr, dc in ADJACENT:
            new_r = r + dr 
            new_c = c + dc
            if (new_r, new_c) in neighbor_map and (new_r, new_c) not in seen:
                neighbor_map[(new_r, new_c)] -= 1
                if neighbor_map[(new_r, new_c)] < 4:
                    q.append((new_r, new_c))

    return removable_count


def count_paper_neighbors(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for dr, dc in ADJACENT:
        new_r = r + dr
        new_c = c + dc 
        if (0 <= new_r < rows) and (0 <= new_c < cols) and grid[new_r][new_c] == PAPER:
            count += 1

    return count





if __name__ == "__main__":
    grid = fetch_grid("input.txt")
    pt1_count = count_movable_paper(grid)
    print(f"For part 1 the number of movable rolls of paper is {pt1_count}")

    pt2_count = count_removable_paper(grid)
    print(f"For pat 2 the number of movable rolls of paper is {pt2_count}")

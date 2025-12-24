#!/usr/bin/env python3

def read_file(filename):
    coordinates = []
    with open(filename, "r") as f:
        for line in f:
            sx, sy = line.split(",")
            coordinates.append((int(sx), int(sy)))
    return coordinates

def calculate_area(point_a, point_b):
    return (abs(point_a[0] - point_b[0]) + 1) * (abs(point_a[1] - point_b[1]) + 1)

def get_largest_area(coordinates):
    n = len(coordinates)
    total = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            a = coordinates[i]
            b = coordinates[j]
            area = calculate_area(a, b)
            total = max(total, area)
    return total

def compress_coordinates(coordinates):
    x_coords = list(set(c[0] for c in coordinates))
    y_coords = list(set(c[1] for c in coordinates))
    x_coords.sort()
    y_coords.sort()

    x_map = {key: i for i, key in enumerate(x_coords)}
    y_map = {key: i for i, key in enumerate(y_coords)}

    compressed = []
    for x, y in coordinates:
        new_coord = (x_map[x], y_map[y])
        compressed.append(new_coord) 

    return compressed

def get_points_between(point_a, point_b):
    points = set()
    a_x, a_y = point_a
    b_x, b_y = point_b

    # When columns are the same add vertical
    if a_x == b_x:
        low, high = (a_y, b_y) if a_y <= b_y else (b_y, a_y)
        for y in range(low + 1, high):
            points.add((a_x, y))
    # When rows are the same add horizontal
    else:
        low, high = (a_x, b_x) if a_x <= b_x else (b_x, a_x)
        for x in range(low + 1, high):
            points.add((x, a_y))

    return points

def get_boundary(coordinates):
    boundary = set()
    n = len(coordinates)

    for i in range(n):
        curr = coordinates[i]
        nxt = coordinates[(i + 1) % n]
        between = get_points_between(curr, nxt)
        boundary.add(curr)
        boundary.add(nxt)
        boundary |= between
   
    return boundary

def get_grid(boundary):
    ROWS = max(c[1] for c in boundary)
    COLS = max(c[0] for c in boundary)

    grid = []
    for y in range(ROWS + 1):
        row = []
        for x in range(COLS + 1):
            if (x, y) in boundary:
                row.append("#")
            else:
                row.append(".")
        grid.append(row)

    return grid

def get_inner_point(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    for r in range(ROWS):
        crossings = 0
        for c in range(0, COLS - 1):
            curr = grid[r][c]
            nxt = grid[r][c + 1]
            if curr == "." and crossings % 2 == 1:
                return (c, r)
            if curr + nxt in ["#.", ".#"]:
                crossings += 1

def get_all_points(coordinates):
    # Get boundary of polygon
    boundary = get_boundary(coordinates)

    # Get grid representation showing polygon
    grid = get_grid(boundary)
    ROWS = len(grid)
    COLS = len(grid[0])

    # Get a point inside the polygon
    inner_point = get_inner_point(grid)
    if inner_point is None:
        return boundary

    # Flood fill DFS to get all inner points
    inner_points = set()
    stack = [inner_point]
    while stack:
        c, r = stack.pop() 
        if grid[r][c] == "#" or (c, r) in inner_points:
            continue

        inner_points.add((c, r))
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_c = c + dc
            new_r = r + dr
            if (0 <= new_c < COLS) and (0 <= new_r < ROWS) and grid[new_r][new_c] != "#" and (new_c, new_r) not in inner_points:
                stack.append((new_c, new_r))

    return inner_points | boundary

def get_rectangle_perimeter(point_a, point_b):
    perimeter = set()
    a_x, a_y = point_a
    b_x, b_y = point_b

    min_x, max_x = (a_x, b_x) if a_x <= b_x else (b_x, a_x)
    min_y, max_y = (a_y, b_y) if a_y <= b_y else (b_y, a_y)

    for x in range(min_x, max_x + 1):
        perimeter.add((x, min_y))
        perimeter.add((x, max_y))

    for y in range(min_y, max_y + 1):
        perimeter.add((min_x, y))
        perimeter.add((max_x, y))

    return perimeter

def get_largest_red_green_area(coordinates):
    # Compress coordinates to reduce problem space
    compressed = compress_coordinates(coordinates)

    # Get all points that make up the polygon
    all_points = get_all_points(compressed)

    # Calculate the area for each rectangle, filtering to valid blue green grids
    n = len(compressed)
    total = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            a = compressed[i]
            b = compressed[j]
            rectangle_perimeter = get_rectangle_perimeter(a, b)
            if rectangle_perimeter.issubset(all_points):
                area = calculate_area(coordinates[i], coordinates[j])
                total = max(total, area)
    return total


if __name__ == "__main__":
    coordinates = read_file("input.txt")

    largest_area = get_largest_area(coordinates)
    print(f"For part 1, the largest area is {largest_area}")

    largest_blue_green_area = get_largest_red_green_area(coordinates)
    print(f"For part 2, the largest red green area is {largest_blue_green_area}")

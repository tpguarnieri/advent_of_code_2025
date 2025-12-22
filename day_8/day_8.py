#!/usr/bin/env python3
import math
from collections import defaultdict, deque

class Point:
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})" 
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y. other.z)

def get_points(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            coords = [int(s.strip()) for s in line.split(",")]
            point = Point(coords[0], coords[1], coords[2])
            points.append(point)
    return points

def connect_n_circuits(n, points):
    # Compute the distance for all pairwise connections, and sort by the shortest
    distances = get_shortest_distances(points)
    n = min(n, len(distances))

    # Connect the first n, and construct adjacency list for graph
    graph = defaultdict(list)
    for i in range(n):
        x, y = distances[i][1:] 
        graph[x].append(y)
        graph[y].append(x)

    # For each point do a BFS traversal to get size of circuits
    visited = set()
    largest = []
    for point in points:
        if point not in visited:
            largest.append(get_size(point, graph, visited))

    # Return three largest multiplied together
    largest.sort(reverse=True)
    return multiply(largest[:3])

def get_size(start, graph, visited=None):
        if visited is None:
            visited = set()

        size = 0
        q = deque([start])
        while q:
            point = q.popleft()
            if point in visited:
                continue

            visited.add(point)
            size += 1
            for neighbor in graph[point]:
                if neighbor not in visited:
                    q.append(neighbor)

        return size


def connect_until_one_circuit(points):
    distances = get_shortest_distances(points) 

    n = 1
    while True:
        graph = defaultdict(list)
        for i in range(n):
            x, y = distances[i][1:] 
            graph[x].append(y)
            graph[y].append(x)

        last_points = distances[n - 1][1:]
        first, second = last_points
        if get_size(first, graph) == len(points):
            return first.x * second.x

        n += 1

def get_shortest_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = get_distance(points[i], points[j])
            distances.append((distance, points[i], points[j]))
    distances.sort(key=lambda a: a[0]) 
    return distances


def get_distance(p: Point, q: Point):
    return math.sqrt((p.x - q.x)**2 + (p.y - q.y)**2 + (p.z - q.z)**2)

def multiply(arr):
    total = arr[0]
    for i in range(1, len(arr)):
        total *= arr[i]
    return total


if __name__ == "__main__":
    points = get_points("input.txt")
    largest_product = connect_n_circuits(1000, points)
    print(f"For part 1, multipling the length of the three largest circuits gives a product of {largest_product}")

    last_product = connect_until_one_circuit(points)
    print(f"For part 2, the result of getting the last point to make one circuit and multiplying the x gives {last_product}")

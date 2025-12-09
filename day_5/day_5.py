#!/usr/bin/env python3

def parse_input(filename):
    with open(filename, "r") as f:
        intervals = []
        ingredients = []
        read_ingredients = False
        
        for line in f:
            if line == "\n":
                read_ingredients = True
                continue

            if not read_ingredients:
                start, end = line.strip().split("-")
                intervals.append((int(start), int(end)))
            else:
                ingredients.append(int(line.strip())) 

        return intervals, ingredients

def fresh_count(intervals, ingredients):
    count = 0
    for ingredient in ingredients:
        for start, end in intervals:
            if start <= ingredient <= end:
                count += 1
                break 
    return count

def fresh_range_count(intervals):
    count = 0
    intervals.sort(key=lambda interval: interval[0])
    stack = [intervals[0]]

    # Merge intervals
    for i in range(1, len(intervals)):
        top_start, top_end = stack[-1] 
        curr_start, curr_end = intervals[i] 
        if top_start <= curr_start <= top_end:
            new_interval = (min(top_start, curr_start), max(top_end, curr_end))
            stack.pop()
            stack.append(new_interval)
        else:
            stack.append(intervals[i])


    # Get new ingredient count
    for start, end in stack:
        count += (end - start) + 1

    return count


if __name__ == "__main__":
    intervals, ingredients = parse_input("input.txt")
    total_fresh = fresh_count(intervals, ingredients)
    total_fresh_range_count = fresh_range_count(intervals)
    print(f"For part 1 the answer is {total_fresh}")
    print(f"For part 2 the answer is {total_fresh_range_count}")

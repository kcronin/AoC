#!/usr/bin/env python3

# every point has coordinates
# top left is 0,0
# bottom right is max(columns), max(rows)
# {'coord': 'times_crossed'} ?

example = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

example_result = 5

#data = example
data = open('5.input', 'r').read()

considered_lines = []

for line in data.split("\n"):
    if len(line) > 0:
        start, finish = line.split(" -> ")
        start, finish = eval(start), eval(finish)
        if start[0] == finish[0] or start[1] == finish[1]:
            considered_lines.append([start, finish])
#print(considered_lines)

# x = across
# y = down
# considered_lines = [[(0,9), (5,9)], [(9,4), (3,4)], [(2,4), (2,1)]]

# points crossed by considered_lines[0] are 0-5,9 or 0,9; 1,9; etc thru 5,9
# points crossed by considered_lines[2] are 2,4-1 or 2,4; 2,3; 2,2; 2,1 <-- note this was an "upward" movement, need to figure that out

total_points_crossed = {}
# this will look like {(0,9): 1, (1,9): 2 ... }

def get_points(line):
    points = []
    start_x, start_y, end_x, end_y = line[0][0], line[0][1], line[1][0], line[1][1]
    inc = 1
    if start_x == end_x: #vert
        if start_y > end_y:
            inc = -1
        for movement in range(start_y, end_y, inc):
            points.append((start_x, movement))
    else: #horiz
        if start_x > end_x:
            inc = -1
        for movement in range(start_x, end_x, inc):
            points.append((movement, start_y))
    points.append(line[1])
    return points


for line in considered_lines:
    points_crossed = get_points(line)
    for point in points_crossed:
        total_points_crossed[point] = total_points_crossed.get(point, 0) + 1

#print(total_points_crossed)
# find all values greater than 1
result = len([v for v in total_points_crossed.values() if v > 1])
print(result)

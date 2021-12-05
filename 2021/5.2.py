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

#data = example
data = open('5.input', 'r').read()
#data = open('5.input', 'r').readlines()

considered_lines = []

for line in data.split("\n"):
    if len(line) > 0:
        start, finish = line.split(" -> ")
        considered_lines.append([eval(start), eval(finish)])

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
        #print(f"Got vertical line: {line}")
        if start_y > end_y:
            inc = -1
        for movement in range(start_y, end_y, inc):
            points.append((start_x, movement))
        inc = 1
    elif start_y == end_y: #horiz
        #print(f"Got horizontal line: {line}")
        if start_x > end_x:
            inc = -1
        for movement in range(start_x, end_x, inc):
            points.append((movement, start_y))
        inc = 1
    else: # diag
        #print(f"Got diagonal line: {line}")
        x_values, y_values = [], []
        if start_x > end_x: # we need to decrease x to get from start to end
            inc = -1
        for x_movement in range(start_x, end_x, inc):
            x_values.append(x_movement)
        #print(f"Got x_values {x_values} for line {line}")
        inc = 1

        if start_y > end_y: # we need to decrease y to get from start to end
            inc = -1
        for y_movement in range(start_y, end_y, inc):
            y_values.append(y_movement)
        #print(f"Got y_values {y_values} for {line}")
        points = list(zip(x_values, y_values))
        inc = 1

    points.append(line[1])
    #print(f"For line {line} got points {points}")
    return points


for line in considered_lines:
    points_crossed = get_points(line)
    for point in points_crossed:
        total_points_crossed[point] = total_points_crossed.get(point, 0) + 1

#print(total_points_crossed)
# find all values greater than 1
result = len([v for v in total_points_crossed.values() if v > 1])
print(result)

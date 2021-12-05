#!/usr/bin/env python3

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

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_points(self):
        points = []
        start_x, start_y, end_x, end_y = self.start[0], self.start[1], self.end[0], self.end[1]
        x_movement = range(start_x, end_x) if start_x <= end_x else range(start_x, end_x, -1)
        y_movement = range(start_y, end_y) if start_y <= end_y else range(start_y, end_y, -1)
        if len(x_movement) == 0: # vertical
            for m in y_movement:
                points.append((start_x, m))
        elif len(y_movement) == 0: # horizontal
            for m in x_movement:
                points.append((m, start_y))
        else: # diag
            points = list(zip(x_movement, y_movement))
        points.append(self.end)
        return points

def get_total_points(lines, ignore_diag=True):
    total_points_crossed = {}
    for line in lines:
        diagonal = (line[0][0] != line[1][0] and line[0][1] != line[1][1])
        if ignore_diag and diagonal:
            continue
        points_crossed = Line(line[0], line[1]).get_points()
        for point in points_crossed:
            total_points_crossed[point] = total_points_crossed.get(point, 0) + 1
    return len([v for v in total_points_crossed.values() if v > 1])

def part_one(lines):
    return get_total_points(lines)

def part_two(lines):
    return get_total_points(lines, ignore_diag=False)

lines = []

for line in data.split("\n"):
    if len(line) > 0:
        start, finish = line.split(" -> ")
        lines.append([eval(start), eval(finish)])

print(f"Part one: {part_one(lines)}")
print(f"Part two: {part_two(lines)}")

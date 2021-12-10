#!/usr/bin/env python3

data = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

data = open('9.input', 'r').read()

lines = [list(map(int, line)) for line in data.split("\n") if len(line) > 0]

risk = 0

def is_least(x, comps):
    return(all(x < val for val in comps))

for i, line in enumerate(lines):
    if i == 0: #top edge
        for y, x in enumerate(line):
            if y == 0:
                comps = [line[y+1], lines[i+1][y]]
            elif y == len(line)-1:
                comps = [line[y-1], lines[i+1][y]]
            else:
                comps = [line[y-1], line[y+1], lines[i+1][y]]
            if is_least(x, comps): risk += x+1
    elif i == len(lines)-1: #bottom edge
        for y, x in enumerate(line):
            if y == 0:
                comps = [line[y+1], lines[i-1][y]]
            elif y == len(line)-1:
                comps = [line[y-1], lines[i-1][y]]
            else:
                comps = [line[y-1], line[y+1], lines[i-1][y]]
            if is_least(x, comps): risk += x+1
    else:
        for y, x in enumerate(line):
            if y == 0:
                comps = [line[y+1], lines[i-1][y], lines[i+1][y]]
            elif y == len(line)-1:
                comps = [line[y-1], lines[i-1][y], lines[i+1][y]]
            else:
                comps = [line[y-1], line[y+1], lines[i-1][y], lines[i+1][y]]
            if is_least(x, comps): risk += x+1

print(risk)

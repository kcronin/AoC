#!/usr/bin/env python3

from collections import defaultdict

with open('input.txt', 'r') as f:
    instructions = f.readlines()

lights = defaultdict(dict)

for inst in instructions:
    inst = inst.replace('turn ', '')
    direction, start, _, end = inst.split()
    x_range = range(int(start.split(',')[0]), int(end.split(',')[0]) + 1)
    y_range = range(int(start.split(',')[1]), int(end.split(',')[1]) + 1)
    for x in x_range:
        for y in y_range:
            if not lights[x].get(y):
                lights[x][y] = 0

            if direction == 'toggle':
                if lights[x][y] == 0:
                    lights[x][y] = 1
                else:
                    lights[x][y] = 0

            elif direction == 'on':
                lights[x][y] = 1
            else:
                lights[x][y] = 0

lights_on = 0

for x_coord in lights:
    for y_coord in lights[x_coord]:
        if lights[x_coord][y_coord] == 1:
            lights_on += 1
print(lights_on)

#!/usr/bin/env python3

input = open('2.input', 'r').readlines()

aim, horiz, depth = 0, 0, 0

def calcaim(aim, x, dir):
    newaim = aim + x if dir == "down" else aim - x
    return newaim

for coord in input:
    dir, x = coord.split()
    if dir.strip() in ["down", "up"]:
        aim = calcaim(aim, int(x), dir)
    else: # forward
        horiz += int(x)
        depth += aim * int(x)

print(horiz * depth)

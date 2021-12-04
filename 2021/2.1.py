#!/usr/bin/env python3

input = open('2.input', 'r').readlines()

h, d = 0, 0

def calcdepth(current, new, dir):
    newdepth = current + int(new) if dir == "down" else current - int(new)
    return newdepth

for coord in input:
    if coord.split()[0] == "forward":
        h += int(coord.split()[1].strip())
    else:
        d = calcdepth(d, coord.split()[1].strip(), coord.split()[0])

print(h * d)

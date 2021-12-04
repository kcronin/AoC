#!/usr/bin/env python3

depths = open('1.input', 'r').readlines()

increases = 0

sumdepths = []

for i, depth in enumerate(depths):

    if i <= len(depths)-3:
        sumdepth = int(depth.strip()) + int(depths[i+1].strip()) + int(depths[i+2].strip())
        sumdepths.append(sumdepth)

for i, depth in enumerate(sumdepths):
    if i > 0:
        if depth > sumdepths[i-1]:
            increases += 1

print(increases)

#!/usr/bin/env python3

depths = open('1.input', 'r').readlines()

increases = 0

i = 1

for depth in depths[i:]:

    if int(depth.strip()) > int(depths[i-1].strip()):
        increases += 1
    i += 1

print(increases)

#!/usr/bin/env python3

max_cals = 0
with open('input.txt', 'r') as input:
    for elf in input.read().split("\n\n"):
        cals = sum([int(x) for x in elf.split('\n') if x])
        if cals > max_cals:
            max_cals = cals
print(max_cals) # 74394

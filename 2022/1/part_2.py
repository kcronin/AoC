#!/usr/bin/env python3

calories = []
with open('input.txt', 'r') as input:
    for elf in input.read().split("\n\n"):
        cals = sum([int(x) for x in elf.split('\n') if x])
        calories.append(cals)
print(sum(sorted(calories)[-3:])) # 212836

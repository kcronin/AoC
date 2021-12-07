#!/usr/bin/env python3

import statistics

data = open('7.input', 'r').read()
#data = "16,1,2,0,4,2,7,1,2,14"

data = list(map(int, data.split(",")))

def part_one(data):
    median = statistics.median(data)
    fuel = 0
    for i in data:
        fuel += abs(i - median)
    return int(fuel)

def part_two(data):
    mean = int(statistics.mean(data))
    potentials = [mean-1, mean, mean+1]
    fuelcosts = {}
    for x in potentials:
        for pos in data:
            moves = abs(pos - x)
            for m in range(moves+1):
                fuelcosts[x] = fuelcosts.get(x, 0) + m
    return min(fuelcosts.values())

print(f"Part one: {part_one(data)}")
print(f"Part two: {part_two(data)}")

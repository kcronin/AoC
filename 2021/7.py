#!/usr/bin/env python3

import statistics

data = open('7.input', 'r').read()
#data = "16,1,2,0,4,2,7,1,2,14"

data = list(map(int, data.split(",")))

median = statistics.median(data)

fuel = 0

for i in data:
    fuel += abs(i - median)

print(int(fuel))

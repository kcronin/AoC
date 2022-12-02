#!/usr/bin/env python3
import math

def gen_footage(dim_list):
    l, w, h = dim_list
    sides = [2*l*w, 2*w*h, 2*h*l]
    return sum(sides) + int(min(sides) / 2)

def gen_ribbon(dim_list):
    bow = math.prod(dim_list)
    ribbon = sum(sorted(dim_list)[:2])*2
    return ribbon + bow

totalsqft = 0
total_ribbon = 0
with open('input.txt', 'r') as f:
    dimensions = f.readlines()
    for dim in dimensions:
        dim_list = [int(x.strip()) for x in dim.split('x') if x]
        totalsqft += gen_footage(dim_list)
        total_ribbon += gen_ribbon(dim_list)

print(totalsqft)
print(total_ribbon)

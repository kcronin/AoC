#!/usr/bin/env python3

input = open('3.input', 'r').readlines()

counts = {}
[counts.setdefault(x, [0, 0]) for x in range(len(input[0].strip()))]

for binary in input:
    binary = binary.strip()
    for pos, val in enumerate(binary):
        counts[pos][int(val)] += 1

gamma = ''

for pos in counts:
    posmax = max(range(len(counts[pos])), key = counts[pos].__getitem__)
    gamma += str(posmax)
    epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])

power = int(gamma, 2) * int(epsilon, 2)
print(power)

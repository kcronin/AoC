#!/usr/bin/env python3

input = open('2.1.input', 'r').readlines()

valid = 0
for item in input:
    policy, password = item.split(':')
    positions, letter = policy.split()
    pos1, pos2 = positions.split('-')
    if (password.strip()[int(pos1)-1] == letter and password.strip()[int(pos2)-1] != letter) or (password.strip()[int(pos1)-1] != letter and password.strip()[int(pos2)-1] == letter):
        print(f"OK: {password.strip()} has {letter} at either position {pos1} or {pos2}.")
        valid += 1

print(valid)

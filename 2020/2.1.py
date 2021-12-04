#!/usr/bin/env python3

input = open('2.1.input', 'r').readlines()

valid = 0
for item in input:
    policy, password = item.split(':')
    minmax, letter = policy.split()
    min, max = minmax.split('-')
    if int(min) <= password.strip().count(letter) <= int(max):
        print(f"OK: {password.strip()} has at least {min} and at most {max} of {letter}.")
        valid += 1

print(valid)

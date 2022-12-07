#!/usr/bin/env python3

with open('input.txt') as f:
    letters = f.read().strip()

# initial solution
def parse_letters(num):
    for i, c in enumerate(letters):
        if i < num-1:
            continue
        if len(set(letters[i-(num-1):i+1])) != num:
            continue
        print(f"Found {letters[i-(num-1):i+1]} at position {i+1}.")
        break

# rethought solution
def parse_letters2(num):
    i = num
    while i < len(letters):
        candidate = letters[i-num:i]
        if len(set(candidate)) != num:
            i += 1
            continue
        print(i)
        break

#parse_letters(4) # 1566
#parse_letters(14) # 2265
parse_letters2(4)
parse_letters2(14)

#!/usr/bin/env python3

vowels = ['a', 'e', 'i', 'o', 'u']
naughty = ['ab', 'cd', 'pq', 'xy']
nice = 0

def check_naughty(string):
    for n in naughty:
        if string.find(n) != -1:
            return 1
    return 0

def check_vowels(string):
    num_v = len([c for c in string if c in vowels])
    return num_v

def check_repeats(string):
    for i, c in enumerate(string):
        if i <= len(string)-2:
            if string[i] == string[i+1]:
                return 1
    return 0

with open('input.txt', 'r') as f:
    strings = f.readlines()

for string in strings:
    string = string.strip()
    # check for naughty strings, continue if found
    if check_naughty(string):
        continue
    # check for at least three vowels, continue if not
    if check_vowels(string) < 3:
        continue
    # check for double letters
    if not check_repeats(string):
        continue
    nice += 1

print(nice)

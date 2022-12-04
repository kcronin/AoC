#!/usr/bin/env python3

import re

nice = 0
total = 0
strings = [
        "hvhtzxzqqjkmpbqj",
        "xxyxx",
        "uurcxstgmygtbstg",
        "ieodomkazucvgmuy",
        ]

def check_pairs(string):
    for i in range(len(string)-3):
        candidate = string[i:i+2]
        if candidate in string[i+2:]:
            return 1
    return 0

def check_aba(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return 1
    return 0

with open('input.txt', 'r') as f:
    strings = f.readlines()

for string in strings:
    string = string.strip()
    if check_pairs(string) and check_aba(string):
        nice += 1

print(nice)

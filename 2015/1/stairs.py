#!/usr/bin/env python3

instructions = open("input.txt", "r").read().strip()
# part 1
print(instructions.count("(") - instructions.count(")"))

# part 2
floor = 0
for index,char in enumerate(instructions):
    if char == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(index + 1)
        break

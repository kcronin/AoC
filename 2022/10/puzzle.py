#!/usr/bin/env python3

filename = 'input.txt'

with open(filename) as f:
    instructions = [inst.strip() for inst in f]

X, cycle, strength = 1, 0, 0
signal_cycle = 20

def execute():
    global cycle, strength, signal_cycle
    cycle += 1
    if cycle == signal_cycle:
        strength += cycle * X
        signal_cycle += 40

for inst in instructions:
    execute() # increment cycle, but we're still on the current instruction
    if inst != 'noop':
        execute() # increment cycle again
        X += int(inst.split()[1]) # add current instruction to X

print(strength)

class Sprite():
    def __init__(self, center):
        self.pixels = range(center-1, center+2)

X, cycle, row = 1, 0, 0

rows = [''] * 6

def execute2():
    global cycle, row
    cycle += 1
    if cycle != 1:
        if (cycle - 1) % 40 == 0: # start a new row
            row += 1

def draw(row, cycle, sprite):
    if row > 0:
        row_pos = cycle - 1 - 40 * row
    else:
        row_pos = cycle

    if row_pos in sprite.pixels:
        rows[row] = rows[row] + '#'
    else:
        rows[row] = rows[row] + '.'

for inst in instructions:
    execute2()
    sprite = Sprite(X)

    draw(row, cycle, sprite)

    if inst != 'noop':
        execute2()
        draw(row, cycle, sprite)
        X += int(inst.split()[1])

for row in rows:
    print(row)

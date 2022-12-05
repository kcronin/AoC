#!/usr/bin/env python3

"""
[T]     [Q]             [S]
[R]     [M]             [L] [V] [G]
[D] [V] [V]             [Q] [N] [C]
[H] [T] [S] [C]         [V] [D] [Z]
[Q] [J] [D] [M]     [Z] [C] [M] [F]
[N] [B] [H] [N] [B] [W] [N] [J] [M]
[P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
[B] [W] [N] [P] [D] [V] [G] [L] [T]
 1   2   3   4   5   6   7   8   9
"""

# top to bottom

def get_stacks():
    return [
    ['T', 'R', 'D', 'H', 'Q', 'N', 'P', 'B'],
    ['V', 'T', 'J', 'B', 'G', 'W'],
    ['Q', 'M', 'V', 'S', 'D', 'H', 'R', 'N'],
    ['C', 'M', 'N', 'Z', 'P'],
    ['B', 'Z', 'D'],
    ['Z', 'W', 'C', 'V'],
    ['S', 'L', 'Q', 'V', 'C', 'N', 'Z', 'G'],
    ['V', 'N', 'D', 'M', 'J', 'G', 'L'],
    ['G', 'C', 'Z', 'F', 'M', 'P', 'T']
    ]

def prep_input():
    return_list = []
    with open('input.txt') as f:
        instructions = f.readlines()
    for inst in instructions:
        _, num, _, from_stack, _, to_stack = inst.strip().split()
        return_list.append([int(x) for x in [num, from_stack, to_stack]])

    return return_list


def part_one(instructions):
    stacks = get_stacks()
    for inst in instructions:
        for i in range(inst[0]):
            stacks[inst[2]-1].insert(0, stacks[inst[1]-1].pop(0))

    print(''.join([stack[0] for stack in stacks]))

def part_two(instructions):
    stacks = get_stacks()
    for inst in instructions:
        to_move = stacks[inst[1]-1][:inst[0]]
        for i in range(len(to_move)):
            stacks[inst[2]-1].insert(i, to_move[i])
        stacks[inst[1]-1] = stacks[inst[1]-1][len(to_move):]

    print(''.join([stack[0] for stack in stacks]))


if __name__ == "__main__":
    instructions = prep_input()
    part_one(instructions) # ZBDRNPMVH
    part_two(instructions) # WDLPFNNNB

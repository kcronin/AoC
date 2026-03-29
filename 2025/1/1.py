#!/usr/bin/env python3

def get_result(current_value, instruction):
    zeros_this_step = 0
    instruction_value = int(instruction[1:])
    if instruction[0] == 'L':
        if instruction_value >= current_value:
            # (abs(50 - 68) + 100) // 100
            zeros_this_step = (abs(current_value - instruction_value) + 100) // 100
        else:
            zeros_this_step = current_value - instruction_value // 100

        new_value = current_value - (instruction_value % 100)
        if new_value < 0:
            new_value += 100

    elif instruction[0] == 'R':
        zeros_this_step = (current_value + instruction_value) // 100
        new_value = current_value + (instruction_value % 100)
        if new_value >= 100:
            new_value -= 100

    print(new_value, zeros_this_step)
    return new_value, zeros_this_step

input = "L68 L30 R48 L5 R60 L55 L1 L99 R14 L82"

instructions = input.split()
# instructions = open("1.txt").readlines()
current_value = 50
total_zeros = 0
for instruction in instructions:
    current_value, zeros_this_step = get_result(current_value, instruction.strip())
    total_zeros += zeros_this_step

print(total_zeros)

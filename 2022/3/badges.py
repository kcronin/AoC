#!/usr/bin/env python3

items = ['vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']

def get_pri(shared):
    pri = ord(shared) - 38 if shared.isupper() else ord(shared) - 96
    return pri

with open('input.txt') as f:
    items = f.readlines()

def part_one():
    total_pri = 0
    for item in items:
        item = item.strip()
        compartment_1 = set(item[:int(len(item)/2)])
        compartment_2 = set(item[int(len(item)/2):])
        shared = compartment_1.intersection(compartment_2)
        if len(shared) == 1: # valid
            shared = list(shared)[0]
            pri = get_pri(shared)
            total_pri += pri

    print(total_pri)

def part_two():
    total_pri = 0
    i = 0
    while i < len(items):
        group = items[i:i+3]
        elf1 = set(group[0].strip())
        elf2 = set(group[1].strip())
        elf3 = set(group[2].strip())

        comp_1 = elf1.intersection(elf2)
        final = comp_1.intersection(elf3)

        if len(final) == 1: # valid
            final = list(final)[0]
            pri = get_pri(final)
            total_pri += pri
        i += 3

    print(total_pri)

if __name__ == "__main__":
    part_one() # 8233
    part_two() # 2821


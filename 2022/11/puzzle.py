#!/usr/bin/env python3

import math

filename = 'input.txt'

class Monkey():
    def __init__(self, worry_levels=[], operation=[], test=0, if_true=0, if_false=0):
        self.worry_levels = worry_levels
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

def get_monkeys():
    monkeylist = []
    with open(filename) as f:
        while True:
            line = f.readline()

            if not line:
                break

            if line != "\n":
                line = line.strip()

                if line.startswith('Monkey'): # new monkey!
                    m = Monkey()
                m.items = f.readline().strip().split(': ')[-1].replace(' ', '').split(',') # ['79', '98']
                m.operation = [x.replace(' ', '') for x in f.readline().strip().split()[4:]] # ['*', '19']
                m.test = int(f.readline().strip().split()[-1]) # 23
                m.if_true = int(f.readline().strip().split()[-1]) # 2
                m.if_false = int(f.readline().strip().split()[-1]) # 3
                m.num_inspected = 0

                monkeylist.append(m)
    return monkeylist

def string_to_math(operator, a, b):
    match operator:
        case '*':
            return a * b
        case '+':
            return a + b

def round(monkeys, worry_divisor, mod):
    for monkey in monkeys:
        if len(monkey.items) == 0:
            continue
        for _ in range(len(monkey.items)):
            item_worry_level = int(monkey.items.pop(0))
            if monkey.operation[1] == 'old':
                b = item_worry_level
            else:
                b = int(monkey.operation[1])

            new_worry_level = string_to_math(monkey.operation[0], item_worry_level, b) # '*', 79, 19
            # relax?
            new_worry_level = math.floor(new_worry_level / worry_divisor) % mod
            # throw!
            if new_worry_level % monkey.test == 0:
                monkeys[monkey.if_true].items.append(new_worry_level)
            else:
                monkeys[monkey.if_false].items.append(new_worry_level)
            monkey.num_inspected += 1

def get_total(monkeys):
    total_inspected = []
    for monkey in monkeys:
        total_inspected.append(monkey.num_inspected)
    monkey_business = sorted(total_inspected)[-1] * sorted(total_inspected)[-2]
    return monkey_business

monkeys = get_monkeys()
mod = math.prod([m.test for m in monkeys]) # thanks @bgreenlee
# part 1
for _ in range(20):
    round(monkeys, 3, mod)
print(get_total(monkeys))

monkeys = get_monkeys()
# part 2
for _ in range(10000):
    round(monkeys, 1, mod)
print(get_total(monkeys))

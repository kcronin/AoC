#!/usr/bin/env python3

with open('input.txt') as f:
    input = f.readlines()

# there are probably stdlibs to do these range comparisons but ¯\_(ツ)_/¯

def part_one():
    total = 0
    for i in input:
        i = i.strip()
        a, b = i.split(',')
        if ((int(a.split('-')[0]) >= int(b.split('-')[0]) and int(a.split('-')[1]) <= int(b.split('-')[1])) or
           (int(a.split('-')[0]) <= int(b.split('-')[0]) and int(a.split('-')[1]) >= int(b.split('-')[1]))):
            total += 1
    return total

def part_two():
    total = 0
    for i in input:
        i = i.strip()
        a, b = i.split(',')
        for z in range(int(a.split('-')[0]), int(a.split('-')[1])+1):
            if z in range(int(b.split('-')[0]), int(b.split('-')[1])+1):
                total += 1
                break
    return total

if __name__ == "__main__":
    print(part_one()) # 471
    print(part_two()) # 888

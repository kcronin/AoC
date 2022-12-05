#!/usr/bin/env python3

def prep_input():
    with open('input.txt') as f:
        input = f.readlines()

    elves_a = []
    elves_b = []
    for pair in input:
        a, b = pair.strip().split(',')
        elves_a.append([int(x) for x in a.split('-')])
        elves_b.append([int(x) for x in b.split('-')])
    return zip(elves_a, elves_b)

def find_overlaps(elves):
    total_1 = 0
    total_2 = 0
    for pair in elves:
        # part one
        if ((pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or
            (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])):
            total_1 += 1
        # part two
        for z in range(pair[0][0], pair[0][1]+1):
            if z in range(pair[1][0], pair[1][1]+1):
                total_2 += 1
                break

    return total_1, total_2 # 471, 888

if __name__ == "__main__":
    elves = prep_input()
    print(find_overlaps(elves))

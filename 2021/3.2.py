#!/usr/bin/env python3

input = open('3.input', 'r').readlines()

def get_rating(binlist, element, i=0):
    counts = [0, 0]
    for x in binlist:
        x = x.strip()
        counts[int(x[i])] += 1
    if len(set(counts)) == 1:
        keep = 1 if element == 'o2' else 0
    else:
        keep = max(range(len(counts)), key = counts.__getitem__) if element == 'o2' else min(range(len(counts)), key = counts.__getitem__)
    new_list = [x.strip() for x in binlist if int(x[i]) == keep]
    if len(new_list) > 1:
        return get_rating(new_list, element, i=i+1)
    else:
        return int(new_list[0], 2)

print(get_rating(input, 'o2') * get_rating(input, 'co2'))

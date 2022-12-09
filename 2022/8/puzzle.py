#!/usr/bin/env python3

import numpy

example = """
30373
25512
65332
33549
35390
"""

with open('input.txt') as f:
    rows = [row.strip() for row in f.readlines()]

columns = [''] * len(rows[1])

for i in range(len(rows[1])): # assumes all same
    for row in rows:
        columns[i] = columns[i] + row[i]

# part_one
visible = 0
for row_idx, row in enumerate(rows):
    # outer rows are fully visible
    if row_idx == 0 or row_idx == len(rows)-1:
        visible += len(row)
        continue
    # inner rows
    for tree_idx, tree in enumerate(row):
        # outer columns are visible (but don't count the ones we've already counted)
        if (tree_idx == 0 or tree_idx == len(row)-1) and row_idx not in [0, len(rows)-1]:
            visible += 1
            continue
        left = row[:tree_idx]
        right = row[tree_idx+1:]
        above = columns[tree_idx][:row_idx]
        below = columns[tree_idx][row_idx+1:]
        if int(tree) > max([int(x) for x in left]) or int(tree) > max([int(x) for x in right]):
            visible += 1
            continue
        if int(tree) > max([int(x) for x in above]) or int(tree) > max([int(x) for x in below]):
            visible += 1
            continue

print(visible)

# part_two

def am_i_tallest(tree, direction):
    if int(tree) > max([int(x) for x in direction]):
        return True
    return False

def count_friends(tree, direction):
    score = 0
    for friend in direction:
        if int(tree) > int(friend):
            score += 1
        else:
            # we add to the score for the tree that blocked us
            score += 1
            break
    return score

max_score = 0
tree_scores = []

for row_idx, row in enumerate(rows):
    # anything on an outer row will have a score of 0
    if row_idx == 0 or row_idx == len(rows)-1:
        continue
    # inner rows
    for tree_idx, tree in enumerate(row):
        # outer columns also will have a score of 0
        if (tree_idx == 0 or tree_idx == len(row)-1):
            continue
        left = ''.join(list(reversed(row[:tree_idx])))
        right = row[tree_idx+1:]
        above = ''.join(list(reversed(columns[tree_idx][:row_idx])))
        below = columns[tree_idx][row_idx+1:]

        directions_and_scores = {left: 0, right: 0, above: 0, below: 0}

        for direction in directions_and_scores:
            if am_i_tallest(tree, direction):
                directions_and_scores[direction] = len(direction)
            else:
                directions_and_scores[direction] = count_friends(tree, direction)

        tree_score = numpy.prod(list(directions_and_scores.values()))
        if tree_score > max_score:
            max_score = tree_score

print(max_score)

#!/usr/bin/env python3

import numpy

def prep_input():
    with open('input.txt') as f:
        rows = [row.strip() for row in f.readlines()]

    columns = [''] * len(rows[1])

    for i in range(len(rows[1])): # assumes all same
        for row in rows:
            columns[i] = columns[i] + row[i]

    return rows, columns

def get_directions(row, column, row_idx, tree_idx):
    left = row[:tree_idx]
    right = row[tree_idx+1:]
    above = column[:row_idx]
    below = column[row_idx+1:]
    return (left, right, above, below)

def part_one(rows, columns):
    visible = 0
    for row_idx, row in enumerate(rows):
        # outer rows are fully visible
        if row_idx == 0 or row_idx == len(rows)-1:
            visible += len(row)
            continue
        # inner rows
        for tree_idx, tree in enumerate(row):
            # outer columns are visible
            if tree_idx == 0 or tree_idx == len(row)-1:
                visible += 1
                continue
            left, right, above, below = get_directions(row, columns[tree_idx], row_idx, tree_idx)
            if int(tree) > max([int(x) for x in left]) or int(tree) > max([int(x) for x in right]):
                visible += 1
                continue
            if int(tree) > max([int(x) for x in above]) or int(tree) > max([int(x) for x in below]):
                visible += 1
                continue

    return visible # 1840

def part_two(rows, columns):
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

    for row_idx, row in enumerate(rows):
        # anything on an outer row will have a score of 0
        if row_idx == 0 or row_idx == len(rows)-1:
            continue
        # inner rows
        for tree_idx, tree in enumerate(row):
            # outer columns also will have a score of 0
            if (tree_idx == 0 or tree_idx == len(row)-1):
                continue
            left, right, above, below = get_directions(row, columns[tree_idx], row_idx, tree_idx)
            left = ''.join(list(reversed(left)))
            above = ''.join(list(reversed(above)))

            directions_and_scores = {left: 0, right: 0, above: 0, below: 0}

            for direction in directions_and_scores:
                if am_i_tallest(tree, direction):
                    directions_and_scores[direction] = len(direction)
                else:
                    directions_and_scores[direction] = count_friends(tree, direction)

            tree_score = numpy.prod(list(directions_and_scores.values()))
            if tree_score > max_score:
                max_score = tree_score

    return max_score # 405769

if __name__ == "__main__":
    rows, columns = prep_input()
    print(part_one(rows, columns))
    print(part_two(rows, columns))

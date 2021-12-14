#!/usr/bin/env python3

data = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0
"""

folds = """
y=7
x=5
"""

data = open('13.input', 'r').read()
folds = open('13.folds', 'r').read()

data, folds = data.split("\n"), folds.split("\n")

width = max(list(map(int, [i.split(',')[0] for i in data if i != ''])))
height = max(list(map(int, [i.split(',')[1] for i in data if i != ''])))

grid = {}
[grid.setdefault(y, []) for y in range(height + 1)]

for point in data:
    if point != '':
        x, y = point.split(',')
        grid[int(y)] = grid.get(int(y), [])
        grid[int(y)].append(int(x))

def y_fold(grid, foldline, height): # horizonal fold upwards
    for i in range(1, foldline+1):
        try:
            grid[foldline - i] = list(set(grid[foldline - i] + grid[foldline + i]))
            grid[foldline + i] = []
        except KeyError:
            break
    height = height - foldline
    return grid, height

def x_fold(grid, foldline, width):
    for line in grid:
        for i, x in enumerate(grid[line]):
            if x > foldline:
                grid[line][i] = width - x
        grid[line] = list(set(grid[line]))
        output_line = ['.' for x in range(width + 1)]
    width = width - foldline
    return grid, width

for fold in folds:
    if fold != '':
        fold_direction, foldline = fold.split('=')
        foldline = int(foldline)
        if fold_direction == 'x':
            grid, width = x_fold(grid, foldline, width)
        else:
            grid, height = y_fold(grid, foldline, height)

        visible_points = 0
        for i in grid.values():
            visible_points += len(i)
        print(f"Visible points after this fold: {visible_points}")

#for line in grid.values():
#    if len(line) > 0:
#        final_line = ['.' for i in range(width)]
#        for x in line:
#            final_line[x] = '#'
#        print(''.join(final_line))

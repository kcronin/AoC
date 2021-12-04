#!/usr/bin/env python3

treemap = open('3.1.input', 'r').readlines()

def gettrees(x, y):
    startingpoint = 0
    trees = 0
    i = 0
    while i < len(treemap) - y:
        startingpoint += x
        if startingpoint >= len(treemap[i+y].strip()):
            startingpoint = startingpoint - len(treemap[i+y].strip())
        if treemap[i+y][startingpoint] == '#':
#            printme = treemap[i+y].strip()[:startingpoint] + 'X' + treemap[i+y].strip()[startingpoint + 1:]
            trees += 1
#        else:
#            printme = treemap[i+y].strip()[:startingpoint] + 'O' + treemap[i+y].strip()[startingpoint + 1:]
#        print(printme)
        i += y
    return trees

a = gettrees(1, 1)
b = gettrees(3, 1)
c = gettrees(5, 1)
d = gettrees(7, 1)
e = gettrees(1, 2)

print(f"Got {a} * {b} * {c} * {d} * {e} = {a*b*c*d*e}") 

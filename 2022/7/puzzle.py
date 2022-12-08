#!/usr/bin/env python3

import re
import gc

with open('input.txt') as f:
    terminal = f.read()

# look ma, a recursive function!
def increase_size(dirobj, size):
    dirobj.size += size
    if dirobj.parent:
        increase_size(dirobj.parent, size)

class Directory():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

root = Directory('root')

for line in terminal.split("\n"):
    if line:
        if line.startswith('$ cd'):
            if line.split()[2] == '/':
                cwd = root
            elif line.split()[2] == '..':
                cwd = cwd.parent
            else:
                child = Directory(line.split()[2], parent=cwd)
                cwd.children.append(child)
                cwd = child
        if re.match(r"^\d+", line):
            increase_size(cwd, int(line.split()[0]))

total = 0
for obj in gc.get_objects():
    if isinstance(obj, Directory):
        if obj.size <= 100000:
            total += obj.size

# part one
print(total)

total_disk = 70000000
space_needed = 30000000
unused_space = total_disk - root.size
need_to_free = space_needed - unused_space

candidate_size = total_disk # something known to be larger than largest dir size
for obj in gc.get_objects():
    if isinstance(obj, Directory):
        if obj.size >= need_to_free and obj.size < candidate_size:
            candidate_size = obj.size

# part two
print(candidate_size)


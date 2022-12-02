#!/usr/bin/env python3

santa_location = (0, 0)
robo_location = santa_location
delivered = {santa_location, robo_location}

def move(direction, current):
    match direction:
        case '^':
            return (current[0], current[1]+1)
        case '<':
            return (current[0]-1, current[1])
        case 'v':
            return (current[0], current[1]-1)
        case '>':
            return (current[0]+1, current[1])

with open('input.txt', 'r') as f:
    directions = f.read().strip()
    for index, d in enumerate(directions):
        if index % 2 == 0: # move santa
            santa_location = move(d, santa_location)
            delivered.add(santa_location)
        else: # move robo
            robo_location = move(d, robo_location)
            delivered.add(robo_location)

print(len(delivered))





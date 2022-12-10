#!/usr/bin/env python3

import math

example = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
#moves = [line for line in example.split("\n") if line]
with open('input.txt') as f:
    moves = f.readlines()

class Knot():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visited = [f"{self.x},{self.y}"]

def sign(num):
    return int(math.copysign(1, num)) if num != 0 else 0

def move_knots(knots):
    for knot_idx, knot in enumerate(knots):
        if knot_idx > 0: # 0 is the head
            # need to figure out where previous knot is and how to move to follow it
            previous = knots[knot_idx-1]
            x_diff, y_diff = previous.x - knot.x, previous.y - knot.y
            if abs(x_diff) > 1 or abs(y_diff) > 1:
                knot.x += sign(x_diff)
                knot.y += sign(y_diff)

            knot.visited.append(f"{knot.x},{knot.y}")

def main(knots):
    head = knots[0]
    tail = knots[-1]
    for move in moves:
        direction, distance = move.split()
        for i in range(int(distance)):

            match direction:
                case 'R':
                    head.x += 1
                    #print(f"head is now at {head.x},{head.y}")
                case 'L':
                    head.x -= 1
                case 'U':
                    head.y += 1
                case 'D':
                    head.y -= 1

            move_knots(knots)
    return len(set(tail.visited))

if __name__ == "__main__":
    # part 1
    knots = [Knot() for _ in range(2)]
    print(main(knots)) # 6563

    # part 2
    knots = [Knot() for _ in range(10)]
    print(main(knots)) # 2653

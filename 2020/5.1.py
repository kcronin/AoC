#!/usr/bin/env python3

seats = open('5.1.input', 'r').readlines()

# we already know that the highest seat id will be in the back of the plane,
# so we can disregard any seats that start with F.

max = 0

def splitrange(r, dir):
    halfway = int(len(r)/2)
    if dir in ['F', 'L']:
        return r[:halfway]
    else:
        return r[halfway:]

for seat in seats:
    if seat[0] == 'B':
        rowrange = range(64, 128)
        seatrange = range(0, 8)
        for i in range(1, 7):
            rowrange = splitrange(rowrange, seat[i])
        row = rowrange[0]
        for i in range(7, 10):
            seatrange = splitrange(seatrange, seat[i])
        seat = seatrange[0]

        seatid = row * 8 + seat
        if seatid > max:
            max = seatid

print(max)

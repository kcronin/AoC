#!/usr/bin/env python3

seats = open('5.1.input', 'r').readlines()

def splitrange(r, dir):
    halfway = int(len(r)/2)
    if dir in ['F', 'L']:
        return r[:halfway]
    else:
        return r[halfway:]

seatids = []

for seat in seats:
    rowrange = range(0, 128)
    seatrange = range(0, 8)
    for i in range(0, 7):
        rowrange = splitrange(rowrange, seat[i])
    row = rowrange[0]
    for i in range(7, 10):
        seatrange = splitrange(seatrange, seat[i])
    seat = seatrange[0]

    seatid = row * 8 + seat
    seatids.append(seatid)

seatids.sort()
print(seatids)
myseat = [s for s in range(seatids[0], seatids[-1]+1) if s not in seatids]
print(myseat)

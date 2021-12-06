#!/usr/bin/env python3
import copy

#data = "3,4,3,1,2"

data = open('6.input', 'r').read()

data = list(map(int, data.split(",")))

fishtimers = {}
[fishtimers.setdefault(x, 0) for x in range(9)]
for x in data:
    fishtimers[x] += 1

#print(f"initial state: {fishtimers}")

def getfish(days, fishtimers):
    for i in range(days):
        tempdict = {}
        [tempdict.setdefault(x, 0) for x in range(9)]
        for x in range(8):
            tempdict[x] = fishtimers[x+1]
        tempdict[6] += fishtimers[0]
        tempdict[8] = fishtimers[0]
        fishtimers = copy.deepcopy(tempdict)
        #print(f"After {i} day(s): {fishtimers}")
    return (sum(fishtimers.values()))

print(f"Part one: {getfish(80, fishtimers)}")
print(f"Part two: {getfish(256, fishtimers)}")

#!/usr/bin/env python3

data = "3,4,3,1,2"

#data = open('6.input', 'r').read()

# decrement each element in list by one each day.
# if any increment is 0, append an 8 to the list, then repeat.
# once an 8 counts down to zero, restart it at 6.
# repeat for 80 days.

fishtimers = data.split(",")
fishtimers = list(map(int, fishtimers))
print(fishtimers)

def spawn(yesterday):
    return [8 for x in yesterday if x == 0]

yesterday = fishtimers

i = 1
while i <= 256:
    fishtimers = [x - 1 if x > 0 else 6 for x in fishtimers]
    # do we need to spawn? (any 0s from yesterday?)
    fishtimers += spawn(yesterday)
    yesterday = fishtimers
    print(f"After {i} day(s): {fishtimers}")
    i += 1

print(len(fishtimers))

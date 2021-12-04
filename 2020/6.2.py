#!/usr/bin/env python3

import collections

f = open('6.input', 'r').read()

answers = f.split('\n\n')

total_yesses = 0

for answer in answers:
    num_in_group = len(answer.strip().split("\n"))
    group_responses = collections.Counter(answer.replace("\n", ""))
    num_what_said_yes = len([k for k,v in group_responses.items() if v == num_in_group])
    total_yesses += num_what_said_yes

print(total_yesses)

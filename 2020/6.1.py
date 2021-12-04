#!/usr/bin/env python3

f = open('6.input', 'r').read()

answers = f.split('\n\n')
print(answers)

total_yesses = 0
for answer in answers:
    answer = answer.replace("\n", '')
    print(answer)
    total_yesses += len(set(answer))
print(total_yesses)

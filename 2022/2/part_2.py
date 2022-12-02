#!/usr/bin/env python3

elf = {'A': 'rock',
       'B': 'paper',
       'C': 'scissors'}

outcomes = {'X': 'lose',
      'Y': 'draw',
      'Z': 'win'}

hierarchy = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}

scores = {'rock': 1,
          'paper': 2,
          'scissors': 3,
          'win': 6,
          'draw': 3}

with open('input.txt', 'r') as f:
    rounds = f.readlines()

total_score = 0
for r in rounds:
    round_score = 0
    e, o = r.strip().split()
    if outcomes[o] == 'draw':
        round_score = scores[elf[e]] + scores['draw']
    elif outcomes[o] == 'lose':
        round_score = scores[hierarchy[elf[e]]]
    else:
        my_play = [p for p in hierarchy if hierarchy[p] == elf[e]]
        round_score = scores[my_play[0]] + scores['win']
    total_score += round_score

print(total_score)

#!/usr/bin/env python3

elf = {'A': 'rock',
       'B': 'paper',
       'C': 'scissors'}

me = {'X': 'rock',
      'Y': 'paper',
      'Z': 'scissors'}

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
    e, m = r.strip().split()
    #print(f"elf: {e} ({elf[e]}), me: {m} ({me[m]})")
    if elf[e] == me[m]: # draw
        #print("draw!")
        round_score = scores['draw'] + scores[me[m]]
    elif hierarchy[elf[e]] == me[m]: # elf wins
        #print("elf wins!")
        round_score = scores[me[m]]
    else: # i win
        #print("i win!")
        round_score = scores[me[m]] + scores['win']
    total_score += round_score

print(total_score)

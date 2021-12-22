#!/usr/bin/env python3

class Player:
    def __init__(self, starting_pos):
        self.position = starting_pos
        self.score = 0
        self.num_rolls = 3

    def roll(self, die_pos):
        roll_total = 0
        for i in range(1, self.num_rolls+1):
            die_pos = self.get_next_roll(die_pos)
            roll_total += die_pos
        self.position = (self.position + roll_total) - 10 * int((self.position + roll_total) / 10)
        if self.position == 0:
            self.position = 10
        self.score += self.position
        return self.position, self.score, die_pos

    def get_next_roll(self, num):
        if num < 100:
            die_pos = num + 1
        else:
            die_pos = 1
        return die_pos

total_rolls = 0
die_pos = 0

player1 = Player(5)
player2 = Player(8)

player1_score, player2_score = (0,0)

while True:
    player1_pos, player1_score, die_pos = player1.roll(die_pos)
    total_rolls += 3
    if player1_score >= 1000:
        print("player1 wins!")
        break
    player2_pos, player2_score, die_pos = player2.roll(die_pos)
    total_rolls += 3
    if player2_score >= 1000:
        print("player2 wins!")
        break

low_score = player1_score if player1_score < player2_score else player2_score
print(f"total rolls: {total_rolls}; low score: {low_score}; answer: {low_score * total_rolls}")

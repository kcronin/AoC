#!/usr/bin/env python3

data = open('4.input', 'r').read().split("\n\n")
numbers = open('4.numbers', 'r').read().split(',')

example = """
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

example_numbers = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"

#data = example.split("\n\n")
#numbers = example_numbers.split(',')

class Board:
    def __init__(self, board_number, rows):
        self.board_number = board_number
        self.rows = [row.strip().split() for row in rows.split("\n") if len(row) > 0]
        for i, row in enumerate(self.rows):
            row = [int(x) for x in row]
            self.rows[i] = row
        self.columns = [list(r) for r in zip(*self.rows)]

    def check_rows_and_columns(self, number):
        for r, row in enumerate(self.rows):
            for i, num in enumerate(row):
                if int(number) == num:
                    self.rows[r][i] = 'B'
                    self.columns[i][r] = 'B'

    def total_remaining(self):
        total_remaining = 0
        for row in self.rows:
            total_remaining += sum([x for x in row if type(x) is int])
        return total_remaining

    def check_board(self, number):
        # any rows or columns bingoed?
        for row_or_column in self.rows + self.columns:
            if row_or_column.count('B') == len(row_or_column): # bingo!
                #print(f"BINGO! Board {self.board_number} bingoed with number {number}")
                return self.total_remaining()
        return False

bingo = False

boards = []

for i, board in enumerate(data):
    boards.append(Board(i, board))

def part_one(boards, numbers):
	for i, number in enumerate(numbers):
		for board in boards:
			board.check_rows_and_columns(int(number))
			if i >= 4:
				bingo = board.check_board(int(number))
				if bingo:
					#print("woohoo! stopping. Got total_remaining: ", bingo)
					return bingo * int(number)

def part_two(boards, numbers):
    num_moves, score = 0, 0

    for board in boards:
        for i, number in enumerate(numbers, 1):
            board.check_rows_and_columns(int(number))
            if i > 4:
                bingo = board.check_board(int(number))
                if bingo:
                    if i > num_moves:
                        num_moves = i
                        score = bingo * int(number)
                    break
    return score

print(f"Part one: {part_one(boards, numbers)}")
print(f"Part two: {part_two(boards, numbers)}")

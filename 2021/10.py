#!/usr/bin/env python3

import statistics

data = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

data = open('10.input', 'r').read()

delimiters = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
        }

corrupt_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }

autocomplete_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
        }

corrupt_score = 0

autocompleted = []

for line in data.split('\n'):
    if len(line) > 0:
        chunks = []
        corrupt = False
        for char in line:
            if char in delimiters: # opener
                chunks.append(char)
            else: # closer
                if delimiters[chunks.pop()] != char: # corrupted
                    corrupt_score += corrupt_scores[char]
                    corrupt = True
        if corrupt == False and len(chunks) > 0: # we have unclosed chunks
            autocomplete_score = 0
            completed = ''
            for opener in reversed(chunks):
                completed += delimiters[opener]
                autocomplete_score = autocomplete_score * 5 + autocomplete_scores[delimiters[opener]]
            autocompleted.append(autocomplete_score)


print(f"Part one: {corrupt_score}")
autocompleted.sort()
print(f"Part two: {int(statistics.median(autocompleted))}")



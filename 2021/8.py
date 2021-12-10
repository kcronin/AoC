#!/usr/bin/env python3

# 0 = 6
# 1 = 2 *
# 2 = 5
# 3 = 5
# 4 = 4 *
# 5 = 5
# 6 = 6
# 7 = 3 *
# 8 = 7 *
# 9 = 6

# 1 (2), 4 (4), 7 (3) , 8 (7) are unique

data = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

data = open('8.input', 'r').readlines()

total_unique = 0

for line in data:
    print(line)
    if len(line) > 0:
        digits = line.split('|')[1].split()
        for d in digits:
            if len(d) in [2, 4, 3, 7]:
                total_unique += 1

print(total_unique)

digit_codes = [
    'abcefg', # 0 len(6)
    'cf',     # 1 len(2)
    'acdeg',  # 2 len(5) 
    'acdfg',  # 3 len(5)
    'bcdf',   # 4 len(4)
    'abdfg',  # 5 len(5)
    'abdefg', # 6 len(6)
    'acf',    # 7 len(3)
    'abcdefg',# 8 len(7)
    'abcdfg', # 9 len(6)
    ]

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb  cefbgd gcbe
   1       8      9      6    4     5      0     3     2   7         8     3       9    4

# first, check if right-hand of | is known-unique numbers (1, 4, 8, 7), if so, continue
# first, find easy targets (1, 4, 7, 8) on both sides
# then move onto len5s on left hand side, for each one discovered, check against len5s on right side
# same w/ len6s until all numbers accounted for

unique_digits = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
    }

total = 0

for line in data:
    result = {}
    left_side, right_side = line.split(' | ')
    for i, digit in enumerate(right_side.split()):
        if len(digit.strip()) in unique_digits:
            result[i] = unique_digits[len(digit.strip())]
    if len(result) == 4:
        total += int(''.join(result.values()))
        continue
    else:
        deciphered = {}
        for i, digit in enumerate(left_side.split()):
            if len(digit.strip()) in unique_digits:
                deciphered[i] = digit.strip()
            elif len(digit.strip()) == 5:
                possibilities_5 = [2,3,5]
                # do we contain a 1?
                if digit.strip().find(deciphered[1][0]


        possibilities_5 = [2, 3, 5]




# cefdb can only be 3 because of the three posibilities, it is the only one with b and e
# cefbgd has be, so can only be 0 or 9
# can't be zero because it shares all letters with 4, so 9
# fdcge (len5) could be 2, 3 or 5
# doesn't have be so can't be 3
# closest known with all same letters is 9, so 5
# so now we know the remaining 5-letter combo is 2
# fgaecd (len 6) remaining options are 0 and 6
# do we have be? no - cannot be 0, must be 6






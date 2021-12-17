#!/usr/bin/env python3

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

data = open('8.input', 'r').read()

total_unique = 0

for line in data.split("\n"):
    if len(line) > 0:
        digits = line.split(' | ')[1].split()
        for d in digits:
            if len(d) in [2, 4, 3, 7]:
                total_unique += 1

print(f"Part one: {total_unique}")

total = 0

for line in data.split("\n"):
    result = []
    if len(line) > 0:
        left_side, right_side = line.split(' | ')
        for digit in left_side.split():
            if len(digit) == 2:
                one = set(digit)
            elif len(digit) == 4:
                four = set(digit)

        for digit in right_side.split():
            if len(digit) == 2:
                num = 1
            elif len(digit) == 3:
                num = 7
            elif len(digit) == 4:
                num = 4
            elif len(digit) == 5:
                if len(one & set(digit)) == 2:
                    num = 3
                elif len(four & set(digit)) == 2:
                    num = 2
                else:
                    num = 5
            elif len(digit) == 6:
                if len(one & set(digit)) == 1:
                    num = 6
                elif len(four & set(digit)) == 4:
                    num = 9
                else:
                    num = 0
            else:
                num = 8

            result.append(num)
        total += int(''.join(map(str, result)))

print(f"Part two: {total}")

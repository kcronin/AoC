#!/usr/bin/env python3

from copy import deepcopy

data = """
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

template = "NNCB"

data = open('14.input', 'r').read()
template = "BCHCKFFHSKPBSNVVKVSK"

class Polymer:
    def __init__(self, template, steps, rules):
        self.template = template
        self.steps = steps
        self.rules = {}

        for rule in rules.split("\n"):
            if rule != "":
                self.rules[rule.split(" -> ")[0]] = rule.split(" -> ")[1]

    def generate(self):
        pair_counts = {}
        for pair in self.rules:
            pair_counts[pair] = self.template.count(pair)

        for i in range(self.steps):
            result = deepcopy(pair_counts)
            for pair, count in pair_counts.items():
                result[pair] -= count
                result[pair[0] + self.rules[pair]] += count
                result[self.rules[pair] + pair[1]] += count
            pair_counts = result

        counts = {}
        for pair in pair_counts:
            counts[pair[0]] = counts.get(pair[0], 0) + pair_counts[pair]
        counts[self.template[-1]] += 1

        return max(counts.values())-min(counts.values())

print(f"Part one: {Polymer(template, 10, data).generate()}") # 2797
print(f"Part two: {Polymer(template, 40, data).generate()}") # 2926813379532

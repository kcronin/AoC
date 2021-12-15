#!/usr/bin/env python3

#data = """
#CH -> B
#HH -> N
#CB -> H
#NH -> C
#HB -> C
#HC -> B
#HN -> C
#NN -> C
#BH -> H
#NC -> B
#NB -> B
#BN -> B
#BB -> N
#BC -> B
#CC -> N
#CN -> C
#"""
#
#template = "NNCB"

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

    def step(self, step_no):
        result = ''

        for i in range(len(self.template)):
            pair = self.template[i:i+2]
            if pair in self.rules:
                result = result + self.template[i] + self.rules[pair]
            else:
                result += pair
            if i == len(self.template):
                result += self.template[-1]

        self.template = result

        #print(f"Step {step_no}: length {len(self.template)}, result: {self.template}")

    def generate(self):
        for i in range(1, self.steps+1):
            self.step(i)
        return self.template

polymer = Polymer(template, 40, data)
result = polymer.generate()
counts = {}

for char in result:
    counts[char] = result.count(char)
#print(counts)
print(max(counts.values())-min(counts.values()))

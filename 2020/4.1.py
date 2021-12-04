#!/usr/bin/env python3

import re

f = open('4.1.input', 'r').read()

valid = 0

regex_map = {
        "byr": r"^(19[2-9][0-9]|200[0-2])$",
        "iyr": r"^20(1[0-9]|20)$",
        "eyr": r"^20(2[0-9]|30)$",
        "hgt": r"^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth){1}$",
        "pid": r"^[0-9]{9}$"
        }

for passport_string in f.split('\n\n'):
    passport = {}
    passport_string = passport_string.replace('\n', ' ')
    for item in passport_string.split():
        passport[item.split(':')[0]] = item.split(':')[1]
    print(passport)
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport.keys()):
        # potentially valid
        matches = 0
        for key in regex_map.keys():
            m = re.match(regex_map[key], passport[key])
            if m:
                matches += 1
            else:
                print(f"Got invalid {key}: {passport[key]}")
                break
        if matches == 7:
            valid += 1

print(valid)
